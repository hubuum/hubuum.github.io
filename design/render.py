#!/usr/bin/env python3
"""Render dependency-free landing studies. Run with Python 3.11 or newer."""

from html import escape
from pathlib import Path
import math
import string
import sys

ROOT = Path(__file__).resolve().parent
CONCEPTS = [
    dict(slug="confluence", number="01", name="Confluence", mood="Fluid · spacious · connected",
         headline="Every connection.<br><em>A clearer picture.</em>",
         description="Bring your operational data into a shared model. Connect the resources, people, and systems that make your world work.",
         idea="Fine currents gather around a shared centre, then travel outward together. An airy, understated expression of Hubuum as the meeting point for your data.",
         caption="Many sources. One shared model.",
         theme="Warm white, deep teal, and softly coloured currents."),
    dict(slug="orbit", number="02", name="Orbit", mood="Luminous · precise · centred",
         headline="Put your world<br><em>in relation.</em>",
         description="Your resources are part of a bigger picture. Hubuum gives their data a common home, and their connections a language.",
         idea="A luminous centre holds a constellation of independent systems. A spacious, darker direction that makes the hub the unmistakable focus.",
         caption="Independent systems. Connected context.",
         theme="Midnight blue, luminous mint, and quiet orbital geometry."),
    dict(slug="fabric", number="03", name="Fabric", mood="Architectural · layered · open",
         headline="A shared foundation.<br><em>For a connected world.</em>",
         description="Build an inventory around the way your organisation works. Give different data a shared structure, and connect it on your terms.",
         idea="Translucent planes and crossing paths form a connected foundation. An architectural direction with a more editorial voice and a strong sense of structure.",
         caption="Your resources. Your relationships. Your model.",
         theme="Soft ivory, ink, teal, and architectural blue."),
]


def mark(x, y, size=1, color="currentColor"):
    return f'''<g transform="translate({x} {y}) scale({size})" fill="none" stroke="{color}" stroke-width="2.3" stroke-linecap="round" stroke-linejoin="round"><path d="M-14-10 0-18 14-10 14 7 0 15-14 7Z M-14-10 0-2 14-10 M0-2V15 M0-18V-27 M14 7 23 12 M-14 7-23 12"/><circle cx="0" cy="-30" r="3"/><circle cx="26" cy="14" r="3"/><circle cx="-26" cy="14" r="3"/></g>'''


def svg_start(title, viewbox):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="{viewbox}" role="img" aria-labelledby="title"><title id="title">{title}</title>'''


def confluence():
    parts = [svg_start("Abstract currents from independent sources meet at the Hubuum centre", "0 0 1000 850"), '''<defs>
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
    for x, y in [(283, 152), (766, 650), (189, 343), (808, 552), (692, 165), (364, 675)]:
        parts.append(f'<circle cx="{x}" cy="{y}" r="9" fill="#f5f8f4" stroke="#95b2af"/><circle cx="{x}" cy="{y}" r="3" fill="#3b7475"/>')
    parts.extend(['<circle cx="515" cy="425" r="90" fill="none" stroke="#79a8a1" stroke-opacity=".25"/><circle cx="515" cy="425" r="66" fill="url(#pearl)" stroke="white" stroke-width="2" filter="url(#shadow)"/>', mark(515, 432, 1.25, "#174f57"), '<text x="515" y="534" text-anchor="middle" font-family="system-ui,sans-serif" font-size="12" letter-spacing="4" fill="#426866">HUBUUM</text>', '</svg>'])
    return "\n".join(parts)


def orbit():
    parts = [svg_start("An illuminated Hubuum centre connects a constellation of independent systems", "0 0 1400 760"), '''<defs>
    <radialGradient id="halo"><stop stop-color="#6dcbbc" stop-opacity=".34"/><stop offset=".42" stop-color="#39898c" stop-opacity=".12"/><stop offset="1" stop-color="#164954" stop-opacity="0"/></radialGradient>
    <radialGradient id="pearl" cx=".35" cy=".2"><stop stop-color="#fffef0"/><stop offset=".65" stop-color="#c2f3de"/><stop offset="1" stop-color="#77beaf"/></radialGradient>
    <linearGradient id="arc"><stop stop-color="#629fba" stop-opacity=".08"/><stop offset=".5" stop-color="#a8d7cb" stop-opacity=".7"/><stop offset="1" stop-color="#73b7b2" stop-opacity=".08"/></linearGradient>
    </defs><ellipse cx="700" cy="377" rx="520" ry="365" fill="url(#halo)"/>''']
    for rotation in [-27, -14, 0, 14, 27]:
        for i in range(3):
            parts.append(f'<ellipse cx="700" cy="380" rx="{460+i*18}" ry="{153+i*14}" transform="rotate({rotation} 700 380)" fill="none" stroke="url(#arc)" stroke-width=".8"/>')
    for x, y, label in [(247, 380, "RESOURCES"), (447, 170, "APPLICATIONS"), (958, 191, "PEOPLE"), (1128, 421, "SYSTEMS"), (551, 573, "LOCATIONS")]:
        parts.append(f'<path d="M700 380 Q{(700+x)/2} {y} {x} {y}" fill="none" stroke="#79b0b0" stroke-width="1" opacity=".4"/><circle cx="{x}" cy="{y}" r="17" fill="#102e38" stroke="#648c8d"/><circle cx="{x}" cy="{y}" r="4" fill="#c7e9d6"/><text x="{x}" y="{y+42}" text-anchor="middle" font-size="11" letter-spacing="2.3" fill="#a0b9bd" font-family="system-ui,sans-serif">{label}</text>')
    for i in range(42):
        angle = i * 2.39996
        radius = 160 + (i * 31) % 400
        x, y = 700 + math.cos(angle) * radius, 380 + math.sin(angle) * radius * .66
        parts.append(f'<circle cx="{x:.2f}" cy="{y:.2f}" r="1.4" fill="#abcbce" opacity=".5"/>')
    parts.extend(['<circle cx="700" cy="380" r="101" fill="none" stroke="#b4ded4" stroke-opacity=".13"/><circle cx="700" cy="380" r="80" fill="none" stroke="#b4ded4" stroke-opacity=".25"/><circle cx="700" cy="380" r="59" fill="url(#pearl)"/>', mark(700, 387, 1.05, "#174f57"), '<text x="700" y="506" text-anchor="middle" font-family="system-ui,sans-serif" font-size="11" letter-spacing="4" fill="#a6d3ca">HUBUUM</text>', '</svg>'])
    return "\n".join(parts)


