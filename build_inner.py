#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Genera blog.html, producto.html y marca.html."""

from build_shell import render

# ==========================================================================
# BLOG
# ==========================================================================

POSTS = [
    ("LANZAMIENTO", "Aura llega a San Pedro Sula, y solo a seis lugares",
     "Toallas de tela reutilizables, cosidas en la ciudad, que salen a la venta el 1 de septiembre sin pasar por el supermercado. La decisión de canal es deliberada, y explicarla es parte del producto.",
     "articulos/lanzamiento-aura-san-pedro-sula.html", "10 MIN · 3 REFERENCIAS"),
    ("EVIDENCIA", "Reutilizable contra desechable: lo que midieron los análisis de ciclo de vida",
     "Los reutilizables ganan la comparación general, pero con dos condiciones que casi ninguna marca menciona. Una de ellas puede invertir el resultado por completo.",
     "articulos/reutilizable-o-desechable.html", "8 MIN · 4 REFERENCIAS"),
    ("ECONOMÍA", "Cuánto dura una toalla de tela y cuánto ahorra de verdad",
     "Vida media observada de 4.3 años, rango posible hasta diez, y una inversión inicial que no se recupera en el primer ciclo. La cuenta completa, con sus supuestos a la vista.",
     "articulos/cuanto-dura-cuanto-ahorra.html", "7 MIN · 3 REFERENCIAS"),
    ("CUIDADO", "Cómo lavarlas sin arruinarlas",
     "El obstáculo de este producto casi nunca es el producto: es la rutina. Cuatro pasos, cinco errores que acortan la vida útil, y qué hacer cuando estás fuera de casa.",
     "articulos/como-lavar-toallas-de-tela.html", "8 MIN · 3 REFERENCIAS"),
    ("MERCADEO", "Greenwashing: el 53 % de las promesas verdes no resiste una revisión",
     "La Comisión Europea auditó las afirmaciones ambientales del mercado y encontró que más de la mitad eran vagas o infundadas. La primera trampa de la lista es la de nuestra propia categoría.",
     "articulos/greenwashing-marketing-verde.html", "9 MIN · 6 REFERENCIAS"),
    ("CONTEXTO", "Pobreza menstrual: el costo de no poder elegir",
     "Dos de cada cinco niñas de la región faltan a clases durante su periodo. Por qué un producto reutilizable ayuda menos de lo que parece donde no hay agua confiable.",
     "articulos/pobreza-menstrual-america-latina.html", "7 MIN · 6 REFERENCIAS"),
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
      <p class="lede">Seis artículos sobre materiales, ciclo de vida, cuidado y comunicación ambiental en la categoría de higiene menstrual. Cada afirmación está enlazada al estudio que la respalda. Donde la evidencia contradice nuestro propio argumento comercial, también lo decimos.</p>
    </div>
  </section>

  <section class="band--paper-2" style="padding-top:var(--s7)">
    <div class="wrap" style="margin-bottom:var(--s6)">
      <p class="eyebrow">Seis artículos · 25 referencias</p>
    </div>
    <div class="post-grid">
{cards}
    </div>
  </section>

  <section class="band" id="metodo">
    <div class="wrap" style="max-width:780px">
      <p class="eyebrow">Método editorial</p>
      <h2 class="display-l" style="margin-bottom:var(--s6)">Cinco reglas que nos<br>pusimos al escribir esto.</h2>

      <div class="faq">
        <details open>
          <summary>Priorizamos literatura revisada por pares</summary>
          <p>Cuando existe un estudio publicado en una revista con revisión por pares, esa es la fuente. Los informes de organismos internacionales se usan cuando aportan una síntesis que la literatura individual no da, y quedan identificados como tales en la lista de referencias.</p>
        </details>
        <details>
          <summary>Publicamos los datos que nos contradicen</summary>
          <p>El informe de la Life Cycle Initiative concluye que una toalla reutilizable importada por vía aérea puede tener mayor impacto que una desechable. Es un dato que puede volverse en contra de nuestra propia categoría, y está citado en dos de nuestros artículos, porque omitirlo sería exactamente la práctica que criticamos en el resto de la industria.</p>
        </details>
        <details>
          <summary>Separamos lo observado de lo prometido</summary>
          <p>La vida útil media observada en la literatura es de 4.3 años. El rango que permite el producto con buen cuidado llega a diez. Son dos cifras distintas y las presentamos como tales, en lugar de publicar solo la más favorable.</p>
        </details>
        <details>
          <summary>Decimos para quién no sirve</summary>
          <p>Este producto necesita agua limpia, jabón y un lugar donde secar. Si esas tres condiciones no están, no va a funcionar. Preferimos perder una venta que ganar una devolución y una mala experiencia.</p>
        </details>
        <details>
          <summary>Fechamos y corregimos</summary>
          <p>Cada artículo lleva su fecha. Si encontrás un error, escribinos a <a href="mailto:hola@aura.hn">hola@aura.hn</a>. Las correcciones se hacen sobre el texto y se anotan al pie.</p>
        </details>
      </div>
    </div>
  </section>

  <section class="band band--forest band--tight">
    <div class="wrap" style="display:flex;flex-wrap:wrap;gap:var(--s6);align-items:center;justify-content:space-between">
      <div style="max-width:42ch">
        <h2 class="display-m" style="margin-bottom:var(--s3)">Uso libre para fines educativos.</h2>
        <p class="lede" style="margin:0">Si sos docente o trabajás en salud comunitaria, podés reproducir estos textos con atribución. El de lavado es el más útil para talleres.</p>
      </div>
      <a class="btn btn--solid" href="mailto:hola@aura.hn">Escribinos</a>
    </div>
  </section>
"""

render("blog.html", "Blog — Aura",
       "Seis artículos con referencias sobre ciclo de vida de productos menstruales, vida útil de toallas reutilizables, cuidado, greenwashing y pobreza menstrual.",
       BLOG, depth=0, active="sci")

# ==========================================================================
# PRODUCTO
# ==========================================================================

SPECS = [
    ("Aura Diario", "#C6D2BE", "PROTECTOR DIARIO · SIN ALAS", "L 145", "por unidad",
     [("Largo", "180 mm"), ("Capas absorbentes", "2"), ("Contacto", "Algodón"),
      ("Núcleo", "Bambú"), ("Base", "Capa impermeable"), ("Cierre", "Broche de presión")],
     "Para los días de inicio y cierre del ciclo, y para uso con copa. La más delgada de las tres."),
    ("Aura Día", "#A3B79B", "FLUJO MEDIO · CON ALAS", "L 185", "por unidad",
     [("Largo", "250 mm"), ("Capas absorbentes", "4"), ("Contacto", "Algodón"),
      ("Núcleo", "Bambú"), ("Base", "Capa impermeable"), ("Cierre", "Broche de presión")],
     "El formato de todos los días. Alas con broche que rodean la ropa interior y evitan el desplazamiento."),
    ("Aura Noche", "#E8C6B5", "FLUJO ALTO · CON ALAS", "L 225", "por unidad",
     [("Largo", "330 mm"), ("Capas absorbentes", "6"), ("Contacto", "Algodón"),
      ("Núcleo", "Bambú"), ("Base", "Capa impermeable"), ("Cierre", "Broche de presión")],
     "Más larga y con más capas, para las horas en que no te levantás. También sirve para posparto."),
]

blocks = []
for i, (name, color, tag, price, unit, rows, desc) in enumerate(SPECS):
    trs = "\n".join(f'            <tr><th scope="row">{k}</th><td class="num">{v}</td></tr>' for k, v in rows)
    flip = "direction:rtl" if i % 2 else ""
    blocks.append(f"""
    <div class="wrap" style="display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:var(--s7);align-items:center;padding-block:var(--s7);{flip}">
      <div style="direction:ltr">
        <div style="background:{color};border-radius:var(--radius-lg);aspect-ratio:4/3;position:relative;overflow:hidden">
          <div style="position:absolute;inset:0;background-image:radial-gradient(circle, rgba(255,255,255,.6) 1.6px, transparent 1.8px);background-size:20px 20px"></div>
        </div>
      </div>
      <div style="direction:ltr">
        <span class="sku__for">{tag}</span>
        <h2 class="display-l" style="margin:var(--s3) 0 var(--s4)">{name}</h2>
        <p class="lede" style="margin-bottom:var(--s5)">{desc}</p>
        <table class="spec-table" style="border:1px solid var(--line);border-radius:var(--radius);margin-bottom:var(--s5);background:var(--paper-2)">
          <tbody>
{trs}
          </tbody>
        </table>
        <div style="display:flex;align-items:baseline;gap:var(--s4);flex-wrap:wrap">
          <span class="display-m">{price}</span>
          <span class="data" style="color:var(--ink-soft)">{unit} · precio único en todos los puntos</span>
        </div>
      </div>
    </div>""")

PUNTOS = [
    ("Barrio Río de Piedras", "Farmacia", "Zona norte"),
    ("Avenida Circunvalación", "Tienda naturista", "Zona Viva"),
    ("Colonia Trejo", "Farmacia", "Zona sureste"),
    ("Colonia Jardines del Valle", "Tienda naturista", "Zona suroeste"),
    ("Barrio Guamilito", "Farmacia", "Centro"),
    ("Colonia Universidad", "Tienda naturista", "Zona este"),
]

pts = "\n".join(f"""
        <div class="pos">
          <span class="pos__n">{i:02d}</span>
          <h3 class="pos__zona">{zona}</h3>
          <p class="pos__tipo">{tipo}</p>
          <p class="pos__sec">{sector}</p>
        </div>""" for i, (zona, tipo, sector) in enumerate(PUNTOS, 1))

PROD = f"""
  <section class="band band--tight">
    <div class="wrap" style="max-width:780px">
      <p class="eyebrow">Producto</p>
      <h1 class="display-xl" style="margin-bottom:var(--s5)">Tres tamaños.<br>Un solo estándar.</h1>
      <p class="lede">Cambia el largo y cambia el número de capas absorbentes. No cambia el material: algodón en la capa de contacto, bambú en el núcleo y una capa impermeable que impide el traspaso. Todas se cierran con broche de presión y se cosen en San Pedro Sula.</p>
    </div>
  </section>

  <section class="band--paper-2" style="padding-block:var(--s6)">
    <div class="wrap">
      <figure class="figure" style="margin:0">
        <img src="assets/img/producto-mesa.jpg" alt="Los tres tamaños de toallas reutilizables Aura en verde salvia, crema y rosa, con su bolsa de lienzo" width="1408" height="768">
        <figcaption>Los tres tamaños y la bolsa de transporte de lienzo crudo, incluida en el juego completo.</figcaption>
      </figure>
    </div>
  </section>

  <section>
{''.join(blocks)}
  </section>

  <section class="band band--linen">
    <div class="wrap" style="max-width:900px">
      <p class="eyebrow">Cuántas necesitás</p>
      <h2 class="display-l" style="margin-bottom:var(--s5)">La pregunta que decide<br>si el cambio funciona.</h2>
      <p class="lede" style="margin-bottom:var(--s7)">Depende de tu flujo y de cada cuánto lavás. Comprar de menos es el error más común: te quedás sin toallas secas a mitad del ciclo, volvés a las desechables por urgencia y el juego termina en un cajón.</p>

      <div class="stat-row">
        <div class="stat">
          <span class="stat__n">5–7</span>
          <span class="stat__l"><strong>Si lavás todos los días.</strong> Un juego pequeño alcanza, combinando diario y día.</span>
        </div>
        <div class="stat">
          <span class="stat__n">10–12</span>
          <span class="stat__l"><strong>Si lavás cada dos o tres días.</strong> Juego completo, para no quedarte sin toallas secas.</span>
        </div>
        <div class="stat">
          <span class="stat__n">2–3</span>
          <span class="stat__l"><strong>Si querés probar.</strong> Para los días de flujo bajo, manteniendo desechables el resto. Un cambio parcial sigue siendo un cambio.</span>
        </div>
      </div>

      <p style="margin-top:var(--s6);max-width:64ch"><a href="articulos/cuanto-dura-cuanto-ahorra.html">La cuenta completa del ahorro</a>, con la vida útil observada en la literatura y los supuestos a la vista.</p>
    </div>
  </section>

  <section class="band" id="cuidado">
    <div class="wrap">
      <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:var(--s7);align-items:center">
        <div>
          <p class="eyebrow">Cuidado</p>
          <h2 class="display-l" style="margin-bottom:var(--s5)">Agua fría, jabón neutro,<br>secado completo.</h2>
          <p class="lede" style="margin-bottom:var(--s5)">Esos tres pasos son casi toda la diferencia entre una toalla que dura tres años y una que dura siete. El agua caliente fija la mancha, el suavizante impermeabiliza la fibra y guardarlas húmedas produce el olor que ya no sale.</p>
          <a class="btn btn--ghost" href="articulos/como-lavar-toallas-de-tela.html">Leer la guía completa</a>
        </div>
        <div>
          <figure class="figure" style="margin:0">
            <img src="assets/img/producto-bano.jpg" alt="Bolsa de transporte Aura sobre una repisa de baño, junto a la caja de la marca y toallas dobladas" width="1024" height="559" loading="lazy">
            <figcaption>La bolsa impermeable resuelve el punto más difícil: qué hacer con una toalla usada fuera de casa.</figcaption>
          </figure>
        </div>
      </div>
    </div>
  </section>

  <section class="band band--forest" id="puntos">
    <div class="wrap">
      <div style="max-width:660px;margin-bottom:var(--s7)">
        <p class="eyebrow">Distribución exclusiva</p>
        <h2 class="display-l" style="margin-bottom:var(--s4)">Seis puntos,<br>todos en San Pedro Sula.</h2>
        <p class="lede">Aura no se vende en supermercados. Cada punto firmó un acuerdo de exclusividad recíproca, recibió capacitación sobre materiales, tamaños y lavado, y sostiene el mismo precio publicado. Las seis zonas no se solapan: dos aliados compitiendo por el mismo radio anularían el sentido del acuerdo.</p>
        <p style="margin-top:var(--s5)"><a class="btn btn--ghost" href="articulos/lanzamiento-aura-san-pedro-sula.html">Por qué elegimos este canal</a></p>
      </div>

      <div class="pos-grid">
{pts}
      </div>

      <p style="margin-top:var(--s6);font-family:var(--mono);font-size:.75rem;color:var(--paper-soft);max-width:66ch">
        Las direcciones exactas se publican el 1 de septiembre. La ampliación dentro de San Pedro Sula se habilita cuando estos seis puntos sostengan seis meses sin quiebres de inventario.
      </p>
    </div>
  </section>

  <section class="band">
    <div class="wrap" style="max-width:820px">
      <p class="eyebrow">Preguntas</p>
      <h2 class="display-l" style="margin-bottom:var(--s7)">Lo que conviene que sepas.</h2>

      <div class="faq">
        <details open>
          <summary>¿Se sienten húmedas?</summary>
          <p>Menos de lo que la gente espera, pero más que una desechable con gel superabsorbente. Una desechable retiene el líquido en un polímero y deja la superficie seca al tacto; una toalla de tela lo distribuye entre sus capas y la superficie se percibe textil.</p>
          <p>Es una diferencia real de sensación, no un defecto de fabricación, y conviene saberlo antes de comprar.</p>
        </details>
        <details>
          <summary>¿Se corren o se mueven?</summary>
          <p>Las alas se cierran con broche de presión alrededor de la ropa interior, así que quedan sujetas por debajo en lugar de pegadas por arriba. Con ropa interior ajustada se mantienen bien; con ropa interior muy holgada, cualquier toalla se mueve.</p>
        </details>
        <details>
          <summary>¿Se nota el olor?</summary>
          <p>El olor de la menstruación aparece sobre todo por la interacción con materiales sintéticos y por el tiempo de exposición al aire. Al ser fibra natural y cambiarse con la misma frecuencia que una desechable, la mayoría de las usuarias reporta menos olor, no más.</p>
          <p>Guardadas húmedas sí desarrollan olor, y eso no se corrige después. El secado completo es la parte que no se puede saltar.</p>
        </details>
        <details>
          <summary>¿Y si estoy fuera de casa todo el día?</summary>
          <p>Doblás la toalla usada con la cara de contacto hacia adentro, la cerrás con su propio broche y la guardás en la bolsa impermeable. Queda cerrada y sin contacto con el resto de tus cosas. En casa seguís la rutina normal.</p>
        </details>
        <details>
          <summary>¿Son higiénicas?</summary>
          <p>La revisión sistemática más amplia disponible sobre toallas reutilizables, con 44 estudios y cerca de 14.800 participantes, no reportó casos objetivos de infección asociados a su uso. En un cohorte en Uganda, la irritación cutánea autorreportada fue del 23.8 % a los tres meses de uso, frente al 72.8 % registrado al inicio con toallas desechables.</p>
          <p>Conviene leerlo con cuidado: esos datos vienen de contextos muy distintos al hondureño y los propios autores califican la calidad general de los estudios como baja. Lo presentamos como está, sin convertirlo en una promesa de salud.</p>
        </details>
        <details>
          <summary>¿Y si no tengo agua confiable?</summary>
          <p>Entonces este producto probablemente no te va a funcionar. Necesita agua limpia, jabón y un lugar donde secar. Preferimos decirlo antes de la compra que después.</p>
        </details>
      </div>
    </div>
  </section>
"""

render("producto.html", "Producto — Aura",
       "Toallas sanitarias reutilizables Aura en tres tamaños: materiales, cuántas necesitás, cuidado y los seis puntos de venta exclusivos en San Pedro Sula.",
       PROD, depth=0, active="prod")

# ==========================================================================
# MARCA
# ==========================================================================

VOZ = [
    ("«Vida media observada: 4.3 años»", "«Duran para siempre»"),
    ("«Se cose en San Pedro Sula»", "«Comprometidas con el planeta»"),
    ("«Necesita agua limpia y un lugar donde secar»", "«Para todas las mujeres»"),
    ("«Seis puntos de venta»", "«Disponible en puntos seleccionados»"),
    ("«Cuesta más al inicio y se recupera con los años»", "«Invertí en vos misma»"),
]

voz_rows = "\n".join(
    f'''            <tr>
              <th scope="row" style="font-weight:400">{a}</th>
              <td>{b}</td>
            </tr>''' for a, b in VOZ
)

MIX = [
    ("Producto", "Toalla de tela reutilizable en tres tamaños, con bolsa de transporte. El atributo diferencial no es el material sino la producción local, que es la condición que la evidencia de ciclo de vida señala como determinante."),
    ("Precio", "Inversión inicial superior a un paquete de desechables, con recuperación a mediano plazo. Precio único publicado, sin descuentos por punto."),
    ("Plaza", "Distribución exclusiva en San Pedro Sula. Seis puntos sin solape territorial, exclusividad recíproca y capacitación obligatoria del punto de venta."),
    ("Promoción", "Mercadeo de contenidos. El blog es el canal principal: seis artículos con referencias verificables, en lugar de pauta de alcance."),
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
      <p class="lede">Esta página documenta el razonamiento de mercadeo detrás del lanzamiento en San Pedro Sula: a quién le hablamos, qué posición ocupamos, por qué elegimos un canal exclusivo y qué reglas de lenguaje seguimos. Está publicada a propósito, porque una marca cuyo argumento es la transparencia no puede esconder su propia estrategia.</p>
    </div>
  </section>

  <section class="band band--paper-2">
    <div class="wrap" style="max-width:820px">
      <p class="eyebrow">Posicionamiento</p>
      <h2 class="display-l" style="margin-bottom:var(--s5)">Un enunciado, cuatro consecuencias.</h2>
      <div class="pull" style="margin-top:0">
        Para mujeres de San Pedro Sula que ya cuestionan lo que consumen, Aura es la toalla reutilizable que se cose en la misma ciudad donde se vende, porque la evidencia de ciclo de vida muestra que una toalla de tela importada por avión puede contaminar más que la desechable que dice reemplazar.
      </div>
      <p style="margin-top:var(--s6)">El enunciado obliga a cuatro cosas, y cada una tiene una consecuencia operativa visible en el sitio:</p>
      <ol style="font-family:var(--read);font-size:1.0625rem;line-height:1.7;padding-left:1.3em">
        <li style="margin-bottom:var(--s3)">Fabricar localmente, aunque el costo por unidad sea mayor que importar.</li>
        <li style="margin-bottom:var(--s3)">Publicar la vida útil observada en la literatura, no la más favorable.</li>
        <li style="margin-bottom:var(--s3)">Citar los estudios que nos contradicen dentro de nuestros propios artículos.</li>
        <li>Elegir un canal donde el producto se pueda explicar, aunque cueste cobertura.</li>
      </ol>
    </div>
  </section>

  <section class="band">
    <div class="wrap">
      <div style="max-width:620px;margin-bottom:var(--s7)">
        <p class="eyebrow">Segmento</p>
        <h2 class="display-l">A quién le habla<br>este blog.</h2>
      </div>

      <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(290px,1fr));gap:var(--s5)">
        <div style="border:1px solid var(--line);border-radius:var(--radius-lg);padding:var(--s6);background:var(--paper-2)">
          <span class="data" style="color:var(--wood)">SEGMENTO PRIMARIO</span>
          <h3 class="display-m" style="margin:var(--s3) 0 var(--s4)">La que ya lee etiquetas</h3>
          <p style="font-size:.9375rem;color:var(--ink-soft)">Mujer de 24 a 38 años, residente en San Pedro Sula, con ingreso propio. Ya cambió otros productos de su rutina por versiones sin fragancia. Desconfía de la palabra «natural» porque la vio usada en demasiadas cosas.</p>
          <p style="font-size:.9375rem;color:var(--ink-soft);margin:0"><strong style="color:var(--forest)">Qué la mueve:</strong> poder verificar. No busca que le prometan, busca poder comprobar.</p>
        </div>

        <div style="border:1px solid var(--line);border-radius:var(--radius-lg);padding:var(--s6);background:var(--paper-2)">
          <span class="data" style="color:var(--wood)">SEGMENTO SECUNDARIO</span>
          <h3 class="display-m" style="margin:var(--s3) 0 var(--s4)">La que tuvo irritación</h3>
          <p style="font-size:.9375rem;color:var(--ink-soft)">Mujer de cualquier edad con antecedente de molestia recurrente con toallas desechables. Llega buscando una alternativa concreta, no un discurso ambiental.</p>
          <p style="font-size:.9375rem;color:var(--ink-soft);margin:0"><strong style="color:var(--forest)">Qué la mueve:</strong> el alivio. Es el segmento con el que hay que ser más cuidadoso, porque es donde más tentador resulta prometer salud.</p>
        </div>

        <div style="border:1px solid var(--line);border-radius:var(--radius-lg);padding:var(--s6);background:var(--paper-2)">
          <span class="data" style="color:var(--wood)">INFLUENCIA</span>
          <h3 class="display-m" style="margin:var(--s3) 0 var(--s4)">El punto de venta</h3>
          <p style="font-size:.9375rem;color:var(--ink-soft)">En las farmacias de barrio y tiendas naturistas de San Pedro Sula, la recomendación de mostrador pesa más que cualquier empaque. Con un producto que exige explicación, ese actor deja de ser intermediario y pasa a ser parte del mensaje.</p>
          <p style="font-size:.9375rem;color:var(--ink-soft);margin:0"><strong style="color:var(--forest)">Qué lo mueve:</strong> margen superior, protección territorial y saber explicar el producto sin equivocarse.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="band band--linen">
    <div class="wrap" style="max-width:900px">
      <p class="eyebrow">Estrategia de canal</p>
      <h2 class="display-l" style="margin-bottom:var(--s5)">Por qué exclusiva<br>y no intensiva.</h2>
      <p class="lede" style="margin-bottom:var(--s7)">La categoría de higiene femenina opera casi sin excepción en distribución intensiva. Aura opera en el extremo opuesto durante su fase de lanzamiento: seis puntos, una sola ciudad. La decisión sacrifica cobertura y compra control. La justificación es específica del producto: una toalla reutilizable exige una conversación, no un empaque.</p>

      <figure class="figure" style="margin-top:0">
        <img src="assets/img/fig-distribucion.svg" alt="Diagrama comparativo de distribución intensiva, selectiva y exclusiva" width="780" height="330" loading="lazy">
        <figcaption>Aura opera en el tercer modelo. La expansión avanza por fases con condición de entrada medible, no por fecha: primero ampliar dentro de San Pedro Sula, después Tegucigalpa, y solo al final la transición a distribución selectiva.</figcaption>
      </figure>

      <div class="spec-label" style="max-width:none;margin-top:var(--s7)">
        <div class="spec-label__head">
          <h3 class="spec-label__title">Mezcla de mercadeo</h3>
          <p class="spec-label__sub">FASE DE LANZAMIENTO · SAN PEDRO SULA · 2026</p>
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
        <p class="lede" style="margin-top:var(--s4)">El blog no habla del producto. Habla de las cuatro cosas que hacen que el producto tenga sentido, y deja que quien lee haga la conexión.</p>
      </div>

      <div class="stat-row">
        <div class="stat">
          <span class="stat__n">01</span>
          <span class="stat__l"><strong style="color:var(--forest)">Evidencia de ciclo de vida.</strong> Qué se midió al comparar reutilizables con desechables, y bajo qué condiciones se invierte el resultado.</span>
        </div>
        <div class="stat">
          <span class="stat__n">02</span>
          <span class="stat__l"><strong style="color:var(--forest)">Uso y cuidado.</strong> El pilar más útil y el menos glamoroso. Es el que decide si el producto se usa o se abandona.</span>
        </div>
        <div class="stat">
          <span class="stat__n">03</span>
          <span class="stat__l"><strong style="color:var(--forest)">Comunicación ambiental.</strong> Cómo leer una afirmación verde. Le da a quien lee herramientas para auditarnos a nosotros también.</span>
        </div>
        <div class="stat">
          <span class="stat__n">04</span>
          <span class="stat__l"><strong style="color:var(--forest)">Contexto social.</strong> Pobreza menstrual y acceso. Es el pilar que no vende, y por eso es el que da credibilidad a los otros tres.</span>
        </div>
      </div>
    </div>
  </section>

  <section class="band band--paper-2">
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

  <section class="band band--linen">
    <div class="wrap" style="max-width:860px">
      <p class="eyebrow">Identidad visual</p>
      <h2 class="display-l" style="margin-bottom:var(--s6)">El sol y el lienzo.</h2>
      <p class="lede" style="margin-bottom:var(--s7)">La paleta sale del producto, no de un tablero de tendencias: el verde del logotipo, el crudo del lienzo de la bolsa, el salvia y el rosado de las telas, el dorado del sol naciente. Nada de rosa pastel ni de líquido azul, que es donde vive la publicidad del resto de la categoría.</p>

      <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(130px,1fr));gap:var(--s4);margin-bottom:var(--s7)">
        <div><div style="height:80px;background:#2C4636;border-radius:var(--radius)"></div><p class="data" style="margin:var(--s3) 0 0">#2C4636 · Bosque</p></div>
        <div><div style="height:80px;background:#A3B79B;border-radius:var(--radius)"></div><p class="data" style="margin:var(--s3) 0 0">#A3B79B · Salvia</p></div>
        <div><div style="height:80px;background:#C4913C;border-radius:var(--radius)"></div><p class="data" style="margin:var(--s3) 0 0">#C4913C · Sol</p></div>
        <div><div style="height:80px;background:#E8C6B5;border-radius:var(--radius)"></div><p class="data" style="margin:var(--s3) 0 0">#E8C6B5 · Rosado</p></div>
        <div><div style="height:80px;background:#8A6C4A;border-radius:var(--radius)"></div><p class="data" style="margin:var(--s3) 0 0">#8A6C4A · Madera</p></div>
        <div><div style="height:80px;background:#F5F1E8;border-radius:var(--radius);border:1px solid var(--line-2)"></div><p class="data" style="margin:var(--s3) 0 0">#F5F1E8 · Lienzo</p></div>
      </div>

      <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:var(--s5)">
        <div style="border-top:2px solid var(--forest);padding-top:var(--s4)">
          <p style="font-family:var(--display);font-weight:600;font-size:2rem;line-height:1;margin-bottom:var(--s3);color:var(--forest)">Petrona</p>
          <p class="data" style="margin:0;color:var(--ink-soft)">Titulares. Serif de trazo cálido, cercano al del logotipo.</p>
        </div>
        <div style="border-top:2px solid var(--forest);padding-top:var(--s4)">
          <p style="font-family:var(--read);font-size:2rem;line-height:1;margin-bottom:var(--s3);color:var(--forest)">Newsreader</p>
          <p class="data" style="margin:0;color:var(--ink-soft)">Cuerpo de artículo. Pensada para lectura larga en pantalla.</p>
        </div>
        <div style="border-top:2px solid var(--forest);padding-top:var(--s4)">
          <p style="font-family:var(--mono);font-size:1.625rem;line-height:1;margin-bottom:var(--s3);color:var(--forest)">DM Mono</p>
          <p class="data" style="margin:0;color:var(--ink-soft)">Datos y referencias. La monoespaciada señala «esto es un dato, no una promesa».</p>
        </div>
      </div>
    </div>
  </section>

  <section class="band band--forest">
    <div class="wrap" style="max-width:860px">
      <p class="eyebrow">Medición</p>
      <h2 class="display-l" style="margin-bottom:var(--s5)">Qué mira esta estrategia<br>para saber si funciona.</h2>
      <p class="lede" style="margin-bottom:var(--s6)">En mercadeo de contenidos el alcance es una métrica engañosa: mide cuánta gente pasó, no cuánta entendió. Y en un producto reutilizable, la venta tampoco basta: lo que importa es que se siga usando.</p>

      <div class="faq">
        <details open>
          <summary>Recompra de reposición, no venta inicial</summary>
          <p>Un producto que dura años no se mide por ventas repetidas rápidas. Se mide por quién vuelve a los seis meses a ampliar su juego. Esa es la señal de que el producto se está usando y no quedó en un cajón.</p>
        </details>
        <details>
          <summary>Profundidad de lectura, no visitas</summary>
          <p>Porcentaje de lectores que llega al 75 % del artículo de lavado. Es el texto que determina si el producto dura tres años o siete, así que su lectura completa vale más que diez visitas a la portada.</p>
        </details>
        <details>
          <summary>Venta por punto, no venta total</summary>
          <p>En distribución exclusiva la venta total dice poco, porque los puntos son pocos por diseño. Importa la rotación media por punto y su dispersión: si un punto vende cinco veces más que otro, el problema es de capacitación, no de demanda.</p>
        </details>
        <details>
          <summary>Precisión del punto de venta</summary>
          <p>Visitas de comprador incógnito para verificar que el personal explica cuántas toallas hacen falta y cómo se lavan, sin inventar beneficios de salud. Es el indicador que protege todo lo demás.</p>
        </details>
      </div>
    </div>
  </section>

  <section class="band band--paper-2 band--tight">
    <div class="wrap" style="display:flex;flex-wrap:wrap;gap:var(--s6);align-items:center;justify-content:space-between">
      <div style="max-width:42ch">
        <h2 class="display-m" style="margin-bottom:var(--s3)">La estrategia empieza en el artículo de lanzamiento.</h2>
        <p class="lede" style="margin:0">Ahí está desarrollada la decisión de canal, con los criterios de selección de los seis puntos y las razones para elegir San Pedro Sula.</p>
      </div>
      <a class="btn btn--solid" href="articulos/lanzamiento-aura-san-pedro-sula.html">Leer el lanzamiento</a>
    </div>
  </section>
"""

render("marca.html", "Estrategia de marca — Aura",
       "Posicionamiento, segmentos, estrategia de distribución exclusiva, pilares de contenido, tono de voz e identidad visual de Aura.",
       MARCA, depth=0, active="mark")
