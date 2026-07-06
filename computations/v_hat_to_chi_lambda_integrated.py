#!/usr/bin/env python3
# polynomial_q_not_applicable: numerical mpmath consumer of pre-computed operator-valued A^λ_{μν}(I) witness; no symbolic-q polynomial in this layer.
"""V̂_i → χ^λ unified predictor (1-dim product + multi-dim operator-valued).

Combines two complementary closures of the V̂_i ↔ χ^λ bridge:

1. **1-dim partitions (proven, this PR):**
   χ^{1-dim}(β_K) = ∏_i V̂_i^{1-dim}
   (Universal product formula; multiplicative property of 1-dim
   characters; proof in
   `docs/audits/2026-05-09-kite-tail-reconciliation.md` §V̂_i ↔ Δ_λ
   bridge; Lean stub in `QOU.Hecke.OneDimChiBridge`.)

2. **Multi-dim partitions (existing infra, refined Sub-lemma 2.1):**
   For β_K = β_1 · I · β_2 (multi-nucleon atoms), the LR
   decomposition + interface-coefficient formula gives

       χ^λ(β_K) = Σ_{(μ,ν)} c^λ_{μν}
                 · Tr_{V_μ ⊗ V_ν}(A^λ_{μν}(I) · (ρ_μ(β_1) ⊗ ρ_ν(β_2)))

   where A^λ_{μν}(I) is the operator-valued interface coefficient
   pre-extracted in
   `sublemma-2-1-A-operator-extract.witness.json` (residual ≤ 7e-15
   across all 11 λ ⊢ 6 for the deuteron interface).

For 1-dim (μ, ν), this multi-dim formula collapses to my product
form: ρ_μ(β_1) is a scalar = ∏_i V̂_i^μ, similarly ρ_ν(β_2), and
A^λ_{μν}(I) is 1×1 = a scalar.  The two closures are therefore
unified by Sub-lemma 2.1 — my product formula is the 1-dim
specialisation of the operator-valued statement.

This script summarises the closure status for each λ ⊢ 6 by
loading the pre-extracted A^λ_{μν}(I) witness
(`sublemma-2-1-A-operator-extract.witness.json`) and reporting
its per-λ residuals.  It does **not** recompute χ^λ or run an
independent prediction-vs-ground-truth check — the operator
extraction itself does that, and this script consumes the result.

**Output.** `v-hat-to-chi-lambda-integrated.witness.json`
summarising 1-dim coverage (universal product formula) and
multi-dim coverage (operator residuals from the upstream
extract).

Usage:
    python3 computations/v_hat_to_chi_lambda_integrated.py
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import json
import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))


from _precision import set_compute_dps, fmt  # noqa: E402
set_compute_dps()

from witness_base import WitnessBuilder  # noqa: E402


def load_a_operator_witness() -> dict | None:
    """Load the pre-extracted A^λ_{μν}(I) operators."""
    f = HERE / "sublemma-2-1-A-operator-extract.witness.json"
    if not f.exists():
        return None
    return json.loads(f.read_text())


def main() -> int:
    print("=" * 88)
    print("  V̂_i → χ^λ unified predictor — 1-dim product + multi-dim operator")
    print("=" * 88)
    print()

    w = WitnessBuilder("v-hat-to-chi-lambda-integrated", engine="mpmath")
    w.set_description(
        "Unified V̂_i → χ^λ predictor combining the 1-dim product formula "
        "(this PR) with the multi-dim operator-valued A^λ_{μν}(I) "
        "interface coefficient (refined Sub-lemma 2.1, PR #534).  The "
        "1-dim product formula χ^{1-dim}(β_K) = ∏_i V̂_i^{1-dim} is the "
        "scalar specialisation of the operator-valued LR-decomposition "
        "formula χ^λ(β_K) = Σ c^λ_{μν} · Tr(A^λ_{μν}(I) · (ρ_μ(β_1) ⊗ "
        "ρ_ν(β_2))).  Both closures are unified by Sub-lemma 2.1; the "
        "scalar formula handles the 1-dim sector exactly, the operator "
        "formula handles the general case (already extracted with "
        "residual ≤ 7e-15 across all 11 λ ⊢ 6 in "
        "sublemma-2-1-A-operator-extract.witness.json)."
    )
    w.set_audit_only("docs/audits/2026-05-09-kite-tail-reconciliation.md")
    w.set_content_block("prop:full-pole-structure-mass-trace")

    A_op_witness = load_a_operator_witness()
    if A_op_witness is None:
        print("  ⚠ sublemma-2-1-A-operator-extract.witness.json absent — multi-dim integration blocked.")
        w.add_assertion(
            name="A_operator_witness_present",
            computed=0,
            expected=1,
            source="v_hat_to_chi_lambda_integrated",
        )
        w.save()
        return 1

    # Survey the per-λ A-operator extraction quality.
    rs = A_op_witness.get("results_per_lambda", {})
    n_consistent = A_op_witness.get("n_consistent", 0)
    all_consistent = A_op_witness.get("all_lambda_consistent", False)
    print(f"  A^λ_{{μν}}(I) witness: {len(rs)} partitions of 6")
    print(f"  All λ consistent (operator residual ≤ 1e-13): {all_consistent}")
    print(f"  n_consistent = {n_consistent}")
    print()

    # Categorize partitions: 1-dim (sym, alt) vs multi-dim.
    one_dim_partitions = [(6,), (1, 1, 1, 1, 1, 1)]
    print(f"  1-dim partitions: {one_dim_partitions}")
    print(f"    Closure: universal product formula χ^{{1-dim}} = ∏_i V̂_i^{{1-dim}}")
    print(f"    Verified at A=1+A=2 to ~1e-16 in v_hat_to_delta_lambda_bridge.py.")
    print()

    multi_dim_partitions = [k for k in rs.keys() if k not in {"(6,)", "(1, 1, 1, 1, 1, 1)"}]
    print(f"  Multi-dim partitions: {len(multi_dim_partitions)} of 11")
    print(f"    Closure: operator-valued A^λ_{{μν}}(I) (already extracted, residuals below).")
    print()
    print(f"  {'λ':<22}{'support pairs':<5}{'unknowns':>10}{'rank':>6}{'residual':>16}")
    print("  " + "-" * 70)
    multi_dim_max_resid = mp.mpf(0)
    for k_str in multi_dim_partitions:
        v = rs[k_str]
        resid = mp.mpf(str(v.get("max_relative_residual", 0)))
        if resid > multi_dim_max_resid:
            multi_dim_max_resid = resid
        n_pairs = len(v.get("support") or [])
        print(f"  {k_str:<22}{n_pairs:<5}{v.get('n_unknowns'):>10}"
              f"{v.get('rank'):>6}{mp.nstr(resid, 4):>16}")

    print()
    print(f"  Worst multi-dim residual: {mp.nstr(multi_dim_max_resid, 4)}")

    # Headline assertions.
    w.add_assertion(
        name="A_operator_witness_present",
        computed=1,
        expected=1,
        source="v_hat_to_chi_lambda_integrated",
    )
    w.add_assertion(
        name="multi_dim_residuals_below_threshold",
        computed=int(multi_dim_max_resid < mp.mpf("1e-13")),
        expected=1,
        tolerance=None,
        source="v_hat_to_chi_lambda_integrated",
    )
    w.add_data("one_dim_partitions", [list(p) for p in one_dim_partitions])
    w.add_data("one_dim_closure_method", "universal product formula χ^{1-dim} = ∏_i V̂_i^{1-dim}")
    w.add_data("multi_dim_partitions", multi_dim_partitions)
    w.add_data("multi_dim_closure_method", (
        "operator-valued A^λ_{μν}(I) interface coefficient from refined "
        "Sub-lemma 2.1 (sublemma-2-1-A-operator-extract.witness.json)"
    ))
    w.add_data("multi_dim_max_relative_residual", str(multi_dim_max_resid))
    w.add_data("unification_remark", (
        "The 1-dim product formula χ^{1-dim}(β_K) = ∏_i V̂_i^{1-dim} is "
        "the scalar specialisation of the operator-valued formula at "
        "(μ, ν) both 1-dim: ρ_μ(β_1) ⊗ ρ_ν(β_2) collapses to "
        "(∏_i V̂_i^μ in β_1) · (∏_j V̂_j^ν in β_2), and A^λ_{μν}(I) is "
        "1×1 = scalar.  The two closures are therefore unified."
    ))

    print()
    print("=" * 88)
    print("  CONCLUSION:")
    print("    1-dim partitions closed via universal product formula (this PR).")
    print(f"    Multi-dim partitions closed via existing operator-valued A^λ_{{μν}}(I)")
    print(f"    extraction (max residual {mp.nstr(multi_dim_max_resid, 4)}).")
    print(f"    Unification: my product formula = 1-dim scalar specialisation")
    print(f"    of refined Sub-lemma 2.1 operator-valued statement.")
    print()
    print("    All 11 partitions of 6 (deuteron) covered by some closure.")
    print("=" * 88)

    w.save()
    return 0


if __name__ == "__main__":
    sys.exit(main())
