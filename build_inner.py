#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Genera blog.html, producto.html y marca.html."""

from build_pages import render

# ==========================================================================
# BLOG — índice de artículos
# ==========================================================================

POSTS = [
    ("LANZAMIENTO", "Aura llega a Honduras, y solo a catorce lugares",
     "Una toalla sanitaria de fibra vegetal que sale a la venta el 1 de septiembre sin pasar por el supermercado. La decisión de canal es deliberada, y explicarla es parte del producto.",
     "articulos/lanzamiento-aura-honduras.html", "9 MIN · 6 REFERENCIAS"),
    ("MERCADEO", "Greenwashing: el 53 % de las promesas verdes no resiste una revisión",
     "La Comisión Europea auditó las afirmaciones ambientales del mercado y encontró que más de la mitad eran vagas o infundadas. Qué significa eso para una marca que sí invirtió en cambiar su producto.",
     "articulos/greenwashing-marketing-verde.html", "9 MIN · 8 REFERENCIAS"),
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
    f'''      <a class="post-card" href="{h}">
        <span class="post-card__kicker">{k}</span>
        <h3 class="post-card__title">{t}</h3>
        <p class="post-card__dek">{d}</p>
        <span class="post-card__meta">{m}</span>
      </a>''' for k, t, d, h, m in POSTS
)

BLOG = f"""
  <section class="band band--tight">
    <div class="wrap" style="max-width:780px">
      <p class="eyebrow">Blog</p>
      <h1 class="display-xl" style="margin-bottom:var(--s5)">Con la fuente<br>a la vista.</h1>
      <p class="lede">Seis artículos sobre materiales, química, normativa y comunicación ambiental en la categoría de higiene menstrual. Cada afirmación está enlazada al estudio que la respalda. Donde la evidencia es débil o contradice nuestro propio argumento comercial, también lo decimos.</p>
    </div>
  </section>

  <section class="band--light" style="padding-top:var(--s7)">
    <div class="wrap" style="margin-bottom:var(--s6)">
      <p class="eyebrow">Seis artículos · 49 referencias</p>
    </div>
    <div class="post-grid">
{cards}
    </div>
  </section>

  <section class="band band--light" id="metodo">
    <div class="wrap" style="max-width:780px">
      <p class="eyebrow">Método editorial</p>
      <h2 class="display-l" style="margin-bottom:var(--s6)">Cinco reglas que nos<br>pusimos al escribir esto.</h2>

      <div class="faq">
        <details open>
          <summary>Priorizamos literatura revisada por pares</summary>
          <p>Cuando existe un estudio publicado en una revista con revisión por pares, esa es la fuente. Los informes de organizaciones y las notas de prensa se usan solo para contexto o cuando no hay literatura académica disponible, y quedan identificados como tales en la lista de referencias.</p>
        </details>
        <details>
          <summary>Publicamos los datos que nos contradicen</summary>
          <p>El estudio sobre compuestos volátiles en el mercado estadounidense encontró que los productos etiquetados como orgánicos o naturales no presentaban necesariamente concentraciones menores. Está citado en el artículo sobre química con esa conclusión textual, porque omitirlo sería exactamente la práctica que criticamos en el resto de la industria.</p>
        </details>
        <details>
          <summary>Separamos «se detectó» de «causa daño»</summary>
          <p>Que un compuesto esté presente en un producto no equivale a que produzca un efecto en salud. Es una distinción que la publicidad de productos naturales borra con frecuencia. En estos artículos, la presencia documentada y el riesgo demostrado se tratan como dos afirmaciones distintas, porque lo son.</p>
        </details>
        <details>
          <summary>No usamos sellos que no tenemos</summary>
          <p>Aura está en proceso de certificación de compostabilidad industrial. Hasta que exista un certificado con código de trazabilidad verificable en el registro del organismo emisor, no vas a ver un sello en el empaque ni la palabra «certificado» en este sitio.</p>
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
      <div style="max-width:42ch">
        <h2 class="display-m" style="margin-bottom:var(--s3)">Uso libre para fines educativos.</h2>
        <p style="margin:0;opacity:.85;font-family:var(--read)">Si sos docente o trabajás en salud comunitaria, podés reproducir estos textos con atribución. No hace falta pedir permiso.</p>
      </div>
      <a class="btn btn--solid" href="mailto:hola@aura.hn">Escribinos</a>
    </div>
  </section>
"""

