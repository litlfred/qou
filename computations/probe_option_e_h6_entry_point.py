#!/usr/bin/env python3
# polynomial_q_not_applicable: structural cross-check probe — reads
#   the per-block H_6 Hoefsmit-seminormal Gram from
#   option-e-phase1-gram-h6.witness.json (PR #1697) and exposes the
#   structural data PROBE 1 / PROBE 4 of the Option-E ledger need.
#   NOT a fit; NOT a derivation; reads canonical witness data only.
"""
Phase 2 entry-point probe for Option E at H_6 (deuteron scope).

# Ref: docs/audits/2026-05-25-option-e-crystal-weight-delta-lambda.md
# Ref: docs/coordination/option-e.md (master ledger, PROBE 1 + PROBE 4)
# Ref: PR #1697 (Phase 1 H_6 Gram landed)

## What this probe does

H_6 analogue of probe_option_e_h3_entry_point.py.  Reads the
per-partition Hoefsmit-seminormal data from
option-e-phase1-gram-h6.witness.json (11 partitions of 6) and
exposes the structural quantities consumed by Phase 2 derive-or-
falsify probes:

1. **Per-block invertibility fingerprint** — confirms σ_k matrices
   for each of the 5 generators × 11 blocks are non-degenerate
   (det ≠ 0, condition number bounded) at q_0.
2. **Sum-of-squares identity** — Σ_λ dim_λ² = n! = 720 for H_6,
   structural sanity check on the partition coverage.
3. **PROBE 1 data exposure (#1707)** — tabulates
   tr(ρ_λ(σ_1)) and (1 + tr(ρ_λ(σ_1)))/2 per block, lets the
   (1+q_0)/2 derivation in #1707 read the data without recomputing.
4. **PROBE 4 data exposure (#1516)** — tabulates the diagonal of
   ρ_λ(w_0) per block (Hoefsmit-seminormal diagonalises w_0 on
   the YT basis); these are the candidate crystal-vertex weights
   for the Δ_λ(K) = Σ_w n^w_λ · ρ_w(K) ansatz at H_6.
5. **χ_λ(w_0) cross-check propagation** — confirms each block's
   direct-vs-chain residual is ≤ 1e-12 (already in the input
   witness; re-asserted here for the audit trail).

This is a **structural probe** — it does not close Δ_λ(D), does
not derive (1+q)/2, does not enumerate crystal vertices.  It
exposes data so the derive-or-falsify probes in #1707 (PROBE 1)
and this PR's PROBE 4 work can consume the H_6 Hoefsmit data
without recomputing the σ_k matrices.

## Usage

    cd computations
    python3 probe_option_e_h6_entry_point.py

Emits: probe-option-e-h6-entry-point.witness.json
"""
from __future__ import annotations
import json
import sys
import warnings
from pathlib import Path
from datetime import datetime, timezone

warnings.filterwarnings("ignore")
sys.path.insert(0, str(Path(__file__).resolve().parent))
import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/

import mpmath as mp  # noqa: E402
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()


def load_witness(name: str) -> dict:
    return json.loads((Path(__file__).parent / name).read_text())


# ── Load #1697's H_6 Gram witness ─────────────────────────────────
gram_w = load_witness("option-e-phase1-gram-h6.witness.json")
h6 = gram_w["data"]["h6"]
q0_str = gram_w["data"]["q_0_50dps"]
q0 = mp.mpf(q0_str)

# ── Cross-check 1: per-block σ_k invertibility ────────────────────
block_invertibility = []
all_invertible = True
for pname, pdata in h6["blocks"].items():
    dets = [mp.mpf(repr(d)) for d in pdata["sigma_k_dets"]]
    conds = [mp.mpf(repr(c)) for c in pdata["sigma_k_conds"]]
    min_abs_det = min(abs(d) for d in dets)
    max_cond = max(conds)
    invertible = min_abs_det > mp.mpf("1e-12")
    if not invertible:
        all_invertible = False
    block_invertibility.append({
        "partition": pname,
        "dim": pdata["dim"],
        "min_abs_det_sigma_k": str(min_abs_det),
        "max_cond_sigma_k": str(max_cond),
        "invertible": bool(invertible),
    })

# ── Cross-check 2: Σ dim_λ² = n! = 720 ────────────────────────────
total_dim_sq = sum(pdata["dim"] ** 2 for pdata in h6["blocks"].values())
sum_of_squares_ok = (total_dim_sq == 720)

# ── PROBE 1 data exposure: tr(ρ_λ(σ_1)) per block ─────────────────
sigma_1_traces = []
half_one_plus_q_target = (1 + q0) / 2  # ≈ 1.0549893
for pname, pdata in h6["blocks"].items():
    sig1 = pdata["sigma_k_at_q0_re"][0]  # 0-indexed → σ_1
    dim = pdata["dim"]
    trace = sum(mp.mpf(repr(sig1[i][i])) for i in range(dim))
    half = (1 + trace) / 2
    sigma_1_traces.append({
        "partition": pname,
        "dim": dim,
        "tr_sigma_1": str(trace),
        "one_plus_tr_over_2": str(half),
        "diff_from_target": str(half - half_one_plus_q_target),
    })

