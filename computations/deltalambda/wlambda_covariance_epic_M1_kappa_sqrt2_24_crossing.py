#!/usr/bin/env python3
"""kappa_n CROSSES sqrt(2)/24 between n = 68 and n = 69 -- the window that decides it is
already committed, and two live claims were written before it existed.

Bean qou-k5r5 (gap), epic qou-x631.  NO NEW COMPUTE: every number here is read out of
computations/deltalambda/b1-kappa-window-extension.json, which holds M_1(n) as an EXACT
rational for n = 68..78.  What is new is the comparison, not the data.

WHY THIS IS WORTH A FILE.  Three claims in the corpus turn on where kappa_n sits relative
to sqrt(2)/24, and they were written at three different times against three different data
ranges:

  1. 2026-08-21-covariance-kernel-M1-kappa-exact-leading-exponent.md, with exact data to
     n = 50, correctly withdrew "kappa trends above sqrt(2)/24" and said no constant is
     confirmed -- "sqrt(2)/24, 1/17 = 0.058824, and neighbours are all within the still-
     moving window".  That was the right call ON THAT DATA.

  2. 2026-08-21-covariance-kernel-M1-kappa-analytic-IO-derivation.md DERIVED
     kappa = 128/(225 pi^2) = 0.0576404956 from the VKLS limit shape, and added a
     parenthetical: "the finite-n data never reaches it because the corrections are large".
     Read as written that says the exact sequence never gets down to sqrt(2)/24.  It does.

  3. Commit 106a6784c5f (2026-09-08) revived the retired constant as a live target:
     "kappa's gap is 0.3 % (~0.0591 vs sqrt(2)/24 = 0.058926)".  Both halves are stale --
     0.0591 is kappa_n in its PEAK region near n = 32, not kappa, and sqrt(2)/24 was
     retired on 2026-08-21 as a fit to n = 400..800 float64 data
     (wlambda_covariance_epic_M1_kappa_structure.py:63 "BOTH ARE WRONG").

The committed n = 68..78 window settles (1) for this constant and refutes (2)'s
parenthetical.  It does NOT settle 1/17: kappa_n is still above it at n = 78.  That
asymmetry is the point -- report which neighbours the window excludes and which it does
not, rather than one verdict for the class.

CONTROL, and it is the reason this is not merely a table re-print: the stored decimal
kappa_n is RECOMPUTED from the stored exact rational M_1 = num/den.  A crossing read off a
decimal field nobody re-derived would be a claim about a serialiser.  If the two disagree
anywhere the probe fails and prints nothing.

NO float64: Fraction for M_1, mpmath at 60 dps for n^{5/2} and the two constants (the only
irrational steps).  float() appears in no arithmetic.
"""
import json
import os
import sys
from fractions import Fraction as F

from mpmath import mp, mpf, nstr, power, sqrt

mp.dps = 60

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
WINDOW = os.path.join(REPO, "computations", "deltalambda",
                      "b1-kappa-window-extension.json")

KAPPA_DERIVED = mpf(128) / (225 * mp.pi ** 2)   # VKLS Chebyshev-mode integral, PR #5428
SQRT2_24 = sqrt(2) / 24                          # RETIRED 2026-08-21; the constant under test
ONE_17 = mpf(1) / 17                             # the audit's other named neighbour


