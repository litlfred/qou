#!/usr/bin/env python3
"""
Cusp rows of the derived two-bridge triangulations, and the A-polynomial by elimination
(bean qou-yvyd, second rung).

`two_bridge_layered_nz_probe.py` derived triangulations of S³∖4₁ (word R, 2 tetrahedra) and
S³∖5₂ (word RL, 4 tetrahedra) from the Farey word with the end folds found by search, and
recorded the folds in its witness. This probe rebuilds those triangulations from the recorded
folds (no search) and does what was left open:

1. **Longitude and meridian, homologically.** Cusp cycles are loops in the dual 1-skeleton of
   the triangulation, so their classes in H₁(M) ≅ ℤ are computable from the dual spine
   (d₁, d₂ as in `h1_invariants`). The longitude λ is the primitive cusp class that dies in
   H₁(M); the meridian μ is a cusp class mapping to a generator (Bézout), determined modulo λ.
   No cusp-shape heuristics, no reference data.
2. **The A-polynomial.** Points on the deformation curve are sampled by continuation from the
   complete structure (edge rows + H(μ) = m², 50 dps); the A-polynomial A(L, M) is recovered as
   the integer polynomial of minimal bidegree vanishing on them (nullspace over monomials, then
   integer rounding, then re-verification on fresh samples to 1e-30). M² = H(μ), L² = H(λ).
3. **Framing and chirality from the Newton polygon.** Boundary slopes are the edge slopes of the
   Newton polygon (Δdeg_M/Δdeg_L, Culler–Cooper–Gillet–Long–Shalen). The residual μ → μ + kλ
   ambiguity is fixed by requiring the derived slopes to be integers with 0 among them; the sign
   of the non-zero slopes is the chirality of the derived triangulation relative to the
   literature convention. The corpus holds the 5₂ slopes only as LITERATURE-RECALLED values
   ({0, −4, −10} in `qbeta_g3_aomega_route_a_newton_polygon.py`, "max slope 10" in the
   2026-08-11 memo); they are compared to, never used.
4. **Control.** 4₁ goes through the same path and must reproduce A_{4₁} (already derived by the
   bundle route in `nz_gluing_from_braid_monodromy_probe.py`) with slopes {±4}.

Precision: mpmath 50 dps; integer polynomials; A(±1, ±1) = 0 checked exactly at the complete
point. No q, no Markov parameter, no anchor (q0Anchor independent).

-- Ref: [manuscript] computations/probes/two_bridge_layered_nz_probe.py
-- Ref: [manuscript] computations/probes/nz_gluing_from_braid_monodromy_probe.py
"""
from __future__ import annotations

import ast
import json
import os
import random
import sys
from fractions import Fraction as Fr
from math import gcd

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402

import sympy as sp  # noqa: E402
from mpmath import mp  # noqa: E402

from nz_gluing_from_braid_monodromy_probe import (  # noqa: E402
    edge_classes, edge_rows, find_cycles, holonomy_rows, nontrivial_cycles, rect_expr,
    rect_eval, develop, affine_from, corner_value, ccw_at, cusp_neighbor, bloch_wigner,
)
from two_bridge_layered_nz_probe import pillowcase_layers, glue_layers  # noqa: E402

set_compute_dps()
mp.dps = 50
HERE = os.path.dirname(os.path.abspath(__file__))


# ─────────────────────────────────────────────────────────────────────────────
# 1. Rebuild from the recorded folds
# ─────────────────────────────────────────────────────────────────────────────
def load_recorded(knot: str):
    w = json.load(open(os.path.join(HERE, "two-bridge-layered-nz.witness.json")))
    d = w.get("data", w)
    return (d[f"{knot}_word"], [ast.literal_eval(s) for s in d[f"{knot}_fold_bottom"]],
            [ast.literal_eval(s) for s in d[f"{knot}_fold_top"]], d)


def rebuild(word, fold_bot, fold_top):
    tets = pillowcase_layers(word)
    gl = glue_layers(tets)
    for rec in fold_bot + fold_top:
        A, fa, B, fb, vm = rec["tet_a"], tuple(rec["face_a"]), rec["tet_b"], tuple(rec["face_b"]), rec["vmap"]
        gl[(A, fa)] = (B, fb, dict(vm))
        gl[(B, fb)] = (A, fa, {q: p for p, q in vm.items()})
    assert len(gl) == 4 * len(tets)
    return tets, gl


