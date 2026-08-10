# Aura — blog de marca

Toallas sanitarias **de tela reutilizables**, cosidas en San Pedro Sula.

Sitio estático, sin build. HTML, CSS y JavaScript plano. Se sube tal cual a
GitHub Pages, Netlify o cualquier hosting.

---

## Cómo responde a la consigna

> *«Publicación en Blog/Página web: Creación de un artículo promocionando el
> lanzamiento de una marca eco-amigable utilizando una estrategia de
> distribución exclusiva.»*

| Elemento pedido | Dónde está |
|---|---|
| **El artículo de lanzamiento** | `articulos/lanzamiento-aura-san-pedro-sula.html` — pieza principal, destacada en la portada |
| **Marca eco-amigable** | Aura: toallas sanitarias de tela reutilizables. Composición, origen y vida útil publicadas en `index.html#composicion` |
| **Estrategia de distribución exclusiva** | Desarrollada en el artículo: comparación de los tres modelos de intensidad, selección de plaza de entrada, cuatro razones de la elección, cinco criterios de selección de puntos y contraprestación al aliado |
| **Publicación en blog / web** | Sitio completo de 11 páginas con 6 artículos y 25 referencias |

**El artículo de lanzamiento es la entrega.** Todo lo demás existe para
sostenerlo: el blog le da contexto, la ficha de producto lista los seis
puntos y `marca.html` documenta el razonamiento estratégico.

### Conceptos de mercadeo que quedan demostrados

- **Intensidad de distribución.** Intensiva, selectiva y exclusiva comparadas
  y graficadas (`assets/img/fig-distribucion.svg`). Se justifica por qué una
  categoría que normalmente es intensiva opera aquí en el extremo opuesto.
- **Selección de plaza de entrada.** Por qué San Pedro Sula y no lanzamiento
  nacional: densidad del segmento, tejido de comercio independiente y
  logística de un solo radio. Incluye el argumento de medición — con seis
  puntos en un mismo mercado, las diferencias de rotación se explican por
  ejecución y no por variables regionales.
- **Expansión por fases con condición de entrada medible.** Ampliar dentro de
  San Pedro Sula, después Tegucigalpa, y solo al final la transición a
  distribución selectiva. Cada fase se activa por métrica, no por fecha.
- **No solape territorial.** Las seis zonas no se cruzan: dos aliados
  compitiendo por el mismo radio anularían el sentido de la exclusividad.
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
- **Comunicación ambiental y greenwashing.** Datos de la Comisión Europea, en
  `articulos/greenwashing-marketing-verde.html`. La primera trampa de la lista
  es la de la propia categoría de Aura.

### Criterio de redacción

Ninguna afirmación del sitio va sin fuente enlazada. Donde la evidencia es
débil o contradice el argumento comercial de la marca, el texto lo dice. Dos
ejemplos deliberados:

- El artículo de ciclo de vida cita que **una toalla reutilizable importada
  por vía aérea puede tener mayor impacto que una desechable** (Life Cycle
  Initiative del PNUMA). Es el dato más peligroso posible para una marca de
  toallas reutilizables, y está en dos artículos.
- El mismo artículo cita que los productos desechables **orgánicos** tienen
  impactos mayores que los no orgánicos, lo que desarma la equivalencia entre
  «natural» y «mejor» de la que vive media categoría.

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
│   ├── lanzamiento-aura-san-pedro-sula.html   <- LA ENTREGA
│   ├── reutilizable-o-desechable.html
│   ├── cuanto-dura-cuanto-ahorra.html
│   ├── como-lavar-toallas-de-tela.html
│   ├── greenwashing-marketing-verde.html
│   └── pobreza-menstrual-america-latina.html
├── assets/
│   ├── css/aura.css                Sistema visual completo
│   ├── js/aura.js                  Sin dependencias
│   └── img/                        Fotos de producto, logotipo, figura
├── .nojekyll · robots.txt · sitemap.xml
└── build_*.py                      Generadores de páginas (opcionales)
```

Peso total: unos 500 KB, la mayor parte en las dos fotos de producto. Sin frameworks, sin `node_modules`, sin compilación.

---

## Datos ficticios que conviene ajustar

Este es un ejercicio académico, así que varios datos son inventados de forma
plausible. Si vas a presentarlo, revisá que la ficción sea coherente con lo
que digas en la defensa.

| Dato | Valor actual | Nota |
|---|---|---|
| Fecha de lanzamiento | 1 de septiembre | Ajustala a tu calendario |
| Puntos de venta | 6, todos en San Pedro Sula | Se nombran por zona y tipo de comercio, no por razón social, para no atribuir nada a negocios reales |
| Precios | L 145 / L 185 / L 225 por unidad | Coherentes con un producto que dura años, no con un paquete de desechables |
| Materiales por capa | Algodón, bambú, capa impermeable | Sustituilos por los de tu ficha real de confección |
| Correo | `hola@aura.hn` | Dominio ficticio |

**Los datos científicos y regulatorios sí son reales** y están enlazados a su
fuente: los estudios citados, las normas EN 13432 y ASTM D6400, las cifras de
la Comisión Europea y los datos de ONU Mujeres y UNESCO.

---

## Advertencia sobre afirmaciones ambientales

El sitio está redactado para no prometer lo que no se puede sostener, y esa
redacción es deliberada: es parte del argumento del trabajo. Tres ejemplos
que conviene **no** cambiar:

1. **Vida útil.** Se publica 4.3 años como media observada en la literatura,
   no como garantía de la marca. El rango de hasta diez años se presenta
   como lo que es: un techo con buen cuidado.
2. **Producción local.** El argumento no es identidad, es la condición que
   la Life Cycle Initiative del PNUMA señala como determinante. Si algún día
   el producto se importa, ese argumento deja de ser válido.
3. **Para quién no sirve.** El sitio dice explícitamente que sin agua limpia,
   jabón y un lugar donde secar, el producto no funciona. Es lo que separa
   informar de vender.

Lo mismo con las afirmaciones de salud: se cita la irritación reportada en
estudios concretos, señalando que vienen de contextos distintos al hondureño
y que sus autores califican la calidad general como baja.

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
python3 build_articles.py     # los seis artículos
python3 build_inner.py        # blog, producto y marca
python3 gen_logo.py           # marca gráfica y favicon
python3 gen_fig_dist.py       # figura de distribución
```

`build_shell.py` contiene el encabezado, el pie y la plantilla de artículo
que comparten todas las páginas.

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
- Las fotos de producto están en `assets/img/producto-mesa.jpg` y
  `producto-bano.jpg`. La del hero se recorta a 5:4 con `object-fit: cover`;
  si la sustituís, cuidá que el producto quede en el centro del cuadro.
- El logotipo se genera con `gen_logo.py` en tres variantes: marca sobre
  claro, sobre oscuro y favicon.
