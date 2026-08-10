#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Los seis artículos del blog de Aura."""

from build_shell import render, article, sup

REL = {
    "lanza":  ("LANZAMIENTO", "Aura llega a San Pedro Sula, y solo a seis lugares", "lanzamiento-aura-san-pedro-sula.html"),
    "acv":    ("EVIDENCIA", "Reutilizable contra desechable: lo que midieron los análisis de ciclo de vida", "reutilizable-o-desechable.html"),
    "vida":   ("ECONOMÍA", "Cuánto dura una toalla de tela y cuánto ahorra de verdad", "cuanto-dura-cuanto-ahorra.html"),
    "lavado": ("CUIDADO", "Cómo lavarlas sin arruinarlas", "como-lavar-toallas-de-tela.html"),
    "green":  ("MERCADEO", "Greenwashing: el 53 % de las promesas verdes no resiste una revisión", "greenwashing-marketing-verde.html"),
    "pobreza":("CONTEXTO", "Pobreza menstrual: el costo de no poder elegir", "pobreza-menstrual-america-latina.html"),
}

# ==========================================================================
# 1 · LANZAMIENTO
# ==========================================================================

A_LANZA = f"""
        <p>Aura sale a la venta en San Pedro Sula el 1 de septiembre. Son toallas sanitarias de tela, lavables y reutilizables, con capa de contacto de algodón, núcleo absorbente de bambú y broche de presión en las alas. Se cosen acá, en la ciudad.</p>

        <p>Y no las vas a encontrar en el supermercado.</p>

        <p>No es un problema de producción ni una promesa de «pronto en más puntos». Es una decisión de canal tomada antes de cortar la primera tela. Aura arranca con <strong>seis puntos de venta, todos en San Pedro Sula</strong>, cada uno con un acuerdo de exclusividad firmado. Este artículo explica por qué, porque la razón es también el argumento del producto.</p>

        <figure class="figure">
          <img src="../assets/img/producto-mesa.jpg" alt="Toallas sanitarias reutilizables Aura en verde salvia, crema y rosa, junto a su bolsa de lienzo con el logotipo de la marca" width="1408" height="768" loading="lazy">
          <figcaption>Los tres tamaños de Aura y la bolsa de transporte de lienzo crudo. Cada toalla se cierra con broche de presión bajo la ropa interior.</figcaption>
        </figure>

        <h2>El dato que decidió dónde fabricar</h2>

        <p>Hay un hallazgo en la literatura de ciclo de vida que casi ninguna marca de toallas reutilizables menciona, porque la deja mal parada. El informe de la Life Cycle Initiative del Programa de las Naciones Unidas para el Medio Ambiente, que reúne y compara los estudios disponibles, concluye que <strong>las toallas reutilizables producidas en el extranjero y enviadas por vía aérea tienen el mayor impacto ambiental de todas las opciones evaluadas, incluso frente a las desechables</strong>. Y remata: comprar localmente es clave.{sup(1)}</p>

        <p>Dicho sin rodeos: una toalla de tela fabricada en Asia, traída en avión y vendida como producto ecológico puede ser peor que la desechable que dice reemplazar.</p>

        <p class="pull">Coser en San Pedro Sula y vender en San Pedro Sula no es una historia de marca. Es la condición para que el argumento ambiental se sostenga.</p>

        <p>El mismo informe señala que, según el contexto geográfico, las toallas reutilizables lavadas de forma eficiente en energía sí tienen menor impacto que las desechables.{sup(1)} Las dos condiciones —producción local y lavado razonable— no son opcionales. Son lo que separa una toalla reutilizable que cumple de una que solo lo aparenta.</p>

        <h2>Tres maneras de cubrir un mercado</h2>

        <p>Cuando una marca de consumo masivo decide dónde estará disponible, elige entre tres intensidades de distribución. La categoría de higiene femenina opera, casi sin excepción, en la primera.</p>

        <figure class="figure">
          <img src="../assets/img/fig-distribucion.svg" alt="Diagrama comparativo de distribución intensiva, selectiva y exclusiva" width="780" height="330" loading="lazy">
          <figcaption>En distribución exclusiva la cobertura es la variable que se sacrifica. Lo que se compra a cambio es control sobre el precio, sobre el mensaje y sobre quién representa a la marca frente al cliente.</figcaption>
        </figure>

        <h3>Distribución intensiva</h3>
        <p>Estar en la mayor cantidad de puntos posible. Es la estrategia correcta cuando el producto se compra por impulso o por costumbre, y la decisión se toma en segundos frente al estante.</p>

        <h3>Distribución selectiva</h3>
        <p>Un número limitado de minoristas que cumplen ciertos criterios. Electrodomésticos, cosmética de gama media, calzado deportivo.</p>

        <h3>Distribución exclusiva</h3>
        <p>Un solo aliado por territorio, con contrato de exclusividad. Se usa cuando el producto necesita explicación, cuando el precio no puede erosionarse y cuando la marca no puede permitirse que un tercero la represente mal.</p>

        <h2>Cuatro razones para renunciar a la cobertura</h2>

        <h3>1. Una toalla reutilizable exige una conversación, no un empaque</h3>

        <p>Este es el punto decisivo, y es específico del producto. Una desechable no requiere explicación: se usa y se tira. Una toalla de tela requiere que alguien responda cuántas necesitás para un ciclo completo, cómo se lava, cuánto tarda en secar, cuántos años dura y qué hacer cuando estás fuera de casa.</p>

        <p>Ninguna de esas preguntas cabe en un empaque, y todas determinan si la compra termina en uso real o en un cajón. La revisión sistemática más amplia disponible sobre toallas reutilizables —cuarenta y cuatro estudios, cerca de catorce mil ochocientas participantes— identifica precisamente el lavado, el secado y la privacidad como las dificultades más reportadas por las usuarias.{sup(2)} Un producto cuyo principal obstáculo es de uso, no de compra, necesita un canal que enseñe.</p>

        <h3>2. Protege la posición de precio</h3>

        <p>Aura cuesta más de entrada que un paquete de desechables. Esa comparación solo tiene sentido repartida en los años que dura el producto, y hacer esa cuenta frente a una góndola no lo hace nadie. El contrato de exclusividad fija una política de precio única en los seis puntos: cuesta lo mismo en Guamilito que en Jardines del Valle, y eso es verificable.</p>

        <h3>3. Control de la promesa ambiental</h3>

        <p>La Comisión Europea revisó una muestra de afirmaciones ambientales usadas para vender productos y encontró que <strong>el 53 % daba información vaga, engañosa o infundada</strong>, y que el 40 % no tenía ninguna evidencia detrás. La mitad de las etiquetas verdes ofrece verificación débil o inexistente.{sup(3)}</p>

        <p>En un estante compartido, una marca que fabrica localmente y otra que importa por avión se ven igual de verdes a un metro de distancia. La distribución exclusiva saca a Aura de esa comparación y la lleva a un contexto donde la diferencia se puede explicar.</p>

        <h3>4. Capacidad real de un taller que cose</h3>

        <p>Hay una razón menos elegante y conviene decirla. Esto se cose, no se imprime: la producción inicial tiene un techo por costurera y por hora. Prometer presencia amplia y no cumplirla daña más que empezar chico y cumplir.</p>

        <h2>Por qué San Pedro Sula y no todo el país</h2>

        <p>Lanzar en cuatro ciudades a la vez habría significado dos puntos por plaza: presencia simbólica en todas partes y masa crítica en ninguna. San Pedro Sula reúne tres condiciones que el resto del país no tiene al mismo tiempo:</p>

        <ul>
          <li><strong>Densidad del segmento.</strong> Es la plaza comercial del país y donde se concentra la mayor cantidad de mujeres del perfil al que apunta la marca.</li>
          <li><strong>Tejido de comercio independiente.</strong> Farmacias de barrio y tiendas de producto natural donde la recomendación de mostrador todavía pesa más que el empaque. Ese canal es el que hace posible la estrategia.</li>
          <li><strong>Cero transporte para el producto.</strong> Se cose y se vende en la misma ciudad. Es la condición que el informe de la Life Cycle Initiative señala como determinante{sup(1)}, y acá se cumple por diseño, no por suerte.</li>
        </ul>

        <p>Concentrar el lanzamiento en una ciudad permite además medir: con seis puntos en un mismo mercado, las diferencias de rotación se explican por ejecución y no por variables regionales que no controlamos.</p>

        <h2>Cómo se eligieron los seis puntos</h2>

        <ol>
          <li><strong>Disposición a capacitarse.</strong> El personal recibe una sesión sobre materiales, tamaños, lavado y vida útil. Un punto que no acepta la capacitación no entra.</li>
          <li><strong>Exclusividad recíproca.</strong> El aliado no vende otra marca de toalla reutilizable mientras dure el acuerdo. Aura no vende a otro minorista dentro de su radio.</li>
          <li><strong>Cumplimiento de la política de precio.</strong> Precio único publicado, sin descuentos unilaterales.</li>
          <li><strong>Consulta previa del cliente.</strong> Comercios donde la gente pregunta antes de comprar, en lugar de tomar y pagar.</li>
          <li><strong>Reparto geográfico dentro de la ciudad.</strong> Los seis puntos cubren zonas distintas, sin solaparse. Dos aliados compitiendo por el mismo radio anulan el sentido de la exclusividad.</li>
        </ol>

        <div class="callout">
          <span class="callout__label">Qué gana el aliado</span>
          <p>La exclusividad no es una restricción disfrazada: es una contraprestación. El punto recibe margen superior al estándar de la categoría, capacitación pagada por la marca, material de exhibición propio y protección territorial frente a competidores directos dentro de su radio.</p>
          <p>A cambio, asume el compromiso de explicar el producto con precisión: cuántas toallas hacen falta, cómo se lavan y cuánto duran. Es un intercambio de cobertura por profundidad.</p>
        </div>

        <h2>Dónde encontrarlas desde el 1 de septiembre</h2>

        <p>Seis puntos, repartidos por la ciudad. La lista completa está en la <a href="../producto.html#puntos">página del producto</a> y se actualiza cada vez que cambia.</p>

        <ul>
          <li>Barrio Río de Piedras</li>
          <li>Avenida Circunvalación</li>
          <li>Colonia Trejo</li>
          <li>Colonia Jardines del Valle</li>
          <li>Barrio Guamilito</li>
          <li>Colonia Universidad</li>
        </ul>

        <p>La cifra se publica a propósito. Una marca que dice «disponible en puntos seleccionados» sin decir cuántos está usando la ambigüedad como recurso. Si el número es seis, decimos seis.</p>

        <h2>Qué sigue</h2>

        <p>La expansión avanza por fases, y cada una tiene una condición de entrada medible en lugar de una fecha:</p>

        <ol>
          <li><strong>Ampliar dentro de San Pedro Sula.</strong> Cuando los seis puntos sostengan seis meses sin quiebres de inventario.</li>
          <li><strong>Segunda plaza, Tegucigalpa.</strong> Requiere además un protocolo de capacitación replicable sin presencia directa del equipo. Y obliga a revisar el argumento de transporte: dejaría de ser producción y venta en la misma ciudad.</li>
          <li><strong>Transición a distribución selectiva.</strong> Solo cuando la marca tenga reputación propia suficiente para defenderse en un estante compartido.</li>
        </ol>

        <h2>Lo que este lanzamiento no va a afirmar</h2>

        <p>No vamos a decir que Aura es «cero residuo». Una toalla de tela reduce residuo; no lo elimina. Tiene una vida útil, se desgasta y en algún momento termina en la basura.</p>

        <p>No vamos a prometer beneficios de salud. Hay evidencia de menor irritación reportada al cambiar de desechables a reutilizables{sup(2)}, pero viene de estudios en contextos muy distintos al hondureño y con calidad metodológica que los propios autores califican de baja. Lo decimos como está.</p>

        <p>Y no vamos a decir que sirven para todo el mundo. Necesitan agua limpia, jabón y un lugar donde secar. Si no tenés esas tres cosas de forma confiable, este producto no es para vos, y preferimos decirlo antes de la compra que después.</p>
"""