# ─────────────────────────────────────────────────────────────────────────────
# 2. Dual spine, H₁(M), and the class of a cusp cycle
# ─────────────────────────────────────────────────────────────────────────────
def dual_spine(tets, gl):
    """dual edges (glued face pairs, oriented (i,f) → (j,g)), index map, d₁ and d₂."""
    N = len(tets)
    pairs = {}
    for (i, f), (j, g, vmap) in gl.items():
        key = frozenset([(i, frozenset(f)), (j, frozenset(g))])
        pairs.setdefault(key, (i, frozenset(f), j, frozenset(g)))
    dual_edges = list(pairs.values())
    idx = {}
    for k, (i, f, j, g) in enumerate(dual_edges):
        idx[(i, f)] = (k, 1); idx[(j, g)] = (k, -1)
    cols = []
    for cl in edge_classes(tets, gl):
        i, p, q = cl[0]
        col = [0] * len(dual_edges)
        r = next(v for v in range(4) if v not in (p, q))
        face = frozenset((p, q, r))
        cur = (i, p, q, face)
        seen = 0
        while True:
            i, p, q, face = cur
            k, sgn = idx[(i, face)]
            col[k] += sgn
            j, g, vmap = gl[next(key for key in gl if key[0] == i and frozenset(key[1]) == face)]
            p2, q2 = vmap[p], vmap[q]
            r2 = next(v for v in g if v not in (p2, q2))
            other = next(v for v in range(4) if v not in (p2, q2, r2))
            cur = (j, p2, q2, frozenset((p2, q2, other)))
            seen += 1
            if (cur[0], frozenset((cur[1], cur[2]))) == (cl[0][0], frozenset((cl[0][1], cl[0][2]))) \
                    and cur[3] == frozenset((cl[0][1], cl[0][2], r)):
                break
            assert seen < 10 * len(cl) + 10
        cols.append(col)
    D2 = sp.Matrix(cols).T
    d1 = sp.zeros(N, len(dual_edges))
    for k, (i, f, j, g) in enumerate(dual_edges):
        d1[j, k] += 1; d1[i, k] -= 1
    return dual_edges, idx, d1, D2


def cycle_vector(tets, gl, idx, cyc, n_edges):
    """A dual cusp cycle (list of (i, a, (u, s)): leave cusp triangle (i,a) through side {u,s},
    i.e. tetrahedron face (a,u,s)) as a vector over dual edges."""
    v = [0] * n_edges
    for (i, a, (u, s)) in cyc:
        k, sgn = idx[(i, frozenset((a, u, s)))]
        v[k] += sgn
    return v


def h1_functional(d1, D2):
    """A rational vector w with wᵀ D₂ = 0 that is NOT in the row space of d₁: it evaluates
    cycles to a well-defined homomorphism H₁(M) → ℚ, nonzero (H₁ ≅ ℤ here)."""
    left_kernel = D2.T.nullspace()      # vectors w with D2ᵀ w = 0
    rows_d1 = d1.rowspace()
    Rspan = sp.Matrix.vstack(*rows_d1) if rows_d1 else sp.zeros(0, D2.shape[0])
    for w in left_kernel:
        M = sp.Matrix.vstack(Rspan, w.T) if Rspan.shape[0] else w.T
        if M.rank() > (Rspan.rank() if Rspan.shape[0] else 0):
            return w
    raise RuntimeError("no functional outside the coboundaries — H₁ rank 0?")


def cycle_translation(tets, gl, shapes, cyc):
    """Developed translation (and dilation) of a closed dual cusp cycle: place its first
    triangle as develop() does and walk the cycle."""
    i0, a0, _ = cyc[0]
    x, y, wv = ccw_at(tets[i0], a0)
    P = {x: mp.mpc(0), y: mp.mpc(1), wv: corner_value(shapes[i0], tets[i0].etype(a0, x))}
    start = dict(P)
    for (i, a, (u, s)) in cyc:
        j, a2, u2, s2 = cusp_neighbor(tets, gl, i, a, u, s)
        x2, y2, w2 = ccw_at(tets[j], a2)
        v2 = next(q for q in (x2, y2, w2) if q not in (u2, s2))
        order = (x2, y2, w2)
        k = order.index(s2)
        if order[(k + 1) % 3] != u2:
            c2 = corner_value(shapes[j], tets[j].etype(a2, u2))
            P = {u2: P[u], s2: P[s], v2: P[u] + (P[s] - P[u]) * c2}
        else:
            c2 = corner_value(shapes[j], tets[j].etype(a2, s2))
            P = {s2: P[s], u2: P[u], v2: P[s] + (P[u] - P[s]) * c2}
    d, tr_, err = affine_from(start, P)
    return d, tr_, err


