#!/usr/bin/env python3
# polynomial_q_not_applicable: mpmath at >= 60 dps for the algebraic seed, exact
# sympy for the counting section; audit-only falsifiability probe
# (compute-author 1.3), no witness, no fitted parameter, NO float64 anywhere.
"""Probe: C1 on the residue tower with the ACTUAL Sigma seed.  (bean `qou-an6y`)

CONTEXT.  #6628 (QOU.Mass.C1KernelLevelReading) made the symbol identification
of conj:qdifference-kernel-prolongation-symbol computable on the level axis:
for a derivative-only two-term tower D = c2(e) S_2 + c1(e) S_1 the residues
r_n = (D^n X)(-2) satisfy C1 from level 2,
      [n+2]_q r_{n+2} = r_{n+1} + r_n   (n >= 2),
iff the t^1-coefficients s_m = (D^m X)(1) satisfy the index-shifted C1.  With a
GENERIC seed that is always satisfiable by choosing the seed's tail, so the
content sits in the seed, which the geometry fixes: X = X0 + sum a_k t^k is the
Puiseux expansion of the colour cubic
      P(X, z) = X^3 + (z+1) X^2 + (z^2+z+1) X + (z^3+z^2+z+1)
at z = z_c + t^2, z_c a root of disc_X P, X0 the colliding double root -- the
simple branch zgeometric_ramification_parity_probe.py uses.

WHAT IS CHECKED:
  (1) The seed.  z_c, X0 from mp.polyroots at 80 dps; the Puiseux coefficients
      a_k by the order-by-order Newton step
         a_k = -[t^{k+1}] P(X0 + S_{k-1}(t), z_c + t^2) / (P_XX(X0,z_c) a_1),
      a_1^2 = -2 P_z / P_XX.  Verified by re-substituting: |P(X(t), z_c+t^2)|
      is O(t^{K+1}) to the working precision.
  (2) The two derivative-only candidates -- Jackson [e+1]_q S_1 + q-d/dz
      [e+2]_q S_2, balanced and geometric q-integers -- and their residue
      towers r_n, n = 0..8, at several exact rational q and at the proton q0.
      The C1 defect  d_n = [n+2]_q r_{n+2} - r_{n+1} - r_n  for n = 2..6.
      An identity in q must vanish at every q; a defect of order 1 at 60 dps
      is a scope-(a) negative for THAT candidate on THAT seed.
  (3) Both signs of a_1 (the two sheets of the cover) and both q-integer
      conventions.
  (4) COUNTING (exact sympy, generic symbolic seed and weights): per level,
      how many weight values c1(e), c2(e) appear in constraint m for the first
      time, against ONE constraint -- is the weight problem underdetermined?

Reproduce:
    PYTHONPATH=computations python3 -u computations/probes/c1_residue_tower_sw_seed_probe.py
"""
from __future__ import annotations

import sys as _sys
from pathlib import Path as _Path

import mpmath as mp
import sympy as sp

_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from qou_substrate.constants import Q_50_DIGIT_STR, Q_MP  # noqa: E402

mp.mp.dps = 80
K = 22   # Puiseux order kept


# ---------------------------------------------------------------- the seed
def ramification_point():
    X, z = sp.symbols("X z")
    P = X**3 + (z + 1) * X**2 + (z**2 + z + 1) * X + (z**3 + z**2 + z + 1)
    d = sp.Poly(sp.discriminant(P, X), z)
    cs = [mp.mpf(int(c)) for c in d.all_coeffs()]      # integer coefficients, exact
    zc = mp.polyroots(cs, maxsteps=400, extraprec=200)[0]
    a = [mp.mpf(1), zc + 1, zc**2 + zc + 1, zc**3 + zc**2 + zc + 1]
    rts = mp.polyroots(a, maxsteps=400, extraprec=200)
    Pp = lambda r: 3 * a[0] * r**2 + 2 * a[1] * r + a[2]
    X0 = min(rts, key=lambda r: abs(Pp(r)))
    # A double root of the cubic is determined by polyroots only to HALF the
    # working precision (~1e-41 at 80 dps): refine (X0, z_c) jointly on the
    # nonsingular 2x2 system P = P_X = 0 instead -- quadratic convergence to
    # full precision at a simple branch.
    Pf = lambda x, w: x**3 + (w + 1) * x**2 + (w**2 + w + 1) * x + (w**3 + w**2 + w + 1)
    PXf = lambda x, w: 3 * x**2 + 2 * (w + 1) * x + (w**2 + w + 1)
    X0, zc = mp.findroot([Pf, PXf], (X0, zc), tol=mp.mpf(10) ** (-75), maxsteps=60)
    return zc, X0, abs(PXf(X0, zc))


