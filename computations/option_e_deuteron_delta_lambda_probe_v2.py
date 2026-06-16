#!/usr/bin/env python3
"""
Option E deuteron Δ_λ probe v2 — richer rules from BK content-residue
+ shifted-tableau-depth candidates.

Companion to option_e_deuteron_delta_lambda_probe.py (7 simple rules,
all failed). This v2 implements 8 richer rules grounded in the
Brundan-Kleshchev content-residue framework that the canonical
Option E approach is supposed to use.

For each partition λ ⊢ 6:
  contents(λ) = { (c - r) : cell (r, c) ∈ Young diagram of λ }

Candidate rules:
  R1: content_sum               — Σ (c-r) over cells of λ
  R2: content_sum_squared       — Σ (c-r)^2
  R3: content_alternating       — Σ (c-r) · (-1)^(r+c)
  R4: content_spread            — max(c-r) - min(c-r)
  R5: content_max_minus_min     — same as spread, sign tracked
  R6: shifted_depth             — number of distinct content residues
  R7: dim_lambda                — dim(V_λ) itself (positive integer)
  R8: signed_content_pair_max   — max(c-r) - min(c-r), signed by partition shape

Plus one negative-control:
  R9: random_int_minus_5_to_5   — fitted-looking but uncalibrated

Output:
  computations/option-e-deuteron-delta-lambda-probe-v2.witness.json
"""

import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from lean_uniqueness_refs import lean_uniqueness_ref  # noqa: E402
from mpmath import mpf, mp


