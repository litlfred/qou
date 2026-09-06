#!/usr/bin/env python3
"""
Neumann–Zagier gluing data DERIVED from the braid word — Route E for A_ω, first rung.

Bean qou-n2cl (2026-09-06). The 2026-08-11 memo (Route E) asked whether the 3d-index of a knot
could be made internal by deriving the Neumann–Zagier (NZ) gluing data of an ideal triangulation
of S³∖K from the framework's own data, instead of importing it from SnapPy. This probe does that
for the figure-eight along the only chain the corpus can currently support:

  canonical 3-braid  (σ₁σ₂⁻¹)²                              [Hecke / braid data]
    → Stallings–Gabai fibre monodromy  φ = T_{γ₁} T_{γ₂}⁻¹     [one Dehn twist per crossing column]
    → φ = [[2,1],[1,1]] = R·L in SL₂(ℤ)                        [LR word, trace 3 = −Δ_{4₁} middle coeff]
    → Floyd–Hatcher layered (monodromy) triangulation          [one tetrahedron per letter]
    → NZ rows: edge equations + cusp (meridian, longitude)     [derived combinatorially here]

Nothing is imported from SnapPy. The derived data is CHECKED against four independent facts:
  (1) the gluing equations have the exact solution ζ₀ = ζ₁ = e^{iπ/3} (solved symbolically),
  (2) Vol = 2·Cl₂(π/3) = Vol(4₁) to 50 dps,
  (3) the cusp shape is 2√3·i (the figure-eight's cusp modulus), which also separates the knot
      complement V_{+φ} = m004 from its sister V_{−φ} = m003 (same word, same volume),
  (4) the A-polynomial obtained by eliminating the shapes equals the corpus's A_{4₁}
      = −M⁴ + L(1 − M² − 2M⁴ − M⁶ + M⁸) − L²M⁴ (2026-08-11 memo §2c),
plus the NZ adjoint-torsion |det J| = √3 that the corpus previously obtained from SnapPy rows
(borromean_nz_adjoint_torsion.py), and the Neumann–Zagier symplectic relations on the rows.
A second word (R²L, three tetrahedra) is run through the same code as a non-trivial test of the
general layering; its volume is reported and compared to the census value for m009/m010.

SCOPE, stated up front. The chain's first step (Stallings) needs a homogeneous braid whose closure
is fibred with once-punctured-torus fibre; among hyperbolic knots in S³ that is 4₁ alone. It does
NOT reach 5₂ (not fibred), so the cross-knot gate of the A_ω arc is untouched by this probe. The
route to 5₂ is Guéritaud's layered triangulation of two-bridge links from the Farey word of the
continued fraction — same machinery, different layering — and is beaned separately. What this
probe makes internal is the NZ DATA; the 3d-index and its q→0 Stokes/DT count are downstream
computations on that data and are not re-derived here.

Precision: all combinatorics exact (integers); shapes for 4₁ exact in ℚ(√−3) via sympy; volumes
and cusp shapes in mpmath at 50 dps. No float64 arithmetic, no fit, no q₀ (q0Anchor independent).

-- Ref: [manuscript] docs/audits/2026-08-11-aomega-internal-derivation-attack-options.md §3 Route E
-- Ref: library/arxiv-0808.2716v4 (Futer–Kalfagianni–Purcell, Cusp areas of Farey manifolds) §2.2,
--      the Floyd–Hatcher / monodromy triangulation and the R, L matrices used here.
-- Ref: library/arxiv-2109.00379v1 (twisted Neumann–Zagier matrices) for the NZ symplectic form.
"""
from __future__ import annotations

import os
import sys
from fractions import Fraction
from itertools import product as iproduct

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402

import sympy as sp  # noqa: E402
from mpmath import mp  # noqa: E402

set_compute_dps()
mp.dps = 50

# ─────────────────────────────────────────────────────────────────────────────
# 0. Stallings / Gabai: fibre monodromy of a homogeneous 3-braid closure
# ─────────────────────────────────────────────────────────────────────────────
R = sp.Matrix([[1, 1], [0, 1]])   # Dehn twist T_{γ₁} on H₁(F) with γ₁·γ₂ = +1
L = sp.Matrix([[1, 0], [1, 1]])   # = T_{γ₂}⁻¹


def stallings_monodromy(word: list[tuple[int, int]]) -> sp.Matrix:
    """Monodromy on H₁ of the fibre of a homogeneous 3-braid closure.

    `word` is a list of (generator, sign) with generator ∈ {1, 2}. Homogeneity (each generator
    with one sign throughout) is asserted; then the fibre is the Murasugi sum of the two column
    pieces (each an annulus whose monodromy is a Dehn twist with the column's sign), and the total
    monodromy is the product of the two twists (Stallings 1978, Gabai 1983). The two column cores
    meet once, so T_{γ₁} = R and T_{γ₂} = L⁻¹ in the basis (γ₁, γ₂)."""
    signs = {}
    for g, s in word:
        assert s in (1, -1)
        if g in signs:
            assert signs[g] == s, "braid is not homogeneous — Stallings does not apply"
        signs[g] = s
    assert set(signs) == {1, 2}, "need both generators of B₃"
    T1 = R if signs[1] == 1 else R.inv()
    T2 = L.inv() if signs[2] == 1 else L
    return T1 * T2


# ─────────────────────────────────────────────────────────────────────────────
# 1. Floyd–Hatcher layering from an LR word (exact combinatorics)
# ─────────────────────────────────────────────────────────────────────────────
def _canon(v):
    """Slope = primitive integer vector up to sign; canonical representative."""
    x, y = int(v[0]), int(v[1])
    if x < 0 or (x == 0 and y < 0):
        x, y = -x, -y
    return (x, y)


def _det(a, b):
    return a[0] * b[1] - a[1] * b[0]


def _add(a, b, s=1):
    return (a[0] + s * b[0], a[1] + s * b[1])


def _neg(a):
    return (-a[0], -a[1])