def fabric():
    parts = [svg_start("Layered translucent networks meet around the Hubuum hub", "0 0 1000 900"), '''<defs>
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
    for x, y, end in [(265, 337, 557), (736, 340, 562), (502, 170, 390), (498, 510, 730)]:
        parts.append(f'<path d="M{x} {y}V{end}" stroke="#4b7a8a" stroke-dasharray="3 6" opacity=".45"/><circle cx="{x}" cy="{y}" r="6" fill="#f4f1e9" stroke="#47798b"/><circle cx="{x}" cy="{end}" r="3" fill="#47798b"/>')
    parts.extend(['<path d="M500 340 610 393 500 446 390 393Z" fill="#286473" opacity=".13"/><path d="M500 305 610 358 500 411 390 358Z" fill="url(#tile)" stroke="white" stroke-width="1.5"/><path d="M390 358V375L500 428 610 375V358L500 411Z" fill="#b9d0d2" opacity=".7"/>', mark(500, 364, .9, "#174f57"), '<path d="M500 195V293 M500 435V631 M260 355 379 355 M623 355 742 355" fill="none" stroke="#386988" stroke-width="1.5"/><text x="752" y="359" font-family="system-ui,sans-serif" font-size="11" letter-spacing="3" fill="#345969">HUBUUM</text>', '</svg>'])
    return "\n".join(parts)


def story_art():
    return svg_start("Example model: the Atlas application runs on web-01, located in Oslo, and is owned by the Platform team", "0 0 800 550") + '''
    <defs><radialGradient id="wash"><stop stop-color="#61988f" stop-opacity=".2"/><stop offset="1" stop-color="#61988f" stop-opacity="0"/></radialGradient></defs>
    <circle cx="400" cy="280" r="270" fill="url(#wash)"/>
    <g fill="none" stroke="#75a59d" stroke-width="1.2"><path d="M250 155C400 155 400 155 550 155 M550 185C550 310 400 275 400 400"/></g>
    <g font-family="system-ui,sans-serif" text-anchor="middle"><g fill="#bdd4ce" font-size="12"><text x="400" y="136">runs on</text><text x="549" y="294">located in</text><text x="235" y="301">owned by</text></g>
    <g fill="#102f36" stroke="#577b79"><rect x="135" y="104" width="230" height="103" rx="9"/><rect x="435" y="104" width="230" height="103" rx="9"/><rect x="285" y="357" width="230" height="103" rx="9"/><rect x="62" y="357" width="174" height="83" rx="9"/></g>
    <g fill="#b6cfc9" font-size="10" letter-spacing="2"><text x="250" y="135">APPLICATION</text><text x="550" y="135">SERVER</text><text x="400" y="389">LOCATION</text><text x="149" y="387">TEAM</text></g>
    <g fill="#f1f5ee" font-size="25"><text x="250" y="175">Atlas</text><text x="550" y="175">web-01</text><text x="400" y="429">Oslo</text><text x="149" y="419" font-size="20">Platform</text></g></g>
    <path d="M250 207C250 275 149 290 149 357" fill="none" stroke="#75a59d" stroke-width="1.2"/>
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
        content = template.substitute(**concept, symbol=symbol, switcher=switcher)
        (ROOT / f'{concept["slug"]}.html').write_text(content)
    cards = "\n".join(f'''<a class="concept-card {c['slug']}" href="{c['slug']}.html"><div class="concept-art"><img src="assets/{c['slug']}.svg" alt="{escape(c['idea'])}"></div><div class="concept-copy"><span class="eyebrow">{c['number']} / {c['mood']}</span><h2>{c['name']} <span aria-hidden="true">↗</span></h2><p>{c['idea']}</p><span class="text-link">Explore this direction <span aria-hidden="true">→</span></span></div></a>''' for c in CONCEPTS)
    gallery = string.Template((ROOT / "gallery.html.template").read_text()).substitute(cards=cards, symbol=symbol)
    (ROOT / "index.html").write_text(gallery)


if __name__ == "__main__":
    render()
