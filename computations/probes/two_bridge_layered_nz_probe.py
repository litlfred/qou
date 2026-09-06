#!/usr/bin/env python3
"""
Two-bridge link complements: Neumann–Zagier data from the Farey word (bean qou-yvyd).

Extends `nz_gluing_from_braid_monodromy_probe.py` (once-punctured-torus bundles, 4₁ only) to
the class that reaches the A_ω cross-knot gate: the two-bridge knots 4₁ = S(5,2) and 5₂ = S(7,3).

CONSTRUCTION (Futer–Kalfagianni–Purcell §2.4, library arxiv-0808.2716v4; Guéritaud 2006 is
NOT held, so the fold is not transcribed — see below). The complement of a two-bridge link
K(Ω) contains a product region S × I, S the 4-punctured sphere (a pillowcase with its four
corners removed), layered by the monodromy word Ω exactly as a punctured-torus bundle is —
except that a diagonal exchange on the pillowcase replaces BOTH arcs of a slope, so each letter
contributes TWO flip tetrahedra (the front and back squares of the pillowcase). The two ends of
the product region are not glued to each other; each end surface is FOLDED onto itself,
"identifying its four ideal triangles in pairs" (FKP §2.4), which is the clasp closing the
4-string braid.

THE FOLD IS FOUND, NOT ASSUMED. Guéritaud's explicit fold rule is not in the library, so this
probe enumerates every pairing of the four end triangles with every orientation-reversing
simplicial identification (27 per end, 729 in all) and keeps the candidates that are
(i) manifolds with torus cusps, (ii) one-cusped, and (iii) geometric — a complete hyperbolic
structure with all Im z > 0 exists. The surviving structure is then CHECKED, for 4₁, against
Vol(4₁) = 2·Cl₂(π/3) and the cusp modulus 2√3 i (which the bundle route derived independently),
and for 5₂ against the corpus value Vol(5₂) = 2.82812208833078316… (held in
`fivetwo_ak_state_integral.py`) — a volume the search never sees.

The pillowcase model. The 4-punctured sphere is T₄/ι, where T₄ = ℝ²/ℤ² minus the four
half-integer points and ι = −1. For a Farey pair (a, b), the lines of slopes a and b through the
punctures cut T₄ into four parallelograms with sides a/2, b/2 and corners at the punctures; ι
swaps them in pairs, so the pillowcase has two squares ("front", corner 0; "back", corner a/2),
each with all four punctures as vertices. A flip on slope a+b → b−a in each square is one
tetrahedron; cusp identity of a vertex is its puncture, which ι fixes.

Precision: exact combinatorics; shapes by mpmath at 50 dps; volumes by Bloch–Wigner. No q, no
Markov parameter, no anchor (q0Anchor independent).

-- Ref: library/arxiv-0808.2716v4 §2.2–2.4 (Futer–Kalfagianni–Purcell, Cusp areas of Farey
--      manifolds) — the layering and the fold, described but not specified.
-- Ref: [manuscript] computations/probes/nz_gluing_from_braid_monodromy_probe.py
"""
from __future__ import annotations

import os
import sys
from fractions import Fraction as Fr
from itertools import product as iproduct, permutations

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402

import sympy as sp  # noqa: E402
from mpmath import mp  # noqa: E402

from nz_gluing_from_braid_monodromy_probe import (  # noqa: E402
    Tet, UF, edge_classes, edge_rows, cusp_vertices, ccw_at, cusp_neighbor, develop,
    affine_from, corner_value, bloch_wigner, rect_eval, rect_expr, nz_symplectic_check,
    torsion_det, find_cycles, holonomy_rows, nontrivial_cycles, _canon, _det,
)

set_compute_dps()
mp.dps = 50


# ─────────────────────────────────────────────────────────────────────────────
# 1. Pillowcase layering
# ─────────────────────────────────────────────────────────────────────────────
def _fr(v):
    return (Fr(v[0]), Fr(v[1]))