class Tet:
    """One flip tetrahedron. Square P,Q,R,S counterclockwise in the fibre; sides a (PQ, SR) and
    b (PS, QR); bottom diagonal PR = a+b (removed slope); top diagonal QS = b−a (added slope).
    Vertex labels 0=P,1=Q,2=R,3=S. Class-O ordering (0,1,3,2) ⇒ shape types:
    a-sides {01,23}: z (type 0); b-sides {03,12}: z' (type 1); diagonals {02,13}: z'' (type 2)."""

    def __init__(self, idx, a, b):
        self.i = idx
        self.a, self.b = a, b
        self.pos = {0: (0, 0), 1: a, 2: _add(a, b), 3: b}
        self.O = (0, 1, 3, 2)  # class-O vertex ordering (see docstring)

    def etype(self, p, q):
        """shape type of edge {p,q}: 0 → z, 1 → z', 2 → z''."""
        o = self.O
        i, j = sorted((o.index(p), o.index(q)))
        return {(0, 1): 0, (2, 3): 0, (0, 2): 1, (1, 3): 1, (0, 3): 2, (1, 2): 2}[(i, j)]

    def faces(self):
        """(name, vertex-cycle) for the two bottom faces and two top faces, each as a
        counterclockwise vertex cycle in the fibre plane."""
        return {"bot": [(0, 1, 2), (0, 2, 3)], "top": [(0, 1, 3), (1, 2, 3)]}

    def cycle_vectors(self, cyc):
        return [_add(self.pos[cyc[(k + 1) % 3]], self.pos[cyc[k]], -1) for k in range(3)]


def layer(word: str):
    """Build the Floyd–Hatcher stack for an LR word. Returns (tets, closing_maps) where
    closing_maps are the two SL₂(ℤ) matrices ±M identifying τ_m with τ_0."""
    # Farey triangle state: entry edge (x, y), apex v. Start: x=(1,0), y=(0,1), v=(1,1).
    x, y, v = (1, 0), (0, 1), (1, 1)
    x0, y0, v0 = x, y, v
    tets = []
    for i, letter in enumerate(word):
        # Exit across (y, v) [letter R] or (x, v) [letter L]; the removed vertex is the one not on
        # the exit edge; the new apex is the other Farey neighbour of the exit edge.
        # State (x, y, v): entry edge (x, y) with x on the LEFT of the direction of travel and
        # y on the RIGHT, apex v. A right turn exits across (y, v) and pivots on y, which stays on
        # the right; a left turn exits across (x, v) and pivots on x. Consecutive equal letters
        # therefore fan around one vertex and alternating letters zigzag (each slope lives for
        # exactly three triangles) — the Farey-path semantics of Futer–Kalfagianni–Purcell §2.2.
        if letter == "R":
            removed, k1, k2 = x, y, v
            nxt = lambda new: (v, y, new)   # noqa: E731
        elif letter == "L":
            removed, k1, k2 = y, x, v
            nxt = lambda new: (x, v, new)   # noqa: E731
        else:
            raise ValueError(letter)
        # other neighbour of edge (k1,k2): the one of k1±k2 that is not ±removed
        cand = [_add(k1, k2), _add(k1, k2, -1)]
        new = next(c for c in cand if _canon(c) != _canon(removed))
        # orient the square: signs so that removed = a + b exactly, det(a,b) > 0
        found = None
        for sa, sb in iproduct((1, -1), (1, -1)):
            a = (sa * k1[0], sa * k1[1])
            b = (sb * k2[0], sb * k2[1])
            if _add(a, b) == removed:
                found = (a, b)
                break
        assert found is not None, "removed slope is not a Farey sum of the kept slopes"
        a, b = found
        if _det(a, b) < 0:
            a, b = b, a
        assert _canon(_add(b, a, -1)) == _canon(new)
        tets.append(Tet(i, a, b))
        x, y, v = nxt(new)
    # closing map M: τ_m = M τ_0, with M ∈ SL₂(ℤ) sending (x0,y0) ↦ (±x,±y) and v0 ↦ ±v
    maps = []
    for sx, sy in iproduct((1, -1), (1, -1)):
        B0 = sp.Matrix([[x0[0], y0[0]], [x0[1], y0[1]]])
        B1 = sp.Matrix([[sx * x[0], sy * y[0]], [sx * x[1], sy * y[1]]])
        M = B1 * B0.inv()
        if M.det() != 1 or any(e.q != 1 for e in M):
            continue
        Mv = M * sp.Matrix(v0)
        if _canon((int(Mv[0]), int(Mv[1]))) == _canon(v):
            maps.append(M)
    assert len(maps) == 2 and maps[0] == -maps[1]
    return tets, maps


def glue(tets, M):
    """Face gluings top(Δ_i) ↔ bot(Δ_{i+1}); the last via M. Returns dict:
    (i, face_cycle) → (j, face_cycle', vertex map as dict)."""
    m = len(tets)
    Mi = [[int(M[0, 0]), int(M[0, 1])], [int(M[1, 0]), int(M[1, 1])]]

    def apply(Mm, vec):
        return (Mm[0][0] * vec[0] + Mm[0][1] * vec[1], Mm[1][0] * vec[0] + Mm[1][1] * vec[1])

    gl = {}
    for i in range(m):
        j = (i + 1) % m
        for ft in tets[i].faces()["top"]:
            vt = tets[i].cycle_vectors(ft)
            if j == 0:  # top of the last layer lives in τ_m = M τ_0: pull back by M⁻¹
                Minv = [[Mi[1][1], -Mi[0][1]], [-Mi[1][0], Mi[0][0]]]
                vt = [apply(Minv, w) for w in vt]
            hit = None
            for fb in tets[j].faces()["bot"]:
                vb = tets[j].cycle_vectors(fb)
                for r in range(3):
                    if [vb[(k + r) % 3] for k in range(3)] == vt:
                        # vertex k of ft (between vt[k-1] and vt[k]) ↔ vertex (k+r) of fb
                        vmap = {ft[k]: fb[(k + r) % 3] for k in range(3)}
                        hit = (fb, vmap)
                        break
                if hit:
                    break
            assert hit is not None, "top face has no matching bottom face"
            fb, vmap = hit
            gl[(i, ft)] = (j, fb, vmap)
            gl[(j, fb)] = (i, ft, {q: p for p, q in vmap.items()})
    assert len(gl) == 4 * m
    return gl


# ─────────────────────────────────────────────────────────────────────────────
# 2. Edge classes, corner rows, cusp triangulation, holonomy rows
# ─────────────────────────────────────────────────────────────────────────────
TYPE_ROW = {0: ((1, 0), 1), 1: ((0, -1), 1), 2: ((-1, 1), -1)}   # z, 1/(1−z), (z−1)/z


class UF:
    def __init__(self):
        self.p = {}

    def find(self, x):
        self.p.setdefault(x, x)
        while self.p[x] != x:
            self.p[x] = self.p[self.p[x]]
            x = self.p[x]
        return x

    def union(self, x, y):
        self.p[self.find(x)] = self.find(y)


