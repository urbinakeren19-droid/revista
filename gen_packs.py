#!/usr/bin/env python3
"""Genera las ilustraciones de empaque de Aura en SVG."""

import os

OUT = "/home/claude/aura/assets/img"
os.makedirs(OUT, exist_ok=True)

VOID = "#1B0E13"
GARNET = "#8C1D33"
HALO = "#E5A83B"
PULP = "#E6E8DD"
MOSS = "#4A5A46"

VARIANTS = [
    {
        "file": "pack-dia.svg",
        "name": "DÍA",
        "sub": "FLUJO MEDIO",
        "count": "10",
        "body": GARNET,
        "body_dark": "#6E1728",
        "accent": HALO,
        "wing": True,
    },
    {
        "file": "pack-noche.svg",
        "name": "NOCHE",
        "sub": "FLUJO ALTO",
        "count": "8",
        "body": "#3E2038",
        "body_dark": "#281426",
        "accent": HALO,
        "wing": True,
    },
    {
        "file": "pack-diario.svg",
        "name": "DIARIO",
        "sub": "PROTECTOR",
        "count": "20",
        "body": MOSS,
        "body_dark": "#37422F",
        "accent": PULP,
        "wing": False,
    },
]

TEMPLATE = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 400" role="img" aria-label="Empaque Aura {name}">
  <defs>
    <linearGradient id="g{i}" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="{dark}"/>
      <stop offset=".18" stop-color="{body}"/>
      <stop offset=".62" stop-color="{body}"/>
      <stop offset="1" stop-color="{dark}"/>
    </linearGradient>
    <linearGradient id="s{i}" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#ffffff" stop-opacity=".16"/>
      <stop offset=".5" stop-color="#ffffff" stop-opacity="0"/>
    </linearGradient>
    <radialGradient id="h{i}" cx=".5" cy=".5" r=".5">
      <stop offset="0" stop-color="{accent}" stop-opacity=".30"/>
      <stop offset="1" stop-color="{accent}" stop-opacity="0"/>
    </radialGradient>
  </defs>

  <!-- resplandor -->
  <ellipse cx="160" cy="200" rx="150" ry="170" fill="url(#h{i})"/>

  <!-- sombra de apoyo -->
  <ellipse cx="160" cy="372" rx="96" ry="12" fill="#000" opacity=".35"/>

  <!-- cuerpo de la bolsa -->
  <path d="M62 54 h196 a6 6 0 0 1 6 6 v300 a6 6 0 0 1 -6 6 h-196 a6 6 0 0 1 -6 -6 v-300 a6 6 0 0 1 6 -6 z"
        fill="url(#g{i})"/>

  <!-- sellado superior dentado -->
  <path d="M56 54 h208 v-16 h-208 z" fill="{dark}"/>
  <path d="M56 38 l10 8 l10 -8 l10 8 l10 -8 l10 8 l10 -8 l10 8 l10 -8 l10 8 l10 -8 l10 8 l10 -8
           l10 8 l10 -8 l10 8 l10 -8 l10 8 l10 -8 l10 8 l10 -8 v-6 h-208 z" fill="{dark}"/>

  <!-- sellado inferior -->
  <path d="M56 348 h208 v18 h-208 z" fill="{dark}" opacity=".8"/>

  <!-- brillo -->
  <path d="M62 54 h196 v300 h-196 z" fill="url(#s{i})"/>

  <!-- marca de agua: arco del aura -->
  <path d="M160 118 m-52 0 a52 52 0 1 1 104 0" fill="none" stroke="{accent}" stroke-width="2.5" opacity=".9"/>
  <circle cx="160" cy="118" r="7" fill="{accent}"/>

  <!-- logotipo -->
  <text x="160" y="176" text-anchor="middle" fill="{accent}"
        font-family="Georgia, 'Times New Roman', serif" font-size="42" letter-spacing="6">aura</text>

  <!-- filete -->
  <rect x="104" y="192" width="112" height="1.5" fill="{accent}" opacity=".5"/>

  <!-- variante -->
  <text x="160" y="224" text-anchor="middle" fill="{ink}"
        font-family="Helvetica, Arial, sans-serif" font-size="19" font-weight="700" letter-spacing="5">{name}</text>
  <text x="160" y="246" text-anchor="middle" fill="{ink}" opacity=".65"
        font-family="Helvetica, Arial, sans-serif" font-size="9.5" letter-spacing="3.4">{sub}</text>

  <!-- ventana de composición -->
  <rect x="86" y="266" width="148" height="54" rx="2" fill="#000" opacity=".18"/>
  <text x="98" y="284" fill="{ink}" opacity=".8"
        font-family="Courier New, monospace" font-size="8.5">BAMBU · CELULOSA FSC</text>
  <text x="98" y="298" fill="{ink}" opacity=".8"
        font-family="Courier New, monospace" font-size="8.5">BASE DE ALMIDON DE MAIZ</text>
  <text x="98" y="312" fill="{accent}"
        font-family="Courier New, monospace" font-size="8.5">SIN CLORO · SIN PERFUME</text>

  <!-- conteo -->
  <circle cx="252" cy="86" r="21" fill="{accent}"/>
  <text x="252" y="92" text-anchor="middle" fill="{dark}"
        font-family="Helvetica, Arial, sans-serif" font-size="18" font-weight="700">{count}</text>
  <text x="252" y="120" text-anchor="middle" fill="{ink}" opacity=".7"
        font-family="Helvetica, Arial, sans-serif" font-size="7" letter-spacing="1.5">UNIDADES</text>

  {wings}
</svg>
"""

WINGS = """<!-- marca de alas -->
  <g opacity=".55">
    <path d="M92 330 h18 M92 336 h12" stroke="{ink}" stroke-width="1.4" stroke-linecap="round"/>
  </g>"""


def build():
    for i, v in enumerate(VARIANTS):
        ink = PULP if v["name"] != "DIARIO" else "#F1F2EB"
        svg = TEMPLATE.format(
            i=i,
            name=v["name"],
            sub=v["sub"],
            count=v["count"],
            body=v["body"],
            dark=v["body_dark"],
            accent=v["accent"],
            ink=ink,
            wings=WINGS.format(ink=ink) if v["wing"] else "",
        )
        path = os.path.join(OUT, v["file"])
        with open(path, "w", encoding="utf-8") as f:
            f.write(svg)
        print("escrito:", path, len(svg), "bytes")


if __name__ == "__main__":
    build()
