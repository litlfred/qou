#!/usr/bin/env python3
"""M_1>0 machinery (qou-k5r5 / qou-tvok): measure the V_A remainder rate and coefficient, and
determine which Euler-Maclaurin tool can actually deliver it. HONEST NEGATIVE on my own prediction.

Gap qou-k5r5. Remaining: a RIGOROUS bound on |V_A(theta)/theta^2 - v_A| (Route 1). The corpus already
has, sorry-free, the tool

  QOU.MathlibExt.abs_integral_sub_composite_le_osc :
    | int_a^{a+kh} g - [ h*sum_j g(a+jh) - (h/2)(g a + g(a+kh)) - (h^2/12)(g'(a+kh) - g' a) ] |
      <= h^3/12 * ( g''(a) - g''(a+kh) )          for g'' ANTITONE on the interval.

whose decisive feature is that the right-hand side carries NO FACTOR OF k -- the per-cell oscillations
telescope, so the remainder is governed by the TOTAL VARIATION of g'', not by the number of cells.
That is exactly what the pointwise Bessel route lacked (_pointwise_bound_insufficiency.py). With the
bulk grid x in [-2sqrt(theta), 2sqrt(theta)] at unit spacing, the rescaled step is h = 1/(2 sqrt(theta)),
so dividing by h leaves remainder <= h^2 TV(g'')/12 = TV(g'')/(48 theta) -- a theta^{-1} rate.

I PREDICTED that rate for V_A and MEASURED theta^{-1/2}. The prediction is WRONG for this ingredient,
and the reason is structural, not numerical: `_osc` requires g'' ANTITONE on the interval, and the
Sum|c| weight's rescaled test function is |u|, which has a KINK at u = 0. The kink breaks monotonicity;
splitting the interval there leaves an UN-CANCELLED Euler-Maclaurin boundary term at u=0 (g' jumps),
and that term is O(h) = O(theta^{-1/2}), not O(h^2). So the clean TV(g'')/(48 theta) route applies to
the SMOOTH ingredients (Sum c^2 and the covariance, which the corpus power-counting already puts at
theta^{-1}), and NOT to the kink ingredient V_A.

MEASURED HERE (exact descent-DPP kernel, NO float64), d(theta) := V_A/theta^2 - 8/pi^2:

  theta      250        500       1000       2000       4000
  d       0.055650   0.038941   0.027331   0.019224   0.013543
  exponent    --       0.5151     0.5107     0.5076     0.5054     -> theta^{-1/2}
  sqrt(th)*d 0.8799    0.8707     0.8643     0.8597     0.8565     -> C_A ~ 0.857

This CONFIRMS the corpus power-counting in
docs/audits/2026-08-29-covariance-kernel-M1-rigorous-finite-n-bound.md ("the kink costs half an order
in Euler-Maclaurin ... O(theta^{-1/2}) rather than O(theta^{-1})"), and it DISAGREES with the figures
recorded on bean qou-tvok STEP 2 ("rate theta^{-1}, c_1 ~ -0.0678, sign d<0") in BOTH rate and SIGN --
here d > 0 (V_A/theta^2 approaches 8/pi^2 from ABOVE). This probe does not adjudicate that: the two may
be measuring different objects (poissonized vs de-poissonized V_A, or the margin rather than V_A). The
discrepancy is FLAGGED, not resolved, and the sibling figure is not assumed wrong.

Scope: this measures ONE ingredient. It does NOT give the (CS) margin's constant, which is what the
closure needs; the margin's own empirical envelope is ~0.087 (constant-C audit) -- an order of
magnitude BELOW V_A's own 0.857, because the ratio sigma_D/sigma_A cancels most of the common
correction. NO float64 (mpmath.mpf). Nothing wired; no c_k; L2 unchanged. Gap qou-k5r5 OPEN.
"""
from __future__ import annotations
import mpmath as mp

mp.mp.dps = 40
V_A_POISSON = 8 / mp.pi ** 2          # leading Var(Sum|c|)/theta^2, poissonized (tvok STEP 1, derived)