render("blog.html", "Blog — Aura",
       "Seis artículos con referencias sobre plástico en toallas sanitarias, química de productos menstruales, normas de compostabilidad, greenwashing y pobreza menstrual.",
       BLOG, depth=0, active="sci")

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
    trs = "\n".join(f'            <tr><th scope="row">{k}</th><td class="num">{v}</td></tr>' for k, v in rows)
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
        <div style="display:flex;align-items:baseline;gap:var(--s4);flex-wrap:wrap">
          <span class="display-m" style="color:var(--halo)">{price}</span>
          <span class="data" style="color:var(--paper-soft)">{unit} · precio único en todos los puntos</span>
        </div>
      </div>
    </div>""")

PUNTOS = [
    ("San Pedro Sula", 5, ["Farmacia — Barrio Río de Piedras", "Farmacia — Col. Trejo",
                           "Tienda naturista — Av. Circunvalación", "Farmacia — Barrio Guamilito",
                           "Tienda naturista — Col. Jardines del Valle"]),
    ("Tegucigalpa", 5, ["Farmacia — Col. Palmira", "Tienda naturista — Col. Lomas del Guijarro",
                        "Farmacia — Barrio La Granja", "Farmacia — Col. Kennedy",
                        "Tienda naturista — Col. Miraflores"]),
    ("Puerto Cortés", 2, ["Farmacia — Barrio El Centro", "Tienda naturista — Barrio Medina"]),
    ("La Ceiba", 2, ["Farmacia — Barrio El Iman", "Tienda naturista — Zona Viva"]),
]

pts = "\n".join(f"""
        <div style="border:1px solid var(--void-3);border-radius:var(--radius);padding:var(--s5);background:var(--void)">
          <div style="display:flex;align-items:baseline;justify-content:space-between;gap:var(--s3);padding-bottom:var(--s3);margin-bottom:var(--s4);border-bottom:1px solid var(--void-3)">
            <h3 style="font-family:var(--display);font-size:1.25rem">{c}</h3>
            <span class="data" style="color:var(--halo);flex:none">{n} PUNTOS</span>
          </div>
          <ul style="list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:var(--s3)">
            {"".join(f'<li style="font-size:.875rem;color:var(--paper-soft)">{p}</li>' for p in lst)}
          </ul>
        </div>""" for c, n, lst in PUNTOS)

PROD = f"""
  <section class="band band--tight">
    <div class="wrap" style="max-width:780px">
      <p class="eyebrow">Producto</p>
      <h1 class="display-xl" style="margin-bottom:var(--s5)">Tres formatos.<br>Un solo estándar.</h1>
      <p class="lede">Cambia el largo y cambia la superficie de retención. No cambia la lista de materiales: bambú hilado en la superficie, celulosa de pulpa certificada en el núcleo, base de PLA derivado de almidón de maíz. Sin perfume, sin colorante, sin cloro elemental, sin látex.</p>
    </div>
  </section>

  <section class="prod-spec">
{''.join(blocks)}
  </section>

  <section class="band band--void-2" id="puntos">
    <div class="wrap">
      <div style="max-width:660px;margin-bottom:var(--s7)">
        <p class="eyebrow">Distribución exclusiva</p>
        <h2 class="display-l" style="margin-bottom:var(--s4)">Catorce puntos.<br>Ni uno más, por ahora.</h2>
        <p class="lede">Aura no se vende en supermercados. Cada punto de esta lista firmó un acuerdo de exclusividad recíproca, recibió capacitación sobre la composición del producto y sostiene el mismo precio publicado. Si un local no aparece acá, no es un punto autorizado.</p>
        <p style="margin-top:var(--s5)"><a class="btn btn--ghost" href="articulos/lanzamiento-aura-honduras.html">Por qué elegimos este canal</a></p>
      </div>

      <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:var(--s5);align-items:start">
{pts}
      </div>

      <p style="margin-top:var(--s6);font-family:var(--mono);font-size:.75rem;color:var(--paper-soft);max-width:64ch">
        Las direcciones completas se publican el 1 de septiembre. La lista se actualiza cada vez que cambia, con la fecha del último cambio al pie.
      </p>
    </div>
  </section>

  <section class="band band--light">
    <div class="wrap" style="max-width:820px">
      <p class="eyebrow">Preguntas</p>
      <h2 class="display-l" style="margin-bottom:var(--s7)">Lo que conviene que sepas.</h2>

      <div class="faq">
        <details open>
          <summary>¿Por qué no está en el supermercado?</summary>
          <p>Porque el argumento del producto es una tabla de composición con siete componentes, y eso no se comunica en el segundo y medio que dura una decisión frente a la góndola. La distribución exclusiva permite que quien vende el producto sepa qué está vendiendo.</p>
          <p>También protege el precio: el acuerdo fija una política única en los catorce puntos, así que cuesta lo mismo en Puerto Cortés que en Tegucigalpa.</p>
        </details>
        <details>
          <summary>¿Absorbe igual que una toalla con gel?</summary>
          <p>Un estudio comparativo midió la retención de líquido de toallas comerciales frente a biodegradables bajo carga de un kilogramo. En tamaño mediano, la comercial retuvo 33.50 g y la biodegradable 31.97 g. La diferencia existe, pero es menor a la que sugiere la publicidad.</p>
          <p>Donde sí notás el cambio es en la sensación: sin polímero superabsorbente, la superficie se percibe más textil y menos plastificada.</p>
        </details>
        <details>
          <summary>¿Puedo compostarla en casa?</summary>
          <p>No, y conviene decirlo claro. La base de PLA necesita temperaturas sostenidas de entre 55 y 60 °C, y una compostera doméstica no las alcanza. Las normas EN 13432 y ASTM D6400 se refieren a compostaje industrial.</p>
          <p>Lo explicamos con detalle en <a href="articulos/biodegradable-o-compostable.html">el artículo sobre normas de compostaje</a>.</p>
        </details>
        <details>
          <summary>¿Es hipoalergénica?</summary>
          <p>Aura no lleva perfume, colorante, látex ni blanqueo con cloro elemental, que son los cuatro desencadenantes más frecuentes de irritación por contacto en esta categoría. Eso reduce el riesgo, pero ninguna marca seria puede garantizar que un producto no cause reacción en ninguna persona.</p>
          <p>Si tenés dermatitis diagnosticada o antecedentes de reacción a productos de higiene, consultalo con tu médico antes de cambiar.</p>
        </details>
        <details>
          <summary>¿Tienen certificación de compostabilidad?</summary>
          <p>Estamos en proceso. Mientras no tengamos el certificado con código de trazabilidad en mano, no vamos a usar el sello ni la palabra «certificado», porque las guías de publicidad ambiental consideran engañoso llamar biodegradable a un producto sin evidencia de ensayo específica.</p>
          <p>Cuando lo tengamos, vas a poder verificar el número en el registro del organismo certificador, no en nuestra palabra.</p>
        </details>
      </div>
    </div>
  </section>
