#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Artículo 5: greenwashing y comunicación ambiental."""

from build_pages import render, article, sup, REL

A5_BODY = f"""
        <p>En 2020 la Comisión Europea revisó una muestra de afirmaciones ambientales usadas para vender productos y servicios en la Unión Europea. El resultado es incómodo para cualquiera que trabaje en mercadeo: <strong>el 53 % de esas afirmaciones daba información vaga, engañosa o infundada</strong>, y el 40 % no tenía ninguna evidencia que la respaldara.{sup(1, 2)}</p>

        <p>El mismo diagnóstico agrega dos datos que explican por qué el problema se sostiene. La mitad de las etiquetas verdes ofrece una verificación débil o directamente inexistente, y en el mercado europeo circulan unas 230 etiquetas de sostenibilidad con niveles de transparencia muy dispares.{sup(1)}</p>

        <p class="pull">Cuando la mitad de los sellos no verifica nada, un sello deja de ser información y pasa a ser decoración.</p>

        <h2>Por qué esto es un problema de mercadeo, no de sostenibilidad</h2>

        <p>La consecuencia obvia es que el consumidor no puede elegir bien. La consecuencia menos obvia, y más relevante para quien construye una marca, es que el greenwashing <strong>castiga a las empresas que sí invirtieron</strong>. Si una marca cambió su formulación, pagó ensayos de laboratorio y absorbió un costo mayor por kilo de material, compite en el mismo estante contra otra que solo imprimió una hoja verde en el empaque. A igualdad de mensaje percibido, gana la que gastó menos.</p>

        <p>Ese es el razonamiento que la Comisión Europea usó al proponer en marzo de 2023 la Directiva de Afirmaciones Verdes: emparejar la cancha exigiendo que toda afirmación ambiental se sustente con datos verificables y perspectiva de ciclo de vida completo.{sup(2, 3)}</p>

        <div class="callout">
          <span class="callout__label">Actualización regulatoria</span>
          <p>La Directiva de Afirmaciones Verdes quedó en pausa: la Comisión anunció en junio de 2025 su intención de retirar la propuesta, tras señalamientos de que imponía requisitos desproporcionados a las microempresas.{sup(4)}</p>
          <p>Eso no significa vía libre. La Directiva sobre empoderamiento de los consumidores para la transición ecológica, Directiva (UE) 2024/825, ya está en vigor y prohíbe las afirmaciones ambientales vagas o no verificadas del tipo «eco» o «verde» sin evidencia rigurosa.{sup(4)}</p>
        </div>

        <h2>Los tribunales ya se movieron</h2>

        <p>Mientras la norma específica se discutía, la jurisprudencia avanzó. En una sentencia del 27 de junio de 2024, el Tribunal Federal de Justicia alemán estableció que a las afirmaciones ambientales deben aplicarse estándares tan estrictos como los que rigen la publicidad de salud, argumentando la relevancia emocional que el medioambiente tiene para el público destinatario.{sup(5)}</p>

        <p>Tras esa sentencia, las asociaciones alemanas contra la competencia desleal ganaron una sucesión de casos de greenwashing con un argumento simple: la afirmación era vaga, no estaba sustanciada y por lo tanto inducía a error. En Francia se declaró engañosa una afirmación sobre «contribuir a la preservación» del mundo, por ser demasiado vaga frente al impacto real de la empresa.{sup(5)}</p>

        <h2>Las cuatro trampas más comunes en esta categoría</h2>

        <p>Aplicado a productos menstruales, el patrón se repite con formas reconocibles:</p>

        <h3>1. El adjetivo sin norma</h3>
        <p>«Biodegradable» sin plazo, sin condición y sin norma de referencia. Prácticamente todo es biodegradable con tiempo suficiente. Las guías de publicidad ambiental de la Comisión Federal de Comercio de Estados Unidos consideran engañoso el término sin evidencia de ensayo específica.{sup(6)}</p>

        <h3>2. El atributo parcial presentado como total</h3>
        <p>Empaque exterior compostable, producto de plástico convencional. La afirmación es literalmente cierta y comunicativamente falsa, porque el consumidor la atribuye a lo que se lleva puesto.</p>

        <h3>3. El sello propio</h3>
        <p>Un logo verde diseñado internamente, sin organismo certificador detrás. Con 230 etiquetas circulando, distinguir a simple vista cuál tiene auditoría independiente y cuál es un gráfico es prácticamente imposible.{sup(1)}</p>

        <h3>4. La palabra «natural»</h3>
        <p>No tiene definición regulatoria en esta categoría. Y hay evidencia directa de que no predice mejor desempeño: un análisis de compuestos orgánicos volátiles en productos de higiene femenina del mercado estadounidense encontró que los productos etiquetados como orgánicos, naturales o para piel sensible <strong>no presentaban necesariamente concentraciones menores</strong>.{sup(7)}</p>

        <h2>Qué queda cuando se quitan las palabras vacías</h2>

        <p>Si «eco», «natural», «verde» y «biodegradable» no comunican nada verificable, la pregunta interesante es qué sí lo hace. Tres cosas:</p>

        <ol>
          <li><strong>La lista de materiales con proporciones.</strong> Es un dato, no una promesa. Se puede contrastar contra la ficha técnica del proveedor.</li>
          <li><strong>La norma citada por su nombre.</strong> EN 13432 o ASTM D6400 tienen umbrales numéricos: 90 % de conversión del carbono orgánico en 180 días bajo compostaje industrial. Una marca que cita la norma se expone a que la midan.</li>
          <li><strong>El código de certificado verificable.</strong> Consultable en el registro público del organismo emisor, no en la palabra de la marca.</li>
        </ol>

        <p>Ninguna de las tres es tan atractiva como una hoja verde impresa. Todas son auditables, que es exactamente el punto.</p>

        <h2>Cómo se aplica esto a Aura</h2>

        <p>Aura está en proceso de certificación de compostabilidad industrial. Todavía no existe el certificado con código de trazabilidad, y por eso en este sitio no vas a encontrar un sello ni la palabra «certificado». Sería el caso de manual de la trampa número tres.</p>

        <p>Lo que sí publicamos es la <a href="../index.html#composicion">lista completa de materiales con porcentajes por capa</a>, que es el tipo de dato que un tercero puede contrastar. No es una posición moral: es la única afirmación que podemos sostener hoy sin quedar del lado de ese 53 %.</p>

        <div class="callout">
          <span class="callout__label">Para quien estudia mercadeo</span>
          <p>La lectura estratégica de estos datos es que la transparencia radical dejó de ser un gesto ético y pasó a ser una <strong>posición competitiva defendible</strong>. En una categoría donde la mitad de las etiquetas no verifica nada, publicar información contrastable es una de las pocas señales que la competencia no puede imitar sin incurrir en el mismo costo.</p>
          <p>Dicho de otro modo: cuando todos dicen lo mismo, el diferencial no está en decirlo mejor, sino en decir algo que se pueda comprobar.</p>
        </div>
"""

