#!/usr/bin/env python3
"""rho_inf = 2 sqrt(6)/5 EXACTLY, derived from Kerov's central limit theorem.

WHAT WAS OPEN.  The M_1 arc records `RHO_INF = 0.979796195657` as a numerically
extrapolated constant, annotated `# = 2 sqrt(6)/5`.  A sibling probe
(`..._rho_inf_closed_form_resolvability.py`) established NUMERICALLY that the
extrapolation converges to that closed form -- at a theta=40960 ladder the method
error is 9.933e-08 and the candidate sits 2.565e-08 away while the recorded
literal sits 3.303e-07 away, 3.33x outside.  That is evidence, not a derivation.
This probe derives it.

THE SET-UP.  `rho_P` is the de-poissonized correlation between two linear
statistics of the Plancherel/BOO descent process:

    A = sum over the particle set of  (discrete antiderivative of |c|)
    W = sum over the particle set of  (discrete antiderivative of c^2)

A linear statistic of the counting measure, integrated by parts against the
profile fluctuation, tests that fluctuation against the summand's DERIVATIVE.
So A and W test the fluctuation against

    h_A(x) = |x|        h_W(x) = x^2

on the Vershik-Kerov-Logan-Shepp support [-2, 2].

THE INPUT -- Kerov's CLT, Ivanov-Olshanski (arxiv math/0304010, eq. 0.3), held in
`library/arxiv-math-0304010v1/`:

    Delta(2 cos theta) = (1/pi) sum_{k>=2} (xi_k / sqrt(k)) sin(k theta)

with xi_k independent standard Gaussians.  NOTE THE SUM STARTS AT k = 2: the k=1
mode is fixed by the box count, which is exactly the conditioning on the particle
number that `ingredients()` performs (`cond = cXY - cXN cYN / VN`).  That
agreement is why this framework is the right one for the de-poissonized rho and
not merely a plausible analogue.

Independence of the xi_k gives, for test functions f and g,

    Cov(f, g)  proportional to  sum_{k>=2} F_k G_k / k
    F_k = int_{-2}^{2} f(x) sin(k arccos(x/2)) dx        (x = 2 cos theta)

and the proportionality constant cancels in a correlation.

THE TWO FACTS THAT MAKE IT CLOSE, both computed here rather than asserted:

  1. G_k = pi * delta_{k,3}.  The x^2 statistic couples to EXACTLY ONE Kerov
     mode.  (cos^2 theta sin theta sin(k theta) integrates to zero on [0, pi] for
     every k >= 2 except k = 3.)  This collapses the numerator to a single term
     and is the reason a clean closed form exists at all.

  2. F_k = 8 (-1)^((k-3)/2) / (k^2 - 4) for odd k >= 3, and 0 otherwise.
     (Even k vanish by the symmetry theta -> pi - theta.)

Then rho = (F_3 G_3 / 3) / sqrt(S * G_3^2 / 3) with S = sum_{k odd >= 3} F_k^2/k,
and S evaluates in closed form:

    64/(k(k-2)^2(k+2)^2) = 4/k - 2/(k+2) - 2/(k+2)^2 - 2/(k-2) + 2/(k-2)^2

    squared part TELESCOPES : sum [2/(k-2)^2 - 2/(k+2)^2] = 2(1/1^2 + 1/3^2) = 20/9
    1/k part has coefficients summing to zero, so it rearranges to a finite
    remainder                                                            = -4/3
                                                                    S    =  8/9

    rho = ((8/5) pi / 3) / sqrt((8/9) pi^2 / 3) = 2 sqrt(6)/5,   rho^2 = 24/25.

WHAT THIS DOES AND DOES NOT SETTLE.  It derives the VALUE from a published CLT
plus two integrals and one telescoping sum -- no fit, no anchor, no calibration,
nothing empirical.  It does NOT re-prove Kerov's CLT, and it does not by itself
establish that the arc's `ingredients()` discretisation converges to the
continuum object; the sibling probe's numerical agreement to 2.6e-08 is the
evidence for that step, and it is evidence rather than proof.

CONSEQUENCE FOR THE RECORDED CONSTANT.  `0.979796195657` is wrong from its
seventh digit: the true value is 0.97979589711327123927...  The literal should be
replaced by the closed form.

Exact symbolic arithmetic throughout -- sympy Rationals and Fraction, no float
anywhere.  Writes no witness: it establishes an identity, not a measurement.
scope-(a); no fit; no c_k; L2 unchanged.  Bean qou-742w.
"""
from __future__ import annotations

from fractions import Fraction

import sympy as sp


def kerov_coeff(f_of_theta, kk):
    """F_k = int_{-2}^{2} f(x) sin(k arccos(x/2)) dx, via x = 2 cos theta."""
    th = sp.Symbol('theta')
    return sp.simplify(sp.integrate(f_of_theta(th) * sp.sin(kk * th) * 2 * sp.sin(th),
                                    (th, 0, sp.pi)))