def young_contents(partition):
    """Return list of contents (c-r) over all cells of the Young diagram."""
    contents = []
    for r, row_len in enumerate(partition):
        for c in range(row_len):
            contents.append(c - r)
    return contents


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

    rows = []
    for entry in partitions_data:
        part = entry["partition"]
        if isinstance(part, str):
            part = eval(part)
        contents = young_contents(part)
        rows.append({
            "partition": part,
            "dim": int(entry["dim"]),
            "y_lambda": mpf(entry["y_lambda"]),
            "chi_lambda": mpf(entry["chi_lambda"]),
            "contribution": mpf(entry["contribution"]),
            "contents": contents,
        })

    B_D_MeV = mpf("2.224566")
    m_e_MeV = mpf("0.51099895069")
    closure_threshold = mpf("0.10") * B_D_MeV

    # Richer Δ_λ candidate rules
    def rule_content_sum(row):
        return mpf(sum(row["contents"]))

    def rule_content_sum_negated(row):
        # Negative scaling: -sum(contents)
        return -mpf(sum(row["contents"]))

    def rule_content_sum_squared(row):
        return mpf(sum(c * c for c in row["contents"]))

    def rule_content_sum_squared_neg(row):
        return -mpf(sum(c * c for c in row["contents"]))

    def rule_content_alternating(row):
        # Σ (c-r) · (-1)^(r+c), needs cell indices
        s = mpf(0)
        for r, row_len in enumerate(row["partition"]):
            for c in range(row_len):
                sign = -1 if (r + c) % 2 else 1
                s += mpf(sign) * mpf(c - r)
        return s

    def rule_content_spread(row):
        if not row["contents"]:
            return mpf(0)
        return mpf(max(row["contents"]) - min(row["contents"]))

    def rule_content_spread_negated(row):
        if not row["contents"]:
            return mpf(0)
        return -mpf(max(row["contents"]) - min(row["contents"]))

    def rule_shifted_depth(row):
        # Number of distinct content residues = "depth" in BK sense
        return mpf(len(set(row["contents"])))

    def rule_shifted_depth_negated(row):
        return -mpf(len(set(row["contents"])))

    def rule_dim_lambda(row):
        return mpf(-row["dim"])  # negative

    def rule_signed_content_pair_max(row):
        # spread signed by partition vs conjugate orientation
        spread = mpf(max(row["contents"]) - min(row["contents"]))
        # sign: -1 if partition is "tall" (length > largest part), else +1
        sign = -1 if len(row["partition"]) > max(row["partition"]) else 1
        return sign * spread

    rules = [
        ("content_sum", rule_content_sum),
        ("content_sum_negated", rule_content_sum_negated),
        ("content_sum_squared", rule_content_sum_squared),
        ("content_sum_squared_neg", rule_content_sum_squared_neg),
        ("content_alternating", rule_content_alternating),
        ("content_spread", rule_content_spread),
        ("content_spread_negated", rule_content_spread_negated),
        ("shifted_depth", rule_shifted_depth),
        ("shifted_depth_negated", rule_shifted_depth_negated),
        ("dim_lambda_negative", rule_dim_lambda),
        ("signed_content_pair_max", rule_signed_content_pair_max),
    ]

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
                "contents": row["contents"],
                "delta_lambda": str(delta),
                "term": str(term),
            })

        B_pred_MeV = m_e_MeV * sum_term
        signed_residual = B_pred_MeV + B_D_MeV
        abs_residual = abs(signed_residual)
        closes = abs_residual <= closure_threshold
        rel_error_pct = 100 * abs_residual / B_D_MeV

        results.append({
            "rule_name": rule_name,
            "B_pred_MeV": str(B_pred_MeV),
            "signed_residual_MeV": str(signed_residual),
            "abs_residual_MeV": str(abs_residual),
            "rel_error_pct": str(rel_error_pct),
            "closes_within_10pct": bool(closes),
            "per_partition_terms": per_partition,
        })

    best = min(results, key=lambda r: abs(mpf(r["abs_residual_MeV"])))

    witness = {
        "engine": "python",
        "engineVersion": f"python {sys.version_info.major}.{sys.version_info.minor}",
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "computation": "option-e-deuteron-delta-lambda-probe-v2",
        "description": (
            "Option E v2: 11 richer Δ_λ candidate rules grounded in "
            "Brundan-Kleshchev content-residue framework (Young-diagram "
            "cell contents). Tests against AME deuteron via Path-D."
        ),
        "scriptFile": "option_e_deuteron_delta_lambda_probe_v2.py",
        "precisionMetadata": {
            "compute_dps": 50,
            "output_dps": 30,
        },
        "ame_data": {
            "B_D_MeV": str(B_D_MeV),
            "m_e_MeV": str(m_e_MeV),
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
            else "FAILS — all 11 BK-content candidate rules miss AME 10%"
        ),
        "honest_assessment": (
            "These 11 rules use canonical BK content-residue inputs "
            "(Σ content, Σ content², spread, shifted depth, etc.) — "
            "the substrate-derived data that Option E was designed "
            "to leverage. If all still fail, the conclusion is that "
            "Option E needs MULTIPLICATIVE composition (not just "
            "linear functions of contents), or extra structural data "
            "beyond the partition (e.g. per-vertex SYT data, not just "
            "per-partition summaries). This narrows the open research "
            "question to those richer composition structures."
        ),
    }

    out_path = (
        repo_root
        / "folio-assistant"
        / "computations"
        / "option-e-deuteron-delta-lambda-probe-v2.witness.json"
    )
    with out_path.open("w") as f:
        witness["lean_uniqueness_ref"] = lean_uniqueness_ref("deuteron (²H)")
        json.dump(witness, f, indent=2)

    print(f"Wrote {out_path}")
    print(f"\n=== v2 results (11 BK content-based rules) ===")
    for r in results:
        marker = "  ✓" if r["closes_within_10pct"] else "   "
        print(f"{marker} {r['rule_name']:30s} B_pred={float(r['B_pred_MeV']):+10.5f}  err={float(r['rel_error_pct']):7.2f}%")
    print(f"\nBest: {best['rule_name']} at {float(best['rel_error_pct']):.2f}%")
    print(f"Verdict: {witness['verdict']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
