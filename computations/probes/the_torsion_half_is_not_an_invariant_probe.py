#!/usr/bin/env python3
"""The torsion half is not an invariant: total torsion of a realisation of the
component knots varies freely along an isotopy, while the curvature half's
infimum `2π·b` is approached by the same family. So the fractional framing
scalar the hull exit needs cannot be an isotopy invariant of the closure —
which is why the substrate's fractional twist is algebraic.

WHERE THIS SITS IN THE THREAD
-----------------------------
`total_curvature_is_the_computable_half_probe` and
`the_canonical_closure_is_a_chain_of_torus_links_probe` (bean `qou-m3sh`) fixed
the curvature half exactly: every component of the canonical closure is a
`(2, 2g+1)`-torus knot, the bridge number is `2A+1`, and Milnor's infimum of
total curvature over the isotopy class is `2π(2A+1)`. The thread's refrain was
that the *other* half of Călugăreanu — the torsion, hence the twist — is what
the binding gap needs (`the_hull_exit_is_a_fractional_twist_probe`: a
fractional framing scalar in the window `e ∈ [0, 0.8897722518)`), and that the
osculating-circle picture is blind to it.

This probe says what that half can and cannot be, and measures it.

THE PRINCIPLE
-------------
For a closed space curve with a framing `F`, Călugăreanu–White–Fuller gives
`Lk_F = Wr + Tw_F` with `Lk_F ∈ ℤ`; for the Frenet framing `Tw_F = (1/2π)∮τ ds`.
`Lk_F` is an invariant of the framed isotopy class; `Wr` and `∮τ ds` are not
invariants of anything — a small helical perturbation of any arc changes the
total torsion by an arbitrary amount while preserving the isotopy class. The
infimum of total *curvature* over the isotopy class IS an invariant (Milnor:
`2π·b`); the total *torsion* has no such extremal invariant. Hence:

  * an isotopy-invariant "fractional twist" of the closure does not exist;
  * whatever fractional framing datum the substrate carries is a property of
    the algebra (`q^{2c(λ)/n}`, `can_the_substrate_carry_a_fractional_twist`),
    or of a canonical *embedding* (a Möbius-energy or ropelength minimiser),
    never of the knot type.

That is the honest closure of the "missing half" question inside this thread:
the half the geometry can supply invariantly is exactly the half we already
have, and it is not the one the binding gap needs.

THE MEASUREMENT
---------------
Standard torus embedding of `T(2, q)`, `q ∈ {3, 5, 7}`, major radius `R = 1`,
tube radius `r ∈ {0.45, 0.30, 0.18, 0.10, 0.05, 0.02}`:

    γ(t) = ((R + r cos qt) cos 2t, (R + r cos qt) sin 2t, r sin qt),  t ∈ [0, 2π).

With mpmath quadrature at 24 dps (no float64 in the hot path):

  * `κ_min` over the curve — the Frenet frame is a global framing iff it is `> 0`;
  * total curvature `∫κ ds`, against Milnor's floor `2π·b = 4π`;
  * total torsion `∮τ ds` and the Frenet twist `Tw_F = ∮τ ds / 2π`;
  * the writhe `Wr` — the Gauss double integral in coordinates `(t, u = s − t)`,
    trapezoid in the periodic `t`, Gauss–Legendre panels in `u` refined toward the
    three sharp features (`u = π`, where the second strand passes at distance
    exactly `2r`; `u → 0, 2π`, where the next complex zero of `|γ(t+u) − γ(t)|²`
    sits at `|u| ≈ 2/(r q²)`);
  * `Lk_F = Wr + Tw_F`, which must be an integer — the check on the numerics,
    cross-checked once against the push-off linking integral `Lk(γ, γ + εN)`.

FOUND
-----
  * `∫κ ds` decreases monotonically to `4π`: `∫κ/4π` runs `1.34 → 1.0003`
    (`q = 3`), `2.26 → 1.003` (`q = 5`), `3.27 → 1.014` (`q = 7`) from
    `r = 0.45` to `0.02`. The infimum is approached, never attained — at `r = 0`
    the curve is the doubly covered core circle, not a knot.
  * `∮τ ds` and `Wr` both move with `r` (spreads `> 1` and `> 0.1` in every
    family). The fractional part of `Wr` — the only "fractional twist" a
    geometric realisation offers — is a smooth function of `r`.
  * `Wr + Tw_F` is an integer at every `r` (Călugăreanu holds) — **but the
    integer is not constant.** `Lk_F = −2q` on the fat side and `−q` on the thin
    side of `r* = 4/(q² + 4)` (`4/13, 4/29, 4/53`). At `t = π/q` the curvature
    vanishes exactly when `q² r = 4(1 − r)`:

        γ'(π/q) × γ''(π/q) = (q² r − 4(1 − r)) · (q r s, −q r c, −2(1 − r)),
        c = cos(2π/q), s = sin(2π/q),

    and `cos qt = −1` at the `q` parameters `(2k+1)π/q`, so the family crosses
    `q` inflection points at once, the Frenet normal flips at each, and the
    Frenet self-linking jumps by `q`. The factorisation is exact (sympy, §I) and
    the algebra is in Lean (`QOU/Mass/TorusInflection.lean`). So even the
    integer half of Călugăreanu is a property of the *curve*: the Frenet framing
    is not a framing of the knot type, and no framing datum — fractional or
    integral — comes from the geometry of the isotopy class alone.

WHAT IS NOT CLAIMED
-------------------
No comparison of any geometric torsion number with the substrate's window is
made, because the principle above says such a comparison has no invariant
meaning. No canonical embedding is chosen. Nothing about binding. That the
`t = π/q` inflections are the only ones in the family is observed (`κ_min`
sampled on 720 points, positive at every listed `r`), not proved.
"""
from __future__ import annotations