A_LANZA_REFS = [
    'Life Cycle Initiative (PNUMA). <em>Single-use menstrual products and their alternatives: Recommendations from Life Cycle Assessments.</em> 2021. <a href="https://www.lifecycleinitiative.org/menstrual-products-and-sustainable-alternatives-report-2021/" rel="noopener">lifecycleinitiative.org</a>',
    'van Eijk, A.M. et al. <em>Exploring menstrual products: A systematic review and meta-analysis of reusable menstrual pads for public health internationally.</em> PLOS ONE, 2021. 44 estudios, ~14.800 participantes. <a href="https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0257610" rel="noopener">journals.plos.org</a>',
    'Comisión Europea. <em>Green claims.</em> Estudio de 2020 sobre afirmaciones ambientales. <a href="https://environment.ec.europa.eu/topics/circular-economy-topics/green-claims_en" rel="noopener">environment.ec.europa.eu</a>',
]

# ==========================================================================
# 2 · CICLO DE VIDA
# ==========================================================================

A_ACV = f"""
        <p>La intuición dice que una toalla lavable contamina menos que una desechable. La intuición tiene razón, pero con condiciones, y las condiciones son la parte interesante.</p>

        <p>Un análisis comparativo de ciclo de vida publicado en <em>Cleaner Environmental Systems</em> en 2022 evaluó tampones y toallas desechables —orgánicos y no orgánicos—, toallas reutilizables, ropa interior menstrual y copas, durante un año de uso, en ocho indicadores de impacto ambiental y en tres países: Francia, India y Estados Unidos. La conclusión general es clara: <strong>los productos menstruales reutilizables tienen impactos ambientales significativamente menores que los desechables</strong>.{sup(1)}</p>

        <h2>El hallazgo que incomoda a media industria</h2>

        <p>El mismo estudio reporta algo que casi nunca aparece en la publicidad de productos «eco»: <strong>los productos desechables orgánicos tienen impactos ambientales mayores que los no orgánicos</strong>.{sup(1)}</p>

        <p>No es un error de redacción. El algodón orgánico rinde menos por hectárea, así que producir la misma cantidad de fibra exige más tierra y más agua. Comprar una desechable de algodón orgánico puede ser peor, en varios indicadores, que comprar la convencional que estabas evitando.</p>

        <div class="callout">
          <span class="callout__label">Por qué publicamos esto</span>
          <p>Porque nos afecta. Aura vende un producto de fibra natural, y la lección del estudio es que «natural» no es sinónimo de «menor impacto». Lo que reduce el impacto en este caso no es el material: es que el producto se use muchas veces.</p>
        </div>

        <h2>La condición que casi nadie menciona</h2>

        <p>El informe de la Life Cycle Initiative del Programa de las Naciones Unidas para el Medio Ambiente, que compara los estudios de ciclo de vida disponibles sobre productos menstruales, es todavía más directo: <strong>las toallas reutilizables producidas en el extranjero y enviadas por vía aérea tienen los mayores impactos ambientales, incluso frente a las opciones de un solo uso</strong>. Por eso concluye que comprar localmente es clave.{sup(2)}</p>

        <p class="pull">Una toalla de tela traída en avión puede ser peor que la desechable que dice reemplazar. El material no salva al producto; la logística lo puede hundir.</p>

        <p>El segundo condicionante es el lavado. El mismo informe señala que el comportamiento de quien usa el producto es un determinante clave del impacto, y que con los reutilizables la usuaria tiene mucho más margen de influencia que con los desechables: lavados en frío o tibio y secados al aire, los reutilizables quedan por debajo de las alternativas de un solo uso.{sup(2)}</p>

        <p>Con una desechable, el impacto está decidido en la fábrica y no podés hacer nada. Con una reutilizable, una parte del impacto la decidís vos cada vez que la lavás. Es más responsabilidad, y también más control.</p>

        <h2>El punto de equilibrio</h2>

        <p>Un producto reutilizable arrastra una deuda ambiental inicial: fabricar una toalla de tela cuesta más recursos que fabricar una desechable. Esa deuda se paga con usos. Cuantas más veces se usa, más se reparte el impacto de fabricación entre cada ciclo.</p>

        <p>Por eso la vida útil no es un dato comercial, es una variable ambiental. La revisión sistemática de PLOS ONE, sobre 69 marcas, estimó una vida media de <strong>4.3 años</strong> por toalla reutilizable, con diferencias marcadas entre países de ingreso alto (4.9 años) y de ingreso bajo y medio (2.9 años).{sup(3)} Una revisión publicada en el <em>International Journal of Gynecology &amp; Obstetrics</em> ubica el rango general de las toallas de tela entre cinco y diez años de uso con lavado adecuado.{sup(4)}</p>

        <p>La diferencia entre 2.9 y 4.9 años no está en la tela. Está en el agua, el jabón, el secado y el trato. Es exactamente el motivo por el que el <a href="como-lavar-toallas-de-tela.html">cuidado</a> ocupa un artículo propio en este blog y una sesión de capacitación en cada punto de venta.</p>

        <h2>Cuánto residuo se evita</h2>

        <p>La misma revisión estimó, para escenarios de cinco años en países de ingreso bajo y medio, un ahorro aproximado de <strong>entre 600 y 1.600 toallas desechables</strong> por persona, según cuántas unidades reutilizables se usen por periodo.{sup(3)}</p>

        <p>Conviene leer ese número con cuidado: no es una promesa individual, es un rango de escenarios modelados. Tu resultado depende de cuántas toallas usés por ciclo, cuántos años te duren y si el cambio es total o parcial.</p>

        <h2>Qué se puede afirmar con honestidad</h2>

        <ol>
          <li>Los reutilizables tienen impactos significativamente menores que los desechables en la comparación general.{sup(1)}</li>
          <li>Esa ventaja <strong>desaparece</strong> si el producto se fabrica lejos y viaja en avión.{sup(2)}</li>
          <li>Esa ventaja <strong>se reduce</strong> si el lavado es intensivo en energía o si la toalla se estropea antes de tiempo.{sup(2, 3)}</li>
          <li>«Orgánico» no equivale a «menor impacto»: en desechables, ocurre lo contrario.{sup(1)}</li>
        </ol>

        <p>Aura se cose en San Pedro Sula y se vende en San Pedro Sula. No es una decisión de identidad local: es la condición número dos de esa lista.</p>
"""