"""

render("producto.html", "Producto — Aura",
       "Fichas técnicas de Aura Día, Noche y Diario, y los catorce puntos de venta exclusivos donde se consigue la marca en Honduras.",
       PROD, depth=0, active="prod")

# ==========================================================================
# MARCA — estrategia
# ==========================================================================

VOZ = [
    ("«Composición completa publicada: 7 componentes, % en peso»", "«100 % natural»"),
    ("«En proceso de certificación EN 13432»", "«Certificado ecológico»"),
    ("«Los estudios detectaron ftalatos; el daño no está establecido»", "«Libre de tóxicos»"),
    ("«Catorce puntos de venta»", "«Disponible en puntos seleccionados»"),
    ("«Cuesta más porque la fibra cuesta más»", "«Invertí en vos misma»"),
]

voz_rows = "\n".join(
    f'''            <tr>
              <th scope="row" style="font-weight:400">{a}</th>
              <td>{b}</td>
            </tr>''' for a, b in VOZ
)

MIX = [
    ("Producto", "Toalla de fibra vegetal en tres formatos. El atributo diferencial no es el desempeño, es la trazabilidad de materiales."),
    ("Precio", "Superior a la categoría, sostenido por costo real de insumo. Precio único publicado, sin descuentos por punto."),
    ("Plaza", "Distribución exclusiva. Catorce puntos, exclusividad recíproca, capacitación obligatoria del punto de venta."),
    ("Promoción", "Mercadeo de contenidos. El blog es el canal principal: seis artículos con 49 referencias verificables, en lugar de pauta de alcance."),
]

mix_rows = "\n".join(
    f'''            <tr>
              <th scope="row">{k}</th>
              <td>{v}</td>
            </tr>''' for k, v in MIX
)

MARCA = f"""
  <section class="band band--tight">
    <div class="wrap" style="max-width:780px">
      <p class="eyebrow">Estrategia de marca</p>
      <h1 class="display-xl" style="margin-bottom:var(--s5)">Las decisiones<br>detrás del sitio.</h1>
      <p class="lede">Esta página documenta el razonamiento de mercadeo que sostiene todo lo demás: a quién le hablamos, qué posición ocupamos, por qué elegimos un canal exclusivo y qué reglas de lenguaje seguimos. Está publicada a propósito, porque una marca cuyo argumento es la transparencia no puede esconder su propia estrategia.</p>
    </div>
  </section>

  <section class="band band--light">
    <div class="wrap" style="max-width:820px">
      <p class="eyebrow">Posicionamiento</p>
      <h2 class="display-l" style="margin-bottom:var(--s5)">Un enunciado, cuatro consecuencias.</h2>
      <div class="pull" style="margin-top:0">
        Para mujeres de zonas urbanas de Honduras que ya cuestionan lo que consumen, Aura es la toalla sanitaria que publica su composición completa, porque en una categoría donde la mitad de las etiquetas verdes no verifica nada, el dato contrastable es la única diferencia que la competencia no puede copiar sin pagar el mismo costo.
      </div>
      <p style="margin-top:var(--s6)">El enunciado obliga a cuatro cosas, y cada una tiene una consecuencia operativa visible en el sitio:</p>
      <ol style="font-family:var(--read);font-size:1.0625rem;line-height:1.7;padding-left:1.3em">
        <li style="margin-bottom:var(--s3)">Publicar la tabla de composición con porcentajes, aunque nadie lo exija.</li>
        <li style="margin-bottom:var(--s3)">No usar sellos ni la palabra «certificado» hasta tener el código de trazabilidad.</li>
        <li style="margin-bottom:var(--s3)">Citar los estudios que nos contradicen dentro de nuestros propios artículos.</li>
        <li>Elegir un canal donde el dato se pueda explicar, aunque cueste cobertura.</li>
      </ol>
    </div>
  </section>

  <section class="band">
    <div class="wrap">
      <div style="max-width:620px;margin-bottom:var(--s7)">
        <p class="eyebrow">Segmento</p>
        <h2 class="display-l">A quién le habla<br>este blog.</h2>
      </div>

      <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:var(--s5)">
        <div style="border:1px solid var(--void-3);border-radius:var(--radius-lg);padding:var(--s6);background:var(--void-2)">
          <span class="data" style="color:var(--halo)">SEGMENTO PRIMARIO</span>
          <h3 style="font-family:var(--display);font-size:1.5rem;margin:var(--s3) 0 var(--s4)">La que ya lee etiquetas</h3>
          <p style="font-size:.9375rem;color:var(--paper-soft)">Mujer de 24 a 38 años, urbana, con ingreso propio. Ya cambió otros productos de su rutina por versiones sin fragancia o sin ciertos ingredientes. Desconfía de la palabra «natural» porque la vio usada en demasiadas cosas.</p>
          <p style="font-size:.9375rem;color:var(--paper-soft);margin:0"><strong style="color:var(--pulp)">Qué la mueve:</strong> poder verificar. No busca que le prometan, busca poder comprobar.</p>
        </div>

        <div style="border:1px solid var(--void-3);border-radius:var(--radius-lg);padding:var(--s6);background:var(--void-2)">
          <span class="data" style="color:var(--halo)">SEGMENTO SECUNDARIO</span>
          <h3 style="font-family:var(--display);font-size:1.5rem;margin:var(--s3) 0 var(--s4)">La que tuvo irritación</h3>
          <p style="font-size:.9375rem;color:var(--paper-soft)">Mujer de cualquier edad con antecedente de molestia recurrente con toallas convencionales. Llega buscando una alternativa concreta, no un discurso ambiental.</p>
          <p style="font-size:.9375rem;color:var(--paper-soft);margin:0"><strong style="color:var(--pulp)">Qué la mueve:</strong> una lista clara de lo que el producto no lleva. Es el segmento con el que hay que ser más cuidadoso al hablar de salud.</p>
        </div>

        <div style="border:1px solid var(--void-3);border-radius:var(--radius-lg);padding:var(--s6);background:var(--void-2)">
          <span class="data" style="color:var(--halo)">INFLUENCIA</span>
          <h3 style="font-family:var(--display);font-size:1.5rem;margin:var(--s3) 0 var(--s4)">El punto de venta</h3>
          <p style="font-size:.9375rem;color:var(--paper-soft)">En farmacias y tiendas naturistas de Honduras, la recomendación de mostrador pesa más que cualquier empaque. En distribución exclusiva ese actor deja de ser un intermediario y pasa a ser parte del mensaje.</p>
          <p style="font-size:.9375rem;color:var(--paper-soft);margin:0"><strong style="color:var(--pulp)">Qué lo mueve:</strong> margen superior, protección territorial y saber explicar el producto sin equivocarse.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="band band--light-2">
    <div class="wrap" style="max-width:900px">
      <p class="eyebrow">Estrategia de canal</p>
      <h2 class="display-l" style="margin-bottom:var(--s5)">Por qué exclusiva<br>y no intensiva.</h2>
      <p class="lede" style="margin-bottom:var(--s7)">La categoría de higiene femenina opera casi sin excepción en distribución intensiva. Aura opera en el extremo opuesto durante su fase de lanzamiento. La decisión sacrifica cobertura y compra control.</p>

      <figure class="figure" style="margin-top:0">
        <img src="assets/img/fig-distribucion.svg" alt="Diagrama comparativo de distribución intensiva, selectiva y exclusiva" width="780" height="330" loading="lazy">
        <figcaption>Aura opera en el tercer modelo. La transición a distribución selectiva está condicionada a dos métricas: seis meses sin quiebres de inventario y un protocolo de capacitación replicable sin presencia del equipo.</figcaption>
      </figure>

      <div class="spec-label" style="max-width:none;margin-top:var(--s7)">
        <div class="spec-label__head">
          <h3 class="spec-label__title">Mezcla de mercadeo</h3>
          <p class="spec-label__sub">FASE DE LANZAMIENTO · HONDURAS · 2026</p>
        </div>
        <table class="spec-table">
          <tbody>
{mix_rows}
          </tbody>
        </table>
      </div>
    </div>
  </section>

  <section class="band">
    <div class="wrap">
      <div style="max-width:620px;margin-bottom:var(--s7)">
        <p class="eyebrow">Pilares de contenido</p>
        <h2 class="display-l">Sobre qué escribe<br>una marca de toallas.</h2>
        <p class="lede" style="margin-top:var(--s4)">El blog no habla del producto. Habla de las cuatro cosas que hacen que el producto tenga sentido, y deja que el lector haga la conexión.</p>
      </div>

      <div class="stat-row">
        <div class="stat">
          <span class="stat__n">01</span>
          <span class="stat__l"><strong style="color:var(--pulp)">Materiales y residuos.</strong> Qué hay dentro de una toalla y qué pasa después. Es el pilar que sostiene el argumento del producto.</span>
        </div>
        <div class="stat">
          <span class="stat__n">02</span>
          <span class="stat__l"><strong style="color:var(--pulp)">Salud y evidencia.</strong> Qué dicen los estudios y, sobre todo, qué no dicen. Es el pilar donde más fácil sería exagerar.</span>
        </div>
        <div class="stat">
          <span class="stat__n">03</span>
          <span class="stat__l"><strong style="color:var(--pulp)">Normativa y sellos.</strong> Cómo leer una afirmación ambiental. Le da al lector herramientas para auditarnos a nosotros también.</span>
        </div>
        <div class="stat">
          <span class="stat__n">04</span>
          <span class="stat__l"><strong style="color:var(--pulp)">Contexto social.</strong> Pobreza menstrual y acceso. Es el pilar que no vende, y por eso es el que da credibilidad a los otros tres.</span>
        </div>
      </div>
    </div>
  </section>

  <section class="band band--light">
    <div class="wrap" style="max-width:860px">
      <p class="eyebrow">Tono de voz</p>
      <h2 class="display-l" style="margin-bottom:var(--s6)">Cómo se escribe Aura.</h2>

      <div class="spec-label" style="max-width:none">
        <div class="spec-label__head">
          <h3 class="spec-label__title">Decimos / No decimos</h3>
          <p class="spec-label__sub">REGLA GENERAL: SI NO SE PUEDE VERIFICAR, NO SE ESCRIBE</p>
        </div>
        <table class="spec-table">
          <thead>
            <tr><th scope="col">Sí</th><th scope="col">No</th></tr>
          </thead>
          <tbody>
{voz_rows}
          </tbody>
        </table>
      </div>

      <p style="margin-top:var(--s6);max-width:64ch">Voseo, segunda persona, frases cortas. Sin signos de admiración. Sin adjetivos que no se puedan medir. Cuando hay una cifra, va la cifra; cuando no la hay, se dice que no la hay.</p>
    </div>
  </section>

  <section class="band band--light-2">
    <div class="wrap" style="max-width:860px">
      <p class="eyebrow">Identidad visual</p>
      <h2 class="display-l" style="margin-bottom:var(--s6)">Granate, no rosa.</h2>
      <p class="lede" style="margin-bottom:var(--s7)">La categoría entera usa rosa pastel y líquido azul en su publicidad. Aura usa el color de aquello que la toalla efectivamente absorbe. Es una decisión de diferenciación, no de provocación: en un lineal donde todo es claro y rosado, un empaque granate sobre mora se ve a distancia.</p>

      <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(140px,1fr));gap:var(--s4);margin-bottom:var(--s7)">
        <div><div style="height:78px;background:#1B0E13;border-radius:var(--radius);border:1px solid rgba(34,26,28,.2)"></div><p class="data" style="margin:var(--s3) 0 0">#1B0E13 · Mora</p></div>
        <div><div style="height:78px;background:#8C1D33;border-radius:var(--radius)"></div><p class="data" style="margin:var(--s3) 0 0">#8C1D33 · Granate</p></div>
        <div><div style="height:78px;background:#E5A83B;border-radius:var(--radius)"></div><p class="data" style="margin:var(--s3) 0 0">#E5A83B · Halo</p></div>
        <div><div style="height:78px;background:#4A5A46;border-radius:var(--radius)"></div><p class="data" style="margin:var(--s3) 0 0">#4A5A46 · Musgo</p></div>
        <div><div style="height:78px;background:#E6E8DD;border-radius:var(--radius);border:1px solid rgba(34,26,28,.2)"></div><p class="data" style="margin:var(--s3) 0 0">#E6E8DD · Pulpa</p></div>
      </div>

      <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:var(--s5)">
        <div style="border-top:2px solid var(--ink);padding-top:var(--s4)">
          <p style="font-family:var(--display);font-size:2rem;line-height:1;margin-bottom:var(--s3)">Young Serif</p>
          <p class="data" style="margin:0;color:var(--ink-soft)">Titulares. Serif de contraste vivo, sin la elegancia fría de las serif editoriales habituales.</p>
        </div>
        <div style="border-top:2px solid var(--ink);padding-top:var(--s4)">
          <p style="font-family:var(--read);font-size:2rem;line-height:1;margin-bottom:var(--s3)">Newsreader</p>
          <p class="data" style="margin:0;color:var(--ink-soft)">Cuerpo de artículo. Pensada para lectura larga en pantalla.</p>
        </div>
        <div style="border-top:2px solid var(--ink);padding-top:var(--s4)">
          <p style="font-family:var(--mono);font-size:1.75rem;line-height:1;margin-bottom:var(--s3)">DM Mono</p>
          <p class="data" style="margin:0;color:var(--ink-soft)">Datos, porcentajes y referencias. La monoespaciada señala «esto es un dato, no una promesa».</p>
        </div>
      </div>
    </div>
  </section>

  <section class="band">
    <div class="wrap" style="max-width:860px">
      <p class="eyebrow">Medición</p>
      <h2 class="display-l" style="margin-bottom:var(--s5)">Qué mira esta estrategia<br>para saber si funciona.</h2>
      <p class="lede" style="margin-bottom:var(--s6)">En mercadeo de contenidos el alcance es una métrica engañosa: mide cuánta gente pasó, no cuánta entendió. Estos son los indicadores que sí responden a la pregunta.</p>

      <div class="faq" style="border-top-color:var(--void-3)">
        <details open style="border-bottom-color:var(--void-3)">
          <summary style="color:var(--pulp)">Profundidad de lectura, no visitas</summary>
          <p style="color:var(--paper-soft)">Porcentaje de lectores que llega al 75 % de un artículo. Un texto de nueve minutos con seis referencias que nadie termina no está haciendo su trabajo, aunque tenga tráfico.</p>
        </details>
        <details style="border-bottom-color:var(--void-3)">
          <summary style="color:var(--pulp)">Recorrido de blog a producto</summary>
          <p style="color:var(--paper-soft)">Proporción de lectores del artículo de lanzamiento que abre la lista de puntos de venta. Mide si el contenido está convirtiendo interés en intención.</p>
        </details>
        <details style="border-bottom-color:var(--void-3)">
          <summary style="color:var(--pulp)">Venta por punto, no venta total</summary>
          <p style="color:var(--paper-soft)">En distribución exclusiva la venta total dice poco, porque los puntos son pocos por diseño. Lo que importa es la rotación media por punto y su dispersión: si un punto vende cinco veces más que otro, el problema es de capacitación, no de demanda.</p>
        </details>
        <details style="border-bottom-color:var(--void-3)">
          <summary style="color:var(--pulp)">Precisión del punto de venta</summary>
          <p style="color:var(--paper-soft)">Visitas de comprador incógnito para verificar que el personal explica la composición sin inventar beneficios de salud ni afirmar certificaciones inexistentes. Es el indicador que protege todo lo demás.</p>
        </details>
      </div>
    </div>
  </section>

  <section class="band band--garnet band--tight">
    <div class="wrap" style="display:flex;flex-wrap:wrap;gap:var(--s6);align-items:center;justify-content:space-between">
      <div style="max-width:42ch">
        <h2 class="display-m" style="margin-bottom:var(--s3)">La estrategia empieza en el artículo de lanzamiento.</h2>
        <p style="margin:0;opacity:.85;font-family:var(--read)">Ahí está desarrollada la decisión de canal, con los criterios de selección de los catorce puntos.</p>
      </div>
      <a class="btn btn--solid" href="articulos/lanzamiento-aura-honduras.html">Leer el lanzamiento</a>
    </div>
  </section>
"""

render("marca.html", "Estrategia de marca — Aura",
       "Posicionamiento, segmentos, estrategia de distribución exclusiva, pilares de contenido, tono de voz e identidad visual de Aura.",
       MARCA, depth=0, active="mark")
