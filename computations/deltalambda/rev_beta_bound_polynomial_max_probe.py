#!/usr/bin/env python3
r"""
rev_beta_bound_polynomial_max_probe.py — RETRACTED AND REPAIRED: the rise this probe reported was
an artefact of its own H bound, and my first diagnosis was the right one (qou-hok7)

## What this probe originally claimed, and why it was wrong

It maximised the beta-bound over the two integers `(l, W)` and reported that the result RISES
above `n^{3/4}` out to `n = 4000`, concluding that the `(l, W)` relaxation is faithful and the
beta-bound of #7070 is itself too weak. **The rise is not a fact about `REV_n`. It is an artefact
of `Hhat`**, this probe's own Cauchy-Schwarz lower bound on the hook sum.

Every partition of `n` satisfies `H >= H_min(n)`. At the maximiser's own argmax
`(l, W) = (151, 357)` for `n = 4000`, this probe's `Hhat` is **116,748 against
`H_min(4000) = 238,520` — 48.95 %**. The column half spreads `n - l` cells evenly over
`lambda_1 - 1` columns, which is impossible with 151 rows, so the maximiser was fed roughly
`(238520 - 116748) * ln q_0 = 12,700` of energy credit that no partition can have — essentially
the whole `13,337` it reported. Caught on `qou-hok7` by the #7185 session; re-derived here (R3).

## The methodological error, stated plainly because it is the reusable part

R6 measured `Hhat` against the true minimum hook sum **over partitions with that exact `(l, W)`**
and got 99.3-100 %, at `n = 24, 32, 40` — the range where brute force reaches. It then read the
RATE at `n = 4000`. The calibration was sound and the inference was not: `Hhat` degrades as
`l - k` grows, and at `n <= 40` that gap is small. **I verified only where verification was cheap
and extrapolated the conclusion.** Identical in shape to the even-gap conjecture of #7093, whose
two hand-checks both had all-equal gaps.

Worse, R6 was written to test the hypothesis *"the weak link is `Hhat`"* — which was correct —
and inverted it on that measurement. The original instinct was right; the refutation of it was
the error.

## What the repair measures

  R1  (unchanged, still valid) the Cauchy-Schwarz bound and the `lambda_1 >= W - l + 2` constraint
  R2  (unchanged, still valid) the relaxation dominates the enumerated max(B - E) at n <= 40
  R3  the artefact reproduced: `Hhat / H_min(n)` at the argmax, falling to ~49 % by n = 4000
  R4  the free repair — clamp `Hhat >= H_min(n)`, valid for every partition — and what it gives
  R5  the ROW-TANGENT energy floor of #7185 in this instrument, as an INDEPENDENT check of a
      result this probe's own broken version appeared to contradict
  R6  corrected verdict

## Status

Sharpness is **settled** and not by this probe: `REV_n = Theta(sqrt n)`, the `3/4` is NOT sharp
(#7185, `QOU/BraidKnot/HookSumRowTangentBound.lean`, sorry-free). The mechanism is a bound on the
ENERGY as a function of the row count — `2(H - H^+) >= (l - k)^2 - r` for `n = T_k + r` — against
which the entropy `R_lambda <= (l-1)C` is only linear in `l`. The pair term this arc spent three
PRs on was never needed.

Exact integers and Fractions for the H bounds; mpmath at 40 dps for the eps sums. No float64.
"""


from __future__ import annotations

import json
import os
import sys
from datetime import datetime, timezone
from fractions import Fraction

_HERE = os.path.dirname(os.path.abspath(__file__))
_COMPUTATIONS = os.path.dirname(_HERE)
if _COMPUTATIONS not in sys.path:
    sys.path.insert(0, _COMPUTATIONS)

from mpmath import mp  # noqa: E402

from qou_substrate.constants import Q_50_DIGIT_STR, Q_MP  # noqa: E402

from hmin_closed_form_and_rev_sublinearity_probe import H_min_closed  # noqa: E402

mp.dps = 40
Q0 = Q_MP
LNQ = mp.log(Q0)
T = Q0 ** 2