def poly_P(Xs, zs):
    """P as truncated series: Xs, zs lists of mpc coefficients in t (length K+2)."""
    def mul(u, v):
        out = [mp.mpc(0)] * len(u)
        for i, ui in enumerate(u):
            if ui == 0:
                continue
            for j, vj in enumerate(v):
                if i + j < len(out):
                    out[i + j] += ui * vj
        return out

    def add(u, v):
        return [ui + vi for ui, vi in zip(u, v)]

    def scal(c, u):
        return [c * ui for ui in u]

    one = [mp.mpc(1)] + [mp.mpc(0)] * (len(Xs) - 1)
    z1 = add(zs, one)
    z2 = mul(zs, zs)
    z3 = mul(z2, zs)
    X2 = mul(Xs, Xs)
    X3 = mul(X2, Xs)
    term2 = mul(z1, X2)
    term1 = mul(add(add(z2, zs), one), Xs)
    term0 = add(add(add(z3, z2), zs), one)
    return add(add(X3, term2), add(term1, term0))


def puiseux_seed(zc, X0, sign):
    L = K + 2
    zs = [mp.mpc(0)] * L
    zs[0] = mp.mpc(zc)
    zs[2] = mp.mpc(1)
    # derivatives at the branch
    PX = lambda x: 3 * x**2 + 2 * (zc + 1) * x + (zc**2 + zc + 1)
    PXX = 6 * X0 + 2 * (zc + 1)
    Pz = X0**2 + (2 * zc + 1) * X0 + (3 * zc**2 + 2 * zc + 1)
    a = [mp.mpc(0)] * L
    a[0] = mp.mpc(X0)
    a[1] = sign * mp.sqrt(-2 * Pz / PXX)
    for k in range(2, K + 1):
        Xs = list(a)
        Xs[k] = mp.mpc(0)
        val = poly_P(Xs, zs)
        # [t^{k+1}] with a_k = 0, then a_k = -val / (PXX * a1)
        a[k] = -val[k + 1] / (PXX * a[1])
    resid = poly_P(a, zs)
    tail = max(abs(c) for c in resid[: K + 1])
    return a, tail, PX(X0)


# ---------------------------------------------------------------- the towers
def qint_bal(q, m):
    return (q**m - q**(-m)) / (q - 1 / q)


def qint_geo(q, m):
    return (q**m - 1) / (q - 1)


def tower_residues(a, q, qi, nmax):
    """Jackson [e+1] S_1 + q-d/dz [e+2] S_2 on the seed dict; residues at -2."""
    f = {e: a[e] for e in range(len(a))}

    def D(g):
        out = {}
        lo = min(g) - 2
        hi = max(g)
        for e in range(lo, hi + 1):
            v = mp.mpc(0)
            if e + 2 in g:
                v += qi(q, e + 2) * g[e + 2]
            if e + 1 in g:
                v += qi(q, e + 1) * g[e + 1]
            if v != 0:
                out[e] = v
        return out

    rs, ss = [], []
    g = f
    for n in range(nmax):
        rs.append(g.get(-2, mp.mpc(0)))
        ss.append(g.get(1, mp.mpc(0)))
        g = D(g)
    return rs, ss