import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE.parent / "substrate"))
import _path_bridge  # noqa: F401,E402

import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402

mp.mp.dps = 24
M_TRAP = 160        # trapezoid nodes in t for the writhe (periodic direction: spectral)
GL_DEGREE = 4       # mpmath Gauss–Legendre degree per u-panel: 3·2^(m-1) = 24 nodes
N_KAPPA = 720       # sample points for the curvature minimum (Frenet frame global?)
FAMILY = [mp.mpf(s) for s in ("0.45", "0.30", "0.18", "0.10", "0.05", "0.02")]
WINDOW_HI = "0.8897722518"   # the hull-exit window, quoted for the record only


def curve_funcs(q: int):
    """Symbolic γ, γ', γ'', γ''' for T(2,q) on the torus (R=1, r symbolic)."""
    t, r = sp.symbols("t r", real=True)
    R = 1
    g = sp.Matrix([(R + r * sp.cos(q * t)) * sp.cos(2 * t),
                   (R + r * sp.cos(q * t)) * sp.sin(2 * t),
                   r * sp.sin(q * t)])
    g1, g2, g3 = g.diff(t), g.diff(t, 2), g.diff(t, 3)
    f = {k: sp.lambdify((t, r), v, "mpmath") for k, v in
         (("g", g), ("g1", g1), ("g2", g2), ("g3", g3))}
    return f


def vec(m):
    return [mp.mpf(m[i]) for i in range(3)]


def cross(a, b):
    return [a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0]]


def dot(a, b):
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]


def norm(a):
    return mp.sqrt(dot(a, a))


def kappa_at(f, r, t):
    g1, g2 = vec(f["g1"](t, r)), vec(f["g2"](t, r))
    return norm(cross(g1, g2)) / norm(g1) ** 3


def kappa_min(f, r, n=N_KAPPA):
    """Sampled minimum of κ. Positive ⟹ the Frenet frame is a global framing,
    which is what makes `Wr + (1/2π)∮τ ds` an integer in the first place."""
    return min(kappa_at(f, r, 2 * mp.pi * i / n) for i in range(n))