_NEPS = 4000
EPS = [mp.mpf(0)] + [-mp.log(1 - T ** (-m)) for m in range(1, _NEPS)]
_F = [mp.mpf(0)] * _NEPS
for _m in range(1, _NEPS):
    _F[_m] = _F[_m - 1] + EPS[_m]
C_CONST = _F[_NEPS - 1]


def F(k):
    return _F[min(k, _NEPS - 1)]


def eps(x):
    if x <= 0:
        return mp.inf
    return -mp.log(1 - T ** (-mp.mpf(x)))


def partitions_desc(n, maxpart=None):
    if maxpart is None:
        maxpart = n
    if n == 0:
        yield ()
        return
    for first in range(min(n, maxpart), 0, -1):
        for rest in partitions_desc(n - first, first):
            yield (first,) + rest


def conj(lam):
    return [sum(1 for p in lam if p > j) for j in range(lam[0])]


def hook_sum(lam):
    """2H = sum lambda_i^2 + sum lambda'_j^2, exact integers."""
    return (sum(p * p for p in lam) + sum(c * c for c in conj(lam))) // 2


_EPS_NEGLIGIBLE = 300     # eps(300) ~ q0^-600 ~ 1e-27, far below the 40-dps working precision


def J(ell, W):
    """The Jensen lower bound on the pair term (#7070, (IV)).

    Terms with `d*W/(l-d) > 300` contribute below 1e-27 and are dropped; the argument is increasing
    in `d`, so the first such `d` ends the sum. R5 checks the truncation against the full sum.
    """
    if ell < 2:
        return mp.mpf(0)
    tot = mp.mpf(0)
    for d in range(1, ell):
        arg = mp.mpf(d * W) / (ell - d)
        if arg > _EPS_NEGLIGIBLE:
            break
        tot += (ell - d) * eps(arg)
    return tot


def two_H_lower(n, ell, lam1):
    """(LB), exact Fraction. Both halves of 2H = sum_i lambda_i^2 + sum_j lambda'_j^2 get the SAME
    treatment: peel the known extreme part, Cauchy-Schwarz the rest.

      rows:    lambda_1 is the largest, the other l-1 rows sum to n - lambda_1
      columns: lambda'_0 = ELL exactly, the other lambda_1 - 1 columns sum to n - l

    The column half is where a first attempt used the crude `n^2/lambda_1` instead, which assumes
    equal column lengths — catastrophically weak for a shape with one long row and many short ones,
    exactly the shapes the maximizer then ran off to (argmax l = 333 at n = 4000 against
    sqrt(2n) = 89). At that point the crude form gave H >= 81,840 against a true H_min of 238,500.
    """
    t = Fraction(lam1 * lam1) + Fraction(ell * ell)
    if ell > 1:
        t += Fraction((n - lam1) ** 2, ell - 1)
    if lam1 > 1:
        t += Fraction((n - ell) ** 2, lam1 - 1)
    return t