def identify_mu_lambda(tets, gl, shapes):
    """λ from the H₁ functional (the primitive cusp class dying in H₁(M)); μ₀ a Bézout
    complement, which is a meridian only up to the framing μ₀ ↦ μ₀ + kλ that homology cannot
    see. The frame is then pinned by `meridian_frame` (below). λ is oriented so that the developed
    cusp shape t_λ / t_μ has positive imaginary part — a frame-independent sign, since
    Im(τ/(1 − kτ)) has the sign of Im τ."""
    N = len(tets)
    classes = edge_classes(tets, gl)
    erows = edge_rows(tets, classes)
    cycles = find_cycles(tets, gl)
    hr = holonomy_rows(tets, gl, None, cycles)
    nt = nontrivial_cycles(erows, hr)
    assert len(nt) == 2, f"expected 2 independent cusp cycles, got {nt}"
    c1, c2 = cycles[nt[0]], cycles[nt[1]]
    r1, r2 = hr[nt[0]][0], hr[nt[1]][0]
    dual_edges, idx, d1, D2 = dual_spine(tets, gl)
    w = h1_functional(d1, D2)

    def phi_of(cyc):
        v = sp.Matrix(cycle_vector(tets, gl, idx, cyc, len(dual_edges)))
        assert (d1 * v).is_zero_matrix
        return (w.T * v)[0]

    a, b = phi_of(c1), phi_of(c2)
    den = sp.ilcm(sp.Rational(a).q, sp.Rational(b).q)
    a, b = int(a * den), int(b * den)
    g = gcd(a, b)
    a, b = a // g, b // g
    lam = (b, -a)
    x, y = _bezout(a, b)
    mu0 = (x, y)

    def combo_row(coefs, rows=(r1, r2)):
        A = [0] * N; B = [0] * N; s = 1
        for c, row in zip(coefs, rows):
            for j in range(N):
                A[j] += c * row[0][j]; B[j] += c * row[1][j]
            if row[2] == -1 and c % 2:
                s = -s
        return (A, B, s)

    _, t1, _ = cycle_translation(tets, gl, shapes, c1)
    _, t2, _ = cycle_translation(tets, gl, shapes, c2)
    t_lam = lam[0] * t1 + lam[1] * t2
    t_mu0 = mu0[0] * t1 + mu0[1] * t2
    if mp.im(t_lam / t_mu0) < 0:
        lam = (-lam[0], -lam[1]); t_lam = -t_lam
    # is (μ₀, λ) a basis of the translation lattice? Reduce the lattice of ALL fundamental
    # cycles' translations and express t_μ₀, t_λ in it.
    trans = []
    for cyc in cycles:
        _, t, _ = cycle_translation(tets, gl, shapes, cyc)
        if abs(t) > mp.mpf(10) ** -30:
            trans.append(t)
    b1 = min(trans, key=abs)
    b2 = min((t for t in trans if abs(mp.im(t / b1)) > mp.mpf(10) ** -20), key=abs)
    # Gauss reduction of (b1, b2)
    for _ in range(50):
        r = mp.nint(mp.re(b2 / b1))
        b2 = b2 - r * b1
        if abs(b2) < abs(b1):
            b1, b2 = b2, b1
        else:
            break
    # every translation must be an integer combination of (b1, b2)
    def coords(t):
        det = mp.re(b1) * mp.im(b2) - mp.im(b1) * mp.re(b2)
        xx = (mp.re(t) * mp.im(b2) - mp.im(t) * mp.re(b2)) / det
        yy = (mp.re(b1) * mp.im(t) - mp.im(b1) * mp.re(t)) / det
        return xx, yy
    all_int = all(abs(c - mp.nint(c)) < mp.mpf(10) ** -25 for t in trans for c in coords(t))
    xm, ym = coords(t_mu0); xl, yl = coords(t_lam)
    det_ml = mp.nint(xm) * mp.nint(yl) - mp.nint(ym) * mp.nint(xl)
    basis_ok = all_int and all(abs(c - mp.nint(c)) < mp.mpf(10) ** -25 for c in (xm, ym, xl, yl)) \
        and abs(det_ml) == 1
    return dict(erows=erows, classes=classes, c1=c1, c2=c2, r1=r1, r2=r2, phi=(a, b),
                lam=lam, lam_row=combo_row(lam), mu0=mu0, mu0_row=combo_row(mu0),
                tau0=t_lam / t_mu0, basis_ok=basis_ok, combo_row=combo_row)


def _curve_solver(tets, erows, lam_row):
    """Newton solver for the shapes at a prescribed λ-holonomy ℓ = e^s: the independent edge rows
    plus H(λ) = ℓ. Returns solve_at(s, z_guess) → shapes or None (degenerate / not converged)."""
    N = len(tets)
    zs = sp.symbols(f"y0:{N}")
    base, chosen = [], []
    for r in erows:
        trial = base + [list(r[0]) + list(r[1])]
        if sp.Matrix(trial).rank() > (sp.Matrix(base).rank() if base else 0):
            base = trial; chosen.append(r)
    chosen = chosen[:N - 1]
    lsym = sp.symbols("ell")
    eqs = [rect_expr(r, zs) - 1 for r in chosen] + [rect_expr(lam_row, zs) - lsym]
    f = sp.lambdify([*zs, lsym], eqs, "mpmath")

    def solve_at(s_, z_guess):
        ell = mp.exp(s_)
        try:
            sol = mp.findroot(lambda *v: f(*v, ell), z_guess, tol=mp.mpf(10) ** -40, maxsteps=40)
        except (ValueError, ZeroDivisionError, TypeError, IndexError):
            return None
        z = [sol[j] for j in range(N)]
        if any(abs(zj) < mp.mpf(10) ** -8 or abs(zj - 1) < mp.mpf(10) ** -8 or abs(zj) > mp.mpf(10) ** 8 for zj in z):
            return None
        if max(abs(e) for e in f(*z, ell)) > mp.mpf(10) ** -30:
            return None
        return z
    return solve_at


