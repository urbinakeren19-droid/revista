#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Genera las páginas interiores de Aura a partir de una plantilla común."""

import os

ROOT = "/home/claude/aura"

# --------------------------------------------------------------------------
# Plantilla común
# --------------------------------------------------------------------------

SHELL = """<!DOCTYPE html>
<html lang="es-HN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="icon" href="{p}assets/img/favicon.svg" type="image/svg+xml">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="{ogtype}">
<meta property="og:locale" content="es_HN">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Young+Serif&family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,500;1,6..72,400&family=Instrument+Sans:wght@400;500;600&family=DM+Mono:wght@400;500&display=swap" rel="stylesheet">
<script>document.documentElement.className+=" js";</script>
<link rel="stylesheet" href="{p}assets/css/aura.css">
{head_extra}</head>
<body>

<a class="skip" href="#main">Saltar al contenido</a>
{progress}
<header class="masthead">
  <div class="wrap masthead__inner">
    <a class="brand" href="{p}index.html" aria-label="Aura, inicio">
      <svg viewBox="0 0 32 32" aria-hidden="true">
        <path d="M16 22 m-11 0 a11 11 0 1 1 22 0" fill="none" stroke="#E5A83B" stroke-width="2.4" stroke-linecap="round"/>
        <circle cx="16" cy="22" r="3.6" fill="#8C1D33"/>
      </svg>
      <span style="font-family:var(--display);font-size:1.4rem;letter-spacing:.02em">aura</span>
    </a>

    <button class="nav-toggle" aria-expanded="false" aria-controls="nav" aria-label="Abrir menú"><span></span></button>

    <nav class="nav" id="nav">
      <a href="{p}index.html"{c_home}>Inicio</a>
      <a href="{p}producto.html"{c_prod}>Producto</a>
      <a href="{p}ciencia.html"{c_sci}>Investigación</a>
      <a href="{p}index.html#preguntas">Preguntas</a>
      <a class="btn btn--solid" href="{p}producto.html#comprar">Pedir por WhatsApp</a>
    </nav>
  </div>
</header>

<main id="main">
{body}
</main>

<footer class="foot">
  <div class="wrap">
    <div class="foot__grid">
      <div>
        <a class="brand" href="{p}index.html" style="margin-bottom:var(--s4)">
          <svg viewBox="0 0 32 32" aria-hidden="true" style="height:26px">
            <path d="M16 22 m-11 0 a11 11 0 1 1 22 0" fill="none" stroke="#E5A83B" stroke-width="2.4" stroke-linecap="round"/>
            <circle cx="16" cy="22" r="3.6" fill="#8C1D33"/>
          </svg>
          <span style="font-family:var(--display);font-size:1.4rem">aura</span>
        </a>
        <p class="foot__blurb">Toallas sanitarias de fibra vegetal con la composición publicada. Puerto Cortés, Honduras.</p>
      </div>

      <div>
        <h4>Producto</h4>
        <ul>
          <li><a href="{p}producto.html">Fichas técnicas</a></li>
          <li><a href="{p}index.html#composicion">Composición</a></li>
          <li><a href="{p}producto.html#comprar">Dónde comprar</a></li>
          <li><a href="{p}index.html#preguntas">Preguntas</a></li>
        </ul>
      </div>

      <div>
        <h4>Investigación</h4>
        <ul>
          <li><a href="{p}articulos/plastico-en-toallas-sanitarias.html">Plástico en toallas</a></li>
          <li><a href="{p}articulos/quimicos-en-productos-menstruales.html">Química y piel</a></li>
          <li><a href="{p}articulos/biodegradable-o-compostable.html">Normas de compostaje</a></li>
          <li><a href="{p}articulos/pobreza-menstrual-america-latina.html">Pobreza menstrual</a></li>
        </ul>
      </div>

      <div>
        <h4>Contacto</h4>
        <ul>
          <li><a href="https://wa.me/504XXXXXXXX">WhatsApp</a></li>
          <li><a href="mailto:hola@aura.hn">hola@aura.hn</a></li>
          <li><a href="https://instagram.com/">Instagram</a></li>
        </ul>
      </div>
    </div>

    <div class="foot__legal">
      <span>&copy; <span data-year>2026</span> Aura. Honduras.</span>
      <span>La información de este sitio no sustituye una consulta médica.</span>
    </div>
  </div>
</footer>

<script src="{p}assets/js/aura.js" defer></script>
</body>
</html>
"""

CUR = ' aria-current="page"'


def render(path, title, desc, body, depth=0, active="", ogtype="website",
           progress=False, head_extra=""):
    p = "../" * depth
    html = SHELL.format(
        p=p, title=title, desc=desc, body=body, ogtype=ogtype,
        head_extra=head_extra,
        progress='<div class="progress" aria-hidden="true"></div>\n' if progress else "",
        c_home=CUR if active == "home" else "",
        c_prod=CUR if active == "prod" else "",
        c_sci=CUR if active == "sci" else "",
    )
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(html)
    print("escrito:", path, f"{len(html):,} bytes")


