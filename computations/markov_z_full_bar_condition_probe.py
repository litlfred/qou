#!/usr/bin/env python3
"""The ``z`` dilemma of #4767 / #4802 rests on the wrong bar condition.

#4767 declined the ``z`` edit partly because convention **C**
(``z = 1/(q^{1/2}+q^{-1/2})``) is bar-invariant where convention **D**
(``z = q^3/(q^2+1)``) is not, and #4802 sharpened that into a dilemma: no
fibre rank ``N`` yields a bar-invariant ``z``, so bar-invariance and the fibre
reading cannot both be had.

Both computed bar-invariance as ``z(q^{-1}) = z(q)`` -- the **coefficient
half** of ``def:bar-involution``, holding the algebra fixed.  But ``z`` is
defined by Markov axiom M3,

    tau(x * sigma_n) = z * tau(x),

and the bar involution inverts ``sigma_n`` as well as ``q``.  Applying it to
M3 therefore does *not* compare ``z`` with ``bar(z)``; it compares ``z`` with
the **negative-stabilisation** parameter.  Since ``sigma^2 = h*sigma + 1``
gives ``sigma^{-1} = sigma - h`` exactly,

    tau(x * sigma_n^{-1}) = (z - h) * tau(x),

so the bar-partner of ``z`` is ``z - h``, and the correct covariance
condition on the Markov parameter is

    bar(z) = z - h,        h = q - q^{-1}.

**Result: convention D satisfies it; convention C does not** -- the exact
reverse of the coefficient-half verdict.  And the dilemma does not merely
tip, it *dissolves*: ``bar(z) = z - h`` is an **identity of the whole fibre
family**, verified for symbolic ``N`` (equivalently ``z_N = h/(1-q^(-2N))``).
Bar-covariance and the fibre reading are not competing desiderata to trade
off against each other; they are the **same condition**.

Convention C fails it because C is not a member of the family at any fixed
rank: solving ``z_C = h/(1-q^(-2N))`` for ``N`` returns a *q-dependent*
expression, so C's implied rank varies with ``q``.  The ``N = 2.5995`` of
#4766 / #4802 is a pointwise inversion at ``q_0``, not a rank.

This is the same error class as the ``eigenbasis-structural-lemmas`` item-2
defect (PR #4826): a bar claim about an object living inside the algebra,
computed with the coefficient half only.

Scope (a) on the conclusion: this shows the *stated grounds* for preferring C
do not survive using the full involution.  It does not by itself settle which
convention the corpus should adopt -- the >= 8 corpus sites hard-coding C, and
the owner reservation noted in #4767, are unchanged and are not weighed here.

Conventions
-----------
Symbolic in ``q``; no substrate pin is used or needed.
"""

from __future__ import annotations

import sys
from pathlib import Path

import sympy as sp

_REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(_REPO / "tools" / "qou-substrate" / "python"))

from qou_substrate import WitnessBuilder  # noqa: E402

q = sp.Symbol("q", positive=True)
h = q - 1 / q


def bar(expr):
    """Coefficient half of the bar involution: q -> q^{-1}."""
    return sp.simplify(expr.subs(q, 1 / q))