def discover_sheets(tets, erows, mu0_row, lam_row, found, known_starts, n_re=22, n_im=22):
    """Continue each found filling point (s, z) back to ℓ = 1 along a straight line in s; every
    distinct set of shapes reached at s = 0 is a new sheet of the ℓ-projection over the
    rectangle, and gets its own continuation grid (coarser than the first). Returns the new
    grids' points and the updated list of sheet start shapes."""
    solve_at = _curve_solver(tets, erows, lam_row)
    N = len(tets)
    new_pts, starts = [], list(known_starts)
    for (s_f, z_f) in found:
        z = list(z_f)
        ok = True
        for q in range(1, 9):
            zn = solve_at(s_f * (1 - mp.mpf(q) / 8), z)
            if zn is None:
                ok = False; break
            z = zn
        if not ok:
            continue
        if any(max(abs(z[j] - st[j]) for j in range(N)) < mp.mpf(10) ** -15 for st in starts):
            continue
        starts.append(list(z))
        new_pts.extend(sample_curve(tets, erows, mu0_row, lam_row, z, n_re=n_re, n_im=n_im))
    return new_pts, starts


def meridian_frame(tets, erows, mu0_row, lam_row, samples, k_range=range(-8, 9), seeds_per_k=10):
    """Pin the meridian among μ₀ + kλ. A solution of the gluing equations with all shapes
    nondegenerate is a nontrivial representation ρ : π₁(M) → PSL₂(ℂ). If H(μ₀ + kλ) = 1 while
    H(λ) ≠ 1, the cusp subgroup's image is abelian with a loxodromic element, so the element
    μ₀ + kλ, of eigenvalue ±1, is the identity in PSL₂(ℂ): ρ factors through the Dehn filling
    M(μ₀ + kλ), whose fundamental group is therefore nontrivial. The meridian filling is S³, so
    the meridian's frame k* is the unique k in range for which no such solution exists (that k*
    exists and is unique in any range uses Property P — Kronheimer–Mrowka 2004: no nontrivial
    surgery on a nontrivial knot has trivial π₁, ref [kronheimer2004]; only k* survives because
    every other frame is certified by an explicit solution).

    Search: `samples` is a continuation GRID over the curve in s = log H(λ) (see sample_curve),
    so g_k(s) = H(μ₀)(z(s))·e^{ks} − 1 is tabulated everywhere the grid reaches; from the grid
    points with the smallest |g_k| (away from ℓ = 1, where every frame vanishes at the complete
    point) an undeflated complex secant in s, with the shapes re-solved by continuation at each
    step, converges to the zero. Earlier variants failed for measurable reasons: four-variable
    Newton from random starts (0–4 hits per frame); seeds near the complete point (every frame
    fell onto it); a deflated target (the secant converged to the deflator's own zero — at ℓ = ∞
    for 1/(ℓ−1)², at ℓ = −3.7 for ((ℓ+3.7)/(ℓ−1))², linearly, while the genuine k = 0 roots of
    4₁ sit at ℓ = 0.374, 2.675 and four points on the unit circle). The absence at k* is checked
    exactly afterwards on the fitted A-polynomial (A(L, ±1) has no root off L = ±1)."""
    N = len(tets)
    solve_at = _curve_solver(tets, erows, lam_row)
    far = [t for t in samples if abs(t[1] ** 2 - 1) > mp.mpf("0.15")]
    table = {}
    found_all = []
    for k in k_range:
        def g(s_, z):
            return rect_eval(mu0_row, z) * mp.exp(k * s_) - 1
        ranked = sorted(far, key=lambda t: abs(t[0] * t[1] ** (2 * k) - 1))
        # distinct seeds: skip grid points within 0.3 (in s) of an already chosen one
        seeds = []
        for t in ranked:
            s_t = 2 * mp.log(-t[1])
            if all(abs(s_t - 2 * mp.log(-u[1])) > mp.mpf("0.3") for u in seeds):
                seeds.append(t)
            if len(seeds) >= seeds_per_k:
                break
        sols, lox = [], 0
        for (x0, L, z0) in seeds:
            s_a, z_a = 2 * mp.log(-L), list(z0)
            g_a = g(s_a, z_a)
            s_b = s_a + mp.mpc("0.02", "0.015")
            z_b = solve_at(s_b, z_a)
            if z_b is None:
                continue
            g_b = g(s_b, z_b)
            found = None
            for _ in range(60):
                if abs(g_b) < mp.mpf(10) ** -36:
                    found = (s_b, z_b); break
                if g_b == g_a:
                    break
                step = -g_b * (s_b - s_a) / (g_b - g_a)
                if abs(step) > mp.mpf("0.25"):
                    step = step / abs(step) * mp.mpf("0.25")
                s_n = s_b + step
                z_n = solve_at(s_n, z_b)
                tries = 0
                while z_n is None and tries < 4:
                    step = step / 2; s_n = s_b + step; z_n = solve_at(s_n, z_b); tries += 1
                if z_n is None:
                    break
                s_a, z_a, g_a = s_b, z_b, g_b
                s_b, z_b, g_b = s_n, z_n, g(s_n, z_n)
            if found is None:
                continue
            s_f, z_f = found
            if abs(mp.exp(s_f) - 1) < mp.mpf(10) ** -20:
                continue                       # a parabolic point: no certificate
            if any(max(abs(z_f[j] - s_[j]) for j in range(N)) < mp.mpf(10) ** -20 for s_ in sols):
                continue
            sols.append(z_f)
            found_all.append((s_f, z_f))
            lox += 1
        table[k] = (len(sols), lox)
    survivors = [k for k, (n, lox) in table.items() if lox == 0]
    return survivors, table, found_all