def article(kicker, title, dek, author, date, read, body_html, refs, related):
    """Compone el cuerpo de un artículo."""
    ref_items = "\n".join(
        f'      <li id="r{i}">{r}</li>' for i, r in enumerate(refs, 1)
    )
    rel = "\n".join(
        f'      <a class="post-card" href="{href}">\n'
        f'        <span class="post-card__kicker">{k}</span>\n'
        f'        <h3 class="post-card__title">{t}</h3>\n'
        f'      </a>' for k, t, href in related
    )
    return f"""
  <article class="article">
    <div class="article__header">
      <div class="wrap">
        <span class="article__kicker">{kicker}</span>
        <h1 class="article__title">{title}</h1>
        <p class="article__dek">{dek}</p>
        <div class="byline">
          <span>{author}</span>
          <span>{date}</span>
          <span>{read} de lectura</span>
          <span>{len(refs)} referencias</span>
        </div>
      </div>
    </div>

    <div class="article__body">
      <div class="wrap">
{body_html}

        <section class="refs">
          <h2>Referencias</h2>
          <ol>
{ref_items}
          </ol>
        </section>
      </div>
    </div>
  </article>

  <section class="band band--light-2" style="padding-bottom:0">
    <div class="wrap" style="margin-bottom:var(--s6)">
      <p class="eyebrow">Seguir leyendo</p>
    </div>
    <div class="post-grid">
{rel}
    </div>
  </section>

  <section class="band band--garnet band--tight">
    <div class="wrap" style="display:flex;flex-wrap:wrap;gap:var(--s6);align-items:center;justify-content:space-between">
      <div style="max-width:38ch">
        <h2 class="display-m" style="margin-bottom:var(--s3)">Aura publica su composición completa.</h2>
        <p style="margin:0;opacity:.85;font-family:var(--read)">Cinco capas, su material y su vía de degradación. Sin letra chica.</p>
      </div>
      <a class="btn btn--solid" href="../index.html#composicion">Ver la etiqueta</a>
    </div>
  </section>
"""


def sup(*nums):
    inner = ", ".join(f'<a href="#r{n}">{n}</a>' for n in nums)
    return f'<sup class="ref">[{inner}]</sup>'


# ==========================================================================
# ARTÍCULO 1 — plástico
# ==========================================================================

A1_BODY = f"""
        <p>El dato circula en cada publicación sobre menstruación sostenible: una toalla sanitaria convencional es <strong>noventa por ciento plástico</strong>. Se repite tanto que ya casi nadie pregunta de dónde salió. Vale la pena preguntarlo, porque la respuesta dice bastante sobre cómo funciona esta industria.</p>

        <p>La cifra aparece en literatura revisada por pares. Un análisis de ciclo de vida publicado en <em>Environmental Science and Pollution Research</em> en 2025, que comparó una toalla de pulpa de bambú con una convencional, parte de la premisa de que la mayoría de las toallas desechables se componen de plásticos y pulpa de madera blanqueada, y que esa combinación puede representar hasta el noventa por ciento de su peso.{sup(1)} Una revisión sobre fibras biodegradables publicada en 2025 describe la misma arquitectura: la lámina de barrera exterior es un polímero impermeable, similar al polietileno, resistente a la degradación bacteriana en los sistemas de alcantarillado.{sup(2)}</p>

        <h2>Lo que pasa cuando alguien desarma el paquete</h2>

        <p>Hay una forma más directa de averiguarlo: abrir las toallas y pesar las piezas. Eso hizo el equipo de Natracare con tres marcas —dos líderes de mercado y una de marca propia de supermercado—, separando manualmente los componentes plásticos y pesándolos en balanza de precisión. El promedio fue de <strong>36 gramos de plástico por paquete</strong>: 2.4 gramos por toalla y otros 2.5 gramos en el envoltorio exterior, el equivalente aproximado a cinco bolsas de supermercado.{sup(3)}</p>

        <p>Un cálculo independiente del Ashank Desai Centre for Policy Studies del IIT Bombay llega a un orden de magnitud parecido: contando alas, adhesivos, gel superabsorbente y empaque, cada toalla contiene alrededor de dos gramos de plástico no biodegradable, cerca de cuatro bolsas por paquete.{sup(4)}</p>

        <div class="callout">
          <span class="callout__label">La parte incómoda</span>
          <p>Un ejercicio de verificación periodística europeo concluyó que la cifra del noventa por ciento es, en rigor, <strong>imposible de comprobar de forma independiente</strong>. No porque sea falsa, sino porque a nivel europeo los fabricantes de toallas sanitarias no están obligados a divulgar la lista exhaustiva de sus componentes, y mucho menos sus proporciones. Cuando en 2016 se consultó a la Comisión Europea sobre el tema, la respuesta fue que, al no haberse identificado riesgo para la salud en los estudios disponibles, no podía exigirse a los fabricantes hacer públicos sus ingredientes.{sup(5)}</p>
          <p>Es decir: el dato que todas las marcas ecológicas usan como argumento de venta no puede auditarse, porque la industria convencional no publica los números. Ese vacío regulatorio es, en sí mismo, el argumento más fuerte.</p>
        </div>

        <h2>La escala: de gramos a siglos</h2>

        <p>Dos gramos no impresionan a nadie. El problema aparece al multiplicar. Se estima que una persona puede usar del orden de diez mil toallas entre la menarquia y la menopausia, y que cada unidad tarda entre quinientos y ochocientos años en descomponerse en un relleno sanitario.{sup(4)} La revisión de fibras biodegradables de 2025 usa una cifra equivalente: hasta cinco siglos.{sup(2)} A eso se suma la huella de fabricación, estimada en unos diez gramos de gases de efecto invernadero por toalla producida.{sup(2)}</p>

        <figure class="figure">
          <img src="../assets/img/fig-degradacion.svg" alt="Gráfico comparativo: la fibra vegetal se degrada en 180 días bajo compostaje industrial; una toalla convencional con base de polietileno tarda entre 500 y 800 años" width="760" height="300" loading="lazy">
          <figcaption>La escala es logarítmica: cada marca del eje multiplica por diez. Umbral de 180 días según EN 13432 y ASTM D6400; estimación de 500 a 800 años según el Centre for Policy Studies del IIT Bombay.</figcaption>
        </figure>

        <p class="pull">Cada mes menstrúan más de dos mil millones de personas en el mundo. La aritmética se resuelve sola.{sup(6)}</p>

        <h2>Dónde está exactamente el plástico</h2>

        <p>No es una sola pieza. Está repartido en casi toda la estructura:</p>

        <ul>
          <li><strong>La lámina superior.</strong> Lo que muchas marcas llaman «capa de tela» suele ser una lámina plástica perforada, no un textil.{sup(4)}</li>
          <li><strong>El núcleo absorbente.</strong> Combina pulpa de madera con polímeros superabsorbentes, que son plástico en forma de gel.{sup(2)}</li>
          <li><strong>La base impermeable.</strong> Polietileno o similar. Es la pieza que garantiza que no traspase, y también la que resiste la degradación biológica.{sup(2)}</li>
          <li><strong>Alas, adhesivos y envoltorio.</strong> Cada envoltorio individual es una unidad más de plástico de un solo uso.{sup(4)}</li>
        </ul>

        <p>Vale la pena señalar algo que casi nunca se menciona: en el Reino Unido las toallas y tampones ni siquiera están clasificados como dispositivos médicos ni se venden estériles, de modo que buena parte de ese envoltorio individual no cumple una función sanitaria real.{sup(7)}</p>

        <h2>Qué cambia al sustituir la base</h2>

        <p>La pieza más estudiada como punto de sustitución es la lámina impermeable. Un análisis de ciclo de vida publicado en 2025 evaluó específicamente reemplazar el polietileno por ácido poliláctico —el PLA que se obtiene de almidón de maíz— en toallas sanitarias.{sup(8)} Es la misma decisión de diseño que tomamos en Aura, y la razón es simple: es la capa que más pesa en la persistencia del residuo y la que tiene un sustituto vegetal técnicamente maduro.</p>

        <p>El rendimiento no se desploma al hacerlo. Un ensayo que midió retención de líquido bajo carga de un kilogramo encontró que una toalla comercial de tamaño mediano retenía 33.50 gramos frente a 31.97 gramos de una biodegradable equivalente.{sup(2)} Hay diferencia, y sería deshonesto negarla, pero está lejos del abismo que sugiere el mercadeo de las marcas convencionales.</p>

        <h2>Qué conviene exigirle a una marca</h2>

        <p>Si una marca dice ser libre de plástico, la pregunta útil no es cuánto plástico tienen las demás. Es cuál es su propia lista de materiales, capa por capa, con proporciones. Esa información no está obligada a darla nadie{sup(5)}, y precisamente por eso separa a quien tiene la ficha técnica en la mano de quien solo tiene una historia.</p>
"""

