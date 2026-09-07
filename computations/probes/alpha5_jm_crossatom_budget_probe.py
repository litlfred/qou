#!/usr/bin/env python3
"""Is the alpha_5 atom-independence test measuring c_5, or the weight's drift?

Bean `qou-oots`, closing the last untriaged file of the corrected blast radius
(PR #6840: 11 of 37, not 4 of 36).

THE SETUP. `alpha/alpha_5_jucys_murphy_central.py` tests whether the
Jucys-Murphy central scalar c_5 is ATOM-INDEPENDENT, by comparing

    alpha_5(A) = SUM_{lam |- 3A, ht(lam)=6} w_lam(q) * c_5(lam),
    w_lam = dim_q(lam)^2 / [n]_q!,   n = 3A

across A = 2, 3, 4 and reporting the relative spread. Because n = 3A, this is a
CROSS-ATOM comparison at three DIFFERENT n.

WHY THAT IS THE ONE PLACE THIS WEIGHT MAY NOT GO. Two corpus results, neither
of them mine, say so already:

  - AGENTS.md, notation register: "SUM_lam w_lam(q) is NOT [1] -- measured
    0.987 / 0.982 / 0.982 / 0.991 / 1.111 / 1.517 at n = 3/4/5/6/9/12. That
    defect is structural, not a q-integer-convention artifact ... so it does
    not cancel across different n and distorts any CROSS-ATOM metric -- n = 3A.
    Cross-atom consumers use the self-normalised d_q^2/D^2."
  - `qou-oots` requirement R2 (`crossRatio_smul`, Lean): w -> k_n w multiplies
    the cross-nucleus metric by k_1/k_2, so the normaliser must be
    n-INDEPENDENT => SCOPE-(b) exclusion of dim_q^2/[n]_q! for cross-nucleus
    use. It stays valid SAME-n, by `WLambdaNormalizationInvariance.ratio_invariant`.

n = 3A at A = 2,3,4 is n = 6,9,12 -- the exact three n at which that quoted
sequence reads 0.991, 1.111, 1.517.

WHAT THIS PROBE MEASURES, and it is a narrower quantity than that sequence. The
producer restricts to HEIGHT-6 partitions, so the relevant total is not the full
SUM_lam but the height-6 partial budget

    B_6(A) = SUM_{lam |- 3A, ht(lam)=6} dim_q(lam)^2 / [3A]_q!

If B_6 varies across A, then alpha_5(A) is a product of a varying total mass and
a c_5 average, and a spread in alpha_5 does not distinguish "c_5 moved" from
"the budget moved". The decomposition is exact and is checked here:

    alpha_5(A) = B_6(A) * <c_5>_A,      <c_5>_A = SUM w c_5 / SUM w

and <c_5>_A is precisely what the producer's own third route,
`alpha_5_at_A_partial_normalized`, already computes -- the route its docstring
calls "the structurally derived normaliser". So the fix, if one is needed, is
not new code; it is a choice among routes the producer already has.

THE ANSWER, and it makes this finding SMALLER rather than larger. The budget
confound is real as arithmetic -- B_6 spreads 222x across A = 2,3,4, and the
factorisation is exact -- but it does NOT overturn anything, because the
producer's conclusion is a NEGATIVE and every one of its three routes reaches
it. Run on `main`, its own stdout:

    Atom-independence (NORMALIZED by [3A]_q!)  relative spread   482.16 %
    Atom-independence (RAW)                    relative spread    83.163894
    q-sweep, partial-norm (self-normalised)    relative spread  1327.18 %
    VERDICT: strongly atom-dependent (mechanism orthogonal to JM-central)

So the weight-family choice cannot rescue or overturn this result: the answer is
"not atom-independent" under the excluded weight, under the raw sum, and under
the self-normalised route that qou-oots R2 says is the admissible one. The file
is AFFECTED IN PRINCIPLE (it does use dim_q^2/[n]_q! in a cross-atom metric,
which is the scope-(b)-excluded use) and IMMATERIAL IN FACT (its conclusion is
route-invariant). Recorded that way rather than as a distortion finding, because
that is what the measurement says.

VERIFIED AGAINST THE PRODUCER, not merely modelled on it. This probe's raw
alpha_5 reproduces the producer's printed values at all three A
(5.608246e-04 / 1.978017e+00 / 1.645002e+02) and its self-normalised column
reproduces the producer's partial-norm c_5 at q_0 (0.4704417 / 42.94229), so
the decomposition below is a decomposition OF the producer's quantity.

CAUTION on comparing spreads. The producer reports relative spread as
range/median; this probe reports max/min. They are different statistics and
both are quoted above under their own names -- do not read one as a correction
of the other.

No float64: mpmath end to end, partitions and hook lengths exact integers.
"""

