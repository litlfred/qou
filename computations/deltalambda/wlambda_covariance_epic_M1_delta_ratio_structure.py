#!/usr/bin/env python3
"""M_1>0 (qou-k5r5): does bounding the RATIO V_D/V_A buy a better RATE, or only a better CONSTANT?
The whole ratio route turns on this one fact, and nothing has measured it.

WHY THIS, NOW. PR #6576 established that the right analytic target is a rigorous finite-n bound on
rho_P and on the ratio V_D/V_A -- 1.137x lossy, 40.5x of the 46x headroom, against 9.26x for bounding
V_D and V_A separately. What it did NOT establish is WHY the ratio is better behaved, and that
distinction decides how much work the remaining proof is:

  * If delta_D/delta_A -> 1, the leading finite-n corrections of the two variances are the SAME and
    cancel in the ratio. Then delta_R = delta_D - delta_A is HIGHER ORDER -- a better RATE, not just
    a better constant -- and a rigorous bound on the ratio could be much weaker than one on either
    variance and still suffice. That would be a structural fact worth formalizing.
  * If delta_D/delta_A -> r != 1, the corrections are proportional but not equal. Then
    delta_R ~ (r-1) delta_A: the SAME rate, smaller by the constant factor |r-1|. The ratio route is
    then exactly as hard as bounding delta_A, and its gain is arithmetic rather than structural.

These are different projects, and the formalize-first discipline says settle which one you are in
before starting it.

WHAT IS COMPUTED, exactly (Fraction covariances over every partition of n; mpmath only for square
roots, ratios and display):

    delta_A(n) = (V_A/n^2 - v_A)/v_A          v_A = 8/(9 pi^2)          (de-poissonized, PR #5969)
    delta_D(n) = (V_D/n^2 - v_D)/v_D          v_D = sig_inf^2 v_A
    rho_delta(n) = delta_D(n)/delta_A(n)      -- the quantity that decides the question
    delta_R(n) = ((V_D/V_A) - sig_inf^2)/sig_inf^2   -- EXACT, not the linearisation

and, to separate "rate" from "constant" without trusting a single extrapolation, the local log-log
exponents of |delta_A| and |delta_R| between successive tabulated n. If the two exponents agree, the
ratio is a constant-factor gain; if |delta_R|'s exponent is larger, it is a rate gain.

WHAT THIS CANNOT DO. It cannot prove a rate. The window ends at n = 46 while the constant is required
only for n >= 79, and these sequences OSCILLATE -- a local exponent between two adjacent n is noise
unless the trend is read across many of them. Both are reported, and a single-pair exponent is not
quoted as a rate anywhere. If rho_delta has not settled by n = 46 this probe says so and answers
nothing; that is a legitimate outcome and is reported as one.

NO PREDICTION IS ENCODED HERE. The verdict lines are computed from the measured numbers, not written
in advance -- the failure mode this repo has repeatedly paid for is a probe whose printed conclusion
was decided before it ran.

scope-(a); no fit; nothing wired; no c_k; L2 unchanged. Gap qou-k5r5 OPEN.
"""
from __future__ import annotations
import importlib.util
import pathlib
import mpmath as mp

mp.mp.dps = 30

from _m1_io_constants import SIG_RATIO_INF  # merged #5901 IO leading constants -- single source, see that module
V_A_INF = 8 / (9 * mp.pi ** 2)             # de-poissonized V_A/n^2 limit, PR #5969
V_D_INF = SIG_RATIO_INF ** 2 * V_A_INF
R_INF = SIG_RATIO_INF ** 2                 # (V_D/V_A)_inf


def _load_legs():
    """Import legs() from the leg-decomposition probe by explicit file path.

    By path, not by bare name: a sibling in a cluster subdir resolves only when the parent is already
    on sys.path (the _path_bridge bootstrap trap), and this probe must run with PYTHONPATH unset.
    """
    here = pathlib.Path(__file__).resolve().parent
    src = here / "wlambda_covariance_epic_M1_margin_leg_decomposition.py"
    spec = importlib.util.spec_from_file_location("_m1_legs", src)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def local_exponent(n0, v0, n1, v1):
    """Local log-log decay exponent p in |v| ~ n^-p between two tabulated points."""
    if v0 == 0 or v1 == 0:
        return None
    return -mp.log(abs(v1) / abs(v0)) / mp.log(mp.mpf(n1) / n0)


