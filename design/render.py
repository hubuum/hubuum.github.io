#!/usr/bin/env python3
"""Render dependency-free landing studies. Run with Python 3.11 or newer."""

from html import escape
from pathlib import Path
import math
import string
import sys

ROOT = Path(__file__).resolve().parent
HEADLINE = "Your CMDB.<br>Your data. <em>Your model.</em>"
DESCRIPTION = (
    "Manage authoritative records alongside data from other systems. "
    "Enforce schemas where you need them, let data evolve freely where you don’t, "
    "and connect objects through meaningful relationships."
)
CONCEPTS = [
    dict(slug="confluence", number="01", name="Confluence", mood="Fluid · spacious · connected",
         idea="Structured and free-form records meet in flowing currents around a shared CMDB. An airy, understated home for the data you own and bring together.",
         caption="Different data. A shared CMDB.",
         theme="Warm white, deep teal, and softly coloured currents."),
    dict(slug="orbit", number="02", name="Orbit", mood="Luminous · precise · centred",
         idea="A luminous CMDB holds a constellation of structured and free-form records. Data from different sources shares a centre without losing its individuality.",
         caption="Your data. Other sources. One connected model.",
         theme="Midnight blue, luminous mint, and quiet orbital geometry."),
    dict(slug="fabric", number="03", name="Fabric", mood="Architectural · layered · open",
         idea="Defined grids and open records inhabit translucent connected layers. An architectural CMDB where schema-bound and schema-free data coexist.",
         caption="Structure and freedom. On a common foundation.",
         theme="Soft ivory, ink, teal, and architectural blue."),
]


def mark(x, y, size=1, color="currentColor"):
    return f'''<g transform="translate({x} {y}) scale({size})" fill="none" stroke="{color}" stroke-width="2.3" stroke-linecap="round" stroke-linejoin="round"><path d="M-14-10 0-18 14-10 14 7 0 15-14 7Z M-14-10 0-2 14-10 M0-2V15 M0-18V-27 M14 7 23 12 M-14 7-23 12"/><circle cx="0" cy="-30" r="3"/><circle cx="26" cy="14" r="3"/><circle cx="-26" cy="14" r="3"/></g>'''