def main():
    if not os.path.exists(WINDOW):
        print(f"FAIL: window file absent: {WINDOW}")
        return 1
    rows = json.load(open(WINDOW))["rows"]

    checks = []

    # -- CONTROL: recompute kappa_n from the exact rational, do not trust the decimal ------
    recomputed = []
    ctrl_ok = True
    worst = mpf(0)
    for r in rows:
        n = r["n"]
        m1 = F(int(r["M1_num"]), int(r["M1_den"]))
        kn = mpf(m1.numerator) / mpf(m1.denominator) / power(n, mpf(5) / 2)
        stored = mpf(r["kappa_n"])
        rel = abs(kn - stored) / stored
        worst = max(worst, rel)
        # the stored field is 26 significant digits; anything beyond serialisation noise fails
        if rel > mpf(10) ** -24:
            ctrl_ok = False
        recomputed.append((n, kn))
    checks.append(("CONTROL: stored kappa_n reproduced from the stored exact rational M_1",
                   ctrl_ok,
                   f"worst relative disagreement over {len(rows)} rows = {nstr(worst, 4)}"))

    if not ctrl_ok:
        for name, ok, detail in checks:
            print(f"[{'PASS' if ok else 'FAIL'}] {name}\n        {detail}")
        return 1

    # -- CONTROL: the window must be strictly decreasing, or "crossing" is not well posed --
    dec = all(recomputed[i][1] > recomputed[i + 1][1] for i in range(len(recomputed) - 1))
    checks.append(("CONTROL: kappa_n strictly decreasing across the window",
                   dec,
                   f"n = {recomputed[0][0]}..{recomputed[-1][0]}; "
                   f"{nstr(recomputed[0][1], 12)} -> {nstr(recomputed[-1][1], 12)}"))

    # -- FINDING 1: the crossing of sqrt(2)/24 ---------------------------------------------
    above = [n for n, k in recomputed if k > SQRT2_24]
    below = [n for n, k in recomputed if k < SQRT2_24]
    crossed = bool(above) and bool(below) and max(above) + 1 == min(below)
    checks.append(("FINDING 1: kappa_n crosses sqrt(2)/24 INSIDE the committed window",
                   crossed,
                   f"above at n = {above}; below at n = {below}; "
                   f"last-above n = {max(above) if above else None}, "
                   f"first-below n = {min(below) if below else None}"))

    # -- FINDING 2: 1/17 is NOT crossed -- the class verdict differs by constant ------------
    still_above_17 = all(k > ONE_17 for _, k in recomputed)
    checks.append(("FINDING 2: 1/17 is NOT crossed by n = 78 -- do not generalise FINDING 1",
                   still_above_17,
                   f"kappa_78 = {nstr(recomputed[-1][1], 12)} vs 1/17 = {nstr(ONE_17, 12)}; "
                   f"margin {nstr((recomputed[-1][1] / ONE_17 - 1) * 100, 4)} %"))

    # -- FINDING 3: the derived limit lies below BOTH, so both are transients ---------------
    below_both = KAPPA_DERIVED < SQRT2_24 and KAPPA_DERIVED < ONE_17
    checks.append(("FINDING 3: the DERIVED limit is below both, so both crossings are forced",
                   below_both,
                   f"kappa = 128/(225 pi^2) = {nstr(KAPPA_DERIVED, 12)} < "
                   f"1/17 = {nstr(ONE_17, 12)} < sqrt(2)/24 = {nstr(SQRT2_24, 12)}"))

    # -- FINDING 4: 0.0591 is a PEAK-region kappa_n, not kappa -----------------------------
    # The peak (n = 32, kappa_32 = 0.0591961) is recorded exactly in
    # m1-kappa-n-exact.witness.json; here we only need that the window sits well below it,
    # which is what makes quoting ~0.0591 as "kappa" wrong by more than the claimed gap.
    peak_region = mpf("0.0591961077")
    gap_claimed = abs(peak_region - SQRT2_24) / peak_region          # the "0.3 %"
    gap_true = abs(recomputed[-1][1] - KAPPA_DERIVED) / KAPPA_DERIVED
    checks.append(("FINDING 4: ~0.0591 is kappa_n near its n=32 peak, not the limit kappa",
                   recomputed[-1][1] < peak_region,
                   f"peak kappa_32 = {nstr(peak_region, 10)}; kappa_78 = "
                   f"{nstr(recomputed[-1][1], 10)}; distance peak->sqrt(2)/24 = "
                   f"{nstr(gap_claimed * 100, 3)} % (the quoted '0.3 %'), but kappa_78 is "
                   f"still {nstr(gap_true * 100, 3)} % above the DERIVED limit"))

    print("kappa_n vs the two retired candidate constants, from the committed exact window")
    print(f"  derived limit  kappa = 128/(225 pi^2) = {nstr(KAPPA_DERIVED, 14)}")
    print(f"  candidate      sqrt(2)/24            = {nstr(SQRT2_24, 14)}   (retired 2026-08-21)")
    print(f"  candidate      1/17                  = {nstr(ONE_17, 14)}   (named, never derived)")
    print()
    print(f"  {'n':>4} {'kappa_n':>26} {'vs sqrt(2)/24':>16} {'vs 1/17':>12}")
    for n, k in recomputed:
        print(f"  {n:>4} {nstr(k, 20):>26} "
              f"{nstr((k / SQRT2_24 - 1) * 100, 5):>16} {nstr((k / ONE_17 - 1) * 100, 5):>12}")
    print()

    for name, ok, detail in checks:
        print(f"[{'PASS' if ok else 'FAIL'}] {name}")
        print(f"        {detail}")

    npass = sum(1 for _, ok, _ in checks if ok)
    print(f"\n{npass}/{len(checks)} checks pass")
    print("\nGap qou-k5r5 stays OPEN.  A constant being excluded is not a bound on kappa_n,")
    print("and this file proves nothing about n > 78.")
    return 0 if npass == len(checks) else 1


if __name__ == "__main__":
    sys.exit(main())
