#!/usr/bin/env python3
"""
graded_reference_simplex_basis_span_probe — the coordination-simplex basis the
residual decomposition uses cannot represent the graded reference it is
decomposing. Exact at the three points that pin it, off by 142x by A=8.

Bean `qou-brng`, arc `bk-crossing-mass-binding`. Companion to
`gs_tower_jet_degree_body_order_probe` (same PR); the two findings are one
finding seen from two sides.

## What the corpus does

`deltalambda_kappa_interface_residual_simplex_probe` (#4316/#4320) takes the
damping-wall residual

    M(A) = rho_strong(A) - rho_grad(A),   rho_grad(A) = [A]_q! / [2]_q!

and expands it in the derived coordination-graph counts as basis:

    M(A) = mu_2*C(A,2) + mu_3*C(A,3) + mu_4*C(A,4)

Three points A = 2,3,4 give three coefficients, so the solve is EXACT and
0-free-parameter -- the probe says so, and correctly insists this is not a fit.
`helium_four_body_cluster_probe` then records `mu_4 = s_4 - g_4` where
`g_4 = +8.37` is "the graded reference's own 4-body simplex coefficient", i.e.
the corpus already expands `rho_grad` in this same basis.

## What is measured here

Expand `rho_grad` ALONE in that basis -- no AME, no `rho_strong`, no empirical
input of any kind, so nothing here can be a fit -- pin `(g_2,g_3,g_4)` on
A = 2,3,4, and then ask the only question a 0-freedom solve leaves open: does it
hold at A = 5?

    A    true rho_grad     simplex prediction    ratio
    2         1.0                1.0             1.0        <- pinned
    3         3.342031037        3.342031037     1.0        <- pinned
    4        15.73957214        15.73957214      1.0        <- pinned
    5        98.01875404        55.27755031      0.5639
    6       775.5666987        147.4123406       0.1901
    7      7587.081858         325.9717659       0.04296
    8     89971.48231          633.1550972       0.007037

By A=8 the basis reproduces 0.7 % of the object it is supposed to decompose.

The cross-check that says this is the corpus's own object and not a lookalike:
the solve returns `g_4 = 8.371447988`, reproducing the `+8.37` quoted in
`helium_four_body_cluster_probe`'s docstring to the precision it is quoted at.
`g_2 = 1` exactly, forced by `rho_grad(2) = 1` with `C(2,3) = C(2,4) = 0`.

## Why -- and why it is the same finding as the tower probe

`rho_grad(A) = [A]_q!/[2]_q!` grows factorially in A; `C(A,2), C(A,3), C(A,4)`
are polynomials in A of degree at most 4. No finite polynomial basis tracks a
factorial, so divergence is structural rather than numerical.

The companion probe measures the mechanism directly: the graded dimension's
degree range is `0..C(A,2)`, and at the proton pin its coefficient mass migrates
into the high degrees as A grows -- 20.9 % above degree A at A=4, 96.1 % at A=8.
The basis fails exactly where the mass goes.

## What follows, and what does not

Follows: the `mu_k` are an exact re-expression AT A = 2,3,4 and carry no
information about the object away from those points. In particular `mu_4 < 0` is
a statement about A = 4; it may not be read as "the 4-body cluster coefficient is
negative" as a general fact, because the basis carrying it demonstrably does not
extend.

Does NOT follow, and must not be written down:

  * That #4316/#4320 is a fit. It is not, and the probe is careful to say so --
    a 3-point solve for 3 coefficients has no freedom to fit WITH. The defect is
    in the basis's span, which is a different and weaker charge.
  * That the sign pattern (mu_2 = 0, mu_3 > 0, mu_4 < 0) is wrong. Those are
    correct arithmetic at their three points. The corpus's own framing already
    says "the CONTENT is which coefficients are non-zero" rather than their
    values; this probe says the sign pattern inherits the same restriction to
    A <= 4 that the values do.
  * Any claim about `rho_strong`. It is not touched here.

Scope **(a)**. Nothing wired, no closure proposed, no replacement basis offered.

NO FLOAT64: exact integer coefficients from sympy, exact `math.comb` counts, all
arithmetic in mpmath `mpf` at 50 dps against the 50-digit proton pin. `float`
appears nowhere.
"""

from __future__ import annotations

import sys as _sys
from pathlib import Path as _Path

_sys.path.insert(0, str(_Path(__file__).resolve().parent))
import _path_bridge as _bridge  # noqa: E402, F401

from math import comb  # noqa: E402

import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402

from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402

mp.mp.dps = 50

A_MAX = 8
PIN = (2, 3, 4)                    # the three points the simplex solve uses
_q = sp.symbols("q")


def rho_grad(A: int, q0):
    """[A]_q!/[2]_q! at the pin, from exact integer Mahonian coefficients."""
    poly = sp.Poly(
        sp.expand(sp.prod([sum(_q**i for i in range(k)) for k in range(1, A + 1)])),
        _q,
    )
    coeffs = [int(c) for c in poly.all_coeffs()[::-1]]
    return mp.fsum([mp.mpf(v) * q0**l for l, v in enumerate(coeffs)]) / (1 + q0)


def C(A: int, k: int):
    return mp.mpf(comb(A, k))


def fmt(x, n=8):
    return mp.nstr(x, n)