A_ACV_REFS = [
    'Fourcassier, S., Douziech, M., Pérez-López, P. y Schiebinger, L. <em>Menstrual products: A comparable Life Cycle Assessment.</em> Cleaner Environmental Systems, vol. 7, 2022. <a href="https://www.sciencedirect.com/science/article/pii/S2666789422000277" rel="noopener">sciencedirect.com</a>',
    'Life Cycle Initiative (PNUMA). <em>Single-use menstrual products and their alternatives: Recommendations from Life Cycle Assessments.</em> 2021. <a href="https://www.lifecycleinitiative.org/menstrual-products-and-sustainable-alternatives-report-2021/" rel="noopener">lifecycleinitiative.org</a>',
    'van Eijk, A.M. et al. <em>Exploring menstrual products: A systematic review and meta-analysis of reusable menstrual pads for public health internationally.</em> PLOS ONE, 2021. <a href="https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0257610" rel="noopener">journals.plos.org</a>',
    'Harrison, M.E. y Tyson, N. <em>Menstruation: Environmental impact and need for global health equity.</em> International Journal of Gynecology &amp; Obstetrics, 2023. <a href="https://obgyn.onlinelibrary.wiley.com/doi/full/10.1002/ijgo.14311" rel="noopener">obgyn.onlinelibrary.wiley.com</a>',
]

