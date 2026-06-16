#!/usr/bin/env python3
# polynomial_q_not_applicable: EXPLORATORY probe per
#   `production-vs-exploratory-discipline`. Tests cheap crystal-vertex
#   weight candidates as Δ_λ closure factors for the deuteron binding
#   energy. Reads canonical witness data ONLY (no fit, no parameter
#   tuning).  Asserts expected-negative magnitudes when candidates are
#   refuted, so CI stays green on a clean refutation.
"""
Option-E Phase 2 PROBE 4 (cheap pass) — crystal-vertex weight
candidates for Δ_λ closure at the deuteron (H_6, A=2).

# Ref: docs/audits/2026-05-25-option-e-crystal-weight-delta-lambda.md
# Ref: docs/coordination/option-e.md (master ledger, PROBE 4)
# Ref: docs/audits/2026-05-31-rho-w-crystal-vertex-trace-design.md
# Ref: PR #1697 (H_6 Hoefsmit-seminormal Gram landed; provides χ_λ(w_0))
# Ref: PR #1709 (volume-Wedderburn refutation; analogous "cheap proxy
#                first" strategy)

## Upstream: `rho_w_crystal_vertex_trace.py` (already on main)

`computations/rho_w_crystal_vertex_trace.py` (landed
on main before this branch) implements the genuine per-vertex
ρ_w := ⟨v_T|ρ_λ(β_K)|v_T⟩ from the Hoefsmit/Young seminormal
representation, then computes `Δ_λ^{ρ_w}(K) = Σ_w n^w_λ · ρ_w(K)`
with `n^w_λ = 1` (regular multiplicity).  By the trace-as-diagonal-
sum identity, this collapses to the Hecke character χ^λ(β_K) which
is already on disk — the regular-multiplicity sum does NOT close
the deuteron (`closure_status: does_not_close`).

## What this probe adds (orthogonal scope)

This probe does NOT recompute the forced identity that
`rho_w_crystal_vertex_trace.py` already established.  Instead it
tests four **ad-hoc closed-form candidates** for `Δ_λ` that are
NOT the regular-multiplicity sum:

The Option-E binding-energy formula is
    B(K) = m_e · Σ_λ y_λ(q_0) · χ^λ(β_K) · Δ_λ
With `n^w_λ = 1` and ρ_w summed, this reduces to χ^λ(β_K) and gives
tr_M (i.e. the existing rho_w_crystal_vertex_trace.py result, no
closure).  The full Kashiwara/KL ansatz proposes

    Δ_λ = Σ_w n^w_λ · ρ_w(K)

with non-trivial n^w_λ (Kazhdan-Lusztig multiplicities) and
non-trivial single-vertex selection.  Full KL machinery for S_6 is
not scaffolded (`kazhdan_lusztig.py` caps at n ≤ 4).  Following PR
#1709's "cheap proxy first" strategy, this probe tests four
single-vertex / closed-form candidates for Δ_λ at H_6 / deuteron,
using existing witness data:

| Candidate | Δ_λ formula |
|-----------|-------------|
| **A** (longest-word character) | χ^λ(w_0) [from #1697 Gram witness] |
| **B** (longest-word abs)        | \\|χ^λ(w_0)\\| |
| **C** (sign × dim)              | sgn(χ^λ(w_0)) · dim_λ |
| **D** (peak weight)             | max-abs diagonal of ρ_λ(w_0) |

For each candidate, this probe computes
    S_X := Σ_λ y_λ(q_0) · χ^λ(β_D) · Δ_λ(X)
and compares to the empirical target
    target_signed = (B_AME / m_e) · sign
                  = -4.35337
                    (per `delta-lambda-empirical-tabulation.witness.json`).

### Refutation criterion (analog of #1709)

A candidate X is REFUTED if |S_X - target_signed| / |target_signed|
≥ 0.10 (10%).  ALL four candidates being refuted is a CLEAN NEGATIVE
result — it says the per-block crystal-vertex weight at w_0 (or its
closed-form variants) cannot supply Δ_λ closure, and that PROBE 4's
positive direction requires the FULL Kazhdan-Lusztig multiplicity
machinery n^w_λ across multiple vertices w, not a single-vertex
shortcut.  This mirrors #1709's outcome: content/hook-angle Vol_λ
proxies refuted → q-6j saddle isolated as the remaining live
direction.

### Asserts

This probe asserts the refutation magnitudes (expected-negative
shape): if any candidate accidentally closes to within 10% of target,
the assertion fails and we have a POSITIVE finding to escalate.
Otherwise CI stays green.

## Usage

    cd computations
    python3 probe_option_e_phase2_crystal_vertex_candidates.py

Emits: probe-option-e-phase2-crystal-vertex-candidates.witness.json
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
gram_w = load_witness("option-e-phase1-gram-h6.witness.json")
chi_w = load_witness("chi-deuteron-h6-at-q0-50dps.witness.json")
empirical_w = load_witness("delta-lambda-empirical-tabulation.witness.json")

target_signed = mp.mpf(empirical_w["data"]["per_atom"]["D"]["target_signed"])
tr_M_D = mp.mpf(chi_w["tr_M_at_q0"])

# Build per-partition records: y_λ, χ^λ(β_D) at q_0
# chi_w stores `by_partition` as a list with partition encoded as list[int]
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

# Augment with χ^λ(w_0) + ρ_λ(w_0) diagonal max-abs from #1697
for key, h6_block in gram_w["data"]["h6"]["blocks"].items():
    if key not in per_partition:
        raise SystemExit(f"missing partition {key} in chi-deuteron witness")
    chi_w0 = mp.mpf(repr(h6_block["chi_lambda_w0_direct"]))
    w0_diag = [mp.mpf(repr(h6_block["w0_matrix_at_q0_re"][i][i]))
               for i in range(h6_block["dim"])]
    max_abs_diag = max(abs(d) for d in w0_diag)
    per_partition[key]["chi_lambda_w0"] = chi_w0
    per_partition[key]["max_abs_w0_diag"] = max_abs_diag

# ── Sanity: re-sum tr_M from per-partition y·χ ────────────────────
tr_M_resum = mp.mpf(0)
for p in per_partition.values():
    tr_M_resum += p["y_lambda"] * p["chi_beta_D"]
sanity_tr_M_diff = abs(tr_M_resum - tr_M_D)

# ── Candidate Δ_λ rules ───────────────────────────────────────────
def signum(x: mp.mpf) -> int:
    if x > 0:
        return 1
    if x < 0:
        return -1
    return 0

candidates = {
    "A_longest_word_char": (
        lambda p: p["chi_lambda_w0"],
        "Δ_λ = χ^λ(w_0): character at longest word (#1697 direct)",
    ),
    "B_longest_word_abs": (
        lambda p: abs(p["chi_lambda_w0"]),
        "Δ_λ = |χ^λ(w_0)|: magnitude of longest-word character",
    ),
    "C_sign_times_dim": (
        lambda p: signum(p["chi_lambda_w0"]) * mp.mpf(p["dim"]),
        "Δ_λ = sgn(χ^λ(w_0)) · dim_λ: sign carried by trivial-equiv "
        "channel, magnitude by SYT count",
    ),
    "D_peak_w0_diag": (
        lambda p: p["max_abs_w0_diag"],
        "Δ_λ = max_i |ρ_λ(w_0)_{ii}|: peak weight in the Hoefsmit-"
        "seminormal w_0 diagonal",
    ),
}

results = {}
for name, (rule, desc) in candidates.items():
    s = mp.mpf(0)
    contribs = []
    for key, p in per_partition.items():
        delta = rule(p)
        c = p["y_lambda"] * p["chi_beta_D"] * delta
        s += c
        contribs.append({
            "partition": key,
            "y_lambda": str(p["y_lambda"]),
            "chi_beta_D": str(p["chi_beta_D"]),
            "delta_candidate": str(delta),
            "contribution": str(c),
        })
    rel_err = abs(s - target_signed) / abs(target_signed)
    closes = (rel_err < mp.mpf("0.10"))
    results[name] = {
        "description": desc,
        "S_candidate": str(s),
        "rel_err_vs_target": str(rel_err),
        "closes_within_10pct": bool(closes),
        "contributions": contribs,
    }

# ── Refutation assertion (expected-negative shape) ────────────────
any_closes = any(r["closes_within_10pct"] for r in results.values())
assertions = [{
    "name": "no_single_vertex_candidate_closes_within_10pct",
    "expected_closes": False,
    "actual_closes": bool(any_closes),
    "passed": not any_closes,
    "note": (
        "Negative-shape assertion: all four cheap candidates miss the "
        "deuteron target by ≥ 10%. If this assertion FAILS, one of the "
        "candidates accidentally closed and we have a POSITIVE finding "
        "to escalate."
    ),
}]
all_passed = all(a["passed"] for a in assertions)

out = {
    "computation": "option-e-phase2-crystal-vertex-candidates",
    "auditOnly": True,
    "description": (
        "Option-E PROBE 4 cheap pass: tests four crystal-vertex-weight "
        "candidate rules for Δ_λ at H_6 / deuteron against the empirical "
        "target. Reads canonical witness data only. NOT a fit. Asserts "
        "refutation (expected-negative)."
    ),
    "timestamp_utc": datetime.now(timezone.utc).isoformat(),
    "inputs": {
        "h6_gram_witness": "option-e-phase1-gram-h6.witness.json",
        "chi_deuteron_h6_witness": "chi-deuteron-h6-at-q0-50dps.witness.json",
        "empirical_target_witness": "delta-lambda-empirical-tabulation.witness.json",
    },
    "target_signed": str(target_signed),
    "tr_M_D_at_q0": str(tr_M_D),
    "sanity_checks": {
        "tr_M_resum_from_per_partition": str(tr_M_resum),
        "tr_M_resum_diff": str(sanity_tr_M_diff),
        "resum_consistent_to_1e_30": bool(sanity_tr_M_diff < mp.mpf("1e-30")),
    },
    "candidates": results,
    "assertions": assertions,
    "allPassed": bool(all_passed),
    "verdict": (
        "ALL FOUR cheap candidates REFUTED (consistent with both PR "
        "#1709's volume-Wedderburn refutation AND the upstream "
        "rho_w_crystal_vertex_trace.py result on main — regular-"
        "multiplicity Σ_w ρ_w = χ^λ does not close; four ad-hoc "
        "closed-form variants also do not close). Remaining live "
        "in-Option-E direction: full Kazhdan-Lusztig multiplicity "
        "machinery n^w_λ (non-trivial KL multiplicities, not n^w_λ = 1) "
        "summed across multiple vertices w — requires extending "
        "kazhdan_lusztig.py past its n ≤ 4 cap to S_6. Otherwise: "
        "pivot to GAP-A-3/A-4 per CLAUDE.md §L2."
        if not any_closes else
        "POSITIVE FINDING — one or more candidates closed within 10%. "
        "Escalate: refine the candidate rule, then attempt the full "
        "Σ_w n^w_λ ρ_w(D) sum to see if the leading term carries the "
        "structure."
    ),
    "upstream_reference": (
        "rho_w_crystal_vertex_trace.py (on main, design doc "
        "docs/audits/2026-05-31-rho-w-crystal-vertex-trace-design.md) "
        "implements the genuine per-vertex ρ_w from Hoefsmit/Young "
        "seminormal at first principles; its regular-multiplicity sum "
        "Σ_w ρ_w(K) collapses to χ^λ(β_K) by trace identity and is "
        "shown not to close. This probe complements that work by "
        "testing four ad-hoc closed-form variants that ARE NOT "
        "Σ_w ρ_w; results refute the closed-form direction as well."
    ),
}

out_path = Path(__file__).parent / "probe-option-e-phase2-crystal-vertex-candidates.witness.json"
with open(out_path, "w") as fp:
    json.dump(out, fp, indent=2)

print("=" * 72)
print(" Option-E PROBE 4 (cheap pass) — crystal-vertex candidates @ H_6")
print("=" * 72)
print(f"  target_signed = {float(target_signed):+.6f}")
print(f"  tr_M(β_D) at q_0 = {float(tr_M_D):.6f}  (resum diff "
      f"{float(sanity_tr_M_diff):.2e})")
print()
print(f"  {'Candidate':<24s} {'S_candidate':>18s} {'rel_err':>12s} "
      f"{'closes ≤10%':>14s}")
for name, r in results.items():
    print(f"  {name:<24s} {float(mp.mpf(r['S_candidate'])):>+18.6f} "
          f"{float(mp.mpf(r['rel_err_vs_target']))*100:>11.2f}% "
          f"{str(r['closes_within_10pct']):>14s}")
print()
print(f"  Verdict: {out['verdict']}")
print()
print(f"  All assertions passed: {all_passed}")
print(f"  Witness: {out_path}")

if not all_passed:
    sys.exit(1)