def main() -> int:
    q0 = Q_MP
    print("graded_reference_simplex_basis_span_probe")
    print("=" * 78)
    print(f"q0 (50-digit proton pin) = {fmt(q0, 20)}")
    print()
    print("THE SOLVE.  rho_grad(A) = g2*C(A,2) + g3*C(A,3) + g4*C(A,4), pinned on")
    print(f"  A = {PIN}.  Three points, three coefficients: EXACT, no freedom.")
    print("  No AME, no rho_strong, no empirical input -- this cannot be a fit.")
    print()

    truth = {A: rho_grad(A, q0) for A in range(2, A_MAX + 1)}
    mat = mp.matrix([[C(A, 2), C(A, 3), C(A, 4)] for A in PIN])
    g = mp.lu_solve(mat, mp.matrix([truth[A] for A in PIN]))
    print(f"  g2 = {fmt(g[0], 12)}   g3 = {fmt(g[1], 12)}   g4 = {fmt(g[2], 12)}")
    print()
    print("  Cross-check that this is the CORPUS's object and not a lookalike:")
    print("  helium_four_body_cluster_probe quotes the graded reference's own")
    print("  4-body simplex coefficient as g_4 = +8.37.  Measured here "
          f"independently: {fmt(g[2], 10)}.")
    assert abs(g[2] - mp.mpf("8.37")) < mp.mpf("0.01"), \
        "g4 must reproduce the corpus's quoted +8.37"
    print("  g2 = 1 exactly, forced by rho_grad(2)=1 with C(2,3)=C(2,4)=0:")
    assert abs(g[0] - 1) < mp.mpf(10) ** -40, "g2 must be exactly 1"
    print(f"    |g2 - 1| = {fmt(abs(g[0] - 1), 4)}")
    print()

    print("THE ONLY QUESTION A 0-FREEDOM SOLVE LEAVES OPEN: does it hold at A=5?")
    print("-" * 78)
    print(f"{'A':>3} {'true rho_grad':>17} {'simplex predict':>19} "
          f"{'predict/true':>14} {'':>10}")
    ratios = {}
    for A in range(2, A_MAX + 1):
        pred = g[0] * C(A, 2) + g[1] * C(A, 3) + g[2] * C(A, 4)
        r = pred / truth[A]
        ratios[A] = r
        tag = "pinned" if A in PIN else ""
        print(f"{A:>3} {fmt(truth[A], 10):>17} {fmt(pred, 10):>19} "
              f"{fmt(r, 8):>14} {tag:>10}")
    print()

    # Gates: exact on the pinned points, collapsing monotonically past them.
    for A in PIN:
        assert abs(ratios[A] - 1) < mp.mpf(10) ** -35, \
            f"solve must be exact at its pinned point A={A}"
    free = [A for A in range(5, A_MAX + 1)]
    assert all(ratios[A] < 1 for A in free), "prediction should undershoot past the pin"
    assert all(ratios[free[i + 1]] < ratios[free[i]] for i in range(len(free) - 1)), \
        "the undershoot should deepen monotonically"
    print(f"  Exact at A = {PIN} by construction (zero freedom, so this is not")
    print("  evidence of anything).  At the FIRST unpinned point, A=5, the basis")
    print(f"  already reproduces only {fmt(ratios[5] * 100, 5)} % of the object;")
    print(f"  by A={A_MAX} it reproduces {fmt(ratios[A_MAX] * 100, 4)} %, a factor "
          f"{fmt(1 / ratios[A_MAX], 5)} short.")
    print()

    print("WHY — structural, not numerical")
    print("-" * 78)
    print("  rho_grad(A) = [A]_q!/[2]_q! grows FACTORIALLY in A; C(A,2), C(A,3),")
    print("  C(A,4) are polynomials in A of degree at most 4.  No finite")
    print("  polynomial basis tracks a factorial, so the divergence is forced.")
    print("  Growth ratios rho_grad(A+1)/rho_grad(A), which a degree-4 polynomial")
    print("  basis would have to match:")
    for A in range(2, A_MAX):
        print(f"    A {A} -> {A+1}:  {fmt(truth[A+1] / truth[A], 8)}")
    print()
    print("  The companion probe measures the mechanism: the graded dimension's")
    print("  degree range is 0..C(A,2), and its coefficient mass migrates into the")
    print("  high degrees as A grows (20.9 % above degree A at A=4, 96.1 % at")
    print("  A=8).  The basis fails exactly where the mass goes.")
    print()

    print("WHAT FOLLOWS")
    print("-" * 78)
    print("  The mu_k are an exact re-expression AT A = 2,3,4 and carry no")
    print("  information about the object away from those points.  In particular")
    print("  mu_4 < 0 is a statement about A=4; it may not be read as '4-body")
    print("  clusters are negative' generally, because the basis carrying that")
    print("  coefficient demonstrably does not extend.")
    print()
    print("WHAT DOES NOT FOLLOW — and must not be written down")
    print("-" * 78)
    print("  * NOT that #4316/#4320 is a fit.  It is not, and that probe is")
    print("    careful to say so: a 3-point solve for 3 coefficients has no")
    print("    freedom to fit WITH.  The defect is in the basis's SPAN, which is")
    print("    a different and weaker charge.")
    print("  * NOT that the sign pattern (mu_2=0, mu_3>0, mu_4<0) is wrong.  It is")
    print("    correct arithmetic at its three points.  The corpus's own framing")
    print("    already says the content is WHICH coefficients are non-zero rather")
    print("    than their values; this adds that the sign pattern inherits the")
    print("    same restriction to A <= 4 that the values do.")
    print("  * NOTHING about rho_strong, which is not touched here.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