# ==========================================================================
# 3 · VIDA ÚTIL Y AHORRO
# ==========================================================================

A_VIDA = f"""
        <p>Toda marca de toallas reutilizables promete ahorro. Casi ninguna publica la cuenta completa, porque la cuenta completa incluye una inversión inicial incómoda y un supuesto que puede fallar: que el producto dure lo que dice durar.</p>

        <h2>Cuánto duran, según los datos</h2>

        <p>La revisión sistemática más amplia disponible revisó 69 marcas comerciales de toallas reutilizables y estimó una vida media de <strong>4.3 años</strong>, con una desviación estándar de 2.3 años. El promedio en países de ingreso alto fue de 4.9 años y en países de ingreso bajo y medio, de 2.9 años.{sup(1)}</p>

        <p>Una revisión publicada en el <em>International Journal of Gynecology &amp; Obstetrics</em> señala que la mayoría de las toallas de tela pueden lavarse y reutilizarse durante cinco a diez años, y la ropa interior menstrual entre dos y seis.{sup(2)}</p>

        <p>Los dos rangos no se contradicen: uno mide lo que ocurre en la práctica y el otro lo que el producto permite en buenas condiciones. La diferencia entre ambos es el cuidado.</p>

        <p class="pull">La misma toalla puede durar tres años o siete. La variable no es la tela: es el agua caliente, el suavizante y el secado al sol o a la sombra.</p>

        <h2>La cuenta del ahorro</h2>

        <p>La misma revisión modeló escenarios de costo a cinco años. En países de ingreso bajo y medio, usar entre 4 y 25 toallas reutilizables por periodo resultó más barato —entre 170 y 417 dólares de diferencia— que usar entre 9 y 25 desechables por periodo, con un ahorro de residuo estimado de unas 600 a 1.600 toallas desechables.{sup(1)}</p>

        <p>El precio promedio de una toalla reutilizable entre esas 69 marcas fue de 8.95 dólares, con una diferencia enorme entre mercados: 2.06 dólares en países de ingreso bajo y medio frente a 10.11 en países de ingreso alto.{sup(1)}</p>

        <div class="callout">
          <span class="callout__label">Cómo leer esos números en Honduras</span>
          <p>Son escenarios modelados, no una promesa. El resultado real depende de cuántas toallas uses por ciclo, cuánto te duren, y de si el cambio es total o combinado con desechables.</p>
          <p>Lo honesto es decir que el ahorro existe y llega después, no de inmediato. La inversión inicial de un juego completo es varias veces el costo de un paquete de desechables. Se recupera con el tiempo, no en el primer ciclo.</p>
        </div>

        <h2>Cuántas necesitás realmente</h2>

        <p>Es la pregunta que más recibimos y la que más determina si el cambio funciona. Depende de dos cosas: tu flujo y cada cuánto lavás.</p>

        <ul>
          <li><strong>Si lavás todos los días:</strong> alcanza con un juego pequeño, del orden de cinco a siete unidades entre diario y día.</li>
          <li><strong>Si lavás cada dos o tres días:</strong> necesitás un juego completo, del orden de diez a doce, para no quedarte sin toallas secas.</li>
          <li><strong>Si querés probar sin comprometerte:</strong> empezá con dos o tres para los días de flujo bajo y mantené desechables para el resto. Es un cambio parcial, y sigue siendo un cambio.</li>
        </ul>

        <p>Comprar de menos es el error más frecuente y el que hace abandonar el producto: te quedás sin toallas secas a mitad del ciclo, volvés a las desechables por urgencia y el juego termina en un cajón. Es preferible empezar con pocas y ampliar, que comprar un juego incompleto y darlo por fallido.</p>

        <h2>Qué acorta la vida útil</h2>

        <p>Cuatro cosas, en orden de daño:</p>

        <ol>
          <li><strong>Suavizante de telas.</strong> Deja una película que impermeabiliza la fibra. Una toalla que absorbe menos con el tiempo casi siempre estuvo en contacto con suavizante.</li>
          <li><strong>Agua muy caliente en el primer enjuague.</strong> Fija la mancha en la fibra en lugar de removerla.</li>
          <li><strong>Cloro.</strong> Blanquea, sí, y a cambio degrada el tejido y acorta la vida del producto.</li>
          <li><strong>Guardarlas húmedas.</strong> Es el origen del olor persistente y de la mancha que ya no sale.</li>
        </ol>

        <p>Las cuatro están desarrolladas en <a href="como-lavar-toallas-de-tela.html">el artículo sobre lavado</a>. Vale la pena leerlo antes del primer uso y no después del primer problema.</p>

        <h2>Lo que no te podemos prometer</h2>

        <p>No podemos garantizarte cinco años. Podemos decirte que la literatura ubica el promedio real en torno a 4.3 años{sup(1)}, que el rango posible llega a diez con buen cuidado{sup(2)}, y que la diferencia entre un extremo y otro está casi por completo en cómo se lava.</p>

        <p>Tampoco podemos decirte que vas a ahorrar desde el primer mes. Vas a gastar más al inicio. El ahorro aparece más adelante, y depende de que el producto te dure.</p>
"""