def edge_classes(tets, gl):
    uf = UF()
    for (i, f), (j, g, vmap) in gl.items():
        for p in f:
            for q in f:
                if p < q:
                    uf.union((i, frozenset((p, q))), (j, frozenset((vmap[p], vmap[q]))))
    classes = {}
    for t in tets:
        for p in range(4):
            for q in range(p + 1, 4):
                classes.setdefault(uf.find((t.i, frozenset((p, q)))), []).append((t.i, p, q))
    return list(classes.values())


def row_from_corners(corners, m):
    """corners: list of (tet index, type, exponent ±1) → rect row (a, b, sign)."""
    a, b = [0] * m, [0] * m
    sign = 1
    for i, ty, e in corners:
        (da, db), s = TYPE_ROW[ty]
        a[i] += e * da
        b[i] += e * db
        if s == -1 and e % 2:
            sign = -sign
    return (a, b, sign)


def edge_rows(tets, classes):
    rows = []
    for cl in classes:
        corners = [(i, tets[i].etype(p, q), 1) for (i, p, q) in cl]
        rows.append(row_from_corners(corners, len(tets)))
    return rows


def ccw_at(t: Tet, a):
    """Counterclockwise order of the other three vertices in the cusp triangle at vertex a."""
    o = t.O
    k = o.index(a)
    rot = {0: (o[1], o[2], o[3]), 1: (o[0], o[3], o[2]), 2: (o[3], o[0], o[1]), 3: (o[2], o[1], o[0])}
    return rot[k]


def cusp_neighbor(tets, gl, i, a, x, y):
    """Cross side {x,y} of cusp triangle (i,a): the face (a,x,y) of Δ_i. Returns (j, a', x', y')."""
    face = next(f for fl in tets[i].faces().values() for f in fl if set(f) == {a, x, y})
    j, g, vmap = gl[(i, face)]
    return j, vmap[a], vmap[x], vmap[y]


def cusp_vertices(tets, gl):
    """Union-find on corners (i, a, x): the ends of the edge classes."""
    uf = UF()
    for t in tets:
        for a in range(4):
            x, y, w = ccw_at(t, a)
            for (u, s) in ((x, y), (y, w), (w, x)):
                j, a2, u2, s2 = cusp_neighbor(tets, gl, t.i, a, u, s)
                uf.union((t.i, a, u), (j, a2, u2))
                uf.union((t.i, a, s), (j, a2, s2))
    verts = {}
    for t in tets:
        for a in range(4):
            for x in ccw_at(t, a):
                verts.setdefault(uf.find((t.i, a, x)), []).append((t.i, a, x))
    return list(verts.values()), uf


def corner_shape_type(tets, i, a, x):
    return tets[i].etype(a, x)


def develop(tets, gl, shapes):
    """Place every cusp triangle in ℂ by breadth-first gluing; returns positions
    {(i,a): {vertex: complex}} plus, for each dual edge crossed to an already-placed triangle,
    the affine discrepancy (holonomy). Shapes: list of mpc."""
    from collections import deque

    pos = {}
    hol = []  # (triangle key, existing placement, new placement) discrepancies
    start = (0, 0)
    t0 = tets[0]
    x, y, w = ccw_at(t0, 0)
    z = shapes[0] ** 0  # placeholder 1
    # place (0,0): x at 0, y at 1, w at corner shape at x
    c = corner_value(shapes[0], t0.etype(0, x))
    pos[start] = {x: mp.mpc(0), y: mp.mpc(1), w: c}
    dq = deque([start])
    while dq:
        i, a = dq.popleft()
        P = pos[(i, a)]
        x, y, w = ccw_at(tets[i], a)
        for (u, s) in ((x, y), (y, w), (w, x)):
            j, a2, u2, s2 = cusp_neighbor(tets, gl, i, a, u, s)
            # third vertex of the neighbour
            x2, y2, w2 = ccw_at(tets[j], a2)
            v2 = next(q for q in (x2, y2, w2) if q not in (u2, s2))
            # the neighbour is on the other side of side (u,s): its orientation is ccw too, so
            # traversing (s2, u2) is its ccw direction. Corner at s2 has shape c2 = (v2−s2)/(u2−s2).
            c2 = corner_value(shapes[j], tets[j].etype(a2, s2))
            # orientation check: in ccw (s2, u2, v2)? Determine via ccw order
            order = (x2, y2, w2)
            k = order.index(s2)
            if order[(k + 1) % 3] != u2:
                # then ccw is (u2, s2, v2) → corner at u2
                c2 = corner_value(shapes[j], tets[j].etype(a2, u2))
                base, tip = P[s], P[u]  # from u2's image: u2 sits at P[u], s2 at P[s]
                newpos = {u2: P[u], s2: P[s], v2: P[u] + (P[s] - P[u]) * c2}
            else:
                newpos = {s2: P[s], u2: P[u], v2: P[s] + (P[u] - P[s]) * c2}
            if (j, a2) in pos:
                hol.append(((j, a2), pos[(j, a2)], newpos))
            else:
                pos[(j, a2)] = newpos
                dq.append((j, a2))
    return pos, hol


def corner_value(z, ty):
    return {0: z, 1: 1 / (1 - z), 2: 1 - 1 / z}[ty]


def affine_from(P, Q):
    """Similarity mapping placement P to placement Q (dict vertex→complex): returns (d, t)
    with Q = d·P + t, using two vertices; the third is a consistency check."""
    ks = list(P)
    d = (Q[ks[1]] - Q[ks[0]]) / (P[ks[1]] - P[ks[0]])
    t = Q[ks[0]] - d * P[ks[0]]
    err = abs(Q[ks[2]] - (d * P[ks[2]] + t))
    return d, t, err


# ─────────────────────────────────────────────────────────────────────────────
# 3. Symbolic holonomy of closed dual paths (for the rect rows of μ and λ)
# ─────────────────────────────────────────────────────────────────────────────
def dual_graph(tets, gl):
    """Cusp triangles as nodes; edges = shared sides. Each directed crossing records the corner
    it cuts (vertex shared by entry and exit sides) — the holonomy of a path is the product over
    consecutive crossings of corner^{±1}."""
    nodes = [(t.i, a) for t in tets for a in range(4)]
    adj = {n: [] for n in nodes}
    for (i, a) in nodes:
        x, y, w = ccw_at(tets[i], a)
        for (u, s) in ((x, y), (y, w), (w, x)):
            j, a2, u2, s2 = cusp_neighbor(tets, gl, i, a, u, s)
            adj[(i, a)].append(((j, a2), (u, s), (u2, s2)))
    return nodes, adj


