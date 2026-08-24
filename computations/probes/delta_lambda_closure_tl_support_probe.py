#!/usr/bin/env python3
"""Where can the missing 83.5% of the Delta_lambda closure possibly live?

`rho_w_crystal_vertex_trace` computes the parameter-free deuteron binding as

    B_pred = m_e * | sum_lambda  y_lambda * Delta_lambda * sgn(w_0) * f^lambda |

and captures 16.48 % of AME (0.3666 MeV vs 2.2247). Six ansatze have been
refuted trying to close that gap. This probe asks the prior question — not
"what closes it" but "where is the formula even ABLE to receive a contribution"
— and the answer is sharply constrained.

THE SUM IS SUPPORTED ON THE TEMPERLEY-LIEB QUOTIENT.  `y_lambda` vanishes on
every partition with >= 3 rows, so those blocks enter the sum multiplied by
EXACTLY zero. At n = 6 that is 7 of 11 partitions contributing nothing; only
(6), (5,1), (4,2), (3,3) survive.

That makes this a scope-(b) STRUCTURAL EXCLUSION in the AGENTS.md sense, with a
named exact invariant rather than a numerical observation: no per-block weight
placed on a >= 3-row partition can change this sum's value, because it is
multiplied by zero before anything else happens. It bounds where a seventh
ansatz could act without proposing one.

Scope, stated precisely: this excludes contributions THROUGH THIS FORMULA. A
different formula — one not of the form `sum_lambda y_lambda (...)` — is
untouched by it, and per AGENTS.md the missing piece is expected to be a
separate additive super-pairwise object rather than a per-block reweighting.
This probe is evidence for exactly that expectation, not against it.

AND THE SURVIVING SUM IS CANCELLATION-DOMINATED. The four contributing terms
have absolute values summing to 2.4646 against a total of 0.7174 — a 3.44x
cancellation, with the single largest term (5,1) at 177 % of the total. So the
16.48 % capture is not "we collected a sixth of the terms"; it is large
alternating terms nearly cancelling and leaving a residue about 6x too small.
Any reweighting of the four survivors is fighting that cancellation.

THIS IS THE SAME PHENOMENON AS THE GRAM RADICAL, seen from the weights instead
of from the pairing. `QOU.Interactions.GramMatrixH3Symbolic.gramMatrixD_det_eq_zero`
proves the convention-D H_3 Gram is singular with the q-antisymmetriser — the
(1^3) block, the unique >= 3-row partition of 3 — spanning its radical. The
identity `sum_{lambda >= 3 rows} (dim V_lambda)^2 = n! - Catalan(n)`, verified
here for n = 3..6, is the general-n statement of it, matching the TL_n quotient
result of PR #5592.

Exact throughout: rational/integer combinatorics for the dimension identity, and
mpmath at the witness's own recorded precision for the sums. No float64.
"""

from __future__ import annotations

import json
import pathlib
import sys
from math import comb, factorial

from mpmath import mp, mpf, nstr

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parent.parent
COMP = REPO / "computations"
for _p in (str(COMP), str(COMP / "substrate")):
    if _p not in sys.path:
        sys.path.insert(0, _p)

from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

SOURCE = "computations/rho-w-crystal-vertex-trace.witness.json"


def partitions_of(n: int) -> list[tuple[int, ...]]:
    out: list[tuple[int, ...]] = []

    def go(rem: int, mx: int, cur: list[int]) -> None:
        if rem == 0:
            out.append(tuple(cur))
            return
        for k in range(min(rem, mx), 0, -1):
            go(rem - k, k, cur + [k])

    go(n, n, [])
    return out


def syt_count(lam: tuple[int, ...]) -> int:
    """Hook-length formula — exact integer, no floats."""
    n = sum(lam)
    conj = [sum(1 for r in lam if r > j) for j in range(lam[0])]
    prod = 1
    for i, row in enumerate(lam):
        for j in range(row):
            prod *= (row - j) + (conj[j] - i) - 1
    return factorial(n) // prod