A1_REFS = [
    'Chen, Y. et al. <em>Toward eco-friendly menstrual products: a comparative life cycle assessment of sanitary pads made from bamboo pulp vs. a conventional one.</em> Environmental Science and Pollution Research, 2025. <a href="https://link.springer.com/article/10.1007/s11356-025-36269-8" rel="noopener">link.springer.com/article/10.1007/s11356-025-36269-8</a>',
    '<em>Exploring biodegradable fibers as sustainable alternatives for sanitary napkin: A comprehensive review.</em> Environmental Development / ScienceDirect, 2025. <a href="https://www.sciencedirect.com/science/article/pii/S2352186425007217" rel="noopener">sciencedirect.com/science/article/pii/S2352186425007217</a>',
    'Natracare. <em>How Much Plastic is in Period Pads?</em> Estudio de composición sobre tres marcas comerciales. <a href="https://www.natracare.com/blog/how-much-plastic-in-period-pads/" rel="noopener">natracare.com/blog/how-much-plastic-in-period-pads</a>',
    'Ashank Desai Centre for Policy Studies, IIT Bombay. <em>Disposable Sanitary Napkins: A Case of Single Use Plastic?</em> <a href="https://www.cps.iitb.ac.in/disposable-sanitary-napkins-a-case-of-single-use-plastic/" rel="noopener">cps.iitb.ac.in</a>',
    'EU FactCheck. <em>Uncheckable: «Conventional menstrual pads are made up of 90% plastic materials».</em> <a href="https://eufactcheck.eu/factcheck/uncheckable-conventional-menstrual-pads-are-made-up-of-90-plastic-materials/" rel="noopener">eufactcheck.eu</a>',
    'ONU Mujeres. <em>Pobreza asociada a la menstruación: por qué millones de niñas y mujeres no pueden permitirse los productos menstruales.</em> <a href="https://www.unwomen.org/es/articulos/articulo-explicativo/pobreza-asociada-a-la-menstruacion-por-que-millones-de-ninas-y-mujeres-no-pueden-permitirse-los-productos-menstruales" rel="noopener">unwomen.org</a>',
    'Friends of the Earth. <em>Plastic periods: menstrual products and plastic pollution.</em> <a href="https://friendsoftheearth.uk/sustainable-living/plastic-periods-menstrual-products-and-plastic-pollution" rel="noopener">friendsoftheearth.uk</a>',
    '<em>Evaluation of the substitution of polyethylene for polylactic acid in sanitary pads through life cycle assessment.</em> IOPscience, 2025. <a href="https://iopscience.iop.org/article/10.1088/2977-3504/adbdd2" rel="noopener">iopscience.iop.org/article/10.1088/2977-3504/adbdd2</a>',
    'Verma, A. y Sambyal, S. Citado en Ashank Desai Centre for Policy Studies, IIT Bombay, 2018.',
    'Parthasarathy, P. et al. Estimación de emisiones por unidad producida, citada en la revisión de fibras biodegradables, 2022.',
    'Jeyakanthan, L. et al. Ensayos de retención de líquido en toallas comerciales y biodegradables, 2023. Citado en la revisión de ScienceDirect, ref. 2.',
]

