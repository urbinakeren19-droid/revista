#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Genera ciencia.html y producto.html."""

from build_pages import render

# ==========================================================================
# INVESTIGACIÓN — índice de artículos
# ==========================================================================

POSTS = [
    ("RESIDUOS", "Cuánto plástico hay realmente en una toalla sanitaria",
     "El dato del noventa por ciento se repite en todas partes. Fuimos a buscar de dónde salió, qué lo respalda y por qué es más difícil de verificar de lo que parece.",
     "articulos/plastico-en-toallas-sanitarias.html", "8 MIN · 11 REFERENCIAS"),
    ("SALUD", "Qué encontraron los laboratorios en las toallas convencionales",
     "Ftalatos en el cien por ciento de las marcas analizadas. También la parte que casi ninguna marca ecológica menciona: los productos etiquetados como naturales no salieron necesariamente mejor.",
     "articulos/quimicos-en-productos-menstruales.html", "10 MIN · 9 REFERENCIAS"),
    ("NORMATIVA", "Biodegradable y compostable no significan lo mismo",
     "Qué exigen exactamente las normas EN 13432 y ASTM D6400, por qué una toalla compostable no se degrada en un relleno sanitario, y qué palabra deberías desconfiar en cualquier empaque.",
     "articulos/biodegradable-o-compostable.html", "9 MIN · 8 REFERENCIAS"),
    ("CONTEXTO", "Pobreza menstrual: el costo de no poder elegir",
     "Dos de cada cinco niñas de la región faltan a clases durante su periodo. Qué han hecho México, Colombia y Uruguay al respecto, y dónde queda Honduras en esa conversación.",
     "articulos/pobreza-menstrual-america-latina.html", "7 MIN · 7 REFERENCIAS"),
]

cards = "\n".join(
    f'''      <a class="post-card" href="{href}">
        <span class="post-card__kicker">{k}</span>
        <h3 class="post-card__title">{t}</h3>
        <p class="post-card__dek">{d}</p>
        <span class="post-card__meta">{m}</span>
      </a>''' for k, t, d, href, m in POSTS
)

CIENCIA = f"""
  <section class="band band--tight">
    <div class="wrap" style="max-width:760px">
      <p class="eyebrow">Investigación</p>
      <h1 class="display-xl" style="margin-bottom:var(--s5)">Con la fuente<br>a la vista.</h1>
      <p class="lede">Cada afirmación de este sitio sobre residuos, química o salud está enlazada al estudio que la respalda. Donde la evidencia es débil o contradice nuestro propio argumento comercial, también lo decimos. Es la única forma de que las cifras que sí nos favorecen signifiquen algo.</p>
    </div>
  </section>

  <section class="band--light" style="padding-top:var(--s7)">
    <div class="wrap" style="margin-bottom:var(--s6)">
      <p class="eyebrow">Cuatro artículos</p>
    </div>
    <div class="post-grid">
{cards}
    </div>
  </section>

  <section class="band band--light">
    <div class="wrap" style="max-width:760px">
      <p class="eyebrow">Cómo trabajamos</p>
      <h2 class="display-l" style="margin-bottom:var(--s6)">Reglas que nos pusimos<br>al escribir esto.</h2>

      <div class="faq">
        <details open>
          <summary>Priorizamos literatura revisada por pares</summary>
          <p>Cuando existe un estudio publicado en una revista con revisión por pares, esa es la fuente. Los informes de organizaciones y las notas de prensa se usan solo para contexto o cuando no hay literatura académica disponible, y se identifican como tales en la lista de referencias.</p>
        </details>
        <details>
          <summary>Publicamos los datos que nos contradicen</summary>
          <p>El estudio sobre compuestos volátiles en el mercado estadounidense encontró que los productos etiquetados como orgánicos o naturales no presentaban necesariamente concentraciones menores. Está citado en nuestro artículo sobre química, con esa conclusión textual, porque omitirlo sería exactamente la práctica que criticamos en el resto de la industria.</p>
        </details>
        <details>
          <summary>Separamos «se detectó» de «causa daño»</summary>
          <p>Que un compuesto esté presente en un producto no equivale a que produzca un efecto en salud. Es una distinción que la publicidad de productos naturales borra con frecuencia. En nuestros artículos, la presencia documentada y el riesgo demostrado se tratan como dos afirmaciones distintas, porque lo son.</p>
        </details>
        <details>
          <summary>No usamos sellos que no tenemos</summary>
          <p>Aura está en proceso de certificación de compostabilidad industrial. Hasta que exista un certificado con código de trazabilidad verificable en el registro del organismo emisor, no vas a ver un sello en nuestro empaque ni la palabra «certificado» en este sitio.</p>
        </details>
        <details>
          <summary>Fechamos y corregimos</summary>
          <p>Cada artículo lleva su fecha de última actualización. Si encontrás un error, escribinos a <a href="mailto:hola@aura.hn">hola@aura.hn</a>. Las correcciones se hacen sobre el texto y se anotan al pie.</p>
        </details>
      </div>
    </div>
  </section>

  <section class="band band--garnet band--tight">
    <div class="wrap" style="display:flex;flex-wrap:wrap;gap:var(--s6);align-items:center;justify-content:space-between">
      <div style="max-width:40ch">
        <h2 class="display-m" style="margin-bottom:var(--s3)">Uso libre para fines educativos.</h2>
        <p style="margin:0;opacity:.85;font-family:var(--read)">Si sos docente o trabajás en salud comunitaria, podés reproducir estos textos con atribución. No hace falta pedir permiso.</p>
      </div>
      <a class="btn btn--solid" href="mailto:hola@aura.hn">Escribinos</a>
    </div>
  </section>
"""

