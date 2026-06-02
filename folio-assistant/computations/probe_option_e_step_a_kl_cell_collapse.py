#!/usr/bin/env python3
# polynomial_q_not_applicable: EXPLORATORY refutation probe per
#   `production-vs-exploratory-discipline`. Verifies the predicted
#   collapse of the Option-E PROBE 4 ansatz under the standard KL-
#   cell n^w_λ multiplicities (which are trivial-delta for S_n by
#   the proved Kazhdan-Lusztig conjecture in type A).  Reads
#   canonical witness data only.  Asserts the predicted refutation.
"""
Option-E Phase 2 PROBE 4 — Step A: KL-cell n^w_λ collapse on
the deuteron.

# Ref: docs/audits/2026-06-02-option-e-probe4-closure-deuteron-design.md
# Ref: docs/coordination/option-e.md (master ledger, PROBE 4)
# Ref: PR #1714 (KL recursion scaffold)
# Ref: PR #1516 (cheap-pass refutation of single-vertex shortcuts)

## What this Step does

The Option-E ansatz is

    Δ_λ(K) = Σ_w n^w_λ · ρ_w(K)

with `ρ_w(K) = ⟨v_T | ρ_λ(β_K) | v_T⟩` (Hoefsmit/Young seminormal
trace at crystal vertex w = T ∈ SYT(λ)) and `n^w_λ` = Kazhdan-
Lusztig multiplicities.

For the symmetric group S_n, the Kazhdan-Lusztig two-sided cell
containing w corresponds (via RSK) to the partition `shape(w)`
of the common shape of (P(w), Q(w)).  The KL conjecture
(proved for type A by Kazhdan-Lusztig themselves) says each
left-cell module L_C decomposes as a SINGLE copy of V_λ where
λ = shape(C).  So `n^w_λ = δ_{λ, shape(w)}` (trivial delta).

This gives **two natural Step-A variants**, depending on whether
we sum over the WHOLE two-sided cell C_λ or just over ONE left
cell:

  **Variant v1** (whole two-sided cell, multiplicity-1 per w):
    Σ_{w ∈ C_λ} ρ_w(K) = f^λ · χ^λ(β_K)
                       (each of the f^λ left cells contributes a
                       full trace χ^λ(β_K))

  **Variant v2** (one left cell, the canonical one):
    Σ_{w ∈ L_C, T(w) = T_0} ρ_w(K) = χ^λ(β_K)
                       (single trace; equivalent to the
                       rho_w_crystal_vertex_trace.py
                       regular-multiplicity result already refuted
                       on main)

Both candidates assemble into

    S^{(X)} = Σ_λ y_λ(q_0) · χ^λ(β_D) · Δ_λ^{(X)}

and are compared to the empirical target_signed = −4.35337.

## Why this matters

If BOTH variants refute (predicted), the standard KL-cell reading
of PROBE 4 is exhausted on the deuteron.  The remaining live in-
Option-E directions are the four non-standard Step-B variants
(quantum-dim weighted, Demazure sub-crystal, W-graph edge-weight,
Type-B folded crystal).

## Usage

    cd folio-assistant/computations
    python3 probe_option_e_step_a_kl_cell_collapse.py

Emits: probe-option-e-step-a-kl-cell-collapse.witness.json
"""
from __future__ import annotations
import json
import sys
import warnings
from pathlib import Path
from datetime import datetime, timezone

warnings.filterwarnings("ignore")
sys.path.insert(0, str(Path(__file__).resolve().parent))
import _path_bridge  # noqa: F401, E402

import mpmath as mp  # noqa: E402
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()


def load_witness(name: str) -> dict:
    return json.loads((Path(__file__).parent / name).read_text())


# ── Inputs ────────────────────────────────────────────────────────
chi_w = load_witness("chi-deuteron-h6-at-q0-50dps.witness.json")
empirical_w = load_witness("delta-lambda-empirical-tabulation.witness.json")

target_signed = mp.mpf(empirical_w["data"]["per_atom"]["D"]["target_signed"])
tr_M_D = mp.mpf(chi_w["tr_M_at_q0"])

# Build per-partition records: y_λ, χ^λ(β_D), f^λ (= dim_λ).
def part_key(plist: list[int]) -> str:
    return "_".join(str(p) for p in plist)

per_partition = {}
for entry in chi_w["by_partition"]:
    key = part_key(entry["partition"])
    per_partition[key] = {
        "dim": entry["dim"],
        "y_lambda": mp.mpf(entry["y_lambda"]),
        "chi_beta_D": mp.mpf(entry["chi_lambda"]),
    }

# ── Compute the two Step-A variants ──────────────────────────────
#
# S_v1 = Σ_λ y_λ · χ^λ(β_D) · (f^λ · χ^λ(β_D))
#      = Σ_λ y_λ · f^λ · (χ^λ(β_D))²
#
# S_v2 = Σ_λ y_λ · χ^λ(β_D) · χ^λ(β_D)
#      = Σ_λ y_λ · (χ^λ(β_D))²

S_v1 = mp.mpf(0)
S_v2 = mp.mpf(0)
per_lambda = []
for key, p in per_partition.items():
    chi_sq = p["chi_beta_D"] ** 2
    contrib_v1 = p["y_lambda"] * p["dim"] * chi_sq
    contrib_v2 = p["y_lambda"] * chi_sq
    S_v1 += contrib_v1
    S_v2 += contrib_v2
    per_lambda.append({
        "partition": key,
        "dim": p["dim"],
        "y_lambda": str(p["y_lambda"]),
        "chi_beta_D": str(p["chi_beta_D"]),
        "chi_beta_D_squared": str(chi_sq),
        "contrib_v1_y_dim_chi_sq": str(contrib_v1),
        "contrib_v2_y_chi_sq": str(contrib_v2),
    })