# ==========================================================================
# ARTÍCULO 2 — química
# ==========================================================================

A2_BODY = f"""
        <p>En 2019, un equipo de la Universidad de Illinois en Urbana-Champaign compró once marcas de toallas sanitarias y cuatro de pañales desechables en Estados Unidos, Europa y Asia, y las analizó buscando cuatro ftalatos y tres compuestos orgánicos volátiles. No identificaron las marcas en la publicación. Los resultados fueron consistentes.</p>

        <p>Dos ftalatos —dibutil ftalato (DBP) y di-2-etilhexil ftalato (DEHP)— aparecieron en <strong>todas</strong> las marcas analizadas, tanto de toallas como de pañales. El xileno se detectó en las once marcas de toallas, el tolueno en nueve y el cloruro de metileno en dos.{sup(1, 2)}</p>

        <p>Los propios autores señalaron el motivo de su preocupación: dado que las toallas y los pañales permanecen en contacto directo con los genitales externos durante periodos prolongados, existe la probabilidad de que una cantidad considerable de estos compuestos se absorba.{sup(2)}</p>

        <h2>Un segundo estudio, más amplio</h2>

        <p>Al año siguiente, <em>Environment International</em> publicó un trabajo de Gao y Kannan que midió veinticuatro disruptores endocrinos —nueve ftalatos, seis parabenos, ocho bisfenoles y triclocarbán— en setenta y siete productos de higiene femenina recolectados en el estado de Nueva York.{sup(3)}</p>

        <p>Siete de esos compuestos aparecieron en la totalidad de las muestras de toallas, protectores diarios y tampones. Los protectores diarios registraron las concentraciones medianas más altas de varios ftalatos, con 393 ng/g de DBP y 386 ng/g de DEP, mientras que los tampones encabezaron en DEHP con 267 ng/g. Los autores concluyeron que las dosis estimadas de exposición por vía dérmica derivadas del uso de estos productos eran significativas al compararlas con otras fuentes conocidas.{sup(3)}</p>

        <p class="pull">La piel vulvar absorbe. Esa es la razón por la que la discusión sobre materiales en esta categoría no es equivalente a la de cualquier otro textil.</p>

        <h2>Los compuestos volátiles</h2>

        <p>Un análisis posterior sobre productos de higiene femenina vendidos en el mercado estadounidense encontró benceno en el 83 % de los productos recolectados, con un máximo de 3,604 ng/g, y 1,4-dioxano en el 50 %, con un máximo de 24,354 ng/g. Las concentraciones más altas de volátiles totales no estaban en las toallas, sino en jabones, aerosoles y polvos íntimos.{sup(4)}</p>

        <div class="callout">
          <span class="callout__label">El hallazgo que no favorece a nuestra propia categoría</span>
          <p>Ese mismo estudio encontró que los productos etiquetados como «orgánicos», «naturales» o «para piel sensible» <strong>no presentaban necesariamente concentraciones menores</strong> de compuestos orgánicos volátiles.{sup(4)}</p>
          <p>Lo publicamos porque es cierto y porque define exactamente el estándar que una marca como la nuestra debería cumplir: la etiqueta no es evidencia. Solo lo es un ensayo de laboratorio sobre el lote, y hasta que lo tengamos publicado, cualquier afirmación nuestra sobre este punto vale lo mismo que la de cualquiera.</p>
        </div>

        <h2>Lo que estos estudios no dicen</h2>

        <p>Aquí conviene frenar. Una revisión de políticas de la Brookings Institution advierte contra el salto lógico que va de «hay ftalatos, volátiles y metales pesados en los productos menstruales» a «los productos menstruales son tóxicos», por más razonable que parezca a primera vista.{sup(5)}</p>

        <p>Las preguntas que los estudios de contenido no responden son concretas: cuánto de esa carga química se absorbe realmente durante un periodo, cuánto a lo largo de una vida reproductiva, cuál es la fuerza de la asociación con desenlaces de salud, y cómo se compara con la exposición que ya recibimos por agua y alimentos.{sup(5)}</p>

        <p>Un trabajo de 2025 que evaluó emisiones volátiles, liberación de microplásticos y citotoxicidad en toallas comerciales encontró que, de diez compuestos volátiles buscados, solo el tolueno fue detectado, en concentraciones bajas —menos de 2.79 µg por toalla— y por debajo de los umbrales regulatorios.{sup(6)}</p>

        <h2>Entonces, ¿qué se puede afirmar con honestidad?</h2>

        <p>Tres cosas, y ninguna más:</p>

        <ol>
          <li>La presencia de ftalatos y compuestos volátiles en toallas convencionales está documentada de forma reproducible en varios estudios independientes, con distintas marcas y en distintos países.{sup(1, 3, 4)}</li>
          <li>La vía de exposición es plausible: la piel genital externa absorbe, y el contacto es prolongado y recurrente durante décadas.{sup(2, 3)}</li>
          <li>La magnitud del riesgo clínico para una persona concreta <strong>no está establecida</strong>, y las mediciones cuantitativas disponibles suelen quedar por debajo de los umbrales regulatorios.{sup(5, 6)}</li>
        </ol>

        <p>Una revisión sistemática publicada en 2023 en el <em>British Journal of Obstetrics and Gynaecology</em> analizó el contenido químico de los productos menstruales y encontró que las toallas convencionales pueden contener ftalatos, compuestos orgánicos volátiles, parabenos, fenoles ambientales, compuestos de fragancia y dioxinas, muchos de ellos clasificados como disruptores endocrinos.{sup(7)} Documentar la presencia y demostrar el daño son dos trabajos distintos, y el segundo sigue abierto.</p>

        <h2>Por qué esto igual cambia una decisión de diseño</h2>

        <p>Porque la mayoría de estos compuestos no está ahí por necesidad funcional. Los ftalatos se asocian al PVC flexible de las láminas de base{sup(8)}, las fragancias son un añadido de mercadeo, y las dioxinas son un subproducto del blanqueo con cloro.{sup(9)}</p>

        <p>Cuando una decisión tiene beneficio incierto y costo bajo, se toma. Aura no lleva perfume, ni colorante, ni blanqueo con cloro elemental, y sustituye la base plástica por PLA de almidón de maíz. No lo presentamos como una promesa de salud, porque la evidencia no autoriza esa promesa. Lo presentamos como lo que es: quitar de la fórmula aquello que no cumple ninguna función para vos.</p>

        <div class="callout">
          <span class="callout__label">Nota clínica</span>
          <p>Este artículo resume literatura publicada y no constituye asesoría médica. Si notás irritación, picazón, olor inusual o cambios en tu ciclo, consultá con personal de salud. Ningún producto de higiene sustituye una evaluación profesional.</p>
        </div>
"""