A5_REFS = [
    'Comisión Europea. <em>Green claims.</em> Datos del estudio de 2020: 53 % de afirmaciones vagas, engañosas o infundadas; 40 % sin evidencia; 230 etiquetas de sostenibilidad en circulación. <a href="https://environment.ec.europa.eu/topics/circular-economy-topics/green-claims_en" rel="noopener">environment.ec.europa.eu</a>',
    'Comisión Europea. <em>Consumer protection: enabling sustainable choices and ending greenwashing.</em> Comunicado de prensa, marzo de 2023. <a href="https://ec.europa.eu/commission/presscorner/detail/en/ip_23_1692" rel="noopener">ec.europa.eu</a>',
    'One Click LCA. <em>Green Claims Directive explained.</em> Sobre el requisito de sustanciación con perspectiva de ciclo de vida. <a href="https://oneclicklca.com/en-gb/resources/articles/green-claims-directive-explained-eu-uk-carbon-claims-one-click-lca" rel="noopener">oneclicklca.com</a>',
    'ASUENE. <em>The Withdrawal of the Green Claims Directive: What It Means for Environmental Marketing in the EU.</em> Sobre la retirada de la propuesta y la vigencia de la Directiva (UE) 2024/825. <a href="https://asuene.com/us/blog/the-withdrawal-of-the-green-claims-directive-what-it-means-for-environmental-marketing-in-the-eu" rel="noopener">asuene.com</a>',
    'Sidley Austin LLP. <em>Heightened Scrutiny of Green Claims in the European Union and Switzerland.</em> Sobre la sentencia del BGH alemán del 27 de junio de 2024 y los casos en Francia. <a href="https://www.sidley.com/en/insights/publications/2025/03/heightened-scrutiny-of-green-claims-in-the-european-union-and-switzerland" rel="noopener">sidley.com</a>',
    'Ecofy. <em>ASTM D6400 Compostability Standard.</em> Incluye la referencia a las Green Guides de la FTC sobre el término «biodegradable». <a href="https://ecofy.io/resources/compliance/astm-d6400/" rel="noopener">ecofy.io</a>',
    '<em>Volatile organic compounds in feminine hygiene products sold in the US market: A survey of products and health risks.</em> Environment International, 2020. <a href="https://www.sciencedirect.com/science/article/pii/S0160412020303494" rel="noopener">sciencedirect.com</a>',
    'CEN. <em>EN 13432: Packaging — Requirements for packaging recoverable through composting and biodegradation.</em>',
]

body = article(
    "MERCADEO",
    "Greenwashing: el 53 % de las promesas verdes no resiste una revisión",
    "La Comisión Europea auditó las afirmaciones ambientales del mercado y encontró que más de la mitad eran vagas o infundadas. Qué significa eso para una marca que sí invirtió en cambiar su producto.",
    "Equipo Aura", "Actualizado en agosto de 2026", "9 min",
    A5_BODY, A5_REFS,
    [REL["plastico"], REL["normas"], REL["quimicos"]],
)

render(
    "articulos/greenwashing-marketing-verde.html",
    "Greenwashing: el 53 % de las promesas verdes no resiste una revisión — Aura",
    "Datos de la Comisión Europea sobre afirmaciones ambientales engañosas, el estado de la Directiva de Afirmaciones Verdes y las cuatro trampas más comunes en el mercadeo de productos menstruales.",
    body, depth=1, active="sci", ogtype="article", progress=True,
)
