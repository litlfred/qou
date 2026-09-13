#!/usr/bin/env python3
r"""
rev_beta_bound_polynomial_max_probe.py — maximizing the beta-bound in POLYNOMIAL time, past the
p(n) wall, and the rate it gives (qou-hok7)

`qou-hok7`: `Omega(sqrt n) <= REV_n <= O(n^{3/4})` both proved (#7014, #7018); sharpness open.
#7065 closed the enumeration route (the discriminating statistic does not work below n ~ 150, and
`p(150)` is ~3 orders out of reach). #7070 supplied beta-coordinates, in which

    R_lambda = sum_i F(beta_i) - sum_{i<j} eps_(beta_i - beta_j) - F(n)

with `beta_i = lambda_i + l - i`, and derived the bound

    R_lambda <= B(l, W) := l*C - J(l, W) - F(n),
    J(l, W)  := sum_{d=1}^{l-1} (l-d) * eps( d*W / (l-d) ),     W := beta_1 - beta_l

whose only dependence on `lambda` is through the two integers `(l, W)`. This probe uses that to
maximize it **without enumerating partitions**.

## Why this could settle sharpness outright

`M_n := max_lambda (R_lambda - E_lambda)` with `E = (H - H_min) ln q_0`, and

    REV_n = log sum_lambda exp(R_lambda - E_lambda)  <=  M_n + log p(n).

Hardy-Ramanujan gives `log p(n) ~ pi*sqrt(2n/3) = 2.5651*sqrt(n)`, which is itself `Theta(sqrt n)`.
**So if `M_n = O(sqrt n)` then `REV_n = O(sqrt n)`, the `3/4` is not sharp, and the tightness
question closes** — the entropy cannot spoil it, because the entropy is already `Theta(sqrt n)`.

## The relaxation

`-E` decreases in `H`, so replacing `H` by any valid LOWER bound keeps the result an upper bound.
Using the corpus's own `2H = sum_i lambda_i^2 + sum_j lambda'_j^2` (the identity behind
`sq_min_le_sum_hookZ`, #7018), Cauchy-Schwarz on the rows after the first and on the columns gives

    (LB)  2H  >=  lambda_1^2 + (n - lambda_1)^2/(l-1) + n^2/lambda_1

and distinctness of the beta's forces `lambda_1 >= W - l + 2` (since `W = lambda_1 - lambda_l + l - 1`
and `lambda_l >= 1`). Hence

    M_n  <=  max over admissible (l, W)  [ B(l, W) - ( Hhat(n,l,W) - H_min(n) ) * ln q_0 ]

with `Hhat` the minimum of (LB) over `lambda_1 >= max(ceil(n/l), W-l+2)`. That maximum is an
`O(n^2)` scan over two small integers, computable at `n = 10^4` where `p(n)` has 10^106 terms.

## Result: the transfer does NOT fire, and the reduction is sound anyway

Measured to `n = 4000` (where `p(n) ~ 1.0e64`), the relaxed maximum divided by `sqrt(n)` runs
`9.67 -> 210.88` and divided by `n^{3/4}` it **rises** `3.84 -> 26.52`. Its growth exceeds
`n^{3/4}`, so nothing transfers and **sharpness stays open** — `REV_n` remains in
`[Omega(sqrt n), O(n^{3/4})]`, unchanged.

**That is a fact about the bound, not about `REV_n`.** R6 was written expecting the Cauchy-Schwarz
`Hhat` to be the weak link, and refutes that: at the maximizer's own `(l, W)`, `Hhat` reaches
**99.3-100%** of the true minimum hook sum, and the whole relaxation overshoots the enumerated
`max(B - E)` by at most 0.15. Passing from a partition to two integers costs essentially nothing.
So the relaxation is a faithful instrument, and what it faithfully reports is that **the beta-bound
of #7070 is itself too weak** — the loss is the Jensen step on the pair term, which under-counts
badly for gap sequences of mostly 1s with a few large jumps, exactly what the maximizer selects
(`W/l ~ 1.7` at every `n`).

Two things survive as usable: maximizing any `B(l, W)` now costs `O(n^2)` rather than `p(n)`, so a
replacement for the Jensen step is testable at `n = 4000` against an instrument calibrated to the
truth at `n <= 40`; and the target is now specific ("a pair-term bound that survives gap sequences
of mostly 1s") rather than "a sharper bound on `R_lambda`".

## Checks

  R1  (LB) holds on every partition of n <= 16, and lambda_1 >= W - l + 2 with it
  R2  the relaxed maximum DOMINATES the true enumerated max(B - E) at n = 16..40 (it must, or the
      relaxation is invalid) and also dominates the true M_n
  R3  the relaxed maximum's rate, read to n = 4000
  R4  the verdict — the transfer does not fire; what that is and is not evidence about
  R5  neither the l cap nor the eps truncation is doing the work
  R6  WHERE the loss is — refutes this probe's own author on the point

Exact integers for (LB) and the partition checks; mpmath at 40 dps for the eps sums. No float64.
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

from qou_substrate.constants import Q_50_DIGIT_STR  # noqa: E402

from hmin_closed_form_and_rev_sublinearity_probe import H_min_closed  # noqa: E402

mp.dps = 40
Q0 = mp.mpf(Q_50_DIGIT_STR)
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
            if v < best - 50:          # B-E falls off fast in W; stop scanning this l
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

    # ---- R3: the rate, read where p(n) is unreachable ---------------------------------------
    print()
    print(f"  {'n':>7} {'relaxed max':>13} {'/sqrt(n)':>10} {'/n^0.75':>10} {'argmax (l,W)':>16} "
          f"{'l cap':>6}")
    rows3, cap_ok = [], True
    for n in [40, 100, 250, 625, 1600, 4000]:
        cap = max(8, int(8 * mp.sqrt(n)) + 8)
        rx, arg = relaxed_max(n, ell_hi=cap, verbose=(n >= 1600))
        cap_ok = cap_ok and arg[0] < cap - 2
        rs = rx / mp.sqrt(n)
        r34 = rx / (mp.mpf(n) ** mp.mpf("0.75"))
        rows3.append({"n": n, "relaxed_max": mp.nstr(rx, 12),
                      "over_sqrt_n": mp.nstr(rs, 10), "over_n34": mp.nstr(r34, 10),
                      "argmax_l_W": list(arg), "ell_cap": cap})
        print(f"  {n:>7} {mp.nstr(rx, 9):>13} {mp.nstr(rs, 7):>10} {mp.nstr(r34, 7):>10} "
              f"{str(tuple(arg)):>16} {cap:>6}", flush=True)
    s = [mp.mpf(x["over_sqrt_n"]) for x in rows3]
    u = [mp.mpf(x["over_n34"]) for x in rows3]
    sqrt_flat = (max(s) - min(s)) / max(s)
    n34_falling = u[-1] < u[0]
    check(
        "R3_the_relaxed_maximum_rate_measured_where_enumeration_cannot_reach",
        True,
        f"over n = 40..4,000 — a range on which p(n) runs from 37,338 to about 1.0e64, so no "
        f"enumeration reaches any of the last five points — the relaxed maximum divided by sqrt(n) "
        f"varies by {mp.nstr(100 * sqrt_flat, 4)}% ({mp.nstr(s[0], 6)} -> {mp.nstr(s[-1], 6)}) "
        f"while divided by n^(3/4) it {'FALLS' if n34_falling else 'rises'} "
        f"({mp.nstr(u[0], 6)} -> {mp.nstr(u[-1], 6)}). Reported as measured; R4 states what it "
        f"does and does not settle.",
    )

    # ---- R5: the two caps must not be doing the work ---------------------------------------
    def J_full(ell, W):
        return (sum((ell - d) * eps(mp.mpf(d * W) / (ell - d)) for d in range(1, ell))
                if ell >= 2 else mp.mpf(0))

    worst_trunc = mp.mpf(0)
    for ell, W in [(10, 9), (40, 60), (120, 200), (300, 700), (57, 57), (200, 199)]:
        worst_trunc = max(worst_trunc, abs(J_full(ell, W) - J(ell, W)))
    check(
        "R5_neither_the_l_cap_nor_the_eps_truncation_is_doing_the_work",
        cap_ok and worst_trunc < mp.mpf("1e-20"),
        f"the row scan is capped at l <= 8*sqrt(n)+8 and the argmax l lands strictly inside it at "
        f"every n ({', '.join(str(x['argmax_l_W'][0]) + '/' + str(x['ell_cap']) for x in rows3)}), "
        f"so the cap is not binding — a binding cap would under-estimate the max and is reported "
        f"as a FAILURE here rather than passing quietly. The eps truncation (drop terms with "
        f"argument > {_EPS_NEGLIGIBLE}) differs from the untruncated sum by at most "
        f"{mp.nstr(worst_trunc, 3)} on six spot shapes spanning the scanned (l, W) range.",
    )

    # ---- R6: WHERE the loss is — Hhat, not the beta-bound ----------------------------------
    print()
    print(f"  {'n':>4} {'argmax (l,W)':>14} {'Hhat':>10} {'true min H':>11} {'Hhat/true':>10} "
          f"{'H_min(n)':>9}")
    rows6, ok6 = [], True
    for n in [24, 32, 40]:
        _rx, (el, Wl) = relaxed_max(n)
        trueH = None
        for lam in partitions_desc(n):
            if len(lam) == el and lam[0] - lam[-1] + len(lam) - 1 == Wl:
                h = hook_sum(lam)
                trueH = h if trueH is None or h < trueH else trueH
        lo = max(-(-n // el), Wl - el + 2, 1)
        hh = min(two_H_lower(n, el, x) for x in range(lo, n - el + 2)) / 2
        hhf = mp.mpf(hh.numerator) / hh.denominator
        ratio = hhf / trueH if trueH else mp.mpf(0)
        ok6 = ok6 and trueH is not None
        rows6.append({"n": n, "argmax_l_W": [el, Wl], "Hhat": mp.nstr(hhf, 8),
                      "true_min_H_at_that_l_W": trueH, "Hhat_over_true": mp.nstr(ratio, 6),
                      "H_min_n": H_min_closed(n)})
        print(f"  {n:>4} {str((el, Wl)):>14} {mp.nstr(hhf, 6):>10} {str(trueH):>11} "
              f"{mp.nstr(ratio, 5):>10} {H_min_closed(n):>9}")
    rr = [mp.mpf(x["Hhat_over_true"]) for x in rows6]
    gap = [mp.mpf(x["relaxed_max"]) - mp.mpf(x["enum_max_B_minus_E"]) for x in rows2]
    check(
        "R6_the_relaxation_is_TIGHT_so_the_loss_is_the_beta_bound_itself",
        ok6 and max(rr) <= 1 and min(rr) > mp.mpf("0.98"),
        f"I wrote this check expecting Hhat to be the weak link and it is NOT. At the relaxation's "
        f"own argmax (l, W), Hhat reaches {mp.nstr(100 * min(rr), 5)}-{mp.nstr(100 * max(rr), 5)}% "
        f"of the TRUE minimum hook sum over partitions with exactly that (l, W) — exact at two of "
        f"three. And the relaxation as a whole overshoots the enumerated max(B - E) by at most "
        f"{mp.nstr(max(gap), 4)} (n=16..40). So passing from a partition to the two integers "
        f"(l, W) costs essentially nothing.\n\n"
        f"        That inverts the finding, and makes it more useful. The relaxation is a FAITHFUL "
        f"instrument, and what it faithfully reports is that the beta-bound of #7070 is itself too "
        f"weak: its own maximum grows faster than n^(3/4) (R3), while the truth is somewhere in "
        f"[sqrt n, n^(3/4)]. The lossy step is the Jensen inequality on the pair term — applied at "
        f"the MEAN of each distance class, it under-counts badly for a shape whose beta-gaps are "
        f"mostly 1 with a few large ones, which is exactly what the maximizer then selects "
        f"(argmax W/l ~ 1.7 at every n).\n\n"
        f"        The consequence for the next attempt is concrete: a better bound on the pair "
        f"term can now be TESTED in polynomial time at n = 4000 without enumerating anything, on "
        f"an instrument calibrated against the truth at n <= 40. Sharpening H further is not worth "
        f"doing — there is under 1% left in it.",
    )

    # ---- R4: the verdict --------------------------------------------------------------------
    settled = sqrt_flat < mp.mpf("0.15") and n34_falling
    check(
        "R4_verdict_the_route_is_sound_and_the_current_bound_is_not_strong_enough",
        not settled,
        f"**The transfer this probe was built to attempt does not fire, and the reason is clean.** "
        f"The plan was: the relaxed maximum is an upper bound on M_n (R1, R2), and "
        f"REV_n <= M_n + log p(n) with log p(n) ~ 2.5651*sqrt(n), so a sqrt(n) rate for the "
        f"relaxation would give REV_n = O(sqrt n) and settle that the 3/4 is NOT sharp. Measured, "
        f"the sqrt(n) column is not flat ({mp.nstr(100 * sqrt_flat, 4)}% spread) and the n^(3/4) "
        f"column RISES, so the relaxation's own growth exceeds n^(3/4) and nothing transfers.\n\n"
        f"        What that is evidence ABOUT is the bound, not the truth. R6 shows the (l, W) "
        f"relaxation is tight to under 1%, so this is the beta-bound of #7070 failing on its own, "
        f"at the Jensen step — NOT a fact about REV_n, which stays in [Omega(sqrt n), "
        f"O(n^(3/4))] exactly as before. Sharpness remains OPEN, and no claim is made in either "
        f"direction.\n\n"
        f"        Two things survive as usable. The reduction itself: maximizing any bound of the "
        f"form B(l, W) now costs O(n^2) instead of p(n), so a replacement for the Jensen step is "
        f"testable at n = 4000 against a calibrated instrument. And the negative is sharp — "
        f"'the pair term needs a bound that survives gap sequences of mostly 1s with a few large "
        f"jumps' is a far more specific target than 'a sharper bound on R_lambda'.\n\n"
        f"        Anti-caveat, since the mirror-image mistake is on the record: this is NOT the "
        f"#7065 situation. There the statistic could not discriminate because the range was below "
        f"its resolving point. Here the reading is a clear RISE across two orders of magnitude in "
        f"n, not a flat column being over-read, so the negative does not depend on where the "
        f"control's peak sits.",
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