A2_REFS = [
    'Park, C.J. et al. <em>Sanitary pads and diapers contain higher phthalate contents than those in common commercial plastic products.</em> Reproductive Toxicology, 2019. Estudio sobre 11 marcas de toallas y 4 de pañales.',
    'Environmental Working Group. <em>Study: Elevated Levels of Toxic Chemicals Found in Menstrual Pads and Disposable Diapers.</em> <a href="https://www.ewg.org/news-insights/news/study-elevated-levels-toxic-chemicals-found-menstrual-pads-and-disposable" rel="noopener">ewg.org</a>',
    'Gao, C.-J. y Kannan, K. <em>Phthalates, bisphenols, parabens, and triclocarban in feminine hygiene products from the United States and their implications for human exposure.</em> Environment International, vol. 136, 2020. <a href="https://doaj.org/article/94d0eefaf7c34584bb4703e16f07d597" rel="noopener">doaj.org</a>',
    '<em>Volatile organic compounds in feminine hygiene products sold in the US market: A survey of products and health risks.</em> Environment International, 2020. <a href="https://www.sciencedirect.com/science/article/pii/S0160412020303494" rel="noopener">sciencedirect.com/science/article/pii/S0160412020303494</a>',
    'Brookings Institution. <em>Period products, health risks, and regulations.</em> <a href="https://www.brookings.edu/articles/period-products-health-risks-and-regulations/" rel="noopener">brookings.edu</a>',
    '<em>Safety assessment of commercial sanitary pads: Cytotoxicity, volatile organic compounds, and microplastics release.</em> Journal of Hazardous Materials, 2025. <a href="https://www.sciencedirect.com/science/article/abs/pii/S0304389425026214" rel="noopener">sciencedirect.com/science/article/abs/pii/S0304389425026214</a>',
    'Revisión sistemática sobre contenido químico de productos menstruales. British Journal of Obstetrics and Gynaecology (BJOG), 2023.',
    '<em>The presence of endocrine disrupting chemicals in sanitary pads.</em> Science of the Total Environment, 2026. <a href="https://www.sciencedirect.com/science/article/pii/S0048969726001701" rel="noopener">sciencedirect.com/science/article/pii/S0048969726001701</a>',
    'Mburu, A. y Kinyanjui, T. <em>Development of a highly absorbent and antibacterial biodegradable sanitary pad from bamboo.</em> 2013. Sobre dioxinas como subproducto del blanqueo con cloro.',
]

# ==========================================================================
# ARTÍCULO 3 — normas
# ==========================================================================

