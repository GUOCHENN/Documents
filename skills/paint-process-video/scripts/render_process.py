"""Render an explicitly simulated drawing process from a static image.

Requires numpy, opencv-python-headless, and FFmpeg/FFprobe on PATH.
The animation infers contours; it does not recover an artist's real strokes.
"""
import argparse
from pathlib import Path
import json
import math
import shutil
import subprocess
import sys
import numpy as np
import cv2

def dimensions(width, height, longest):
    if width >= height:
        return longest, max(2, round(height * longest / width / 2) * 2)
    return max(2, round(width * longest / height / 2) * 2), longest

def make_subject(rgb, mask_path=None):
    h,w=rgb.shape[:2]
    if mask_path:
        mask=cv2.imread(str(mask_path),cv2.IMREAD_GRAYSCALE)
        if mask is None: raise ValueError('Cannot read foreground mask')
        return (cv2.resize(mask,(w,h),interpolation=cv2.INTER_NEAREST)>127).astype(np.uint8)
    if min(w,h)<64: raise ValueError('Input too small for automatic masking')
    grab=np.zeros((h,w),np.uint8)
    rectangle=(round(w*.04),round(h*.07),round(w*.92),round(h*.87))
    cv2.grabCut(cv2.cvtColor(rgb,cv2.COLOR_RGB2BGR),grab,rectangle,np.zeros((1,65),np.float64),np.zeros((1,65),np.float64),4,cv2.GC_INIT_WITH_RECT)
    mask=np.isin(grab,[cv2.GC_FGD,cv2.GC_PR_FGD]).astype(np.uint8)
    mask=cv2.morphologyEx(mask,cv2.MORPH_CLOSE,np.ones((5,5),np.uint8))
    if not .015<float(mask.mean())<.92:
        raise ValueError('Automatic foreground mask is unreliable; supply --foreground-mask')
    return mask