def _modZ(p):
    return (p[0] - (p[0].numerator // p[0].denominator), p[1] - (p[1].numerator // p[1].denominator))


class PTet(Tet):
    """Flip tetrahedron on one pillowcase square. Corner P₀ (a puncture, in ½ℤ²), sides a/2, b/2
    (a, b the kept slopes with det(a,b) > 0 and removed = a+b). Vertex labels as in Tet:
    0 = P₀, 1 = P₀ + a/2, 2 = P₀ + (a+b)/2, 3 = P₀ + b/2; class-O ordering (0,1,3,2)."""

    def __init__(self, idx, a, b, corner, layer, square):
        super().__init__(idx, a, b)
        ha, hb = (Fr(a[0], 2), Fr(a[1], 2)), (Fr(b[0], 2), Fr(b[1], 2))
        P0 = _fr(corner)
        self.abs = {0: P0, 1: (P0[0] + ha[0], P0[1] + ha[1]),
                    2: (P0[0] + ha[0] + hb[0], P0[1] + ha[1] + hb[1]),
                    3: (P0[0] + hb[0], P0[1] + hb[1])}
        self.layer, self.square = layer, square

    def puncture(self, v):
        return _modZ(self.abs[v])

    def face_key(self, cyc):
        """ι-canonical key of a face: the set of (puncture, outgoing vector) around the ccw cycle,
        minimised over ι (puncture ↦ −puncture ≡ puncture, vector ↦ −vector)."""
        items = []
        for k in range(3):
            p, q = self.abs[cyc[k]], self.abs[cyc[(k + 1) % 3]]
            items.append((_modZ(p), (q[0] - p[0], q[1] - p[1])))
        k1 = tuple(sorted(items))
        k2 = tuple(sorted((pt, (-e[0], -e[1])) for (pt, e) in items))
        return min(k1, k2)

    def face_cycle_abs(self, cyc):
        """(puncture, vector) list in ccw order — used to align vertices across a gluing."""
        out = []
        for k in range(3):
            p, q = self.abs[cyc[k]], self.abs[cyc[(k + 1) % 3]]
            out.append((_modZ(p), (q[0] - p[0], q[1] - p[1])))
        return out


def pillowcase_layers(word: str):
    """Two PTets per letter. Returns tets (index = 2·layer + square)."""
    x, y, v = (1, 0), (0, 1), (1, 1)
    tets = []
    for i, letter in enumerate(word):
        if letter == "R":
            removed, k1, k2 = x, y, v
            nxt = lambda new: (v, y, new)   # noqa: E731
        elif letter == "L":
            removed, k1, k2 = y, x, v
            nxt = lambda new: (x, v, new)   # noqa: E731
        else:
            raise ValueError(letter)
        cand = [(k1[0] + k2[0], k1[1] + k2[1]), (k1[0] - k2[0], k1[1] - k2[1])]
        new = next(c for c in cand if _canon(c) != _canon(removed))
        found = None
        for sa, sb in iproduct((1, -1), (1, -1)):
            a = (sa * k1[0], sa * k1[1]); b = (sb * k2[0], sb * k2[1])
            if (a[0] + b[0], a[1] + b[1]) == removed:
                found = (a, b); break
        assert found is not None
        a, b = found
        if _det(a, b) < 0:
            a, b = b, a
        # front square corner 0, back square corner a/2
        tets.append(PTet(2 * i, a, b, (0, 0), i, 0))
        tets.append(PTet(2 * i + 1, a, b, (Fr(a[0], 2), Fr(a[1], 2)), i, 1))
        x, y, v = nxt(new)
    return tets


def _align(ft_abs, fb_abs):
    """Vertex alignment between two faces given as ccw (puncture, vector) lists that agree up to
    rotation, possibly after ι on one of them. Returns rotation r and whether ι was needed."""
    for use_iota in (False, True):
        fb = fb_abs if not use_iota else [(pt, (-e[0], -e[1])) for (pt, e) in fb_abs]
        for r in range(3):
            if [fb[(k + r) % 3] for k in range(3)] == ft_abs:
                return r, use_iota
    return None


def glue_layers(tets):
    """top faces of layer i ↔ bottom faces of layer i+1 (matched by ι-canonical key)."""
    gl = {}
    bylayer = {}
    for t in tets:
        bylayer.setdefault(t.layer, []).append(t)
    n = max(bylayer) + 1
    for i in range(n - 1):
        tops = [(t, f) for t in bylayer[i] for f in t.faces()["top"]]
        bots = [(t, f) for t in bylayer[i + 1] for f in t.faces()["bot"]]
        for (tt, ft) in tops:
            key = tt.face_key(ft)
            hit = [(tb, fb) for (tb, fb) in bots if tb.face_key(fb) == key]
            assert len(hit) == 1, f"layer {i}: top face matches {len(hit)} bottom faces"
            tb, fb = hit[0]
            al = _align(tt.face_cycle_abs(ft), tb.face_cycle_abs(fb))
            assert al is not None
            r, _ = al
            vmap = {ft[k]: fb[(k + r) % 3] for k in range(3)}
            for p, q in vmap.items():
                assert tt.puncture(p) == tb.puncture(q)
            gl[(tt.i, ft)] = (tb.i, fb, vmap)
            gl[(tb.i, fb)] = (tt.i, ft, {q: p for p, q in vmap.items()})
    return gl


# ─────────────────────────────────────────────────────────────────────────────
# 2. Fold search at the two ends
# ─────────────────────────────────────────────────────────────────────────────
def _pairings(items):
    a, b, c, d = items
    return [((a, b), (c, d)), ((a, c), (b, d)), ((a, d), (b, c))]


def _rev_maps(f1, f2):
    """Orientation-reversing simplicial identifications of two faces given as ccw cycles:
    ccw (u,v,w) of f1 ↦ a CLOCKWISE cycle of f2 (three rotations)."""
    out = []
    f2r = (f2[0], f2[2], f2[1])
    for r in range(3):
        out.append({f1[k]: f2r[(k + r) % 3] for k in range(3)})
    return out


def fold_candidates(tets, end):
    """All folds of one end: list of gluing dicts for the four free faces."""
    bylayer = {}
    for t in tets:
        bylayer.setdefault(t.layer, []).append(t)
    layer = min(bylayer) if end == "bot" else max(bylayer)
    side = "bot" if end == "bot" else "top"
    faces = [(t.i, f) for t in bylayer[layer] for f in t.faces()[side]]
    cands = []
    for pairing in _pairings(faces):
        maps_per_pair = []
        for (F1, F2) in pairing:
            maps_per_pair.append([(F1, F2, m) for m in _rev_maps(F1[1], F2[1])])
        for choice in iproduct(*maps_per_pair):
            g = {}
            for (F1, F2, m) in choice:
                g[F1] = (F2[0], F2[1], m)
                g[F2] = (F1[0], F1[1], {q: p for p, q in m.items()})
            cands.append(g)
    return cands


def cusp_links(tets, gl):
    """Per cusp: (number of cusp triangles, Euler characteristic). Cusp = class of tetrahedron
    vertices under the face gluings."""
    uf = UF()
    for (i, f), (j, g, vmap) in gl.items():
        for p in f:
            uf.union((i, p), (j, vmap[p]))
    cusp_of = {(t.i, a): uf.find((t.i, a)) for t in tets for a in range(4)}
    cusps = sorted(set(cusp_of.values()), key=str)
    verts, _ = cusp_vertices(tets, gl)   # cusp-triangulation vertices (edge ends)
    out = {}
    for c in cusps:
        F = sum(1 for k, v in cusp_of.items() if v == c)
        V = sum(1 for vl in verts if cusp_of[(vl[0][0], vl[0][1])] == c)
        E = Fr(3 * F, 2)
        out[c] = (F, V - E + F)
    return out, cusp_of


def complete_structure(tets, gl, N, erows, seed=0, tries=40):
    """Multiplicative solve of (N−1 independent edge rows + 1 nontrivial cusp cycle) from random
    starts; accept only a solution with all Im z > 0, every dual cycle developing with derivative
    1, and every edge's corner arguments summing to 2π. Returns shapes or None."""
    import random
    random.seed(seed)
    zs = sp.symbols(f"y0:{N}")
    cycles = find_cycles(tets, gl)
    hr = holonomy_rows(tets, gl, None, cycles)
    nt = nontrivial_cycles(erows, hr)
    if len(nt) < 1:
        return None
    # pick N-1 independent edge rows
    chosen = []
    base = []
    for r in erows:
        trial = base + [list(r[0]) + list(r[1])]
        if sp.Matrix(trial).rank() > (sp.Matrix(base).rank() if base else 0):
            base = trial; chosen.append(r)
    eqs = [rect_expr(r, zs) - 1 for r in chosen[:N - 1]] + [rect_expr(hr[nt[0]][0], zs) - 1]
    if len(eqs) != N:
        # fill with further cusp cycles if the edge rank is short
        k = 1
        while len(eqs) < N and k < len(nt):
            eqs.append(rect_expr(hr[nt[k]][0], zs) - 1); k += 1
        if len(eqs) != N:
            return None
    fl = sp.lambdify(zs, eqs, "mpmath")
    classes_corners = [[(i, tets[i].etype(p, q)) for (i, p, q) in cl] for cl in edge_classes(tets, gl)]
    w = mp.exp(1j * mp.pi / 3)
    starts = [[w] * N] + [[mp.mpc(random.uniform(-1, 2), random.uniform(0.1, 1.6)) for _ in range(N)]
                          for _ in range(tries)]
    for s0 in starts:
        try:
            sol = mp.findroot(lambda *v: fl(*v), s0, tol=mp.mpf(10) ** -40)
        except (ValueError, ZeroDivisionError, TypeError, IndexError):
            continue
        cand = [sol[k] for k in range(N)]
        if not all(mp.im(z) > mp.mpf(10) ** -20 for z in cand):
            continue
        try:
            _, hol = develop(tets, gl, cand)
        except Exception:
            continue
        if not all(abs(affine_from(P, Q)[0] - 1) < mp.mpf(10) ** -30 for (_, P, Q) in hol):
            continue
        if not all(abs(sum(mp.arg(corner_value(cand[i], ty)) for (i, ty) in cl) - 2 * mp.pi)
                   < mp.mpf(10) ** -30 for cl in classes_corners):
            continue
        return cand
    return None


def two_bridge_search(word, label, vol_ref=None, max_solutions=3):
    tets = pillowcase_layers(word)
    N = len(tets)
    base_gl = glue_layers(tets)
    bots = fold_candidates(tets, "bot")
    tops = fold_candidates(tets, "top")
    print(f"\n[{label}] word={word}: {N} tetrahedra, {len(bots)}×{len(tops)} fold candidates")
    stats = {"total": 0, "torus_cusps": 0, "one_cusp": 0, "geometric": 0}
    found = []
    for gb in bots:
        for gt in tops:
            stats["total"] += 1
            gl = dict(base_gl); gl.update(gb); gl.update(gt)
            assert len(gl) == 4 * N
            links, cusp_of = cusp_links(tets, gl)
            if not all(chi == 0 for (_, chi) in links.values()):
                continue
            stats["torus_cusps"] += 1
            if len(links) != 1:
                continue
            stats["one_cusp"] += 1
            classes = edge_classes(tets, gl)
            erows = edge_rows(tets, classes)
            shapes = complete_structure(tets, gl, N, erows)
            if shapes is None:
                continue
            stats["geometric"] += 1
            vol = sum(bloch_wigner(z) for z in shapes)
            found.append(dict(gl=gl, gb=gb, gt=gt, shapes=shapes, vol=vol, erows=erows, classes=classes))
            print(f"  geometric candidate #{stats['geometric']}: Vol = {mp.nstr(vol, 25)}"
                  + (f"  (ref {mp.nstr(vol_ref, 25)}, diff {mp.nstr(abs(vol - vol_ref), 3)})" if vol_ref else ""))
            if stats["geometric"] >= max_solutions:
                break
        if stats["geometric"] >= max_solutions:
            break
    print(f"  stats: {stats}")
    return tets, found, stats


def cusp_modulus(tets, gl, shapes):
    pos, hol = develop(tets, gl, shapes)
    trans = []
    for (key, P, Q) in hol:
        d, t, err = affine_from(P, Q)
        if abs(t) > mp.mpf(10) ** -30:
            trans.append(t)
    trans.sort(key=lambda c: abs(c))
    b1 = trans[0]
    b2 = next(c for c in trans if abs(mp.im(c / b1)) > mp.mpf(10) ** -20)
    # reduce to a fundamental domain basis: search short combos
    best = None
    for xi in range(-4, 5):
        for yi in range(-4, 5):
            if (xi, yi) == (0, 0):
                continue
            v = xi * b1 + yi * b2
            if best is None or abs(v) < abs(best) - mp.mpf(10) ** -30:
                best = v
    mu = best
    # second basis vector: shortest independent
    best2 = None
    for xi in range(-6, 7):
        for yi in range(-6, 7):
            v = xi * b1 + yi * b2
            if abs(mp.im(v / mu)) < mp.mpf(10) ** -20:
                continue
            if best2 is None or abs(v) < abs(best2) - mp.mpf(10) ** -30:
                best2 = v
    r = best2 / mu
    if mp.im(r) < 0:
        r = -r
    r = r - mp.nint(mp.re(r))
    return r


def main() -> int:
    from qou_substrate.witness import WitnessBuilder

    wb = WitnessBuilder("two-bridge-layered-nz", engine="python", _script_path=__file__)
    wb.set_description(
        "Two-bridge link complements from the Farey word: pillowcase layering (two tetrahedra per "
        "letter) with the end folds found by exhaustive search under manifold / one-cusp / geometric "
        "filters; validated on 4₁ (volume, cusp modulus 2√3 i) and 5₂ (corpus volume). Bean qou-yvyd.")
    wb.set_content_block("conj:stokes-dt-bps-bridge")
    ok_all = True

    def check(name, cond, note=""):
        nonlocal ok_all
        ok_all &= bool(cond)
        print(f"  [{'PASS' if cond else 'FAIL'}] {name} {note}")
        wb.add_assertion(name, computed="1" if cond else "0", expected="1", tolerance="0.5",
                         source="two_bridge_layered_nz_probe")

    vol41 = 2 * mp.clsin(2, mp.pi / 3)
    vol52 = mp.mpf("2.8281220883307831627638988092766349427709813173006")

    # ── 4₁ = S(5,2): continued fraction [2,2]; the clasps take one crossing from each end ──
    results = {}
    for word in ("RL", "LR"):
        tets, found, stats = two_bridge_search(word, f"4₁ trial word {word}", vol_ref=vol41)
        results[word] = (tets, found, stats)
    best41 = None
    for word, (tets, found, stats) in results.items():
        for f in found:
            if abs(f["vol"] - vol41) < mp.mpf(10) ** -30:
                best41 = (word, tets, f); break
        if best41:
            break
    check("fourone_two_bridge_geometric_with_vol_2cl2", best41 is not None)
    if best41:
        word, tets, f = best41
        N = len(tets)
        tau = cusp_modulus(tets, f["gl"], f["shapes"])
        print(f"  4₁ via two-bridge: word {word}, {N} tetrahedra, shapes "
              f"{[mp.nstr(z, 12) for z in f['shapes']]}, cusp modulus {mp.nstr(tau, 20)}")
        check("fourone_two_bridge_cusp_modulus_2sqrt3i",
              abs(tau - 2 * mp.sqrt(3) * 1j) < mp.mpf(10) ** -25, "matches the bundle route")
        G = nz_symplectic_check(f["erows"], N)
        check("fourone_two_bridge_edge_rows_isotropic",
              all(G[p][q] == 0 for p in range(len(f['erows'])) for q in range(len(f['erows']))))
        wb.add_data("fourone_word", word)
        wb.add_data("fourone_tetrahedra", N)
        wb.add_data("fourone_edge_rows_rect", [list(r) for r in f["erows"]])
        wb.add_data("fourone_shapes", [mp.nstr(z, 45) for z in f["shapes"]])
        wb.add_data("fourone_cusp_modulus", mp.nstr(tau, 45))
        wb.add_data("fourone_fold_bot", str(f["gb"]))
        wb.add_data("fourone_fold_top", str(f["gt"]))

    # ── 5₂ = S(7,3): continued fraction [2,3] → braid words of length 3 ──
    best52 = None
    stats52 = {}
    for word in ("RLL", "LLR", "RRL", "LRR"):
        tets, found, stats = two_bridge_search(word, f"5₂ trial word {word}", vol_ref=vol52)
        stats52[word] = stats
        for f in found:
            if abs(f["vol"] - vol52) < mp.mpf(10) ** -25:
                best52 = (word, tets, f); break
        if best52:
            break
    check("fivetwo_two_bridge_geometric_with_corpus_volume", best52 is not None,
          "Vol(5₂) = 2.8281220883… is not an input to the search")
    if best52:
        word, tets, f = best52
        N = len(tets)
        tau = cusp_modulus(tets, f["gl"], f["shapes"])
        print(f"  5₂ via two-bridge: word {word}, {N} tetrahedra, shapes "
              f"{[mp.nstr(z, 12) for z in f['shapes']]}, cusp modulus {mp.nstr(tau, 20)}")
        # shape field: 5₂'s invariant trace field is cubic, discriminant −23. Test: the minimal
        # polynomial of each shape over ℚ has degree ≤ 3 (identify by PSLQ on 1, z, z², z³).
        cubic_ok = True
        minpolys = []
        for z in f["shapes"]:
            rel = mp.pslq([1, z, z ** 2, z ** 3], maxcoeff=10 ** 6, maxsteps=10 ** 5)
            minpolys.append(rel)
            cubic_ok &= rel is not None
        print(f"  5₂ shape integer relations (1, z, z², z³): {minpolys}")
        check("fivetwo_shapes_satisfy_cubic_relations", cubic_ok,
              "consistent with the cubic shape field of 5₂ (disc −23)")
        G = nz_symplectic_check(f["erows"], N)
        check("fivetwo_two_bridge_edge_rows_isotropic",
              all(G[p][q] == 0 for p in range(len(f['erows'])) for q in range(len(f['erows']))))
        wb.add_data("fivetwo_word", word)
        wb.add_data("fivetwo_tetrahedra", N)
        wb.add_data("fivetwo_edge_rows_rect", [list(r) for r in f["erows"]])
        wb.add_data("fivetwo_shapes", [mp.nstr(z, 45) for z in f["shapes"]])
        wb.add_data("fivetwo_volume", mp.nstr(f["vol"], 45))
        wb.add_data("fivetwo_cusp_modulus", mp.nstr(tau, 45))
        wb.add_data("fivetwo_shape_relations", [str(r) for r in minpolys])
        wb.add_data("fivetwo_fold_bot", str(f["gb"]))
        wb.add_data("fivetwo_fold_top", str(f["gt"]))
    wb.add_data("fivetwo_search_stats", {k: v for k, v in stats52.items()})

    # ── convention independence ──
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
    check("no_convention_dependence_imports", not hits, f"imports: {sorted(imported)}")

    wb.add_caveat("The fold at each end is FOUND by exhaustive search under manifold, one-cusp "
                  "and geometric filters, not transcribed from Guéritaud (not held). The volume "
                  "references are checks, never inputs.")
    wb.add_caveat("Orientation: the pillowcase squares inherit the fibre orientation ∧ dt; 5₂ is "
                  "chiral, so which of S⁺/S⁻ the derived triangulation corresponds to is NOT "
                  "settled here (mirror gives conjugate shapes, same volume).")
    wb.save({"q0Anchor": "independent",
             "q0AnchorReason": "pure topology/geometry: no q, no Markov parameter, no anchor"})
    print("\nALL PASS" if ok_all else "\nSOME FAIL")
    return 0 if ok_all else 1


if __name__ == "__main__":
    raise SystemExit(main())