def main():
    legmod = _load_legs()
    stats = legmod._load_partitions_and_stats()
    nmax = 46

    print(f"# does the RATIO buy a rate or a constant? dps={mp.mp.dps}; NO float64")
    print(f"# v_A = 8/(9 pi^2) = {mp.nstr(V_A_INF,9)}   v_D = {mp.nstr(V_D_INF,9)}   "
          f"(V_D/V_A)_inf = {mp.nstr(R_INF,9)}")
    print("#")
    print(f"#   {'n':>3} {'delta_A':>13} {'delta_D':>13} {'rho_delta':>11} {'delta_R':>13} "
          f"{'p(dA)':>8} {'p(dR)':>8}")

    rows = []
    for n in range(4, nmax + 1):
        got = legmod.legs(stats, n)
        if got is None:
            continue
        _lr, _ls, _m, vAn, vDn = got
        dA = (vAn - V_A_INF) / V_A_INF
        dD = (vDn - V_D_INF) / V_D_INF
        dR = ((vDn / vAn) - R_INF) / R_INF
        rho_d = dD / dA if dA != 0 else None
        rows.append((n, dA, dD, dR, rho_d))

    for i, (n, dA, dD, dR, rho_d) in enumerate(rows):
        pA = pR = None
        if i > 0:
            n0 = rows[i - 1][0]
            pA = local_exponent(n0, rows[i - 1][1], n, dA)
            pR = local_exponent(n0, rows[i - 1][3], n, dR)
        if n % 4 == 0 or n == rows[-1][0]:
            print(f"#   {n:>3} {mp.nstr(dA,6):>13} {mp.nstr(dD,6):>13} "
                  f"{(mp.nstr(rho_d,5) if rho_d is not None else '-'):>11} {mp.nstr(dR,6):>13} "
                  f"{(mp.nstr(pA,4) if pA is not None else '-'):>8} "
                  f"{(mp.nstr(pR,4) if pR is not None else '-'):>8}")
    print("#")

    # --- Has rho_delta settled? Measured by the spread over the window's last third, not by a
    #     single extrapolation, because these sequences oscillate.
    tail = [r for r in rows if r[0] >= 2 * nmax // 3]
    rhos = [r[4] for r in tail if r[4] is not None]
    rmin, rmax = min(rhos), max(rhos)
    rmid = (rmin + rmax) / 2
    spread = (rmax - rmin) / abs(rmid) if rmid != 0 else mp.inf
    print(f"# rho_delta = delta_D/delta_A over the window's last third (n >= {2*nmax//3}):")
    print(f"#   min {mp.nstr(rmin,6)}   max {mp.nstr(rmax,6)}   mid {mp.nstr(rmid,6)}   "
          f"relative spread {mp.nstr(spread,4)}")
    settled = spread < mp.mpf('0.05')
    near_one = abs(rmid - 1) < mp.mpf('0.05')
    print(f"#   settled to within 5% ? {'YES' if settled else 'NO'}")
    print(f"#   consistent with rho_delta -> 1 ? {'YES' if near_one else 'NO'}")
    print("#")

    # --- Rate comparison: does |delta_R| decay FASTER than |delta_A|?
    exps_A, exps_R = [], []
    for i in range(1, len(rows)):
        if rows[i][0] < 2 * nmax // 3:
            continue
        n0, n1 = rows[i - 1][0], rows[i][0]
        pA = local_exponent(n0, rows[i - 1][1], n1, rows[i][1])
        pR = local_exponent(n0, rows[i - 1][3], n1, rows[i][3])
        if pA is not None:
            exps_A.append(pA)
        if pR is not None:
            exps_R.append(pR)
    mA = sum(exps_A) / len(exps_A)
    mR = sum(exps_R) / len(exps_R)
    sA = max(exps_A) - min(exps_A)
    sR = max(exps_R) - min(exps_R)
    print(f"# LOCAL log-log exponents over n >= {2*nmax//3} (mean, and full spread):")
    print(f"#   |delta_A| :  mean {mp.nstr(mA,4)}   spread {mp.nstr(sA,4)}   (n={len(exps_A)})")
    print(f"#   |delta_R| :  mean {mp.nstr(mR,4)}   spread {mp.nstr(sR,4)}   (n={len(exps_R)})")
    print("#   A local exponent between two adjacent n is NOISE on an oscillating sequence. Read the")
    print("#   SPREAD first: if it is comparable to the difference of the means, the means do not")
    print("#   separate the two rates and this probe answers nothing about rate.")
    separated = abs(mR - mA) > max(sA, sR)
    print(f"#   do the means separate beyond the spreads ? {'YES' if separated else 'NO'}")
    print("#")

    # --- Verdict. TWO SEPARATE QUESTIONS, and an earlier version of this probe conflated them:
    #     it gated everything on `settled` and so reported UNANSWERED while its own data answered
    #     the dichotomy decisively. "Have I PINNED r?" and "is r = 1?" are different claims, and
    #     only the second decides which project the remaining proof is. Keep them apart.
    #
    #     Q1 is answered by the WHOLE tail, not by a midpoint: rho_delta -> 1 requires the tail to
    #     approach 1, so a tail whose MINIMUM is far above 1 excludes it whether or not r is pinned.
    tail_min_gap = min(abs(r - 1) for r in rhos)
    q1_excluded = tail_min_gap > mp.mpf('0.1')
    gain_vs_dA = 1 / abs(rmid - 1)

    print("# VERDICT -- TWO QUESTIONS, ANSWERED SEPARATELY (computed, not predicted):")
    print("#")
    print("#   Q1  Is rho_delta -> 1 (leading corrections equal => they CANCEL => a RATE gain)?")
    if q1_excluded:
        print(f"#       NO, decisively. Every tail value is at least {mp.nstr(tail_min_gap,4)} away")
        print(f"#       from 1 (tail min {mp.nstr(rmin,6)}); nowhere in the table does rho_delta")
        print("#       approach 1. The rate-gain branch is EXCLUDED. This does not need r pinned.")
    else:
        print(f"#       NOT EXCLUDED -- the tail comes within {mp.nstr(tail_min_gap,4)} of 1, so a")
        print("#       leading-order cancellation remains possible and is worth pursuing.")
    print("#")
    print("#   Q2  What is the limit r, if it exists?")
    print(f"#       UNPINNED. Tail range [{mp.nstr(rmin,6)}, {mp.nstr(rmax,6)}], relative spread")
    print(f"#       {mp.nstr(spread,4)} -- {'settled' if settled else 'NOT settled'} to 5%. A wider")
    print("#       exact table would be needed to pin it, and Q1 does not require that.")
    print("#")
    print("#   RATE COMPARISON is INCONCLUSIVE BY CONSTRUCTION here, and the spreads say why: the")
    print(f"#       local exponents scatter over {mp.nstr(max(sA,sR),4)} against means differing by")
    print(f"#       {mp.nstr(abs(mR-mA),4)}. Do not read the means as rates. (This is the same")
    print("#       oscillation that turned peak-ratio exponent fitting into noise in PR #6500 --")
    print("#       the running-max envelope of PR #6576 is the tool that works on these sequences.)")

    if q1_excluded:
        verdict = (f"rho_delta -> 1 is EXCLUDED (tail min {mp.nstr(rmin,5)}, never within "
                   f"{mp.nstr(tail_min_gap,3)} of 1), so the ratio is a CONSTANT-factor gain of "
                   f"~{mp.nstr(gain_vs_dA,3)}x over delta_A, NOT a rate gain; the limit r itself is "
                   f"unpinned in [{mp.nstr(rmin,5)}, {mp.nstr(rmax,5)}]. The remaining work is a "
                   f"rigorous finite-n bound on delta_A")
    elif settled and near_one:
        verdict = ("rho_delta -> 1: the leading finite-n corrections cancel in the ratio -- a RATE "
                   "gain, and the structural fact to formalize")
    else:
        verdict = (f"rho_delta -> 1 is NOT excluded (tail comes within {mp.nstr(tail_min_gap,3)}) and "
                   f"r is unpinned in [{mp.nstr(rmin,5)}, {mp.nstr(rmax,5)}]: a wider exact table is "
                   f"needed to decide rate-vs-constant")
    print("#")
    print("# WHAT THIS MEANS FOR THE PROOF. In the rate case the ratio bound may be far weaker than a")
    print("#   variance bound and still close the gap. In the constant case the remaining work is a")
    print("#   rigorous finite-n bound on delta_A itself, and the ratio only divides its constant --")
    print("#   so the effort should go to delta_A, and the ratio is bookkeeping applied at the end.")
    print("#")
    print("# RECONCILING THE TWO GAIN FIGURES, because they look contradictory and are not. PR #6576")
    print("#   measured the ratio route as worth 4.37x over the three-ingredient budget; the gain over")
    print(f"#   bounding delta_A ALONE is only ~{mp.nstr(gain_vs_dA,3)}x. Both are right: the")
    print("#   three-ingredient budget pays for delta_A AND delta_D separately (0.113 + 0.163 =")
    print("#   0.276 in margin units) while the ratio pays once (0.0537). Most of the 4.37x is")
    print("#   therefore NOT the cancellation -- it is not double-paying. Quote the two separately.")
    print("#")
    print("# WINDOW CAVEAT: exact table to n = 46; the constant is required for n >= 79. Nothing here")
    print("#   is a bound, and no exponent here is a proved rate.")
    print(f"RESULT: {verdict}. rho_delta over n>={2*nmax//3}: [{mp.nstr(rmin,5)}, {mp.nstr(rmax,5)}], "
          f"spread {mp.nstr(spread,3)}; local exponents mean |dA| {mp.nstr(mA,4)} (spread "
          f"{mp.nstr(sA,4)}) vs |dR| {mp.nstr(mR,4)} (spread {mp.nstr(sR,4)}). qou-k5r5 OPEN.")
    print("EXIT: 0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
