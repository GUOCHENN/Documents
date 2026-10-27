---
name: architecture-ink-dissolve
description: Transforma fotografías de arquitectura en carteles de mitad fotografía en color y mitad calco de tinta que se desvanece siguiendo la estructura, con una composición vertical y mucho espacio vacío. Úsalo para edificios que se disuelven en tinta; no para filtros de acuarela ni para reconstrucción arquitectónica exacta.
---

# Arquitectura · Huella de tinta

Crea un cartel independiente por fotografía. La identidad del edificio procede de la foto; las referencias de estilo solo orientan el espacio, el papel y la tinta.

## Resultado y composición

- Formato inicial 3:4 vertical, salvo indicación del usuario.
- Aísla un edificio principal. Conserva punto de vista, proporciones, pisos, techos, ventanas, vigas, columnas y adornos identificables. Retira cielo y elementos ajenos. No inventes la mitad que falta en una foto muy recortada: busca otra fuente si el usuario autorizó la búsqueda; si no, trabaja con el fragmento visible y explica el alcance.
- Papel marfil cálido casi liso, fibra mínima y acabado mate. Edificio centrado, algo bajo, con aire especialmente arriba. Como punto de partida, ancho de 55–65% y altura de 35–50%; adapta el encuadre a una torre esbelta sin deformarla ni recortarla.
- Una línea vertical en el centro divide el MISMO edificio: izquierda en tinta negra/gris, derecha en color fotográfico. Mantén continuidad de tejados, ventanas, barandas y perspectiva en la unión. No reflejes una mitad ni conviertas una vista oblicua en una fachada simétrica.
- La derecha conserva los colores, la luz y los materiales de la fuente. La izquierda traduce la estructura a calco seco y grabado fino, con blancos de papel dentro de los detalles.

## La disolución es estructural

Cerca del eje, las líneas siguen siendo legibles. Hacia el exterior izquierdo pasan por estructura clara → líneas interrumpidas → películas finas de tinta → rastros escasos. Sigue aleros, vigas y barandas; abre también huecos dentro de ventanas y entramados. Cuanto más lejos del eje, más fina, ligera y dispersa es la huella.

Evita una simple foto gris con puntos superpuestos, grandes manchas negras, bloques de piedra volando, humo, explosiones, brillos o partículas luminosas. El eje puede prolongarse en el papel con una línea gris muy fina e interrumpida; nunca una división gruesa.

## Texto y sello

En este paquete, el idioma visual predeterminado es español. Respeta otro idioma si el usuario lo pide. Utiliza una frase corta relacionada con el edificio, pequeña y manuscrita, debajo del sujeto y preferentemente a la izquierda del eje. Por ejemplo: “Memoria”, “Huella dorada”, “Ecos del tiempo”. No copies leyendas de una referencia.

Opcionalmente añade debajo un sello rectangular pequeño de rojo cinabrio con una marca abstracta sencilla; no inventes caracteres chinos o japoneses. Evita titulares grandes, texto ilegible, logotipos, marcos y adornos de sol o luna. Si hay rótulos históricos en la foto, acuerda el tratamiento según la petición: no confundas una traducción con texto histórico auténtico.

## Generación y revisión

Utiliza la herramienta de imágenes disponible; para una entrada local, visualízala primero. En el prompt, identifica cada imagen como fuente del edificio o referencia de estilo. Enumera los invariantes concretos de ESA foto, especialmente número de pisos/techos y perspectiva. Los ejemplos y prompts completos están en [references/prompts.md](references/prompts.md).

Revisa visualmente cada resultado frente a su fuente:
- Igual número de techos y pisos, forma y perspectiva reconocibles.
- Unión continua en el eje; sin desplazamiento de aleros o ventanas.
- Izquierda sin contaminación de color; derecha fiel a materiales y paleta.
- Tinta interrumpida y papel visible por dentro, con dispersión siguiendo la estructura.
- Espacio vacío suficiente, idioma y palabras correctos.

Si falla algo, solicita una edición concreta del resultado preservando lo que sí funciona. Si se requiere exactitud documental o conservación de píxeles, la generación no la garantiza: indica las diferencias y utiliza una composición controlada apropiada al encargo.

## Entrega con comparación

Entrega el cartel final independiente y una muestra comparativa separada: foto original ARRIBA y resultado ABAJO; se permite original a la izquierda y resultado a la derecha si se aprecia mejor. Inserta los archivos originales y finales completos, sin redibujar la fuente ni estirar o recortar el sujeto. Rotula en español “ORIGINAL” y “RESULTADO”. Un cartel individual no contiene paneles de comparación.

Conserva fuentes y condiciones junto a los prompts cuando proceda. La [galería](comparison.html) y el [README](README.md) muestran tres pares. No publiques capturas de redes sociales ni información de cuenta. La publicación en una cuenta externa solo procede con autorización del usuario; invocar este skill por sí solo no autoriza publicar.

## Escena completa opcional

Si el usuario pide conservar todo el paisaje, mantén sus relaciones espaciales en lugar de extraer un edificio. Divide por el eje de la imagen; orienta la disolución según crestas, ramas, agua y reflejos. Evita aplicar las medidas de un edificio aislado a la escena completa.