def total_curvature_torsion(f, r):
    # A first draft wrote κ|γ'| as |γ'×γ''|/|γ'|² · |γ'|, one power of the speed
    # too many: it inflated every ∫κ ds by ≈ |γ'| ≈ 2 and no family approached
    # 4π. κ = |γ'×γ''|/|γ'|³, so κ ds = |γ'×γ''|/|γ'|² dt.
    def kappa_ds(t):
        g1, g2 = vec(f["g1"](t, r)), vec(f["g2"](t, r))
        return norm(cross(g1, g2)) / norm(g1) ** 2                # κ · |γ'|

    def tau_ds(t):
        g1, g2, g3 = vec(f["g1"](t, r)), vec(f["g2"](t, r)), vec(f["g3"](t, r))
        c = cross(g1, g2)
        return dot(c, g3) / dot(c, c) * norm(g1)                # τ · |γ'|

    # κ dips to ~0.04 at (q=3, r=0.3) and the torsion integrand peaks there
    # (|γ'×γ''|² in the denominator). Eight uniform panels left a 3e-5 residual
    # in Wr + Tw_F; putting a panel boundary AT each local minimum of κ, where
    # tanh-sinh clusters its nodes, resolves the peak to working precision.
    pts = _breakpoints(f, r)
    K = mp.quad(kappa_ds, pts)
    T = mp.quad(tau_ds, pts)
    return K, T


def _breakpoints(f, r, n=N_KAPPA):
    """Eight uniform panel boundaries plus every local minimum of |γ'×γ''|²,
    located by a bracketed root of its derivative 2(γ'×γ'')·(γ'×γ''')."""
    def c2(t):
        g1, g2 = vec(f["g1"](t, r)), vec(f["g2"](t, r))
        c = cross(g1, g2)
        return dot(c, c)

    def dc2(t):
        g1, g2, g3 = vec(f["g1"](t, r)), vec(f["g2"](t, r)), vec(f["g3"](t, r))
        return 2 * dot(cross(g1, g2), cross(g1, g3))

    grid = [2 * mp.pi * i / n for i in range(n)]
    vals = [c2(t) for t in grid]
    mins = []
    for i in range(n):
        if vals[i] < vals[i - 1] and vals[i] < vals[(i + 1) % n]:
            a, b = grid[i] - 2 * mp.pi / n, grid[i] + 2 * mp.pi / n
            try:
                t_star = mp.findroot(dc2, (a, b), solver="illinois")
            except Exception:
                t_star = grid[i]
            t_star = t_star % (2 * mp.pi)
            mins.append(t_star)
    pts = sorted(set([2 * mp.pi * k / 8 for k in range(9)] + mins))
    return pts


def _gl_panel(a, b, m=GL_DEGREE):
    """Gauss–Legendre nodes and weights on [a, b] (mpmath degree m → 3·2^(m-1) nodes)."""
    from mpmath.calculus.quadrature import GaussLegendre
    pts = GaussLegendre(mp.mp).calc_nodes(m, mp.mp.prec)
    h = (b - a) / 2
    return [(a + h * (x + 1), h * w) for x, w in pts]


def _u_rule():
    """Quadrature in u = s - t on (0, 2π).

    The Gauss integrand F(s, t) is smooth off the diagonal and has a |s - t| kink
    ON it, so a product rule straddling the diagonal converges only algebraically.
    In (t, u) coordinates u ∈ (0, 2π) never crosses it: F(t, t+u) is analytic in u
    on the open interval, vanishing linearly at both ends. Two sharp features:

      * u = π, where the second strand of T(2, q) passes at distance exactly 2r
        (|γ(t+π) - γ(t)|² = 4r² identically), complex singularity at u ≈ π ± i r/2;
      * u → 0 and u → 2π, where |γ(t+u) - γ(t)|² = u²(|γ'|² + …) has its next
        complex zero at |u| ≈ 2/(r q²) — 0.09 for (q, r) = (7, 0.45).

    Panels are refined geometrically toward all three, down to 1/1024. A first
    draft refined toward π only and left Wr + Tw_F short of an integer by 4e-4
    at (7, 0.45) while every single-direction refinement left the value
    unchanged; the push-off linking integral Lk(γ, γ + εN), computed
    independently, sits on -14 to 7e-9, and so does Wr + Tw_F once the ends are
    refined (4e-8 with 1/256, better with 1/1024)."""
    pi = mp.pi
    offs_desc = [mp.mpf(1) / 4 ** k for k in range(6)]      # 1, 1/4, ..., 1/1024
    offs_asc = list(reversed(offs_desc))
    brk = ([mp.mpf(0)] + offs_asc                                # 0, 1/1024, ..., 1
           + [pi - o for o in offs_desc] + [pi]                  # π-1, ..., π-1/1024, π
           + [pi + o for o in offs_asc]                          # π+1/1024, ..., π+1
           + [2 * pi - o for o in offs_desc] + [2 * pi])         # 2π-1, ..., 2π-1/1024, 2π
    assert all(a < b for a, b in zip(brk, brk[1:]))
    rule = []
    for a, b in zip(brk, brk[1:]):
        rule += _gl_panel(a, b)
    return rule


