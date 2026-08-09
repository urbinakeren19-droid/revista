#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Artículo de lanzamiento — pieza central del sitio."""

from build_pages import render, article, sup, REL

BODY = f"""
        <p>Aura sale a la venta en San Pedro Sula el 1 de septiembre. Es una toalla sanitaria con superficie de bambú hilado, núcleo de celulosa de pulpa certificada y base de PLA derivado de almidón de maíz, sin perfume, sin colorante y sin blanqueo con cloro elemental.</p>

        <p>Y no la vas a encontrar en el supermercado.</p>

        <p>No es un problema de producción ni una promesa de «pronto en más puntos». Es una decisión de canal tomada antes de fabricar la primera unidad. Aura arranca con <strong>seis puntos de venta, todos en San Pedro Sula</strong>, cada uno con un acuerdo de exclusividad firmado. Este artículo explica por qué, porque la razón es también el argumento del producto.</p>

        <h2>Tres maneras de cubrir un mercado</h2>

        <p>Cuando una marca de consumo masivo decide dónde estará disponible, elige entre tres intensidades de distribución. La categoría de higiene femenina opera, casi sin excepción, en la primera.</p>

        <figure class="figure">
          <img src="../assets/img/fig-distribucion.svg" alt="Diagrama comparativo de distribución intensiva, selectiva y exclusiva: la intensiva ocupa todos los puntos, la selectiva ocupa cerca de la mitad, la exclusiva ocupa tres puntos destacados" width="780" height="330" loading="lazy">
          <figcaption>En distribución exclusiva la cobertura es la variable que se sacrifica. Lo que se compra a cambio es control sobre el precio, sobre el mensaje y sobre quién representa a la marca frente al cliente.</figcaption>
        </figure>

        <h3>Distribución intensiva</h3>
        <p>Estar en la mayor cantidad de puntos posible. Es la estrategia correcta cuando el producto se compra por impulso, por costumbre o por precio, y cuando la decisión se toma en segundos frente al estante. Toallas, papel higiénico, jabón, refrescos.</p>

        <h3>Distribución selectiva</h3>
        <p>Un número limitado de minoristas que cumplen ciertos criterios. Electrodomésticos, cosmética de gama media, calzado deportivo.</p>

        <h3>Distribución exclusiva</h3>
        <p>Un solo aliado por territorio, con contrato de exclusividad. Se usa cuando el producto necesita explicación, cuando el precio no puede erosionarse y cuando la marca no puede permitirse que un tercero la represente mal. Automóviles, relojería, equipo profesional.</p>

        <p class="pull">Una toalla sanitaria pertenece por naturaleza al primer grupo. Aura eligió el tercero, y esa contradicción aparente es exactamente el punto.</p>

        <h2>Por qué San Pedro Sula y no todo el país</h2>

        <p>Antes de elegir puntos hay que elegir ciudad. Lanzar en cuatro ciudades a la vez con producción inicial habría significado dos o tres puntos por plaza: presencia simbólica en todas partes y masa crítica en ninguna.</p>

        <p>San Pedro Sula concentra tres condiciones que el resto del país no reúne al mismo tiempo:</p>

        <ul>
          <li><strong>Densidad del segmento.</strong> Es la plaza comercial del país y donde se concentra la mayor cantidad de mujeres del perfil al que apunta la marca: urbanas, con ingreso propio, que ya cambiaron otros productos de su rutina por versiones sin fragancia.</li>
          <li><strong>Tejido de comercio independiente.</strong> Farmacias de barrio y tiendas de producto natural donde la recomendación de mostrador todavía pesa más que el empaque. Ese canal es el que hace posible la estrategia; sin él, la distribución exclusiva no tendría dónde apoyarse.</li>
          <li><strong>Logística de un solo radio.</strong> Reposición desde una bodega, sin transporte interurbano. Menos costo por unidad y, sobre todo, capacidad de resolver un quiebre de inventario el mismo día.</li>
        </ul>

        <p>Concentrar el lanzamiento en una ciudad permite además algo que la dispersión impide: medir. Con seis puntos en un mismo mercado, las diferencias de rotación entre uno y otro se explican por ejecución, no por variables regionales que no controlamos.</p>

        <h2>Cuatro razones para renunciar a la cobertura</h2>

        <h3>1. El producto no se explica solo en un estante</h3>

        <p>El argumento de Aura no es «somos verdes». Es una <a href="../index.html#composicion">tabla de composición con siete componentes, sus porcentajes en peso y su vía de degradación</a>. Eso no se comunica en el segundo y medio que dura una decisión de góndola, entre veinte empaques que gritan.</p>

        <p>En un punto de venta exclusivo, con personal capacitado por la marca y material impreso propio, sí se comunica. La distribución exclusiva permite algo que la intensiva vuelve imposible: que quien vende el producto sepa qué está vendiendo.</p>

        <h3>2. Protege la posición de precio</h3>

        <p>Aura cuesta más que una toalla de supermercado, y va a seguir costando más. El bambú hilado y la celulosa certificada cuestan más por kilo que el polipropileno; el PLA cuesta más que el polietileno. No hay economía de escala que borre esa diferencia en el corto plazo.</p>

        <p>En distribución intensiva, un producto con precio superior entra en guerra de descuentos con el minorista y termina compitiendo contra sí mismo entre cadenas. El contrato de exclusividad fija una política de precio única en todos los puntos. Cuesta lo mismo en Guamilito que en Jardines del Valle, y eso es verificable.</p>

        <h3>3. Control de la promesa ambiental</h3>

        <p>Este es el punto que más pesó. La Comisión Europea revisó una muestra de afirmaciones ambientales usadas para vender productos y encontró que <strong>el 53 % daba información vaga, engañosa o infundada</strong>, y que el 40 % no tenía ninguna evidencia detrás.{sup(1)} La mitad de las etiquetas verdes ofrece verificación débil o inexistente.{sup(1)}</p>

        <p>En un estante compartido, Aura compite contra ese ruido en igualdad de condiciones aparentes: una marca que pagó ensayos de laboratorio y otra que imprimió una hoja verde se ven iguales a un metro de distancia. La distribución exclusiva saca a la marca de esa comparación y la traslada a un contexto donde la evidencia se puede mostrar.</p>

        <h3>4. Capacidad real de la fase de lanzamiento</h3>

        <p>Hay una razón menos elegante y conviene decirla. La producción inicial no alcanza para abastecer distribución nacional sin quiebres de inventario. Prometer presencia amplia y no cumplirla daña más que empezar chico y cumplir.</p>

        <h2>Cómo se eligieron los seis puntos</h2>

        <p>No fue por volumen de venta. Los criterios, en orden de peso:</p>

        <ol>
          <li><strong>Disposición a capacitarse.</strong> El personal recibe una sesión sobre composición, diferencias de material y qué no se puede afirmar del producto. Un punto que no acepta la capacitación no entra.</li>
          <li><strong>Exclusividad recíproca.</strong> El aliado no vende otra marca de toalla de fibra vegetal mientras dure el acuerdo. Aura no vende a otro minorista dentro de su radio.</li>
          <li><strong>Cumplimiento de la política de precio.</strong> Precio único publicado. Sin descuentos unilaterales, sin promociones cruzadas.</li>
          <li><strong>Consulta previa del cliente.</strong> Farmacias y tiendas de producto natural donde la gente ya pregunta antes de comprar, en lugar de tomar y pagar.</li>
          <li><strong>Reparto geográfico dentro de la ciudad.</strong> Los seis puntos cubren zonas distintas de San Pedro Sula, sin solaparse. Dos aliados compitiendo por el mismo radio anulan el sentido de la exclusividad.</li>
        </ol>

        <div class="callout">
          <span class="callout__label">Qué gana el aliado</span>
          <p>La exclusividad no es una restricción disfrazada: es una contraprestación. El punto recibe margen superior al estándar de la categoría, capacitación pagada por la marca, material de exhibición propio y protección territorial frente a competidores directos dentro de su radio.</p>
          <p>A cambio, asume el compromiso de representar la marca con la misma precisión con que está escrita. Es un intercambio de cobertura por profundidad, y funciona en ambas direcciones.</p>
        </div>

        <h2>Dónde encontrarla desde el 1 de septiembre</h2>

        <p>Seis puntos, repartidos por San Pedro Sula. La lista completa con direcciones está en la <a href="../producto.html#puntos">página del producto</a> y se actualiza cada vez que cambia.</p>

        <ul>
          <li>Barrio Río de Piedras</li>
          <li>Avenida Circunvalación</li>
          <li>Colonia Trejo</li>
          <li>Colonia Jardines del Valle</li>
          <li>Barrio Guamilito</li>
          <li>Colonia Universidad</li>
        </ul>

        <p>La cifra se publica a propósito. Una marca que dice «disponible en puntos seleccionados» sin decir cuántos está usando la ambigüedad como recurso. Si el número es seis, decimos seis.</p>

        <h2>Qué sigue después del lanzamiento</h2>

        <p>La expansión está pensada por fases, y cada una tiene una condición de entrada medible en lugar de una fecha:</p>

        <ol>
          <li><strong>Ampliación dentro de San Pedro Sula.</strong> Se habilita cuando los seis puntos iniciales sostengan seis meses sin quiebres de inventario.</li>
          <li><strong>Segunda plaza, Tegucigalpa.</strong> Requiere además un protocolo de capacitación que pueda replicarse sin presencia directa del equipo. Mientras la capacitación dependa de que vayamos nosotros, no hay segunda ciudad.</li>
          <li><strong>Transición a distribución selectiva.</strong> Solo cuando la marca tenga reputación propia suficiente para defenderse en un estante compartido.</li>
        </ol>

        <p>Mientras eso no ocurra, ampliar cobertura sería cambiar control por alcance en el peor momento posible: justo cuando nadie conoce todavía a la marca.</p>

        <h2>Lo que este lanzamiento no va a afirmar</h2>

        <p>Aura está en proceso de certificación de compostabilidad industrial. No tenemos aún el certificado con código de trazabilidad, así que no vas a ver un sello en el empaque ni la palabra «certificado» en ningún material de esta campaña.{sup(2)}</p>

        <p>Tampoco vamos a decir que la toalla se degrada en tu jardín: las normas EN 13432 y ASTM D6400 describen compostaje industrial, con temperaturas sostenidas de 55 a 60 °C que una compostera doméstica no alcanza.{sup(3, 4)}</p>

        <p>Y no vamos a prometer beneficios de salud. Los estudios disponibles documentan la <em>presencia</em> de ftalatos y compuestos volátiles en toallas convencionales{sup(5)}, no un daño demostrado a una persona concreta; una revisión de políticas advierte expresamente contra ese salto lógico.{sup(6)} Lo que hicimos fue quitar de la fórmula lo que no cumple ninguna función: perfume, colorante y cloro elemental.</p>

        <p>Un lanzamiento que se apoya en seis puntos de venta y en una tabla de composición pública no puede permitirse una afirmación que no resista una revisión. Ese es, al final, el mismo motivo por el que elegimos este canal.</p>
"""

