#!/usr/bin/env python3
"""
Option E v4 — canonical q-Reeb phase derivation per cheat sheet.

Per docs/canonical-derivation-cheat-sheet.md line 113 / item 4:
  "Binding carrier = per-rep q-Reeb phase
   θ_λ = arccos(χ^λ/d_λ): Markov-weighted phase closes the A=3
   mirror pair (³H, ³He) to 2%, no fit"

This v4 tests the canonical Δ_λ derivation:

   Δ_λ(K) = θ_λ(K) = arccos(χ^λ(β_K) / d_λ)

with Path-D B_pred = m_e · Σ_λ y_λ χ^λ Δ_λ.

Two variants:
  A. Standard Markov: B = m_e · Σ_λ y_λ χ^λ · θ_λ
  B. Phase-only:     B = m_e · Σ_λ y_λ · θ_λ  (no χ^λ factor — y_λ
                       already encodes Markov weight, and θ_λ IS the
                       binding contribution per the cheat-sheet)

Both for D, T, ³He.

Output:
  option-e-q-reeb-phase-probe-v4.witness.json
"""

import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from mpmath import mpf, mp, acos


M_E_MEV = mpf("0.51099895069")
AME_MeV = {
    "deuteron":  mpf("2.224566"),
    "tritium":   mpf("8.481798"),
    "helium-3":  mpf("7.71806"),
}


def parse_rows(chi_data):
    rows = []
    for entry in chi_data["by_partition"]:
        part = entry["partition"]
        if isinstance(part, str):
            part = eval(part)
        rows.append({
            "partition": part,
            "dim": int(entry["dim"]),
            "y_lambda": mpf(entry["y_lambda"]),
            "chi_lambda": mpf(entry["chi_lambda"]),
            "contribution": mpf(entry["contribution"]),
        })
    return rows


def q_reeb_phase(chi_lambda, d_lambda):
    """θ_λ = arccos(χ^λ / d_λ).

    Clamp argument to [-1, +1] to handle floating-point overshoot from
    the cached 50-dps χ^λ / d_λ ratio at q=q_0.
    """
    ratio = chi_lambda / mpf(d_lambda)
    # Clamp into arccos domain (per-rep phases live in [0, π])
    if ratio > 1:
        ratio = mpf(1)
    elif ratio < -1:
        ratio = mpf(-1)
    return acos(ratio)


def evaluate_variant(name, rows, atom_name, include_chi_factor):
    """B_pred = m_e · Σ_λ y_λ · [χ^λ if include else 1] · θ_λ."""
    s = mpf(0)
    per_lambda = []
    for row in rows:
        theta = q_reeb_phase(row["chi_lambda"], row["dim"])
        if include_chi_factor:
            term = row["y_lambda"] * row["chi_lambda"] * theta
        else:
            term = row["y_lambda"] * theta
        s += term
        per_lambda.append({
            "partition": str(row["partition"]),
            "dim": row["dim"],
            "chi_lambda": str(row["chi_lambda"]),
            "y_lambda": str(row["y_lambda"]),
            "theta_lambda_rad": str(theta),
            "term": str(term),
        })
    B_pred = M_E_MEV * s
    B_target = AME_MeV[atom_name]
    # NOTE: Sign convention. For B(K) > 0 (binding energy is positive),
    # the formula should match +B_target if Markov sums are positive.
    # We test both signs.
    abs_match = abs(B_pred - B_target)
    abs_match_neg = abs(B_pred + B_target)
    rel_err_pos = 100 * abs_match / B_target
    rel_err_neg = 100 * abs_match_neg / B_target

    return {
        "variant": name,
        "atom": atom_name,
        "B_pred_MeV": str(B_pred),
        "B_target_MeV": str(B_target),
        "rel_err_positive_match_pct": str(rel_err_pos),
        "rel_err_negative_match_pct": str(rel_err_neg),
        "closes_within_2pct_positive": bool(abs_match <= mpf("0.02") * B_target),
        "closes_within_10pct_positive": bool(abs_match <= mpf("0.10") * B_target),
        "closes_within_2pct_negative": bool(abs_match_neg <= mpf("0.02") * B_target),
        "closes_within_10pct_negative": bool(abs_match_neg <= mpf("0.10") * B_target),
        "per_lambda_terms": per_lambda[:5],  # truncate display
    }