def inflection_symbolic():
    """γ' × γ'' at t = π/q, exactly, for q = 3, 5, 7: every component carries the
    factor (q² + 4) r − 4, so κ(π/q) = 0 iff r = 4/(q² + 4). Returns the r* values
    and whether the factor is common to all three components at each q."""
    t, r = sp.symbols("t r", real=True)
    out = {}
    for q in (3, 5, 7):
        g = sp.Matrix([(1 + r * sp.cos(q * t)) * sp.cos(2 * t),
                       (1 + r * sp.cos(q * t)) * sp.sin(2 * t), r * sp.sin(q * t)])
        c = sp.simplify(g.diff(t).cross(g.diff(t, 2)).subs(t, sp.pi / q))
        fac = (q ** 2 + 4) * r - 4
        # fac divides every component as a polynomial in r iff the cancelled
        # quotient has a purely numerical denominator
        common = all(sp.fraction(sp.cancel(ci / fac))[1].is_number for ci in c)
        out[q] = (sp.Rational(4, q ** 2 + 4), common, [sp.factor(ci) for ci in c])
    return out


def writhe(f, r, m_trap=M_TRAP):
    """Wr = (1/4π) ∫₀^{2π} dt ∫₀^{2π} du F(t, t+u), F the Gauss integrand.

    Outer integral: trapezoid on the periodic t (spectral for an analytic
    periodic integrand); inner: the panelled Gauss–Legendre rule of `_u_rule`."""
    rule = _u_rule()
    P = [vec(f["g"](t, r)) for t in (2 * mp.pi * i / m_trap for i in range(m_trap))]
    D = [vec(f["g1"](t, r)) for t in (2 * mp.pi * i / m_trap for i in range(m_trap))]
    acc = mp.mpf(0)
    for i in range(m_trap):
        t = 2 * mp.pi * i / m_trap
        inner = mp.mpf(0)
        for u, w in rule:
            s = t + u
            Ps, Ds = vec(f["g"](s, r)), vec(f["g1"](s, r))
            d = [Ps[k] - P[i][k] for k in range(3)]
            inner += w * dot(cross(Ds, D[i]), d) / norm(d) ** 3
        acc += inner
    return acc * (2 * mp.pi / m_trap) / (4 * mp.pi)