A3_BODY = f"""
        <p>Si un empaque dice «biodegradable» y nada más, la palabra no significa gran cosa. Prácticamente todo es biodegradable si se le da tiempo suficiente: la pregunta es cuánto, en qué condiciones y qué queda al final. Las normas existen precisamente para responder eso con números.</p>

        <h2>Qué exige EN 13432</h2>

        <p>La norma europea EN 13432 es el punto de referencia internacional más citado para envases y materiales compostables. Para cumplirla, un producto debe superar cuatro pruebas, no una:{sup(1, 2)}</p>

        <ul>
          <li><strong>Biodegradación.</strong> Al menos el 90 % del carbono orgánico debe convertirse en CO₂ en un máximo de 180 días bajo condiciones de compostaje industrial.</li>
          <li><strong>Desintegración.</strong> Tras doce semanas, menos del 10 % de la masa original puede quedar en fragmentos mayores a 2 mm.</li>
          <li><strong>Ecotoxicidad.</strong> El compost resultante debe permitir el crecimiento vegetal. Se evalúa con ensayos de germinación y biomasa.</li>
          <li><strong>Metales pesados.</strong> Límites estrictos para plomo, cadmio, mercurio y otros.</li>
        </ul>

        <p>La norma estadounidense equivalente es ASTM D6400: exige también un 90 % de conversión del carbono orgánico a CO₂ en 180 días y desintegración a 84 días, con umbrales de metales pesados alineados a la EPA.{sup(3, 4)} La australiana AS 4736 se considera la más exigente de las tres, porque suma un ensayo de toxicidad con lombrices.{sup(1)}</p>

        <div class="callout">
          <span class="callout__label">El detalle que cambia todo</span>
          <p>Estas normas describen <strong>compostaje industrial</strong>, no doméstico. Requieren temperaturas sostenidas de entre 55 y 60 °C, que una compostera de patio no alcanza.{sup(4, 5)}</p>
          <p>Y, sobre todo: cumplir ASTM D6400 <strong>no significa que el producto se degrade en un relleno sanitario</strong>.{sup(6)} Un relleno compacta la basura y la priva de oxígeno; ahí, un material compostable puede permanecer mucho más tiempo del que sugiere su certificado.</p>
        </div>

        <h2>Biodegradable, compostable, oxodegradable</h2>

        <h3>Biodegradable</h3>
        <p>Significa que microorganismos pueden descomponer el material. Sin un plazo ni una condición especificados, no dice nada útil. Las Green Guides de la Comisión Federal de Comercio de Estados Unidos consideran engañoso usar el término sin evidencia de ensayo específica, y señalan a ASTM D6400 como la prueba reconocida.{sup(4)}</p>

        <h3>Compostable</h3>
        <p>Significa que el material se degrada dentro de un plazo definido, en condiciones definidas, y deja un compost que no daña a las plantas. Es una afirmación verificable porque hay un ensayo detrás.{sup(1, 2)}</p>

        <h3>Certificado</h3>
        <p>Significa que un tercero independiente ejecutó ese ensayo. ASTM D6400 es la norma; BPI es el organismo que certifica en Estados Unidos y Canadá, y TÜV Austria o DIN CERTCO en Europa.{sup(4, 7)} La certificación exige divulgación completa de la formulación, incluyendo aditivos, tintas y adhesivos, y el certificado se emite con un código de trazabilidad único, con vigencia de cinco años.{sup(7)}</p>

        <p class="pull">La diferencia entre «cumple la norma» y «está certificado» es la diferencia entre decir que aprobaste el examen y mostrar el diploma.</p>

        <h2>Cómo leer un empaque sin dejarse llevar</h2>

        <p>Cuatro preguntas resuelven casi cualquier caso:</p>

        <ol>
          <li><strong>¿Dice una norma o solo un adjetivo?</strong> «Biodegradable» sin EN 13432 ni ASTM D6400 al lado es publicidad, no información.{sup(4)}</li>
          <li><strong>¿Dice bajo qué condiciones?</strong> Si no distingue entre compostaje industrial y doméstico, está omitiendo el dato decisivo.{sup(5)}</li>
          <li><strong>¿Hay un código de certificado verificable?</strong> Los productos certificados aparecen en registros públicos consultables.{sup(4)}</li>
          <li><strong>¿A qué se refiere la afirmación?</strong> A veces solo la caja exterior es compostable, no el producto ni el envoltorio individual.</li>
        </ol>

        <h2>Dónde está Aura hoy</h2>

        <p>Aura está en proceso de certificación de compostabilidad industrial. Todavía no tenemos el certificado con código de trazabilidad, y por eso no vas a encontrar un sello en nuestro empaque ni la palabra «certificado» en este sitio. Sería exactamente el tipo de afirmación que las guías de publicidad ambiental consideran engañosa.{sup(4)}</p>

        <p>Lo que sí podemos afirmar y sostener con la ficha técnica: la base impermeable es PLA derivado de almidón de maíz en lugar de polietileno, el núcleo es celulosa de pulpa certificada, y la superficie es bambú hilado. Ninguno de esos materiales es plástico de origen fósil. Cuando el certificado exista, vas a poder verificar su número en el registro del organismo, no en nuestra palabra.</p>

        <h2>Y si en tu ciudad no hay compostaje industrial</h2>

        <p>Es el caso de la mayor parte de Honduras, y conviene decirlo sin adornos. Si tu toalla termina en el relleno sanitario municipal, no se va a degradar en 180 días.</p>

        <p>Lo que sí cambia es la cantidad de material persistente que dejás. Una toalla convencional aporta alrededor de 2.4 gramos de plástico de origen fósil, diseñado para resistir la degradación biológica durante siglos.{sup(8)} Una toalla de fibra vegetal aporta fibra vegetal. En un relleno sanitario ambas tardan más de lo deseable; la diferencia es qué queda cuando el tiempo pasa, y si ese residuo aporta microplásticos al suelo o materia orgánica.</p>
"""

A3_REFS = [
    'Nature at Work Packaging. <em>Biodegradability — EN 13432, ASTM D6400, AS 4736.</em> <a href="https://www.nawp.com.au/renewable-nature-based-sourcing/biodegradability-en-13432-astm-d6400-as4736/" rel="noopener">nawp.com.au</a>',
    'CEN. <em>EN 13432: Packaging — Requirements for packaging recoverable through composting and biodegradation.</em> Norma armonizada europea.',
    'ASTM International. <em>ASTM D6400: Standard Specification for Labeling of Plastics Designed to be Aerobically Composted in Municipal or Industrial Facilities.</em>',
    'Ecofy. <em>ASTM D6400 Compostability Standard: U.S. Buyer\u2019s Guide.</em> Incluye referencia a las Green Guides de la FTC. <a href="https://ecofy.io/resources/compliance/astm-d6400/" rel="noopener">ecofy.io/resources/compliance/astm-d6400</a>',
    '<em>ASTM D6400: Compostable Packaging Standards Explained.</em> Sobre el requisito de 55–60 °C y la inviabilidad del compostaje doméstico. <a href="https://mysupplyclub.com/blog/astm-d6400-compostability-standards-explained" rel="noopener">mysupplyclub.com</a>',
    'Orizon. <em>ASTM D6400 Certification Guide.</em> Sobre por qué la certificación no implica degradación en relleno sanitario. <a href="https://orizonbags.com/astm-d6400-compostable-standard/" rel="noopener">orizonbags.com</a>',
    'UKHI. <em>EN 13432 Compostable Packaging Guide.</em> Sobre proceso de certificación, código de trazabilidad y vigencia. <a href="https://ukhi.com/en-13432-explained-for-exporters-compostable-packaging-standard-guide-ukhi/" rel="noopener">ukhi.com</a>',
    'Natracare. <em>How Much Plastic is in Period Pads?</em> <a href="https://www.natracare.com/blog/how-much-plastic-in-period-pads/" rel="noopener">natracare.com</a>',
]