def svg_start(title, viewbox):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="{viewbox}" role="img" aria-labelledby="title"><title id="title">{title}</title>'''


def data_node(x, y, structured=True, dark=False, size=1):
    """A compact record motif: a defined grid or an open, variable structure."""
    ink, paper = ("#a9d6ca", "#112d38") if dark else ("#4b7f80", "#f5f8f2")
    frame = ('<rect x="-24" y="-24" width="48" height="48" rx="5"/>' if structured else
             '<path d="M-24-9V-19Q-24-24-19-24H-9 M9-24H19Q24-24 24-19V-9 M24 9V19Q24 24 19 24H9 M-9 24H-19Q-24 24-24 19V9"/>')
    fields = ('<path d="M-14-11H14 M-14 0H14 M-14 11H14 M-5-15V15"/>' if structured else
              '<path d="M-14-11H12 M-8 0H6 M-14 11H16"/><circle cx="13" cy="0" r="1.5"/>')
    return f'<g transform="translate({x} {y}) scale({size})"><rect x="-24" y="-24" width="48" height="48" rx="8" fill="{paper}"/><g fill="none" stroke="{ink}" stroke-width="1.15">{frame}{fields}</g></g>'


def confluence():
    parts = [svg_start("Schema-bound and schema-free records flow into a common Hubuum CMDB", "0 0 1000 850"), '''<defs>
    <radialGradient id="halo"><stop stop-color="#88c9c1" stop-opacity=".38"/><stop offset="1" stop-color="#88c9c1" stop-opacity="0"/></radialGradient>
    <linearGradient id="thread" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#9fb9d4"/><stop offset=".48" stop-color="#357b80"/><stop offset="1" stop-color="#c1b093"/></linearGradient>
    <radialGradient id="pearl" cx=".3" cy=".2"><stop stop-color="white"/><stop offset="1" stop-color="#dbece8"/></radialGradient>
    <filter id="shadow" x="-100%" y="-100%" width="300%" height="300%"><feDropShadow dx="0" dy="12" stdDeviation="16" flood-color="#174f57" flood-opacity=".13"/></filter>
    </defs><circle cx="515" cy="425" r="280" fill="url(#halo)"/>''']
    for i in range(30):
        t = i / 29
        top = 25 + i * 9
        bottom = 800 - i * 8
        parts.append(f'<path d="M{80+i*4} -20 C{940-i*5} {top}, {10+i*8} {bottom}, {830+i*6} 880" fill="none" stroke="url(#thread)" stroke-width="{0.7+t*.6:.2f}" opacity="{.14+t*.42:.2f}"/>')
    for i in range(15):
        parts.append(f'<path d="M-20 {180+i*15} C320 {180+i*12}, 340 {690-i*12}, 1020 {570+i*8}" fill="none" stroke="#508c87" stroke-width=".85" opacity="{.13+i*.015:.3f}"/>')
    for index, (x, y) in enumerate([(283, 152), (766, 650), (189, 343), (808, 552), (692, 165), (364, 675)]):
        parts.append(data_node(x, y, structured=index % 2 == 0, size=.85))
    parts.extend(['<circle cx="515" cy="425" r="90" fill="none" stroke="#79a8a1" stroke-opacity=".25"/><circle cx="515" cy="425" r="66" fill="url(#pearl)" stroke="white" stroke-width="2" filter="url(#shadow)"/>', mark(515, 432, 1.25, "#174f57"), '<text x="515" y="534" text-anchor="middle" font-family="system-ui,sans-serif" font-size="12" letter-spacing="4" fill="#426866">HUBUUM</text>', '</svg>'])
    return "\n".join(parts)


def orbit():
    parts = [svg_start("An illuminated Hubuum CMDB connects structured and free-form records from different sources", "0 0 1400 760"), '''<defs>
    <radialGradient id="halo"><stop stop-color="#6dcbbc" stop-opacity=".34"/><stop offset=".42" stop-color="#39898c" stop-opacity=".12"/><stop offset="1" stop-color="#164954" stop-opacity="0"/></radialGradient>
    <radialGradient id="pearl" cx=".35" cy=".2"><stop stop-color="#fffef0"/><stop offset=".65" stop-color="#c2f3de"/><stop offset="1" stop-color="#77beaf"/></radialGradient>
    <linearGradient id="arc"><stop stop-color="#629fba" stop-opacity=".08"/><stop offset=".5" stop-color="#a8d7cb" stop-opacity=".7"/><stop offset="1" stop-color="#73b7b2" stop-opacity=".08"/></linearGradient>
    </defs><ellipse cx="700" cy="377" rx="520" ry="365" fill="url(#halo)"/>''']
    for rotation in [-27, -14, 0, 14, 27]:
        for i in range(3):
            parts.append(f'<ellipse cx="700" cy="380" rx="{460+i*18}" ry="{153+i*14}" transform="rotate({rotation} 700 380)" fill="none" stroke="url(#arc)" stroke-width=".8"/>')
    for index, (x, y, label) in enumerate([(247, 380, "CONFIGURATION"), (447, 170, "SERVICES"), (958, 191, "YOUR OWN DATA"), (1128, 421, "RESOURCES"), (551, 573, "CONTEXT")]):
        parts.append(f'<path d="M700 380 Q{(700+x)/2} {y} {x} {y}" fill="none" stroke="#79b0b0" stroke-width="1" opacity=".4"/>' + data_node(x, y, structured=index % 2 == 1, dark=True) + f'<text x="{x}" y="{y+46}" text-anchor="middle" font-size="11" letter-spacing="2.3" fill="#a0b9bd" font-family="system-ui,sans-serif">{label}</text>')
    for i in range(42):
        angle = i * 2.39996
        radius = 160 + (i * 31) % 400
        x, y = 700 + math.cos(angle) * radius, 380 + math.sin(angle) * radius * .66
        parts.append(f'<circle cx="{x:.2f}" cy="{y:.2f}" r="1.4" fill="#abcbce" opacity=".5"/>')
    parts.extend(['<circle cx="700" cy="380" r="101" fill="none" stroke="#b4ded4" stroke-opacity=".13"/><circle cx="700" cy="380" r="80" fill="none" stroke="#b4ded4" stroke-opacity=".25"/><circle cx="700" cy="380" r="59" fill="url(#pearl)"/>', mark(700, 387, 1.05, "#174f57"), '<text x="700" y="506" text-anchor="middle" font-family="system-ui,sans-serif" font-size="11" letter-spacing="4" fill="#a6d3ca">HUBUUM</text>', '</svg>'])
    return "\n".join(parts)


def fabric():
    parts = [svg_start("Defined and open records coexist in the connected layers of a Hubuum CMDB", "0 0 1000 900"), '''<defs>
    <linearGradient id="plane" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#b1cac9" stop-opacity=".07"/><stop offset=".55" stop-color="#aacbdb" stop-opacity=".25"/><stop offset="1" stop-color="#e0cba8" stop-opacity=".25"/></linearGradient>
    <linearGradient id="tile" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#fffdf7"/><stop offset="1" stop-color="#d9e5e6"/></linearGradient>
    </defs>''']
    for layer in range(3):
        offset = 110 * layer
        parts.append(f'<g transform="translate(0 {offset})"><path d="M500 135 925 340 500 545 75 340Z" fill="url(#plane)" stroke="#6d969e" stroke-opacity=".28"/>')
        for i in range(1, 11):
            t = i / 11
            parts.append(f'<path d="M{500-425*t:.2f} {135+205*t:.2f} {925-425*t:.2f} {340+205*t:.2f} M{500+425*t:.2f} {135+205*t:.2f} {75+425*t:.2f} {340+205*t:.2f}" stroke="#5d909d" stroke-width=".7" opacity=".16" fill="none"/>')
        parts.append('</g>')
    for index, (x, y, end) in enumerate([(265, 337, 557), (736, 340, 562), (502, 170, 390), (498, 510, 730)]):
        parts.append(f'<path d="M{x} {y}V{end}" stroke="#4b7a8a" stroke-dasharray="3 6" opacity=".45"/>' + data_node(x, y, structured=index % 2 == 0, size=.7) + f'<circle cx="{x}" cy="{end}" r="3" fill="#47798b"/>')
    parts.extend(['<path d="M500 340 610 393 500 446 390 393Z" fill="#286473" opacity=".13"/><path d="M500 305 610 358 500 411 390 358Z" fill="url(#tile)" stroke="white" stroke-width="1.5"/><path d="M390 358V375L500 428 610 375V358L500 411Z" fill="#b9d0d2" opacity=".7"/>', mark(500, 364, .9, "#174f57"), '<path d="M500 195V293 M500 435V631 M260 355 379 355 M623 355 742 355" fill="none" stroke="#386988" stroke-width="1.5"/><text x="650" y="445" font-family="system-ui,sans-serif" font-size="11" letter-spacing="3" fill="#345969">HUBUUM</text>', '</svg>'])
    return "\n".join(parts)


def story_art():
    return svg_start("Example CMDB: schema-bound Atlas and web-01 connect to schema-free research notes and Oslo; authority lives in Hubuum or upstream independently of schema choice", "0 0 800 580") + '''
    <defs><radialGradient id="wash"><stop stop-color="#61988f" stop-opacity=".2"/><stop offset="1" stop-color="#61988f" stop-opacity="0"/></radialGradient></defs>
    <circle cx="400" cy="280" r="270" fill="url(#wash)"/>
    <g fill="none" stroke="#75a59d" stroke-width="1.2"><path d="M350 172H450 M235 250C235 300 210 300 210 350 M570 250C570 300 595 300 595 350"/></g>
    <g font-family="system-ui,sans-serif" text-anchor="middle">
    <g fill="#bdd4ce" font-size="13"><text x="400" y="154">runs on</text><text x="642" y="307">located in</text><text x="154" y="307">described by</text></g>
    <g fill="#102f36" stroke="#779c95"><rect x="105" y="90" width="245" height="160" rx="5"/><rect x="450" y="90" width="245" height="160" rx="5"/></g>
    <g fill="#102f36" stroke="#779c95" stroke-dasharray="5 6"><rect x="85" y="350" width="250" height="160" rx="16"/><rect x="460" y="350" width="250" height="160" rx="16"/></g>
    <g fill="#b6cfc9" font-size="11" letter-spacing="2"><text x="228" y="121">SERVICE</text><text x="573" y="121">SERVER</text><text x="210" y="382">CONTEXT</text><text x="585" y="382">LOCATION</text></g>
    <g fill="#f1f5ee" font-size="27"><text x="228" y="165">Atlas</text><text x="573" y="165">web-01</text><text x="210" y="425" font-size="23">Research notes</text><text x="585" y="425">Oslo</text></g>
    <g fill="#c2d9cd" font-size="13"><text x="228" y="204">Schema-bound</text><text x="573" y="204">Schema-bound</text><text x="210" y="465">Schema-free</text><text x="585" y="465">Schema-free</text></g>
    <g fill="#9fbab4" font-size="11"><text x="228" y="229">Authority: Hubuum</text><text x="573" y="229">Authority: upstream</text><text x="210" y="490">Authority: Hubuum</text><text x="585" y="490">Authority: upstream</text></g></g>
    </svg>'''


def render():
    if sys.version_info < (3, 11):
        raise SystemExit("Use Python 3.11 or newer.")
    assets = ROOT / "assets"
    for slug, renderer in [("confluence", confluence), ("orbit", orbit), ("fabric", fabric), ("relationships", story_art)]:
        (assets / f"{slug}.svg").write_text(renderer() + "\n")
    template = string.Template((ROOT / "page.html.template").read_text())
    symbol = f'<svg class="brand-mark" viewBox="-32 -35 64 60" aria-hidden="true">{mark(0, 0)}</svg>'
    for concept in CONCEPTS:
        switcher = "".join(
            '<a href="' + c["slug"] + '.html"'
            + (' aria-current="page"' if c == concept else '')
            + f'>{c["number"]}<span> {c["name"]}</span></a>'
            for c in CONCEPTS
        )
        content = template.substitute(**concept, headline=HEADLINE, description=DESCRIPTION,
                                      symbol=symbol, switcher=switcher)
        (ROOT / f'{concept["slug"]}.html').write_text(content)
    cards = "\n".join(f'''<a class="concept-card {c['slug']}" href="{c['slug']}.html"><div class="concept-art"><img src="assets/{c['slug']}.svg" alt="{escape(c['idea'])}"></div><div class="concept-copy"><span class="eyebrow">{c['number']} / {c['mood']}</span><h2>{c['name']} <span aria-hidden="true">↗</span></h2><p>{c['idea']}</p><span class="text-link">Explore this direction <span aria-hidden="true">→</span></span></div></a>''' for c in CONCEPTS)
    gallery = string.Template((ROOT / "gallery.html.template").read_text()).substitute(cards=cards, symbol=symbol)
    (ROOT / "index.html").write_text(gallery)


if __name__ == "__main__":
    render()