def main() -> int:
    checks: list[tuple[str, bool]] = []

    def check(name, ok):
        checks.append((name, bool(ok)))
        print(f"  [{'ok ' if ok else 'FAIL'}] {name}")

    print(__doc__.split("\n")[0])
    print(f"\nmpmath dps {mp.mp.dps}; writhe: trapezoid × panelled Gauss–Legendre in (t, u), "
          f"{M_TRAP} × {len(_u_rule())} nodes")
    results = {}
    worst_lk = mp.mpf(0)
    t_start = time.time()
    for q in (3, 5, 7):
        f = curve_funcs(q)
        print("\n" + "=" * 72)
        print(f"T(2,{q}) on the torus R = 1, bridge number 2, Milnor floor 2π·2 = {mp.nstr(4*mp.pi, 12)}")
        print("=" * 72)
        print("    r     κ_min     ∫κ ds       ∫κ/4π      ∮τ ds       Tw_F        Wr         Wr+Tw_F     frac(Wr)")
        rows = []
        for r in FAMILY:
            t0 = time.time()
            km = kappa_min(f, r)
            K, T = total_curvature_torsion(f, r)
            W = writhe(f, r)
            Tw = T / (2 * mp.pi)
            Lk = W + Tw
            frac = W - mp.floor(W)
            rows.append((r, km, K, T, Tw, W, Lk, frac))
            worst_lk = max(worst_lk, abs(Lk - mp.nint(Lk)))
            print(f"  {mp.nstr(r, 3):>5s}  {mp.nstr(km, 4):>6s}  {mp.nstr(K, 10):>11s}  {mp.nstr(K/(4*mp.pi), 8):>9s}  "
                  f"{mp.nstr(T, 8):>10s}  {mp.nstr(Tw, 8):>10s}  {mp.nstr(W, 8):>10s}  "
                  f"{mp.nstr(Lk, 10):>12s}  {mp.nstr(frac, 6)}   ({time.time() - t0:.0f}s)", flush=True)
        results[q] = rows
        check(f"T(2,{q}): κ > 0 on the whole family — the Frenet frame is a global framing",
              all(row[1] > 0 for row in rows))
        lk_int = all(abs(row[6] - mp.nint(row[6])) < mp.mpf("1e-7") for row in rows)
        check(f"T(2,{q}): Wr + Tw_F is an integer at every r to 1e-7 (Călugăreanu, numerically)", lk_int)
        r_star = mp.mpf(4) / (q * q + 4)
        jump_ok = all((mp.nint(row[6]) == (-2 * q if row[0] > r_star else -q)) for row in rows)
        check(f"T(2,{q}): Lk_F = -{2*q} for r > 4/(q²+4) = {mp.nstr(r_star, 6)} and -{q} below it "
              f"— the Frenet self-linking JUMPS by q across the inflection radius", jump_ok)
        Ks = [row[2] for row in rows]
        check(f"T(2,{q}): ∫κ ds decreases monotonically toward 4π as r → 0 and stays above it",
              all(Ks[i] > Ks[i + 1] for i in range(len(Ks) - 1)) and all(K > 4 * mp.pi for K in Ks))
        check(f"T(2,{q}): ∫κ ds comes within 5 % of Milnor's floor at the smallest r",
              Ks[-1] / (4 * mp.pi) < mp.mpf("1.05"))
        Ts = [row[3] for row in rows]
        check(f"T(2,{q}): total torsion is not constant along the family (spread > 1)",
              max(Ts) - min(Ts) > 1)
        Ws = [row[5] for row in rows]
        check(f"T(2,{q}): the writhe is not constant along the family either (spread > 0.1)",
              max(Ws) - min(Ws) > mp.mpf("0.1"))
    print(f"\n  worst |Lk_F - nint(Lk_F)| over all 18 rows: {mp.nstr(worst_lk, 3)}   "
          f"(total {time.time() - t_start:.0f}s)")

    print("\n" + "=" * 72)
    print("§I  THE INFLECTION RADIUS, EXACTLY: κ(π/q) = 0 ⟺ r = 4/(q² + 4)")
    print("=" * 72)
    sym = inflection_symbolic()
    infl_ok = True
    for q, (r_star, common, comps) in sym.items():
        f = curve_funcs(q)
        k_at = kappa_at(f, mp.mpf(r_star.p) / r_star.q, mp.pi / q)
        print(f"  q = {q}: γ'×γ'' at t = π/q has the common factor ({q*q+4})r - 4  [{common}]"
              f"   r* = {r_star} = {mp.nstr(mp.mpf(r_star.p)/r_star.q, 8)}   κ(π/q; r*) = {mp.nstr(k_at, 3)}")
        print(f"         components: {comps}")
        infl_ok &= common and k_at < mp.mpf("1e-15")
    check("γ'×γ'' at t = π/q carries the factor (q²+4)r − 4 for q = 3, 5, 7 (sympy, exact), "
          "and κ(π/q; 4/(q²+4)) vanishes to 1e-15", infl_ok)
    print("  general q (substituting cos qt = -1, sin qt = 0, ρ = 1 - r):")
    print("    γ'(π/q) = (-2ρ s, 2ρ c, -q r),  γ''(π/q) = ((q² r - 4ρ) c, (q² r - 4ρ) s, 0),")
    print("    γ'×γ'' = (q² r - 4ρ)·(q r s, -q r c, -2ρ(c² + s²))   — Lean: QOU.Mass.TorusInflection")
    print("  cos(qt) = -1 at the q parameters t_k = (2k+1)π/q, so the family crosses q inflections")
    print("  at once and the Frenet self-linking jumps by q: -2q on the fat side, -q on the thin side.")

    print("\n" + "=" * 72)
    print("§Σ  WHAT THE TWO HALVES ARE WORTH")
    print("=" * 72)
    print("  curvature: an isotopy-invariant infimum, 2π·b, approached along the family — HAVE IT")
    print("  torsion:   no invariant; ∮τ ds and Wr move with r; Wr + Tw_F is an integer at every r")
    print("             but even that integer is a property of the CURVE — it jumps by q at r = 4/(q²+4)")
    print(f"  the hull-exit window e ∈ [0, {WINDOW_HI}) is therefore not a property of the knot")
    print("  type; the substrate's fractional twist is algebraic, q^(2c(λ)/n), or nothing.")

    try:
        from witness_base import WitnessBuilder  # noqa: E402

        wb = WitnessBuilder(Path(__file__).stem, engine="mpmath")
        wb.set_description(
            "The torsion half of Calugareanu is not an isotopy invariant, the "
            "curvature half's infimum is. Standard torus embeddings of T(2,3), "
            "T(2,5), T(2,7) along a family r -> 0: total curvature decreases "
            "toward Milnor's floor 4*pi (bridge number 2) and stays above it; "
            "total torsion and writhe vary across the family while Wr + Tw_F "
            "is an integer at every r. Hence the fractional framing scalar the "
            "hull exit needs cannot be an isotopy invariant of the closure; the "
            "substrate's fractional twist is algebraic or nothing. mpmath "
            "quadrature at 24 dps, no float64 in the hot path.")
        for q, rows in results.items():
            for r, km, K, T, Tw, W, Lk, frac in rows:
                tag = f"T2{q}_r{mp.nstr(r, 3).replace('.', 'p')}"
                wb.add_data(f"{tag}_kappa_min", mp.nstr(km, 8))
                wb.add_data(f"{tag}_total_curvature", mp.nstr(K, 15))
                wb.add_data(f"{tag}_total_torsion", mp.nstr(T, 15))
                wb.add_data(f"{tag}_writhe", mp.nstr(W, 15))
                wb.add_data(f"{tag}_Lk_Frenet", mp.nstr(Lk, 12))
        wb.add_data("worst_Lk_integrality_residual", mp.nstr(worst_lk, 3))
        for name, ok in checks:
            wb.add_assertion(name=name, computed=str(int(ok)), expected="1")
        wb.add_caveat(
            "The torus embedding is a convenience, not a canonical realisation; "
            "every torsion and writhe number here is a property of that "
            "embedding and of r, which is the point being made. A canonical "
            "embedding (Mobius-energy or ropelength minimiser) would give "
            "canonical numbers, and would still not give an isotopy invariant.")
        wb.add_caveat(
            "Writhe is a trapezoid x panelled Gauss-Legendre double integral in "
            "(t, u = s - t) coordinates, checked only through the integrality of "
            "Wr + Tw_F (residual reported as worst_Lk_integrality_residual); its "
            "absolute accuracy is well below the 24-dps working precision of the "
            "single integrals.")
        wb.add_caveat(
            "Per component only. A realisation of the whole chain link is not "
            "constructed; the principle does not depend on it.")
        print(f"\nWitness: {wb.save({"q0Anchor": "independent", "q0AnchorReason": "q0_independence_checker: the fully-resolved import cone reads no q0 and the source carries no q0-shaped literal"})}")
    except Exception as e:  # pragma: no cover
        print(f"\n(witness emit skipped: {e})")

    bad = [n for n, ok in checks if not ok]
    print(f"\n{len(checks) - len(bad)}/{len(checks)} checks passed")
    return 1 if bad else 0


if __name__ == "__main__":
    raise SystemExit(main())