A_VIDA_REFS = [
    'van Eijk, A.M. et al. <em>Exploring menstrual products: A systematic review and meta-analysis of reusable menstrual pads for public health internationally.</em> PLOS ONE, 2021. Datos sobre 69 marcas, vida útil media y escenarios de costo a cinco años. <a href="https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0257610" rel="noopener">journals.plos.org</a>',
    'Harrison, M.E. y Tyson, N. <em>Menstruation: Environmental impact and need for global health equity.</em> International Journal of Gynecology &amp; Obstetrics, 2023. <a href="https://obgyn.onlinelibrary.wiley.com/doi/full/10.1002/ijgo.14311" rel="noopener">obgyn.onlinelibrary.wiley.com</a>',
    'Fourcassier, S. et al. <em>Menstrual products: A comparable Life Cycle Assessment.</em> Cleaner Environmental Systems, 2022. <a href="https://www.sciencedirect.com/science/article/pii/S2666789422000277" rel="noopener">sciencedirect.com</a>',
]

# ==========================================================================
# 4 · LAVADO
# ==========================================================================

A_LAVADO = f"""
        <p>La revisión sistemática más amplia sobre toallas reutilizables, que reunió 44 estudios y cerca de catorce mil ochocientas participantes, identificó las dificultades con el lavado y el cambio como uno de los obstáculos más reportados: falta de agua, de privacidad, de jabón, de recipientes y de lugares donde secar.{sup(1)}</p>

        <p>Es decir: el problema de este producto casi nunca es el producto. Es la rutina. Por eso este artículo es más largo que la ficha técnica.</p>

        <figure class="figure">
          <img src="../assets/img/producto-bano.jpg" alt="Bolsa de transporte Aura con estampado de hojas sobre una repisa de baño, junto a la caja de cartón kraft de la marca y toallas dobladas" width="1024" height="559" loading="lazy">
          <figcaption>La bolsa impermeable acompaña al producto porque resuelve el punto más difícil: qué hacer con una toalla usada cuando no estás en tu casa.</figcaption>
        </figure>

        <h2>La rutina, en cuatro pasos</h2>

        <h3>1. Enjuagar en frío, apenas se pueda</h3>
        <p>Agua fría, siempre. El agua caliente coagula la proteína de la sangre y la fija a la fibra: la mancha deja de ser una mancha superficial y pasa a ser parte del tejido. Enjuagá bajo el chorro hasta que el agua salga clara.</p>
        <p>Si no podés hacerlo en el momento, no pasa nada: dobla la toalla hacia adentro, cerrala con el broche y guardala en la bolsa impermeable hasta llegar a tu casa.</p>

        <h3>2. Remojar, si hace falta</h3>
        <p>Para manchas que ya se secaron, remojo en agua fría entre treinta minutos y un par de horas. Cambiá el agua si se oscurece mucho. No hace falta más tiempo, y dejarlas remojando toda la noche desgasta la fibra sin mejorar el resultado.</p>

        <h3>3. Lavar con jabón neutro</h3>
        <p>A mano o en máquina, con agua fría o tibia. Detergente común sin blanqueador, o jabón neutro. Nada de suavizante.</p>

        <h3>4. Secar completamente antes de guardar</h3>
        <p>Al aire libre si se puede. El secado completo es la parte que más se descuida y la que más problemas causa: una toalla guardada húmeda desarrolla olor y manchas que después ya no salen.</p>

        <div class="callout">
          <span class="callout__label">Sobre secar al sol</span>
          <p>El sol ayuda a aclarar manchas leves y es la forma más barata de secar. Circula también la idea de que la radiación ultravioleta desinfecta la tela; es una afirmación que se repite mucho en blogs y que no vamos a presentar como si estuviera demostrada para este uso, porque no tenemos un estudio que lo respalde.</p>
          <p>Lo que sí podemos decir con confianza: un lavado con jabón y un secado completo son las dos condiciones que importan. La revisión sistemática de PLOS ONE, con 44 estudios, no reportó casos objetivos de infección asociados al uso de toallas reutilizables.{sup(1)}</p>
        </div>

        <h2>Lo que nunca</h2>

        <ul>
          <li><strong>Suavizante.</strong> Recubre la fibra con una película que repele el líquido. Es la causa número uno de que una toalla «deje de absorber».</li>
          <li><strong>Cloro.</strong> Degrada el tejido y acorta la vida útil del producto. La mancha se va; la toalla también, más rápido.</li>
          <li><strong>Agua caliente en el primer enjuague.</strong> Fija la mancha de forma prácticamente irreversible.</li>
          <li><strong>Plancha sobre la capa impermeable.</strong> El calor directo puede dañar la lámina interior que impide el traspaso.</li>
          <li><strong>Guardarlas sin secar del todo.</strong> Origen de olor y de manchas permanentes.</li>
        </ul>

        <h2>Las manchas y lo que hay que aceptar</h2>

        <p>Con el tiempo, la tela de contacto puede tomar un tono más oscuro. No significa que esté sucia ni que haya perdido capacidad de absorción: significa que se usó. Una toalla limpia con marca de uso es un producto funcionando, no un producto fallado.</p>

        <p>Si te molesta visualmente, los estampados y los tonos medios —el salvia y el rosado de Aura— disimulan bastante más que un blanco liso. Es una de las razones por las que la línea no tiene una versión blanca.</p>

        <h2>Fuera de casa</h2>

        <p>Es la duda que más frena la compra, y tiene una respuesta sencilla. Doblás la toalla usada con la cara de contacto hacia adentro, la cerrás con su propio broche y la guardás en la bolsa impermeable. Queda cerrada, sin olor perceptible y sin contacto con el resto de tus cosas. En casa seguís la rutina normal.</p>

        <p>Para una jornada larga fuera, dos o tres toallas y la bolsa alcanzan sin problema.</p>

        <h2>Cuándo reemplazar una toalla</h2>

        <p>Tres señales, ninguna relacionada con el color:</p>

        <ol>
          <li>Absorbe visiblemente menos que las demás del juego, incluso después de un lavado sin suavizante.</li>
          <li>La capa impermeable dejó pasar líquido a la ropa dos veces seguidas sin que hubiera desborde por saturación.</li>
          <li>El broche no cierra o la costura se abrió.</li>
        </ol>

        <p>Fuera de eso, una toalla manchada pero funcional sigue siendo una toalla funcional. La literatura ubica la vida media real en torno a 4.3 años, con un rango que llega a diez años con buen cuidado.{sup(2, 3)} Casi toda esa diferencia se decide en el lavado.</p>

        <h2>Si no tenés agua confiable</h2>

        <p>Decirlo es parte de vender esto con honestidad. Este producto necesita agua limpia, jabón y un lugar donde secar. La revisión de PLOS ONE documenta que, donde esas condiciones faltan, el lavado y el secado se vuelven el principal obstáculo de uso.{sup(1)}</p>

        <p>Si en tu casa el agua es intermitente o no tenés dónde secar con privacidad, este producto probablemente no te va a funcionar, y preferimos que lo sepas antes de comprarlo.</p>
"""

