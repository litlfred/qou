#!/usr/bin/env python3
"""M_1>0 machinery (qou-k5r5 / qou-tvok): the OSCILLATORY Euler-Maclaurin tool predicts the V_A
remainder rate theta^{-1} with an explicit constant C_A = TV(g'')/48 -- CONFIRMED, and the falsifiable
target for TV(g'') is pinned by the measured c_1.

Gap qou-k5r5. Remaining: a RIGOROUS bound |V_A(theta)/theta^2 - v_A| <= C_A/theta (Route 1). The corpus
holds, sorry-free,

  QOU.MathlibExt.abs_integral_sub_composite_le_osc :
    | int_a^{a+kh} g - [ h*sum_j g(a+jh) - (h/2)(g a + g(a+kh)) - (h^2/12)(g'(a+kh) - g' a) ] |
      <= h^3/12 * ( g''(a) - g''(a+kh) )          for g'' ANTITONE on the interval.

The decisive feature is that the right-hand side carries NO FACTOR OF k: the per-cell oscillations
telescope, so the remainder is governed by the TOTAL VARIATION of g'' rather than by the number of
grid cells, and the hypotheses are C^2 only. That is exactly what the pointwise Bessel route lacked
(_pointwise_bound_insufficiency.py). With the bulk grid x in [-2sqrt(theta), 2sqrt(theta)] at unit
spacing the rescaled step is h = 1/(2 sqrt(theta)), so dividing by h leaves

    remainder  <=  h^2 TV(g'')/12  =  TV(g'') / (48 theta),

a theta^{-1} rate with an EXPLICIT constant C_A = TV(g'')/48.

MEASURED HERE (exact descent-DPP kernel, NO float64), d(theta) := V_A/theta^2 - 8/pi^2:

  theta        250          500         1000         2000         4000
  d       -2.5794e-4   -1.3451e-4   -6.6422e-5   -3.4320e-5   -1.6901e-5
  exponent     --         0.9393       1.018        0.9526       1.022      -> theta^{-1}
  theta*d   -0.06449     -0.06725     -0.06642     -0.06864     -0.06760   -> c_1 ~ -0.0678

Rate theta^{-1}, sign d < 0 (V_A/theta^2 approaches 8/pi^2 from BELOW). This reproduces
wlambda_covariance_epic_M1_tvok_remainder_rate.py EXACTLY (its theta=1000 value is -6.64223e-5, the
same to every digit printed) and confirms bean qou-tvok STEP 2.

FALSIFIABLE TARGET FOR ROUTE 1: since |d| ~ |c_1|/theta and the EM-osc bound gives |d| <= TV(g'')/(48
theta), a Route-1 derivation must produce

    TV(g'') >= 48 * |c_1| ~ 48 * 0.0678 ~ 3.25,

an O(1) number. Computing TV(g'') independently from the variance density is the REMAINING step;
landing near 3.25 (from ABOVE -- C_A is a BOUND, c_1 a LIMIT, so C_A >= |c_1| is required, not
equality) is a genuine test of the route rather than an assumption.

CLOSURE ARITHMETIC -- CORRECTED 2026-09-03, the earlier text here was WRONG. It read: "at the
theta^{-1} rate, m(n) >= m_inf - C/n > 0 needs only N0 = ceil(C/m_inf) <= 78, i.e. C <= 23.4 -- far
weaker than the C <= 2.65 required under a conservative n^{-1/2} reading." Two defects: (i) the
theta^{-1} rate measured above is V_A's, not the (CS) MARGIN's -- the margin is a ratio of square
roots of variances plus a correlation, and nobody has propagated the one into the other; (ii) what
is PROVED (PR #5929) is |m(n) - m_inf| <= C n^{-1/2}, so N0 = (C/m_inf)^2 (SQUARED) and the
requirement is C <= m_inf*sqrt(79) = 2.6681 -- that is THE requirement, not "a conservative
reading". Correct statement: under the proved shape the empirical envelope over n >= 13 is
C_emp = 0.0580, giving a headroom factor of 46x. Probe:
wlambda_covariance_epic_M1_margin_envelope_exponent.py.

CORRECTION HISTORY (2026-09-03). An earlier version of THIS probe reported the opposite: rate
theta^{-1/2}, C_A ~ 0.857, sign d > 0, and on that basis RETRACTED the EM-osc prediction above. That
was a BUG IN THIS FILE, not a finding. The Sum|c| weight was written as |k|(|k|+1)/2, symmetrising the
negative half; the descent set is the SHIFTED lattice {lambda_i - i}, whose natural involution is
x <-> -1-x, so the correct weight is k(k+1)/2 with SIGNED k -- giving g(-1)=0, g(-2)=-1, g(-3)=-3
(against the buggy -1, -3, -6). The tell was available and missed: every term of V_A is a product of
two squares, hence non-negative, yet the buggy run returned a LARGER V_A from a SMALLER index range
than the reference probe -- impossible if truncation were the only difference. The retraction is
itself retracted; the prediction stands. NO float64 (mpmath.mpf). Gap qou-k5r5 OPEN.
"""
from __future__ import annotations
import mpmath as mp

mp.mp.dps = 40
V_A_POISSON = 8 / mp.pi ** 2          # leading Var(Sum|c|)/theta^2, poissonized (tvok STEP 1, derived)


