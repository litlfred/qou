#!/usr/bin/env python3
# polynomial_q_not_applicable: structural test against pre-computed
# spectra; no symbolic-q output.
"""Test whether the LP cost vector $t_\\lambda = y_\\lambda \\cdot \\chi^\\lambda_q(\\beta)$
identifies the empirical dominant partition per atom.

The operator-selection LP / SDP per
[prop:operator-selection-lp](#prop:operator-selection-lp) consumes
the per-block cost $t_\\lambda(q_0, \\beta) := y_\\lambda(q_0) \\cdot \\chi^\\lambda_q(\\beta)$.
A natural FIRST candidate selector — simpler than the full SDP
shadow price $y_\\lambda^\\star$ — is:

  $\\mathrm{isMaxEigSpectrum}(\\lambda) \\stackrel{?}{=}
   \\lambda = \\mathop{\\mathrm{argmax}}_{\\lambda'} \\lvert t_{\\lambda'} \\rvert.$

This script tests the hypothesis against PR #639's empirical
dominants (the partitions whose per-partition $\\Phi_q^{[\\leq k=2]}$
contributions dominate the brane-tower failure at uniform $k$):

  D     empirical dominant: $\\lambda = [2, 2, 1, 1]$
  T     empirical dominant: $\\lambda = [6, 3]$
  ³He   empirical dominant: $\\lambda = [5, 4]$

**Result (negative)**: the LP cost argmax matches only $T$. For $D$
the empirical dominant is not even in the top-5 by $\\lvert t_\\lambda\\rvert$;
for ³He it ranks 4th. The simpler hypothesis is **refuted**.

This refutation **rules in** the SDP dual variable $y_\\lambda^\\star$
(per `prop:operator-selection-sdp`) as the next candidate — the
SDP shadow price is structurally different from the LP cost (the
cost is the *coefficient* in the objective; the shadow price is
the marginal *price* in the dual that emerges from the
primal-dual coupling).

Class C (diagnostic / probe).

Output: `probe-lp-cost-dominant-partition.witness.json`.
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp

mp.mp.dps = 50

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from witness_base import WitnessBuilder  # noqa: E402


# ── #638 per-eigenvalue probe data (extracted; do not bundle 400KB raw) ─
# Source: probe-phiq-operator-valued.witness.json on
#   claude/close-level-selection-rule-bvMvw

# Top-5 partitions per atom by |y_λ · χ_q^λ| (the LP cost), extracted
# 2026-05-11 from #638's witness.
PER_ATOM_LP_COST_TOP5 = {
    "D": [  # n = 6, empirical dominant [2,2,1,1]
        ([5, 1],       0.189611),
        ([6],          0.092319),
        ([4, 2],       0.067426),
        ([3, 3],       0.060001),
        ([3, 2, 1],    0.014438),
    ],
    "T": [  # n = 9, empirical dominant [6,3]
        ([6, 3],       0.045312),  # ← MATCH
        ([8, 1],       0.027328),
        ([7, 2],       0.019998),
        ([9],          0.010336),
        ([5, 4],       0.010156),
    ],
    "He3": [  # n = 9, empirical dominant [5,4]
        ([6, 3],       0.071594),
        ([8, 1],       0.047986),
        ([7, 2],       0.047441),
        ([5, 4],       0.017666),  # ← rank 4, NOT argmax
        ([9],          0.015689),
    ],
}

EMPIRICAL_DOMINANT = {
    "D":   [2, 2, 1, 1],
    "T":   [6, 3],
    "He3": [5, 4],
}


def main() -> int:
    w = WitnessBuilder("probe-lp-cost-dominant-partition",
                       engine="python")

    print("=" * 78)
    print("LP COST |y_λ · χ_q^λ| argmax test (simpler than SDP shadow)")
    print("=" * 78)
    print()

    findings = []
    for atom in ("D", "T", "He3"):
        emp = EMPIRICAL_DOMINANT[atom]
        top5 = PER_ATOM_LP_COST_TOP5[atom]
        argmax_lambda = top5[0][0]
        argmax_value = top5[0][1]
        rank_of_emp = None
        for i, (lam, val) in enumerate(top5):
            if lam == emp:
                rank_of_emp = i + 1
                emp_value = val
                break
        is_match = (argmax_lambda == emp)
        print(f"  {atom:>5}  empirical: λ={str(emp):<14}  argmax: λ={str(argmax_lambda):<14}"
              f"  {'✓' if is_match else '✗'}")
        if not is_match:
            if rank_of_emp:
                print(f"          empirical rank in top-5 by |y·χ| = {rank_of_emp}"
                      f"  (|y·χ|={emp_value:.4f} vs argmax {argmax_value:.4f})")
            else:
                print(f"          empirical NOT in top-5 by |y·χ|")
        findings.append({
            "atom": atom,
            "empirical_dominant": emp,
            "lp_cost_argmax": argmax_lambda,
            "lp_cost_argmax_value": argmax_value,
            "empirical_rank_in_top5": rank_of_emp,
            "match": is_match,
        })

    n_matches = sum(1 for f in findings if f["match"])
    print()
    print(f"  LP-cost argmax matches empirical dominant: {n_matches}/3")
    print()
    if n_matches < 3:
        print("  ✗ NEGATIVE FINDING: simpler hypothesis refuted.")
        print()
        print("  Implication: the SDP shadow price y_λ^* (per")
        print("  prop:operator-selection-sdp) is the next candidate to test —")
        print("  structurally different from the LP cost (the cost is the")
        print("  objective coefficient; the shadow price is the marginal")
        print("  price emerging from primal-dual coupling). Running the")
        print("  operator-selection SDP at each atom's braid word with the")
        print("  per-block Gram + Markov-trace data is the next probe in")
        print("  the queue.")

    w.set_content_block("rem:per-partition-k-lambda-rule")
    w.set_description(
        "Tests the LP cost argmax hypothesis: dominant partition = "
        "argmax_λ |y_λ(q_0) · χ_q^λ(β_atom)|. The LP cost is the "
        "objective coefficient in the operator-selection LP "
        "(prop:operator-selection-lp). NEGATIVE FINDING: matches "
        "only T (1/3 atoms). For D the empirical dominant [2,2,1,1] "
        "isn't even in the top-5; for ³He [5,4] ranks 4th. This "
        "rules out the simpler LP-cost hypothesis and rules IN the "
        "full SDP shadow price y_λ^* (which is structurally different "
        "from the cost) as the next selector candidate. Substrate-"
        "only data from PR #638's per-eigenvalue probe. Class C."
    )
    w.add_parameter("source", "PR #638 probe-phiq-operator-valued.witness.json")
    w.add_data("per_atom_findings", findings)
    w.add_data("matches", n_matches)
    w.add_data("conclusion", (
        "LP-cost-argmax hypothesis REFUTED. Rules in the full SDP "
        "shadow price y_λ^* (operator-selection-sdp's dual variable) "
        "as the next selector candidate; the cost is the LP objective "
        "coefficient, while the shadow price is the dual marginal "
        "price that emerges from primal-dual coupling — distinct "
        "objects with different empirical content."
    ))
    w.add_assertion(
        "lp_cost_argmax_does_not_match_for_D",
        computed=(not findings[0]["match"]),
        expected=True,
    )
    w.add_assertion(
        "lp_cost_argmax_matches_for_T",
        computed=findings[1]["match"],
        expected=True,
    )
    w.add_assertion(
        "lp_cost_argmax_does_not_match_for_He3",
        computed=(not findings[2]["match"]),
        expected=True,
    )
    out = w.save()
    print(f"\n  Wrote {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