render(
    "ciencia.html",
    "Investigación — Aura",
    "Artículos con referencias sobre plástico en toallas sanitarias, química de productos menstruales, normas de compostabilidad y pobreza menstrual en América Latina.",
    CIENCIA, depth=0, active="sci",
)

# ==========================================================================
# PRODUCTO
# ==========================================================================

SPECS = [
    ("Aura Día", "pack-dia.svg", "FLUJO MEDIO · CON ALAS", "L 65", "10 unidades",
     [("Largo", "240 mm"), ("Alas", "Sí"), ("Superficie", "Bambú hilado"),
      ("Núcleo", "Celulosa certificada"), ("Base", "PLA de maíz"), ("Envoltorio", "Papel kraft")]),
    ("Aura Noche", "pack-noche.svg", "FLUJO ALTO · CON ALAS", "L 72", "8 unidades",
     [("Largo", "320 mm"), ("Alas", "Sí, con extensión posterior"), ("Superficie", "Bambú hilado"),
      ("Núcleo", "Celulosa certificada"), ("Base", "PLA de maíz"), ("Envoltorio", "Papel kraft")]),
    ("Aura Diario", "pack-diario.svg", "PROTECTOR DIARIO", "L 58", "20 unidades",
     [("Largo", "155 mm"), ("Alas", "No"), ("Superficie", "Bambú hilado"),
      ("Núcleo", "Celulosa certificada"), ("Base", "PLA de maíz"), ("Envoltorio", "Papel kraft")]),
]

blocks = []
for i, (name, img, tag, price, unit, rows) in enumerate(SPECS):
    trs = "\n".join(
        f'            <tr><th scope="row">{k}</th><td class="num">{v}</td></tr>'
        for k, v in rows
    )
    flip = "direction:rtl" if i % 2 else ""
    blocks.append(f"""
    <div class="wrap" style="display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:var(--s7);align-items:center;padding-block:var(--s7);{flip}">
      <div style="direction:ltr;background:var(--void-2);border:1px solid var(--void-3);border-radius:var(--radius-lg);padding:var(--s7);display:grid;place-items:center">
        <img src="assets/img/{img}" alt="Empaque de {name}" width="240" height="300" loading="lazy" style="max-width:240px">
      </div>
      <div style="direction:ltr">
        <span class="sku__for" style="color:var(--halo)">{tag}</span>
        <h2 class="display-l" style="margin:var(--s3) 0 var(--s5)">{name}</h2>
        <table class="spec-table" style="border:1px solid var(--void-3);border-radius:var(--radius);margin-bottom:var(--s5)">
          <tbody>
{trs}
          </tbody>
        </table>
        <div style="display:flex;align-items:baseline;gap:var(--s4);margin-bottom:var(--s5)">
          <span class="display-m" style="color:var(--halo)">{price}</span>
          <span class="data" style="color:var(--paper-soft)">{unit}</span>
        </div>
        <a class="btn btn--solid" href="https://wa.me/504XXXXXXXX?text=Hola%2C%20quiero%20pedir%20{name.replace(' ', '%20')}">Pedir {name} por WhatsApp</a>
      </div>
    </div>""")