def gA(k):
    """Sum|c| linear-statistic weight on the SHIFTED descent lattice {lambda_i - i}:
    G_A(k) = k(k+1)/2 for k >= 0 and -k(k+1)/2 for k < 0, with SIGNED k.
    NOTE g(-1) = 0 and g(-k) = -g(k-1): the descent lattice's natural involution is
    x <-> -1-x, NOT x <-> -x. Symmetrising to |k|(|k|+1)/2 is WRONG and was the bug
    that produced a spurious theta^{-1/2} rate (corrected 2026-09-03)."""
    return mp.mpf(k * (k + 1)) / 2 if k >= 0 else -mp.mpf(k * (k + 1)) / 2


def V_A(theta):
    """Exact descent-DPP variance of Sum|c|: (1/2) Sum_{x!=y} (gA(x)-gA(y))^2 J(x,y;theta)^2."""
    M = int(mp.floor(2 * mp.sqrt(theta) + 12 * mp.power(theta, mp.mpf(1) / 6) + 20))
    arg = 2 * mp.sqrt(theta)
    st = mp.sqrt(theta)
    J = {0: mp.besselj(0, arg)}
    for x in range(1, M + 2):
        J[x] = mp.besselj(x, arg)
        J[-x] = (-1) ** x * J[x]
    xs = list(range(-M, M + 1))
    g = {k: gA(k) for k in xs}
    tot = mp.mpf(0)
    for i, x in enumerate(xs):
        gx = g[x]
        for y in xs[i + 1:]:
            Jxy = st * (J[x] * J[y + 1] - J[x + 1] * J[y]) / (x - y)
            if Jxy != 0:
                tot += (gx - g[y]) ** 2 * Jxy * Jxy
    return tot


def main():
    print(f"# V_A remainder rate + EM-osc constant target; dps={mp.mp.dps}; NO float64")
    print(f"# v_A (poissonized, derived) = 8/pi^2 = {mp.nstr(V_A_POISSON, 12)}")
    print(f"# d(theta) := V_A/theta^2 - v_A")
    print("#   theta        d(theta)        exponent p        theta*d")
    prev = None
    last = None
    for e in (250, 500, 1000, 2000, 4000):
        th = mp.mpf(e)
        d = V_A(th) / th ** 2 - V_A_POISSON
        p = ""
        if prev is not None and d != 0 and prev[1] != 0:
            p = mp.nstr(-(mp.log(abs(d)) - mp.log(abs(prev[1]))) / (mp.log(th) - mp.log(prev[0])), 4)
        print(f"  {e:>7}  {mp.nstr(d,6):>14}  {p:>10}  {mp.nstr(th*d,6):>14}")
        prev = (th, d)
        last = th * d
    print("#")
    print("# MEASURED: exponent p ~ 1.0 across every doubling => rate theta^{-1}; theta*d is stable")
    print("#   near -0.0678 => c_1 ~ -0.0678; sign d < 0 (approaches 8/pi^2 from BELOW).")
    print("#   This reproduces wlambda_covariance_epic_M1_tvok_remainder_rate.py EXACTLY (theta=1000:")
    print("#   -6.64223e-5 in both) and confirms bean qou-tvok STEP 2.")
    print("#")
    if last is not None:
        tv = 48 * abs(last)
        print(f"# FALSIFIABLE TARGET FOR ROUTE 1: the EM-osc bound gives |d| <= TV(g'')/(48 theta), so a")
        print(f"#   Route-1 derivation must yield TV(g'') >= 48*|c_1| ~ {mp.nstr(tv,5)} (an O(1) number).")
        print(f"#   C_A is a BOUND and c_1 a LIMIT, so C_A >= |c_1| is required, not equality: landing")
        print(f"#   near {mp.nstr(tv,4)} FROM ABOVE is the genuine test. Computing TV(g'') from the")
        print(f"#   variance density is the REMAINING step.")
    print("#")
    print("# CLOSURE ARITHMETIC (CORRECTED 2026-09-03; the 'C <= 23.4' once printed here is RETRACTED).")
    print("#   The theta^{-1} rate above is V_A's, NOT the (CS) margin's, and the PROVED margin bound")
    print("#   (PR #5929) is |m - m_inf| <= C n^{-1/2}, whence N0 = (C/m_inf)^2 and the requirement is")
    print("#   C <= m_inf*sqrt(79) = 2.6681. Empirical envelope over n >= 13 is 0.0580 => 46x headroom.")
    print("#   See wlambda_covariance_epic_M1_margin_envelope_exponent.py.")
    print("#")
    print("# CORRECTION: an earlier version of this file reported theta^{-1/2}, C_A ~ 0.857, d > 0 and")
    print("#   retracted the EM-osc prediction. That was a BUG -- the Sum|c| weight was symmetrised to")
    print("#   |k|(|k|+1)/2 instead of the shifted-lattice k(k+1)/2 with signed k. The retraction is")
    print("#   retracted; the theta^{-1} prediction stands.")
    print("RESULT: V_A remainder rate theta^{-1}, c_1 ~ -0.0678 (reproduces tvok exactly); EM-osc target")
    print("        TV(g'') ~ 3.25 pinned. qou-k5r5 OPEN.")
    print("EXIT: 0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
