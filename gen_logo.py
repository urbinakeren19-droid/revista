#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Marca gráfica de Aura: sol naciente con rayos."""

import math

GOLD = "#C4913C"
FOREST = "#2C4636"


def rays(cx, cy, r_in, r_out, n=9, spread=180, width=2.6, color=GOLD):
    """Rayos radiales sobre un semicírculo."""
    out = []
    for i in range(n):
        a = math.radians(180 + spread * (i + .5) / n)
        x1, y1 = cx + r_in * math.cos(a), cy + r_in * math.sin(a)
        x2, y2 = cx + r_out * math.cos(a), cy + r_out * math.sin(a)
        out.append(
            f'<line x1="{x1:.2f}" y1="{y1:.2f}" x2="{x2:.2f}" y2="{y2:.2f}" '
            f'stroke="{color}" stroke-width="{width}" stroke-linecap="round"/>'
        )
    return "\n  ".join(out)


# --- Marca suelta, para usar en línea junto al texto -----------------------
MARK = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 72 44" role="img" aria-label="Aura">
  <path d="M18 38 a18 18 0 0 1 36 0" fill="none" stroke="{GOLD}" stroke-width="3" stroke-linecap="round"/>
  {rays(36, 38, 23, 33, n=9, spread=180, width=2.8)}
</svg>'''

# --- Favicon ---------------------------------------------------------------
FAVICON = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
  <rect width="64" height="64" rx="13" fill="#F5F1E8"/>
  <path d="M17 44 a15 15 0 0 1 30 0" fill="none" stroke="{FOREST}" stroke-width="3.4" stroke-linecap="round"/>
  {rays(32, 44, 19.5, 27, n=7, spread=180, width=3, color=GOLD)}
</svg>'''

# --- Marca sobre fondo oscuro ---------------------------------------------
MARK_LIGHT = MARK.replace(f'stroke="{GOLD}"', 'stroke="#E3B463"')

for name, svg in [("logo-marca.svg", MARK),
                  ("favicon.svg", FAVICON),
                  ("logo-marca-claro.svg", MARK_LIGHT)]:
    path = f"/home/claude/aura/assets/img/{name}"
    with open(path, "w", encoding="utf-8") as f:
        f.write(svg)
    print("escrito:", name)
