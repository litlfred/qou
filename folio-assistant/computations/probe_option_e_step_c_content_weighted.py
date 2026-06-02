#!/usr/bin/env python3
# polynomial_q_not_applicable: EXPLORATORY measure-level pivot per
#   triage finding (sibling commits d7c56c17e1 / 5e388f598b on main):
#   y_λ is the WRONG outer assembly weight for binding at A≥3;
#   |content_λ| is the best of 6 candidates tested (5% A-growth
#   error).  This probe tests several content-weighted reformulations
#   of the Step-A/B assembly on the deuteron.  Reads canonical
#   witness data only.  Asserts the expected-negative or escalation
#   shape based on outcome.
"""
Option-E Phase 2 PROBE 4 — Step C: measure-level pivot to
|content_λ|.

# Ref: docs/audits/2026-06-02-option-e-probe4-closure-deuteron-design.md
# Ref: docs/audits/2026-06-02-binding-measure-search.md (sibling main commit)
# Ref: docs/audits/2026-06-02-full-theta-binding-probe.md (sibling main commit)
# Ref: probe_option_e_step_a_kl_cell_collapse.py (Step A)
# Ref: probe_option_e_step_b1_wgraph_weight.py (Step B-1)
# Ref: probe_option_e_step_b2_quantum_dim_weighted.py (Step B-2)

## What this Step does

The triage of 4 sibling main commits identified a critical
diagnosis: **`y_λ` is the wrong outer weight for binding at A≥3**.
The Wenzl/Markov measure suppresses the growth channels where
extensive binding lives.  The leading parameter-free replacement
(per d7c56c17e1) is `|content_λ|` — sum of |content| over Young
diagram cells, where content(i, j) = j − i.

This probe tests four content-weighted reformulations and
compares to the empirical target_signed = −4.353:

  **C-1** (content replaces y_λ in v2 = Step-A trivial collapse):
    S = Σ_λ |content_λ| · (χ^λ(β_D))²

  **C-2** (content replaces y_λ in v1 = Step-A whole-cell):
    S = Σ_λ |content_λ| · f^λ · (χ^λ(β_D))²

  **C-3** (content joins y_λ, multiplicative):
    S = Σ_λ |content_λ| · y_λ · (χ^λ(β_D))²

  **C-4** (content directly carries Δ, no χ-squared):
    S = Σ_λ y_λ · χ^λ(β_D) · |content_λ|

If any close (rel_err ≤ 10 %), that's the measure-level closure
candidate — escalate to Lean PROBE 3.  If all refute, the case
that Option-E is structurally exhausted (across both
multiplicity Δ_λ and outer measure) gets stronger.

## Usage

    cd folio-assistant/computations
    python3 probe_option_e_step_c_content_weighted.py

Emits: probe-option-e-step-c-content-weighted.witness.json
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


def abs_content(part: list[int]) -> int:
    """|content_λ| = Σ_{(i,j) ∈ λ} |j − i| (0-indexed).

    Sum of absolute distance from the main diagonal across all
    cells of the Young diagram.  At λ = (n) (single row) this is
    0+1+…+(n−1) = n(n−1)/2; same for the conjugate column.
    Self-conjugate partitions like (3,2,1) have a smaller value
    (more cells near the diagonal).
    """
    total = 0
    for i, lam_i in enumerate(part):
        for j in range(lam_i):
            total += abs(j - i)
    return total


def signed_content_sum(part: list[int]) -> int:
    """Σ_{(i,j) ∈ λ} (j − i).  Zero on self-conjugate; positive on
    row-heavy partitions; negative on column-heavy.  Provided as a
    sanity / structural complement to |content_λ|."""
    total = 0
    for i, lam_i in enumerate(part):
        for j in range(lam_i):
            total += (j - i)
    return total


# ── Inputs ────────────────────────────────────────────────────────
chi_w = load_witness("chi-deuteron-h6-at-q0-50dps.witness.json")
empirical_w = load_witness("delta-lambda-empirical-tabulation.witness.json")
target_signed = mp.mpf(empirical_w["data"]["per_atom"]["D"]["target_signed"])
q_0 = mp.mpf(chi_w["q_0_50dps"])

per_partition = {}
for entry in chi_w["by_partition"]:
    key = "_".join(str(p) for p in entry["partition"])
    per_partition[key] = {
        "partition": entry["partition"],
        "dim": entry["dim"],
        "y_lambda": mp.mpf(entry["y_lambda"]),
        "chi_beta_D": mp.mpf(entry["chi_lambda"]),
        "abs_content": abs_content(entry["partition"]),
        "signed_content_sum": signed_content_sum(entry["partition"]),
    }

# Sanity: Σ |content_λ| · dim_λ across partitions should match a
# known integer (Frobenius-Knuth identity Σ_λ f^λ · n(λ) = ...
# but we just record the values for documentation).
content_summary = []
for key, p in per_partition.items():
    content_summary.append({
        "partition": key,
        "dim": p["dim"],
        "abs_content": p["abs_content"],
        "signed_content_sum": p["signed_content_sum"],
    })

# ── Compute variants ──────────────────────────────────────────────
def assemble(weight_fn, delta_fn) -> mp.mpf:
    """Σ_λ weight(λ) · χ^λ(β_D) · delta(λ)."""
    s = mp.mpf(0)
    for p in per_partition.values():
        s += mp.mpf(weight_fn(p)) * p["chi_beta_D"] * mp.mpf(delta_fn(p))
    return s


variants = {
    "C1_abs_content_x_chi_sq": {
        "formula": "Δ_λ = χ^λ(β_D), weight = |content_λ|",
        "S_value_func": lambda: assemble(
            lambda p: p["abs_content"], lambda p: p["chi_beta_D"]
        ),
    },
    "C2_abs_content_x_f_lam_x_chi_sq": {
        "formula": "Δ_λ = f^λ · χ^λ(β_D), weight = |content_λ|",
        "S_value_func": lambda: assemble(
            lambda p: p["abs_content"],
            lambda p: p["dim"] * p["chi_beta_D"],
        ),
    },
    "C3_abs_content_x_y_lambda_x_chi_sq": {
        "formula": "Δ_λ = χ^λ(β_D), weight = |content_λ| · y_λ",
        "S_value_func": lambda: assemble(
            lambda p: p["abs_content"] * float(p["y_lambda"]),
            lambda p: p["chi_beta_D"],
        ),
    },
    "C4_y_lambda_x_abs_content_alone": {
        "formula": "Δ_λ = |content_λ|, weight = y_λ",
        "S_value_func": lambda: assemble(
            lambda p: p["y_lambda"], lambda p: p["abs_content"]
        ),
    },
    "C5_signed_content_x_chi_sq": {
        "formula": "Δ_λ = χ^λ(β_D), weight = signed Σ content_λ "
                   "(zero on self-conjugate)",
        "S_value_func": lambda: assemble(
            lambda p: p["signed_content_sum"], lambda p: p["chi_beta_D"]
        ),
    },
}

results = {}
any_closes = False
best_variant = None
best_rel_err = mp.mpf("inf")
for name, v in variants.items():
    s = v["S_value_func"]()
    rel_err = abs(s - target_signed) / abs(target_signed)
    closes = rel_err < mp.mpf("0.10")
    if rel_err < best_rel_err:
        best_rel_err = rel_err
        best_variant = name
    if closes:
        any_closes = True
    results[name] = {
        "formula": v["formula"],
        "S_value": str(s),
        "rel_err": str(rel_err),
        "closes_within_10pct": bool(closes),
    }

assertions = [{
    "name": "step_c_content_pivot_outcome",
    "any_variant_closes": bool(any_closes),
    "best_variant": best_variant,
    "best_rel_err": str(best_rel_err),
    "passed": True,  # informational; no expected outcome
    "note": (
        "Step C is a pivot probe: either it closes (positive measure-"
        "level finding — escalate) or it refutes (cumulative "
        "evidence Option-E exhausted at standard framework).  "
        "Both outcomes are informative; we don't assert an expected "
        "direction here."
    ),
}]
all_passed = all(a["passed"] for a in assertions)

verdict = (
    "POSITIVE — at least one Step-C variant closed within 10% of "
    "target.  Measure-level pivot to |content_λ| supplies the "
    "missing structure.  Escalate to Lean PROBE 3 conditional "
    "formalisation; cross-link sibling main commit d7c56c17e1."
    if any_closes else
    "REFUTED — no Step-C variant closes within 10%.  Best is "
    f"`{best_variant}` at {float(best_rel_err)*100:.2f}% miss.  "
    "Combined with cumulative refutation pile (Step A, B-1, B-2, "
    "sibling y_λ-Reeb refutations), Option-E is structurally "
    "exhausted on the deuteron within the standard framework; "
    "pivot to GAP-A-3/A-4 per CLAUDE.md §L2."
)

out = {
    "computation": "option-e-probe4-step-c-content-weighted",
    "auditOnly": True,
    "description": (
        "Option-E PROBE 4 Step C: measure-level pivot from y_λ to "
        "|content_λ| per sibling-commit triage finding "
        "(d7c56c17e1, 5e388f598b on main).  Tests 5 reformulations.  "
        "Reads canonical witness data only.  No expected-outcome "
        "assertion (pivot probe)."
    ),
    "timestamp_utc": datetime.now(timezone.utc).isoformat(),
    "inputs": {
        "chi_deuteron_h6_witness": "chi-deuteron-h6-at-q0-50dps.witness.json",
        "empirical_target_witness": "delta-lambda-empirical-tabulation.witness.json",
    },
    "target_signed": str(target_signed),
    "q_0_at_50dps": chi_w["q_0_50dps"],
    "content_per_partition": content_summary,
    "variants": results,
    "best_variant": best_variant,
    "best_rel_err": str(best_rel_err),
    "any_variant_closes": bool(any_closes),
    "assertions": assertions,
    "allPassed": bool(all_passed),
    "verdict": verdict,
    "sibling_coord_refs": [
        "d7c56c17e1 (main): probe(Δ_λ): binding measure search",
        "5e388f598b (main): full-order θ_λ — y_λ wrong measure",
        "d59bcb79de (main): θ_λ per-λ carry",
        "ba7af156cb (main): per-block θ_λ — absolute open",
    ],
}

out_path = Path(__file__).parent / "probe-option-e-step-c-content-weighted.witness.json"
with open(out_path, "w") as fp:
    json.dump(out, fp, indent=2)

print("=" * 72)
print(" Option-E PROBE 4 Step C — content-weighted pivot")
print("=" * 72)
print(f"  target_signed = {float(target_signed):+.6f}")
print()
print(f"  Per-λ |content_λ|:")
for c in content_summary:
    print(f"    {c['partition']:<14s} f^λ={c['dim']:>3d}  "
          f"|content|={c['abs_content']:>4d}  "
          f"signed_sum={c['signed_content_sum']:>+4d}")
print()
print(f"  {'Variant':<42s} {'S':>14s} {'rel_err':>10s} {'closes':>8s}")
for name, r in results.items():
    print(f"  {name:<42s} {float(mp.mpf(r['S_value'])):>+14.6f} "
          f"{float(mp.mpf(r['rel_err']))*100:>9.2f}% "
          f"{str(r['closes_within_10pct']):>8s}")
print()
print(f"  Best: {best_variant} @ {float(best_rel_err)*100:.2f}% miss")
print()
print(f"  Verdict: {verdict}")
print(f"  Witness: {out_path}")
