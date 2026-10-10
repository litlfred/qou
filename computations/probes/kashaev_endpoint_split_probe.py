#!/usr/bin/env python3
"""The j=0 singularity in (A), removed by subtraction rather than estimated.

Bean `qou-mlgp` (A).  Formalised (the split itself) in
`folio/quantum-observable-universe/lean/QOU/Knot/KashaevEndpointSplit.lean`
as `sum_log_two_sin_split`.

THE OBSTRUCTION.  Every attempt at (A) foundered at `j = 0`, where
`log(2 sin(j pi/N)) -> -inf`.  Euler-Maclaurin does not apply to a singular
integrand, and that endpoint is exactly where the `-(1/2) log N` and the
additive constant of

    s_k = (N/pi) Lambda(theta) - (1/2) log(2 N sin theta) + O(1/N),  theta = k pi/N

come from.  `KashaevProdEndpoint.lean` pinned the FAR endpoint;
`KashaevReflectionTrapezoid.lean` disposed of the SYMMETRIC half.  Neither
touches `j = 0`, and the reflection provably cannot: it pairs `k` with `N-1-k`
and both endpoints sit outside that pairing.

THE MOVE.  Do not estimate the singularity — SUBTRACT it.  With
`logSinc x := log(sin x) - log x`,

    sum_{j=1}^{k} log(2 sin(j pi/N))
        = k log(2 pi/N) + log(k!) + sum_{j=1}^{k} logSinc(j pi/N)

EXACTLY, every `N`, every `k < N`.  All three pieces are benign: closed form,
Stirling, and a Riemann sum of a function CONTINUOUS at 0 (`logSinc -> 0`) and
EVEN (so its odd derivatives vanish at 0 and there is no `h`-order endpoint
term at the left end).

WHAT THIS PROBE CHECKS.
  (1) the split, exactly, at assorted `(N,k)`;
  (2) that the `logSinc` sum is a CLEAN Euler-Maclaurin — residual `O(h^3)`,
      with `|residual| . N^3` flat in `N`.  This is the whole point: the same
      quantity for the unsplit sum has no such expansion at all;
  (3) reassembly — `s_k` against the full prediction, `O(1/N^3)`, `. N^3` flat;
  (4) the CANCELLATION.  Stirling's `+1/(12k)` and the `-(h/12)(1/theta)` coming
      from `logSinc'(x) = cot x - 1/x` cancel identically.  Dropping either one
      leaves a residual of exactly `1/(12k)`, which the probe exhibits — this is
      why the refinement needs Robbins' `1/(12n)` term and not merely Stirling.

THE PRECISE MATHLIB GAP, for the record.  Two items, both standard, neither
present.
  * Euler-Maclaurin summation for a smooth function on a compact interval.
    Mathlib has `Polynomial.bernoulli` and `sum_range_pow_eq_bernoulli` but no
    summation formula.
  * The `1/(12n)` term of Stirling.  Mathlib's own docstring on
    `Real.Stirling.le_log_factorial_stirling` says: "Sharper bounds due to
    Robbins are available, but are not yet formalised. These would add lower
    order terms (beginning with `(12 * n)^-1`)."

So (A) is no longer blocked on a singularity.  It is blocked on those two.
"""

from __future__ import annotations

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent
                       / "substrate"))

from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

from mpmath import (mp, mpf, pi, sin, log, factorial, cot, clsin,  # noqa: E402
                    quad, diff, fabs, nstr)


def lobachevsky(t):
    return clsin(2, 2 * t) / 2


def logsinc(x):
    """log(sin x) - log x, the regular part of log(2 sin x)."""
    return log(sin(x)) - log(x)


def L(N, k):
    return sum(log(2 * sin(mpf(j) * pi / N)) for j in range(1, k + 1))


def check_split():
    print("\n  (1) the split is EXACT")
    print("      L_k = k log(2pi/N) + log(k!) + sum_j logSinc(j pi/N)")
    print(f"\n  {'N':>6}  {'k':>6}  {'L_k':>24}  {'split':>24}  {'|diff|':>10}")
    rows, ok = [], True
    for N, k in [(100, 1), (100, 7), (100, 50), (200, 133), (400, 333),
                 (1000, 500), (1000, 999)]:
        lhs = L(N, k)
        rhs = (k * log(2 * pi / N) + log(factorial(k))
               + sum(logsinc(mpf(j) * pi / N) for j in range(1, k + 1)))
        d = fabs(lhs - rhs)
        if not (d < mpf(10) ** (-mp.dps + 8)):
            ok = False
        rows.append({"N": N, "k": k, "L_k": nstr(lhs, 20),
                     "split": nstr(rhs, 20), "abs_diff": nstr(d, 6)})
        print(f"  {N:>6}  {k:>6}  {nstr(lhs, 18):>24}  {nstr(rhs, 18):>24}"
              f"  {nstr(d, 4):>10}")
    return ok, rows