# ==========================================================================
# ARTÍCULO 4 — pobreza menstrual
# ==========================================================================

A4_BODY = f"""
        <p>Cada mes menstrúan más de dos mil millones de personas en el mundo. Millones de ellas no pueden pagar los productos necesarios para gestionarlo, ni tienen acceso a agua y saneamiento seguros para hacerlo con dignidad.{sup(1)} A esa combinación se le llama pobreza menstrual, y no es un problema de higiene: es un problema de acceso.</p>

        <h2>La cifra que ordena la conversación</h2>

        <p>ONU Mujeres América Latina y el Caribe, citando datos de la Organización Mundial de la Salud, señala que en la región <strong>dos de cada cinco niñas faltan a la escuela durante su menstruación</strong>, un ausentismo agravado por el estigma que rodea el tema.{sup(2)}</p>

        <p>Otras mediciones llegan a órdenes similares por caminos distintos. Un comunicado de AIDS Healthcare Foundation de 2024 estima que una de cada tres adolescentes en América Latina falta a clases de manera regular por no contar con lo necesario: agua limpia, ropa interior adecuada y toallas, tampones o copas.{sup(3)} La UNESCO, con alcance global, calcula que una de cada diez jóvenes en edad menstrual pierde días de clase por falta de acceso a recursos menstruales.{sup(4)}</p>

        <p class="pull">Faltar tres o cuatro días al mes, mes tras mes, no es una molestia. Es una fracción del año escolar que no se recupera.</p>

        <h2>El estigma también cuesta</h2>

        <p>Un estudio de Plan International encontró que el 35 % de las adolescentes y jóvenes a nivel mundial considera que la menstruación debe mantenerse en secreto, por tratarse de un asunto privado o vergonzoso.{sup(3)}</p>

        <p>Ese silencio tiene consecuencias materiales concretas. La falta de información y de infraestructura sanitaria empuja a recurrir a soluciones improvisadas —trapos, papel, materiales no diseñados para el uso— que aumentan el riesgo de infección y agravan el impacto emocional del ciclo.{sup(5)}</p>

        <h2>Qué han hecho otros países de la región</h2>

        <p>La política pública en América Latina se ha movido en tres frentes distintos:{sup(6)}</p>

        <ul>
          <li><strong>Impuestos.</strong> Colombia eliminó en 2018 el impuesto sobre las toallas sanitarias. México siguió en 2021, cuando el movimiento Menstruación Digna logró retirar el 16 % de IVA a los productos de gestión menstrual.</li>
          <li><strong>Distribución directa.</strong> Uruguay lanzó en 2023 el programa Gestión Menstrual + Igualdad + Inclusión para repartir kits gratuitos en Montevideo. Brasil anunció distribución gratuita de toallas en farmacias de todo el país para mujeres de bajos recursos.</li>
          <li><strong>Datos.</strong> México levantó una Encuesta Nacional sobre Gestión Menstrual junto con UNICEF, Essity y Menstruación Digna, cubriendo personas menstruantes de 12 a 70 años.{sup(3)}</li>
        </ul>

        <p>La secuencia importa: primero medir, después legislar. Sin la encuesta, el debate se queda en anécdotas.</p>

        <h2>Dónde queda Honduras</h2>

        <p>Honduras no aparece entre los países con una política pública articulada sobre gestión menstrual, ni con una encuesta nacional que permita dimensionar el problema con datos propios. Esa ausencia de información es, en sí misma, un dato.</p>

        <p>Aura es una empresa, no una organización de incidencia, y sería deshonesto presentar la venta de un producto como una solución a un problema estructural. Un producto de mejor material no resuelve la pobreza menstrual: en el corto plazo, un producto más caro puede incluso alejarse de quien más lo necesita.</p>

        <h2>Lo que sí nos corresponde</h2>

        <p>Tres compromisos concretos, que se pueden verificar:</p>

        <ol>
          <li><strong>Precio por unidad visible.</strong> Impreso en cada empaque, para que puedas comparar contra cualquier marca sin hacer cuentas. Los productos «premium» suelen esconder el costo real detrás del tamaño del paquete.</li>
          <li><strong>Contenido abierto.</strong> Los artículos de este sitio, incluidas sus referencias, se pueden reproducir libremente con atribución para uso educativo. Si sos docente o trabajás en salud comunitaria, usalos.</li>
          <li><strong>Precio de costo para programas escolares.</strong> Vendemos sin margen a instituciones educativas y organizaciones que distribuyan gratuitamente en Honduras. No es filantropía; es la condición mínima para tener derecho a hablar del tema.</li>
        </ol>

        <div class="callout">
          <span class="callout__label">Si trabajás en esto</span>
          <p>Escribinos a <a href="mailto:hola@aura.hn">hola@aura.hn</a> con el nombre de la institución y el número aproximado de participantes. No pedimos exclusividad, ni logo, ni fotos.</p>
        </div>
"""

