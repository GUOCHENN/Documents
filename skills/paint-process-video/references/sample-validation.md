# Validación del ejemplo

Entrada: imagen generada de una cesta de manzanas del skill photo-miniature-diorama, basada en una [fotografía de Misky](https://unsplash.com/photos/apple-fruits-in-brown-wicker-basket-66_SpSQ1_IA). La fotografía original mantiene la [licencia Unsplash](https://unsplash.com/license). No se incluyen las capturas de pantalla privadas del briefing.

Salida medida por FFprobe:

- Contenedor MP4; vídeo H.264; píxeles yuv420p.
- 2880×3840, 60/1 fps, 960 fotogramas, 16 segundos.
- Entrada 1086×1448; trabajo 768×1024. La salida se amplió: no contiene detalle nativo nuevo de 4K.
- Final del trazo a 6,4 s; sujeto coloreado a 12 s; fondo completado a 14,4 s; cierre hasta 16 s.

Se inspeccionaron los fotogramas de evidencia: lápiz visible durante el trazo; sujeto coloreado sobre blanco antes del fondo; imagen completa al final. El objeto contiene doce formas de fruta aproximadamente, no una reproducción exacta de la cantidad de manzanas de la fotografía inicial.

Limitaciones: el contorno es una inferencia por bordes y puede simplificar líneas o duplicarlas; el relleno avanza según una máscara y una distancia, no según semántica de objetos ni pinceladas reales. La máscara automática de este ejemplo incluye parte de la sombra. Para otras imágenes debe revisarse de nuevo.