def side_monomial(t: Tet, a, p, q):
    """The oriented side vector (q − p) of the cusp triangle at vertex `a` of `t`, as a rect
    monomial (da, db, sign) in the tetrahedron's shape z, in units of the side (y − x) where
    (x, y, w) is the ccw order. With ζ the corner shape at x (type τ): y − x = 1, w − x = ζ,
    w − y = ζ − 1. In rect form (z^da (1−z)^db · sign):
        τ=0: ζ = z            → (1,0,+);   ζ−1 = −(1−z)     → (0,1,−)
        τ=1: ζ = 1/(1−z)      → (0,−1,+);  ζ−1 = z/(1−z)    → (1,−1,+)
        τ=2: ζ = (z−1)/z      → (−1,1,−);  ζ−1 = −1/z       → (−1,0,−)
    This mirrors develop() exactly, so a row built from these ratios evaluates to the developed
    derivative by construction."""
    x, y, w = ccw_at(t, a)
    tau = t.etype(a, x)
    ZETA = {0: (1, 0, 1), 1: (0, -1, 1), 2: (-1, 1, -1)}[tau]
    ZM1 = {0: (0, 1, -1), 1: (1, -1, 1), 2: (-1, 0, -1)}[tau]
    table = {(x, y): (0, 0, 1), (x, w): ZETA, (y, w): ZM1}
    if (p, q) in table:
        return table[(p, q)]
    da, db, s = table[(q, p)]
    return (da, db, -s)


def mono_div(m1, m2):
    return (m1[0] - m2[0], m1[1] - m2[1], m1[2] * m2[2])


def path_corners(tets, gl, path_sides):
    """path_sides: list of (i, a, (u, s)) — leave triangle (i,a) through side (u, s), oriented
    u → s. The frame carried along the path is the oriented side vector; inside a triangle the
    frame changes by the ratio (exit side)/(entry side), a rect monomial from side_monomial.
    Across a side the frame is unchanged (develop() places the glued side on the same segment).
    Returns per-step (tet index, (da, db, sign)) — a list of monomials, not corner exponents."""
    steps = []
    n = len(path_sides)
    for k in range(n):
        i, a, (u, s) = path_sides[k]
        ip, ap, (up, sp_) = path_sides[k - 1]
        j, a2, u2, s2 = cusp_neighbor(tets, gl, ip, ap, up, sp_)
        assert (j, a2) == (i, a)
        entry = side_monomial(tets[i], a, u2, s2)
        exit_ = side_monomial(tets[i], a, u, s)
        steps.append((i, mono_div(exit_, entry)))
    return steps


def nontrivial_cycles(erows, hrows):
    """Indices of dual cycles whose rect rows are ℚ-independent of the edge rows (a vertex
    link's row is an edge equation and carries no cusp information); greedy, so the returned
    list is also mutually independent modulo the edge span."""
    base = [list(r[0]) + list(r[1]) for r in erows]
    chosen = []
    for k, (row, _) in enumerate(hrows):
        trial = base + [list(row[0]) + list(row[1])]
        if sp.Matrix(trial).rank() > sp.Matrix(base).rank():
            base = trial
            chosen.append(k)
    return chosen


def holonomy_rows(tets, gl, shapes_exact, cycles):
    """For each closed dual cycle, the rect row (a, b, sign) of its holonomy derivative."""
    out = []
    m = len(tets)
    for cyc in cycles:
        steps = path_corners(tets, gl, cyc)
        a, b, sign = [0] * m, [0] * m, 1
        for i, (da, db, s) in steps:
            a[i] += da
            b[i] += db
            sign *= s
        out.append(((a, b, sign), steps))
    return out


def find_cycles(tets, gl):
    """Two independent closed dual cycles on the cusp torus via a spanning tree of the dual
    graph; returns list of cycles as path_sides lists, plus the tree."""
    nodes, adj = dual_graph(tets, gl)
    root = nodes[0]
    parent = {root: None}
    order = [root]
    from collections import deque
    dq = deque([root])
    tree_edges = set()
    while dq:
        n = dq.popleft()
        for (n2, side, side2) in adj[n]:
            if n2 not in parent:
                parent[n2] = (n, side, side2)
                tree_edges.add((n, frozenset(side)))
                tree_edges.add((n2, frozenset(side2)))
                dq.append(n2)
                order.append(n2)
    cycles = []
    seen = set()
    for n in nodes:
        for (n2, side, side2) in adj[n]:
            key = frozenset([(n, frozenset(side)), (n2, frozenset(side2))])
            if (n, frozenset(side)) in tree_edges or key in seen:
                continue
            seen.add(key)
            # cycle: root→…→n (tree), cross to n2, n2→…→root (tree reversed)
            def path_to_root(v):
                p = []
                while parent[v] is not None:
                    pv, s, s2 = parent[v]
                    p.append((pv, s, v, s2))
                    v = pv
                return p[::-1]  # root→v as list of (from, side, to, side_in_to)
            up = path_to_root(n)
            down = path_to_root(n2)
            steps = [(f, s) for (f, s, t_, s2) in up] + [(n, side)] + \
                    [(t_, s2) for (f, s, t_, s2) in reversed(down)]
            # 'down' reversed: we go from n2 back to root: leave t_ via the side s2 it was entered
            cyc = [(f[0], f[1], s) for (f, s) in steps]
            cycles.append(cyc)
    return cycles


# ─────────────────────────────────────────────────────────────────────────────
# 4. Geometry: solve, volume, cusp shape, A-polynomial, torsion, symplectic check
# ─────────────────────────────────────────────────────────────────────────────
def bloch_wigner(z):
    return mp.im(mp.polylog(2, z)) + mp.arg(1 - z) * mp.log(abs(z))


def rect_eval(row, shapes):
    a, b, s = row
    v = mp.mpc(1)
    for j, z in enumerate(shapes):
        v *= z ** a[j] * (1 - z) ** b[j]
    return v * s


def rect_expr(row, zs):
    a, b, s = row
    e = sp.Integer(s)
    for j, z in enumerate(zs):
        e *= z ** a[j] * (1 - z) ** b[j]
    return e


