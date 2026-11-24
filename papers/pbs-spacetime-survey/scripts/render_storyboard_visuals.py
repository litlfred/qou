#!/usr/bin/env python3
"""Generate crisp, lay-friendly SVG storyboard visuals for papers/pbs-spacetime-survey/assets/.

Uses mpmath at 60 decimal places (zero float64 literals or operations) and
emits standalone, GitHub-compatible vector SVGs with plain-English labels.
"""

from pathlib import Path
import mpmath as mp

mp.mp.dps = 60

ASSETS_DIR = Path(__file__).resolve().parent.parent / "assets"

BG = "#0d1326"
PANEL = "#131c36"
PANEL_ALT = "#182444"
BORDER = "#2a3b68"
TEXT = "#f1f5f9"
MUTED = "#94a3b8"
CYAN = "#38bdf8"
AMBER = "#f59e0b"
CORAL = "#fb7185"
GREEN = "#34d399"
VIOLET = "#a78bfa"
GOLD = "#fbbf24"
WHITE = "#ffffff"
SLATE = "#475569"

FONT = "system-ui, -apple-system, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"


def fmt(x) -> str:
    return mp.nstr(mp.mpf(x), 6, min_fixed=-4, max_fixed=6)


class SvgCanvas:
    def __init__(self, width: int = 960, height: int = 500, title: str = ""):
        self.w = width
        self.h = height
        self.title = title
        self.items: list[str] = []
        self.defs: list[str] = [
            f'<marker id="arrow-cyan" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 1 L 10 5 L 0 9 z" fill="{CYAN}"/></marker>',
            f'<marker id="arrow-amber" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 1 L 10 5 L 0 9 z" fill="{AMBER}"/></marker>',
            f'<marker id="arrow-green" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 1 L 10 5 L 0 9 z" fill="{GREEN}"/></marker>',
            f'<marker id="arrow-coral" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 1 L 10 5 L 0 9 z" fill="{CORAL}"/></marker>',
            f'<marker id="arrow-muted" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 1 L 10 5 L 0 9 z" fill="{MUTED}"/></marker>',
        ]

    def rect(self, x, y, w, h, fill=PANEL, stroke=BORDER, sw=1, rx=10, opacity=None, dash=None):
        op = f' opacity="{fmt(opacity)}"' if opacity is not None else ""
        da = f' stroke-dasharray="{dash}"' if dash else ""
        self.items.append(
            f'<rect x="{fmt(x)}" y="{fmt(y)}" width="{fmt(w)}" height="{fmt(h)}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{fmt(sw)}"{op}{da}/>'
        )

    def line(self, x1, y1, x2, y2, stroke=MUTED, sw=2, dash=None, marker_end=None, opacity=None):
        da = f' stroke-dasharray="{dash}"' if dash else ""
        mk = f' marker-end="url(#{marker_end})"' if marker_end else ""
        op = f' opacity="{fmt(opacity)}"' if opacity is not None else ""
        self.items.append(
            f'<line x1="{fmt(x1)}" y1="{fmt(y1)}" x2="{fmt(x2)}" y2="{fmt(y2)}" stroke="{stroke}" stroke-width="{fmt(sw)}" stroke-linecap="round"{da}{mk}{op}/>'
        )

    def circle(self, cx, cy, r, fill="none", stroke=CYAN, sw=2, dash=None, opacity=None):
        da = f' stroke-dasharray="{dash}"' if dash else ""
        op = f' opacity="{fmt(opacity)}"' if opacity is not None else ""
        self.items.append(
            f'<circle cx="{fmt(cx)}" cy="{fmt(cy)}" r="{fmt(r)}" fill="{fill}" stroke="{stroke}" stroke-width="{fmt(sw)}"{da}{op}/>'
        )

    def ellipse(self, cx, cy, rx, ry, fill="none", stroke=CYAN, sw=2, dash=None, opacity=None):
        da = f' stroke-dasharray="{dash}"' if dash else ""
        op = f' opacity="{fmt(opacity)}"' if opacity is not None else ""
        self.items.append(
            f'<ellipse cx="{fmt(cx)}" cy="{fmt(cy)}" rx="{fmt(rx)}" ry="{fmt(ry)}" fill="{fill}" stroke="{stroke}" stroke-width="{fmt(sw)}"{da}{op}/>'
        )

    def path(self, d: str, stroke=CYAN, sw=3, fill="none", dash=None, marker_end=None, opacity=None):
        da = f' stroke-dasharray="{dash}"' if dash else ""
        mk = f' marker-end="url(#{marker_end})"' if marker_end else ""
        op = f' opacity="{fmt(opacity)}"' if opacity is not None else ""
        self.items.append(
            f'<path d="{d}" fill="{fill}" stroke="{stroke}" stroke-width="{fmt(sw)}" stroke-linecap="round" stroke-linejoin="round"{da}{mk}{op}/>'
        )

    def polyline(self, pts, stroke=CYAN, sw=3, fill="none", close=False, opacity=None):
        coord = " ".join(f"{fmt(x)},{fmt(y)}" for x, y in pts)
        op = f' opacity="{fmt(opacity)}"' if opacity is not None else ""
        tag = "polygon" if close else "polyline"
        self.items.append(
            f'<{tag} points="{coord}" fill="{fill}" stroke="{stroke}" stroke-width="{fmt(sw)}" stroke-linecap="round" stroke-linejoin="round"{op}/>'
        )

    def text(self, x, y, s: str, size=15, fill=TEXT, anchor="middle", weight="normal", italic=False):
        esc = s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        st = ' font-style="italic"' if italic else ""
        self.items.append(
            f'<text x="{fmt(x)}" y="{fmt(y)}" fill="{fill}" font-family="{FONT}" font-size="{size}" font-weight="{weight}" text-anchor="{anchor}"{st}>{esc}</text>'
        )

    def header(self, title: str, subtitle: str = ""):
        self.text(self.w // 2, 34, title, size=20, fill=TEXT, weight="600")
        if subtitle:
            self.text(self.w // 2, 56, subtitle, size=13, fill=MUTED)

    def crossing_vertical(self, x_left, x_right, y_top, y_bot, over_is_left: bool, col_left: str, col_right: str, sw=5, bg=PANEL):
        ym = mp.mpf(y_top + y_bot) / 2
        d_lr = f"M {fmt(x_left)} {fmt(y_top)} C {fmt(x_left)} {fmt(ym)}, {fmt(x_right)} {fmt(ym)}, {fmt(x_right)} {fmt(y_bot)}"
        d_rl = f"M {fmt(x_right)} {fmt(y_top)} C {fmt(x_right)} {fmt(ym)}, {fmt(x_left)} {fmt(ym)}, {fmt(x_left)} {fmt(y_bot)}"
        if over_is_left:
            self.path(d_rl, stroke=col_right, sw=sw)
            self.path(d_lr, stroke=bg, sw=sw + 7)
            self.path(d_lr, stroke=col_left, sw=sw)
        else:
            self.path(d_lr, stroke=col_left, sw=sw)
            self.path(d_rl, stroke=bg, sw=sw + 7)
            self.path(d_rl, stroke=col_right, sw=sw)

    def save(self, filename: str):
        ASSETS_DIR.mkdir(parents=True, exist_ok=True)
        out = [
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {self.w} {self.h}" width="{self.w}" height="{self.h}">',
            f"<title>{self.title}</title>",
            "<defs>" + "".join(self.defs) + "</defs>",
            f'<rect x="0" y="0" width="{self.w}" height="{self.h}" rx="14" fill="{BG}"/>',
            *self.items,
            "</svg>",
        ]
        (ASSETS_DIR / filename).write_text("\n".join(out) + "\n", encoding="utf-8")


def build_sec01_grid_to_braids():
    c = SvgCanvas(960, 460, "From Background Coordinate Grid to Braided Strands")
    c.header(
        "Replacing an Empty Coordinate Grid with Braided Strands",
        "Time is step-by-step order (bottom to top); space is side-by-side order and strand swaps (left to right)",
    )
    c.rect(36, 78, 390, 346, fill=PANEL)
    c.text(231, 108, "Standard Starting Point", size=16, fill=MUTED, weight="600")
    c.text(231, 128, "Assumes an invisible coordinate box (t, x, y, z)", size=12, fill=MUTED)
    for k in range(6):
        gx = 90 + k * 52
        gy = 158 + k * 36
        c.line(gx, 155, gx, 345, stroke=SLATE, sw=1, dash="4 4", opacity=mp.mpf("0.55"))
        c.line(85, gy, 365, gy, stroke=SLATE, sw=1, dash="4 4", opacity=mp.mpf("0.55"))
    c.line(85, 345, 145, 295, stroke=CORAL, sw=2, marker_end="arrow-coral")
    c.line(85, 345, 175, 345, stroke=CORAL, sw=2, marker_end="arrow-coral")
    c.line(85, 345, 85, 260, stroke=CORAL, sw=2, marker_end="arrow-coral")
    c.text(231, 385, "Shifting empty space changes no physical measurement", size=12, fill=CORAL)

    c.line(442, 250, 514, 250, stroke=CYAN, sw=3, marker_end="arrow-cyan")
    c.text(478, 236, "Drop grid", size=12, fill=CYAN, weight="600")

    c.rect(530, 78, 394, 346, fill=PANEL)
    c.text(727, 108, "Relational Starting Point (Braids)", size=16, fill=TEXT, weight="600")
    c.text(727, 128, "Only strand order and over/under crossings are kept", size=12, fill=MUTED)
    xs = [650, 727, 804]
    c.crossing_vertical(xs[0], xs[1], 155, 218, True, CYAN, AMBER, sw=5)
    c.line(xs[2], 155, xs[2], 218, stroke=CORAL, sw=5)
    c.line(xs[0], 218, xs[0], 281, stroke=AMBER, sw=5)
    c.crossing_vertical(xs[1], xs[2], 218, 281, False, CYAN, CORAL, sw=5)
    c.crossing_vertical(xs[0], xs[1], 281, 344, True, AMBER, CORAL, sw=5)
    c.line(xs[2], 281, xs[2], 344, stroke=CYAN, sw=5)
    c.line(588, 338, 588, 162, stroke=GREEN, sw=2, marker_end="arrow-green")
    c.text(576, 252, "Before → After", size=11, fill=GREEN, anchor="end")
    c.line(645, 368, 809, 368, stroke=GOLD, sw=2, marker_end="arrow-amber")
    c.text(727, 392, "Side-by-side neighbors & swaps (no ruler needed)", size=12, fill=GOLD)
    c.save("sec01-grid-to-braids.svg")


def build_sec01_skein_relation():
    c = SvgCanvas(960, 440, "The Strand-Swapping Rule Controlled by One Number q")
    c.header(
        "Equation (1): One Number q Controls How Crossing Strands Differ",
        "Flipping an over-crossing into an under-crossing leaves a straight parallel piece weighted by q - 1/q",
    )
    c.rect(48, 92, 180, 220, fill=PANEL)
    c.text(138, 120, "Over-crossing (σᵢ)", size=15, fill=CYAN, weight="600")
    c.crossing_vertical(98, 178, 145, 275, True, CYAN, AMBER, sw=6)
    c.text(138, 298, "Left strand on top", size=12, fill=MUTED)

    c.text(258, 208, "−", size=34, fill=TEXT, weight="600")

    c.rect(288, 92, 180, 220, fill=PANEL)
    c.text(378, 120, "Under-crossing (σᵢ⁻¹)", size=15, fill=AMBER, weight="600")
    c.crossing_vertical(338, 418, 145, 275, False, CYAN, AMBER, sw=6)
    c.text(378, 298, "Left strand underneath", size=12, fill=MUTED)

    c.text(505, 208, "=", size=30, fill=TEXT, weight="600")
    c.rect(538, 170, 146, 68, fill=PANEL_ALT, stroke=GOLD, sw=2)
    c.text(611, 198, "q − 1/q", size=19, fill=GOLD, weight="600")
    c.text(611, 222, "(zero if q = 1)", size=12, fill=MUTED)
    c.text(708, 208, "×", size=26, fill=TEXT, weight="600")

    c.rect(732, 92, 180, 220, fill=PANEL)
    c.text(822, 120, "Uncrossed strands (1)", size=15, fill=GREEN, weight="600")
    c.line(782, 145, 782, 275, stroke=CYAN, sw=6)
    c.line(862, 145, 862, 275, stroke=AMBER, sw=6)
    c.text(822, 298, "Straight ahead", size=12, fill=MUTED)

    c.rect(48, 336, 864, 74, fill=PANEL_ALT)
    c.text(
        480,
        364,
        "What happens if you twist two strands twice in a row:   σᵢ² = (q − 1/q) σᵢ + 1",
        size=16,
        fill=TEXT,
        weight="600",
    )
    c.text(
        480,
        390,
        "At q = 1, two swaps undo each other completely. When q > 1, a double twist leaves a lasting single-twist echo.",
        size=13,
        fill=MUTED,
    )
    c.save("sec01-skein-relation.svg")


def build_sec01_loop_quotient():
    c = SvgCanvas(960, 450, "Closing Strands into Measurement Loops and Built-In Distance")
    c.header(
        "Closing Strands into Loops & Simplifying Invisible Tangles",
        "Looping top ends back to bottom ends reads out a number; tangles that always read zero are dropped",
    )
    c.rect(40, 82, 430, 336, fill=PANEL)
    c.text(255, 112, "1. Measurement = Closing the Braid into a Loop", size=15, fill=TEXT, weight="600")
    c.rect(145, 175, 110, 56, fill=PANEL_ALT, stroke=CYAN, sw=2)
    c.text(200, 208, "Step B", size=15, fill=CYAN, weight="600")
    c.rect(145, 255, 110, 56, fill=PANEL_ALT, stroke=AMBER, sw=2)
    c.text(200, 288, "Step A", size=15, fill=AMBER, weight="600")
    for k, dx in enumerate([-28, 0, 28]):
        x0 = 200 + dx
        xr = 315 + k * 22
        c.line(x0, 231, x0, 255, stroke=TEXT, sw=2)
        c.path(
            f"M {fmt(x0)} 175 L {fmt(x0)} 150 C {fmt(x0)} 128, {fmt(xr)} 128, {fmt(xr)} 165 L {fmt(xr)} 320 C {fmt(xr)} 355, {fmt(x0)} 355, {fmt(x0)} 330 L {fmt(x0)} 311",
            stroke=GOLD,
            sw=2,
        )
    c.circle(337, 242, 18, fill=PANEL_ALT, stroke=VIOLET, sw=2)
    c.text(337, 247, "twist", size=11, fill=VIOLET, weight="600")
    c.text(255, 382, "At q > 1, sliding Step A around the loop distinguishes", size=12, fill=MUTED)
    c.text(255, 402, "left-handed and right-handed return paths.", size=12, fill=GOLD, weight="600")

    c.rect(496, 82, 424, 336, fill=PANEL)
    c.text(708, 112, "2. Invisible Differences Simplify to 5 Patterns", size=15, fill=TEXT, weight="600")
    c.rect(526, 142, 364, 78, fill=PANEL_ALT, stroke=SLATE, sw=1, dash="5 4")
    c.text(708, 170, "Tangle combinations that read 0 on every loop", size=13, fill=MUTED)
    c.text(708, 196, "cannot affect any observation → set equal to 0", size=12, fill=CORAL)
    c.line(708, 228, 708, 256, stroke=GREEN, sw=2, marker_end="arrow-green")
    labels = ["Straight", "Left turn", "Right turn", "Left wave", "Right wave"]
    for idx, lab in enumerate(labels):
        bx = 532 + idx * 72
        by = 266
        c.rect(bx, by, 60, 92, fill=PANEL_ALT, stroke=GREEN, sw=1, rx=6)
        s0, s1, s2 = bx + 14, bx + 30, bx + 46
        yt, yb = by + 14, by + 78
        if idx == 0:
            c.line(s0, yt, s0, yb, stroke=CYAN, sw=3)
            c.line(s1, yt, s1, yb, stroke=CYAN, sw=3)
            c.line(s2, yt, s2, yb, stroke=CYAN, sw=3)
        elif idx == 1:
            c.path(f"M {s0} {yt} C {s0} {yt+24}, {s1} {yt+24}, {s1} {yt}", stroke=CYAN, sw=3)
            c.path(f"M {s0} {yb} C {s0} {yb-24}, {s1} {yb-24}, {s1} {yb}", stroke=CYAN, sw=3)
            c.line(s2, yt, s2, yb, stroke=CYAN, sw=3)
        elif idx == 2:
            c.line(s0, yt, s0, yb, stroke=CYAN, sw=3)
            c.path(f"M {s1} {yt} C {s1} {yt+24}, {s2} {yt+24}, {s2} {yt}", stroke=CYAN, sw=3)
            c.path(f"M {s1} {yb} C {s1} {yb-24}, {s2} {yb-24}, {s2} {yb}", stroke=CYAN, sw=3)
        elif idx == 3:
            c.path(f"M {s0} {yt} C {s0} {yt+22}, {s1} {yt+22}, {s1} {yt}", stroke=CYAN, sw=3)
            c.path(f"M {s1} {yb} C {s1} {yb-22}, {s2} {yb-22}, {s2} {yb}", stroke=CYAN, sw=3)
            c.path(f"M {s2} {yt} C {s2} {by+46}, {s0} {by+46}, {s0} {yb}", stroke=CYAN, sw=3)
        else:
            c.path(f"M {s1} {yt} C {s1} {yt+22}, {s2} {yt+22}, {s2} {yt}", stroke=CYAN, sw=3)
            c.path(f"M {s0} {yb} C {s0} {yb-22}, {s1} {yb-22}, {s1} {yb}", stroke=CYAN, sw=3)
            c.path(f"M {s0} {yt} C {s0} {by+46}, {s2} {by+46}, {s2} {yb}", stroke=CYAN, sw=3)
        c.text(bx + 30, by + 110, lab, size=10, fill=GREEN, weight="600")
    c.text(708, 400, "Built-in ruler: distance = max readout shift under one swap", size=12, fill=MUTED)
    c.save("sec01-loop-quotient.svg")


def build_sec02_model_vs_measurement():
    c = SvgCanvas(960, 470, "Mathematical Model vs Physical Measurement and the Three Inputs")
    c.header(
        "Rules of the Game: Mathematical Model vs. Laboratory Measurement",
        "Only three measured numbers set units and q₀; every other compared quantity has zero adjustable knobs",
    )
    inputs = [
        ("1. Electron Mass mₑ", "0.51099895 MeV", "Sets the energy unit (MeV)", CYAN),
        ("2. Proton/Electron Ratio", "1836.1526734 (Input Pin)", "Fixes q₀ = 1.10997858275...", GOLD),
        ("3. Pion Mass Scale m_π", "139.57039 MeV", "Sets nuclear touch distance 1.41 fm", VIOLET),
    ]
    for i, (t1, t2, t3, col) in enumerate(inputs):
        bx = 44 + i * 298
        c.rect(bx, 76, 276, 86, fill=PANEL, stroke=col, sw=2)
        c.text(bx + 138, 102, t1, size=14, fill=col, weight="600")
        c.text(bx + 138, 124, t2, size=14, fill=TEXT, weight="600")
        c.text(bx + 138, 146, t3, size=12, fill=MUTED)
        c.line(bx + 138, 162, bx + 138, 192, stroke=col, sw=2, marker_end="arrow-muted")

    c.rect(44, 198, 402, 236, fill=PANEL, stroke=CYAN, sw=2)
    c.text(245, 228, "Inside the Mathematical Model", size=16, fill=CYAN, weight="600")
    c.text(245, 254, "• Words like 'photon' and 'proton' name specific braids", size=13, fill=TEXT)
    c.text(245, 280, "• Knot volumes and closed loops output pure ratios", size=13, fill=TEXT)
    c.text(245, 306, "• Zero tuned exponents, cutoffs, or knot-table shopping", size=13, fill=TEXT)
    c.text(245, 340, "Outputs pure unit-free numbers", size=13, fill=GOLD, weight="600")
    c.text(245, 364, "(e.g. 1/α = 137.035999127,  m_μ/mₑ = 206.768326)", size=12, fill=MUTED)
    c.text(245, 404, "mₚ / mₑ is used to solve for q₀, so it is NOT a prediction", size=12, fill=CORAL, weight="600")

    c.line(480, 190, 480, 442, stroke=GOLD, sw=3, dash="7 5")
    c.rect(448, 292, 64, 44, fill=PANEL_ALT, stroke=GOLD, sw=2, rx=6)
    c.text(480, 311, "Compare", size=11, fill=GOLD, weight="600")
    c.text(480, 326, "Here", size=11, fill=GOLD, weight="600")

    c.rect(514, 198, 402, 236, fill=PANEL, stroke=GREEN, sw=2)
    c.text(715, 228, "Laboratory Reference Tables", size=16, fill=GREEN, weight="600")
    c.text(715, 256, "• Atomic & lepton precision constants (CODATA)", size=13, fill=TEXT)
    c.text(715, 284, "• Collider & neutrino measurements (PDG)", size=13, fill=TEXT)
    c.text(715, 312, "• Nuclear masses & radioactive half-lives (AME2020)", size=13, fill=TEXT)
    c.rect(544, 344, 342, 68, fill=PANEL_ALT, stroke=BORDER)
    c.text(715, 369, "Why zero curve-fitting matters:", size=13, fill=TEXT, weight="600")
    c.text(715, 392, "When a formula misses, the miss points to what is missing", size=12, fill=MUTED)
    c.save("sec02-model-vs-measurement.svg")


def build_sec02_figure_eight_tetrahedra():
    c = SvgCanvas(960, 470, "Figure-Eight Knot Volume and the Muon Mass Ratio Test")
    c.header(
        "Equations (2)–(3): Figure-Eight Knot Volume & the Muon Mass Test",
        "Space around the 4-crossing figure-eight knot fits two curved 3D pyramids of total volume 2.0298832...",
    )
    c.rect(36, 80, 290, 356, fill=PANEL)
    c.text(181, 108, "Figure-Eight Knot (4₁)", size=15, fill=CYAN, weight="600")
    c.text(181, 128, "Simplest 4-crossing knot", size=12, fill=MUTED)
    N = 240
    pts = []
    for k in range(N + 1):
        t = 2 * mp.pi * mp.mpf(k) / N
        x = 181 + 88 * mp.sin(2 * t) * (mp.mpf("0.72") + mp.mpf("0.28") * mp.cos(t))
        y = 258 + 96 * mp.sin(t) + 26 * mp.sin(3 * t)
        pts.append((x, y))
    c.polyline(pts, stroke=CYAN, sw=6)
    for cx, cy, col in [(181, 198, GOLD), (181, 318, GOLD), (144, 258, CYAN), (218, 258, CYAN)]:
        c.circle(cx, cy, 8, fill=PANEL, stroke=col, sw=3)
    c.text(181, 408, "Surrounding space curves inward", size=12, fill=MUTED)

    c.rect(344, 80, 292, 356, fill=PANEL)
    c.text(490, 108, "Two Curved 3D Pyramids", size=15, fill=GREEN, weight="600")
    c.text(490, 128, "60° edge angles: 2 × 1.01494 = 2.02988", size=12, fill=MUTED)
    top = (490, 152)
    bot = (490, 364)
    p1, p2, p3 = (392, 258), (588, 258), (508, 286)
    c.polyline([top, p1, p3], stroke=GREEN, sw=2, fill="#103637", close=True, opacity=mp.mpf("0.65"))
    c.polyline([top, p3, p2], stroke=GREEN, sw=2, fill="#134e4a", close=True, opacity=mp.mpf("0.65"))
    c.polyline([bot, p1, p3], stroke=CYAN, sw=2, fill="#112e4a", close=True, opacity=mp.mpf("0.65"))
    c.polyline([bot, p3, p2], stroke=CYAN, sw=2, fill="#163b5c", close=True, opacity=mp.mpf("0.65"))
    c.line(p1[0], p1[1], p2[0], p2[1], stroke=GOLD, sw=2, dash="5 4")
    for vx, vy in [top, bot, p1, p2, p3]:
        c.circle(vx, vy, 5, fill=GOLD, stroke=BG, sw=1)
    c.text(490, 408, "Exact knot volume Vol(4₁) = 2.0298832...", size=13, fill=GOLD, weight="600")

    c.rect(654, 80, 270, 356, fill=PANEL)
    c.text(789, 108, "Testing the Muon Mass Ratio", size=15, fill=TEXT, weight="600")
    c.rect(674, 134, 230, 74, fill=PANEL_ALT, stroke=GOLD, sw=1)
    c.text(789, 158, "Pinned from mₚ / mₑ:", size=12, fill=GOLD, weight="600")
    c.text(789, 180, "q₀ = 1.10997858275...", size=13, fill=TEXT, weight="600")
    c.text(789, 198, "step size 1 − 1/q₀ = 0.0990817", size=11, fill=MUTED)
    c.line(789, 210, 789, 236, stroke=CYAN, sw=2, marker_end="arrow-cyan")
    c.rect(674, 240, 230, 92, fill=PANEL_ALT, stroke=CYAN, sw=1)
    c.text(789, 264, "Model m_μ/mₑ:    206.7683264", size=13, fill=CYAN, weight="600")
    c.text(789, 288, "Measured m_μ/mₑ: 206.7682827", size=13, fill=GREEN, weight="600")
    c.text(789, 314, "Difference: 211 parts per billion", size=12, fill=CORAL, weight="600")
    c.text(789, 366, "Matches to 1 part in 5 million,", size=12, fill=MUTED)
    c.text(789, 386, "yet sits 9.5 error bars outside", size=12, fill=MUTED)
    c.text(789, 406, "lab uncertainty — left unpatched.", size=12, fill=CORAL)
    c.save("sec02-figure-eight-tetrahedra.svg")


def build_sec03_photon_and_borromean():
    c = SvgCanvas(960, 480, "The Four-Term Photon, Two-Ring Electron, and Three-Ring Proton")
    c.header(
        "Equation (4): Light, the Two-Ring Electron, and the Three-Ring Proton Core",
        "Combining two light braids produces a linked two-ring electron and three interlocked proton rings",
    )
    c.rect(36, 78, 888, 156, fill=PANEL)
    c.text(480, 102, "A Photon Combines Four 3-Strand Moves:   γ = 1 + φ₀ σ₀ + φ₁ σ₁ + φ₀₁ σ₀σ₁⁻¹", size=15, fill=GOLD, weight="600")
    tiles = [
        ("1 (Straight)", "none"),
        ("φ₀ σ₀ (Left pair over)", "s0"),
        ("φ₁ σ₁ (Right pair over)", "s1"),
        ("φ₀₁ σ₀σ₁⁻¹ (Over then under)", "v"),
    ]
    for idx, (lab, mode) in enumerate(tiles):
        bx = 64 + idx * 214
        c.rect(bx, 116, 188, 104, fill=PANEL_ALT, stroke=VIOLET if mode == "v" else BORDER, sw=2 if mode == "v" else 1)
        x0, x1, x2 = bx + 54, bx + 94, bx + 134
        yt, ym, yb = 128, 160, 192
        if mode == "none":
            c.line(x0, yt, x0, yb, stroke=WHITE, sw=4)
            c.line(x1, yt, x1, yb, stroke=WHITE, sw=4)
            c.line(x2, yt, x2, yb, stroke=WHITE, sw=4)
        elif mode == "s0":
            c.crossing_vertical(x0, x1, yt, yb, True, CYAN, AMBER, sw=4, bg=PANEL_ALT)
            c.line(x2, yt, x2, yb, stroke=WHITE, sw=4)
        elif mode == "s1":
            c.line(x0, yt, x0, yb, stroke=WHITE, sw=4)
            c.crossing_vertical(x1, x2, yt, yb, True, AMBER, CORAL, sw=4, bg=PANEL_ALT)
        else:
            c.crossing_vertical(x0, x1, yt, ym, True, CYAN, AMBER, sw=4, bg=PANEL_ALT)
            c.line(x2, yt, x2, ym, stroke=CORAL, sw=4)
            c.line(x0, ym, x0, yb, stroke=AMBER, sw=4)
            c.crossing_vertical(x1, x2, ym, yb, False, CYAN, CORAL, sw=4, bg=PANEL_ALT)
        c.text(bx + 94, 211, lab, size=11, fill=VIOLET if mode == "v" else MUTED, weight="600")

    c.rect(36, 250, 430, 200, fill=PANEL)
    c.text(251, 278, "Electron Braid σ₀σ₁σ₀ → Two Linked Rings", size=15, fill=CYAN, weight="600")
    c.circle(215, 352, 46, stroke=CYAN, sw=7)
    c.circle(285, 352, 46, stroke=AMBER, sw=7)
    c.path("M 238 313 A 46 46 0 0 1 260 342", stroke=PANEL, sw=13)
    c.path("M 235 311 A 46 46 0 0 1 261 345", stroke=CYAN, sw=7)
    c.text(251, 428, "Hopf link (trefoil knot backup; exchange sign unsolved)", size=12, fill=MUTED)

    c.rect(494, 250, 430, 200, fill=PANEL)
    c.text(709, 278, "Proton Core (σ₀σ₁⁻¹)³ → Three Borromean Rings", size=15, fill=GREEN, weight="600")
    r = 38
    c1 = (709, 332)
    c2 = (683, 372)
    c3 = (735, 372)
    c.circle(c1[0], c1[1], r, stroke=CORAL, sw=6)
    c.circle(c2[0], c2[1], r, stroke=GREEN, sw=6)
    c.circle(c3[0], c3[1], r, stroke=CYAN, sw=6)
    c.circle(673, 336, 6, fill=GREEN, stroke=PANEL, sw=2)
    c.circle(745, 336, 6, fill=CORAL, stroke=PANEL, sw=2)
    c.circle(709, 396, 6, fill=CYAN, stroke=PANEL, sw=2)
    c.text(709, 432, "Cut any one quark ring and the other two fall apart", size=12, fill=MUTED)
    c.save("sec03-photon-and-borromean.svg")


def build_sec03_brings_surface_pentagons():
    c = SvgCanvas(960, 460, "Bring's Four-Holed Surface and the Two Matching Doughnut Knots")
    c.header(
        "A Four-Holed Symmetric Surface & the Only Two Matching Doughnut Knots",
        "Permuting 5 balanced coordinates shapes a 4-holed surface; only 9-crossing and 10-crossing torus knots share 4 holes",
    )
    c.rect(36, 80, 444, 348, fill=PANEL)
    c.text(258, 108, "Bring's Four-Holed Surface (120 Symmetries)", size=15, fill=VIOLET, weight="600")
    c.text(258, 128, "Five coordinates summing to zero in power 1, 2, and 3", size=12, fill=MUTED)
    cx, cy = 258, 268
    c.circle(cx, cy, 108, fill="#1e1b4b", stroke=VIOLET, sw=3)
    pent = []
    for k in range(5):
        ang = -mp.pi / 2 + 2 * mp.pi * k / 5
        pent.append((cx + 96 * mp.cos(ang), cy + 96 * mp.sin(ang)))
    c.polyline(pent, stroke=GOLD, sw=2, close=True, opacity=mp.mpf("0.7"))
    for k, (px, py) in enumerate(pent):
        c.circle(px, py, 6, fill=GOLD, stroke=BG, sw=1)
        c.text(px + 16 * mp.cos(-mp.pi / 2 + 2 * mp.pi * k / 5), py + 16 * mp.sin(-mp.pi / 2 + 2 * mp.pi * k / 5) + 4, f"z{k+1}", size=11, fill=GOLD, weight="600")
    for hx, hy in [(cx - 38, cy - 34), (cx + 38, cy - 34), (cx - 38, cy + 38), (cx + 38, cy + 38)]:
        c.ellipse(hx, hy, 22, 13, fill=BG, stroke=CYAN, sw=2)
        c.path(f"M {fmt(hx-15)} {fmt(hy+2)} Q {fmt(hx)} {fmt(hy+12)} {fmt(hx+15)} {fmt(hy+2)}", stroke=VIOLET, sw=2)
    c.text(258, 404, "Surface hole count (genus):  g = 4", size=13, fill=CYAN, weight="600")

    c.rect(500, 80, 424, 348, fill=PANEL)
    c.text(712, 108, "Which Doughnut Knots T(p, r) Have 4 Holes?", size=15, fill=TEXT, weight="600")
    c.text(712, 128, "Hole count of knot T(p, r):  g = (p − 1)(r − 1) / 2", size=12, fill=MUTED)
    rows = [
        ("T(2, 3)", "3", "(1 × 2)/2 = 1", "Too few", MUTED),
        ("T(2, 5)", "5", "(1 × 4)/2 = 2", "Too few", MUTED),
        ("T(2, 7)", "7", "(1 × 6)/2 = 3", "Too few", MUTED),
        ("T(2, 9)", "9", "(1 × 8)/2 = 4", "Exact match", GOLD),
        ("T(3, 5)", "10", "(2 × 4)/2 = 4", "Exact match", GOLD),
        ("T(3, 7)", "14", "(2 × 6)/2 = 6", "Too many", SLATE),
    ]
    c.text(552, 162, "Knot", size=12, fill=MUTED, weight="600")
    c.text(632, 162, "Crossings", size=12, fill=MUTED, weight="600")
    c.text(738, 162, "Holes g", size=12, fill=MUTED, weight="600")
    c.text(850, 162, "Fits g = 4?", size=12, fill=MUTED, weight="600")
    for idx, (kn, cr, gf, st, col) in enumerate(rows):
        ry = 176 + idx * 38
        highlight = col == GOLD
        c.rect(520, ry, 384, 32, fill="#292524" if highlight else PANEL_ALT, stroke=GOLD if highlight else BORDER, sw=2 if highlight else 1, rx=6)
        c.text(552, ry + 21, kn, size=13, fill=col, weight="600")
        c.text(632, ry + 21, cr, size=13, fill=TEXT if highlight else MUTED, weight="600" if highlight else "normal")
        c.text(738, ry + 21, gf, size=13, fill=TEXT if highlight else MUTED)
        c.text(850, ry + 21, st, size=12, fill=col, weight="600")
    c.text(712, 414, "Only 9 and 10 crossings fit g = 4 → set the strength of light", size=12, fill=GOLD, weight="600")
    c.save("sec03-brings-surface-pentagons.svg")


def _draw_torus_knot(c: SvgCanvas, cx, cy, R_maj, r_min, p: int, r: int, col: str, bg=PANEL):
    N = 420
    pts3 = []
    for k in range(N):
        t = 2 * mp.pi * mp.mpf(k) / N
        rad = R_maj + r_min * mp.cos(r * t)
        x = cx + rad * mp.cos(p * t)
        y = cy + rad * mp.sin(p * t)
        z = mp.sin(r * t)
        pts3.append((x, y, z, k))
    segs = []
    for k in range(N):
        x1, y1, z1, _ = pts3[k]
        x2, y2, z2, _ = pts3[(k + 1) % N]
        segs.append(((z1 + z2) / 2, x1, y1, x2, y2))
    segs.sort(key=lambda s: s[0])
    for _, x1, y1, x2, y2 in segs:
        c.line(x1, y1, x2, y2, stroke=bg, sw=9)
        c.line(x1, y1, x2, y2, stroke=col, sw=4)


def build_sec04_torus_knots_alpha():
    c = SvgCanvas(960, 470, "The 9-Crossing and 10-Crossing Knots and the Strength of Light")
    c.header(
        "Equations (5)–(6): Stretching 9 × 10 = 90 into 137.035999127 at q₀",
        "Curved q-numbers stretch the 9-crossing and 10-crossing genus-4 knots directly to the fine-structure constant",
    )
    c.rect(36, 80, 265, 270, fill=PANEL)
    c.text(168, 106, "T(2, 9) — 9 Crossings", size=14, fill=CYAN, weight="600")
    _draw_torus_knot(c, 168, 218, 66, 26, 2, 9, CYAN)
    c.text(168, 334, "Stretched [9] = 10.3350", size=12, fill=MUTED)

    c.rect(318, 80, 265, 270, fill=PANEL)
    c.text(450, 106, "T(3, 5) — 10 Crossings", size=14, fill=GOLD, weight="600")
    _draw_torus_knot(c, 450, 218, 64, 28, 3, 5, GOLD)
    c.text(450, 334, "Stretched [10] = 11.9303", size=12, fill=MUTED)

    c.rect(600, 80, 324, 270, fill=PANEL)
    c.text(762, 106, "Assembling 1 / α (g = 4)", size=15, fill=TEXT, weight="600")
    parts = [
        ("Knot product q₀ · [9] · [10]", "+136.86022", GOLD),
        ("4-hole surface curvature", "  +0.21221", VIOLET),
        ("Self-feedback loop term", "  −0.03643", CYAN),
    ]
    for i, (k, v, col) in enumerate(parts):
        ry = 132 + i * 44
        c.rect(618, ry, 288, 36, fill=PANEL_ALT, stroke=BORDER, rx=6)
        c.text(630, ry + 23, k, size=12, fill=MUTED, anchor="start")
        c.text(894, ry + 23, v, size=13, fill=col, anchor="end", weight="600")
    c.line(620, 272, 904, 272, stroke=BORDER, sw=2)
    c.text(630, 298, "Model 1/α:", size=13, fill=TEXT, anchor="start", weight="600")
    c.text(898, 298, "137.035999127", size=14, fill=GREEN, anchor="end", weight="600")
    c.text(630, 322, "Measured:", size=13, fill=MUTED, anchor="start")
    c.text(898, 322, "137.035999177", size=13, fill=TEXT, anchor="end")

    c.rect(36, 366, 888, 78, fill=PANEL_ALT)
    c.line(90, 398, 860, 398, stroke=SLATE, sw=4)
    c.circle(150, 398, 7, fill=MUTED, stroke=BG, sw=2)
    c.text(150, 384, "At q = 1:  1 × 9 × 10 = 90", size=12, fill=MUTED)
    c.circle(790, 398, 8, fill=GREEN, stroke=BG, sw=2)
    c.text(790, 384, "At q₀ = 1.10997858:  137.035999127 (0.4 ppb)", size=12, fill=GREEN, weight="600")
    c.line(164, 398, 776, 398, stroke=GOLD, sw=3, marker_end="arrow-green")
    c.text(480, 428, "Caveat: Loop-weight step is still unproved; using muon q₀ instead of proton q₀ shifts 1/α by 79 ppb.", size=12, fill=CORAL)
    c.save("sec04-torus-knots-alpha.svg")


def build_sec04_electroweak_higgs_rg():
    c = SvgCanvas(960, 460, "Higgs Energy Bowl and Force Strength Evolution")
    c.header(
        "The Higgs Boson Mass (125.23 GeV) & Force Strengths at High Energy",
        "Strong force matches at 0.1185 (+0.41%), while single-step weak-mixing evolution misses 0.2312",
    )
    c.rect(36, 80, 434, 348, fill=PANEL)
    c.text(253, 108, "Higgs Energy Bowl & Radial Mass", size=15, fill=GREEN, weight="600")
    c.text(253, 128, "Circular valley feeds W±, Z⁰; flat ray keeps light massless", size=11, fill=MUTED)
    pts = []
    for k in range(121):
        u = -mp.mpf("1.45") + mp.mpf("2.90") * k / 120
        val = (u**2 - 1) ** 2
        px = 253 + u * 112
        py = 338 - val * 110
        pts.append((px, py))
    c.polyline(pts, stroke=CYAN, sw=4)
    c.circle(253 + 112, 338, 8, fill=GREEN, stroke=BG, sw=2)
    c.line(253, 338, 253 + 112, 338, stroke=GOLD, sw=2, dash="4 4", marker_end="arrow-amber")
    c.text(309, 356, "Valley radius = 246.22 GeV", size=12, fill=GOLD, weight="600")
    c.text(253, 388, "Model Higgs: 125.23 GeV  |  Measured: 125.20 ± 0.11 GeV", size=12, fill=GREEN, weight="600")
    c.text(253, 410, "Difference: +0.024% (bowl steepness λ_H = 0.1293)", size=12, fill=MUTED)

    c.rect(490, 80, 434, 348, fill=PANEL)
    c.text(707, 108, "Force Strengths at the Z-Boson Energy M_Z", size=15, fill=TEXT, weight="600")
    c.rect(514, 132, 386, 118, fill=PANEL_ALT, stroke=GREEN, sw=2)
    c.text(707, 156, "Strong Force α_s(M_Z) — Close Agreement", size=14, fill=GREEN, weight="600")
    c.text(707, 180, "Base proton scale: mₚ (q₀² − 1) = 217.73 MeV", size=12, fill=TEXT)
    c.text(707, 206, "Evolved to M_Z:   Model 0.1185   vs.   Measured 0.1180", size=12, fill=GREEN, weight="600")
    c.text(707, 228, "Difference: +0.41% (within lab uncertainty)", size=12, fill=MUTED)

    c.rect(514, 268, 386, 138, fill=PANEL_ALT, stroke=CORAL, sw=2)
    c.text(707, 292, "Weak Mixing Angle sin²θ_W(M_Z) — Unsolved Gap", size=14, fill=CORAL, weight="600")
    c.text(707, 316, "High-symmetry starting ratio:  3 / 8 = 0.375", size=12, fill=TEXT)
    c.text(707, 342, "Short 4-step evolution stops at 0.342  (measured: 0.2312)", size=12, fill=CORAL, weight="600")
    c.text(707, 366, "Long single-step evolution hits 0.2312 but drops α_s to 0.074", size=12, fill=MUTED)
    c.text(707, 388, "No extra mass threshold is invented to patch the two.", size=11, fill=CORAL)
    c.save("sec04-electroweak-higgs-rg.svg")


def build_sec05_unknot_neutrino_framing():
    c = SvgCanvas(960, 460, "Simple Loop Neutrino Mass and Ribbon Twist")
    c.header(
        "Equation (7): Why a Simple Unknotted Loop Weighs 40 Million Times Less Than an Electron",
        "A plain loop has zero knot volume, so neutrino mass comes only from 12 tiny weak-switch steps (q₀² − 1)¹²",
    )
    c.rect(36, 80, 520, 348, fill=PANEL)
    c.text(296, 108, "Plain Loop (Zero Knot Volume) + 12 Weak Steps", size=15, fill=CYAN, weight="600")
    c.circle(124, 208, 48, stroke=CYAN, sw=6)
    c.text(124, 204, "Plain Loop", size=13, fill=CYAN, weight="600")
    c.text(124, 224, "Volume = 0", size=12, fill=MUTED)
    c.line(182, 208, 224, 208, stroke=GOLD, sw=2, marker_end="arrow-amber")
    c.rect(232, 152, 304, 112, fill=PANEL_ALT, stroke=GOLD, sw=2)
    c.text(384, 178, "mₑ × (q₀² − 1)¹²", size=16, fill=GOLD, weight="600")
    c.text(384, 202, "= 511,000 eV × (0.23205)¹²", size=12, fill=MUTED)
    c.text(384, 228, "= 12.5 meV  (17.6 meV with knot dressing)", size=13, fill=GREEN, weight="600")
    c.text(384, 250, "2-step solar loop control: 9.12 meV (+5.1%)", size=12, fill=CYAN)

    c.text(296, 296, "Comparison with Measured Neutrino Mass-Splitting Window:", size=12, fill=TEXT, weight="600")
    c.rect(76, 314, 440, 32, fill=PANEL_ALT, stroke=BORDER, rx=6)
    c.rect(146, 318, 250, 24, fill="#064e3b", stroke=GREEN, sw=1, rx=4)
    c.text(271, 335, "Measured window: 8.68 to 49.5 meV", size=11, fill=GREEN, weight="600")
    c.circle(182, 330, 6, fill=GOLD, stroke=BG, sw=1)
    c.circle(214, 330, 6, fill=CYAN, stroke=BG, sw=1)
    c.text(296, 376, "Total of 3 neutrinos: 0.016–0.036 eV  (safely under < 0.12 eV sky limit)", size=12, fill=MUTED)
    c.text(296, 402, "8 steps gives 4.3 eV (too heavy); 14 steps gives 0.67 meV (too light)", size=11, fill=CORAL)

    c.rect(576, 80, 348, 348, fill=PANEL)
    c.text(750, 108, "Ribbon Twist: Distinct vs. Self-Conjugate", size=15, fill=VIOLET, weight="600")
    c.rect(600, 134, 300, 124, fill=PANEL_ALT, stroke=CYAN, sw=1)
    c.text(750, 158, "Full Integer Ribbon Twist", size=14, fill=CYAN, weight="600")
    c.text(750, 182, "+1 twist ≠ −1 twist (distinct antiparticle)", size=12, fill=TEXT)
    c.text(750, 206, "→ Keeps matter count strictly conserved", size=12, fill=GREEN)
    c.text(750, 228, "→ Rare neutrinoless nuclear decay does not occur", size=11, fill=MUTED)

    c.rect(600, 276, 300, 128, fill=PANEL_ALT, stroke=VIOLET, sw=1)
    c.text(750, 300, "Clock-of-2 Ribbon Twist (Even/Odd)", size=14, fill=VIOLET, weight="600")
    c.text(750, 324, "Two full twists unwind back to zero", size=12, fill=TEXT)
    c.text(750, 348, "→ Neutrino acts as its own antiparticle via Higgs pair", size=12, fill=GOLD)
    c.text(750, 372, "→ Testable in underground double-beta detectors", size=11, fill=MUTED)
    c.save("sec05-unknot-neutrino-framing.svg")


def build_sec05_generations_and_pmns():
    c = SvgCanvas(960, 450, "Three Matter Copies and Neutrino Mixing Angles")
    c.header(
        "Why Three Matter Families? (Unsolved) & Neutrino Mixing Angles",
        "Four surface waves split into 3 + 1 under 4-way symmetry, while strand crossing strength h sets mixing",
    )
    c.rect(36, 80, 440, 338, fill=PANEL)
    c.text(256, 108, "Why 3 Families of Matter? (Unsolved Filter)", size=15, fill=CORAL, weight="600")
    c.rect(136, 132, 240, 44, fill=PANEL_ALT, stroke=VIOLET, sw=2)
    c.text(256, 159, "4 Natural Wave Modes on the 4-Holed Surface", size=12, fill=VIOLET, weight="600")
    c.line(206, 176, 152, 220, stroke=GREEN, sw=2, marker_end="arrow-green")
    c.line(306, 176, 356, 220, stroke=CORAL, sw=2, marker_end="arrow-coral")
    c.rect(60, 226, 190, 96, fill=PANEL_ALT, stroke=GREEN, sw=2)
    c.text(155, 250, "4-Way Symmetry Split", size=13, fill=GREEN, weight="600")
    c.text(155, 276, "4  =  3  +  1", size=16, fill=TEXT, weight="600")
    c.text(155, 300, "3-family group + 1 solo", size=12, fill=MUTED)

    c.rect(268, 226, 188, 96, fill=PANEL_ALT, stroke=CORAL, sw=2)
    c.text(362, 250, "Other Symmetry Slices", size=13, fill=CORAL, weight="600")
    c.text(362, 276, "Give 4, 3, or 2", size=15, fill=TEXT, weight="600")
    c.text(362, 300, "Why nature picks 3 is unproved", size=11, fill=CORAL)

    c.text(256, 356, "Also unsolved: Heavy tau electron cousin (m_τ / mₑ = 3477.2)", size=12, fill=CORAL, weight="600")
    c.text(256, 380, "(Tested knot candidates land at 2391 to 5854: −31% to +68%)", size=12, fill=MUTED)

    c.rect(496, 80, 428, 338, fill=PANEL)
    c.text(710, 108, "Neutrino Wave Mixing (Zero Free Knobs)", size=15, fill=GREEN, weight="600")
    c.text(710, 128, "sin²θ₁₃ = ½ (q₀ − 1/q₀)² = 0.02185", size=13, fill=GOLD, weight="600")
    bars = [
        ("Reactor angle sin²θ₁₃", mp.mpf("0.02185"), mp.mpf("0.0220"), mp.mpf("0.03"), "0.02185 vs 0.0220 (−0.67%)"),
        ("Solar angle sin²θ₁₂", mp.mpf("0.2977"), mp.mpf("0.307"), mp.mpf("0.60"), "0.298 vs 0.307 (−3.0%)"),
        ("Atmospheric sin²θ₂₃", mp.mpf("0.4888"), mp.mpf("0.546"), mp.mpf("0.60"), "0.489 vs 0.546 (−10.5%)"),
    ]
    for i, (name, mod, exp, scale, note) in enumerate(bars):
        by = 158 + i * 82
        c.text(520, by, name, size=13, fill=TEXT, anchor="start", weight="600")
        c.text(900, by, note, size=12, fill=MUTED, anchor="end")
        w_mod = 360 * (mod / scale)
        w_exp = 360 * (exp / scale)
        c.rect(520, by + 10, w_mod, 16, fill=CYAN, stroke="none", rx=4)
        c.rect(520, by + 30, w_exp, 16, fill=GREEN, stroke="none", rx=4)
    c.rect(540, 392, 14, 10, fill=CYAN, stroke="none", rx=2)
    c.text(560, 401, "Model", size=12, fill=CYAN, anchor="start")
    c.rect(630, 392, 14, 10, fill=GREEN, stroke="none", rx=2)
    c.text(650, 401, "Measured (PDG)", size=12, fill=GREEN, anchor="start")
    c.save("sec05-generations-and-pmns.svg")


def build_sec06_beta_decay_nine_strand():
    c = SvgCanvas(960, 460, "Nine-Strand Neutron Decay and Energy Release")
    c.header(
        "Equation (8a): Neutron Decay Requires All Nine Participating Strands",
        "Treating the neutron alone misses half the energy (0.33 MeV); coupling the 6 outgoing lepton strands gives 0.764 MeV",
    )
    c.rect(36, 80, 500, 348, fill=PANEL)
    c.text(286, 108, "6 Outgoing Lepton Strands + 3 Nucleon Strands", size=15, fill=TEXT, weight="600")
    lxs = [78 + i * 36 for i in range(6)]
    qxs = [342 + i * 48 for i in range(3)]
    c.rect(64, 126, 208, 28, fill=PANEL_ALT, stroke=CYAN, rx=5)
    c.text(168, 145, "Electron + antineutrino + loop", size=12, fill=CYAN, weight="600")
    c.rect(324, 126, 134, 28, fill=PANEL_ALT, stroke=AMBER, rx=5)
    c.text(391, 145, "Neutron → Proton", size=12, fill=AMBER, weight="600")

    for i in range(5):
        c.line(lxs[i], 164, lxs[i], 344, stroke=CYAN, sw=3, opacity=mp.mpf("0.75"))
    for j in (1, 2):
        c.line(qxs[j], 164, qxs[j], 344, stroke=AMBER, sw=4)
    c.line(lxs[5], 164, lxs[5], 218, stroke=CYAN, sw=4)
    c.line(qxs[0], 164, qxs[0], 218, stroke=AMBER, sw=4)
    c.crossing_vertical(lxs[5], qxs[0], 218, 290, False, CYAN, AMBER, sw=5)
    c.line(lxs[5], 290, lxs[5], 344, stroke=AMBER, sw=4)
    c.line(qxs[0], 290, qxs[0], 344, stroke=CYAN, sw=4)
    c.circle((lxs[5] + qxs[0]) / 2, 254, 22, fill="none", stroke=GOLD, sw=2, dash="4 3")
    c.text(286, 376, "Only the under-crossing hands charge from quark to electron;", size=12, fill=GOLD, weight="600")
    c.text(286, 398, "taking the logarithm of loop ratios cancels bystander strands.", size=12, fill=MUTED)

    c.rect(556, 80, 368, 348, fill=PANEL)
    c.text(740, 108, "Decay Energy Q_β Comparison", size=15, fill=TEXT, weight="600")
    rows = [
        ("3-strand neutron alone", mp.mpf("0.33"), "0.33 MeV (−58%)", CORAL),
        ("9-strand coupled interaction", mp.mpf("0.764"), "0.764 MeV (−2.37%)", CYAN),
        ("Measured in laboratory", mp.mpf("0.782"), "0.7823 MeV", GREEN),
    ]
    for idx, (lab, val, tag, col) in enumerate(rows):
        ry = 148 + idx * 82
        c.text(580, ry, lab, size=13, fill=TEXT, anchor="start", weight="600")
        c.text(900, ry, tag, size=13, fill=col, anchor="end", weight="600")
        w = 310 * (val / mp.mpf("0.85"))
        c.rect(580, ry + 12, 310, 22, fill=PANEL_ALT, stroke=BORDER, rx=5)
        c.rect(580, ry + 12, w, 22, fill=col, stroke="none", rx=5)
    c.text(740, 396, "Keeping the 0.33 MeV miss unpatched revealed", size=12, fill=MUTED)
    c.text(740, 414, "that all 9 strands must be included together.", size=12, fill=GOLD)
    c.save("sec06-beta-decay-nine-strand.svg")


def build_sec06_proton_neutron_em():
    c = SvgCanvas(960, 440, "Proton vs Neutron Electric Energy Without Pion Input")
    c.header(
        "Equation (8b): Electric Energy Inside the Proton vs. Neutron (No Pion Needed)",
        "Quark-pair charges cancel to zero in the proton (uud) and add to −1/3 in the neutron (udd)",
    )
    c.rect(40, 82, 420, 260, fill=PANEL)
    c.text(250, 110, "Proton (u u d) — Total Charge +1", size=15, fill=CYAN, weight="600")
    pts_p = [(250, 152, "u (+2/3)", CYAN), (182, 262, "u (+2/3)", CYAN), (318, 262, "d (−1/3)", AMBER)]
    c.line(250, 152, 182, 262, stroke=CORAL, sw=3)
    c.line(250, 152, 318, 262, stroke=GREEN, sw=3)
    c.line(182, 262, 318, 262, stroke=GREEN, sw=3)
    for x, y, lab, col in pts_p:
        c.circle(x, y, 28, fill=PANEL_ALT, stroke=col, sw=3)
        c.text(x, y + 5, lab, size=11, fill=TEXT, weight="600")
    c.text(250, 320, "Pair products: (+4/9) + (−2/9) + (−2/9) = 0", size=13, fill=GREEN, weight="600")

    c.rect(500, 82, 420, 260, fill=PANEL)
    c.text(710, 110, "Neutron (u d d) — Total Charge 0", size=15, fill=AMBER, weight="600")
    pts_n = [(710, 152, "u (+2/3)", CYAN), (642, 262, "d (−1/3)", AMBER), (778, 262, "d (−1/3)", AMBER)]
    c.line(710, 152, 642, 262, stroke=GREEN, sw=3)
    c.line(710, 152, 778, 262, stroke=GREEN, sw=3)
    c.line(642, 262, 778, 262, stroke=CORAL, sw=3)
    for x, y, lab, col in pts_n:
        c.circle(x, y, 28, fill=PANEL_ALT, stroke=col, sw=3)
        c.text(x, y + 5, lab, size=11, fill=TEXT, weight="600")
    c.text(710, 320, "Pair products: (−2/9) + (−2/9) + (+1/9) = −1/3", size=13, fill=GOLD, weight="600")

    c.rect(40, 358, 880, 62, fill=PANEL_ALT, stroke=GOLD, sw=1)
    c.text(
        480,
        384,
        "Electric self-energy difference:   ΔE_EM(p − n) = α × m_proton × (1/9) = 0.761 MeV",
        size=14,
        fill=TEXT,
        weight="600",
    )
    c.text(
        480,
        406,
        "Sits inside the observed [0.76, 1.04] MeV range using (mₑ, q₀) alone — the pion input m_π drops out.",
        size=12,
        fill=GREEN,
    )
    c.save("sec06-proton-neutron-em.svg")


def build_sec07_hidden_colour_deuteron():
    c = SvgCanvas(960, 460, "Shared Quark Colour Pairings and Nuclear Binding")
    c.header(
        "Sharing Colour Strands Between Neighboring Protons and Neutrons",
        "Re-pairing 6 quarks binds heavy hydrogen at 2.265 MeV (+1.8%), while helium-4 still misses half its binding",
    )
    c.rect(36, 80, 440, 348, fill=PANEL)
    c.text(256, 108, "Ways Quarks Can Form a Balanced White Group", size=15, fill=CYAN, weight="600")
    counts = [
        ("3 quarks (1 proton/neutron)", "1 way", "No extra cross-nucleon pairings", 28, MUTED),
        ("6 quarks (²H heavy hydrogen)", "5 ways", "4 shared cross-nucleon pairings", 95, CYAN),
        ("9 quarks (³H / ³He)", "42 ways", "41 shared cross-nucleon pairings", 195, GOLD),
        ("12 quarks (⁴He helium core)", "462 ways", "461 shared cross-nucleon pairings", 340, GREEN),
    ]
    for i, (lab, ways, sub, bw, col) in enumerate(counts):
        ry = 136 + i * 70
        c.text(60, ry, f"{lab}  —  {ways}", size=13, fill=TEXT, anchor="start", weight="600")
        c.rect(60, ry + 10, bw, 18, fill=col, stroke="none", rx=4)
        c.text(60, ry + 43, sub, size=11, fill=MUTED, anchor="start")

    c.rect(496, 80, 428, 348, fill=PANEL)
    c.text(710, 108, "Nuclear Binding Energy: Model vs. Lab", size=15, fill=TEXT, weight="600")
    c.rect(520, 132, 380, 112, fill=PANEL_ALT, stroke=GREEN, sw=2)
    c.text(710, 156, "Deuteron ²H (1 Proton + 1 Neutron)", size=14, fill=GREEN, weight="600")
    c.text(710, 182, "6-quark shared-colour model:  2.265 MeV", size=13, fill=TEXT, weight="600")
    c.text(710, 204, "Measured in laboratory:       2.225 MeV  (+1.81%)", size=13, fill=GREEN)
    c.text(710, 226, "(Older unshared formula gave 2.86 MeV, +29%)", size=11, fill=MUTED)

    c.rect(520, 262, 380, 142, fill=PANEL_ALT, stroke=CORAL, sw=2)
    c.text(710, 286, "Helium-4 ⁴He (2 Protons + 2 Neutrons — Unsolved)", size=14, fill=CORAL, weight="600")
    c.text(710, 312, "Unshared baseline formula:   8.77 MeV  (−69%)", size=12, fill=MUTED)
    c.text(710, 334, "12-quark shared colour only: 14.49 MeV (−49%)", size=13, fill=GOLD, weight="600")
    c.text(710, 356, "Measured in laboratory:      28.30 MeV", size=13, fill=GREEN, weight="600")
    c.text(710, 384, "Missing: 4-way spin & proton/neutron swap symmetry", size=11, fill=CORAL)
    c.save("sec07-hidden-colour-deuteron.svg")


def build_sec07_nuclear_chambers_hoyle():
    c = SvgCanvas(960, 460, "The 73 Nuclear Stability Regions, Mass-5 Breakup, and Stellar Carbon")
    c.header(
        "Equation (9a): Out of 73 Possible Nuclear Worlds, the Model Lands in Ours",
        "Grouping rules automatically break mass-5 apart (⁵He → ⁴He + n) and fuse 3 heliums into carbon-12",
    )
    c.rect(36, 80, 434, 348, fill=PANEL)
    c.text(253, 108, "Map of the 73 Possible Grouping Regions", size=15, fill=GOLD, weight="600")
    cx, cy = 253, 256
    rays = 16
    for k in range(rays):
        a1 = 2 * mp.pi * k / rays
        a2 = 2 * mp.pi * (k + 1) / rays
        for r1, r2 in [(58, 98), (98, 132)]:
            pts = [
                (cx + r1 * mp.cos(a1), cy + r1 * mp.sin(a1)),
                (cx + r2 * mp.cos(a1), cy + r2 * mp.sin(a1)),
                (cx + r2 * mp.cos(a2), cy + r2 * mp.sin(a2)),
                (cx + r1 * mp.cos(a2), cy + r1 * mp.sin(a2)),
            ]
            c.polyline(pts, stroke=BORDER, sw=1, fill=PANEL_ALT, close=True)
    phys = []
    for k in range(5):
        ang = -mp.pi / 2 + 2 * mp.pi * k / 5
        phys.append((cx + 58 * mp.cos(ang), cy + 58 * mp.sin(ang)))
    c.polyline(phys, stroke=GREEN, sw=3, fill="#064e3b", close=True)
    c.circle(cx - 10, cy + 4, 5, fill=GOLD, stroke=BG, sw=1)
    c.circle(cx + 12, cy - 6, 5, fill=CYAN, stroke=BG, sw=1)
    c.text(cx, cy + 24, "Region 1 of 73", size=12, fill=GREEN, weight="600")
    c.text(253, 408, "Both model q₀ (cyan) & lab nuclei (gold) sit in this region", size=12, fill=TEXT)

    c.rect(490, 80, 434, 348, fill=PANEL)
    c.text(707, 108, "What Landing in This Region Predicts", size=15, fill=TEXT, weight="600")
    c.rect(514, 130, 386, 84, fill=PANEL_ALT, stroke=CYAN, sw=1)
    c.text(707, 154, "1. Why No Stable Mass-5 Atom Exists", size=13, fill=CYAN, weight="600")
    c.text(707, 178, "2 protons + 3 neutrons (⁵He)  ──►  ⁴He + loose neutron", size=13, fill=TEXT, weight="600")
    c.text(707, 200, "Whole-number grouping leaves one neutron unbound", size=11, fill=MUTED)

    c.rect(514, 226, 386, 96, fill=PANEL_ALT, stroke=GOLD, sw=1)
    c.text(707, 250, "2. How Stars Forge Carbon-12", size=13, fill=GOLD, weight="600")
    c.text(707, 274, "⁸Be  ──►  2 helium-4  (splits apart in 10⁻¹⁶ s)", size=12, fill=CORAL, weight="600")
    c.text(707, 296, "3 helium-4  ──►  ¹²C  (three-way fusion locks shut)", size=13, fill=GREEN, weight="600")

    c.rect(514, 334, 386, 74, fill=PANEL_ALT, stroke=VIOLET, sw=1)
    c.text(707, 358, "3. Full Nuclear Shell Totals", size=13, fill=VIOLET, weight="600")
    c.text(707, 384, "Closed shells at:  2,  8,  20,  28,  50,  82,  126", size=13, fill=TEXT, weight="600")
    c.save("sec07-nuclear-chambers-hoyle.svg")


def build_sec07_po210_alpha_tunneling():
    c = SvgCanvas(960, 450, "Heavy-Atom Alpha Tunneling and Polonium-210 Shell Drop")
    c.header(
        "Equation (9b): Quantum Barrier Tunneling & Polonium-210 (126 Neutrons)",
        "Tunneling outside the nucleus requires q → 1 in empty space; shell counting gives 1/20 = 0.050 vs. 0.055",
    )
    c.rect(36, 80, 540, 340, fill=PANEL)
    c.text(306, 108, "Tunneling Through the Electric Repulsion Hill", size=14, fill=CYAN, weight="600")
    ox, oy = 84, 368
    c.line(ox, oy, 544, oy, stroke=MUTED, sw=2, marker_end="arrow-muted")
    c.line(ox, oy, ox, 134, stroke=MUTED, sw=2, marker_end="arrow-muted")
    c.text(538, 390, "Distance r (fm)", size=11, fill=MUTED, anchor="end")
    c.text(94, 144, "Energy", size=11, fill=MUTED, anchor="start")
    rtouch = 176
    c.line(ox, 336, rtouch, 336, stroke=GREEN, sw=3)
    c.line(rtouch, 336, rtouch, 158, stroke=GOLD, sw=3)
    coul = []
    for k in range(121):
        rx = rtouch + mp.mpf(k) * mp.mpf("2.9")
        vy = oy - 210 * (mp.mpf(rtouch - ox) / mp.mpf(rx - ox))
        coul.append((rx, vy))
    c.polyline(coul, stroke=GOLD, sw=3)
    qy = 286
    rturn = ox + 210 * mp.mpf(rtouch - ox) / mp.mpf(oy - qy)
    c.line(ox, qy, 530, qy, stroke=CYAN, sw=2, dash="5 4")
    c.text(130, qy - 10, "5.41 MeV", size=11, fill=CYAN, weight="600")
    wave = []
    for k in range(160):
        wx = rtouch + mp.mpf(k) * mp.mpf("2.15")
        if wx <= rturn:
            amp = 22 * mp.exp(-mp.mpf("2.4") * (wx - rtouch) / (rturn - rtouch))
            wy = qy - amp * mp.sin(mp.mpf("0.18") * (wx - rtouch))
        else:
            wy = qy - 5 * mp.sin(mp.mpf("0.32") * (wx - rturn))
        wave.append((wx, wy))
    c.polyline(wave, stroke=CORAL, sw=2)
    c.text(306, 404, "Confirms q → 1 in empty space (keeping core q₀ outside misses ²³⁸U by 2600×)", size=11, fill=GREEN)

    c.rect(596, 80, 328, 340, fill=PANEL)
    c.text(760, 108, "Full 126-Neutron Shell (²¹⁰Po)", size=15, fill=VIOLET, weight="600")
    c.text(760, 130, "Counting slots to assemble a helium-4 cluster", size=12, fill=MUTED)
    c.rect(620, 152, 280, 106, fill=PANEL_ALT, stroke=VIOLET, sw=2)
    c.text(760, 176, "Proton shell slots:   10", size=12, fill=TEXT)
    c.text(760, 198, "Neutron hole slots:   2", size=12, fill=TEXT)
    c.text(760, 232, "Chance = 1 / (10 × 2) = 0.0500", size=14, fill=GOLD, weight="600")
    c.rect(620, 276, 280, 120, fill=PANEL_ALT, stroke=GREEN, sw=1)
    c.text(760, 302, "Measured chance:   0.0553", size=13, fill=GREEN, weight="600")
    c.text(760, 328, "Model half-life:  153 days", size=13, fill=TEXT)
    c.text(760, 350, "Measured:         138.4 days", size=13, fill=GREEN)
    c.text(760, 378, "(0.3 MeV error in energy shifts life by 1000×)", size=11, fill=CORAL)
    c.save("sec07-po210-alpha-tunneling.svg")


def build_sec08_five_layer_tower():
    c = SvgCanvas(960, 480, "Five Layers of Matter Without Refitted Constants")
    c.header(
        "Equation (10): Five Layers of Matter & Why Chemistry Never Transmutes Nuclei",
        "Whenever the tug from the layer above is much smaller than the binding gap below (η < 1), lower units stay intact",
    )
    layers = [
        ("Layer 4: Molecules & Chemical Reactions", "Chemical bonds (~4.5 eV) vs. inner carbon shell (442 eV)", "η₃ = 1.0 × 10⁻²", GREEN),
        ("Layer 3: Neutral Atoms & Electron Shells", "Atomic electron energy (13.6 eV) vs. nuclear bind (7.68 MeV)", "η₂ = 1.77 × 10⁻⁶", GOLD),
        ("Layer 2: Atomic Nuclei (Protons & Neutrons)", "Nuclear bind (7.68 MeV) vs. proton rest energy (938 MeV)", "η₁ = 8.2 × 10⁻³", CYAN),
        ("Layer 1: Protons, Neutrons & Pions", "Electric tug (α mₚ) vs. proton rest energy (938 MeV)", "η₀ = 7.3 × 10⁻³", VIOLET),
        ("Layer 0: Braided Strands at q₀ > 1", "Elementary over/under strand crossings", "Base Layer", CORAL),
    ]
    for idx, (title, desc, eta, col) in enumerate(layers):
        ry = 82 + idx * 74
        c.rect(44, ry, 600, 62, fill=PANEL, stroke=col, sw=2)
        c.text(64, ry + 26, title, size=14, fill=col, anchor="start", weight="600")
        c.text(64, ry + 47, desc, size=12, fill=MUTED, anchor="start")
        c.rect(476, ry + 14, 152, 34, fill=PANEL_ALT, stroke=col, sw=1, rx=6)
        c.text(552, ry + 36, eta, size=13, fill=TEXT, weight="600")
        if idx < 4:
            c.line(344, ry + 74, 344, ry + 62, stroke=col, sw=2, marker_end="arrow-muted")

    c.rect(666, 82, 254, 358, fill=PANEL)
    c.text(793, 112, "Why Chemistry Is Safe", size=15, fill=GOLD, weight="600")
    c.text(793, 138, "η₂ = 1.77 × 10⁻⁶", size=16, fill=GREEN, weight="600")
    c.text(793, 162, "A nearly million-to-one gap", size=12, fill=TEXT)
    c.text(793, 182, "locks nuclei solid during", size=12, fill=MUTED)
    c.text(793, 202, "every chemical reaction.", size=12, fill=MUTED)

    c.line(690, 228, 896, 228, stroke=BORDER, sw=1)

    c.text(793, 258, "Crushing the Lock (η₂ → 1)", size=15, fill=CORAL, weight="600")
    c.text(793, 284, "Electron energy > 1.293 MeV", size=13, fill=CORAL, weight="600")
    c.text(793, 310, "Critical density:", size=12, fill=MUTED)
    c.text(793, 330, "7.37 × 10³⁰ electrons/cm³", size=12, fill=TEXT, weight="600")
    c.text(793, 358, "Forces p + e⁻ → n + νₑ", size=12, fill=CYAN)
    c.text(793, 380, "inside white dwarfs &", size=12, fill=MUTED)
    c.text(793, 400, "neutron-star crusts.", size=12, fill=MUTED)
    c.save("sec08-five-layer-tower.svg")


def build_sec08_horizon_punctures():
    c = SvgCanvas(960, 440, "Black-Hole Horizon Strand Punctures and Unsolved Area Unit")
    c.header(
        "Equation (11): Strands Piercing a Black-Hole Horizon & the Unsolved Area Unit",
        "Counting strand punctures sets entropy per puncture, while the absolute area unit a₀ is still unproved",
    )
    c.rect(40, 80, 520, 326, fill=PANEL)
    c.text(300, 108, "Black-Hole Horizon Pierced by Braided Strands", size=15, fill=CYAN, weight="600")
    c.rect(62, 130, 196, 246, fill="#090d1a", stroke=BORDER, rx=8)
    c.text(160, 158, "Inside Horizon (Hidden)", size=12, fill=MUTED, weight="600")
    c.text(160, 352, "Exact particle identities blocked", size=11, fill=SLATE)
    c.path("M 268 128 Q 312 253 268 378", stroke=GOLD, sw=4)
    c.text(306, 148, "Horizon", size=12, fill=GOLD, weight="600")
    spins = [("spin 1/2", 182, CYAN), ("spin 1", 232, AMBER), ("spin 1/2", 282, CYAN), ("spin 3/2", 332, VIOLET)]
    for lab, py, col in spins:
        c.line(120, py, 286, py, stroke=col, sw=3, dash="5 4")
        c.circle(286, py, 7, fill=col, stroke=BG, sw=2)
        c.line(296, py, 430, py, stroke=GREEN, sw=2, marker_end="arrow-green")
        c.text(485, py + 4, f"{lab} puncture", size=12, fill=col)

    c.rect(580, 80, 340, 326, fill=PANEL)
    c.text(750, 108, "Proved vs. Unsolved at Horizon", size=15, fill=TEXT, weight="600")
    c.rect(604, 130, 292, 114, fill=PANEL_ALT, stroke=GREEN, sw=1)
    c.text(750, 154, "State-Counting Balance (Proved)", size=13, fill=GREEN, weight="600")
    c.text(750, 178, "Unique balance point Z₁(s_⋆) = 1", size=12, fill=TEXT)
    c.text(750, 200, "determines entropy per puncture", size=12, fill=MUTED)
    c.text(750, 222, "and closed loops balance total flux.", size=12, fill=MUTED)

    c.rect(604, 262, 292, 122, fill=PANEL_ALT, stroke=CORAL, sw=2)
    c.text(750, 286, "Unsolved Gravitational Step", size=13, fill=CORAL, weight="600")
    c.text(750, 310, "Converting puncture count to area", size=12, fill=TEXT)
    c.text(750, 332, "currently matches S = A / 4ℓ_P² by hand;", size=12, fill=MUTED)
    c.text(750, 354, "deriving the area unit a₀ from", size=12, fill=CORAL, weight="600")
    c.text(750, 372, "first principles is not yet done.", size=11, fill=CORAL)
    c.save("sec08-horizon-punctures.svg")


def build_sec09_unified_comparison_chart():
    c = SvgCanvas(960, 520, "Unified Comparison of Model Numbers Against Laboratory Measurements")
    c.header(
        "The Scoreboard: How Close Model Numbers Come to Measurement (Log Scale)",
        "Computed from three measured inputs (mₑ, q₀ from mₚ/mₑ, and m_π) with zero curve-fitting",
    )
    c.rect(36, 76, 888, 412, fill=PANEL)
    x_min, x_max = mp.mpf(300), mp.mpf(880)
    ticks = [
        (-10, "0.1 ppb"),
        (-8, "10 ppb"),
        (-6, "1 ppm"),
        (-4, "0.01%"),
        (-2, "1%"),
        (0, "100%"),
    ]
    for lg, lab in ticks:
        tx = x_min + (x_max - x_min) * (mp.mpf(lg + 10) / 10)
        c.line(tx, 108, tx, 452, stroke=BORDER, sw=1, dash="3 3")
        c.text(tx, 98, lab, size=11, fill=MUTED)

    items = [
        ("Strength of light 1/α (conditional)", mp.mpf("3.7e-10"), "0.37 ppb", GREEN),
        ("Kaon / pion mass ratio (series)", mp.mpf("5.1e-8"), "51 ppb", GREEN),
        ("Muon / electron mass ratio", mp.mpf("2.11e-7"), "211 ppb (9.5σ)", GOLD),
        ("Higgs boson mass m_H", mp.mpf("2.4e-4"), "+0.024%", GREEN),
        ("Strong force α_s at Z pole", mp.mpf("4.1e-3"), "+0.41%", GREEN),
        ("Reactor neutrino angle sin²θ₁₃", mp.mpf("6.7e-3"), "−0.67%", GREEN),
        ("Deuteron ²H (6-quark shared colour)", mp.mpf("1.81e-2"), "+1.81%", CYAN),
        ("Neutron decay Q_β (9-strand coupled)", mp.mpf("2.37e-2"), "−2.37%", CYAN),
        ("²¹⁰Po α-cluster chance (N = 126)", mp.mpf("9.6e-2"), "0.050 vs 0.055", CYAN),
        ("Neutron–proton split (3-strand alone)", mp.mpf("0.35"), "−35%", CORAL),
        ("Weak angle sin²θ_W (short 4-step run)", mp.mpf("0.479"), "+48%", CORAL),
        ("Neutron decay Q_β (3-strand alone)", mp.mpf("0.58"), "−58%", CORAL),
        ("Helium-4 ⁴He binding (unshared / 12q)", mp.mpf("0.69"), "−69% / −49%", CORAL),
    ]
    for idx, (label, err, note, col) in enumerate(items):
        ry = 122 + idx * 26
        lg = mp.log10(err)
        bx = x_min + (x_max - x_min) * ((lg + 10) / 10)
        c.text(290, ry + 5, label, size=12, fill=TEXT, anchor="end")
        c.line(x_min, ry, bx, ry, stroke=col, sw=6)
        c.circle(bx, ry, 5, fill=col, stroke=BG, sw=1)
        c.text(min(bx + 10, mp.mpf(820)), ry + 4, note, size=11, fill=col, anchor="start", weight="600")
    c.text(480, 474, "Green/Cyan: < 10% difference   |   Gold: 211 ppb (9.5σ tension)   |   Coral: large unsolved gaps", size=12, fill=MUTED)
    c.save("sec09-unified-comparison-chart.svg")


def build_sec09_unsolved_questions_map():
    c = SvgCanvas(960, 460, "Six Unsolved Questions and Formal Checking")
    c.header(
        "Six Unsolved Questions Where the Model Can Succeed or Fail",
        "Proved theorems are machine-checked in Lean 4; numerical checks use 50–80 digits with zero curve-fitting",
    )
    cards = [
        ("1. Why Three Matter Families?", "Prove why waves on the 4-holed surface pick the 3-member slice rather than 4 or 2.", CORAL),
        ("2. Tau Mass & Quark Mixing", "Find a parameter-free braid for the heavy tau (m_τ / mₑ = 3477.2) and quark mixing.", CORAL),
        ("3. Helium-4 Binding Strength", "Combine 12-quark colour sharing with spin-and-proton/neutron swap symmetry.", CORAL),
        ("4. The 211 ppb Muon–Proton Split", "Close the tiny q₀ gap via joint radiative loops and prove the proton 1/q³ factor.", GOLD),
        ("5. Weak Angle Evolution & Loop Step", "Connect sin²θ_W = 3/8 to M_Z without tuned thresholds; complete the 1/α loop proof.", GOLD),
        ("6. Black-Hole Area Unit & Spin Sign", "Derive the horizon puncture area a₀ from scratch and prove electron exchange sign.", CORAL),
    ]
    for i, (title, body, col) in enumerate(cards):
        col_idx = i % 2
        row_idx = i // 2
        bx = 40 + col_idx * 450
        by = 82 + row_idx * 92
        c.rect(bx, by, 430, 78, fill=PANEL, stroke=col, sw=2)
        c.text(bx + 18, by + 28, title, size=14, fill=col, anchor="start", weight="600")
        c.text(bx + 18, by + 54, body, size=12, fill=TEXT, anchor="start")

    c.rect(40, 368, 880, 66, fill=PANEL_ALT, stroke=CYAN, sw=1)
    c.text(
        480,
        394,
        "How Claims Are Kept Honest:   Machine-Checked Proofs   +   80-Digit Arithmetic   +   Open CC BY 4.0 Code",
        size=13,
        fill=CYAN,
        weight="600",
    )
    c.text(
        480,
        418,
        "Unproved steps are labeled explicitly as conjectures so assumptions are never mistaken for proved results.",
        size=12,
        fill=MUTED,
    )
    c.save("sec09-unsolved-questions-map.svg")


def main():
    builders = [
        build_sec01_grid_to_braids,
        build_sec01_skein_relation,
        build_sec01_loop_quotient,
        build_sec02_model_vs_measurement,
        build_sec02_figure_eight_tetrahedra,
        build_sec03_photon_and_borromean,
        build_sec03_brings_surface_pentagons,
        build_sec04_torus_knots_alpha,
        build_sec04_electroweak_higgs_rg,
        build_sec05_unknot_neutrino_framing,
        build_sec05_generations_and_pmns,
        build_sec06_beta_decay_nine_strand,
        build_sec06_proton_neutron_em,
        build_sec07_hidden_colour_deuteron,
        build_sec07_nuclear_chambers_hoyle,
        build_sec07_po210_alpha_tunneling,
        build_sec08_five_layer_tower,
        build_sec08_horizon_punctures,
        build_sec09_unified_comparison_chart,
        build_sec09_unsolved_questions_map,
    ]
    for fn in builders:
        fn()
    print(f"Generated {len(builders)} SVG visual frames in {ASSETS_DIR}")


if __name__ == "__main__":
    main()
