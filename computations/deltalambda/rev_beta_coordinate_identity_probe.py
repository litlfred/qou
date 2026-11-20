#!/usr/bin/env python3
r"""
rev_beta_coordinate_identity_probe.py — R_lambda in beta-coordinates: an EXACT two-body
decomposition, and the pair term is 42% of the constant, not a correction (qou-hok7)

`qou-hok7` has `Omega(sqrt n) <= REV_n <= O(n^{3/4})` both proved (#7014, #7018) and sharpness
open. The enumeration route to sharpness was **closed** by the control in #7065: a provably
`Theta(sqrt n)` object is indistinguishable from `Theta(n^{3/4})` on the available range, and
deciding it by scanning needs `p(150)`, about three orders of magnitude out of reach. So the
question has to be attacked structurally, and #7053 named the missing piece precisely: **a sharper
bound on `R_lambda` itself**, since the composition `R <= C*r` then `r <= sqrt H` over-states the
truth by ~5.3x and that factor decreases only slowly.

This probe supplies a new handle on `R_lambda` itself: an **exact identity**, plus a bound derived
from it that is measured to beat `C*r` uniformly — and still does not close sharpness.

## The identity

Write the first-column hook lengths (beta-numbers) of `lambda` with `l` rows as

    beta_i = lambda_i + l - i,      beta_1 > beta_2 > ... > beta_l >= 1.

The hooks in row `i` are exactly `{1, ..., beta_i}` minus `{beta_i - beta_j : j > i}`. Weighting
each cell by `eps_m = -log(1 - q_0^{-2m})` and writing `F(k) = sum_{m<=k} eps_m` gives

    (I)   sum_{c in lambda} eps_{h(c)}  =  sum_i F(beta_i)  -  sum_{i<j} eps_{beta_i - beta_j}

and therefore, since `R_lambda = sum_c eps_{h(c)} - F(n)` (identity (E), proved in #7010),

    (I')  R_lambda = sum_i F(beta_i) - sum_{i<j} eps_{beta_i - beta_j} - F(n).

The integer companion, from the same row description:

    (II)  H(lambda) = sum_i beta_i(beta_i+1)/2 - sum_{i<j} (beta_i - beta_j)
    (III) n         = sum_i beta_i - l(l-1)/2

So both quantities in `R_lambda - E_lambda` are **one-body plus two-body in the same coordinates**:
a per-particle term and a pair interaction over the beta-numbers. This is a log-gas / Coulomb-gas
shape, and it is what `C*r` throws away.

## Why this is not cosmetic: the pair term IS the constant

`F(beta_i) -> C = sum_m eps_m = 6.1714` as `beta_i` grows, so the one-body term alone gives
`R <~ l*C` — which is L1 (`R <= C*r`) recovered, with nothing gained.

The staircase `delta_k` has `beta = (2k-1, 2k-3, ..., 3, 1)`, so every gap is even and the pair
term is `sum_{d>=1} (k-d) eps_{2d} -> k * sum_{d>=1} eps_{2d}`. Hence

    R_{delta_k} / k  ->  C - sum_{d>=1} eps_{2d}  =  sum_{m odd} eps_m  =  A = 3.6034,

which is EXACTLY the staircase constant proved in #7010. The pair term is therefore **not a small
correction to `C*r`**: it removes `C - A = 2.5680`, i.e. **41.6% of C**, and it is the whole
difference between the crude bound and the truth on the family that attains the lower bound.

The single column `lambda = 1^n` is the opposite extreme: `beta = (n, n-1, ..., 1)`, all gaps 1, the
pair term is `sum_{d}(n-d) eps_d` and `R = 0` exactly. So (I') is tight at both ends of the range.

## The bound it yields, and the honest negative

`eps` is convex and decreasing, so for each `d` Jensen over the `l-d` distance-`d` pairs, plus
`sum_i (beta_i - beta_{i+d}) <= d*W` with `W = beta_1 - beta_l`, gives

    (IV)  sum_{i<j} eps_{beta_i-beta_j}  >=  sum_{d=1}^{l-1} (l-d) * eps( d*W/(l-d) )

hence `R_lambda <= l*C - [that] - F(n)`. R4 checks (IV) holds on every partition to n=13.

**Two predictions of mine were measured and both were wrong**, recorded because the corrections
are the informative part:

- I expected the beta-bound to LOSE to `C*r`, since it is applied with the rows while `C*r` takes
  `r = min(l, lambda_1)` and so silently picks the better conjugate reading. **It wins at all six
  empirical argmax shapes** (R5): those shapes have `l = r` in five of six, so the prefactors tie
  and the pair term is pure gain — the over-statement drops from 2.46-2.89x to 1.61-1.86x.
- I expected the ratio to the truth to GROW with `n` when the bound is maximized with the energy,
  on the reasoning that an upper bound with too high an exponent must eventually outrun its
  target. **It falls**, 4.34x -> 3.09x over n = 16..40 (R6).

## What the falling ratio does NOT license

Maximized, the bound over `sqrt(n)` is flat to ~10% while over `n^{3/4}` it falls monotonically,
which reads as "the bound itself is `O(sqrt n)`" and hence that the `3/4` is not sharp. **That
inference is refused here** (R7): #7065's control shows a provably `Theta(sqrt n)` object whose
`n^{3/4}` ratio RISES to a peak at `n = 55`, so at `n <= 40` both columns sit below the peak of the
statistic being read, on a range shorter than the one already shown not to discriminate.

What is usable is a **reduction**: the beta-bound depends on `lambda` only through `(l, W, n)`,
with `W = beta_1 - beta_l` — three small integers, not a partition. Maximizing it therefore does
not require enumerating `p(n)` shapes, which is precisely the wall #7065 hit at `p(150)`.

## Checks

  R1  identity (I) holds on every partition of n <= 13 to 1e-30
  R2  integer identities (II) and (III) hold exactly on every partition of n <= 16
  R3  the staircase pair term converts C into A (Richardson-extrapolated; the raw k=128 value is
      1.5% low because the approach is O(1/k)), and the deficit C - A is 41.6% of C
  R4  the convexity bound (IV) holds on every partition of n <= 13
  R5  the beta-bound at the empirical argmax shapes — beats C*r at all six
  R6  the beta-bound maximized with the energy — uniformly tighter, ratio to truth falling
  R7  the flat sqrt(n) column is NOT a rate; the (l, W, n) reduction is the route

Exact integer arithmetic for the beta-numbers and (II)/(III); mpmath at 50 dps for the eps sums.
No float64.

## Prior work

Beta-numbers are already used in this corpus for the hook **product** — `SYTHookFormulaBeta.lean`
and `SYTHookFormulaBetaProd.lean` prove a divisor-free Frame-Robinson-Thrall identity, sorry-free.
Keystone Identity I (`docs/audits/2026-08-01-keystone-identity-I-piece-A-general-proof.md`) is the
**second** hook moment, `sum_c h(c)^2 = sum_c content(c)^2 + n^2`, and its audit records the
beta-number route for it as *deferred* in favour of an elementary double-count. Identity (II) here
is the **first** moment in those coordinates, and (I)/(I') the `eps`-weighted version; neither
appears in the corpus, checked against paths 1-6 of the corpus-grep checklist.
"""