rel_err_v1 = abs(S_v1 - target_signed) / abs(target_signed)
rel_err_v2 = abs(S_v2 - target_signed) / abs(target_signed)
closes_v1 = (rel_err_v1 < mp.mpf("0.10"))
closes_v2 = (rel_err_v2 < mp.mpf("0.10"))

# ── Refutation assertion (expected-negative shape) ────────────────
assertions = [{
    "name": "neither_step_a_variant_closes_within_10pct",
    "expected_closes_v1": False,
    "expected_closes_v2": False,
    "actual_closes_v1": bool(closes_v1),
    "actual_closes_v2": bool(closes_v2),
    "passed": not (closes_v1 or closes_v2),
    "note": (
        "Predicted: both Step-A variants miss ≥ 10%; v2 reproduces "
        "the rho_w_crystal_vertex_trace.py 'does_not_close' verdict "
        "via the trace identity Σ_w ρ_w = χ^λ; v1 adds the f^λ "
        "factor for summing across all left cells of the two-sided "
        "cell C_λ.  Both are bound to refute (expected-negative)."
    ),
}]
all_passed = all(a["passed"] for a in assertions)

out = {
    "computation": "option-e-probe4-step-a-kl-cell-collapse",
    "auditOnly": True,
    "description": (
        "Option-E PROBE 4 Step A: tests the trivial KL-cell "
        "multiplicity Δ_λ = Σ_w n^w_λ · ρ_w(K) with n^w_λ = "
        "δ_{λ, shape(w)} (proved KL-cell decomposition for type A) "
        "in two normalisation variants.  Reads canonical witness "
        "data only.  Asserts expected-negative refutation."
    ),
    "timestamp_utc": datetime.now(timezone.utc).isoformat(),
    "inputs": {
        "chi_deuteron_h6_witness": "chi-deuteron-h6-at-q0-50dps.witness.json",
        "empirical_target_witness": "delta-lambda-empirical-tabulation.witness.json",
    },
    "target_signed": str(target_signed),
    "tr_M_D_at_q0": str(tr_M_D),
    "variants": {
        "v1_whole_two_sided_cell": {
            "formula": "Δ_λ = f^λ · χ^λ(β_D)  ⟹  S = Σ_λ y_λ · f^λ · (χ^λ)²",
            "S_value": str(S_v1),
            "rel_err": str(rel_err_v1),
            "closes_within_10pct": bool(closes_v1),
            "note": (
                "Sums ρ_w over the whole two-sided KL cell C_λ; the "
                "|C_λ| = (f^λ)² elements partition into f^λ left "
                "cells each contributing trace χ^λ(β_D)."
            ),
        },
        "v2_single_left_cell": {
            "formula": "Δ_λ = χ^λ(β_D)  ⟹  S = Σ_λ y_λ · (χ^λ)²",
            "S_value": str(S_v2),
            "rel_err": str(rel_err_v2),
            "closes_within_10pct": bool(closes_v2),
            "note": (
                "Sums ρ_w over a single left cell of C_λ; equivalent "
                "by the trace identity to rho_w_crystal_vertex_trace.py "
                "regular-multiplicity result (closure_status: "
                "does_not_close)."
            ),
        },
    },
    "per_lambda_contributions": per_lambda,
    "assertions": assertions,
    "allPassed": bool(all_passed),
    "verdict": (
        "BOTH Step-A variants REFUTED (predicted by design).  "
        "Standard KL-cell reading of PROBE 4 exhausted on deuteron.  "
        "Live in-Option-E directions remaining: 4 Step-B non-standard "
        "variants (quantum-dim, Demazure, W-graph, Type-B folded)."
        if not (closes_v1 or closes_v2) else
        "POSITIVE FINDING — at least one Step-A variant closed.  "
        "Surprise vs. theoretical prediction; escalate to deeper "
        "verification."
    ),
}

out_path = Path(__file__).parent / "probe-option-e-step-a-kl-cell-collapse.witness.json"
with open(out_path, "w") as fp:
    json.dump(out, fp, indent=2)

print("=" * 72)
print(" Option-E PROBE 4 Step A — KL-cell trivial-multiplicity collapse")
print("=" * 72)
print(f"  target_signed = {float(target_signed):+.6f}")
print(f"  tr_M(β_D)     = {float(tr_M_D):.6f}")
print()
print(f"  {'Variant':<26s} {'S':>16s} {'rel_err':>12s} {'closes ≤10%':>14s}")
print(f"  {'v1 (whole 2-sided cell)':<26s} {float(S_v1):>+16.6f} "
      f"{float(rel_err_v1)*100:>11.2f}% {str(closes_v1):>14s}")
print(f"  {'v2 (single left cell)':<26s} {float(S_v2):>+16.6f} "
      f"{float(rel_err_v2)*100:>11.2f}% {str(closes_v2):>14s}")
print()
print(f"  Verdict: {out['verdict']}")
print()
print(f"  All assertions passed: {all_passed}")
print(f"  Witness: {out_path}")

if not all_passed:
    sys.exit(1)