from __future__ import annotations

import sys as _sys
from pathlib import Path as _Path

_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from mpmath import mp  # noqa: E402

from _precision import set_compute_dps, fmt  # noqa: E402
from qou_substrate.witness import WitnessBuilder  # noqa: E402
from qou_substrate.constants import Q_50_DIGIT_STR  # noqa: E402

_sys.path.insert(0, str(_Path(__file__).resolve().parent))
import molien_feray_meliot_bridge_probe as MB  # noqa: E402
import plancherel_deformation_uniqueness_probe as PU  # noqa: E402

A_VALUES = (2, 3, 4)
HEIGHT = 6  # the stratum the producer restricts to


def cell_contents(shape: tuple[int, ...]) -> list[int]:
    return [j - i for i in range(len(shape)) for j in range(shape[i])]


def e5_central(shape: tuple[int, ...], q: mp.mpf) -> mp.mpf:
    """5th elementary symmetric polynomial in {q^{2c} : cells}, as the producer.

    Newton/generating-function form rather than C(len,5) subsets: at n = 12 the
    explicit enumeration is 792 products per partition, and e_5 is the q^5
    coefficient of prod(1 + x*q^{2c}), which is O(cells * 5).
    """
    cells = cell_contents(shape)
    if len(cells) < 5:
        return mp.mpf(0)
    e = [mp.mpf(1)] + [mp.mpf(0)] * 5
    for c in cells:
        v = q ** (2 * c)
        for k in range(5, 0, -1):
            e[k] = e[k] + e[k - 1] * v
    return e[5]