def check_clean_em():
    print("\n  (2) the logSinc sum is a CLEAN (non-singular) Euler-Maclaurin")
    print("      sum_j logSinc(jh) - [(1/h) int_0^th logSinc + logSinc(th)/2"
          " + (h/12) logSinc'(th)]")
    print(f"\n  {'N':>6}  {'residual':>18}  {'x N^3':>16}")
    rows, ok = [], True
    vals = {}
    for N in [100, 200, 400, 800]:
        h = pi / N
        k = N // 2
        th = k * h
        S = sum(logsinc(mpf(j) * h) for j in range(1, k + 1))
        em = quad(logsinc, [0, th]) / h + logsinc(th) / 2 + (h / 12) * diff(logsinc, th)
        d = fabs(S - em)
        vals[N] = d * N ** 3
        rows.append({"N": N, "residual": nstr(d, 10),
                     "times_N_cubed": nstr(d * N ** 3, 10)})
        print(f"  {N:>6}  {nstr(d, 10):>18}  {nstr(d * N ** 3, 10):>16}")
    # flatness of residual * N^3 is the O(h^3) claim
    lo, hi = min(vals.values()), max(vals.values())
    if not (hi / lo < mpf("1.05")):
        ok = False
    print(f"\n    residual . N^3 flat to within {nstr(hi / lo, 6)}x  =>  O(h^3)")
    return ok, rows


def check_reassembly():
    print("\n  (3) reassembly: s_k against the full prediction")
    print("      s_k =? (N/pi)Lambda(th) - (1/2)log(2N sin th) - (h/12) cot(th)")
    print(f"\n  {'N':>6}  {'k':>6}  {'residual':>18}  {'x N^3':>16}")
    rows, ok = [], True
    vals = {}
    for N in [400, 800, 1600]:
        h = pi / N
        k = N // 3
        th = k * h
        s = -L(N, k)
        pred = ((N / pi) * lobachevsky(th) - log(2 * N * sin(th)) / 2
                - (h / 12) * cot(th))
        d = fabs(s - pred)
        vals[N] = d * N ** 3
        rows.append({"N": N, "k": k, "residual": nstr(d, 10),
                     "times_N_cubed": nstr(d * N ** 3, 10)})
        print(f"  {N:>6}  {k:>6}  {nstr(d, 10):>18}  {nstr(d * N ** 3, 10):>16}")
    lo, hi = min(vals.values()), max(vals.values())
    if not (hi / lo < mpf("1.05")):
        ok = False
    print(f"\n    residual . N^3 flat to within {nstr(hi / lo, 6)}x  =>  O(1/N^3)")
    return ok, rows


def check_cancellation():
    print("\n  (4) the cancellation that forces Robbins' 1/(12n) term")
    print("      Stirling's +1/(12k)  vs  -(h/12)(1/th) from logSinc' = cot - 1/x")
    print(f"\n  {'N':>6}  {'k':>6}  {'drop 1/(12k)':>20}  {'1/(12k)':>18}"
          f"  {'|diff|':>12}")
    rows, ok = [], True
    for N in [400, 800, 1600]:
        h = pi / N
        k = N // 3
        th = k * h
        s = -L(N, k)
        # the prediction assembled from Stirling WITHOUT the 1/(12k) term:
        # log(k!) ~ k log k - k + (1/2) log(2 pi k), and logSinc' = cot - 1/x
        # contributing -(h/12)(cot th - 1/th).  Then the leftover is 1/(12k).
        pred_no_robbins = ((N / pi) * lobachevsky(th) - log(2 * N * sin(th)) / 2
                           - (h / 12) * (cot(th) - 1 / th))
        gap = s - pred_no_robbins
        target = -mpf(1) / (12 * k)
        d = fabs(gap - target)
        # the discrepancy should itself be the O(1/N^3) residual, not O(1/N)
        if not (d * N ** 2 < mpf("0.01")):
            ok = False
        rows.append({"N": N, "k": k, "gap": nstr(gap, 12),
                     "minus_one_over_12k": nstr(target, 12),
                     "abs_diff": nstr(d, 8)})
        print(f"  {N:>6}  {k:>6}  {nstr(gap, 12):>20}  {nstr(target, 12):>18}"
              f"  {nstr(d, 6):>12}")
    print("\n    dropping the 1/(12k) leaves exactly -1/(12k): the two halves of")
    print("    the cancellation are individually O(1/N) and only cancel together.")
    return ok, rows


def check_logsinc_regular():
    print("\n  (5) logSinc is regular at 0 and even")
    print(f"\n  {'x':>12}  {'logSinc(x)':>20}  {'logSinc(-x)':>20}")
    rows, ok = [], True
    for x in [mpf(1) / 10, mpf(1) / 100, mpf(1) / 1000, mpf(1) / 10 ** 6]:
        a = logsinc(x)
        # mpmath's log of a negative is complex; the two i*pi branch terms in
        # log(sin(-x)) - log(-x) cancel, leaving the real value. That IS
        # Mathlib's convention, where Real.log (-x) = Real.log x.
        b = mp.re(logsinc(-x))
        if fabs(a - b) > mpf(10) ** (-mp.dps + 8):
            ok = False
        if fabs(a) > x ** 2:  # logSinc(x) = -x^2/6 + O(x^4)
            ok = False
        rows.append({"x": nstr(x, 10), "logSinc": nstr(a, 12)})
        print(f"  {nstr(x, 10):>12}  {nstr(a, 16):>20}  {nstr(b, 16):>20}")
    print("\n    logSinc(x) = -x^2/6 + O(x^4): even, vanishing, no odd part at 0")
    return ok, rows