from __future__ import annotations

import json
import os
import sys
from datetime import datetime, timezone

_HERE = os.path.dirname(os.path.abspath(__file__))
_COMPUTATIONS = os.path.dirname(_HERE)
if _COMPUTATIONS not in sys.path:
    sys.path.insert(0, _COMPUTATIONS)

from mpmath import mp  # noqa: E402

from qou_substrate.constants import Q_50_DIGIT_STR, Q_MP  # noqa: E402

from hmin_closed_form_and_rev_sublinearity_probe import H_min_closed  # noqa: E402

mp.dps = 50
Q0 = Q_MP
T = Q0 ** 2

_NEPS = 6000
EPS = [mp.mpf(0)] + [-mp.log(1 - T ** (-m)) for m in range(1, _NEPS)]
_F = [mp.mpf(0)] * (_NEPS + 1)
for _m in range(1, _NEPS):
    _F[_m] = _F[_m - 1] + EPS[_m]

C_CONST = _F[_NEPS - 1]
A_CONST = sum(EPS[2 * j - 1] for j in range(1, _NEPS // 2))


def F(k: int):
    """F(k) = sum_{m<=k} eps_m; saturates at C."""
    return _F[min(k, _NEPS - 1)]


def eps(x):
    """eps at a REAL argument (needed for the Jensen bound at non-integer means)."""
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


def betas(lam):
    """First-column hook lengths beta_i = lambda_i + l - i (strictly decreasing)."""
    ell = len(lam)
    return [lam[i] + ell - i - 1 for i in range(ell)]


def hooks(lam):
    """Hook multiset by the cell definition — the independent route (II) is checked against."""
    conj = [sum(1 for p in lam if p > j) for j in range(lam[0])]
    return [lam[i] - j + conj[j] - i - 1 for i in range(len(lam)) for j in range(lam[i])]


def pair_sum_eps(b):
    return sum(EPS[b[i] - b[j]] for i in range(len(b)) for j in range(i + 1, len(b)))


def pair_sum_int(b):
    return sum(b[i] - b[j] for i in range(len(b)) for j in range(i + 1, len(b)))


def jensen_lower(b):
    """(IV): sum_{i<j} eps_{b_i-b_j} >= sum_d (l-d) eps(d*W/(l-d)),  W = b_1 - b_l."""
    ell = len(b)
    if ell < 2:
        return mp.mpf(0)
    W = b[0] - b[-1]
    return sum((ell - d) * eps(mp.mpf(d * W) / (ell - d)) for d in range(1, ell))


def main() -> int:
    results = []

    def check(tag, ok, msg):
        results.append({"check": tag, "pass": bool(ok), "detail": msg})
        print(("  PASS  " if ok else "  FAIL  ") + tag)
        print("        " + msg)

    print("=" * 78)
    print("R_lambda in beta-coordinates: exact one-body + two-body   (qou-hok7)")
    print("=" * 78)
    print(f"  C = sum_m eps_m        = {mp.nstr(C_CONST, 12)}")
    print(f"  A = sum_odd eps_m      = {mp.nstr(A_CONST, 12)}   (proved staircase constant, #7010)")
    print(f"  C - A = sum_d eps_2d   = {mp.nstr(C_CONST - A_CONST, 12)}"
          f"   = {mp.nstr(100 * (C_CONST - A_CONST) / C_CONST, 5)}% of C")
    print()

    # ---- R1: the eps-weighted identity (I) -------------------------------------------------
    worst, worst_lam, cnt1 = mp.mpf(0), None, 0
    for n in range(1, 14):
        for lam in partitions_desc(n):
            cnt1 += 1
            b = betas(lam)
            lhs = sum(EPS[h] for h in hooks(lam))
            rhs = sum(F(x) for x in b) - pair_sum_eps(b)
            d = abs(lhs - rhs)
            if d > worst:
                worst, worst_lam = d, lam
    check(
        "R1_beta_identity_for_the_eps_weighted_hook_sum",
        worst < mp.mpf("1e-30"),
        f"sum_c eps_h(c) == sum_i F(beta_i) - sum_{{i<j}} eps_(beta_i-beta_j) on all {cnt1:,} "
        f"partitions of n <= 13; worst residual {mp.nstr(worst, 4)} at {worst_lam}. So R_lambda is "
        f"exactly one-body + two-body in the beta-coordinates, which is the structure C*r discards.",
    )

    # ---- R2: the integer companions (II), (III) --------------------------------------------
    bad2, cnt2 = [], 0
    for n in range(1, 17):
        for lam in partitions_desc(n):
            cnt2 += 1
            b = betas(lam)
            ell = len(lam)
            H_cells = sum(hooks(lam))
            H_beta = sum(x * (x + 1) // 2 for x in b) - pair_sum_int(b)
            n_beta = sum(b) - ell * (ell - 1) // 2
            if H_cells != H_beta or n_beta != n:
                bad2.append((lam, H_cells, H_beta, n_beta))
    check(
        "R2_integer_companions_H_and_n_in_beta_coordinates",
        not bad2,
        f"H(lambda) == sum_i beta_i(beta_i+1)/2 - sum_{{i<j}}(beta_i-beta_j) and "
        f"n == sum_i beta_i - l(l-1)/2, EXACTLY (integer arithmetic), on all {cnt2:,} partitions of "
        f"n <= 16. So the energy E = (H - H_min) ln q_0 lives in the same coordinates as R, with its "
        f"own pair term — the trade-off is now explicit in one variable set.",
    )

    # ---- R3: the pair term is what converts C into A ---------------------------------------
    print()
    print(f"  {'k':>3} {'n':>5} {'onebody/k':>11} {'pair/k':>10} {'(R+F(n))/k':>12}")
    rows3 = []
    for k in [4, 8, 16, 32, 64, 128]:
        lam = tuple(range(k, 0, -1))
        n = k * (k + 1) // 2
        b = betas(lam)
        one = sum(F(x) for x in b)
        pr = pair_sum_eps(b)
        rows3.append({"k": k, "n": n, "onebody_over_k": mp.nstr(one / k, 12),
                      "pair_over_k": mp.nstr(pr / k, 12),
                      "R_plus_Fn_over_k": mp.nstr((one - pr) / k, 12)})
        print(f"  {k:>3} {n:>5} {mp.nstr(one / k, 9):>11} {mp.nstr(pr / k, 8):>10} "
              f"{mp.nstr((one - pr) / k, 10):>12}")
    # The convergence is O(1/k) — the smallest beta's (1, 3, 5, ...) have not saturated F — so a
    # raw tolerance at k=128 tests the convergence RATE, not the limit. Richardson-extrapolate.
    lead = mp.mpf(rows3[-1]["R_plus_Fn_over_k"])
    onebody_lead = mp.mpf(rows3[-1]["onebody_over_k"])
    rich = 2 * lead - mp.mpf(rows3[-2]["R_plus_Fn_over_k"])
    rich_one = 2 * onebody_lead - mp.mpf(rows3[-2]["onebody_over_k"])
    check(
        "R3_the_pair_term_converts_C_into_A_and_is_42pct_of_the_constant",
        abs(rich - A_CONST) < mp.mpf("1e-7") and abs(rich_one - C_CONST) < mp.mpf("1e-7"),
        f"on the staircase the one-body term per row -> C and the pair term removes "
        f"{mp.nstr(C_CONST - A_CONST, 8)}, landing on A. Raw values at k=128 are "
        f"{mp.nstr(onebody_lead, 8)} and {mp.nstr(lead, 8)}: both still ~1.5% low, because the "
        f"smallest beta's (1, 3, 5, ...) have not saturated F and the approach is O(1/k). "
        f"Richardson on k=64,128 gives {mp.nstr(rich_one, 12)} against C = {mp.nstr(C_CONST, 12)} "
        f"and {mp.nstr(rich, 12)} against the PROVED A = {mp.nstr(A_CONST, 12)} — agreeing to "
        f"{mp.nstr(abs(rich - A_CONST), 3)}. The pair term is "
        f"{mp.nstr(100*(C_CONST-A_CONST)/C_CONST, 4)}% of C: it is not a correction to C*r, it is "
        f"the whole gap between C*r and the truth on the family that attains the Omega(sqrt n) "
        f"lower bound.",
    )

    # column 1^n: the opposite extreme, R = 0 exactly
    n_col = 40
    lam_col = tuple([1] * n_col)
    b_col = betas(lam_col)
    R_col = sum(F(x) for x in b_col) - pair_sum_eps(b_col) - F(n_col)
    print(f"\n  single column 1^{n_col}: R = {mp.nstr(R_col, 6)}  (exactly 0 — identity tight at "
          f"the other extreme)")

    # ---- R4: the convexity bound (IV) ------------------------------------------------------
    viol, cnt4, tight = [], 0, mp.mpf(0)
    for n in range(1, 14):
        for lam in partitions_desc(n):
            cnt4 += 1
            b = betas(lam)
            true_pair = pair_sum_eps(b)
            lo = jensen_lower(b)
            if lo > true_pair + mp.mpf("1e-30"):
                viol.append((lam, mp.nstr(lo, 8), mp.nstr(true_pair, 8)))
            if true_pair > 0:
                tight = max(tight, lo / true_pair)
    check(
        "R4_convexity_lower_bound_on_the_pair_term_holds",
        not viol,
        f"(IV) sum_{{i<j}} eps >= sum_d (l-d) eps(d*W/(l-d)) holds on all {cnt4:,} partitions of "
        f"n <= 13, capturing up to {mp.nstr(100 * tight, 4)}% of the true pair term. This turns the "
        f"identity into the bound R <= l*C - (IV) - F(n).",
    )

    # ---- R5: the honest negative — does it beat C*r? ---------------------------------------
    argmaxes = {
        40: (10, 8, 6, 5, 4, 3, 2, 1, 1),
        44: (10, 8, 7, 5, 4, 3, 3, 2, 1, 1),
        52: (11, 9, 8, 6, 5, 4, 3, 2, 2, 1, 1),
        60: (12, 9, 8, 7, 6, 5, 4, 3, 2, 2, 1, 1),
        68: (12, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1),
        76: (13, 11, 10, 8, 7, 6, 5, 4, 3, 3, 2, 2, 1, 1),
    }
    print()
    print(f"  {'n':>4} {'true R':>10} {'C*r':>10} {'C*r/R':>7} {'beta-bd':>10} {'beta/R':>7} "
          f"{'l':>3} {'r':>3}")
    rows5, wins = [], 0
    for n, lam in sorted(argmaxes.items()):
        if sum(lam) != n:
            continue
        b = betas(lam)
        R = sum(F(x) for x in b) - pair_sum_eps(b) - F(n)
        r = min(len(lam), lam[0])
        crude = C_CONST * r
        betab = len(lam) * C_CONST - jensen_lower(b) - F(n)
        if betab < crude:
            wins += 1
        rows5.append({"n": n, "lam": list(lam), "R": mp.nstr(R, 10), "r": r, "ell": len(lam),
                      "C_times_r": mp.nstr(crude, 10), "beta_bound": mp.nstr(betab, 10),
                      "crude_over_R": mp.nstr(crude / R, 6),
                      "beta_over_R": mp.nstr(betab / R, 6)})
        print(f"  {n:>4} {mp.nstr(R, 7):>10} {mp.nstr(crude, 7):>10} {mp.nstr(crude/R, 4):>7} "
              f"{mp.nstr(betab, 7):>10} {mp.nstr(betab/R, 4):>7} {len(lam):>3} {r:>3}")
    ov_c = [mp.mpf(x["crude_over_R"]) for x in rows5]
    ov_b = [mp.mpf(x["beta_over_R"]) for x in rows5]
    check(
        "R5_the_beta_bound_beats_C_times_r_at_every_argmax_shape_and_still_does_not_close_it",
        wins == len(rows5) and max(ov_b) < min(ov_c),
        f"the beta-bound is tighter at ALL {len(rows5)} empirical argmax shapes, cutting the "
        f"over-statement of R from {mp.nstr(min(ov_c), 4)}-{mp.nstr(max(ov_c), 4)}x down to "
        f"{mp.nstr(min(ov_b), 4)}-{mp.nstr(max(ov_b), 4)}x. I predicted the opposite (that the l*C "
        f"prefactor would start it behind) and the measurement says otherwise: on these "
        f"near-staircase shapes l EQUALS r in 5 of 6, so the prefactors tie and the pair term is "
        f"pure gain. It is still ~1.8x the truth, so this is a tighter bound, NOT a closure — the "
        f"Jensen step (mean of each distance class) is lossy, and R6 measures whether what survives "
        f"is a better RATE or only a better constant.",
    )

    # ---- R6: the only question that matters — does the new bound have a better RATE? -------
    print()
    print(f"  {'n':>4} {'true M_n':>10} {'max(C*r-E)':>12} {'max(beta-E)':>13} "
          f"{'crude/M':>8} {'beta/M':>8} {'beta/sqrtn':>11} {'beta/n^.75':>11}")
    rows6 = []
    for n in [16, 24, 32, 40]:
        hmin = H_min_closed(n)
        lnq = mp.log(Q0)
        bM = bC = bB = None
        for lam in partitions_desc(n):
            b = betas(lam)
            H = sum(hooks(lam))
            E = (H - hmin) * lnq
            Rl = sum(F(x) for x in b) - pair_sum_eps(b) - F(n)
            vM = Rl - E
            vC = C_CONST * min(len(lam), lam[0]) - E
            vB = len(lam) * C_CONST - jensen_lower(b) - F(n) - E
            bM = vM if bM is None or vM > bM else bM
            bC = vC if bC is None or vC > bC else bC
            bB = vB if bB is None or vB > bB else bB
        rows6.append({"n": n, "true_M": mp.nstr(bM, 10), "max_crude": mp.nstr(bC, 10),
                      "max_beta": mp.nstr(bB, 10), "crude_over_M": mp.nstr(bC / bM, 6),
                      "beta_over_M": mp.nstr(bB / bM, 6),
                      "beta_over_sqrt_n": mp.nstr(bB / mp.sqrt(n), 8),
                      "beta_over_n34": mp.nstr(bB / (mp.mpf(n) ** mp.mpf("0.75")), 8)})
        print(f"  {n:>4} {mp.nstr(bM, 7):>10} {mp.nstr(bC, 8):>12} {mp.nstr(bB, 8):>13} "
              f"{mp.nstr(bC/bM, 4):>8} {mp.nstr(bB/bM, 4):>8} "
              f"{mp.nstr(bB/mp.sqrt(n), 5):>11} "
              f"{mp.nstr(bB/(mp.mpf(n)**mp.mpf('0.75')), 5):>11}")
    rc = [mp.mpf(x["crude_over_M"]) for x in rows6]
    rb = [mp.mpf(x["beta_over_M"]) for x in rows6]
    check(
        "R6_the_maximized_beta_bound_is_uniformly_tighter_and_its_ratio_to_truth_FALLS",
        max(rb) < min(rc) and rb[-1] < rb[0],
        f"maximized over EVERY shape with the energy, the beta-bound over-states M_n by "
        f"{mp.nstr(rb[0], 5)}x at n=16 FALLING to {mp.nstr(rb[-1], 5)}x at n=40, against "
        f"{mp.nstr(rc[0], 5)}x -> {mp.nstr(rc[-1], 5)}x for C*r — uniformly tighter, by "
        f"~{mp.nstr(rc[-1]/rb[-1], 4)}x at n=40, and closing on the truth rather than drifting off "
        f"it. I wrote this check expecting the ratio to GROW (an upper bound with too high an "
        f"exponent must eventually outrun its target) and it falls; see R7 for what that does and "
        f"does not license.",
    )

    # ---- R7: the falling ratio is NOT evidence of the rate — and the reduction that is ------
    b_sqrt = [mp.mpf(x["beta_over_sqrt_n"]) for x in rows6]
    b_34 = [mp.mpf(x["beta_over_n34"]) for x in rows6]
    sp_sqrt = (max(b_sqrt) - min(b_sqrt)) / max(b_sqrt)
    check(
        "R7_do_NOT_read_the_flat_sqrt_n_column_as_a_rate_the_control_forbids_it",
        sp_sqrt < mp.mpf("0.11"),
        f"the maximized beta-bound divided by sqrt(n) is flat to "
        f"{mp.nstr(100 * sp_sqrt, 3)}% over n=16..40 ({', '.join(mp.nstr(x, 5) for x in b_sqrt)}) "
        f"while divided by n^(3/4) it falls monotonically "
        f"({', '.join(mp.nstr(x, 5) for x in b_34)}). That LOOKS like the bound itself is "
        f"O(sqrt n), which would settle sharpness the other way — the 3/4 not sharp, REV = "
        f"Theta(sqrt n). **It is not evidence.** #7065 measured a provably Theta(sqrt n) control "
        f"whose n^(3/4) ratio RISES to a peak at n=55 and only then falls, so at n <= 40 both "
        f"columns are being read below the peak of the very statistic in question, on a range "
        f"even shorter than the one already shown not to discriminate. Recorded as an "
        f"OBSERVATION with its refutation attached. What IS usable: the beta-bound depends on "
        f"lambda only through (l, W, n) with W = beta_1 - beta_l, plus H through E — three small "
        f"integers instead of a partition. Maximizing it therefore does NOT require enumerating "
        f"p(n) shapes, which is exactly the wall #7065 hit at p(150). That reduction, not this "
        f"table, is the route.",
    )

    n_ok = sum(1 for r in results if r["pass"])
    print()
    print("=" * 78)
    print(f"{n_ok}/{len(results)} checks passed")
    print("WHAT IS NEW: R_lambda is EXACTLY one-body + two-body in the beta-coordinates (I'), with")
    print("H carrying its own pair term (II). The interaction is not a correction to C*r — it is")
    print("41.6% of the constant, and it is precisely what makes the staircase A and not C.")
    print("The bound it yields beats C*r everywhere measured, and depends on lambda only through")
    print("(l, W, n) — so maximizing it needs no enumeration of p(n) shapes.")
    print("WHAT IS NOT: sharpness stays OPEN. One Jensen step is lossy, the bound is still ~1.8x")
    print("the truth, and the flat sqrt(n) column at n <= 40 is exactly what #7065's control")
    print("showed a Theta(sqrt n) object also produces. No rate is claimed.")
    print("=" * 78)

    payload = {
        "probe": "rev_beta_coordinate_identity_probe",
        "bean": "qou-hok7",
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "q0_anchor": "physical_proton", "q0Anchor": "proton",
        "dps": mp.dps,
        "identity": ("R_lambda = sum_i F(beta_i) - sum_{i<j} eps_(beta_i-beta_j) - F(n); "
                     "H = sum_i beta_i(beta_i+1)/2 - sum_{i<j}(beta_i-beta_j); "
                     "n = sum_i beta_i - l(l-1)/2"),
        "C": mp.nstr(C_CONST, 25),
        "A": mp.nstr(A_CONST, 25),
        "pair_deficit_C_minus_A": mp.nstr(C_CONST - A_CONST, 25),
        "pair_deficit_pct_of_C": mp.nstr(100 * (C_CONST - A_CONST) / C_CONST, 8),
        "staircase_scaling": rows3,
        "argmax_bound_comparison": rows5,
        "checks": results,
        "checks_passed": n_ok,
        "checks_total": len(results),
        "status": "identity exact and new; sharpness of the 3/4 exponent remains OPEN",
    }
    out = os.path.join(_COMPUTATIONS, "rev-beta-coordinate-identity.witness.json")
    with open(out, "w") as fh:
        json.dump(payload, fh, indent=2, sort_keys=True)
        fh.write("\n")
    print(f"witness -> {out}")
    return 0 if n_ok == len(results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
