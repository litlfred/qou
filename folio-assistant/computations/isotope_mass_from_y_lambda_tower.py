#!/usr/bin/env python3
"""Apply the H_4-H_6 α/y tower to isotope mass predictions.

Goal: connect the structural derivations (closed-form r_λ at H_4,
adaptive-gauge α_λ at H_5/H_6) back to the original mass-prediction
goal. NO fitting.

Strategy:
- Use the gauge-independent Jones-Markov weights y_λ (from witness).
- Use the depth-stratified Φ_k(β) values per isotope (existing
  hoefsmit witness; Φ_k = Σ_{depth(λ)=k} y_λ · log|χ_λ(β)|).
- Predict binding energy via:
    B_pred(β) = m_e · Σ_k Φ_k(β)
  (zero-parameter, summing all depth strata uniformly).
- Compare to AME 2020.

This is a "0-parameter" structural baseline. No α_k coefficients, no
gauge ambiguity.
"""
from __future__ import annotations
import json, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q as Q0_FLOAT

# AME 2020 binding energies
AME = {
    "D":   ( 1, 1,  1876.12393,    2.22456612),
    "T":   ( 1, 2,  2809.43215,    8.481798),
    "3He": ( 2, 1,  2809.41347,    7.718058),
    "4He": ( 2, 2,  3728.40133,   28.29566),
    "6Li": ( 3, 3,  5603.05181,   31.99405),
    "7Li": ( 3, 4,  6535.36652,   39.24452),
}

m_e = 0.51099895


def main():
    with open(Path(__file__).parent / "depth-resolved-phi-k-hoefsmit.witness.json") as f:
        ws = json.load(f)
    iso_phi_k = ws["isotope_Phi_k"]
    fitted_alpha = ws.get("fitted_alpha_k_MeV", [])

    print("=" * 80)
    print("ZERO-PARAMETER STRUCTURAL MASS PREDICTION")
    print("=" * 80)
    print(f"Substrate: q_0 ≈ {Q0_FLOAT}")
    print(f"m_e = {m_e} MeV")
    print()
    print("Formula: B_pred(β) = m_e · Σ_k Φ_k(β)")
    print("  where Φ_k = Σ_{depth(λ)=k} y_λ · log|χ_λ(β)|")
    print("  (y_λ are Jones-Markov gauge-free; Φ_k from Hoefsmit characters)")
    print()
    print(f"{'iso':>5} {'A':>3} {'Z':>2} {'N':>2} "
          f"{'B_AME':>10} {'B_0param':>10} {'err %':>8} {'err ppb':>14}")
    print("-" * 80)
    results = {}
    for iso, (Z, N, M_AME, B_AME) in AME.items():
        if iso not in iso_phi_k:
            print(f"{iso:>5} {Z+N:>3} {Z:>2} {N:>2} {B_AME:>10.4f}  (no Phi_k data)")
            continue
        phi_k = iso_phi_k[iso]["Phi_k"]
        # Sum all depth strata; Phi_k keys are strings of integer depths
        total_phi = sum(phi_k.values())
        B_pred = m_e * total_phi
        err_pct = (B_pred - B_AME) / B_AME * 100 if B_AME != 0 else 0
        err_ppb = (B_pred - B_AME) / B_AME * 1e9 if B_AME != 0 else 0
        print(f"{iso:>5} {Z+N:>3} {Z:>2} {N:>2} "
              f"{B_AME:>10.4f} {B_pred:>10.4f} {err_pct:>+7.3f}% {err_ppb:>+14.2e}")
        results[iso] = {
            "A": Z + N, "Z": Z, "N": N,
            "B_AME": B_AME, "B_pred_0param": B_pred,
            "err_pct": err_pct, "err_ppb": err_ppb,
            "Phi_k_total": total_phi,
        }

    # Now also try with fitted α_k (4 calibrations: p, n, D, T)
    print()
    print("=" * 80)
    print("FITTED α_k COMPARISON (4-calibration baseline)")
    print("=" * 80)
    if fitted_alpha:
        print(f"{'iso':>5} {'B_AME':>10} {'B_fitted':>10} {'err %':>8}")
        print("-" * 50)
        for iso, (Z, N, M_AME, B_AME) in AME.items():
            if iso not in iso_phi_k:
                continue
            phi_k = iso_phi_k[iso]["Phi_k"]
            B_pred_fit = sum(fitted_alpha[k] * phi_k[str(k)]
                             for k in range(min(len(fitted_alpha), 8))
                             if str(k) in phi_k)
            err_pct = (B_pred_fit - B_AME) / B_AME * 100
            print(f"{iso:>5} {B_AME:>10.4f} {B_pred_fit:>10.4f} {err_pct:>+7.3f}%")

    # Output
    out = {
        "computation": "isotope-mass-from-y-lambda-tower",
        "description": (
            "Zero-parameter structural mass prediction: B_pred(β) = m_e · "
            "Σ_k Φ_k(β) where Φ_k uses the gauge-free Jones-Markov "
            "weights y_λ from the witness file. No fitting, no α_k "
            "calibration. Comparison against AME 2020 + the existing "
            "fitted α_k (4-calibration baseline) shown for context."
        ),
        "q_0": float(Q0_FLOAT),
        "m_e_MeV": m_e,
        "results": results,
        "precision": "f64_numeric_fallback",
        "truncation_eps": 0.0,
    }
    out_path = Path(__file__).parent / "isotope-mass-from-y-lambda-tower.witness.json"
    with open(out_path, "w") as fp:
        json.dump(out, fp, indent=2, default=str)
    print(f"\nWitness: {out_path}")


if __name__ == "__main__":
    main()
