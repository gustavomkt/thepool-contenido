# Proceso: calendario → aprobación → ajustes → programación

Este repo es el "canvas" del contenido de redes de The Pool (IG, FB, LinkedIn).
La página `index.html` (GitHub Pages) muestra cada calendario. El cliente aprueba o pide cambios
**sin cuenta de GitHub**: sus acciones se guardan en Supabase.

## Piezas del sistema

| Qué | Dónde |
|---|---|
| Página de revisión | https://gustavomkt.github.io/thepool-contenido/?cal=<CAL>&k=<TOKEN> |
| Contenido (copys, slides, guiones) | `calendarios/<CAL>/content.py` |
| Media publicada | `calendarios/<CAL>/media/<id>/` (slides .jpg + PDF LinkedIn, o reel.mp4 + portada.jpg) |
| Voz de reels | `calendarios/<CAL>/audio/<id>.mp3` (ElevenLabs, voz "Silverio" `lLu7VwiNjffLb7HZ3LFW`, modelo `eleven_v4`) |
| Generador | `generador/` (render.py carruseles, reel.py reels, build.py todo) |
| Fotos de sedes | `generador/fotos/` (sacadas de OperIA) |
| Estados y comentarios | Supabase proyecto `gxifhvpkymxeuewrcsnx`, tablas `posts`, `feedback`, `review_tokens` |

Estados de `posts.status`: `pendiente` → (`aprobado` | `cambios`) → `en_ajuste` → `pendiente` (nueva versión) … → `programado` → `publicado`.

## Marca (pedido de Luis)
Colores sobrios, **sin naranja**: negro #1B1B1B, blanco, grises #F0F0F0 / #6B6B6B / #AAAAAA.
Tipografía Open Sauce One. Logo oficial (`generador/brand/`). Precios siempre "+ IVA". Copys en español
casual y cercano, sin frases de IA. No inventar testimonios ni datos.
**No mezclar sedes** (Luis, 19-nov): una pieza de una sede solo muestra fotos y datos de esa sede; si una pieza junta varias sedes, cada foto lleva su etiqueta de sede (el generador la pone sola). Números escritos con cifra en guiones y subtítulos ("Goldsmith 40", "10%").

## Ciclo de revisión (lo corre la tarea programada)

1. Leer pendientes:
   ```sql
   select f.*, p.tipo, p.status from feedback f join posts p on p.id=f.post_id
   where not f.atendido order by f.created_at;
   ```
2. **Cambios** (`accion='cambios'`):
   - `update posts set status='en_ajuste' where id=...`
   - Editar `calendarios/<CAL>/content.py` según el comentario. Si cambia el guion de un reel, generar
     nueva voz en ElevenLabs (misma voz/modelo, 1 take) y guardarla en `audio/<id>.mp3`.
   - `CAL=<CAL> python3 generador/build.py <id>` y revisar visualmente el resultado.
   - Subir versión: `versiones.json[id] += 1`, volver a correr build.py (actualiza calendar.json), commit + push.
   - `update posts set status='pendiente', version=version+1 where id=...`
   - `update feedback set atendido=true, respuesta='<qué se cambió, 1 línea>' where id=...`
   - Si el comentario pide algo imposible o ambiguo, no adivinar: responder en `respuesta` y avisar a Gustavo.
3. **Aprobados** (`accion='aprobar'` y `posts.status='aprobado'`):
   - Programar en **Meta Business Suite** (portafolio ThePoolMX, business_id 111905939699283,
     page_id 155211851294770 → FB + IG @thepoolmx) y en **LinkedIn** (página company/2873700)
     desde el Chrome de Gustavo, en la fecha de la pieza a las 10:00 (America/Mexico_City).
     Carrusel: subir los JPG en orden (IG/FB) y el PDF como documento (LinkedIn). Reel: reel.mp4 + portada.jpg.
     Copy IG/FB y copy LinkedIn desde `calendar.json`.
   - Si la fecha ya pasó, programar para el siguiente día hábil a las 10:00 y avisar.
   - `update posts set status='programado', programado_en='{"ig":"...","fb":"...","linkedin":"..."}'`.
   - `update feedback set atendido=true where ...`