def nz_symplectic_check(rows, N):
    """Neumann–Zagier: for edge rows (a_i|b_i) and cusp rows, the form
    ω((a,b),(a',b')) = Σ_j (a_j b'_j − b_j a'_j) vanishes between any two edge rows, between an
    edge row and a cusp row, and equals ±2 between the meridian and longitude of one cusp
    (with the 'rect' normalisation Π z^a (1−z)^b, the (z, z'') basis). Returns the Gram table."""
    def om(r1, r2):
        return sum(r1[0][j] * r2[1][j] - r1[1][j] * r2[0][j] for j in range(N))
    n = len(rows)
    return [[om(rows[p], rows[q]) for q in range(n)] for p in range(n)]


def torsion_det(rows, N, shapes):
    w = [z / (1 - z) for z in shapes]
    def jrow(row):
        a, b, _ = row
        return [mp.mpf(a[j]) - mp.mpf(b[j]) * w[j] for j in range(N)]
    cand = [jrow(r) for r in rows]
    chosen = []
    for r in cand:
        trial = chosen + [r]
        Mx = mp.matrix(trial)
        # rank via SVD
        sv = mp.svd_r(Mx, compute_uv=False) if False else None
        # simple Gaussian elimination rank
        A = [row[:] for row in trial]
        rank = 0
        for col in range(N):
            piv = next((k for k in range(rank, len(A)) if abs(A[k][col]) > mp.mpf(10) ** -30), None)
            if piv is None:
                continue
            A[rank], A[piv] = A[piv], A[rank]
            for k in range(len(A)):
                if k != rank and abs(A[k][col]) > 0:
                    f = A[k][col] / A[rank][col]
                    A[k] = [A[k][c] - f * A[rank][c] for c in range(N)]
            rank += 1
        if rank > len(chosen):
            chosen.append(r)
        if len(chosen) == N:
            break
    return abs(mp.det(mp.matrix(chosen)))


def run_word(word, M, label):
    tets, _ = layer(word)
    gl = glue(tets, M)
    N = len(tets)
    classes = edge_classes(tets, gl)
    erows = edge_rows(tets, classes)
    cverts, _ = cusp_vertices(tets, gl)
    cycles = find_cycles(tets, gl)
    print(f"\n[{label}] word={word} closing M={M.tolist()} tr={M.trace()}")
    print(f"  tetrahedra {N}, edge classes {len(classes)}, cusp vertices {len(cverts)}, "
          f"dual cycles {len(cycles)}")
    for r in erows:
        print(f"  edge row a={r[0]} b={r[1]} sign={r[2]}")
    return tets, gl, N, classes, erows, cverts, cycles