A_LAVADO_REFS = [
    'van Eijk, A.M. et al. <em>Exploring menstrual products: A systematic review and meta-analysis of reusable menstrual pads for public health internationally.</em> PLOS ONE, 2021. 44 estudios, ~14.800 participantes. <a href="https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0257610" rel="noopener">journals.plos.org</a>',
    'Harrison, M.E. y Tyson, N. <em>Menstruation: Environmental impact and need for global health equity.</em> International Journal of Gynecology &amp; Obstetrics, 2023. <a href="https://obgyn.onlinelibrary.wiley.com/doi/full/10.1002/ijgo.14311" rel="noopener">obgyn.onlinelibrary.wiley.com</a>',
    'Life Cycle Initiative (PNUMA). <em>Single-use menstrual products and their alternatives.</em> 2021. Sobre el efecto del método de lavado en el impacto ambiental. <a href="https://www.lifecycleinitiative.org/menstrual-products-and-sustainable-alternatives-report-2021/" rel="noopener">lifecycleinitiative.org</a>',
]

# ==========================================================================
# 5 · GREENWASHING
# ==========================================================================

A_GREEN = f"""
        <p>En 2020 la Comisión Europea revisó una muestra de afirmaciones ambientales usadas para vender productos y servicios en la Unión Europea. El resultado es incómodo para cualquiera que trabaje en mercadeo: <strong>el 53 % de esas afirmaciones daba información vaga, engañosa o infundada</strong>, y el 40 % no tenía ninguna evidencia que la respaldara.{sup(1)}</p>

        <p>El mismo diagnóstico agrega dos datos que explican por qué el problema se sostiene: la mitad de las etiquetas verdes ofrece verificación débil o inexistente, y en el mercado europeo circulan unas 230 etiquetas de sostenibilidad con niveles de transparencia muy dispares.{sup(1)}</p>

        <p class="pull">Cuando la mitad de los sellos no verifica nada, un sello deja de ser información y pasa a ser decoración.</p>

        <h2>Por qué esto es un problema de mercadeo</h2>

        <p>La consecuencia obvia es que quien compra no puede elegir bien. La menos obvia, y más relevante para quien construye una marca, es que el greenwashing <strong>castiga a las empresas que sí invirtieron</strong>. Si una marca fabrica localmente para no cargar transporte aéreo y absorbe el costo mayor que eso implica, compite en el mismo estante contra otra que importa contenedores y solo imprime una hoja verde en el empaque. A igualdad de mensaje percibido, gana la que gastó menos.</p>

        <p>Ese fue el razonamiento de la Comisión Europea al proponer en 2023 la Directiva de Afirmaciones Verdes: exigir que toda afirmación ambiental se sustente con datos verificables y perspectiva de ciclo de vida completo.{sup(2)}</p>

        <h2>Las cuatro trampas de esta categoría</h2>

        <h3>1. «Reutilizable» presentado como sinónimo de «sostenible»</h3>
        <p>Es la trampa específica de nuestro propio producto, y por eso va primera. El informe de la Life Cycle Initiative del PNUMA concluye que las toallas reutilizables producidas en el extranjero y transportadas por vía aérea tienen los mayores impactos ambientales de todas las opciones evaluadas, <strong>incluso frente a las desechables</strong>.{sup(3)}</p>
        <p>La pregunta útil no es si un producto es reutilizable. Es dónde se fabricó, cómo llegó hasta acá y cuántas veces se va a usar.</p>

        <h3>2. El adjetivo sin norma</h3>
        <p>«Biodegradable» sin plazo, sin condición y sin norma de referencia. Prácticamente todo es biodegradable con tiempo suficiente. Las guías de publicidad ambiental de la Comisión Federal de Comercio de Estados Unidos consideran engañoso el término sin evidencia de ensayo específica.{sup(4)}</p>

        <h3>3. El sello propio</h3>
        <p>Un logo verde diseñado internamente, sin organismo certificador detrás. Con 230 etiquetas en circulación, distinguir a simple vista cuál tiene auditoría independiente y cuál es un gráfico bonito es prácticamente imposible.{sup(1)}</p>

        <h3>4. La palabra «natural»</h3>
        <p>No tiene definición regulatoria en esta categoría, y hay evidencia directa de que no predice menor impacto. El análisis comparativo de ciclo de vida publicado en <em>Cleaner Environmental Systems</em> encontró que los productos desechables orgánicos tienen impactos ambientales <strong>mayores</strong> que los no orgánicos.{sup(5)}</p>

        <h2>Qué queda cuando se quitan las palabras vacías</h2>

        <ol>
          <li><strong>Dónde se fabrica.</strong> Verificable, y determinante según la evidencia de ciclo de vida.{sup(3)}</li>
          <li><strong>La lista de materiales con proporciones.</strong> Es un dato, no una promesa.</li>
          <li><strong>La vida útil declarada, con su fuente.</strong> Si una marca afirma diez años, que diga de dónde sale el número.</li>
          <li><strong>Lo que el producto no resuelve.</strong> Una marca que solo enumera ventajas está vendiendo, no informando.</li>
        </ol>

        <h2>Cómo se aplica esto a Aura</h2>

        <p>Aura se cose en San Pedro Sula y se vende en San Pedro Sula: cero transporte para el producto terminado. No es una historia de identidad local, es la condición que la evidencia señala como determinante.{sup(3)}</p>

        <p>Y publicamos los datos que nos incomodan: que «orgánico» no equivale a menor impacto{sup(5)}, que la vida útil media real observada es de 4.3 años y no de diez{sup(6)}, y que si no tenés agua limpia y un lugar donde secar, este producto no te va a funcionar.</p>

        <div class="callout">
          <span class="callout__label">Para quien estudia mercadeo</span>
          <p>La lectura estratégica es que la transparencia radical dejó de ser un gesto ético y pasó a ser una <strong>posición competitiva defendible</strong>. En una categoría donde la mitad de las etiquetas no verifica nada, publicar información contrastable es de las pocas señales que la competencia no puede imitar sin incurrir en el mismo costo.</p>
          <p>Cuando todos dicen lo mismo, el diferencial no está en decirlo mejor, sino en decir algo que se pueda comprobar.</p>
        </div>
"""

