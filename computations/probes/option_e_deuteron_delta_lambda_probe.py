#!/usr/bin/env python3
"""
Option E deuteron Δ_λ probe — experimental verification harness.

Companion to the Lean infrastructure in
content/quantum-observable-universe/lean/QOU/OptionE/.

For the deuteron (Z=1, N=1, A=2, n=6), tries five candidate Δ_λ rules
derived from crystal-graph data + tests Path-D mass-prediction closure.

Each candidate rule is "substrate-derived" in the sense that its
Δ_λ values come from properties of the partition λ (not directly
from AME measurements). The probe reports which (if any) closes
deuteron AME within 10%.

Inputs:
- folio-assistant/computations/chi-deuteron-h6-at-q0-50dps.witness.json
  (y_λ, χ^λ(β_D) for each of the 11 partitions of 6)
- AME binding energy B_D = 2.224566 MeV
- m_e = 0.51099895069 MeV

Path-D prediction:
  B_pred / m_e = Σ_λ y_λ · χ^λ(β_D) · Δ_λ

Output:
- folio-assistant/computations/option-e-deuteron-delta-lambda-probe.witness.json
"""


# Path bridge (subdirectory refactor — Phase 1, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the `probes/` cluster subdirectory. The bridge
# module also puts every other cluster subdir on sys.path so
# cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from mpmath import mpf, mp