# La tabla de fichas usa fondo oscuro: se corrige el color del texto localmente.
PROD = f"""
  <section class="band band--tight">
    <div class="wrap" style="max-width:760px">
      <p class="eyebrow">Producto</p>
      <h1 class="display-xl" style="margin-bottom:var(--s5)">Tres formatos.<br>Un solo estándar.</h1>
      <p class="lede">Cambia el largo y cambia la superficie de retención. No cambia la lista de materiales: bambú hilado en la superficie, celulosa de pulpa certificada en el núcleo, base de PLA derivado de almidón de maíz. Sin perfume, sin colorante, sin cloro elemental, sin látex.</p>
    </div>
  </section>

  <style>
    .prod-spec .spec-table tbody th {{ color: var(--pulp); }}
    .prod-spec .spec-table tbody td {{ color: var(--paper-soft); }}
    .prod-spec .spec-table th, .prod-spec .spec-table td {{ border-bottom-color: var(--void-3); }}
  </style>

  <section class="prod-spec" id="comprar">
{''.join(blocks)}
  </section>

  <section class="band band--light">
    <div class="wrap" style="max-width:820px">
      <p class="eyebrow">Antes de pedir</p>
      <h2 class="display-l" style="margin-bottom:var(--s7)">Lo que conviene que sepas.</h2>

      <div class="faq">
        <details open>
          <summary>Cómo se hace un pedido</summary>
          <p>Por WhatsApp. Nos escribís el formato y la cantidad, confirmamos disponibilidad y coordinamos la entrega. En Puerto Cortés y San Pedro Sula entregamos directamente; al resto del país enviamos por encomienda.</p>
          <p>No tenemos tienda en línea con pasarela de pago todavía. Cuando la tengamos, va a estar en esta misma página.</p>
        </details>
        <details>
          <summary>Devolución del primer paquete</summary>
          <p>Si probás Aura un ciclo completo y no te convence, te devolvemos el dinero del primer paquete. Nos escribís por el mismo WhatsApp del pedido y listo. No hay formulario ni hay que devolver el producto usado.</p>
          <p>Aplica una vez por persona, sobre el primer paquete de cada formato.</p>
        </details>
        <details>
          <summary>Cómo desecharla</summary>
          <p>Envolvela en su papel kraft y depositala en la basura común, salvo que en tu municipio exista recolección diferenciada de orgánicos. Nunca al inodoro: ninguna toalla sanitaria, ecológica o no, debe ir al sistema de drenaje.</p>
          <p>Si tenés compostera doméstica, las capas de fibra vegetal se degradan ahí, pero la base de PLA no alcanza la temperatura que necesita. Lo explicamos con detalle en <a href="articulos/biodegradable-o-compostable.html">el artículo sobre normas de compostaje</a>.</p>
        </details>
        <details>
          <summary>Instituciones educativas y programas comunitarios</summary>
          <p>Vendemos a precio de costo, sin margen, a escuelas, colegios y organizaciones que distribuyan gratuitamente en Honduras. Escribinos a <a href="mailto:hola@aura.hn">hola@aura.hn</a> con el nombre de la institución y el número aproximado de participantes.</p>
        </details>
      </div>
    </div>
  </section>

  <section class="band band--light-2 band--tight">
    <div class="wrap" style="max-width:760px;text-align:center">
      <p class="eyebrow" style="justify-content:center">Composición</p>
      <h2 class="display-l" style="margin-bottom:var(--s5)">La lista completa de materiales<br>está publicada.</h2>
      <a class="btn btn--garnet" href="index.html#composicion">Ver la etiqueta de composición</a>
    </div>
  </section>
"""

render(
    "producto.html",
    "Producto — Aura",
    "Fichas técnicas de Aura Día, Noche y Diario: medidas, materiales por capa y precio por unidad. Pedidos por WhatsApp en Honduras.",
    PROD, depth=0, active="prod",
)