def ordered_strokes(rgb,mask,max_strokes):
    gray=cv2.cvtColor(rgb,cv2.COLOR_RGB2GRAY)
    gray=cv2.bilateralFilter(gray,7,40,40)
    edges=cv2.Canny(gray,45,105)
    edges[mask==0]=0
    contours,_=cv2.findContours(edges,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
    contours=[cv2.approxPolyDP(c,1.1,False).reshape(-1,2) for c in contours if cv2.arcLength(c,False)>30]
    contours=sorted((c for c in contours if len(c)>3),key=lambda c:-cv2.arcLength(c.astype(np.int32),False))[:max_strokes]
    if not contours: raise ValueError('No useful contours found')
    paths=[]
    current=np.array([rgb.shape[1]*.5,rgb.shape[0]*.15])
    while contours:
        index=min(range(len(contours)),key=lambda i:min(np.linalg.norm(contours[i][0]-current),np.linalg.norm(contours[i][-1]-current)))
        contour=contours.pop(index)
        if np.linalg.norm(contour[-1]-current)<np.linalg.norm(contour[0]-current): contour=contour[::-1]
        if paths:
            # Lift the tip while travelling continuously between disconnected contours.
            count=max(2,int(np.linalg.norm(contour[0]-current)/6))
            paths.extend((p,False) for p in np.linspace(current,contour[0],count))
        paths.append((contour[0].astype(float),False))
        for a,b in zip(contour[:-1],contour[1:]):
            count=max(1,int(np.linalg.norm(b-a)/2))
            paths.extend((p,True) for p in np.linspace(a,b,count+1)[1:])
        current=contour[-1]
    return paths

def draw_pencil(frame,tip):
    x,y=map(float,tip)
    u=np.array([.55,-.835],float)
    v=np.array([.835,.55],float)
    tip=np.array([x,y])
    body=np.array([tip+u*12+v*4,tip+u*83+v*4,tip+u*83-v*4,tip+u*12-v*4],np.int32)
    nib=np.array([tip,tip+u*15+v*4,tip+u*15-v*4],np.int32)
    cv2.fillConvexPoly(frame,body,(65,68,70),cv2.LINE_AA)
    cv2.fillConvexPoly(frame,nib,(188,151,105),cv2.LINE_AA)
    cv2.line(frame,tuple(tip.astype(int)),tuple((tip+u*5).astype(int)),(35,35,35),2,cv2.LINE_AA)

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input',required=True,type=Path)
    parser.add_argument('--out',required=True,type=Path)
    parser.add_argument('--foreground-mask',type=Path)
    parser.add_argument('--long-edge',type=int,default=3840)
    parser.add_argument('--fps',type=int,default=60)
    parser.add_argument('--duration',type=float,default=16)
    parser.add_argument('--work-long-edge',type=int,default=1024)
    parser.add_argument('--max-strokes',type=int,default=120)
    args=parser.parse_args()
    if not shutil.which('ffmpeg') or not shutil.which('ffprobe'): raise RuntimeError('FFmpeg and FFprobe are required')
    if args.fps<1 or args.long_edge<64 or args.long_edge%2 or args.duration<5: raise ValueError('Use an even long edge, positive fps and duration >= 5 seconds')
    if args.out.exists(): raise FileExistsError('Output already exists; use a new filename')
    original=cv2.imdecode(np.fromfile(args.input,dtype=np.uint8),cv2.IMREAD_COLOR)
    if original is None: raise ValueError('Cannot read input image')
    oh,ow=original.shape[:2]
    w,h=dimensions(ow,oh,args.work_long_edge)
    tw,th=dimensions(ow,oh,args.long_edge)
    rgb=cv2.cvtColor(cv2.resize(original,(w,h),interpolation=cv2.INTER_AREA),cv2.COLOR_BGR2RGB)
    mask=make_subject(rgb,args.foreground_mask)
    paths=ordered_strokes(rgb,mask,args.max_strokes)
    args.out.parent.mkdir(parents=True,exist_ok=True)
    evidence=args.out.parent/(args.out.stem+'-evidence')
    evidence.mkdir(exist_ok=True)
    cv2.imwrite(str(evidence/'foreground-mask.png'),mask*255)
    inside=cv2.distanceTransform(mask,cv2.DIST_L2,5)
    outside=cv2.distanceTransform(1-mask,cv2.DIST_L2,5)
    rank_subject=inside/max(1.,float(inside.max()))
    rank_background=1-outside/max(1.,float(outside.max()))
    smooth=cv2.bilateralFilter(rgb,9,50,50).astype(np.float32)
    target=rgb.astype(np.float32)
    sketch=np.full_like(rgb,255)
    total=round(args.duration*args.fps)
    sketch_end=args.duration*.40
    subject_end=args.duration*.75
    background_end=args.duration*.90
    snapshots={round(args.fps*sketch_end*.65):'01-trazo.jpg',round(args.fps*sketch_end):'02-lineas.jpg',round(args.fps*subject_end):'03-sujeto.jpg',total-1:'04-final.jpg'}
    command=['ffmpeg','-hide_banner','-loglevel','error','-y','-f','rawvideo','-pix_fmt','rgb24','-s',f'{w}x{h}','-r',str(args.fps),'-i','-','-an','-vf',f'scale={tw}:{th}:flags=lanczos','-c:v','libx264','-preset','ultrafast','-crf','21','-threads','4','-pix_fmt','yuv420p','-movflags','+faststart','-r',str(args.fps),str(args.out)]
    log_path=evidence/'encoder.log'
    last=0
    with log_path.open('wb') as log:
        encoder=subprocess.Popen(command,stdin=subprocess.PIPE,stderr=log)
        try:
            for i in range(total):
                time=i/args.fps
                if time<=sketch_end:
                    upto=min(len(paths)-1,int(time/sketch_end*(len(paths)-1)))
                    for j in range(max(1,last),upto+1):
                        if paths[j][1]: cv2.line(sketch,tuple(np.rint(paths[j-1][0]).astype(int)),tuple(np.rint(paths[j][0]).astype(int)),(65,65,65),1,cv2.LINE_AA)
                    last=upto+1
                    frame=sketch.copy()
                    draw_pencil(frame,paths[upto][0])
                elif time<=subject_end:
                    p=(time-sketch_end)/(subject_end-sketch_end)
                    alpha=np.clip((p*1.09-rank_subject)/.09,0,1)*mask
                    detail=np.clip((p-.65)/.35,0,1)
                    color=smooth*(1-detail)+target*detail
                    frame=np.rint(sketch*(1-alpha[...,None])+color*alpha[...,None]).astype(np.uint8)
                elif time<=background_end:
                    p=(time-subject_end)/(background_end-subject_end)
                    alpha=np.clip((p*1.09-rank_background)/.09,0,1)*(1-mask)+mask
                    frame=np.rint(sketch*(1-alpha[...,None])+target*alpha[...,None]).astype(np.uint8)
                else:
                    frame=rgb
                if i in snapshots:
                    cv2.imwrite(str(evidence/snapshots[i]),cv2.cvtColor(frame,cv2.COLOR_RGB2BGR),[cv2.IMWRITE_JPEG_QUALITY,93])
                encoder.stdin.write(np.ascontiguousarray(frame).tobytes())
                if i%max(1,args.fps*2)==0: print(f'Rendered {i}/{total} frames',flush=True)
        finally:
            encoder.stdin.close()
        code=encoder.wait()
    if code: raise RuntimeError(f'FFmpeg failed ({code}); see {log_path}')
    info=json.loads(subprocess.check_output(['ffprobe','-v','error','-select_streams','v:0','-show_entries','stream=codec_name,width,height,avg_frame_rate,pix_fmt,nb_frames:format=duration','-of','json',str(args.out)],text=True))
    stream=info['streams'][0]
    assert stream['codec_name']=='h264' and stream['pix_fmt']=='yuv420p'
    assert (stream['width'],stream['height'])==(tw,th)
    numerator,denominator=map(int,stream['avg_frame_rate'].split('/'))
    assert numerator/denominator==args.fps
    assert int(stream['nb_frames'])==total
    assert abs(tw/th-ow/oh)<.002
    info['simulation']=True
    info['input_size']=[ow,oh]
    info['render_working_size']=[w,h]
    info['upscaled']=args.long_edge>max(ow,oh)
    info['stage_seconds']={'sketch_end':sketch_end,'subject_end':subject_end,'background_end':background_end,'total':args.duration}
    info['notes']='Inferred contour animation and simulated color reveal, not an artist recording. Color stage has no pencil or hand. Final image preserves source proportions; encoded resolution does not add source detail.'
    (args.out.with_suffix('.json')).write_text(json.dumps(info,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps(info,ensure_ascii=False),flush=True)

if __name__=='__main__': main()
