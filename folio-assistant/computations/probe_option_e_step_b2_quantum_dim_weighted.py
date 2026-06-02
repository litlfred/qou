#!/usr/bin/env python3
# polynomial_q_not_applicable: EXPLORATORY Step-B variant per
#   `production-vs-exploratory-discipline`. Tests the quantum-
#   dimension qdim_λ(q_0) substitution in the Step-A v1 formula
#   (replacing f^λ).  Reads canonical witness data only.  Asserts
#   the expected-negative shape (refutation) unless the deformation
#   accidentally closes.
"""
Option-E Phase 2 PROBE 4 — Step B-2: quantum-dim weighted variant.

# Ref: docs/audits/2026-06-02-option-e-probe4-closure-deuteron-design.md
# Ref: docs/coordination/option-e.md (master ledger, PROBE 4)
# Ref: PR #1714 (KL recursion scaffold)
# Ref: probe_option_e_step_a_kl_cell_collapse.py (Step A refutation)

## What this Step does

Step A refuted the trivial KL-cell n^w_λ = δ_{λ, shape(w)} reading
in two normalisations:
- v1 (whole 2-sided cell): Δ_λ = f^λ · χ^λ(β_D)
- v2 (single left cell):   Δ_λ = χ^λ(β_D)

Step B-2 explores the natural q-deformation: replace the classical
dimension f^λ with the q-dimension qdim_λ(q_0) in v1:

  **Variant B-2a**: Δ_λ = qdim_λ(q_0) · χ^λ(β_D)
                   ⟹  S = Σ_λ y_λ · qdim_λ(q_0) · (χ^λ)²

This is structurally motivated: at q_0 ≠ 1, the Hecke algebra
H_n(q) is NOT semisimple-isomorphic to ℂ[S_n], and the irreps V_λ
have q-dimensions that genuinely differ from f^λ.  If the
"correct" cell-multiplicity is f^λ at q=1 (classical), the
deformation at q_0 should be qdim_λ(q_0).

  qdim_λ(q) = [n]_q! / ∏_{c ∈ λ} [h(c)]_q

(q-deformation of the hook-length formula; at q=1, [k]_q = k so
qdim_λ(1) = f^λ.)

This probe also computes **Variant B-2b** with the simpler form
Δ_λ = qdim_λ(q_0) only (no χ factor), as a control.

## Usage

    cd folio-assistant/computations
    python3 probe_option_e_step_b2_quantum_dim_weighted.py

Emits: probe-option-e-step-b2-quantum-dim-weighted.witness.json
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


# ── q-integer + q-factorial utilities ────────────────────────────
def q_int(k: int, q: mp.mpf) -> mp.mpf:
    """[k]_q = (1 − q^k) / (1 − q) = 1 + q + q² + … + q^{k−1}.

    At q = 1 this is k; at q ≠ 1 it's the standard q-deformation.
    """
    if k == 0:
        return mp.mpf(0)
    return (1 - q ** k) / (1 - q)


def q_factorial(n: int, q: mp.mpf) -> mp.mpf:
    """[n]_q! = ∏_{k=1}^{n} [k]_q."""
    out = mp.mpf(1)
    for k in range(1, n + 1):
        out *= q_int(k, q)
    return out


# ── Hook lengths + quantum dimension ─────────────────────────────
def transpose(part: list[int]) -> list[int]:
    """Conjugate partition (transpose of the Young diagram)."""
    if not part:
        return []
    max_len = part[0]
    return [sum(1 for p in part if p >= i + 1) for i in range(max_len)]


def hook_lengths(part: list[int]) -> list[int]:
    """All hook lengths of partition `part`."""
    pt = transpose(part)
    hooks: list[int] = []
    for i, lam_i in enumerate(part):
        for j in range(lam_i):
            # h(i,j) = λ_i − j − 1 + λ'_j − i + 1 = λ_i + λ'_j − i − j − 1
            # (Using 0-indexed (i, j); careful with off-by-one.)
            h = lam_i + pt[j] - i - j - 1
            hooks.append(h)
    return hooks


def qdim(part: list[int], q: mp.mpf) -> mp.mpf:
    """q-deformation of f^λ via the hook-length formula:

      qdim_λ(q) = [n]_q! / ∏_{c ∈ λ} [h(c)]_q

    At q = 1 this reduces to the classical hook formula
    f^λ = n! / ∏ h(c).
    """
    n = sum(part)
    num = q_factorial(n, q)
    den = mp.mpf(1)
    for h in hook_lengths(part):
        den *= q_int(h, q)
    return num / den


# ── Inputs ────────────────────────────────────────────────────────
chi_w = load_witness("chi-deuteron-h6-at-q0-50dps.witness.json")
empirical_w = load_witness("delta-lambda-empirical-tabulation.witness.json")

target_signed = mp.mpf(empirical_w["data"]["per_atom"]["D"]["target_signed"])
q_0 = mp.mpf(chi_w["q_0_50dps"])

# Sanity: qdim_λ(1) should equal f^λ.
qdim_at_one_check = []
for entry in chi_w["by_partition"]:
    part = entry["partition"]
    f_lam = entry["dim"]
    qdim_1 = qdim(part, mp.mpf("0.99999999999999"))  # numeric q=1 approx
    diff = abs(float(qdim_1) - f_lam)
    qdim_at_one_check.append({
        "partition": "_".join(str(p) for p in part),
        "f_lam": f_lam,
        "qdim_at_q_near_1": str(qdim_1),
        "diff": diff,
    })
sanity_max_diff = max(c["diff"] for c in qdim_at_one_check)
sanity_ok = sanity_max_diff < 1e-6

# Compute the variants ────────────────────────────────────────────
S_v1_at_q0 = mp.mpf(0)
S_b2a = mp.mpf(0)   # qdim · χ
S_b2b = mp.mpf(0)   # qdim alone
per_lambda = []
for entry in chi_w["by_partition"]:
    part = entry["partition"]
    f_lam = entry["dim"]
    y = mp.mpf(entry["y_lambda"])
    chi = mp.mpf(entry["chi_lambda"])
    q_dim = qdim(part, q_0)
    chi_sq = chi ** 2
    # Reference: Step A v1 with f^λ
    S_v1_at_q0 += y * f_lam * chi_sq
    # Variant B-2a: replace f^λ by qdim_λ(q_0)
    S_b2a += y * q_dim * chi_sq
    # Variant B-2b: Δ_λ = qdim_λ(q_0) directly (no extra χ)
    S_b2b += y * chi * q_dim
    per_lambda.append({
        "partition": "_".join(str(p) for p in part),
        "f_lam": f_lam,
        "qdim_at_q0": str(q_dim),
        "qdim_over_f_lam": str(q_dim / f_lam),
        "y_lambda": str(y),
        "chi_beta_D": str(chi),
        "contrib_b2a_y_qdim_chi_sq": str(y * q_dim * chi_sq),
        "contrib_b2b_y_chi_qdim": str(y * chi * q_dim),
    })

rel_err_v1 = abs(S_v1_at_q0 - target_signed) / abs(target_signed)
rel_err_b2a = abs(S_b2a - target_signed) / abs(target_signed)
rel_err_b2b = abs(S_b2b - target_signed) / abs(target_signed)
closes_b2a = rel_err_b2a < mp.mpf("0.10")
closes_b2b = rel_err_b2b < mp.mpf("0.10")

assertions = [{
    "name": "qdim_at_q1_matches_f_lam_sanity",
    "passed": bool(sanity_ok),
    "max_diff_qdim_minus_f_lam_at_q_near_1": sanity_max_diff,
    "expected": "< 1e-6",
}, {
    "name": "neither_step_b2_variant_closes_within_10pct",
    "expected_closes_b2a": False,
    "expected_closes_b2b": False,
    "actual_closes_b2a": bool(closes_b2a),
    "actual_closes_b2b": bool(closes_b2b),
    "passed": not (closes_b2a or closes_b2b),
    "note": (
        "Predicted: q-deformation of f^λ at q_0 ≈ 1.11 shifts "
        "S_v1 from +6.007 to S_b2a by a small amount (typically "
        "~10-20% relative); not enough to close the 238% miss to "
        "target_signed = −4.353.  Wrong-sign survives the "
        "deformation too."
    ),
}]
all_passed = all(a["passed"] for a in assertions)

out = {
    "computation": "option-e-probe4-step-b2-quantum-dim-weighted",
    "auditOnly": True,
    "description": (
        "Option-E PROBE 4 Step B-2: tests the natural q-deformation "
        "of Step A's v1 formula (replace f^λ with qdim_λ(q_0)).  "
        "Reads canonical witness data only.  Asserts qdim(1) sanity "
        "+ expected-negative refutation."
    ),
    "timestamp_utc": datetime.now(timezone.utc).isoformat(),
    "inputs": {
        "chi_deuteron_h6_witness": "chi-deuteron-h6-at-q0-50dps.witness.json",
        "empirical_target_witness": "delta-lambda-empirical-tabulation.witness.json",
    },
    "q_0_at_50dps": chi_w["q_0_50dps"],
    "target_signed": str(target_signed),
    "qdim_at_q_near_1_sanity": qdim_at_one_check,
    "qdim_sanity_max_diff": sanity_max_diff,
    "S_a_v1_reference_with_f_lam": str(S_v1_at_q0),
    "variants": {
        "B2a_qdim_replaces_f_lam_in_v1": {
            "formula": "Δ_λ = qdim_λ(q_0) · χ^λ(β_D)  ⟹  S = Σ_λ y_λ · qdim_λ(q_0) · (χ^λ)²",
            "S_value": str(S_b2a),
            "rel_err": str(rel_err_b2a),
            "closes_within_10pct": bool(closes_b2a),
        },
        "B2b_qdim_alone": {
            "formula": "Δ_λ = qdim_λ(q_0)  ⟹  S = Σ_λ y_λ · χ^λ(β_D) · qdim_λ(q_0)",
            "S_value": str(S_b2b),
            "rel_err": str(rel_err_b2b),
            "closes_within_10pct": bool(closes_b2b),
        },
    },
    "per_lambda_contributions": per_lambda,
    "assertions": assertions,
    "allPassed": bool(all_passed),
    "verdict": (
        "BOTH B-2 variants REFUTED.  Quantum-dim deformation at "
        "q_0 ≈ 1.11 doesn't supply enough structural change to "
        "close the deuteron Δ_λ gap.  Adds B-2 to the cumulative "
        "Option-E refutation pile."
        if not (closes_b2a or closes_b2b) else
        "POSITIVE FINDING — at least one B-2 variant closed within "
        "10%.  q-deformation supplies the missing structure.  "
        "Escalate to Lean PROBE 3 conditional formalisation."
    ),
}

out_path = Path(__file__).parent / "probe-option-e-step-b2-quantum-dim-weighted.witness.json"
with open(out_path, "w") as fp:
    json.dump(out, fp, indent=2)

print("=" * 72)
print(" Option-E PROBE 4 Step B-2 — quantum-dim weighted")
print("=" * 72)
print(f"  q_0 ≈ {float(q_0):.6f}, target_signed = {float(target_signed):+.6f}")
print(f"  qdim(q≈1) ≈ f^λ sanity: max diff {sanity_max_diff:.2e} → {sanity_ok}")
print()
print(f"  Reference (Step A v1, f^λ at q_0):  S = {float(S_v1_at_q0):+.6f}")
print()
print(f"  {'Variant':<32s} {'S':>14s} {'rel_err':>10s} {'closes ≤10%':>14s}")
print(f"  {'B-2a: qdim · χ (replaces f^λ)':<32s} {float(S_b2a):>+14.6f} "
      f"{float(rel_err_b2a)*100:>9.2f}% {str(closes_b2a):>14s}")
print(f"  {'B-2b: qdim alone':<32s} {float(S_b2b):>+14.6f} "
      f"{float(rel_err_b2b)*100:>9.2f}% {str(closes_b2b):>14s}")
print()
print("  qdim_λ(q_0) / f^λ per partition:")
for c in per_lambda:
    ratio = float(mp.mpf(c["qdim_over_f_lam"]))
    print(f"    {c['partition']:<14s} f^λ={c['f_lam']:>3d}  qdim/f^λ = {ratio:.4f}")
print()
print(f"  Verdict: {out['verdict']}")
print(f"  All assertions passed: {all_passed}")
print(f"  Witness: {out_path}")

if not all_passed:
    sys.exit(1)