def _bezout(a, b):
    """x, y with a x + b y = gcd(a,b) = 1 (here)."""
    old_r, r = a, b
    old_s, s = 1, 0
    old_t, t = 0, 1
    while r:
        qq = old_r // r
        old_r, r = r, old_r - qq * r
        old_s, s = s, old_s - qq * s
        old_t, t = t, old_t - qq * t
    if old_r < 0:
        old_s, old_t = -old_s, -old_t
    return old_s, old_t


# ─────────────────────────────────────────────────────────────────────────────
# 3. Deformation-curve sampling and the A-polynomial
# ─────────────────────────────────────────────────────────────────────────────
def sample_curve(tets, erows, mu_row, lam_row, shapes0, n_samples=None, seed=1, n_re=34, n_im=34):
    """Continuation GRID over the deformation curve, parametrised by the λ-holonomy ℓ = H(λ) =
    e^s on the rectangle Re s ∈ [−3.4, 3.4] (|ℓ| ∈ [0.03, 30]), Im s ∈ (−π, π]. Starting at the
    complete structure (s = 0) the grid is walked as a snake — row Im s = 0 outwards, then row by
    row upwards, then again from s = 0 downwards — solving the independent edge rows and
    H(λ) = e^s for the shapes from the previous grid point, so every point lies on the sheet
    reached continuously from the complete structure. The developing map returns squared
    eigenvalues; L = −e^{s/2} is the continuous lift on the rectangle (ℓ never winds around 0
    inside it), with L = −1 at the complete point (the parabolic holonomy has trace −2 in SL₂;
    the other lift is L ↦ −L and is checked separately for the 4₁ control). Returns
    (H(μ_row), L, shapes) triples — all grid points, or a random subset of n_samples."""
    N = len(tets)
    solve_at = _curve_solver(tets, erows, lam_row)
    re_max = mp.mpf("3.4")
    re_vals = [re_max * (2 * i / (n_re - 1) - 1) for i in range(n_re)]
    re_vals = sorted(set(re_vals + [mp.mpf(0)]), key=lambda v: v)
    im_vals = [mp.pi * (2 * j / n_im - 1) + mp.pi / n_im for j in range(n_im)]   # symmetric about 0? no: half-offset
    im_vals = sorted(set([mp.mpf(0)] + im_vals), key=lambda v: v)
    i0 = re_vals.index(mp.mpf(0)); j0 = im_vals.index(mp.mpf(0))
    pts = []

    def walk(rows, start_z):
        """rows: list of (im, re-sequence) visited in order; continuation from start_z at s=0."""
        z = list(start_z)
        prev_s = mp.mpc(0)
        for (im, res) in rows:
            for re_ in res:
                s_ = mp.mpc(re_, im)
                # sub-step from prev_s to s_ in up to 3 pieces if the direct solve fails
                zn = solve_at(s_, z)
                if zn is None:
                    zt = z; ok = True
                    for q in (1, 2, 3):
                        st = prev_s + (s_ - prev_s) * mp.mpf(q) / 3
                        zt = solve_at(st, zt)
                        if zt is None:
                            ok = False; break
                    zn = zt if ok else None
                if zn is None:
                    continue                   # leave the point out; keep continuing from z
                z, prev_s = zn, s_
                pts.append((rect_eval(mu_row, z), -mp.exp(s_ / 2), list(z)))

    right = re_vals[i0:]; left = re_vals[:i0][::-1]
    # upward half: row j0 rightwards from 0, then leftwards from 0; then rows above, snaking
    walk([(im_vals[j0], right)], shapes0)
    walk([(im_vals[j0], left)], shapes0)
    # snake from s = 0 upward through the rows, then downward; right half-plane then left
    def snake(js):
        rows = []
        for n_, j in enumerate(js):
            seq = right if n_ % 2 == 0 else right[::-1]
            rows.append((im_vals[j], seq))
        return rows
    walk(snake(list(range(j0 + 1, len(im_vals)))), shapes0)
    walk(snake(list(range(j0 - 1, -1, -1))), shapes0)
    # left half-plane rows
    def snake_left(js):
        rows = []
        for n_, j in enumerate(js):
            seq = left if n_ % 2 == 0 else left[::-1]
            rows.append((im_vals[j], seq))
        return rows
    walk(snake_left(list(range(j0 + 1, len(im_vals)))), shapes0)
    walk(snake_left(list(range(j0 - 1, -1, -1))), shapes0)
    if n_samples is not None and len(pts) > n_samples:
        random.seed(seed)
        pts = random.sample(pts, n_samples)
    return pts