A_GREEN_REFS = [
    'Comisión Europea. <em>Green claims.</em> Estudio de 2020: 53 % de afirmaciones vagas, engañosas o infundadas; 40 % sin evidencia; 230 etiquetas de sostenibilidad en circulación. <a href="https://environment.ec.europa.eu/topics/circular-economy-topics/green-claims_en" rel="noopener">environment.ec.europa.eu</a>',
    'Comisión Europea. <em>Consumer protection: enabling sustainable choices and ending greenwashing.</em> Comunicado de prensa, marzo de 2023. <a href="https://ec.europa.eu/commission/presscorner/detail/en/ip_23_1692" rel="noopener">ec.europa.eu</a>',
    'Life Cycle Initiative (PNUMA). <em>Single-use menstrual products and their alternatives.</em> 2021. <a href="https://www.lifecycleinitiative.org/menstrual-products-and-sustainable-alternatives-report-2021/" rel="noopener">lifecycleinitiative.org</a>',
    'Ecofy. <em>ASTM D6400 Compostability Standard.</em> Incluye la referencia a las Green Guides de la FTC. <a href="https://ecofy.io/resources/compliance/astm-d6400/" rel="noopener">ecofy.io</a>',
    'Fourcassier, S. et al. <em>Menstrual products: A comparable Life Cycle Assessment.</em> Cleaner Environmental Systems, 2022. <a href="https://www.sciencedirect.com/science/article/pii/S2666789422000277" rel="noopener">sciencedirect.com</a>',
    'van Eijk, A.M. et al. <em>Exploring menstrual products.</em> PLOS ONE, 2021. <a href="https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0257610" rel="noopener">journals.plos.org</a>',
]

# ==========================================================================
# 6 · POBREZA MENSTRUAL
# ==========================================================================

A_POBREZA = f"""
        <p>Cada mes menstrúan más de dos mil millones de personas en el mundo. Millones de ellas no pueden pagar los productos necesarios para gestionarlo, ni tienen acceso a agua y saneamiento seguros para hacerlo con dignidad.{sup(1)} A esa combinación se le llama pobreza menstrual, y no es un problema de higiene: es un problema de acceso.</p>

        <h2>La cifra que ordena la conversación</h2>

        <p>ONU Mujeres América Latina y el Caribe, citando datos de la Organización Mundial de la Salud, señala que en la región <strong>dos de cada cinco niñas faltan a la escuela durante su menstruación</strong>, un ausentismo agravado por el estigma que rodea el tema.{sup(2)}</p>

        <p>Otras mediciones llegan a órdenes similares. Un comunicado de AIDS Healthcare Foundation de 2024 estima que una de cada tres adolescentes en América Latina falta a clases de manera regular por no contar con lo necesario.{sup(3)} La UNESCO, con alcance global, calcula que una de cada diez jóvenes en edad menstrual pierde días de clase por falta de acceso a recursos menstruales.{sup(4)}</p>

        <p class="pull">Faltar tres o cuatro días al mes, mes tras mes, no es una molestia. Es una fracción del año escolar que no se recupera.</p>

        <h2>Dónde encajan los productos reutilizables, y dónde no</h2>

        <p>Un producto reutilizable parece la respuesta obvia a un problema de costo recurrente, y en parte lo es: la evidencia de escenarios a cinco años en países de ingreso bajo y medio muestra que las toallas reutilizables resultan más baratas que las desechables, con diferencias del orden de 170 a 417 dólares.{sup(5)}</p>

        <p>Pero hay una condición que conviene no borrar. La misma revisión documenta que las dificultades más reportadas por las usuarias son el lavado y el secado, por falta de agua, jabón, recipientes, privacidad y lugares donde tender.{sup(5)}</p>

        <p>Entregar toallas reutilizables donde no hay agua confiable no resuelve la pobreza menstrual: la traslada. Es una distinción que las campañas de donación suelen pasar por alto, y que cambia por completo el diseño de un programa.</p>

        <div class="callout">
          <span class="callout__label">Un matiz que nos toca directamente</span>
          <p>Aura vende un producto que exige agua limpia, jabón y un lugar donde secar. Eso significa que, tal como está, <strong>no es una solución para los contextos de mayor privación</strong>, que son justamente los que definen la pobreza menstrual.</p>
          <p>Decirlo nos quita un argumento de venta cómodo. Omitirlo sería usar un problema social como material publicitario.</p>
        </div>

        <h2>Qué han hecho otros países de la región</h2>

        <ul>
          <li><strong>Impuestos.</strong> Colombia eliminó en 2018 el impuesto sobre las toallas sanitarias. México siguió en 2021, cuando el movimiento Menstruación Digna logró retirar el 16 % de IVA a los productos de gestión menstrual.{sup(6)}</li>
          <li><strong>Distribución directa.</strong> Uruguay lanzó en 2023 un programa de kits gratuitos en Montevideo. Brasil anunció distribución gratuita en farmacias para mujeres de bajos recursos.{sup(6)}</li>
          <li><strong>Datos.</strong> México levantó una Encuesta Nacional sobre Gestión Menstrual junto con UNICEF, Essity y Menstruación Digna.{sup(3)}</li>
        </ul>

        <p>La secuencia importa: primero medir, después legislar. Sin la encuesta, el debate se queda en anécdotas.</p>

        <h2>Dónde queda Honduras</h2>

        <p>Honduras no aparece entre los países con una política pública articulada sobre gestión menstrual, ni con una encuesta nacional que permita dimensionar el problema con datos propios. Esa ausencia de información es, en sí misma, un dato.</p>

        <h2>Lo que sí nos corresponde</h2>

        <ol>
          <li><strong>Precio por unidad y vida útil visibles.</strong> Para que la comparación con desechables se pueda hacer con números y no con intuición.</li>
          <li><strong>Contenido abierto.</strong> Los artículos de este sitio, con sus referencias, se pueden reproducir libremente con atribución para uso educativo. El de <a href="como-lavar-toallas-de-tela.html">lavado</a> es el más útil para talleres.</li>
          <li><strong>Precio de costo para programas escolares</strong>, con una condición: que el programa incluya acceso a agua y jabón donde se vaya a distribuir. Sin eso, entregar producto es trasladar el problema.</li>
        </ol>

        <div class="callout">
          <span class="callout__label">Si trabajás en esto</span>
          <p>Escribinos a <a href="mailto:hola@aura.hn">hola@aura.hn</a> con el nombre de la institución y el número aproximado de participantes. No pedimos exclusividad, ni logo, ni fotos.</p>
        </div>
"""