# ── PROBE 4 data exposure: ρ_λ(w_0) diagonal per block ────────────
w0_diagonals = []
for pname, pdata in h6["blocks"].items():
    w0 = pdata["w0_matrix_at_q0_re"]
    dim = pdata["dim"]
    diag = [str(mp.mpf(repr(w0[i][i]))) for i in range(dim)]
    diag_sum = sum(mp.mpf(repr(w0[i][i])) for i in range(dim))  # = χ_λ(w_0)
    w0_diagonals.append({
        "partition": pname,
        "dim": dim,
        "w0_diagonal": diag,
        "diagonal_sum": str(diag_sum),
        "chi_lambda_w0_witness": str(pdata["chi_lambda_w0_direct"]),
    })

# ── χ_λ(w_0) cross-check residual propagation ─────────────────────
max_chi_residual = max(
    mp.mpf(repr(pdata["cross_check_residual"]))
    for pdata in h6["blocks"].values()
)
chi_cross_check_ok = max_chi_residual < mp.mpf("1e-12")

out = {
    "computation": "option-e-h6-entry-point",
    "description": (
        "Phase 2 entry-point structural cross-check at H_6 / deuteron "
        "scope. Consumes option-e-phase1-gram-h6.witness.json from "
        "PR #1697. NOT a fit; NOT a derivation; reads canonical "
        "Hoefsmit-seminormal witness data and exposes per-block "
        "structural quantities for ledger PROBE 1 (#1707, derive "
        "(1+q)/2) and ledger PROBE 4 (#1516, Kashiwara-crystal-"
        "coefficient angle)."
    ),
    "timestamp_utc": datetime.now(timezone.utc).isoformat(),
    "inputs": {
        "h6_gram_witness": "option-e-phase1-gram-h6.witness.json",
        "h6_gram_witness_commit_sha": gram_w.get("commitSha"),
    },
    "q_0_50dps": q0_str,
    "half_one_plus_q_0": str(half_one_plus_q_target),
    "cross_checks": {
        "all_blocks_invertible": bool(all_invertible),
        "sum_of_squares_ok": bool(sum_of_squares_ok),
        "total_dim_sq": total_dim_sq,
        "chi_cross_check_ok": bool(chi_cross_check_ok),
        "max_chi_residual": str(max_chi_residual),
    },
    "block_invertibility_h6": block_invertibility,
    "probe1_data_exposure_tr_sigma_1": sigma_1_traces,
    "probe4_data_exposure_w0_diagonal": w0_diagonals,
    "phase_2_scope_notes": [
        ("PROBE 1 (#1707) consumes 'probe1_data_exposure_tr_sigma_1' "
         "to test whether (1 + tr(ρ_λ(σ_1)))/2 matches (1+q_0)/2 "
         "for some λ or weighted sum."),
        ("PROBE 4 (this PR) consumes 'probe4_data_exposure_w0_diagonal' "
         "as the candidate crystal-vertex weight data for the "
         "Δ_λ(K) = Σ_w n^w_λ · ρ_w(K) ansatz."),
        ("Open: derive the n^w_λ coefficients (Kazhdan-Lusztig "
         "multiplicities) and verify against probe-1's empirical "
         "Δ_λ(D) under bar-invariance."),
    ],
}

out_path = Path(__file__).parent / "probe-option-e-h6-entry-point.witness.json"
with open(out_path, "w") as fp:
    json.dump(out, fp, indent=2)

print("Phase 2 H_6 entry-point probe complete")
print("=" * 60)
print(f"  Inputs: option-e-phase1-gram-h6.witness.json")
print(f"  q_0 ≈ {float(q0):.6f}, (1+q_0)/2 ≈ {float(half_one_plus_q_target):.6f}")
print()
print(f"  Cross-checks:")
print(f"    all blocks invertible:  {all_invertible}")
print(f"    Σ dim_λ² = 720:         {sum_of_squares_ok} (got {total_dim_sq})")
print(f"    χ_λ(w_0) cross-check:   {chi_cross_check_ok} "
      f"(max residual {float(max_chi_residual):.2e})")
print()
print(f"  Per-block tr(ρ_λ(σ_1)) and (1+tr)/2 vs (1+q_0)/2 ≈ "
      f"{float(half_one_plus_q_target):.4f}:")
print(f"    {'λ':<14s} {'dim':>4s} {'tr(σ_1)':>10s} {'(1+tr)/2':>12s} "
      f"{'diff':>12s}")
for t in sigma_1_traces:
    print(f"    {t['partition']:<14s} {t['dim']:>4d} "
          f"{float(mp.mpf(t['tr_sigma_1'])):>10.4f} "
          f"{float(mp.mpf(t['one_plus_tr_over_2'])):>12.4f} "
          f"{float(mp.mpf(t['diff_from_target'])):>+12.4f}")
print()
print(f"  Witness: {out_path}")
