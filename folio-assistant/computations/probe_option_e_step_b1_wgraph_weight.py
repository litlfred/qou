#!/usr/bin/env python3
# polynomial_q_not_applicable: EXPLORATORY Step-B variant per
#   `production-vs-exploratory-discipline`. Tests W-graph edge-weight
#   μ(y, w) as the multiplicity n^w_λ in the Option-E ansatz.  Reads
#   canonical witness data only.  Stacks on top of PR #1714's KL
#   recursion (memoized via `kazhdan_lusztig.py`).
"""
Option-E Phase 2 PROBE 4 — Step B-1: W-graph edge-weight μ(y, w).

# Ref: docs/audits/2026-06-02-option-e-probe4-closure-deuteron-design.md
# Ref: PR #1714 (KL recursion scaffold — provides μ via _mu helper)
# Ref: probe_option_e_step_a_kl_cell_collapse.py (Step A)
# Ref: probe_option_e_step_b2_quantum_dim_weighted.py (Step B-2)

## What this Step does

The W-graph of S_n has vertex set = S_n and labeled edges (y, w)
where μ(y, w) is the Kazhdan-Lusztig leading coefficient — the
coefficient of q^{(ℓ(w) − ℓ(y) − 1)/2} in P_{y, w}(q) (zero
unless ℓ(w) − ℓ(y) is odd).

The W-graph carries the SAME information as the canonical-basis
structure constants C_s · C_w = (q + q⁻¹) C_w + Σ μ(z, w) C_z
(when sw < w).  So it's a natural source of non-trivial
multiplicity n^w_λ beyond the trivial-cell delta.

This probe tests three W-graph-derived multiplicities n^w_λ:

  **Variant B-1a (total μ-degree weight):**
    n^w_λ := μ_deg(w)  if shape(w) = λ, else 0
    where μ_deg(w) := Σ_{y < w} |μ(y, w)|
  ⟹ Δ_λ = Σ_{w: shape(w)=λ} μ_deg(w) · ρ_w(β_D)
        ≈ (sum of μ-degrees over the two-sided cell) · χ^λ(β_D)/f^λ

  **Variant B-1b (μ-edge-counted multiplicity):**
    n^w_λ := |{y < w : μ(y, w) ≠ 0}|  if shape(w) = λ, else 0
    (count of non-trivial outgoing μ-edges)

  **Variant B-1c (full μ sum across all (y, w) with shape(w)=λ):**
    Δ_λ := Σ_{(y,w): shape(w)=λ, μ(y,w)≠0} μ(y, w) · ⟨v_{P(w)}|ρ_λ(β_D)|v_{P(w)}⟩

For the diagonal trace approximation, we use
  ⟨v_T|ρ_λ(β_D)|v_T⟩ ≈ χ^λ(β_D) / f^λ
(average diagonal entry; weak approximation but enough for the
refutation magnitude).

## Usage

    cd folio-assistant/computations
    python3 probe_option_e_step_b1_wgraph_weight.py

Emits: probe-option-e-step-b1-wgraph-weight.witness.json
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
from kazhdan_lusztig import (  # noqa: E402
    permutations_S_n, bruhat_le, length,
    _mu, kl_polynomial_recursive, _kl_cache_clear, _kl_cache_size,
)

set_compute_dps()


def load_witness(name: str) -> dict:
    return json.loads((Path(__file__).parent / name).read_text())


# ── RSK shape (Robinson-Schensted row insertion) ─────────────────
def rsk_shape(w: tuple[int, ...]) -> tuple[int, ...]:
    """Compute the partition `shape(w)` via row insertion.  Returns
    the row lengths of the P-tableau (= Q-tableau in shape) under
    RSK applied to w."""
    P: list[list[int]] = []
    for val in w:
        x = val
        placed = False
        for row in P:
            # Find leftmost element > x in this row (binary search
            # is overkill at n=6; linear is fine).
            j = 0
            while j < len(row) and row[j] <= x:
                j += 1
            if j == len(row):
                row.append(x)
                placed = True
                break
            else:
                x, row[j] = row[j], x
        if not placed:
            P.append([x])
    return tuple(len(row) for row in P)


# ── Inputs ────────────────────────────────────────────────────────
chi_w = load_witness("chi-deuteron-h6-at-q0-50dps.witness.json")
empirical_w = load_witness("delta-lambda-empirical-tabulation.witness.json")
target_signed = mp.mpf(empirical_w["data"]["per_atom"]["D"]["target_signed"])

per_partition = {}
for entry in chi_w["by_partition"]:
    key = "_".join(str(p) for p in entry["partition"])
    per_partition[key] = {
        "dim": entry["dim"],
        "y_lambda": mp.mpf(entry["y_lambda"]),
        "chi_beta_D": mp.mpf(entry["chi_lambda"]),
    }

# ── Compute μ-degrees + μ-edge-counts per w ∈ S_6 ────────────────
print("Computing W-graph edge weights for S_6...")
print(f"  (this populates the KL cache; expect minutes for full sweep)")

_kl_cache_clear()
perms6 = permutations_S_n(6)
mu_deg: dict[tuple[int, ...], mp.mpf] = {}
mu_edge_count: dict[tuple[int, ...], int] = {}
shape_of: dict[tuple[int, ...], tuple[int, ...]] = {}

import time
t0 = time.time()
for i, w in enumerate(perms6):
    if i % 100 == 0 and i > 0:
        elapsed = time.time() - t0
        print(f"  progress: {i}/720, elapsed {elapsed:.0f}s, "
              f"cache {_kl_cache_size()}")
    shape_of[w] = rsk_shape(w)
    deg_sum = mp.mpf(0)
    edge_count = 0
    lw = length(w)
    if lw == 0:
        mu_deg[w] = deg_sum
        mu_edge_count[w] = edge_count
        continue
    # Only iterate over y < w in Bruhat order with parity-of-length
    # matching the μ definition.
    for y in perms6:
        ly = length(y)
        if lw - ly < 1 or (lw - ly) % 2 == 0:
            continue
        if not bruhat_le(y, w):
            continue
        mu_yw = _mu(y, w)
        if not mu_yw.equals(0):
            deg_sum += abs(mu_yw)
            edge_count += 1
    mu_deg[w] = deg_sum
    mu_edge_count[w] = edge_count

elapsed = time.time() - t0
print(f"  done in {elapsed:.0f}s; cache size = {_kl_cache_size()}")
print()

# ── Aggregate per partition ──────────────────────────────────────
agg_deg = {key: mp.mpf(0) for key in per_partition}
agg_edge = {key: 0 for key in per_partition}
count_by_shape = {key: 0 for key in per_partition}
for w, shape in shape_of.items():
    key = "_".join(str(p) for p in shape)
    if key not in per_partition:
        continue
    agg_deg[key] += mu_deg[w]
    agg_edge[key] += mu_edge_count[w]
    count_by_shape[key] += 1

# Sanity check: count_by_shape[λ] should equal (f^λ)² = number of
# permutations w with shape(w) = λ.
sanity_dim_sq = []
for key, count in count_by_shape.items():
    p = per_partition[key]
    expected = p["dim"] ** 2
    sanity_dim_sq.append({
        "partition": key,
        "f_lam_sq": expected,
        "count_by_RSK_shape": count,
        "diff": count - expected,
    })
sanity_ok = all(s["diff"] == 0 for s in sanity_dim_sq)

# ── Compute three variants ──────────────────────────────────────
S_b1a = mp.mpf(0)
S_b1b = mp.mpf(0)
S_b1c_per_w = mp.mpf(0)  # μ-degree weighted assembly summed over all w directly
per_lambda = []
for key, p in per_partition.items():
    chi = p["chi_beta_D"]
    f_lam = p["dim"]
    y = p["y_lambda"]
    delta_b1a = agg_deg[key] * chi / f_lam if f_lam > 0 else mp.mpf(0)
    delta_b1b = mp.mpf(agg_edge[key]) * chi / f_lam if f_lam > 0 else mp.mpf(0)
    S_b1a += y * chi * delta_b1a
    S_b1b += y * chi * delta_b1b
    per_lambda.append({
        "partition": key,
        "f_lam": f_lam,
        "f_lam_squared": f_lam ** 2,
        "mu_deg_sum_over_cell": str(agg_deg[key]),
        "mu_edge_count_over_cell": agg_edge[key],
        "y_lambda": str(y),
        "chi_beta_D": str(chi),
        "delta_b1a": str(delta_b1a),
        "delta_b1b": str(delta_b1b),
        "contrib_b1a": str(y * chi * delta_b1a),
        "contrib_b1b": str(y * chi * delta_b1b),
    })

# B-1c: direct sum over all w (no shape grouping needed)
for w in perms6:
    shape = shape_of[w]
    key = "_".join(str(p) for p in shape)
    if key not in per_partition:
        continue
    p = per_partition[key]
    # ρ_w(β_D) approximated as χ^λ(β_D) / f^λ
    rho_w = p["chi_beta_D"] / p["dim"]
    S_b1c_per_w += p["y_lambda"] * mu_deg[w] * rho_w

rel_err_b1a = abs(S_b1a - target_signed) / abs(target_signed)
rel_err_b1b = abs(S_b1b - target_signed) / abs(target_signed)
rel_err_b1c = abs(S_b1c_per_w - target_signed) / abs(target_signed)
closes_b1a = rel_err_b1a < mp.mpf("0.10")
closes_b1b = rel_err_b1b < mp.mpf("0.10")
closes_b1c = rel_err_b1c < mp.mpf("0.10")

assertions = [{
    "name": "rsk_shape_count_matches_f_lam_squared",
    "passed": bool(sanity_ok),
    "note": ("|{w ∈ S_n : shape(w) = λ}| = (f^λ)² by RSK.  "
             "Validates the shape function."),
}, {
    "name": "no_step_b1_variant_closes_within_10pct",
    "expected_closes_b1a": False,
    "expected_closes_b1b": False,
    "expected_closes_b1c": False,
    "actual_closes_b1a": bool(closes_b1a),
    "actual_closes_b1b": bool(closes_b1b),
    "actual_closes_b1c": bool(closes_b1c),
    "passed": not (closes_b1a or closes_b1b or closes_b1c),
}]
all_passed = all(a["passed"] for a in assertions)

out = {
    "computation": "option-e-probe4-step-b1-wgraph-weight",
    "auditOnly": True,
    "description": (
        "Option-E PROBE 4 Step B-1: tests W-graph edge-weight "
        "μ(y, w) as the multiplicity n^w_λ in three variants.  "
        "Consumes PR #1714's memoized KL recursion; stacks on top "
        "of #1714 for the recursion availability."
    ),
    "timestamp_utc": datetime.now(timezone.utc).isoformat(),
    "inputs": {
        "chi_deuteron_h6_witness": "chi-deuteron-h6-at-q0-50dps.witness.json",
        "empirical_target_witness": "delta-lambda-empirical-tabulation.witness.json",
    },
    "target_signed": str(target_signed),
    "kl_cache_size_after_sweep": _kl_cache_size(),
    "rsk_shape_sanity": sanity_dim_sq,
    "rsk_shape_count_ok": bool(sanity_ok),
    "variants": {
        "B1a_total_mu_degree": {
            "formula": "Δ_λ = (Σ_{w: shape=λ} μ_deg(w)) · χ^λ(β_D) / f^λ",
            "S_value": str(S_b1a),
            "rel_err": str(rel_err_b1a),
            "closes_within_10pct": bool(closes_b1a),
        },
        "B1b_mu_edge_count": {
            "formula": "Δ_λ = (Σ_{w: shape=λ} |non-zero μ-edges from y < w|) · χ^λ(β_D) / f^λ",
            "S_value": str(S_b1b),
            "rel_err": str(rel_err_b1b),
            "closes_within_10pct": bool(closes_b1b),
        },
        "B1c_per_w_direct": {
            "formula": "S = Σ_{w ∈ S_6} y_{shape(w)} · μ_deg(w) · ρ_w(β_D)  where ρ_w ≈ χ^{shape(w)}/f^{shape(w)}",
            "S_value": str(S_b1c_per_w),
            "rel_err": str(rel_err_b1c),
            "closes_within_10pct": bool(closes_b1c),
        },
    },
    "per_lambda_aggregates": per_lambda,
    "assertions": assertions,
    "allPassed": bool(all_passed),
    "verdict": (
        "All three B-1 variants REFUTED.  W-graph edge-weight μ(y, w) "
        "as multiplicity does not supply the missing Δ_λ structure on "
        "the deuteron.  Adds B-1 to the cumulative Option-E "
        "refutation pile."
        if not (closes_b1a or closes_b1b or closes_b1c) else
        "POSITIVE FINDING — at least one B-1 variant closed within "
        "10%.  W-graph multiplicity supplies the missing structure.  "
        "Escalate to Lean PROBE 3."
    ),
}

out_path = Path(__file__).parent / "probe-option-e-step-b1-wgraph-weight.witness.json"
with open(out_path, "w") as fp:
    json.dump(out, fp, indent=2)

print("=" * 72)
print(" Option-E PROBE 4 Step B-1 — W-graph edge-weight μ(y, w)")
print("=" * 72)
print(f"  target_signed = {float(target_signed):+.6f}")
print(f"  KL cache size after S_6 μ-sweep: {_kl_cache_size()}")
print(f"  RSK shape-count sanity: {sanity_ok}")
print()
print(f"  {'Variant':<24s} {'S':>14s} {'rel_err':>12s} {'closes ≤10%':>14s}")
print(f"  {'B-1a: total μ-degree':<24s} {float(S_b1a):>+14.6f} "
      f"{float(rel_err_b1a)*100:>11.2f}% {str(closes_b1a):>14s}")
print(f"  {'B-1b: μ-edge count':<24s} {float(S_b1b):>+14.6f} "
      f"{float(rel_err_b1b)*100:>11.2f}% {str(closes_b1b):>14s}")
print(f"  {'B-1c: per-w direct':<24s} {float(S_b1c_per_w):>+14.6f} "
      f"{float(rel_err_b1c)*100:>11.2f}% {str(closes_b1c):>14s}")
print()
print("  Per-λ μ-degree and edge-count aggregates:")
print(f"    {'λ':<14s} {'(f^λ)²':>8s} {'μ_deg sum':>12s} {'μ-edges':>10s}")
for c in per_lambda:
    print(f"    {c['partition']:<14s} {c['f_lam_squared']:>8d} "
          f"{float(mp.mpf(c['mu_deg_sum_over_cell'])):>12.4f} "
          f"{c['mu_edge_count_over_cell']:>10d}")
print()
print(f"  Verdict: {out['verdict']}")
print(f"  All assertions passed: {all_passed}")
print(f"  Witness: {out_path}")

if not all_passed:
    sys.exit(1)