A4_REFS = [
    'ONU Mujeres. <em>Pobreza asociada a la menstruación: por qué millones de niñas y mujeres no pueden permitirse los productos menstruales.</em> <a href="https://www.unwomen.org/es/articulos/articulo-explicativo/pobreza-asociada-a-la-menstruacion-por-que-millones-de-ninas-y-mujeres-no-pueden-permitirse-los-productos-menstruales" rel="noopener">unwomen.org</a>',
    'ONU Mujeres América Latina y el Caribe, citando datos de la OMS. <em>La pobreza menstrual en América Latina.</em>',
    'AIDS Healthcare Foundation México. <em>28 de mayo, Día de la Salud e Higiene Menstrual.</em> 2024. <a href="https://ahfmexico.org.mx/28-de-mayo-dia-de-la-salud-e-higiene-menstrual-la-pobreza-menstrual/" rel="noopener">ahfmexico.org.mx</a>',
    'UNESCO, citada en <em>Pobreza menstrual: el impacto de la falta de recursos en la salud menstrual y la necesidad de apoyo legislativo y educación en América Latina.</em>',
    'CEERI Global. <em>La lucha contra la pobreza menstrual: un vistazo a América Latina.</em> <a href="https://www.ceeriglobal.org/wp-content/uploads/2023/03/La-lucha-contra-la-pobreza-menstrual_Informe.docx.pdf" rel="noopener">ceeriglobal.org</a>',
    'Voices! Consultancy. <em>Desigualdades íntimas: la pobreza menstrual en América Latina.</em> <a href="https://www.voicesconsultancy.com/Prensa/Desigualdades-intimas-la-pobreza-menstrual-en-America-Latina" rel="noopener">voicesconsultancy.com</a>',
    'UNICEF México, Essity y Menstruación Digna México. <em>Encuesta Nacional sobre Gestión Menstrual.</em>',
]

# ==========================================================================
# Ensamblado
# ==========================================================================

REL = {
    "plastico": ("RESIDUOS", "Cuánto plástico hay realmente en una toalla sanitaria", "plastico-en-toallas-sanitarias.html"),
    "quimicos": ("SALUD", "Qué encontraron los laboratorios en las toallas convencionales", "quimicos-en-productos-menstruales.html"),
    "normas": ("NORMATIVA", "Biodegradable y compostable no significan lo mismo", "biodegradable-o-compostable.html"),
    "pobreza": ("CONTEXTO", "Pobreza menstrual: el costo de no poder elegir", "pobreza-menstrual-america-latina.html"),
}

ARTICLES = [
    dict(
        slug="plastico-en-toallas-sanitarias.html",
        kicker="RESIDUOS",
        title="Cuánto plástico hay realmente en una toalla sanitaria",
        dek="El dato del noventa por ciento se repite en todas partes. Fuimos a buscar de dónde salió, qué lo respalda y por qué es más difícil de verificar de lo que parece.",
        desc="Revisión de la evidencia sobre contenido plástico en toallas sanitarias convencionales: qué dicen los análisis de ciclo de vida, los estudios de composición y por qué la cifra del 90 % es difícil de auditar.",
        author="Equipo Aura", date="Actualizado en agosto de 2026", read="8 min",
        body=A1_BODY, refs=A1_REFS,
        related=[REL["quimicos"], REL["normas"], REL["pobreza"]],
    ),
    dict(
        slug="quimicos-en-productos-menstruales.html",
        kicker="SALUD",
        title="Qué encontraron los laboratorios en las toallas convencionales",
        dek="Ftalatos en el cien por ciento de las marcas analizadas. También lo que casi ninguna marca ecológica menciona: los productos etiquetados como naturales no salieron necesariamente mejor.",
        desc="Qué detectaron los estudios de Park (2019), Gao y Kannan (2020) y trabajos posteriores en toallas sanitarias, y qué límites tiene esa evidencia según la revisión de Brookings.",
        author="Equipo Aura", date="Actualizado en agosto de 2026", read="10 min",
        body=A2_BODY, refs=A2_REFS,
        related=[REL["plastico"], REL["normas"], REL["pobreza"]],
    ),
    dict(
        slug="biodegradable-o-compostable.html",
        kicker="NORMATIVA",
        title="Biodegradable y compostable no significan lo mismo",
        dek="Qué exigen exactamente EN 13432 y ASTM D6400, por qué una toalla compostable no se degrada en un relleno sanitario, y qué palabra deberías desconfiar en cualquier empaque.",
        desc="Guía sobre las normas EN 13432, ASTM D6400 y AS 4736: requisitos de biodegradación, desintegración, ecotoxicidad y metales pesados, y cómo leer una afirmación ambiental en un empaque.",
        author="Equipo Aura", date="Actualizado en agosto de 2026", read="9 min",
        body=A3_BODY, refs=A3_REFS,
        related=[REL["plastico"], REL["quimicos"], REL["pobreza"]],
    ),
    dict(
        slug="pobreza-menstrual-america-latina.html",
        kicker="CONTEXTO",
        title="Pobreza menstrual: el costo de no poder elegir",
        dek="Dos de cada cinco niñas de la región faltan a clases durante su periodo. Qué han hecho México, Colombia y Uruguay al respecto, y dónde queda Honduras en esa conversación.",
        desc="Datos de ONU Mujeres, UNESCO y AHF sobre pobreza menstrual en América Latina, políticas públicas de la región y el papel que le corresponde a una marca privada.",
        author="Equipo Aura", date="Actualizado en agosto de 2026", read="7 min",
        body=A4_BODY, refs=A4_REFS,
        related=[REL["plastico"], REL["quimicos"], REL["normas"]],
    ),
]


def build_articles():
    for a in ARTICLES:
        body = article(
            a["kicker"], a["title"], a["dek"], a["author"], a["date"],
            a["read"], a["body"], a["refs"], a["related"],
        )
        render(
            "articulos/" + a["slug"],
            a["title"] + " — Aura",
            a["desc"],
            body,
            depth=1, active="sci", ogtype="article", progress=True,
        )


if __name__ == "__main__":
    build_articles()