def main() -> int:
    mp.dps = 50

    repo_root = Path(__file__).resolve().parent.parent.parent
    chi_path = (
        repo_root
        / "folio-assistant"
        / "computations"
        / "chi-deuteron-h6-at-q0-50dps.witness.json"
    )

    with chi_path.open() as f:
        chi_data = json.load(f)

    partitions_data = chi_data["by_partition"]
    assert len(partitions_data) == 11

    # Parse y_λ and χ^λ
    rows = []
    for entry in partitions_data:
        rows.append({
            "partition": entry["partition"] if isinstance(entry["partition"], list) else eval(entry["partition"]),
            "dim": int(entry["dim"]),
            "y_lambda": mpf(entry["y_lambda"]),
            "chi_lambda": mpf(entry["chi_lambda"]),
            "contribution": mpf(entry["contribution"]),  # y_λ * χ^λ
        })

    # AME data
    B_D_MeV = mpf("2.224566")
    m_e_MeV = mpf("0.51099895069")
    target = -B_D_MeV / m_e_MeV
    closure_threshold = mpf("0.10") * B_D_MeV

    # Candidate Δ_λ rules
    # Each is a function: row → Δ_λ value
    def rule_uniform_minus_one(row):
        """Δ_λ = -1 for all partitions (baseline)."""
        return mpf(-1)

    def rule_depth_inverse(row):
        """Δ_λ = -1 / length(partition) (depth = partition length)."""
        return mpf(-1) / mpf(len(row["partition"]))

    def rule_depth_inverse_largest(row):
        """Δ_λ = -1 / max(partition) (depth = largest part)."""
        return mpf(-1) / mpf(max(row["partition"]))

    def rule_dim_inverse(row):
        """Δ_λ = -1 / dim(V_λ) (weighted by representation dim)."""
        return mpf(-1) / mpf(row["dim"])

    def rule_sign_alternating(row):
        """Δ_λ = (-1)^(partition_length) (alternating sign by length)."""
        return mpf(-1) ** len(row["partition"])

    def rule_n_minus_length_inverse(row):
        """Δ_λ = -(6 - length(λ)) / 6, vanishes for trivial partition (1,...,1)."""
        return -mpf(6 - len(row["partition"])) / mpf(6)

    def rule_largest_minus_one(row):
        """Δ_λ = -(largest_part - 1), penalises wide partitions strongly."""
        return -mpf(max(row["partition"]) - 1)

    rules = [
        ("uniform_minus_one", rule_uniform_minus_one),
        ("depth_inverse_length", rule_depth_inverse),
        ("depth_inverse_largest", rule_depth_inverse_largest),
        ("dim_inverse", rule_dim_inverse),
        ("sign_alternating", rule_sign_alternating),
        ("n_minus_length_over_n", rule_n_minus_length_inverse),
        ("largest_minus_one", rule_largest_minus_one),
    ]

    # Run each rule
    results = []
    for rule_name, rule_fn in rules:
        sum_term = mpf(0)
        per_partition = []
        for row in rows:
            delta = rule_fn(row)
            term = row["contribution"] * delta
            sum_term += term
            per_partition.append({
                "partition": str(row["partition"]),
                "delta_lambda": str(delta),
                "term": str(term),
            })

        # Path-D B_pred (signed)
        B_pred_over_me = sum_term
        B_pred_MeV = m_e_MeV * B_pred_over_me

        # Closure check (using absolute value of B_pred for comparison
        # since AME B_D is positive but B_pred = m_e * Σ has its own sign;
        # the target is -B_D / m_e, so we compare |B_pred + B_D| against threshold)
        signed_residual = B_pred_MeV + B_D_MeV  # closure means this is ~0
        abs_residual = abs(signed_residual)
        closes = abs_residual <= closure_threshold
        rel_error_pct = 100 * abs_residual / B_D_MeV

        results.append({
            "rule_name": rule_name,
            "B_pred_over_me": str(B_pred_over_me),
            "B_pred_MeV": str(B_pred_MeV),
            "target_signed": str(target),
            "B_D_MeV": str(B_D_MeV),
            "signed_residual_MeV": str(signed_residual),
            "abs_residual_MeV": str(abs_residual),
            "rel_error_pct": str(rel_error_pct),
            "closes_within_10pct": bool(closes),
            "per_partition_terms": per_partition,
        })

    # Identify the best rule (smallest |residual|)
    best = min(results, key=lambda r: abs(mpf(r["abs_residual_MeV"])))

    # Write witness
    witness = {
        "engine": "python",
        "engineVersion": f"python {sys.version_info.major}.{sys.version_info.minor}",
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "computation": "option-e-deuteron-delta-lambda-probe",
        "description": (
            "Option E candidate Δ_λ rules tested against AME deuteron "
            "binding energy via Path-D mass prediction. Companion to "
            "QOU.OptionE.DeuteronVerification Lean infrastructure."
        ),
        "scriptFile": "option_e_deuteron_delta_lambda_probe.py",
        "precisionMetadata": {
            "compute_dps": 50,
            "output_dps": 30,
        },
        "ame_data": {
            "B_D_MeV": str(B_D_MeV),
            "m_e_MeV": str(m_e_MeV),
            "target_signed_in_m_e_units": str(target),
            "closure_threshold_10pct_MeV": str(closure_threshold),
        },
        "n_partitions": 11,
        "n_rules_tested": len(rules),
        "rules": [r[0] for r in rules],
        "results": results,
        "best_rule": {
            "name": best["rule_name"],
            "abs_residual_MeV": best["abs_residual_MeV"],
            "rel_error_pct": best["rel_error_pct"],
            "closes_within_10pct": best["closes_within_10pct"],
        },
        "verdict": (
            "CLOSES" if best["closes_within_10pct"]
            else "FAILS — all 7 candidate rules miss AME 10% threshold"
        ),
        "honest_assessment": (
            "These are 7 simple substrate-derived rules. None is the "
            "canonical Option E rule (which requires crystal-graph "
            "depth from explicit SYT enumeration + Brundan-Kleshchev "
            "lift). The probe verifies the verification harness works "
            "and quantifies how far simple rules are from closure."
        ),
    }

    out_path = (
        repo_root
        / "folio-assistant"
        / "computations"
        / "option-e-deuteron-delta-lambda-probe.witness.json"
    )
    with out_path.open("w") as f:
        json.dump(witness, f, indent=2)

    print(f"Wrote {out_path}")
    print(f"Best rule: {best['rule_name']}")
    print(f"  abs residual: {best['abs_residual_MeV']} MeV")
    print(f"  rel error:    {best['rel_error_pct']}%")
    print(f"  closes 10%:   {best['closes_within_10pct']}")
    print(f"Verdict: {witness['verdict']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
