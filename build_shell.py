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
<link href="https://fonts.googleapis.com/css2?family=Petrona:ital,wght@0,400;0,500;0,600;1,400&family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,500;1,6..72,400&family=Instrument+Sans:wght@400;500;600&family=DM+Mono:wght@400;500&display=swap" rel="stylesheet">
<script>document.documentElement.className+=" js";</script>
<link rel="stylesheet" href="{p}assets/css/aura.css">
{head_extra}</head>
<body>

<a class="skip" href="#main">Saltar al contenido</a>
{progress}
<header class="masthead">
  <div class="wrap masthead__inner">
    <a class="brand" href="{p}index.html" aria-label="Aura, inicio">
      <img class="brand__mark" src="{p}assets/img/logo-marca.svg" alt="" width="38" height="24">
      <span class="brand__word">Aura</span>
    </a>

    <button class="nav-toggle" aria-expanded="false" aria-controls="nav" aria-label="Abrir menú"><span></span></button>

    <nav class="nav" id="nav">
      <a href="{p}index.html"{c_home}>Inicio</a>
      <a href="{p}blog.html"{c_sci}>Blog</a>
      <a href="{p}producto.html"{c_prod}>Producto</a>
      <a href="{p}marca.html"{c_mark}>Marca</a>
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
          <img class="brand__mark" src="{p}assets/img/logo-marca-claro.svg" alt="" width="38" height="24">
          <span class="brand__word">Aura</span>
        </a>
        <p class="foot__blurb">Toallas sanitarias ecológicas reutilizables, cosidas en San Pedro Sula. Con la composición y la vida útil publicadas.</p>
      </div>

      <div>
        <h4>Blog</h4>
        <ul>
          <li><a href="{p}articulos/lanzamiento-aura-san-pedro-sula.html">Lanzamiento</a></li>
          <li><a href="{p}articulos/reutilizable-o-desechable.html">Reutilizable o desechable</a></li>
          <li><a href="{p}articulos/cuanto-dura-cuanto-ahorra.html">Vida útil y ahorro</a></li>
          <li><a href="{p}articulos/como-lavar-toallas-de-tela.html">Cómo lavarlas</a></li>
          <li><a href="{p}articulos/greenwashing-marketing-verde.html">Greenwashing</a></li>
          <li><a href="{p}articulos/pobreza-menstrual-america-latina.html">Pobreza menstrual</a></li>
        </ul>
      </div>

      <div>
        <h4>La marca</h4>
        <ul>
          <li><a href="{p}producto.html">El producto</a></li>
          <li><a href="{p}index.html#composicion">Composición</a></li>
          <li><a href="{p}producto.html#puntos">Dónde encontrarlas</a></li>
          <li><a href="{p}marca.html">Estrategia de marca</a></li>
          <li><a href="{p}blog.html#metodo">Método editorial</a></li>
        </ul>
      </div>

      <div>
        <h4>Contacto</h4>
        <ul>
          <li><a href="mailto:hola@aura.hn">hola@aura.hn</a></li>
          <li><a href="{p}blog.html">Todos los artículos</a></li>
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
        c_mark=CUR if active == "mark" else "",
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

  <section class="band band--linen" style="padding-bottom:0">
    <div class="wrap" style="margin-bottom:var(--s6)">
      <p class="eyebrow">Seguir leyendo</p>
    </div>
    <div class="post-grid">
{rel}
    </div>
  </section>

  <section class="band band--forest band--tight">
    <div class="wrap" style="display:flex;flex-wrap:wrap;gap:var(--s6);align-items:center;justify-content:space-between">
      <div style="max-width:40ch">
        <h2 class="display-m" style="margin-bottom:var(--s3)">Cómo escribimos esto.</h2>
        <p class="lede" style="margin:0">Las cinco reglas editoriales que seguimos, incluida la de publicar los datos que nos contradicen.</p>
      </div>
      <a class="btn btn--solid" href="../blog.html#metodo">Ver el método</a>
    </div>
  </section>
"""


def sup(*nums):
    inner = ", ".join(f'<a href="#r{n}">{n}</a>' for n in nums)
    return f'<sup class="ref">[{inner}]</sup>'