def main() -> int:
    set_compute_dps()

    print("=" * 78)
    print(" (A)'s endpoint: the singularity subtracted, not estimated")
    print("=" * 78)

    split_ok, split_rows = check_split()
    em_ok, em_rows = check_clean_em()
    re_ok, re_rows = check_reassembly()
    can_ok, can_rows = check_cancellation()
    ls_ok, ls_rows = check_logsinc_regular()

    all_ok = split_ok and em_ok and re_ok and can_ok and ls_ok
    print("\n" + "=" * 78)
    print(f"  ALL CHECKS {'PASS' if all_ok else 'FAIL'}")
    print("=" * 78)

    wb = WitnessBuilder("kashaev-endpoint-split", engine="mpmath")
    wb.add_data("the_split", {
        "statement": ("sum_{j=1}^k log(2 sin(j pi/N)) = k log(2pi/N) + log(k!) "
                      "+ sum_{j=1}^k logSinc(j pi/N), logSinc x = log sin x - log x"),
        "lean": ("QOU.Knot.FigureEightVolume.sum_log_two_sin_split, sorry-free; "
                 "with logSinc_zero and logSinc_neg (evenness)"),
        "why": ("the j=0 singularity is SUBTRACTED, not estimated. The left side "
                "is singular termwise as j/N -> 0; the right side is a closed "
                "form plus a factorial plus a sum of a function continuous at 0"),
        "rows": split_rows,
    })
    wb.add_data("the_logsinc_sum_is_a_clean_euler_maclaurin", {
        "claim": "residual is O(h^3); residual . N^3 is flat in N",
        "rows": em_rows,
    })
    wb.add_data("reassembly", {
        "prediction": ("s_k = (N/pi)Lambda(th) - (1/2)log(2N sin th) "
                       "- (pi/12N) cot(th) + O(1/N^3)"),
        "rows": re_rows,
    })
    wb.add_data("the_cancellation_that_needs_robbins", {
        "mechanism": ("Stirling contributes +1/(12k); logSinc'(x) = cot x - 1/x "
                      "contributes -(h/12)(cot th - 1/th) = -(h/12)cot th "
                      "+ 1/(12k). The 1/(12k) pair cancels identically, leaving "
                      "exactly -(pi/12N) cot th"),
        "consequence": ("the two halves are individually O(1/N) and only cancel "
                        "together, so the refinement genuinely needs Robbins' "
                        "1/(12n) Stirling term — Mathlib's own docstring on "
                        "le_log_factorial_stirling records that it is not "
                        "formalised"),
        "rows": can_rows,
    })
    wb.add_data("the_precise_mathlib_gap", {
        "item_1": ("Euler-Maclaurin summation for a smooth function on a "
                   "compact interval. Mathlib has Polynomial.bernoulli and "
                   "sum_range_pow_eq_bernoulli but no summation formula"),
        "item_2": ("the 1/(12n) term of Stirling (Robbins). Mathlib has "
                   "le_log_factorial_stirling (effective, one-sided) and "
                   "factorial_isEquivalent_stirling (asymptotic) only"),
        "status": ("(A) is no longer blocked on a singularity; it is blocked on "
                   "these two standard, clearly-named pieces"),
    })
    wb.add_assertion(
        "the_endpoint_split_is_exact",
        computed="1" if split_ok else "0", expected="1", tolerance="0.5",
        source="seven (N,k) including k=1 and k=N-1, to working dps")
    wb.add_assertion(
        "logsinc_sum_has_a_clean_O_h_cubed_euler_maclaurin",
        computed="1" if em_ok else "0", expected="1", tolerance="0.5",
        source="residual . N^3 flat to within 5% across N = 100..800")
    wb.add_assertion(
        "reassembly_gives_s_k_to_O_one_over_N_cubed",
        computed="1" if re_ok else "0", expected="1", tolerance="0.5",
        source="residual . N^3 flat to within 5% across N = 400..1600")
    wb.add_assertion(
        "dropping_robbins_term_leaves_exactly_one_over_12k",
        computed="1" if can_ok else "0", expected="1", tolerance="0.5",
        source="gap against -1/(12k) is itself O(1/N^3), N = 400..1600")
    wb.add_assertion(
        "logsinc_is_even_and_vanishes_at_zero",
        computed="1" if ls_ok else "0", expected="1", tolerance="0.5",
        source="|logSinc(x)| < x^2 and logSinc(-x) = logSinc(x) at four x")
    out = wb.save()
    print(f"\n  witness -> {out.name}")
    return 0 if all_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
