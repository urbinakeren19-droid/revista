# Aura — blog de marca

Sitio estático, sin build. HTML, CSS y JavaScript plano. Se sube tal cual a
GitHub Pages, Netlify o cualquier hosting.

---

## Cómo responde a la consigna

> *«Publicación en Blog/Página web: Creación de un artículo promocionando el
> lanzamiento de una marca eco-amigable utilizando una estrategia de
> distribución exclusiva.»*

| Elemento pedido | Dónde está |
|---|---|
| **El artículo de lanzamiento** | `articulos/lanzamiento-aura-honduras.html` — pieza principal, destacada en la portada |
| **Marca eco-amigable** | Aura: toalla sanitaria de fibra vegetal. Composición completa publicada en `index.html#composicion` |
| **Estrategia de distribución exclusiva** | Desarrollada en el artículo: comparación de los tres modelos de intensidad, cuatro razones de la elección, criterios de selección de puntos y contraprestación al aliado |
| **Publicación en blog / web** | Sitio completo de 11 páginas con 6 artículos y 49 referencias |

**El artículo de lanzamiento es la entrega.** Todo lo demás existe para
sostenerlo: el blog le da contexto, la ficha de producto lista los catorce
puntos y `marca.html` documenta el razonamiento estratégico.

### Conceptos de mercadeo que quedan demostrados

- **Intensidad de distribución.** Intensiva, selectiva y exclusiva comparadas
  y graficadas (`assets/img/fig-distribucion.svg`). Se justifica por qué una
  categoría que normalmente es intensiva opera aquí en el extremo opuesto.
- **Exclusividad recíproca.** El aliado no vende competencia directa; la marca
  no vende a otro minorista en su radio. Con la contraprestación explícita:
  margen superior, capacitación pagada y protección territorial.
- **Control de precio por canal.** Política de precio única como consecuencia
  directa del contrato de exclusividad.
- **Mezcla de mercadeo.** Las cuatro P desarrolladas en `marca.html`.
- **Posicionamiento y segmentación.** Enunciado de posicionamiento con sus
  cuatro consecuencias operativas, más tres perfiles de audiencia.
- **Mercadeo de contenidos.** Cuatro pilares editoriales, con la explicación
  de por qué el pilar que no vende es el que da credibilidad a los otros tres.
- **Métricas.** Cuatro indicadores, con el argumento de por qué en
  distribución exclusiva la venta total es una métrica engañosa.
- **Comunicación ambiental y greenwashing.** Datos de la Comisión Europea y
  jurisprudencia europea reciente, en `articulos/greenwashing-marketing-verde.html`.

### Criterio de redacción

Ninguna afirmación del sitio va sin fuente enlazada. Donde la evidencia es
débil o contradice el argumento comercial de la marca, el texto lo dice. Dos
ejemplos deliberados:

- El artículo sobre química cita que los productos etiquetados como
  «orgánicos» o «naturales» no presentaban necesariamente menos compuestos
  volátiles — un dato que perjudica a la propia categoría de Aura.
- El artículo sobre plástico admite que la cifra del 90 % que usa toda la
  industria ecológica **no puede verificarse de forma independiente**.

Si el trabajo se defiende oralmente, ese es el argumento fuerte: la
credibilidad de las cifras favorables depende de haber publicado también las
desfavorables.

---

## Estructura

```
aura/
├── index.html                      Portada del blog, encabezada por el lanzamiento
├── blog.html                       Índice de artículos + método editorial
├── producto.html                   Fichas técnicas + los 14 puntos de venta
├── marca.html                      Estrategia de marca completa
├── 404.html
├── articulos/
│   ├── lanzamiento-aura-honduras.html        <- LA ENTREGA
│   ├── greenwashing-marketing-verde.html
│   ├── plastico-en-toallas-sanitarias.html
│   ├── quimicos-en-productos-menstruales.html
│   ├── biodegradable-o-compostable.html
│   └── pobreza-menstrual-america-latina.html
├── assets/
│   ├── css/aura.css                Sistema visual completo
│   ├── js/aura.js                  Sin dependencias
│   └── img/                        SVG: empaques, figuras, favicon
├── .nojekyll · robots.txt · sitemap.xml
└── build_*.py                      Generadores de páginas (opcionales)
```

Peso total: unos 368 KB. Sin frameworks, sin `node_modules`, sin compilación.

---

## Datos ficticios que conviene ajustar

Este es un ejercicio académico, así que varios datos son inventados de forma
plausible. Si vas a presentarlo, revisá que la ficción sea coherente con lo
que digas en la defensa.

| Dato | Valor actual | Nota |
|---|---|---|
| Fecha de lanzamiento | 1 de septiembre | Ajustala a tu calendario |
| Puntos de venta | 14, en 4 ciudades | Los nombres son genéricos («Farmacia — Barrio X») a propósito, para no atribuir nada a negocios reales |
| Precios | L 65 / L 72 / L 58 | Coherentes con un posicionamiento superior |
| Porcentajes de composición | Suman 100 % | Si los cambiás, verificá que sigan sumando 100 |
| Correo | `hola@aura.hn` | Dominio ficticio |

**Los datos científicos y regulatorios sí son reales** y están enlazados a su
fuente: los estudios citados, las normas EN 13432 y ASTM D6400, las cifras de
la Comisión Europea y los datos de ONU Mujeres y UNESCO.

---

## Advertencia sobre afirmaciones ambientales

El sitio está redactado para **no** afirmar que el producto está certificado.
Dice que está en proceso de certificación, y esa redacción es deliberada: es
parte del argumento del trabajo.

No la cambies. Las guías de publicidad ambiental consideran engañoso llamar
«biodegradable» o «compostable certificado» a un producto sin evidencia de
ensayo específica, y todo el sitio está construido sobre esa distinción.
Un profesor que revise el detalle va a buscar precisamente eso.

Lo mismo con las afirmaciones de salud: los artículos citan estudios sobre
*presencia* de compuestos, no sobre daño demostrado, y la diferencia está
señalada de forma explícita.

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

Settings → Pages → Deploy from a branch → main → / (root).

El `.nojekyll` ya está incluido. Para dominio propio, agregá un archivo
`CNAME` con el dominio en la raíz.

---

## Regenerar páginas

Las páginas interiores se generan desde una plantilla común para que el menú
y el pie no se desincronicen entre las once páginas.

```bash
python3 build_pages.py        # los 4 artículos base
python3 build_art5.py         # artículo de greenwashing
python3 build_lanzamiento.py  # artículo de lanzamiento
python3 build_inner.py        # blog, producto y marca
python3 gen_packs.py          # SVG de empaques
python3 gen_fig_dist.py       # figura de distribución
```

`index.html` y `404.html` se editan a mano. El sitio funciona sin los scripts;
solo tené presente que un cambio en el menú hay que replicarlo en cada página.

---

## Notas técnicas

- Fuentes desde Google Fonts: Young Serif, Newsreader, Instrument Sans y
  DM Mono. Todas con licencia libre para uso comercial.
- El sitio funciona sin JavaScript: el contenido se ve igual. El JS solo
  agrega el diagrama interactivo, la calculadora, el menú móvil y las
  animaciones de entrada.
- Respeta `prefers-reduced-motion`.
- Navegación por teclado y foco visible en todos los controles.
- Los empaques son ilustraciones SVG, no fotos. Si conseguís producto real,
  reemplazá los `<img src="assets/img/pack-*.svg">` manteniendo proporción 4:5.
