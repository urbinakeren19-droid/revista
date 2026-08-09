# Aura — sitio web

Sitio estático, sin build. HTML, CSS y JavaScript plano. Se sube tal cual a
GitHub Pages, Netlify, Vercel o cualquier hosting.

```
aura/
├── index.html                     Portada (diagrama de capas + etiqueta de composición)
├── producto.html                  Fichas técnicas y pedidos
├── ciencia.html                   Índice de artículos + metodología editorial
├── 404.html
├── articulos/
│   ├── plastico-en-toallas-sanitarias.html
│   ├── quimicos-en-productos-menstruales.html
│   ├── biodegradable-o-compostable.html
│   └── pobreza-menstrual-america-latina.html
├── assets/
│   ├── css/aura.css               Todo el sistema visual
│   ├── js/aura.js                 Sin dependencias
│   └── img/                       SVG: empaques, favicon, figura de degradación
├── .nojekyll                      Necesario en GitHub Pages
├── robots.txt
└── sitemap.xml
```

Peso total: unos 224 KB. Sin frameworks, sin `node_modules`, sin paso de compilación.

---

## Antes de publicar: reemplazos obligatorios

Están marcados en el código con `EDITAR`. Búscalos con `grep -rn "EDITAR" .`

| Qué | Dónde | Ahora dice |
|---|---|---|
| Número de WhatsApp | todas las páginas | `wa.me/504XXXXXXXX` |
| Correo | pie de página y artículos | `hola@aura.hn` |
| Instagram | pie de página | enlace vacío |
| Precios | `index.html`, `producto.html` | L 65 / L 72 / L 58 |
| Porcentajes de composición | `index.html`, sección `#composicion` | valores de ejemplo |
| Medidas y unidades por paquete | `producto.html` | 240/320/155 mm |
| Dominio | `sitemap.xml`, `robots.txt` | `aura.hn` |

---

## La etiqueta de composición

Es el elemento central del sitio y el que sostiene todo el argumento. Los
porcentajes actuales son de ejemplo y **suman 100 %**. Cuando los sustituyas
por los de tu ficha técnica real, verificá que sigan sumando 100.

Si tu proveedor no te entrega el desglose por capa con porcentajes, pedíselo
por escrito antes de lanzar. Sin ese dato, la promesa central del sitio no se
puede sostener.

---

## Advertencia legal sobre afirmaciones ambientales

El sitio está redactado deliberadamente para **no** afirmar que el producto
está certificado. Dice que está en proceso de certificación.

No cambies esa redacción hasta tener el certificado con código de
trazabilidad. Las guías de publicidad ambiental (FTC Green Guides en EE. UU.,
y criterios equivalentes en la UE) consideran engañoso llamar «biodegradable»
o «compostable certificado» a un producto sin evidencia de ensayo específica.
Es la clase de afirmación que puede costar una sanción o una denuncia de
competencia desleal, y que además destruye exactamente la credibilidad que
este sitio está construido para generar.

Lo mismo aplica a las afirmaciones de salud. Los artículos citan estudios
sobre presencia de compuestos, no sobre daño demostrado, y esa distinción
está hecha a propósito.

---

## Fotografía

Los empaques son ilustraciones SVG, no fotos. Funcionan bien para lanzar,
pero cuando tengas producto físico conviene sustituirlas.

Reemplazá los `<img src="assets/img/pack-*.svg">` por tus fotos. Mantené
proporción vertical (aprox. 4:5) y fondo oscuro o recortado.

Tres tomas que valen más que cualquier render:

1. El paquete abierto con las toallas visibles.
2. Un corte transversal real que muestre las capas — es la foto que respalda el hero.
3. La toalla en la mano, para dar escala.

---

## Publicar en GitHub Pages

```bash
git init
git add .
git commit -m "Sitio Aura"
git branch -M main
git remote add origin https://github.com/USUARIO/REPO.git
git push -u origin main
```

En el repositorio: **Settings → Pages → Source: Deploy from a branch → main → / (root)**.

El archivo `.nojekyll` ya está incluido; sin él, GitHub Pages ignora carpetas
que empiezan con guion bajo y puede romper rutas.

Para dominio propio, agregá un archivo `CNAME` con el dominio en la raíz.

---

## Regenerar las páginas

Los artículos y las páginas interiores se generaron con dos scripts en Python
que comparten una sola plantilla, para que el encabezado y el pie no se
desincronicen entre páginas.

```bash
python3 build_pages.py    # los cuatro artículos
python3 build_inner.py    # ciencia.html y producto.html
python3 gen_packs.py      # los SVG de empaque
```

`index.html` y `404.html` se editan a mano.

Si preferís no usar los scripts, podés editar el HTML directamente: el sitio
funciona sin ellos. Solo recordá que un cambio en el menú hay que replicarlo
en las siete páginas.

---

## Notas técnicas

- Las fuentes se cargan desde Google Fonts. Young Serif, Newsreader,
  Instrument Sans y DM Mono, todas con licencia libre para uso comercial.
  Si querés independencia de red, descargalas y serví los `.woff2` localmente.
- El sitio funciona sin JavaScript: el contenido es visible igual. El JS solo
  agrega el diagrama interactivo, la calculadora, el menú móvil y las
  animaciones de entrada.
- Respeta `prefers-reduced-motion`.
- Navegación por teclado y foco visible en todos los controles.