def main() -> int:
    set_compute_dps()
    q0 = mp.mpf(Q_50_DIGIT_STR)

    b = WitnessBuilder("alpha5-jm-crossatom-budget")
    b.set_description(
        "Bean qou-oots. alpha/alpha_5_jucys_murphy_central.py tests "
        "atom-independence of the Jucys-Murphy central scalar c_5 by comparing "
        "SUM_{lam |- 3A, ht=6} w_lam c_5(lam) across A = 2,3,4 with "
        "w_lam = dim_q^2/[n]_q!. Since n = 3A that is a CROSS-ATOM comparison "
        "at three different n, which is the one use AGENTS.md's notation "
        "register and qou-oots requirement R2 both exclude for this weight "
        "(SUM_lam w_lam(q) is not constant in n; scope-(b), n-independence "
        "required). This probe measures the HEIGHT-6 PARTIAL budget "
        "B_6(A) = SUM_{ht=6} dim_q^2/[3A]_q! at each A, and verifies the exact "
        "decomposition alpha_5(A) = B_6(A) * <c_5>_A. If B_6 varies across A, "
        "a spread in alpha_5 cannot distinguish 'c_5 moved' from 'the budget "
        "moved'. <c_5>_A is the producer's OWN third route "
        "(alpha_5_at_A_partial_normalized), which its docstring already calls "
        "'the structurally derived normaliser'. NOT a claim that the "
        "atom-independence conclusion is wrong -- which route it is read off "
        "decides that, and the producer reports three."
    )
    b.add_parameter("q0_50dps", Q_50_DIGIT_STR)
    b.add_parameter("A_values", str(list(A_VALUES)))
    b.add_parameter("height_stratum", str(HEIGHT))

    per_A = {}
    budgets, averages, raws = {}, {}, {}
    for A in A_VALUES:
        n = 3 * A
        qfact = PU.q_factorial(q0, n)
        shapes = [s for s in MB.partitions(n) if len(s) == HEIGHT]
        num = mp.mpf(0)   # SUM w * c_5
        den = mp.mpf(0)   # SUM w  == B_6
        for s in shapes:
            w = PU.dim_q(q0, s) ** 2 / qfact
            num += w * e5_central(s, q0)
            den += w
        avg = num / den if den != 0 else mp.mpf(0)
        budgets[A], averages[A], raws[A] = den, avg, num
        per_A[str(A)] = {
            "n": n,
            "height6_partitions": len(shapes),
            "B_6_partial_budget": fmt(den),
            "alpha_5_raw": fmt(num),
            "c5_average_self_normalised": fmt(avg),
        }
    b.add_data("per_A", per_A)

    def spread(d):
        vs = [abs(d[A]) for A in A_VALUES]
        return max(vs) / min(vs) if min(vs) != 0 else None

    s_budget = spread(budgets)
    s_raw = spread(raws)
    s_avg = spread(averages)
    b.add_data("cross_atom_spreads", {
        "B_6_budget_max_over_min": fmt(s_budget),
        "alpha_5_raw_max_over_min": fmt(s_raw),
        "c5_average_max_over_min": fmt(s_avg),
        "note": "The budget column is the confound. alpha_5 = B_6 * <c_5>, so "
                "any spread in B_6 propagates into the raw comparison whether "
                "or not c_5 moved at all. The self-normalised column is the "
                "quantity that is invariant under a lambda-independent "
                "rescaling of w (qou-oots R2 / ratio_invariant) and is "
                "therefore the one a cross-atom test can be read off.",
    })

    # -- the decomposition is exact, not approximate ---------------------------
    worst = mp.mpf(0)
    for A in A_VALUES:
        recon = budgets[A] * averages[A]
        rel = abs(recon - raws[A]) / abs(raws[A]) if raws[A] != 0 else mp.mpf(0)
        worst = max(worst, rel)
    b.add_assertion(
        "alpha5_factorises_exactly_as_budget_times_average",
        computed=fmt(worst), expected="0", tolerance="1e-40",
        unit="relative",
        source="alpha_5(A) = B_6(A) * <c_5>_A holds identically by definition "
               "of the weighted average; checked numerically so that the "
               "confound claim rests on an identity that was evaluated, not "
               "merely asserted.",
    )

    # -- the part that decides the triage -------------------------------------
    # The producer's own three routes, from its stdout on main. Quoted rather
    # than recomputed: the point is what the PRODUCER concludes, and a
    # re-derivation here would be evidence about this probe instead.
    b.add_data("producer_route_invariance", {
        "normalized_by_qfactorial_rel_spread_pct": "482.16",
        "raw_rel_spread": "83.163894",
        "partial_selfnorm_rel_spread_pct": "1327.18",
        "producer_verdict": "strongly atom-dependent (mechanism orthogonal to "
                            "JM-central)",
        "spread_statistic": "The producer reports range/median; this probe's "
                            "own columns report max/min. Different statistics, "
                            "both quoted under their own names -- neither is a "
                            "correction of the other.",
        "triage": "AFFECTED IN PRINCIPLE, IMMATERIAL IN FACT. The file does use "
                  "dim_q^2/[n]_q! in a cross-atom (n = 3A) metric, which is the "
                  "use AGENTS.md's notation register and qou-oots R2 both "
                  "exclude scope-(b). But its conclusion is a NEGATIVE reached "
                  "identically by all three of its routes -- including the "
                  "self-normalised one R2 admits -- so the weight-family choice "
                  "cannot rescue or overturn it. The Molien ruling does not "
                  "require a change here.",
    })

    b.add_assertion(
        "budget_is_not_constant_across_atoms",
        computed="1" if s_budget > mp.mpf("1.01") else "0",
        expected="1",
        source=f"B_6 max/min = {fmt(s_budget)} across A = {list(A_VALUES)} "
               f"(n = 6, 9, 12). A constant budget would make the raw and "
               f"self-normalised comparisons equivalent; a varying one means "
               f"they are different tests. Threshold is a legibility floor, "
               f"not a physical scale.",
    )

    b.save()

    print(f"q0 = {Q_50_DIGIT_STR[:16]}   stratum: height {HEIGHT}\n")
    print(f"{'A':>2} {'n':>3} {'#ht6':>5}  {'B_6 (budget)':>24}  "
          f"{'alpha_5 raw':>24}  {'<c_5> self-norm':>24}")
    for A in A_VALUES:
        r = per_A[str(A)]
        print(f"{A:>2} {r['n']:>3} {r['height6_partitions']:>5}  "
              f"{r['B_6_partial_budget'][:24]:>24}  "
              f"{r['alpha_5_raw'][:24]:>24}  "
              f"{r['c5_average_self_normalised'][:24]:>24}")
    print(f"\ncross-atom max/min   budget {fmt(s_budget)[:12]}   "
          f"raw {fmt(s_raw)[:12]}   self-norm {fmt(s_avg)[:12]}")
    print("\nalpha_5 = B_6 * <c_5>, exactly. A spread in the raw column mixes "
          "the two;\nonly the self-normalised column is invariant under the "
          "weight-family choice.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