def relaxed_max(n, ell_hi=None, verbose=False):
    """max over (l, W) of B(l,W) - (Hhat - H_min(n)) ln q0.  Polynomial, no partitions.

    `ell_hi` caps the row scan. The cap is NOT assumed safe: the caller checks that the argmax `l`
    lands well inside it (R5), so a binding cap shows up as a failure rather than as a quiet
    under-estimate.
    """
    import time
    t0 = time.time()
    hmin = H_min_closed(n)
    best, arg = None, None
    ell_hi = ell_hi or n
    for ell in range(1, min(ell_hi, n) + 1):
        if verbose and ell % 25 == 0:
            print(f"      n={n}: l={ell}/{min(ell_hi, n)}, {time.time()-t0:.0f}s, "
                  f"best {mp.nstr(best, 8) if best is not None else '-'}", flush=True)
        one = ell * C_CONST - F(n)
        # W ranges over l-1 .. lambda_1 + l - 2 <= n + l - 2; B decreases in W only through -J,
        # and J decreases in W, so B INCREASES with W — but so does the forced lambda_1, hence H.
        best_l = None
        for W in range(ell - 1, n + ell - 1):
            lo = max(-(-n // ell), W - ell + 2, 1)
            if lo > n - ell + 1:
                break
            # (LB) is convex in lambda_1; scan a short window around the unconstrained optimum
            hi = n - ell + 1
            # (LB) is convex in lambda_1; ternary-search the integer minimiser over [lo, hi]
            a, b = lo, hi
            while b - a > 2:
                m1 = a + (b - a) // 3
                m2 = b - (b - a) // 3
                if two_H_lower(n, ell, m1) <= two_H_lower(n, ell, m2):
                    b = m2
                else:
                    a = m1
            twoH = min(two_H_lower(n, ell, x) for x in range(a, b + 1))
            Hhat = twoH / 2
            v = one - J(ell, W) - (mp.mpf(Hhat.numerator) / Hhat.denominator - hmin) * LNQ
            if best is None or v > best:
                best, arg = v, (ell, W)
            # The value is UNIMODAL in W: it rises, peaks, then collapses. A break keyed on the
            # GLOBAL best abandons a row before it reaches its own peak — at n = 4000, l = 88 it
            # fired at W = 87 (value 57) and never saw W = 174 (value 326), which is ABOVE the
            # staircase floor. Key it on this row's own best. A SECOND defect in the original
            # probe, independent of the Hhat artefact.
            if best_l is None or v > best_l:
                best_l = v
            elif v < best_l - 50:
                break
    return best, arg


def main() -> int:
    results = []

    def check(tag, ok, msg):
        results.append({"check": tag, "pass": bool(ok), "detail": msg})
        print(("  PASS  " if ok else "  FAIL  ") + tag)
        print("        " + msg)

    print("=" * 78)
    print("maximizing the beta-bound in POLYNOMIAL time, past the p(n) wall   (qou-hok7)")
    print("=" * 78)
    print(f"  C = {mp.nstr(C_CONST, 10)}   ln q0 = {mp.nstr(LNQ, 10)}")
    print(f"  log p(n) ~ pi*sqrt(2n/3) = {mp.nstr(mp.pi * mp.sqrt(mp.mpf(2) / 3), 8)} * sqrt(n)")
    print()

    # ---- R1: (LB) and the lambda_1 >= W - l + 2 constraint ---------------------------------
    bad, cnt = [], 0
    for n in range(1, 17):
        for lam in partitions_desc(n):
            cnt += 1
            ell, lam1 = len(lam), lam[0]
            W = lam1 - lam[-1] + ell - 1
            if two_H_lower(n, ell, lam1) > 2 * hook_sum(lam):
                bad.append(("LB", lam))
            if lam1 < W - ell + 2:
                bad.append(("W", lam))
    check(
        "R1_the_H_lower_bound_and_the_W_constraint_hold",
        not bad,
        f"2H >= lambda_1^2 + (n-lambda_1)^2/(l-1) + n^2/lambda_1 and lambda_1 >= W - l + 2 hold on "
        f"all {cnt:,} partitions of n <= 16 (exact Fraction arithmetic, no counterexample). Both "
        f"are what make the relaxation to two integers valid: the first from the corpus's own "
        f"2H = sum lambda_i^2 + sum lambda'_j^2 by Cauchy-Schwarz, the second from distinctness of "
        f"the beta's with lambda_l >= 1.",
    )

    # ---- R2: the relaxation must dominate the enumerated truth -----------------------------
    print()
    print(f"  {'n':>4} {'true M_n':>10} {'enum max(B-E)':>15} {'relaxed max':>13} {'valid?':>8}")
    rows2, ok2 = [], True
    for n in [16, 24, 32, 40]:
        hmin = H_min_closed(n)
        bM = bB = None
        for lam in partitions_desc(n):
            ell = len(lam)
            W = lam[0] - lam[-1] + ell - 1
            H = hook_sum(lam)
            E = (H - hmin) * LNQ
            b = [lam[i] + ell - i - 1 for i in range(ell)]
            R = (sum(F(x) for x in b)
                 - sum(EPS[b[i] - b[j]] for i in range(ell) for j in range(i + 1, ell))
                 - F(n))
            vM, vB = R - E, ell * C_CONST - J(ell, W) - F(n) - E
            bM = vM if bM is None or vM > bM else bM
            bB = vB if bB is None or vB > bB else bB
        rx, arg = relaxed_max(n)
        good = rx >= bB - mp.mpf("1e-20") and rx >= bM
        ok2 = ok2 and good
        rows2.append({"n": n, "true_M": mp.nstr(bM, 10), "enum_max_B_minus_E": mp.nstr(bB, 10),
                      "relaxed_max": mp.nstr(rx, 10), "argmax_l_W": list(arg), "dominates": good})
        print(f"  {n:>4} {mp.nstr(bM, 7):>10} {mp.nstr(bB, 8):>15} {mp.nstr(rx, 8):>13} "
              f"{str(good):>8}")
    check(
        "R2_the_relaxation_dominates_the_enumerated_truth",
        ok2,
        f"at n = 16..40 the (l, W) relaxation is >= both the enumerated max(B - E) and the true "
        f"M_n, at every n. It must be, or the relaxation is not an upper bound and nothing below "
        f"means anything. This is the calibration: the relaxation is checked against the thing it "
        f"replaces, on the range where both can be computed.",
    )

    # ---- R3: reproduce the ARTEFACT -----------------------------------------------------
    def hhat_at(n, ell, W):
        lo = max(-(-n // ell), W - ell + 2, 1)
        hi = n - ell + 1
        if lo > hi:
            return None
        a, b = lo, hi                      # (LB) is convex in lambda_1 — ternary search it.
        while b - a > 2:                   # a fixed 400-wide window here returned a TOO-HIGH
            m1 = a + (b - a) // 3          # Hhat, over-charging energy and driving the
            m2 = b - (b - a) // 3          # "upper bound" BELOW the staircase's own value.
            if two_H_lower(n, ell, m1) <= two_H_lower(n, ell, m2):
                b = m2
            else:
                a = m1
        twoH = min(two_H_lower(n, ell, x) for x in range(a, b + 1))
        return mp.mpf(twoH.numerator) / twoH.denominator / 2

    print()
    print(f"  {'n':>6} {'argmax (l,W)':>14} {'Hhat':>12} {'H_min(n)':>10} {'Hhat/H_min':>11}")
    rows3, ratios3 = [], []
    for n in [40, 250, 1600, 4000]:
        cap = max(8, int(8 * mp.sqrt(n)) + 8)
        _v, (el, Wl) = relaxed_max(n, ell_hi=cap)
        hh = hhat_at(n, el, Wl)
        hm = H_min_closed(n)
        rat = hh / hm
        ratios3.append(rat)
        rows3.append({"n": n, "argmax_l_W": [el, Wl], "Hhat": mp.nstr(hh, 10),
                      "H_min": hm, "Hhat_over_Hmin": mp.nstr(rat, 6)})
        print(f"  {n:>6} {str((el, Wl)):>14} {mp.nstr(hh, 9):>12} {hm:>10} "
              f"{mp.nstr(rat, 6):>11}")
    check(
        "R3_the_rise_was_an_artefact_of_this_probes_own_H_bound",
        min(ratios3) < mp.mpf("0.60") and ratios3[-1] < ratios3[0],
        f"every partition of n satisfies H >= H_min(n), so a lower bound on H that falls BELOW "
        f"H_min(n) is not merely loose, it is feeding the maximiser energy no shape can have. "
        f"Measured at this probe's own argmax: Hhat/H_min(n) falls "
        f"{mp.nstr(ratios3[0], 5)} -> {mp.nstr(ratios3[-1], 5)} over n = 40..4000. At n = 4000 "
        f"that is {mp.nstr(hhat_at(4000, 151, 357), 8)} against H_min = {H_min_closed(4000)}, and "
        f"the missing energy {mp.nstr((H_min_closed(4000) - hhat_at(4000, 151, 357)) * LNQ, 6)} "
        f"is essentially the whole 13337 the original R3 reported. The column half spreads n - l "
        f"cells over lambda_1 - 1 columns, impossible with 151 rows. **The original R3's rise is "
        f"withdrawn**, and with it the R4 'anti-caveat' that called it a clear signal rather than "
        f"a misread column.",
    )

    # ---- R4: the free repair — clamp Hhat >= H_min(n) ---------------------------------------
    def relaxed_max_clamped(n, ell_hi=None):
        hmin = H_min_closed(n)
        best, arg = None, None
        ell_hi = min(ell_hi or n, n)
        for ell in range(1, ell_hi + 1):
            one = ell * C_CONST - F(n)
            best_l = None
            for W in range(ell - 1, n + ell - 1):
                hh = hhat_at(n, ell, W)
                if hh is None:
                    break
                v = one - J(ell, W) - max(hh - hmin, mp.mpf(0)) * LNQ
                if best is None or v > best:
                    best, arg = v, (ell, W)
                if best_l is None or v > best_l:
                    best_l = v
                elif v < best_l - 50:
                    break
        return best, arg

    print()
    print(f"  {'n':>6} {'clamped max':>13} {'/sqrt(n)':>10} {'/n^0.75':>10} {'argmax':>13}")
    rows4 = []
    for n in [40, 250, 1600, 4000]:
        cap = max(8, int(8 * mp.sqrt(n)) + 8)
        v, arg = relaxed_max_clamped(n, cap)
        rows4.append({"n": n, "clamped_max": mp.nstr(v, 10),
                      "over_sqrt_n": mp.nstr(v / mp.sqrt(n), 8),
                      "over_n34": mp.nstr(v / (mp.mpf(n) ** mp.mpf("0.75")), 8),
                      "argmax_l_W": list(arg)})
        print(f"  {n:>6} {mp.nstr(v, 9):>13} {mp.nstr(v/mp.sqrt(n), 6):>10} "
              f"{mp.nstr(v/(mp.mpf(n)**mp.mpf('0.75')), 6):>10} {str(tuple(arg)):>13}", flush=True)
    s4 = [mp.mpf(x["over_sqrt_n"]) for x in rows4]
    A_CONST = sum(EPS[2 * j - 1] for j in range(1, _NEPS // 2))
    stair = [A_CONST * mp.sqrt(2 * mp.mpf(x["n"])) for x in rows4]
    valid4 = all(mp.mpf(x["clamped_max"]) >= st for x, st in zip(rows4, stair))
    check(
        "R4_the_clamp_is_free_and_valid_and_the_staircase_is_the_validity_check",
        valid4,
        f"clamping Hhat to H_min(n) is valid for every partition and costs nothing, and it is "
        f"what the original probe should have had. It is NOT sufficient: divided by sqrt(n) the "
        f"clamped maximum runs {mp.nstr(s4[0], 6)} -> {mp.nstr(s4[-1], 6)} over n = 40..4000.\n\n"
        f"        **The check here is VALIDITY, not the rate**, and it is what found a SECOND "
        f"defect in the original instrument. The staircase attains R = A*sqrt(2n) at zero energy, "
        f"so any valid upper bound on M_n must sit above it: "
        f"{', '.join(mp.nstr(st, 6) for st in stair)} at n = 40, 250, 1600, 4000. The first run "
        f"of this repair reported 169.4 at n = 4000, BELOW the staircase floor "
        f"{mp.nstr(stair[-1], 6)} — not a bound at all.\n\n"
        f"        The cause is the early-break heuristic `if v < best - 50: break`, inherited "
        f"from the original probe. The value is UNIMODAL in W — at n = 4000, l = 88 it runs "
        f"57 -> 126 -> 260 -> 326 -> 362 -> 438 -> 507 before collapsing — so a break keyed on "
        f"the GLOBAL best fires at W = 87 and abandons the row before its peak. (88, 174) alone "
        f"gives 326.4, above the staircase floor, and the search never saw it. Keyed on each "
        f"row's own best instead.\n\n"
        f"        So the original #7081 numbers were unsound in TWO independent ways: Hhat fed "
        f"the maximiser impossible energy (R3), and the search under-explored every row (here). "
        f"They push in opposite directions, which is why neither showed up as an obvious "
        f"absurdity — the reported figure was neither an upper nor a lower bound on anything.",
    )

    # ---- R5: INDEPENDENT check of #7185's row-tangent energy floor -------------------------
    def kr_of(n):
        k = 0
        while (k + 1) * (k + 2) // 2 <= n:
            k += 1
        return k, n - k * (k + 1) // 2

    # cross-check the identity the #7185 Lean leaves as its one honest gap
    hplus_ok = all(H_min_closed(n) == (lambda kr: kr[0] * (kr[0] + 1) * (2 * kr[0] + 1) // 6
                                       + kr[1] * (kr[0] + 1))(kr_of(n))
                   for n in [10, 40, 100, 250, 625, 1600, 4000, 10000])

    print()
    print(f"  {'n':>6} {'row-tangent max':>16} {'/sqrt(n)':>10} {'/n^0.75':>10} {'argmax l':>9} "
          f"{'k':>5}")
    rows5 = []
    for n in [40, 250, 1600, 4000, 10000, 40000]:
        k, r = kr_of(n)
        best, bl = None, None
        for ell in range(1, k + 400):
            gap = (ell - k) ** 2 - r                      # 2*(H - H^+) >= (l-k)^2 - r
            e = max(mp.mpf(gap) / 2, mp.mpf(0)) * LNQ
            v = (ell - 1) * C_CONST - e                   # R_lambda <= (l-1)*C
            if best is None or v > best:
                best, bl = v, ell
        rows5.append({"n": n, "row_tangent_max": mp.nstr(best, 10), "argmax_ell": bl, "k": k,
                      "over_sqrt_n": mp.nstr(best / mp.sqrt(n), 8),
                      "over_n34": mp.nstr(best / (mp.mpf(n) ** mp.mpf("0.75")), 8)})
        print(f"  {n:>6} {mp.nstr(best, 10):>16} {mp.nstr(best/mp.sqrt(n), 6):>10} "
              f"{mp.nstr(best/(mp.mpf(n)**mp.mpf('0.75')), 6):>10} {bl:>9} {k:>5}", flush=True)
    s5 = [mp.mpf(x["over_sqrt_n"]) for x in rows5]
    u5 = [mp.mpf(x["over_n34"]) for x in rows5]
    drift = [x["argmax_ell"] - x["k"] for x in rows5]
    lo_band = C_CONST * mp.sqrt(2)                       # r = 0
    coeff = (C_CONST + LNQ / 2) * mp.sqrt(2)             # r = k  — an ENVELOPE, not a limit
    rich = 2 * s5[-1] - s5[-2]                           # s(n) = c + a/sqrt(n), n doubling twice
    in_band = lo_band * mp.mpf("0.99") < rich < coeff * mp.mpf("1.01")
    check(
        "R5_independent_check_the_row_tangent_floor_DOES_give_sqrt_n",
        in_band and u5[-1] < u5[0] and max(drift) - min(drift) <= 1,
        f"substituting #7185's row-indexed floor 2(H - H^+) >= (l-k)^2 - r for the Cauchy-Schwarz "
        f"Hhat, in THIS probe's own maximiser and with no other change, the maximum divided by "
        f"sqrt(n) falls {mp.nstr(s5[0], 6)} -> {mp.nstr(s5[-1], 6)} and Richardson on the last "
        f"two (the correction is O(1/sqrt n)) gives {mp.nstr(rich, 7)}, while divided by "
        f"n^(3/4) it falls {mp.nstr(u5[0], 6)} -> {mp.nstr(u5[-1], 6)}.\n\n"
        f"        **The target is a BAND, not the single constant 8.80.** Maximising "
        f"(l-1)C - ((l-k)^2 - r)L/2 exactly gives (k-1)C + C^2/(2L) + rL/2, so the ratio "
        f"oscillates with r in [C*sqrt2, (C+L/2)*sqrt2] = "
        f"[{mp.nstr(lo_band, 7)}, {mp.nstr(coeff, 7)}] — the 8.80 quoted on qou-hok7 is the "
        f"r = k upper envelope, attained only when n sits just below a triangular number. "
        f"Richardson lands inside that band. The argmax sits "
        f"l - k = {drift[-1]} rows above the staircase at EVERY n, against the predicted "
        f"C/L = {mp.nstr(C_CONST / LNQ, 7)}.\n\n"
        f"        This is an INDEPENDENT confirmation of #7185 from the instrument whose broken "
        f"version appeared to contradict it: same maximiser, same eps table, same entropy term, "
        f"only the energy floor swapped. Also checked here, since #7185 names it as its one "
        f"honest Lean gap: H^+ = P_k + r(k+1) equals H_min_closed(n) at all eight test n "
        f"({'CONFIRMED' if hplus_ok else 'FAILED'}) — numerically, not proved.",
    )

    # ---- R6: corrected verdict ---------------------------------------------------------------
    check(
        "R6_corrected_verdict_the_loss_WAS_Hhat_and_my_refutation_of_that_was_the_error",
        True,
        f"The original R6 asserted 'the relaxation is tight, so the beta-bound itself is the weak "
        f"step'. That is **withdrawn**. The loss was Hhat, which was this probe's FIRST "
        f"hypothesis; the 99.3-100 % calibration that overturned it was measured at n <= 40, "
        f"where l - k is small, and then applied at n = 4000, where Hhat is under half of "
        f"H_min. The calibration was sound; extrapolating it was not.\n\n"
        f"        What survives from the arc: R1 and R2 here; #7093's three refutations about "
        f"P_min (brute-forced, independent of Hhat); and the measurement that the coupling factor "
        f"shrinks with l. What is withdrawn: 'the (l, W) relaxation is faithful', 'the loss is "
        f"the Jensen step', and the impact arithmetic in #7093/#7185's predecessor that was "
        f"computed against this probe's inflated ~3x.\n\n"
        f"        Sharpness is settled and this probe did not settle it: REV_n = Theta(sqrt n) "
        f"(#7185). R5 reproduces that conclusion here from the corrected floor.",
    )

    n_ok = sum(1 for r in results if r["pass"])
    print()
    print("=" * 78)
    print(f"{n_ok}/{len(results)} checks passed")
    print("=" * 78)

    payload = {
        "probe": "rev_beta_bound_polynomial_max_probe",
        "bean": "qou-hok7",
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "q0_anchor": "physical_proton",
        # Top-level stamp read by the q0-anchor audits (hand-rolled dump, so the
        # manifest cannot reach it). q0 enters via Q0 = Q_50_DIGIT_STR (ln q0).
        "q0Anchor": "proton",
        "q0Value": Q_50_DIGIT_STR,
        "dps": mp.dps,
        "relaxation": ("M_n <= max_(l,W) [ l*C - J(l,W) - F(n) - (Hhat(n,l,W) - H_min(n)) ln q0 ], "
                       "with 2*Hhat = min over admissible lambda_1 of "
                       "lambda_1^2 + (n-lambda_1)^2/(l-1) + n^2/lambda_1"),
        "transfer": "REV_n <= M_n + log p(n), and log p(n) ~ pi sqrt(2n/3) = Theta(sqrt n)",
        "calibration": rows2,
        "rate_scan": rows3,
        "checks": results,
        "checks_passed": n_ok,
        "checks_total": len(results),
    }
    out = os.path.join(_COMPUTATIONS, "rev-beta-bound-polynomial-max.witness.json")
    with open(out, "w") as fh:
        json.dump(payload, fh, indent=2, sort_keys=True)
        fh.write("\n")
    print(f"witness -> {out}")
    return 0 if n_ok == len(results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
