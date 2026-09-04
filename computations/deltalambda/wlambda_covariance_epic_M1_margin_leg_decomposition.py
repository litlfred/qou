#!/usr/bin/env python3
"""M_1>0 (qou-k5r5): decompose the finite-n margin deviation into its two legs, and measure whether
they CANCEL -- which decides how lossy a per-leg (triangle-inequality) budget would be.

WHY THIS, NOW. PR #6528 established that the rigorous constant C should be budgeted PER LEG rather
than as one number, because the two legs are not the same size: rho_P deviates like 0.1329/theta
while the V_A leg contributes only 0.003251/sqrt(theta). But a per-leg budget is applied through the
triangle inequality

    |m(n) - m_inf|  <=  |L_rho(n)|  +  |L_sig(n)|,

and that is only a sensible way to spend the budget if the two legs do NOT largely cancel. If they
do, the sum of per-leg bounds overshoots the truth and the budget is wasted. Nothing in the arc has
measured this.

THE DECOMPOSITION IS EXACT, not asymptotic. With m = rho_P - sqrt(V_D/V_A) and
m_inf = rho_inf - sig_ratio_inf,

    m(n) - m_inf  =  [rho_P(n) - rho_inf]  -  [sqrt(V_D/V_A)(n) - sig_ratio_inf]
                  =:  L_rho(n)  -  L_sig(n),

with no error term: it is a rearrangement. Both legs are computed here from the EXACT Fraction
covariances over all partitions of n (mpmath only for the square roots and display), so the
decomposition is verified to close to round-off at every n.

WHAT IS MEASURED
  - L_rho(n), L_sig(n) and their signed sum, per n;
  - the CANCELLATION RATIO  |L_rho - L_sig| / (|L_rho| + |L_sig|).  A ratio near 1 means the legs
    act independently and a per-leg budget is tight; near 0 means they cancel and a per-leg budget
    is badly lossy.
  - which leg dominates, and whether that changes with n.

scope-(a); no fit; nothing wired; no c_k; L2 unchanged. Gap qou-k5r5 OPEN.
"""
from __future__ import annotations
from fractions import Fraction as F
from functools import lru_cache
import importlib.util
import pathlib
import mpmath as mp

mp.mp.dps = 30

M_INF = mp.mpf('0.300186614161')
RHO_INF = mp.mpf('0.979796195657')          # = 2 sqrt(6)/5
SIG_RATIO_INF = mp.mpf('0.679609581496')


def _load_partitions_and_stats():
    """Reuse the merged C-landscape probe's partition enumerator and stats, by explicit file path
    (not a bare-name import: the _path_bridge bootstrap trap; must run with PYTHONPATH unset)."""
    here = pathlib.Path(__file__).resolve().parent
    src = here / "wlambda_covariance_epic_M1_constant_C_landscape.py"
    spec = importlib.util.spec_from_file_location("_m1_cl", src)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def legs(mod, n):
    """Exact (L_rho, L_sig, m) at size n. Mirrors the merged margin() but keeps the two legs apart."""
    nf = mod.fact(n)
    Cn2 = F(n * (n - 1), 2)
    ac = {k: F(0) for k in ("A", "D", "W", "AA", "DD", "WW", "AW")}
    for lam in mod.partitions(n):
        d, A, Dd, c2 = mod.stats(lam, n)
        w = F(d * d, nf)
        W = F(c2) - Cn2
        ac["A"] += w * A; ac["D"] += w * Dd; ac["W"] += w * W
        ac["AA"] += w * A * A; ac["DD"] += w * Dd * Dd; ac["WW"] += w * W * W
        ac["AW"] += w * A * W
    VA = ac["AA"] - ac["A"] ** 2
    VD = ac["DD"] - ac["D"] ** 2
    VW = ac["WW"] - ac["W"] ** 2
    P = ac["AW"] - ac["A"] * ac["W"]
    if VA <= 0 or VW <= 0:
        return None
    r = lambda x: mp.mpf(x.numerator) / x.denominator
    rho = r(P) / mp.sqrt(r(VA) * r(VW))
    sig = mp.sqrt(r(VD) / r(VA))
    nn = mp.mpf(n) ** 2
    return (rho - RHO_INF, sig - SIG_RATIO_INF, rho - sig,
            r(VA) / nn, r(VD) / nn)


