#!/usr/bin/env python3
"""Does the canonical ribbon twist supply the charge quantum `Q = T/3`?

Motivation (derive-then-check, not enumerate-and-fit)
-----------------------------------------------------
`def:strand-twist-datum` makes the per-strand twist `t` a **free** integer
label, so `Q_twist = T(t)/3` can be given any value in `(1/3)Z`.  That is
why the published enumeration cannot corroborate the candidate: the whole
battery reduces to `sum(t) = 3Q`, which is the definition of `Q_twist`
(proved sorry-free in `QOU/StandardModel/TwistBatteryVacuity.lean`).

The proposed repair is to stop treating the twist as a free label and take
the **canonical twist of the ribbon category** instead.  On a simple object
of a ribbon category the twist `theta` acts by a scalar; for Hecke /
quantum-`sl_N` the exponent is the **content sum** of the partition,

    c(lambda) = sum over cells (i, j) of lambda of (j - i),

which the corpus already uses (`contentSum`).  That is a *derived*
per-block integer, not a chosen one.

The falsifiable question this probe asks
----------------------------------------
Does `Q = c(lambda) / 3` reproduce the Standard-Model first-generation
charge spectrum `{+2/3, -1/3, 0, -1}`?

Nothing is fitted: `c(lambda)` is fixed by the partition and the `1/3` is
the colour-tube quantum already fixed structurally in the corpus.  There is
no free parameter to tune, so the answer is a clean yes or no.

Exact rational arithmetic (`fractions.Fraction`); no floats.
"""

from __future__ import annotations

import json
from fractions import Fraction as F


def partitions(n: int) -> list[tuple[int, ...]]:
    """All partitions of `n`, as weakly decreasing tuples."""
    if n == 0:
        return [()]
    out: list[tuple[int, ...]] = []

    def rec(remaining: int, cap: int, acc: tuple[int, ...]) -> None:
        if remaining == 0:
            out.append(acc)
            return
        for part in range(min(remaining, cap), 0, -1):
            rec(remaining - part, part, acc + (part,))

    rec(n, n, ())
    return out


def content_sum(lam: tuple[int, ...]) -> int:
    """c(lambda) = sum of (j - i) over cells, 1-indexed rows i and columns j.

    This is the exponent of the ribbon twist eigenvalue on the Wedderburn
    block `lambda` (equivalently `n(lambda') - n(lambda)`).
    """
    return sum(j - i for i, row in enumerate(lam, start=1)
               for j in range(1, row + 1))


# Standard-Model first-generation electric charges.
SM_CHARGES = {F(2, 3), F(-1, 3), F(0), F(-1)}
QUARK_CHARGES = {F(2, 3), F(-1, 3)}


def main() -> dict:
    results: dict[str, object] = {}
    per_n = []

    for n in range(2, 9):
        rows = []
        for lam in partitions(n):
            c = content_sum(lam)
            q = F(c, 3)
            rows.append(dict(partition=list(lam), content_sum=c,
                             Q_twist=str(q),
                             is_SM_charge=q in SM_CHARGES,
                             is_quark_charge=q in QUARK_CHARGES))
        charges = {F(content_sum(l), 3) for l in partitions(n)}
        # A third-integer charge is one with denominator 3.
        thirds = sorted(str(x) for x in charges if x.denominator == 3)
        per_n.append(dict(
            n=n,
            num_blocks=len(rows),
            charges=sorted(str(x) for x in charges),
            third_integer_charges=thirds,
            has_thirds=bool(thirds),
            covers_SM=SM_CHARGES.issubset(charges),
            covers_quarks=QUARK_CHARGES.issubset(charges),
            blocks=rows))
    results["per_n"] = per_n

    # --- headline questions ---------------------------------------------
    n3 = next(r for r in per_n if r["n"] == 3)
    results["n3_is_lepton_like"] = dict(
        charges=n3["charges"],
        all_integers=not n3["has_thirds"],
        note="H_3(q) has three blocks with content sums {3, 0, -3}; divided "
             "by 3 these are the INTEGER charges {+1, 0, -1}. The canonical "
             "twist on the 3-strand tower produces no third-integer charge "
             "at all, so it cannot supply a quark charge there.")

    first_thirds = next((r["n"] for r in per_n if r["has_thirds"]), None)
    results["first_n_with_third_integer_charge"] = first_thirds

    covers_q = [r["n"] for r in per_n if r["covers_quarks"]]
    covers_all = [r["n"] for r in per_n if r["covers_SM"]]
    results["n_covering_both_quark_charges"] = covers_q
    results["n_covering_full_SM_spectrum"] = covers_all

    results["verdict"] = dict(
        question="Does Q = contentSum(lambda)/3 reproduce {+2/3, -1/3, 0, -1}?",
        answer_n3="NO - all charges are integers {+1, 0, -1} (lepton-like).",
        answer_any_n=("YES at some n" if covers_all else
                      "NO at any n tested (2..8)"),
        scope="(a) - a statement about this particular twist reading, "
              "parameter-free. Not a scope-(b) exclusion of the ribbon "
              "route in general: other ribbon-twist normalisations "
              "(kappa = <lambda, lambda+2rho>, or a colour-tube-weighted "
              "content) are untested here.")
    return results


if __name__ == "__main__":
    res = main()
    for r in res["per_n"]:
        flag = ""
        if r["covers_SM"]:
            flag = "  <== covers full SM spectrum"
        elif r["covers_quarks"]:
            flag = "  <== covers both quark charges"
        elif r["has_thirds"]:
            flag = "  <- has third-integer charges"
        print(f"n={r['n']}  blocks={r['num_blocks']:2d}  "
              f"Q=contentSum/3: {', '.join(r['charges'])}{flag}")
    print()
    print(json.dumps({k: v for k, v in res.items() if k != "per_n"}, indent=2))