def gA(k):
    kk = abs(k)
    v = mp.mpf(kk * (kk + 1)) / 2
    return v if k >= 0 else -v


def V_A(theta):
    """Exact descent-DPP variance of Sum|c|: (1/2) Sum_{x!=y} (gA(x)-gA(y))^2 J(x,y;theta)^2."""
    M = int(mp.floor(2 * mp.sqrt(theta) + 10 * mp.power(theta, mp.mpf(1) / 6) + 24))
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
    print(f"# V_A remainder rate + coefficient; dps={mp.mp.dps}; NO float64")
    print(f"# v_A (poissonized, derived) = 8/pi^2 = {mp.nstr(V_A_POISSON, 12)}")
    print(f"# d(theta) := V_A/theta^2 - v_A")
    print("#   theta        d(theta)        exponent p      sqrt(theta)*d      theta*d")
    prev = None
    for e in (250, 500, 1000, 2000, 4000):
        th = mp.mpf(e)
        d = V_A(th) / th ** 2 - V_A_POISSON
        p = ""
        if prev is not None and d != 0 and prev[1] != 0:
            p = mp.nstr(-(mp.log(abs(d)) - mp.log(abs(prev[1]))) / (mp.log(th) - mp.log(prev[0])), 4)
        print(f"  {e:>7}  {mp.nstr(d,6):>14}  {p:>10}  {mp.nstr(mp.sqrt(th)*d,6):>14}  "
              f"{mp.nstr(th*d,6):>12}")
        prev = (th, d)
    print("#")
    print("# MEASURED: exponent p -> 0.505, i.e. the V_A remainder is theta^{-1/2}, NOT theta^{-1}.")
    print("#   sqrt(theta)*d is nearly constant (0.880 -> 0.857) => C_A ~ 0.857, and it is still")
    print("#   drifting DOWN, so 0.857 is an upper reading rather than a converged limit.")
    print("#   theta*d GROWS (13.9 -> 54.2), which is what rules out theta^{-1} for this ingredient.")
    print("#   SIGN: d > 0 -- V_A/theta^2 approaches 8/pi^2 from ABOVE.")
    print("#")
    print("# MY PREDICTION WAS WRONG, and structurally so. The EM tool _osc requires g'' ANTITONE;")
    print("#   the Sum|c| rescaled test function is |u|, with a KINK at u=0 that breaks monotonicity.")
    print("#   Splitting there leaves an UN-CANCELLED EM boundary term (g' jumps) of order h =")
    print("#   1/(2 sqrt(theta)), i.e. theta^{-1/2} -- not the h^2 the telescoping bound would give.")
    print("#   So TV(g'')/(48 theta) is the right form for the SMOOTH ingredients (Sum c^2, the")
    print("#   covariance), and NOT for the kink ingredient V_A.")
    print("#")
    print("# CONSISTENT WITH: docs/audits/2026-08-29-...-rigorous-finite-n-bound.md (kink costs half")
    print("#   an order). DISAGREES WITH the figures on bean qou-tvok STEP 2 (theta^{-1}, c_1 ~")
    print("#   -0.0678, d<0) in BOTH rate and sign. NOT adjudicated here -- the two may measure")
    print("#   different objects (poissonized vs de-poissonized, or the margin vs V_A). FLAGGED.")
    print("#")
    print("# SCOPE: this is ONE ingredient, not the (CS) margin the closure needs. The margin's own")
    print("#   empirical envelope is ~0.087 -- 10x BELOW V_A's 0.857 -- because sigma_D/sigma_A")
    print("#   cancels most of the common correction. Do not read C_A ~ 0.857 as the margin's C.")
    print("RESULT: V_A remainder is theta^{-1/2}, C_A ~ 0.857, d>0; EM-osc telescoping does NOT apply")
    print("        to the kink ingredient. Prediction retracted. qou-k5r5 OPEN.")
    print("EXIT: 0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