def main() -> int:
    from qou_substrate.witness import WitnessBuilder

    wb = WitnessBuilder("nz-gluing-from-braid-monodromy", engine="python", _script_path=__file__)
    wb.set_description(
        "Neumann–Zagier gluing data of the figure-eight complement DERIVED from the canonical "
        "3-braid (σ₁σ₂⁻¹)² via Stallings monodromy → LR word → Floyd–Hatcher layering; checked "
        "against the exact shape e^{iπ/3}, Vol(4₁)=2Cl₂(π/3), cusp shape 2√3 i, the corpus "
        "A-polynomial, the NZ torsion √3 and the NZ symplectic relations. Bean qou-n2cl.")
    wb.set_content_block("conj:stokes-dt-bps-bridge")
    ok_all = True

    def check(name, cond, note=""):
        nonlocal ok_all
        ok_all &= bool(cond)
        print(f"  [{'PASS' if cond else 'FAIL'}] {name} {note}")
        wb.add_assertion(name, computed="1" if cond else "0", expected="1", tolerance="0.5",
                         source="nz_gluing_from_braid_monodromy_probe")

    # ── Step 0: braid → monodromy → word ───────────────────────────────────
    braid = [(1, 1), (2, -1), (1, 1), (2, -1)]        # (σ₁σ₂⁻¹)², closure = 4₁
    phi = stallings_monodromy(braid)
    print("Step 0: Stallings monodromy of (σ₁σ₂⁻¹)² =", phi.tolist(), "trace", phi.trace())
    t = sp.symbols("t")
    alex = sp.expand((t * sp.eye(2) - phi).det())
    print("        det(t − φ) =", alex, " (Alexander polynomial of 4₁: t² − 3t + 1)")
    check("stallings_monodromy_is_RL", phi == R * L, f"φ = {phi.tolist()} = R·L")
    check("alexander_poly_fourone", sp.expand(alex - (t**2 - 3 * t + 1)) == 0)
    trefoil = stallings_monodromy([(1, 1), (2, 1), (1, 1), (2, 1)])
    check("trefoil_control_trace_one", trefoil.trace() == 1,
          "σ₁σ₂σ₁σ₂ ↦ tr 1, Δ = t²−t+1 (control)")

    # ── Steps 1–3: layering for RL with closing +φ (knot) and −φ (sister) ──
    tets, maps = layer("RL")
    Mplus = next(Mm for Mm in maps if Mm.trace() > 0)
    Mminus = -Mplus
    check("closing_map_conjugate_to_phi", Mplus.trace() == 3 and Mplus.det() == 1,
          f"M = {Mplus.tolist()}")

    z0, z1 = sp.symbols("z0 z1")
    omega = sp.Rational(1, 2) + sp.sqrt(3) * sp.I / 2      # e^{iπ/3}
    results = {}
    for lab, Mm in (("V_{+φ} (knot complement, m004)", Mplus), ("V_{−φ} (sister, m003)", Mminus)):
        tets, gl, N, classes, erows, cverts, cycles = run_word("RL", Mm, lab)
        # exact check of edge rows at ω
        vals = [sp.simplify(rect_expr(r, [z0, z1]).subs({z0: omega, z1: omega})) for r in erows]
        results[lab] = dict(tets=tets, gl=gl, N=N, erows=erows, cycles=cycles, vals=vals,
                            cverts=cverts)
        print("  edge rows at ζ=ω:", vals)

    knot = results["V_{+φ} (knot complement, m004)"]
    sister = results["V_{−φ} (sister, m003)"]
    check("edge_rows_solved_by_omega_knot", all(v == 1 for v in knot["vals"]))
    check("edge_rows_solved_by_omega_sister", all(v == 1 for v in sister["vals"]))
    check("two_tetrahedra_two_edges", knot["N"] == 2 and len(knot["erows"]) == 2)

    # symbolic: the gluing variety of the knot triangulation, solved
    e_knot = sp.together(rect_expr(knot["erows"][0], [z0, z1]) - 1)
    num = sp.numer(e_knot)
    sols_diag = sp.solve(sp.Poly(num.subs(z1, z0), z0), z0)
    print("  edge equation:", sp.factor(num), "= 0")
    print("  diagonal solutions z0=z1:", sols_diag)
    check("omega_is_a_diagonal_solution", any(sp.simplify(s - omega) == 0 for s in sols_diag))

    # ── Volume, cusp shape (numeric, 50 dps) ───────────────────────────────
    w = mp.exp(1j * mp.pi / 3)
    vol = sum(bloch_wigner(w) for _ in range(2))
    vol_ref = 2 * mp.clsin(2, mp.pi / 3)
    print(f"  Vol = {mp.nstr(vol, 30)}  vs 2·Cl₂(π/3) = {mp.nstr(vol_ref, 30)}")
    check("volume_equals_two_cl2_pi_over_3", abs(vol - vol_ref) < mp.mpf(10) ** -40)

    def cusp_lattice(res):
        pos, hol = develop(res["tets"], res["gl"], [w, w])
        trans = []
        for (key, P, Q) in hol:
            d, tr_, err = affine_from(P, Q)
            assert err < mp.mpf(10) ** -35
            assert abs(d - 1) < mp.mpf(10) ** -35, f"derivative {d} ≠ 1: not complete"
            if abs(tr_) > mp.mpf(10) ** -30:
                trans.append(tr_)
        # lattice basis from translations: pick two shortest independent
        trans.sort(key=lambda c: abs(c))
        b1 = trans[0]
        b2 = next(c for c in trans if abs(mp.im(c / b1)) > mp.mpf(10) ** -20)
        # reduce b2 modulo b1 to |Re(b2/b1)| ≤ 1/2, Im>0
        r = b2 / b1
        if mp.im(r) < 0:
            r = -r
        r = r - mp.nint(mp.re(r))
        return r, trans

    tau_knot, _ = cusp_lattice(knot)
    tau_sis, _ = cusp_lattice(sister)
    print(f"  cusp modulus knot   = {mp.nstr(tau_knot, 25)}   (2√3 i = {mp.nstr(2*mp.sqrt(3), 25)} i)")
    print(f"  cusp modulus sister = {mp.nstr(tau_sis, 25)}")
    check("cusp_shape_knot_is_2sqrt3_i",
          abs(tau_knot - 2 * mp.sqrt(3) * 1j) < mp.mpf(10) ** -30)
    check("sister_cusp_shape_differs", abs(tau_sis - tau_knot) > mp.mpf(10) ** -10,
          "same word, same volume, different manifold")

    # ── Cusp rows: μ = shortest lattice vector, λ = the 2√3 i direction ──────
    # Symbolic rows for the two spanning-tree cycles, then integer-combine to (μ, λ) by matching
    # their developed translations.
    pos, hol = develop(knot["tets"], knot["gl"], [w, w])
    hrows = holonomy_rows(knot["tets"], knot["gl"], None, knot["cycles"])
    # translations of the dual cycles: develop along each cycle explicitly
    def cycle_translation(res, cyc):
        # place first triangle as in develop(), then walk the cycle
        tets_, gl_ = res["tets"], res["gl"]
        i0, a0, _ = cyc[0]
        x, y, wv = ccw_at(tets_[i0], a0)
        P = {x: mp.mpc(0), y: mp.mpc(1), wv: corner_value(w, tets_[i0].etype(a0, x))}
        start = dict(P)
        for (i, a, (u, s)) in cyc:
            j, a2, u2, s2 = cusp_neighbor(tets_, gl_, i, a, u, s)
            x2, y2, w2 = ccw_at(tets_[j], a2)
            v2 = next(q for q in (x2, y2, w2) if q not in (u2, s2))
            order = (x2, y2, w2)
            k = order.index(s2)
            if order[(k + 1) % 3] != u2:
                c2 = corner_value(w, tets_[j].etype(a2, u2))
                P = {u2: P[u], s2: P[s], v2: P[u] + (P[s] - P[u]) * c2}
            else:
                c2 = corner_value(w, tets_[j].etype(a2, s2))
                P = {s2: P[s], u2: P[u], v2: P[s] + (P[u] - P[s]) * c2}
        d, tr_, err = affine_from(start, P)
        return d, tr_

    cyc_tr = []
    for (row, corners), cyc in zip(hrows, knot["cycles"]):
        d, tr_ = cycle_translation(knot, cyc)
        val = rect_eval(row, [w, w])
        cyc_tr.append((row, tr_, d, val))
        print(f"  dual cycle: row a={row[0]} b={row[1]} sign={row[2]}  value(ω)={mp.nstr(val,8)} "
              f"derivative={mp.nstr(d,8)} translation={mp.nstr(tr_,12)}")
    check("dual_cycle_rows_evaluate_to_one_at_omega",
          all(abs(v - 1) < mp.mpf(10) ** -30 for (_, _, _, v) in cyc_tr) and
          all(abs(d - 1) < mp.mpf(10) ** -30 for (_, _, d, _) in cyc_tr))
    # express μ (shortest translation t_μ) and λ (t_λ = 2√3 i · t_μ) as integer combos of two
    # INDEPENDENT dual cycles (a spanning-tree cycle basis of the torus has extra, dependent
    # cycles; pick the first pair with non-parallel translations).
    Tall = [c[1] for c in cyc_tr]
    k0 = 0
    k1 = next(k for k in range(1, len(Tall))
              if abs(mp.im(Tall[k] / Tall[k0])) > mp.mpf(10) ** -20)
    T = [Tall[k0], Tall[k1]]
    basis = [cyc_tr[k0], cyc_tr[k1]]
    print(f"  lattice basis from dual cycles {k0}, {k1}: {mp.nstr(T[0], 12)}, {mp.nstr(T[1], 12)}")

    def int_combo(target):
        Mx = mp.matrix([[mp.re(T[0]), mp.re(T[1])], [mp.im(T[0]), mp.im(T[1])]])
        sol = mp.lu_solve(Mx, mp.matrix([mp.re(target), mp.im(target)]))
        xi, yi = int(mp.nint(sol[0])), int(mp.nint(sol[1]))
        assert abs(xi * T[0] + yi * T[1] - target) < mp.mpf(10) ** -30
        return xi, yi

    # shortest lattice vector: search small combos
    best = None
    for xi in range(-4, 5):
        for yi in range(-4, 5):
            if (xi, yi) == (0, 0):
                continue
            v = xi * T[0] + yi * T[1]
            if best is None or abs(v) < abs(best[2]) - mp.mpf(10) ** -30:
                best = (xi, yi, v)
    t_mu = best[2]
    t_lambda = 2 * mp.sqrt(3) * 1j * t_mu
    mu_c = (best[0], best[1])
    lam_c = int_combo(t_lambda)
    print(f"  μ = {mu_c[0]}·c{k0} + {mu_c[1]}·c{k1},  λ = {lam_c[0]}·c{k0} + {lam_c[1]}·c{k1}")

    def combo_row(coefs):
        a = [0] * knot["N"]; b = [0] * knot["N"]; s = 1
        for c, (row, _, _, _) in zip(coefs, basis):
            for j in range(knot["N"]):
                a[j] += c * row[0][j]; b[j] += c * row[1][j]
            if row[2] == -1 and c % 2:
                s = -s
        return (a, b, s)

    mu_row, lam_row = combo_row(mu_c), combo_row(lam_c)
    print(f"  μ row: a={mu_row[0]} b={mu_row[1]} sign={mu_row[2]}")
    print(f"  λ row: a={lam_row[0]} b={lam_row[1]} sign={lam_row[2]}")
    nt = nontrivial_cycles(knot["erows"], [(mu_row, None), (lam_row, None)])
    check("mu_lambda_rows_independent_of_edge_span", nt == [0, 1])
    check("mu_lambda_rows_evaluate_to_one", abs(rect_eval(mu_row, [w, w]) - 1) < mp.mpf(10) ** -30
          and abs(rect_eval(lam_row, [w, w]) - 1) < mp.mpf(10) ** -30)

    # ── NZ symplectic relations ────────────────────────────────────────────
    allrows = knot["erows"] + [mu_row, lam_row]
    G = nz_symplectic_check(allrows, knot["N"])
    print("  NZ symplectic Gram (edges, μ, λ):", G)
    E = len(knot["erows"])
    edge_edge_zero = all(G[p][q] == 0 for p in range(E) for q in range(E))
    edge_cusp_zero = all(G[p][q] == 0 for p in range(E) for q in (E, E + 1))
    mu_lam = G[E][E + 1]
    check("nz_edge_rows_isotropic", edge_edge_zero)
    check("nz_edge_cusp_orthogonal", edge_cusp_zero)
    check("nz_meridian_longitude_pair_is_pm2", abs(mu_lam) == 2, f"ω(μ,λ) = {mu_lam}")

    # ── torsion |det J| = √3 (corpus value from SnapPy rows) ───────────────
    tors = torsion_det(knot["erows"] + [mu_row], knot["N"], [w, w])
    print(f"  |det J_NZ| = {mp.nstr(tors, 25)}  (√3 = {mp.nstr(mp.sqrt(3), 25)})")
    check("nz_torsion_sqrt3", abs(tors - mp.sqrt(3)) < mp.mpf(10) ** -30)

    # ── A-polynomial by elimination ────────────────────────────────────────
    Lsym, Msym = sp.symbols("L M")
    eq_edge = sp.numer(sp.together(rect_expr(knot["erows"][0], [z0, z1]) - 1))
    eq_mu = sp.numer(sp.together(rect_expr(mu_row, [z0, z1]) - Msym**2))
    eq_lam = sp.numer(sp.together(rect_expr(lam_row, [z0, z1]) - Lsym**2))
    r1 = sp.resultant(eq_edge, eq_mu, z1)
    r2 = sp.resultant(eq_edge, eq_lam, z1)
    Apoly = sp.factor(sp.resultant(r1, r2, z0))
    print("  eliminated relation:", Apoly)
    A41 = -Msym**4 + Lsym * (1 - Msym**2 - 2 * Msym**4 - Msym**6 + Msym**8) - Lsym**2 * Msym**4
    # match one irreducible factor with A_{4₁} up to L→±L^{±1}, M→±M^{±1}
    factors = [f for f, _ in sp.factor_list(Apoly)[1]]
    matched = False
    for f in factors:
        for sL, eL, sM, eM in iproduct((1, -1), (1, -1), (1, -1), (1, -1)):
            g = A41.subs({Lsym: sL * Lsym**eL, Msym: sM * Msym**eM}, simultaneous=True)
            g = sp.numer(sp.together(g))
            q = sp.simplify(sp.expand(f) / sp.expand(g))
            if q.is_number and q != 0:
                matched = True
    check("a_polynomial_matches_corpus_A41", matched, "up to L→±L^{±1}, M→±M^{±1}")

    # ── general layering check: R²L (three tetrahedra) ─────────────────────
    tets3, maps3 = layer("RRL")
    M3 = next(Mm for Mm in maps3 if Mm.trace() > 0)
    t3, g3, N3, cl3, er3, cv3, cy3 = run_word("RRL", M3, "R²L, +φ (trace 4)")
    # solve the complete structure numerically: log-edge equations + log H(μ)=0 with μ found
    # by developing at a trial point; here use a volume-maximising Newton on log form.
    zs = sp.symbols("y0:3")
    logs = []
    for r in er3:
        a, b, s = r
        logs.append(sum(a[j] * sp.log(zs[j]) + b[j] * sp.log(1 - zs[j]) for j in range(3))
                    - 2 * sp.pi * sp.I + (sp.pi * sp.I if s == -1 else 0))
    # Complete structure: LOG-form equations (principal Log, all Im z > 0) — two independent
    # edge equations summing to 2πi and one dual cycle with log-holonomy 0. The log form is
    # what separates the complete structure (log H = 0) from a Dehn-filled one (log H = 2πi),
    # which the multiplicative form H = 1 cannot.
    hr3 = holonomy_rows(t3, g3, None, cy3)
    # The rect sign keeps only the PARITY of type-2 corners, so a log form built from it can be
    # off by multiples of iπ; solve multiplicatively instead and verify completeness
    # geometrically: (i) every dual cycle develops with derivative 1 (a Dehn-filled structure
    # fails this on all but the filling slope), (ii) the principal arguments of the corner
    # values around every edge class sum to exactly 2π (the true angle condition), (iii) all
    # Im z > 0.
    nt3 = nontrivial_cycles(er3, hr3)
    print(f"  dual cycles independent of the edge span: {nt3} (expect 2 on a torus)")
    check("RRL_two_independent_cusp_cycles", len(nt3) == 2)
    f = [rect_expr(r, zs) - 1 for r in (er3[0], er3[1], hr3[nt3[0]][0])]
    fl = sp.lambdify(zs, f, "mpmath")
    import random
    random.seed(20260906)
    starts = [[w, w, w]] + [[mp.mpc(random.uniform(-1, 2), random.uniform(0.1, 1.5))
                             for _ in range(3)] for _ in range(300)]
    shapes3, complete3 = None, False
    cl3_corners = [[(i, t3[i].etype(p, q)) for (i, p, q) in cl] for cl in cl3]
    for s0 in starts:
        try:
            sol = mp.findroot(lambda *v: fl(*v), s0, tol=mp.mpf(10) ** -40)
        except (ValueError, ZeroDivisionError):
            continue
        cand = [sol[k] for k in range(3)]
        if not all(mp.im(z) > 0 for z in cand):
            continue
        _, hol3 = develop(t3, g3, cand)
        derivs3 = [affine_from(P, Q)[0] for (_, P, Q) in hol3]
        angle_ok = all(abs(sum(mp.arg(corner_value(cand[i], ty)) for (i, ty) in cl) - 2 * mp.pi)
                       < mp.mpf(10) ** -30 for cl in cl3_corners)
        if all(abs(d - 1) < mp.mpf(10) ** -30 for d in derivs3) and angle_ok:
            shapes3, complete3 = cand, True
            break
    assert shapes3 is not None, "no complete structure found for R²L from the trial starts"
    # exact identification of the numeric solution in a quadratic field, then EXACT verification
    exact3 = [sp.nsimplify(sp.Float(str(mp.re(z)), 40)) + sp.I * sp.nsimplify(sp.Float(str(mp.im(z)), 40),
              [sp.sqrt(7)], tolerance=1e-30) for z in shapes3]
    exact_ok = all(sp.simplify(rect_expr(r, exact3) - 1) == 0 for r in er3)
    print(f"  R²L shapes, exact: {exact3}  exact edge check: {exact_ok}")
    check("RRL_shapes_exact_in_Q_sqrt_minus7", exact_ok,
          "numeric root identified in ℚ(√−7) and re-verified symbolically")
    wb.add_data("RRL_shapes_exact", [str(e) for e in exact3])
    # carry the EXACT shapes forward (the numeric root is only the identification step)
    shapes3 = [mp.mpc(str(sp.N(sp.re(e), 60)), str(sp.N(sp.im(e), 60))) for e in exact3]
    _, hol3 = develop(t3, g3, shapes3)
    complete3 = all(abs(affine_from(P, Q)[0] - 1) < mp.mpf(10) ** -40 for (_, P, Q) in hol3)
    res3 = [abs(rect_eval(r, shapes3) - 1) for r in er3]
    vol3 = sum(bloch_wigner(z) for z in shapes3)
    print(f"  R²L shapes: {[mp.nstr(z, 15) for z in shapes3]}")
    print(f"  R²L residuals: {[mp.nstr(r, 5) for r in res3]}")
    print(f"  R²L volume = {mp.nstr(vol3, 30)}")
    all_upper = all(mp.im(z) > 0 for z in shapes3)
    check("RRL_three_tetrahedra_three_edges", N3 == 3 and len(er3) == 3)
    check("RRL_complete_structure_found",
          all(r < mp.mpf(10) ** -45 for r in res3) and all_upper and complete3,
          "exact shapes; every dual cycle develops with derivative 1; all corner sums 2π")

    # ── convention independence (owner, 2026-09-06: validate probes are not C-dependent) ──
    # AST scan of this file's imports: nothing that carries a Markov parameter, a Hecke
    # trace, or a q₀ anchor is imported, so no convention (C or D) can enter the computation.
    import ast
    tree = ast.parse(open(__file__, encoding="utf-8").read())
    imported = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imported.update(al.name for al in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            imported.add(node.module)
    banned = ("pyhecke", "q_parameter", "hecke", "gram", "markov", "wedderburn", "constants")
    hits = sorted(m for m in imported if any(b in m.lower() for b in banned))
    check("no_convention_dependence_imports", not hits,
          f"imports: {sorted(imported)}")
    G3 = nz_symplectic_check(er3, 3)
    check("RRL_edge_rows_isotropic", all(G3[p][q] == 0 for p in range(3) for q in range(3)))
    # census reference for the trace-4 bundle (m009/m010): 2.666744783449061… — quoted from
    # memory of the SnapPy census, NOT from a held source; recorded as data, not asserted.
    wb.add_data("RRL_volume_50dps", mp.nstr(vol3, 45))
    wb.add_data("RRL_volume_census_reference_from_memory", "2.666744783449061")
    wb.add_caveat("The R²L volume is compared only informally to the census value for the "
                  "trace-4 once-punctured-torus bundle (m009/m010), quoted from memory and not "
                  "from a held source; it is recorded as data and not asserted.")

    # ── record ─────────────────────────────────────────────────────────────
    wb.add_parameter("braid", "(σ₁σ₂⁻¹)² in B₃, closure = 4₁")
    wb.add_parameter("monodromy", str(phi.tolist()))
    wb.add_parameter("word", "RL")
    wb.add_data("edge_rows_rect", [list(r) for r in knot["erows"]])
    wb.add_data("meridian_row_rect", list(mu_row))
    wb.add_data("longitude_row_rect", list(lam_row))
    wb.add_data("nz_symplectic_gram", G)
    wb.add_data("cusp_modulus_knot", mp.nstr(tau_knot, 45))
    wb.add_data("cusp_modulus_sister", mp.nstr(tau_sis, 45))
    wb.add_data("volume_50dps", mp.nstr(vol, 45))
    wb.add_data("torsion_det", mp.nstr(tors, 45))
    wb.add_data("eliminated_relation", str(Apoly))
    wb.add_caveat("Scope: the Stallings step needs a homogeneous braid with once-punctured-torus "
                  "fibre; among hyperbolic knots in S³ that is 4₁ only. 5₂ (not fibred) needs "
                  "Guéritaud's two-bridge layering — beaned, not done here.")
    wb.add_caveat("The meridian is identified as the shortest vector of the derived cusp lattice "
                  "and the longitude as its 2√3 i partner; the identification is then verified "
                  "independently by the A-polynomial elimination.")
    wb.add_caveat("Orientation convention: ambient = (fibre orientation) ∧ dt with the class-O "
                  "vertex ordering (P,Q,S,R). 4₁ is amphichiral so this probe cannot detect a "
                  "global mirror; a chiral case must re-check it (matters for S⁺ vs S⁻).")
    wb.save({"q0Anchor": "independent",
             "q0AnchorReason": "pure topology/geometry: no q, no Markov parameter, no anchor"})
    print("\nALL PASS" if ok_all else "\nSOME FAIL")
    return 0 if ok_all else 1


if __name__ == "__main__":
    raise SystemExit(main())