def main() -> int:
    wb = WitnessBuilder("markov-z-full-bar-condition", engine="python")
    wb.set_description(
        "M3 contains sigma_n, which the bar involution inverts, so the "
        "bar-partner of the Markov parameter z is z - h, not z. Under the "
        "correct condition bar(z) = z - h, convention D holds and C fails -- "
        "reversing the coefficient-half verdict of #4767/#4802."
    )

    checks: dict[str, bool] = {}

    # sigma^{-1} = sigma - h is exact from the Hecke relation.  Verify on the
    # 2-dim H_3 block rather than assuming it.
    s1 = sp.Matrix([[q, 1], [0, -1 / q]])
    ident = sp.eye(2)
    checks["hecke_relation_holds"] = (
        sp.simplify(s1 * s1 - h * s1 - ident) == sp.zeros(2, 2)
    )
    checks["sigma_inv_eq_sigma_minus_h"] = (
        sp.simplify(s1.inv() - (s1 - h * ident)) == sp.zeros(2, 2)
    )

    # Convention C is EXCISED (owner ruling 2026-08-09, re-affirmed 2026-08-15);
    # D is canonical. Both stay because this probe tests the bar condition
    # AGAINST each -- and its result is one of the reasons the ruling reads the
    # way it does: bar(z) = z - h holds exactly for z_D and fails for any
    # bar-even z, hence for z_C, away from q^2 = 1.
    z_C = 1 / (sp.sqrt(q) + 1 / sp.sqrt(q))   # EXCISED — kept as the comparison arm
    z_D = q**3 / (q**2 + 1)                    # CANONICAL

    # The two candidate conditions.
    def coef_half_invariant(z):
        return sp.simplify(bar(z) - z) == 0

    def full_bar_covariant(z):
        return sp.simplify(bar(z) - (z - h)) == 0

    checks["C_is_coefficient_half_invariant"] = coef_half_invariant(z_C)
    checks["D_is_not_coefficient_half_invariant"] = not coef_half_invariant(z_D)
    checks["D_satisfies_full_bar_condition"] = full_bar_covariant(z_D)
    checks["C_fails_full_bar_condition"] = not full_bar_covariant(z_C)
    # The verdict genuinely reverses between the two conditions.
    checks["verdict_reverses_between_conditions"] = (
        coef_half_invariant(z_C)
        and not coef_half_invariant(z_D)
        and full_bar_covariant(z_D)
        and not full_bar_covariant(z_C)
    )

    # D's value under the correct condition, for the record.
    z_D_bar = sp.simplify(bar(z_D))
    z_D_minus_h = sp.simplify(z_D - h)
    checks["D_both_sides_equal_one_over_q3_plus_q"] = (
        sp.simplify(z_D_bar - 1 / (q**3 + q)) == 0
        and sp.simplify(z_D_minus_h - 1 / (q**3 + q)) == 0
    )

    # Does ANY rank-N member of #4802's family satisfy the full condition?
    # z_N = q^(2N-1)(q^2-1)/(q^(2N)-1); N = 2 is D.
    N = sp.Symbol("N", positive=True)
    z_N = q ** (2 * N - 1) * (q**2 - 1) / (q ** (2 * N) - 1)
    per_rank = []
    n_full_ok = 0
    for n_int in range(1, 9):
        zn = sp.simplify(z_N.subs(N, n_int))
        ok_full = sp.simplify(bar(zn) - (zn - h)) == 0
        ok_coef = sp.simplify(bar(zn) - zn) == 0
        if ok_full:
            n_full_ok += 1
        per_rank.append(
            {
                "N": n_int,
                "z_N": str(zn),
                "satisfies_full_bar_condition": bool(ok_full),
                "coefficient_half_invariant": bool(ok_coef),
            }
        )
    checks["every_integer_rank_satisfies_full_condition"] = n_full_ok == 8
    # ...and in fact it is an identity of the family for SYMBOLIC N: the
    # full-bar condition IS the fibre reading, not a competitor to it.
    z_N_sym = z_N
    checks["full_bar_condition_holds_for_symbolic_N"] = (
        sp.simplify(bar(z_N_sym) - (z_N_sym - h)) == 0
    )
    checks["family_equals_h_over_one_minus_q_pow_minus_2N"] = (
        sp.simplify(z_N_sym - h / (1 - q ** (-2 * N))) == 0
    )
    # C is not a member of the family at ANY fixed rank: solving for N returns
    # a q-dependent expression, so its "rank" varies with q.  The 2.5995 of
    # #4766/#4802 is a pointwise inversion at q_0, not a rank.
    sols = sp.solve(sp.Eq(z_C, h / (1 - q ** (-2 * N))), N)
    checks["C_implied_rank_is_q_dependent"] = bool(sols) and all(
        q in s.free_symbols for s in sols
    )
    # #4802's negative result stands under the coefficient half.
    checks["no_rank_is_coefficient_half_invariant"] = not any(
        r["coefficient_half_invariant"] for r in per_rank
    )

    all_pass = all(checks.values())

    wb.add_parameter("exact", "sympy, symbolic in q")
    wb.add_parameter("q_0_pin", "not applicable (symbolic)")
    wb.add_parameter("uses_muon_built_cache", False)
    wb.add_data("checks", {k: bool(v) for k, v in checks.items()})
    wb.add_data("correct_condition", "bar(z) = z - h,  h = q - 1/q")
    wb.add_data(
        "conventions",
        {
            "C": {
                "z": "1/(q^(1/2)+q^(-1/2))",
                "coefficient_half_invariant": True,
                "satisfies_full_bar_condition": False,
            },
            "D": {
                "z": "q^3/(q^2+1)",
                "coefficient_half_invariant": False,
                "satisfies_full_bar_condition": True,
                "both_sides": "1/(q^3+q)",
            },
        },
    )
    wb.add_data("per_rank", per_rank)

    wb.add_assertion(
        "checks_failed", sum(1 for v in checks.values() if not v), 0,
        source="sympy exact",
    )
    wb.add_assertion(
        "n_integer_ranks_satisfying_full_bar_condition", n_full_ok, 8,
        source="sympy exact; ALL of them -- it is an identity of the family",
    )

    wb.add_data(
        "interpretation",
        {
            "the_dilemma_dissolves": (
                "#4802 concluded bar-invariance and a fibre reading are "
                "incompatible at every rank. That holds for the "
                "coefficient-half condition bar(z) = z, and that negative is "
                "reproduced here. But M3 contains sigma_n, which bar inverts, "
                "so the condition the axiom actually supports is "
                "bar(z) = z - h -- and THAT condition is an identity of the "
                "whole fibre family, verified for symbolic N (equivalently "
                "z_N = h/(1 - q^(-2N))). Bar-covariance and the fibre reading "
                "are not competing desiderata; they are the SAME condition. "
                "There was never a trade-off to make."
            ),
            "why_C_fails": (
                "Convention C is not a member of the family at any fixed "
                "rank: solving z_C = h/(1-q^(-2N)) for N returns a "
                "q-dependent expression, so C's implied rank varies with q. "
                "The N = 2.5995 of #4766/#4802 is a pointwise inversion at "
                "q_0, not a rank. That is why C satisfies the coefficient-"
                "half condition and fails the full one."
            ),
            "same_error_class_as_item_2": (
                "Like eigenbasis-structural-lemmas item 2 (PR #4826), a bar "
                "claim about an object living inside the algebra was computed "
                "with the coefficient half alone, dropping the "
                "sigma -> sigma^{-1} half."
            ),
            "what_this_does_not_settle": (
                "Scope (a): it removes the stated grounds for preferring C. "
                "The >= 8 corpus sites hard-coding C and the owner "
                "reservation recorded in #4767 are untouched and not weighed "
                "here."
            ),
        },
    )

    wb.add_caveat(
        "Rests on tau(x sigma_n^{-1}) = (z - h) tau(x), which follows from M3 "
        "plus sigma^{-1} = sigma - h (verified) and LINEARITY of tau. It "
        "further assumes the Markov trace is bar-compatible, tau(bar y) = "
        "bar(tau y); that compatibility is the standard Ocneanu-trace "
        "property but is asserted here, not proved."
    )
    wb.add_caveat(
        "Scope (a). Removes the bar-invariance argument for convention C; "
        "does not by itself decide the convention, and does not touch the >= 8 "
        "corpus sites that hard-code C."
    )

    path = wb.save()

    print("=" * 70)
    print("Markov z under the FULL bar involution")
    print("=" * 70)
    print("  M3: tau(x sigma_n) = z tau(x);  sigma^-1 = sigma - h")
    print("  => tau(x sigma_n^-1) = (z - h) tau(x)")
    print("  => correct condition:  bar(z) = z - h    (NOT bar(z) = z)")
    print()
    print(f"  {'':4s} {'coef-half inv':>14s} {'FULL bar cond':>14s}")
    print(f"  {'C':4s} {'YES':>14s} {'no':>14s}")
    print(f"  {'D':4s} {'no':>14s} {'YES':>14s}   both sides = 1/(q^3+q)")
    print()
    print("  integer ranks satisfying the full condition:",
          [r["N"] for r in per_rank if r["satisfies_full_bar_condition"]])
    print("  integer ranks coefficient-half invariant:   ",
          [r["N"] for r in per_rank if r["coefficient_half_invariant"]])
    print()
    for k, v in checks.items():
        print(f"  [{'PASS' if v else 'FAIL'}] {k}")
    print()
    print(f"  ALL CHECKS {'PASS' if all_pass else 'FAIL'}")
    print(f"  witness -> {path}")
    return 0 if all_pass else 1


if __name__ == "__main__":
    raise SystemExit(main())