def main() -> int:
    mp.dps = 50
    repo_root = Path(__file__).resolve().parent.parent.parent

    files = {
        "deuteron": "chi-deuteron-h6-at-q0-50dps.witness.json",
        "tritium":  "chi-tritium-h9-at-q0-50dps.witness.json",
        "helium-3": "chi-helium-3-h9-at-q0-50dps.witness.json",
    }

    atom_rows = {}
    for atom, fn in files.items():
        with (repo_root / "folio-assistant" / "computations" / fn).open() as f:
            atom_rows[atom] = parse_rows(json.load(f))

    results = {"variant_A_with_chi": {}, "variant_B_phase_only": {}}
    for atom in ["deuteron", "tritium", "helium-3"]:
        rows = atom_rows[atom]
        results["variant_A_with_chi"][atom] = evaluate_variant(
            "Markov + χ + θ_λ", rows, atom, include_chi_factor=True
        )
        results["variant_B_phase_only"][atom] = evaluate_variant(
            "y_λ + θ_λ (no χ)", rows, atom, include_chi_factor=False
        )

    witness = {
        "engine": "python",
        "engineVersion": f"python {sys.version_info.major}.{sys.version_info.minor}",
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "computation": "option-e-q-reeb-phase-probe-v4",
        "description": (
            "Option E v4: canonical q-Reeb phase Δ_λ = arccos(χ^λ/d_λ) "
            "per docs/canonical-derivation-cheat-sheet.md item 4 (A≥3 "
            "binding campaign, PR #1417). Tests on D, T, ³He."
        ),
        "scriptFile": "option_e_q_reeb_phase_probe_v4.py",
        "precisionMetadata": {"compute_dps": 50, "output_dps": 30},
        "rule": "Δ_λ(K) = θ_λ(K) = arccos(χ^λ(β_K) / d_λ)",
        "reference": (
            "docs/canonical-derivation-cheat-sheet.md §'Bind' row + "
            "A≥3 binding campaign summary item 4"
        ),
        "variants_tested": [
            "variant_A_with_chi: B = m_e · Σ y_λ χ^λ θ_λ (Markov standard)",
            "variant_B_phase_only: B = m_e · Σ y_λ θ_λ (phase-only)"
        ],
        "results": results,
    }

    # Find best variant + atom across both variants & both signs
    summary = []
    for variant_key in ["variant_A_with_chi", "variant_B_phase_only"]:
        for atom in ["deuteron", "tritium", "helium-3"]:
            r = results[variant_key][atom]
            err_pos = float(r["rel_err_positive_match_pct"])
            err_neg = float(r["rel_err_negative_match_pct"])
            best_err = min(err_pos, err_neg)
            sign = "+" if err_pos < err_neg else "-"
            summary.append((variant_key, atom, sign, best_err))

    witness["summary"] = [
        {"variant": v, "atom": a, "sign_match": s, "rel_err_pct": str(e)}
        for v, a, s, e in summary
    ]

    out = (
        repo_root / "folio-assistant" / "computations"
        / "option-e-q-reeb-phase-probe-v4.witness.json"
    )
    with out.open("w") as f:
        json.dump(witness, f, indent=2)

    print(f"Wrote {out}\n")
    print("=== q-Reeb phase Δ_λ = arccos(χ^λ/d_λ) ===\n")
    for variant_key in ["variant_A_with_chi", "variant_B_phase_only"]:
        print(f"--- {variant_key} ---")
        for atom in ["deuteron", "tritium", "helium-3"]:
            r = results[variant_key][atom]
            print(f"  {atom:10s}  B_pred={float(r['B_pred_MeV']):+9.5f} MeV  "
                  f"target={float(r['B_target_MeV']):+9.5f}  "
                  f"err+={float(r['rel_err_positive_match_pct']):6.2f}%  "
                  f"err-={float(r['rel_err_negative_match_pct']):6.2f}%")
        print()

    print("=== Summary (best sign per atom × variant) ===")
    for v, a, s, e in summary:
        marker = "  ✓" if e <= 10.0 else "  ✓✓" if e <= 2.0 else "   "
        print(f"{marker} {v:25s} {a:10s} sign={s}  err={e:6.2f}%")

    closes_any_2pct = any(e <= 2.0 for v, a, s, e in summary)
    closes_any_10pct = any(e <= 10.0 for v, a, s, e in summary)
    print(f"\nAny 2% closure: {closes_any_2pct}")
    print(f"Any 10% closure: {closes_any_10pct}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