def main() -> int:
    set_compute_dps()
    w = json.loads((REPO / SOURCE).read_text(encoding="utf-8"))
    mp.dps = max(mp.dps, int(w.get("dps") or 50))

    terms = [
        (tuple(e["partition"]), mpf(str(e["y_lambda"])), mpf(str(e["signed_contribution"])))
        for e in w["by_partition"]
    ]
    total = sum(t for _lam, _y, t in terms)
    abs_sum = sum(abs(t) for _lam, _y, t in terms)
    ge3 = [(lam, y, t) for lam, y, t in terms if len(lam) >= 3]
    le2 = [(lam, y, t) for lam, y, t in terms if len(lam) <= 2]

    # the dimension identity, exact integer arithmetic, several n
    dim_rows = []
    for n in (3, 4, 5, 6):
        P = partitions_of(n)
        hi = [l for l in P if len(l) >= 3]
        lhs = sum(syt_count(l) ** 2 for l in hi)
        rhs = factorial(n) - comb(2 * n, n) // (n + 1)
        dim_rows.append({
            "n": n, "partitions": len(P), "contributing_le2rows": len(P) - len(hi),
            "sum_dim_sq_ge3rows": lhs, "n_factorial_minus_catalan": rhs, "equal": lhs == rhs,
        })

    checks = [
        ("y_lambda_vanishes_on_every_ge3row_block",
         all(y == 0 for _l, y, _t in ge3), True,
         f"{len(ge3)} of {len(terms)} partitions, each contributing exactly 0"),
        ("ge3row_blocks_contribute_exactly_zero",
         sum(t for _l, _y, t in ge3) == 0, True,
         "not small — identically zero, so no per-block weight there can act"),
        ("support_is_the_le2row_set",
         sum(t for _l, _y, t in le2) == total, True,
         "the whole sum is carried by the Temperley-Lieb quotient"),
        ("dimension_identity_holds_n3_to_n6",
         all(r["equal"] for r in dim_rows), True,
         "sum_(>=3 rows) dim^2 = n! - Catalan(n) — the general-n form"),
        ("surviving_sum_is_cancellation_dominated",
         abs_sum / abs(total) > 3, True,
         f"cancellation ratio {nstr(abs_sum / abs(total), 6)}x"),
    ]

    payload = {
        "description": (
            "Support analysis of the parameter-free Delta_lambda closure. y_lambda "
            "vanishes on every >= 3-row partition, so the sum is supported entirely "
            "on the Temperley-Lieb quotient and no per-block weight on a >= 3-row "
            "block can contribute to it. The surviving 4-term sum is "
            "cancellation-dominated (3.44x)."
        ),
        "source_witness": SOURCE,
        "n_strands": w.get("n_strands"),
        "captured_fraction": w.get("captured_fraction"),
        "closure_status": w.get("closure_status"),
        "signed_total": str(total),
        "sum_of_absolute_terms": str(abs_sum),
        "cancellation_ratio": str(abs_sum / abs(total)),
        "largest_term_pct_of_total": str(
            max(abs(t) for _l, _y, t in terms) / abs(total) * 100),
        "by_partition": [
            {"partition": list(lam), "rows": len(lam), "y_lambda": str(y),
             "signed_contribution": str(t), "contributes": y != 0}
            for lam, y, t in terms
        ],
        "dimension_identity": dim_rows,
        "assertions": [
            {"name": n, "value": bool(g), "expected": bool(e),
             "passed": bool(g) is e, "note": note}
            for n, g, e, note in checks
        ],
        "allPassed": all(bool(g) is e for _n, g, e, _note in checks),
        "q0Anchor": w.get("q0Anchor"),
        "q0Value": w.get("q_0_50dps"),
        "context": {
            "bean": "qou-zf9n",
            "scope": (
                "(b) structural exclusion, with the exact invariant named: y_lambda = 0 "
                "on >= 3-row blocks. It excludes contributions THROUGH THIS FORMULA "
                "(sum_lambda y_lambda ...), not from the framework — a separate additive "
                "super-pairwise term is untouched by it, and this is evidence FOR that "
                "expectation rather than against it."
            ),
            "same_phenomenon_as": [
                "QOU.Interactions.GramMatrixH3Symbolic.gramMatrixD_det_eq_zero "
                "(radical = q-antisymmetriser = the (1^3) block)",
                "the TL_n quotient rank result of PR #5592",
                "bean qou-8iru (y_lambda = 0 for >= 3 rows)",
            ],
            "not_a_proposal": (
                "This does NOT propose a seventh ansatz. It bounds where one could "
                "act, which is the opposite move."
            ),
        },
    }

    out = WitnessBuilder.wrap_legacy(
        "delta-lambda-closure-tl-support", payload,
        script_path=__file__, engine="python+mpmath(exact combinatorics)",
    ).save()

    print("=== Where can the missing 83.5% live? ===")
    print(f"  captured {float(w.get('captured_fraction', 0)) * 100:.2f}%  "
          f"closure_status = {w.get('closure_status')}")
    print()
    print(f"  {'lambda':<18} {'rows':>4} {'y_lambda':>16}  contributes")
    for lam, y, _t in terms:
        print(f"  {str(lam):<18} {len(lam):>4} {nstr(y, 10):>16}  {'yes' if y != 0 else 'NO — exactly 0'}")
    print()
    print(f"  >= 3-row blocks contribute : {sum(t for _l, _y, t in ge3)} (exact)")
    print(f"  cancellation ratio         : {nstr(abs_sum / abs(total), 6)}x  "
          f"(sum|term| {nstr(abs_sum, 8)} vs |total| {nstr(abs(total), 8)})")
    print()
    for n, g, e, note in checks:
        print(f"  [{'PASS' if bool(g) is e else 'FAIL'}] {n:<44} ({note})")
    print()
    print(f"  witness -> {out}")
    return 0 if payload["allPassed"] else 1


if __name__ == "__main__":
    sys.exit(main())