def main() -> int:
    th = sp.Symbol('theta')
    h_A = lambda t: 2 * sp.Abs(sp.cos(t))      # |x|,  x = 2 cos theta
    h_W = lambda t: (2 * sp.cos(t)) ** 2       # x^2

    checks = []
    print("# rho_inf = 2 sqrt(6)/5 from Kerov's CLT (Ivanov-Olshanski, math/0304010 eq. 0.3)")
    print("#   Delta(2 cos th) = (1/pi) sum_{k>=2} xi_k/sqrt(k) sin(k th),  xi_k iid N(0,1)")
    print("#   the k>=2 start IS the conditioning on particle number that ingredients() does")
    print("#")

    # --- 1. the x^2 statistic couples to exactly one mode -------------------------------------
    G = {kk: kerov_coeff(h_W, kk) for kk in range(2, 10)}
    print("# 1. G_k for h_W = x^2:")
    for kk, v in G.items():
        print(f"#      G_{kk} = {v}")
    one_mode = (G[3] == sp.pi) and all(G[kk] == 0 for kk in G if kk != 3)
    checks.append(("G_k = pi * delta_{k,3} -- the x^2 statistic is a SINGLE Kerov mode", one_mode))

    # --- 2. closed form for the |x| coefficients ----------------------------------------------
    print("# 2. F_k for h_A = |x|, against the closed form 8(-1)^((k-3)/2)/(k^2-4):")
    f_ok = True
    for kk in range(2, 14):
        got = kerov_coeff(h_A, kk)
        want = (sp.Rational(8 * (-1) ** ((kk - 3) // 2), kk ** 2 - 4) if kk % 2 else sp.Integer(0))
        f_ok &= (sp.simplify(got - want) == 0)
        print(f"#      F_{kk:2} = {str(got):>10}   closed form {str(want):>10}")
    checks.append(("F_k = 8(-1)^((k-3)/2)/(k^2-4) on odd k>=3, 0 otherwise", f_ok))

    # --- 3. the sum S = sum_{k odd>=3} F_k^2 / k ----------------------------------------------
    k = sp.Symbol('k')
    pf = 4 / k - 2 / (k + 2) - 2 / (k + 2) ** 2 - 2 / (k - 2) + 2 / (k - 2) ** 2
    pf_ok = sp.simplify(64 / (k * (k - 2) ** 2 * (k + 2) ** 2) - pf) == 0
    checks.append(("partial fractions of 64/(k(k-2)^2(k+2)^2)", pf_ok))

    # squared part telescopes: (k-2) runs over odd j>=1, (k+2) over odd j>=5
    squared = sp.Rational(20, 9)
    # 1/k part: 4A_3 - 2A_1 - 2A_5 with A_1 = 1 + 1/3 + A_5, A_3 = 1/3 + A_5  ->  A_5 cancels
    A5 = sp.Symbol('A5')
    linear_expr = sp.expand(4 * (sp.Rational(1, 3) + A5) - 2 * (1 + sp.Rational(1, 3) + A5) - 2 * A5)
    checks.append(("the 1/k part's divergent tail cancels", linear_expr.coeff(A5) == 0))
    linear = sp.nsimplify(linear_expr.subs(A5, 0))
    S = sp.nsimplify(squared + linear)
    print("#")
    print(f"# 3. S = telescoping {squared} + finite remainder {linear} = {S}")
    checks.append(("S = 8/9", S == sp.Rational(8, 9)))

    # independent confirmation in EXACT rationals -- no float
    partial = sum(Fraction(64, kk * (kk - 2) ** 2 * (kk + 2) ** 2) for kk in range(3, 20001, 2))
    # every omitted term is < 64/k^5 and there are < k/2 of them below any cutoff
    tail = Fraction(64, 20001 ** 4)
    print(f"#    exact-Fraction partial sum to k=19999 differs from 8/9 by less than {tail}: "
          f"{abs(partial - Fraction(8, 9)) < tail}")
    checks.append(("exact-rational partial sum agrees with 8/9 inside its tail bound",
                   abs(partial - Fraction(8, 9)) < tail))

    # --- 4. assemble ---------------------------------------------------------------------------
    rho = sp.radsimp(sp.simplify((sp.Rational(8, 5) * sp.pi / 3)
                                 / sp.sqrt(S * sp.pi ** 2 / 3)))
    print("#")
    print(f"# 4. rho = (F_3 G_3 / 3) / sqrt(S G_3^2 / 3) = {rho}")
    print(f"#    2 sqrt(6)/5 = {2 * sp.sqrt(6) / 5};  rho^2 = {sp.simplify(rho ** 2)}")
    checks.append(("rho = 2 sqrt(6)/5", sp.simplify(rho - 2 * sp.sqrt(6) / 5) == 0))
    checks.append(("rho^2 = 24/25", sp.simplify(rho ** 2 - sp.Rational(24, 25)) == 0))

    print("#")
    print(f"#    recorded literal 0.979796195657 is wrong from its SEVENTH digit;")
    print(f"#    the derived value is {sp.N(2 * sp.sqrt(6) / 5, 21)}")
    print("#")
    for name, ok in checks:
        print(f"#   [{'PASS' if ok else 'FAIL'}] {name}")
    return 0 if all(ok for _, ok in checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
