# 实际生成提示词

以下为本次内置图像生成工具实际使用的完整提示词。参考素材的位置以技能根目录的相对路径表示；调用时解析为实际文件路径。工具为内置 image_gen，未使用 CLI 或外部 API。

## A｜回响 · 海报构图

参考输入：references/images/01-schmidt-1923.jpg

```text
Use case: stylized-concept
Asset type: original contemporary exhibition poster; skill evaluation A, diagonal graphic construction.
Input image: the attached Joost Schmidt 1923 Bauhaus exhibition poster is a STYLE REFERENCE ONLY. Learn the red/black/gray on cream print palette, assertive diagonal composition, interlocked geometric mass, and lettering integrated with forms. Do not recreate its recognizable head/profile, cross-shaped arrangement, historical lettering, dates, signature, or exact layout.
Primary request: design a new portrait 3:4 poster about sound and physical force, titled "回响". A bold C-shaped red acoustic ring in the lower left interlocks with two offset charcoal rectangular masses rising toward upper right. One long diagonal red beam links the construction; a few thin construction lines cross it. Red ring, black solid mass, cream negative space should have strong dynamic tension and an unmistakable primary diagonal. Keep exactly one hero construction and a generous clear upper-left margin. No humanoid silhouette.
Typography: large exact Chinese text "回响" aligned on the same main diagonal as the beam, integrated into the construction with clear contrast; small "FORM / FORCE" at bottom left; small "01" at top right. No other text. Architectural grotesk lettering, precise, readable, dramatically scaled.
Medium: flat lithographic editorial artwork on clean warm cream paper. Muted oxide red, near black and one middle gray only. Fine restrained printing grain, crisp geometry, no fake old stains, no torn edge. Full-bleed artwork, no frame, no mockup.
Constraints: distinctly new spatial arrangement, no source logo or historical insignia, no watermark, no gradients, no 3D extrusion or cast shadow.
```

## B｜空间 · 建筑几何化

参考输入：references/images/03-dessau-photo.jpg

```text
Use case: stylized-concept
Asset type: source-photo-to-geometric editorial poster; skill evaluation B.
Input image: supplied real photograph of the Bauhaus Dessau building. Use it as the SUBJECT AND SPATIAL STRUCTURE reference. Preserve the recognizable long gridded glass wing receding left, the prominent upright near-right solid facade, and the shorter white blocks receding behind on the right. Translate the actual camera viewpoint and those three relationships into a flat architectural print. Remove all trees, lawn, poles, tiny reflections, detailed doors, and original BAUHAUS lettering.
Primary request: create an original contemporary Bauhaus-inspired architectural poster titled "空间". Portrait 3:4. Full-bleed clean cream sheet; upper third mostly open. Architectural construction occupies lower two thirds. Reduce the whole structure to 6 to 9 decisive planar masses: ultramarine blue glass wing, sparse thin black window grid with only about 7 vertical divisions, a warm yellow light-facing central plane, a charcoal side plane, two white background block volumes, and a small vermilion entry rectangle. A small red sun circle in the empty upper-right field balances the blue mass; only one fine diagonal line continues the roof's perspective toward the title.
The geometry must describe this supplied building, never generic floating circle-square-triangle decoration. Minimal flat screenprint, no photoreal photographic pixels, no perspective distortion of the important building relationships, no simulated 3D lighting or gradients. A quiet small gray plane may separate volumes. Approximately 40 percent negative space. Ink colors: red #D43C32, yellow #E7BC2C, blue #254F9B, black #17191B and warm white #F1EDE3, not equal proportions.
Typography: exact Chinese title "空间" large black at top left, below it small "SPACE / STRUCTURE", and tiny "02" bottom right. Nothing else. Clear grid alignment, strong original design, sharp clean shape edges, extremely subtle paper texture. No logos, no signature, no watermark, no frame or room mockup.
```

## C｜构造 · 摄影与排版

参考输入：references/images/03-dessau-photo.jpg + references/images/01-schmidt-1923.jpg

```text
Use case: stylized-concept
Asset type: original photographic-typographic architectural exhibition poster, skill evaluation C.
Input images: Image 1 is the real Bauhaus Dessau building photograph, SUBJECT reference. Image 2 is the Joost Schmidt 1923 exhibition poster, STYLE reference only.
Primary request: design a refined contemporary portrait 3:4 poster with exact Chinese title "构造", bringing the real architectural photograph into a disciplined red-black-cream typographic construction. Preserve the real building's identity, corner camera perspective, glass grid wing receding left, central solid facade and secondary blocks on the right. Keep the architectural area photographic, with natural window reflections, light and material detail, rendered monochrome with good midtone separation. Do not turn the building into an illustration.
Composition: warm cream paper field, broad quiet margins. Place one large monochrome rectangular photograph in the middle-right and lower area, with its top edge approximately 30 percent down the sheet and its right edge inset 6 percent. A single substantial flat vermilion diagonal stripe rises from the lower left toward upper right across the bottom quarter of the photograph. The title "构造" in large black geometric sans-serif follows that diagonal across the cream field immediately below the stripe, never over dark photographic detail. One small solid black circle near upper left and one fine vertical rule align with the photographic left edge. Let the photograph's strong roofline and the stripe make one coherent directional system, not a scrapbook. Have ample 30 to 40 percent quiet cream space at top. Typography and photo share an underlying grid.
Text: only "构造", small uppercase "IMAGE / STRUCTURE" top left, and small "03" bottom right. Remove or obscure original BAUHAUS building lettering; no invented historical text.
Style transfer from image 2: asymmetric visual weight, red/black/cream economy, forceful diagonal typography structurally integrated with geometric forms. Create an entirely new composition, do not copy the source's head emblem, cross layout, signatures, or lettering. Sharp print layout, slight ink and paper texture, no artificial torn edges, no distressed sepia, no border frame, no mockup, no watermark, no gradients in graphic elements.
```