def main() -> int:
    fail: list[str] = []

    def ok(cond, msg):
        print(f"  [{'OK ' if cond else 'FAIL'}] {msg}")
        if not cond:
            fail.append(msg)

    print("=" * 78)
    print("(1) the seed: Puiseux expansion of the colour cubic at its simple branch")
    print("=" * 78)
    zc, X0, pxres = ramification_point()
    print(f"  z_c = {mp.nstr(zc, 12)}   X0 = {mp.nstr(X0, 12)}   |P_X(X0,z_c)| = {mp.nstr(pxres, 3)}")
    ok(pxres < mp.mpf(10) ** (-60), "genuine simple branch: |P_X(X0, z_c)| < 1e-60 at 80 dps")
    seeds = {}
    for sign in (1, -1):
        a, tail, _ = puiseux_seed(zc, X0, sign)
        seeds[sign] = a
        print(f"  sheet {sign:+d}: a_1 = {mp.nstr(a[1], 10)}, a_2 = {mp.nstr(a[2], 10)}, a_3 = {mp.nstr(a[3], 10)};  |P(X(t), z_c+t^2)| through t^{K} = {mp.nstr(tail, 3)}")
        ok(tail < mp.mpf(10) ** (-55), f"sheet {sign:+d}: re-substitution residual through t^{K} < 1e-55")
    ok(abs(seeds[1][2] - seeds[-1][2]) < mp.mpf(10) ** (-55), "a_2 is sheet-independent (even coefficients agree, odd flip sign)")

    print()
    print("=" * 78)
    print("(2)-(3) C1 defect d_n = [n+2]_q r_{n+2} - r_{n+1} - r_n on the residue tower")
    print("=" * 78)
    qs = [("11/10", mp.mpf(11) / 10), ("3/2", mp.mpf(3) / 2), ("2", mp.mpf(2)), ("q0 (proton)", Q_MP)]
    worst_any_pass = False
    for conv, qi in (("balanced", qint_bal), ("geometric", qint_geo)):
        for sign in (1, -1):
            a = seeds[sign]
            for qname, q in qs:
                rs, ss = tower_residues(a, q, qi, 10)
                d = [qi(q, n + 2) * rs[n + 2] - rs[n + 1] - rs[n] for n in range(2, 7)]
                scale = max(abs(x) for x in rs[2:9]) or mp.mpf(1)
                rel = [abs(x) / scale for x in d]
                mx = max(rel)
                print(f"  {conv:9s} sheet {sign:+d} q={qname:12s}: r_0={mp.nstr(rs[0],3)} r_1={mp.nstr(rs[1],3)} r_2={mp.nstr(rs[2],6)} r_3={mp.nstr(rs[3],6)};  max_n |d_n|/max|r| = {mp.nstr(mx, 4)}")
                if mx < mp.mpf(10) ** (-40):
                    worst_any_pass = True
            # r_0 = r_1 = 0 sanity (derivative-only)
        rs, _ = tower_residues(seeds[1], mp.mpf(3) / 2, qi, 3)
        ok(abs(rs[0]) == 0 and abs(rs[1]) == 0, f"{conv}: r_0 = r_1 = 0 (power-series seed, derivative-like shift 2)")
    ok(not worst_any_pass, "NO (convention, sheet, q) combination has the C1 defect below 1e-40: the Jackson + q-d/dz residue tower on the Sigma seed does NOT satisfy L_K from level 2 -- scope-(a) negative for these two candidates on this seed")

    print()
    print("=" * 78)
    print("(4) COUNTING: new weight unknowns per level vs one constraint (exact, generic)")
    print("=" * 78)
    q_s = sp.Symbol("q", positive=True)
    N = 16
    A = sp.symbols(f"a0:{N}")
    c1 = {e: sp.Symbol(f"c1_{'m' if e < 0 else ''}{abs(e)}") for e in range(-4, N + 4)}
    c2 = {e: sp.Symbol(f"c2_{'m' if e < 0 else ''}{abs(e)}") for e in range(-4, N + 4)}
    c1[-1] = sp.Integer(0)
    c2[-2] = sp.Integer(0)

    def seed(e):
        return A[e] if 0 <= e < N else sp.Integer(0)

    def Dsym(g):
        return lambda e: c2[e] * g(e + 2) + c1[e] * g(e + 1)

    def qgeo(m):
        return sp.cancel((q_s**m - 1) / (q_s - 1))

    g = seed
    s = []
    for m in range(7):
        s.append(sp.expand(g(1)))
        g = Dsym(g)
    seen = set()
    counts = []
    for m in range(4):
        eq = sp.expand(qgeo(m + 4) * s[m + 2] - s[m + 1] - s[m])
        syms = {x for x in eq.free_symbols if str(x).startswith("c")}
        new = syms - seen
        seen |= syms
        counts.append(len(new))
        lin = all(sp.degree(sp.Poly(eq, x)) == 1 for x in new)
        print(f"  level m={m}: constraint involves {len(syms)} weight values, {len(new)} of them NEW; new ones enter linearly: {lin}")
    ok(all(c >= 2 for c in counts), "every level introduces >= 2 new weight unknowns against ONE constraint: with free weights the level-axis identification is UNDERDETERMINED (it constrains nothing until the weights are fixed by geometry)")

    print()
    print("=" * 78)
    if fail:
        print(f"VERDICT: {len(fail)} FAILURE(S)")
        for m_ in fail:
            print("  -", m_)
        return 1
    print("VERDICT:")
    print("  * On the actual Sigma seed, neither Jackson + q-d/dz tower (balanced or")
    print("    geometric, either sheet) has a residue tower satisfying L_K from level 2")
    print("    at any tested q -- scope-(a): these two candidates, on this seed, alone.")
    print("  * With free weights the constraint is underdetermined level by level, so")
    print("    'symbol = L_K' has no content until D_q's weights come from the geometry.")
    print("  D_q is NOT constructed.")
    print("=" * 78)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