REFS = [
    'Comisión Europea. <em>Green claims.</em> Datos del estudio de 2020 sobre afirmaciones ambientales: 53 % vagas, engañosas o infundadas; 40 % sin evidencia; la mitad de las etiquetas con verificación débil o inexistente. <a href="https://environment.ec.europa.eu/topics/circular-economy-topics/green-claims_en" rel="noopener">environment.ec.europa.eu</a>',
    'Ecofy. <em>ASTM D6400 Compostability Standard.</em> Sobre las Green Guides de la FTC y el uso del término «biodegradable» sin evidencia de ensayo. <a href="https://ecofy.io/resources/compliance/astm-d6400/" rel="noopener">ecofy.io</a>',
    'CEN. <em>EN 13432: Packaging — Requirements for packaging recoverable through composting and biodegradation.</em>',
    '<em>ASTM D6400: Compostable Packaging Standards Explained.</em> Sobre el requisito de 55–60 °C en compostaje industrial. <a href="https://mysupplyclub.com/blog/astm-d6400-compostability-standards-explained" rel="noopener">mysupplyclub.com</a>',
    'Gao, C.-J. y Kannan, K. <em>Phthalates, bisphenols, parabens, and triclocarban in feminine hygiene products from the United States.</em> Environment International, vol. 136, 2020. <a href="https://doaj.org/article/94d0eefaf7c34584bb4703e16f07d597" rel="noopener">doaj.org</a>',
    'Brookings Institution. <em>Period products, health risks, and regulations.</em> <a href="https://www.brookings.edu/articles/period-products-health-risks-and-regulations/" rel="noopener">brookings.edu</a>',
]

body = article(
    "LANZAMIENTO",
    "Aura llega a San Pedro Sula, y solo a seis lugares",
    "Una toalla sanitaria de fibra vegetal que sale a la venta el 1 de septiembre sin pasar por el supermercado. La decisión de canal es deliberada, y explicarla es parte del producto.",
    "Equipo Aura", "Publicado el 9 de agosto de 2026", "10 min",
    BODY, REFS,
    [REL["green"], REL["plastico"], REL["normas"]],
)

render(
    "articulos/lanzamiento-aura-san-pedro-sula.html",
    "Aura llega a San Pedro Sula, y solo a seis lugares — Aura",
    "Lanzamiento de Aura, marca hondureña de toallas sanitarias de fibra vegetal, con una estrategia de distribución exclusiva en San Pedro Sula: seis puntos de venta, precio único y exclusividad recíproca.",
    body, depth=1, active="sci", ogtype="article", progress=True,
)