A_POBREZA_REFS = [
    'ONU Mujeres. <em>Pobreza asociada a la menstruación.</em> <a href="https://www.unwomen.org/es/articulos/articulo-explicativo/pobreza-asociada-a-la-menstruacion-por-que-millones-de-ninas-y-mujeres-no-pueden-permitirse-los-productos-menstruales" rel="noopener">unwomen.org</a>',
    'ONU Mujeres América Latina y el Caribe, citando datos de la OMS.',
    'AIDS Healthcare Foundation México. <em>28 de mayo, Día de la Salud e Higiene Menstrual.</em> 2024. <a href="https://ahfmexico.org.mx/28-de-mayo-dia-de-la-salud-e-higiene-menstrual-la-pobreza-menstrual/" rel="noopener">ahfmexico.org.mx</a>',
    'UNESCO, citada en informes regionales sobre acceso a recursos menstruales.',
    'van Eijk, A.M. et al. <em>Exploring menstrual products.</em> PLOS ONE, 2021. Escenarios de costo a cinco años y obstáculos de lavado y secado. <a href="https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0257610" rel="noopener">journals.plos.org</a>',
    'Voices! Consultancy. <em>Desigualdades íntimas: la pobreza menstrual en América Latina.</em> <a href="https://www.voicesconsultancy.com/Prensa/Desigualdades-intimas-la-pobreza-menstrual-en-America-Latina" rel="noopener">voicesconsultancy.com</a>',
]

# ==========================================================================
# Ensamblado
# ==========================================================================

ARTICLES = [
    dict(slug="lanzamiento-aura-san-pedro-sula.html", key="lanza", kicker="LANZAMIENTO",
         title="Aura llega a San Pedro Sula, y solo a seis lugares",
         dek="Toallas sanitarias de tela reutilizables, cosidas en la ciudad, que salen a la venta el 1 de septiembre sin pasar por el supermercado. La decisión de canal es deliberada, y explicarla es parte del producto.",
         desc="Lanzamiento de Aura, marca hondureña de toallas sanitarias reutilizables, con estrategia de distribución exclusiva en San Pedro Sula: seis puntos de venta, precio único y exclusividad recíproca.",
         read="10 min", body=A_LANZA, refs=A_LANZA_REFS,
         related=["acv", "vida", "green"]),
    dict(slug="reutilizable-o-desechable.html", key="acv", kicker="EVIDENCIA",
         title="Reutilizable contra desechable: lo que midieron los análisis de ciclo de vida",
         dek="Los reutilizables ganan la comparación general, pero con dos condiciones que casi ninguna marca menciona. Una de ellas puede invertir el resultado por completo.",
         desc="Qué dicen los análisis comparativos de ciclo de vida sobre toallas reutilizables frente a desechables, incluida la condición de producción local señalada por la Life Cycle Initiative del PNUMA.",
         read="8 min", body=A_ACV, refs=A_ACV_REFS,
         related=["vida", "lavado", "green"]),
    dict(slug="cuanto-dura-cuanto-ahorra.html", key="vida", kicker="ECONOMÍA",
         title="Cuánto dura una toalla de tela y cuánto ahorra de verdad",
         dek="Vida media observada de 4.3 años, rango posible hasta diez, y una inversión inicial que no se recupera en el primer ciclo. La cuenta completa, con sus supuestos a la vista.",
         desc="Datos sobre vida útil y ahorro de las toallas sanitarias reutilizables según la revisión sistemática de PLOS ONE sobre 69 marcas, y cuántas unidades hacen falta realmente.",
         read="7 min", body=A_VIDA, refs=A_VIDA_REFS,
         related=["acv", "lavado", "lanza"]),
    dict(slug="como-lavar-toallas-de-tela.html", key="lavado", kicker="CUIDADO",
         title="Cómo lavarlas sin arruinarlas",
         dek="El obstáculo de este producto casi nunca es el producto: es la rutina. Cuatro pasos, cinco errores que acortan la vida útil, y qué hacer cuando estás fuera de casa.",
         desc="Guía de lavado, secado y conservación de toallas sanitarias reutilizables, con las dificultades de uso documentadas en la revisión sistemática de PLOS ONE.",
         read="8 min", body=A_LAVADO, refs=A_LAVADO_REFS,
         related=["vida", "acv", "pobreza"]),
    dict(slug="greenwashing-marketing-verde.html", key="green", kicker="MERCADEO",
         title="Greenwashing: el 53 % de las promesas verdes no resiste una revisión",
         dek="La Comisión Europea auditó las afirmaciones ambientales del mercado y encontró que más de la mitad eran vagas o infundadas. La primera trampa de la lista es la de nuestra propia categoría.",
         desc="Datos de la Comisión Europea sobre afirmaciones ambientales engañosas y las cuatro trampas más comunes en el mercadeo de productos menstruales reutilizables.",
         read="9 min", body=A_GREEN, refs=A_GREEN_REFS,
         related=["acv", "lanza", "pobreza"]),
    dict(slug="pobreza-menstrual-america-latina.html", key="pobreza", kicker="CONTEXTO",
         title="Pobreza menstrual: el costo de no poder elegir",
         dek="Dos de cada cinco niñas de la región faltan a clases durante su periodo. Por qué un producto reutilizable ayuda menos de lo que parece donde no hay agua confiable.",
         desc="Datos de ONU Mujeres, UNESCO y AHF sobre pobreza menstrual en América Latina, y los límites de los productos reutilizables como respuesta.",
         read="7 min", body=A_POBREZA, refs=A_POBREZA_REFS,
         related=["lavado", "vida", "green"]),
]

AUTHOR = "Equipo Aura"
DATE = "Publicado el 9 de agosto de 2026"

for a in ARTICLES:
    rel = [REL[k] for k in a["related"]]
    body = article(a["kicker"], a["title"], a["dek"], AUTHOR, DATE, a["read"],
                   a["body"], a["refs"], rel)
    render("articulos/" + a["slug"], a["title"] + " — Aura", a["desc"],
           body, depth=1, active="sci", ogtype="article", progress=True)