4. Avisar a Gustavo (resumen corto: qué se ajustó, qué se programó, qué quedó pendiente).

### Notas técnicas para programar (aprendido 25-nov)
- Antes de programar, revisar `posts.programado_en`: si ya trae `fb`/`ig`/`linkedin`, esa red ya está; si trae `*_verificar`, revisar el Planificador de Business Suite antes de reintentar (evita duplicados).
- `status='programado'` solo cuando estén las 3 redes; mientras tanto se va llenando `programado_en` por red.
- Subir archivos sin abrir el selector nativo: copiar la media a `/mnt/user-data/outputs/thepool/<id>/`, parchar `HTMLInputElement.prototype.click` para que el input `file` que crea la página se agregue al DOM (con `aria-label`) en lugar de abrir el diálogo, dar clic en "Agregar foto/video", ubicar el input con `find` y usar `file_upload`. `fetch()` a GitHub está bloqueado por la CSP de Facebook.
- Texto: escribir con la acción `type` (teclado real). `execCommand`/paste rompen el editor. El `type` largo a veces marca timeout pero sí escribe; esperar ~15 s y leer el `contenteditable`.
- Fechas: en el campo de fecha `cmd+a`, escribir `dd/mm/aaaa`, Enter y clic en el día; hora: clic en la hora, escribir `10`, flecha derecha, `00`.
- Reels: usar `/latest/reels_composer`; portada en "Imagen en miniatura → Subir imagen"; en Compartir elegir **Programar** (por defecto viene "Compartir ahora").
- Trabajar siempre en la pestaña activa: las de fondo no repintan las capturas.
- Fechas ya pasadas: siguiente día hábil 10:00.
- Reels: escribir el copy **antes** de subir el video (el preview roba el foco y corta el `type`).

### LinkedIn (aprendido 26-nov)
- Página: `linkedin.com/company/2873700/admin/page-posts/published/` → "Start a post".
- Carrusel: "+" → ícono documento → `file_upload` al input "Choose file" → título obligatorio ("<Gancho> | The Pool") → Done → copy.
- Reel: ícono de media → subir mp4 → ícono de imagen del editor → "Add video thumbnail" → portada.jpg → Add → Next → copy. Adjuntar la media **antes** del copy; si no, thepool.mx genera un link preview que hay que quitar.
- Programar: reloj junto a "Post" → fecha con el calendario (escribirla y dar Enter no la toma) → la hora se pone sola en el siguiente cuarto de hora: abrir la lista, subir un poco y elegir 10:00 AM → Next → Schedule.
- Verificar en reloj → "View all scheduled posts".

Autorización: Gustavo pidió (18-nov-2026) que lo aprobado por el cliente en esta página se programe
sin pedirle confirmación. Solo aplica a piezas de este repo con estado `aprobado`.

## Nuevo calendario (siguiente mes)

1. `cp -r plantilla/content_ejemplo.py calendarios/<NUEVO_CAL>/content.py` y reescribir `POSTS`
   (lun carrusel, mié reel, vie carrusel; pilares comunidad / sedes / opciones / promo).
2. Generar voces de reels → `calendarios/<NUEVO_CAL>/audio/<id>.mp3`. Crear `versiones.json` con `{}`.
3. `CAL=<NUEVO_CAL> python3 generador/build.py`
4. Agregar `{"id": "<NUEVO_CAL>", "nombre": "..."}` a `calendarios/calendarios.json`.
5. En Supabase: insertar filas en `posts` (id `<CAL>/<nn>`) y un token nuevo en `review_tokens`.
6. Commit + push y mandar a Luis el link `?cal=<NUEVO_CAL>&k=<TOKEN>`.