def fit_apoly(pts, max_dL=4, max_dx=8):
    """Smallest bidegree (dL, dx) in (L, x = M²) with a one-dimensional nullspace, integer
    coefficients, verified on all points."""
    for dL in range(1, max_dL + 1):
        for dx in range(1, max_dx + 1):
            monos = [(i, j) for i in range(dL + 1) for j in range(dx + 1)]
            if len(pts) < len(monos) + 8:
                continue
            A = mp.matrix([[x ** j * L ** i for (i, j) in monos] for (x, L, *_) in pts])
            U, S, V = mp.svd_c(A)
            svals = [S[k] for k in range(len(monos))]
            if svals[-1] < mp.mpf(10) ** -30 * svals[0] and svals[-2] > mp.mpf(10) ** -20 * svals[0]:
                vec = [V[len(monos) - 1, k] for k in range(len(monos))]
                # V is unitary: the null vector is the conjugate of the last row
                vec = [mp.conj(v) for v in vec]
                piv = max(range(len(vec)), key=lambda k: abs(vec[k]))
                vec = [v / vec[piv] for v in vec]
                for den in range(1, 64):
                    ints = [int(mp.nint(mp.re(v * den))) for v in vec]
                    if all(abs(v * den - ints[k]) < mp.mpf(10) ** -25 for k, v in enumerate(vec)):
                        g = 0
                        for c in ints:
                            g = gcd(g, abs(c))
                        ints = [c // g for c in ints]
                        poly = {(i, j): c for (i, j), c in zip(monos, ints) if c != 0}
                        return ("Lx", poly)
    return None


def newton_slopes(poly, var):
    """Edge slopes Δdeg_M / Δdeg_L of the Newton polygon. poly keys (i, j) are (deg_L, deg_x),
    x = M², so deg_M = 2 j."""
    pts = sorted(set((i, 2 * j) for (i, j) in poly))
    # convex hull (monotone chain)
    def cross(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
    lower, upper = [], []
    for p in pts:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    for p in reversed(pts):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    hull = lower[:-1] + upper[:-1]
    slopes = set()
    for k in range(len(hull)):
        (i1, j1), (i2, j2) = hull[k], hull[(k + 1) % len(hull)]
        if i2 != i1:
            slopes.add(Fr(j2 - j1, i2 - i1))
        else:
            slopes.add("inf")
    return hull, slopes


# ─────────────────────────────────────────────────────────────────────────────
def run_knot(knot, shapes_hint, check, wb):
    word, fb, ft, data = load_recorded(knot)
    tets, gl = rebuild(word, fb, ft)
    N = len(tets)
    shapes = [mp.mpmathify(str(s).replace(" ", "")) for s in data[f"{knot}_shapes"]] if f"{knot}_shapes" in data else shapes_hint
    info = identify_mu_lambda(tets, gl, shapes)
    print(f"\n[{knot}] word {word}, {N} tetrahedra; H₁ functional on the two cusp cycles: {info['phi']}")
    print(f"  λ = {info['lam']}·(c1,c2)  row a={info['lam_row'][0]} b={info['lam_row'][1]} sign={info['lam_row'][2]}")
    print(f"  μ₀ (Bézout) = {info['mu0']}·(c1,c2); (μ₀, λ) basis of the cusp lattice: {info['basis_ok']}")
    check(f"{knot}_mu0_lambda_is_a_lattice_basis", info["basis_ok"])
    grid = sample_curve(tets, info["erows"], info["mu0_row"], info["lam_row"], shapes)
    print(f"  continuation grid: {len(grid)} points on the deformation curve (μ₀ frame)")
    random.seed(11)
    pts0 = random.sample(grid, min(150, len(grid)))
    starts = [list(shapes)]
    union = list(grid)
    for rnd in range(4):
        survivors, table, found = meridian_frame(tets, info["erows"], info["mu0_row"], info["lam_row"], union)
        print(f"  frame search (round {rnd}, {len(starts)} sheet(s), {len(union)} grid points) "
              "k ↦ (solutions with H(μ₀+kλ)=1, of which loxodromic in λ): " +
              ", ".join(f"{k}:{v}" for k, v in table.items()))
        if len(survivors) <= 1:
            break
        new_pts, starts2 = discover_sheets(tets, info["erows"], info["mu0_row"], info["lam_row"], found, starts)
        if len(starts2) == len(starts):
            print("  no new sheets reached from the found filling points")
            break
        print(f"  sheet discovery: {len(starts2) - len(starts)} new sheet(s), {len(new_pts)} grid points")
        starts = starts2
        union.extend(new_pts)
    info["sheets"] = len(starts)
    check(f"{knot}_meridian_frame_unique", len(survivors) == 1, f"survivors {survivors}")
    if len(survivors) != 1:
        return None
    kstar = survivors[0]
    mu = (info["mu0"][0] + kstar * info["lam"][0], info["mu0"][1] + kstar * info["lam"][1])
    info["mu"] = mu; info["kstar"] = kstar; info["frame_table"] = table
    info["mu_row"] = info["combo_row"](mu)
    print(f"  meridian frame k* = {kstar}: μ = {mu}·(c1,c2)  row a={info['mu_row'][0]} b={info['mu_row'][1]} sign={info['mu_row'][2]}")
    # cusp shape in the (μ, λ) frame from the translations: t_μ = t_μ₀ + k* t_λ
    tau = info["tau0"] / (1 + kstar * info["tau0"])
    info["tau"] = tau
    print(f"  cusp shape t_λ/t_μ = {mp.nstr(tau, 20)}")
    rec = data.get(f"{knot}_cusp_modulus")
    if rec is not None:
        rec = mp.mpmathify(str(rec).replace(" ", ""))
        dtau = tau - rec
        ok_tau = abs(mp.im(dtau)) < mp.mpf(10) ** -25 and abs(mp.re(dtau) - mp.nint(mp.re(dtau))) < mp.mpf(10) ** -25
        check(f"{knot}_cusp_shape_from_mu_lambda_matches_recorded_mod_1", ok_tau,
              f"t_λ/t_μ − recorded = {mp.nstr(dtau, 8)}")
    hl = rect_eval(info["lam_row"], shapes); hm = rect_eval(info["mu_row"], shapes)
    check(f"{knot}_cusp_rows_trivial_at_complete", abs(hl - 1) < mp.mpf(10) ** -30 and abs(hm - 1) < mp.mpf(10) ** -30)
    # M² = M₀² / L^{2k*}: reuse the μ₀-frame samples in the meridian frame
    pts = [(x0 / L ** (2 * kstar), L, z) for (x0, L, z) in pts0]
    fit = fit_apoly(pts)
    check(f"{knot}_apoly_recovered", fit is not None)
    if fit is None:
        return None
    var, poly = fit
    Lsym, Msym = sp.symbols("L M")
    Aexpr = sum(c * Lsym ** i * Msym ** (2 * j) for (i, j), c in poly.items())
    Aexpr = sp.expand(Aexpr)
    print(f"  A(L, M) = {Aexpr}")
    # exact check at the complete point (holonomies 1): A(±1, ±1)
    vals = {(sL, sM): int(Aexpr.subs({Lsym: sL, Msym: sM})) for sL in (1, -1) for sM in (1, -1)}
    check(f"{knot}_apoly_vanishes_at_complete_point", any(v == 0 for v in vals.values()), f"A(±1,±1) = {vals}")
    # exact frame certificate on the polynomial: A(L, ±1) vanishes only at L = ±1
    only_pm1 = True
    for sM in (1, -1):
        pL = sp.Poly(Aexpr.subs(Msym, sM), Lsym)
        if pL.is_zero:
            continue
        rest = sp.factor_list(pL.as_expr())[1]
        for fac, _mult in rest:
            if sp.degree(fac, Lsym) > 0 and fac.as_poly(Lsym).degree() >= 1 and \
                    sp.simplify(fac / (Lsym - 1)).is_number is False and sp.simplify(fac / (Lsym + 1)).is_number is False:
                only_pm1 = False
    check(f"{knot}_apoly_at_M_pm1_has_roots_only_at_L_pm1", only_pm1,
          f"A(L,1) = {sp.factor(Aexpr.subs(Msym, 1))}, A(L,-1) = {sp.factor(Aexpr.subs(Msym, -1))}")
    # fresh-sample verification
    random.seed(23)
    fresh_pool = [t for t in grid if t not in pts0]
    fresh = [(x0 / L ** (2 * kstar), L, z) for (x0, L, z) in random.sample(fresh_pool, min(30, len(fresh_pool)))]
    resid = max(abs(sum(c * L ** i * x ** j for (i, j), c in poly.items())) for (x, L, *_) in fresh) if fresh else None
    scale = max(abs(c) for c in poly.values())
    check(f"{knot}_apoly_verified_on_fresh_samples", resid is not None and resid < mp.mpf(10) ** -28 * scale,
          f"max residual {mp.nstr(resid, 5) if resid is not None else None}")
    hull, slopes = newton_slopes(poly, var)
    print(f"  Newton polygon hull (deg_L, deg_M): {hull}; slopes Δdeg_M/Δdeg_L: {sorted(str(s) for s in slopes)}")
    wb.add_data(f"{knot}_lambda_row", list(info["lam_row"]))
    wb.add_data(f"{knot}_mu_row", list(info["mu_row"]))
    wb.add_data(f"{knot}_h1_functional_on_cycles", list(info["phi"]))
    wb.add_data(f"{knot}_meridian_frame_kstar", info["kstar"])
    wb.add_data(f"{knot}_sheets_searched", info["sheets"])
    wb.add_data(f"{knot}_meridian_frame_table", {str(k): list(v) for k, v in info["frame_table"].items()})
    wb.add_data(f"{knot}_mu_in_cycle_basis", list(info["mu"]))
    wb.add_data(f"{knot}_lambda_in_cycle_basis", list(info["lam"]))
    wb.add_data(f"{knot}_cusp_shape_lambda_over_mu", mp.nstr(info["tau"], 40))
    wb.add_data(f"{knot}_apoly", str(Aexpr))
    wb.add_data(f"{knot}_newton_hull", [list(p) for p in hull])
    wb.add_data(f"{knot}_newton_slopes", sorted(str(s) for s in slopes))
    return dict(info=info, Aexpr=Aexpr, poly=poly, var=var, slopes=slopes, hull=hull)


def main() -> int:
    from qou_substrate.witness import WitnessBuilder
    wb = WitnessBuilder("two-bridge-cusp-rows-apoly", engine="python", _script_path=__file__)
    wb.set_description(
        "Cusp rows (λ homologically, μ by Bézout) of the derived two-bridge triangulations of 4₁ and "
        "5₂, the A-polynomial recovered by sampling the deformation curve, and the Newton-polygon "
        "boundary slopes; 4₁ as control against the bundle-route A_{4₁}. Bean qou-yvyd.")
    wb.set_content_block("conj:stokes-dt-bps-bridge")
    ok_all = True

    def check(name, cond, note=""):
        nonlocal ok_all
        ok_all &= bool(cond)
        print(f"  [{'PASS' if cond else 'FAIL'}] {name} {note}")
        wb.add_assertion(name, computed="1" if cond else "0", expected="1", tolerance="0.5",
                         source="two_bridge_cusp_rows_apoly_probe")

    w6 = mp.exp(1j * mp.pi / 3)
    r41 = run_knot("fourone", [w6, w6], check, wb)
    Lsym, Msym = sp.symbols("L M")
    A41 = -Msym**4 + Lsym * (1 - Msym**2 - 2 * Msym**4 - Msym**6 + Msym**8) - Lsym**2 * Msym**4
    matched = False
    if r41:
        from itertools import product as iproduct
        for sL, eL, sM, eM in iproduct((1, -1), (1, -1), (1, -1), (1, -1)):
            g = sp.numer(sp.together(A41.subs({Lsym: sL * Lsym**eL, Msym: sM * Msym**eM}, simultaneous=True)))
            q = sp.simplify(sp.expand(r41["Aexpr"]) / sp.expand(g))
            if q.is_number and q != 0:
                matched = True
        check("fourone_apoly_matches_bundle_route_A41", matched, "homological μ,λ agree with the lattice-shape identification")
        check("fourone_slopes_pm4", {s for s in r41["slopes"] if s != "inf"} == {Fr(4), Fr(-4)},
              f"slopes {sorted(str(s) for s in r41['slopes'])}")

    r52 = run_knot("fivetwo", None, check, wb)
    if r52:
        S = sorted(int(s) if s.denominator == 1 else s for s in r52["slopes"] if s != "inf")
        check("fivetwo_slopes_integers", all(isinstance(v, int) for v in S), f"{S}")
        lit_pos, lit_neg = [0, 4, 10], [-10, -4, 0]
        check("fivetwo_slopes_are_0_4_10_up_to_mirror", S in (lit_pos, lit_neg),
              f"derived {S} in the (μ by the filling test, λ homological, Im(t_λ/t_μ) > 0) frame; "
              f"literature-recalled {{0, ±4, ±10}} (route_a probe / 2026-08-11 memo)")
        wb.add_data("fivetwo_boundary_slopes_derived", S)
        wb.add_data("fivetwo_chirality_note",
                    "Frame: λ = the cusp class dying in H₁(M); μ = the unique complement whose filling admits no "
                    "nondegenerate representation (Property P certificate, see meridian_frame); λ oriented so "
                    "Im(t_λ/t_μ) > 0 for the Im z > 0 solution. The sign of the "
                    "slopes then distinguishes the triangulated manifold from its mirror; which sign the "
                    "Rolfsen 5₂ carries in this frame is not held in a source here (the corpus's "
                    "{0,−4,−10} is literature-recalled with the same unverified sign).")

    wb.add_caveat("The 5₂ boundary slopes {0, ±4, ±10} are literature-recalled in the corpus, not held "
                  "in a source; the comparison is a consistency check on the derived Newton polygon, "
                  "not a derivation of the slopes from a held reference.")
    wb.add_caveat("The developing map returns squared eigenvalues; L is tracked by continuity from "
                  "L = −1 at the complete point along each continuation walk. The other lift is "
                  "L ↦ −L (checked for the 4₁ control); Newton-polygon slopes are unaffected.")
    wb.save({"q0Anchor": "independent",
             "q0AnchorReason": "pure topology/geometry: no q, no Markov parameter, no anchor"})
    print("\nALL PASS" if ok_all else "\nSOME FAIL")
    return 0 if ok_all else 1


if __name__ == "__main__":
    raise SystemExit(main())