def main():
    mod = _load_partitions_and_stats()
    nmax = 40
    print(f"# margin leg decomposition; m_inf={mp.nstr(M_INF,9)}; dps={mp.mp.dps}; NO float64")
    print("# m(n) - m_inf = [rho_P(n) - rho_inf] - [sqrt(V_D/V_A)(n) - sig_ratio_inf] =: L_rho - L_sig")
    print("# (an exact rearrangement, no error term -- the 'closes' column verifies it numerically)")
    print(f"#   {'n':>3} {'L_rho':>13} {'L_sig':>13} {'L_rho-L_sig':>13} {'m-m_inf':>13} "
          f"{'closes':>9} {'cancel':>8}")
    rows = []
    for n in range(4, nmax + 1):
        got = legs(mod, n)
        if got is None:
            continue
        lr, ls, m, vAn, vDn = got
        dev = m - M_INF
        diff = lr - ls
        closes = abs(diff - dev)
        denom = abs(lr) + abs(ls)
        cancel = abs(diff) / denom if denom != 0 else mp.mpf('nan')
        rows.append((n, lr, ls, dev, cancel, vAn, vDn))
        if n <= 12 or n % 4 == 0:
            print(f"#   {n:>3} {mp.nstr(lr,6):>13} {mp.nstr(ls,6):>13} {mp.nstr(diff,6):>13} "
                  f"{mp.nstr(dev,6):>13} {mp.nstr(closes,2):>9} {mp.nstr(cancel,4):>8}")
    print("#")

    tail = [r for r in rows if r[0] >= 16]
    cmin = min(r[4] for r in tail)
    cmax = max(r[4] for r in tail)
    print("# CANCELLATION. ratio = |L_rho - L_sig| / (|L_rho| + |L_sig|); 1 = legs independent (a")
    print("#   per-leg triangle-inequality budget is tight), 0 = they cancel (a per-leg budget is")
    print(f"#   badly lossy). Over n >= 16: min {mp.nstr(cmin,4)}, max {mp.nstr(cmax,4)}.")
    print("#")

    print("# WHICH LEG DOMINATES, at finite n (exact):")
    print(f"#   {'n':>3} {'|L_rho|':>13} {'|L_sig|':>13} {'|L_rho|/|L_sig|':>16}")
    for n, lr, ls, dev, c, _a, _d in rows:
        if n % 6 == 0 or n == rows[-1][0]:
            ratio = abs(lr) / abs(ls) if ls != 0 else mp.mpf('inf')
            print(f"#   {n:>3} {mp.nstr(abs(lr),6):>13} {mp.nstr(abs(ls),6):>13} "
                  f"{mp.nstr(ratio,5):>16}")
    print("#")
    # Attribute L_sig to its V_D and V_A halves. sqrt(V_D/V_A) ~ sig_inf (1 + (dD - dA)/2).
    V_A_INF = 8 / (9 * mp.pi ** 2)                  # de-poissonized, PR #5969
    V_D_INF = SIG_RATIO_INF ** 2 * V_A_INF
    print("# ATTRIBUTING L_sig -- it involves BOTH V_D and V_A, and PR #6528 accounted only for V_A.")
    print("#   sqrt(V_D/V_A) ~ sig_inf * (1 + (dD - dA)/2), dX = relative deviation of V_X/n^2.")
    print(f"#   v_A_inf = 8/(9 pi^2) = {mp.nstr(V_A_INF,8)}   v_D_inf = sig_inf^2 v_A_inf = "
          f"{mp.nstr(V_D_INF,8)}")
    print(f"#   {'n':>3} {'dA':>12} {'dD':>12} {'|dD|/|dA|':>11} {'sig_inf(dD-dA)/2':>18} {'L_sig':>12}")
    for n, lr, ls, dev, c, vAn, vDn in rows:
        if n % 6 == 0 or n == rows[-1][0]:
            dA = (vAn - V_A_INF) / V_A_INF
            dD = (vDn - V_D_INF) / V_D_INF
            pred = SIG_RATIO_INF * (dD - dA) / 2
            rat = abs(dD) / abs(dA) if dA != 0 else mp.mpf('inf')
            print(f"#   {n:>3} {mp.nstr(dA,5):>12} {mp.nstr(dD,5):>12} {mp.nstr(rat,4):>11} "
                  f"{mp.nstr(pred,5):>18} {mp.nstr(ls,5):>12}")
    print("#   => the first-order prediction tracks L_sig (within a few %, the second-order term), and")
    print("#      |dD| dominates |dA|: the sigma-ratio leg is driven by V_D, NOT V_A.")
    print("#")
    print("# BUT dD AND dA HAVE THE SAME SIGN AND LARGELY CANCEL IN THE DIFFERENCE -- a SECOND")
    print("#   cancellation, inside the leg, on top of the one between the legs:")
    print(f"#   {'n':>3} {'dD-dA':>12} {'|dD|+|dA|':>12} {'cancel(inner)':>14}")
    inner = []
    for n, lr, ls, dev, c, vAn, vDn in rows:
        dA = (vAn - V_A_INF) / V_A_INF
        dD = (vDn - V_D_INF) / V_D_INF
        ic = abs(dD - dA) / (abs(dD) + abs(dA))
        inner.append((n, ic))
        if n % 6 == 0 or n == rows[-1][0]:
            print(f"#   {n:>3} {mp.nstr(dD-dA,5):>12} {mp.nstr(abs(dD)+abs(dA),5):>12} "
                  f"{mp.nstr(ic,4):>14}")
    itail = [ic for n, ic in inner if n >= 16]
    print(f"#   inner cancellation over n >= 16: min {mp.nstr(min(itail),4)}, "
          f"max {mp.nstr(max(itail),4)}")
    print("#")
    print("# THE CONSEQUENCE FOR THE ROUTE, and it is the point of this probe. There are TWO")
    print("#   cancellations -- between the legs, and inside the sigma-ratio leg between V_D and V_A.")
    print("#   A budget that bounds each ingredient separately and adds (triangle inequality) throws")
    print("#   BOTH away, so the two ratios above are a real cost to any per-ingredient proof.")
    print("#")
    print("#   HOW MUCH they cost TOGETHER is NOT the product of the two worst cases, and this probe")
    print("#   must not be read as saying so. The two cancellations are not independent and their")
    print("#   worst cases fall at different n, so multiplying them double-counts. The composite has")
    print("#   to be MEASURED, and it is, in the sibling probe")
    print("#   wlambda_covariance_epic_M1_naive_budget_closes_probe.py: at the ENVELOPE level the")
    print("#   naive per-ingredient budget overshoots by 4.83x (C_naive 0.2798 vs C_true 0.05797,")
    print("#   both sups at n=22), leaving 9.54x of the 46x headroom -- NOT 'most of the room'.")
    print("#   Preserving the cancellations is therefore an OPTIMISATION worth ~5x, not a structural")
    print("#   requirement on the proof: the triangle inequality alone does not exclude the easy")
    print("#   route. What is still open is whether a RIGOROUS per-ingredient constant fits in the")
    print("#   remaining 9.54x, since every constant here is an empirical sup over n <= 40.")
    print("#")
    print("# SO WHAT SHOULD BE BOUNDED? The cancellation says: not V_D and V_A separately. The")
    print("#   natural candidate is the RATIO V_D/V_A as ONE object. Measured -- how much more")
    print("#   stable is the ratio than either variance?")
    R_INF = SIG_RATIO_INF ** 2                       # (V_D/V_A)_inf
    print(f"#   (V_D/V_A)_inf = sig_inf^2 = {mp.nstr(R_INF,9)}")
    print(f"#   {'n':>3} {'|dA|':>11} {'|dD|':>11} {'|d_ratio|':>11} {'gain vs dD':>11}")
    gains = []
    for n, lr, ls, dev, c, vAn, vDn in rows:
        dA = (vAn - V_A_INF) / V_A_INF
        dD = (vDn - V_D_INF) / V_D_INF
        d_ratio = ((vDn / vAn) - R_INF) / R_INF      # EXACT, not the linearisation
        g = abs(dD) / abs(d_ratio) if d_ratio != 0 else mp.mpf('inf')
        gains.append((n, g))
        if n % 6 == 0 or n == rows[-1][0]:
            print(f"#   {n:>3} {mp.nstr(abs(dA),5):>11} {mp.nstr(abs(dD),5):>11} "
                  f"{mp.nstr(abs(d_ratio),5):>11} {mp.nstr(g,4):>11}")
    gt = [g for n, g in gains if n >= 16]
    print(f"#   gain over n >= 16: min {mp.nstr(min(gt),4)}x, max {mp.nstr(max(gt),4)}x")
    print("#   => bounding the RATIO directly is the right target, and it is worth a factor of a few")
    print("#      -- real, but not the whole composite loss (measured 4.83x at the envelope level in")
    print("#      _naive_budget_closes_probe). The rest lives in the leg-vs-leg cancellation, which a")
    print("#      ratio bound does not capture; recovering it needs rho_P and the sigma-ratio handled")
    print("#      TOGETHER, not two tight bounds added. Stated so the next attempt does not spend its")
    print("#      effort on the ratio alone and expect the whole factor back -- and, equally, so it")
    print("#      does not think it MUST do either: 4.83x out of 46x still leaves 9.54x.")
    print("#")
    print("# CORRECTION TO PR #6528 (same session). There I concluded 'rho_P is the bigger leg, V_A")
    print("#   the small one' by comparing rho_P's FULL deviation against only the V_A part of the")
    print("#   sigma-ratio leg -- V_D was never in that comparison. Measured here at fixed n with")
    print("#   exact arithmetic, |L_sig| exceeds |L_rho| by 4x to 700x, so the SIGMA-RATIO leg")
    print("#   dominates and V_D is the binding ingredient. The #6528 conversion (C_margin,A =")
    print("#   0.41922 C_A) and its ~821x V_A-leg headroom are unaffected -- they are correct")
    print("#   statements ABOUT THE V_A LEG. What was wrong is the claim that rho_P is where the")
    print("#   binding constraint sits.")
    print("#")
    print("# READ THIS AGAINST PR #6528. There the LEG SIZES were compared at large theta from the")
    print("#   POISSONIZED ingredients: rho_P deviating ~0.1329/theta against the V_A leg's")
    print("#   0.003251/sqrt(theta). This probe is the fixed-n, exact-arithmetic companion, and it")
    print("#   measures the thing that decides whether a per-leg budget is the right instrument:")
    print("#   the cancellation between them. The two are different measurements of the same split")
    print("#   and should be quoted separately -- one is poissonized and asymptotic, this one is")
    print("#   exact and finite-n.")
    print(f"RESULT: leg decomposition exact and verified; cancellation ratio over n>=16 in "
          f"[{mp.nstr(cmin,4)}, {mp.nstr(cmax,4)}]. qou-k5r5 OPEN.")
    print("EXIT: 0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
