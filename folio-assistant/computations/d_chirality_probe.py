#!/usr/bin/env python3
"""
Probe: which chirality factor matches D binding?

Paper assigns D → (1+h) = 1.209 giving B_pred = -5.63 vs B_AME = 2.22
(err -353%, broken).  This script tests alternative candidate
chirality factors against B_AME.

Candidates:
  (1 + h)      = 1.209  [paper's chiral+]
  (1 - h)      = 0.791  [chiral-]
  (1 - h²)     = 0.956  [amphichiral, used for T/³He]
  (1 + h²)     = 1.044  [amphi-opposite]
  h            = 0.209  [raw deformation]
  (1 + h/2)    = 1.104
  (h + h²)     = 0.253  [bulk-suppressing]
  1            = 1.000  [no chirality]
  (1 - h)/(1 + h) = 0.654

Witness: d-chirality-probe.witness.json
"""
import json
import sys
from pathlib import Path
from datetime import datetime, timezone

sys.path.insert(0, str(Path(__file__).parent))

# Reuse upstream coefficient infrastructure
from bw_chirality_isotopes import (
    B_bulk, B_Zdep, pairing_sign, f_Zdep_scale, h,
    Q0, M_E_MEV,
)
import mpmath as mp


def predict_with_factor(Z: int, N: int, chirality_factor: float):
    """Paper's formula: B = chirality · B_bulk + h·[2]·B_Z."""
    A = Z + N
    sign = pairing_sign(Z, N)
    bulk = B_bulk(A, Z, N, sign)
    zdep = B_Zdep(A, Z, N)
    B = mp.mpf(str(chirality_factor)) * bulk + f_Zdep_scale * zdep
    return float(B)


if __name__ == "__main__":
    print("D CHIRALITY FACTOR PROBE — which a_K matches B_AME = 2.2246 MeV?")
    print("=" * 78)
    print(f"q_0 = {Q0}, h = {float(h):.4f}")
    print()
    Z, N = 1, 1
    B_AME = 2.22457

    candidates = {
        "(1 + h)  [paper, chiral+]":       1 + float(h),
        "(1 - h)  [chiral-]":              1 - float(h),
        "(1 - h²) [amphichiral, T/³He]":   1 - float(h)**2,
        "(1 + h²) [amphi-opposite]":       1 + float(h)**2,
        "h        [raw def]":              float(h),
        "(1 + h/2)":                       1 + float(h)/2,
        "(h + h²)":                        float(h) + float(h)**2,
        "1        [no chirality]":         1.0,
        "(1 - h)/(1 + h)":                 (1 - float(h)) / (1 + float(h)),
        "(1 - h²)^2 [⁴He Borromean²]":     (1 - float(h)**2)**2,
        "(1 + h)/2":                      (1 + float(h))/2,
        "1/(1 + h) [inverse]":            1 / (1 + float(h)),
        "(1 + h)^(-2)":                   1 / (1 + float(h))**2,
    }

    print(f"{'factor':<40}  {'a_K':>8}  {'B_pred':>10}  {'err%':>9}")
    print("-" * 72)
    results = {}
    for name, a_K in candidates.items():
        B_pred = predict_with_factor(Z, N, a_K)
        err = (B_pred - B_AME) / B_AME * 100
        tag = "★" if abs(err) < 5 else (" " if abs(err) < 30 else "✗")
        print(f"{name:<40}  {a_K:>8.4f}  {B_pred:>10.4f}  {err:>+8.2f}% {tag}")
        results[name] = {
            "a_K": a_K,
            "B_pred_MeV": B_pred,
            "err_pct": err,
        }

    best = min(results, key=lambda k: abs(results[k]["err_pct"]))
    print()
    print(f"Best match: {best}")
    print(f"  a_K = {results[best]['a_K']:.6f}")
    print(f"  B_pred = {results[best]['B_pred_MeV']:.4f} MeV")
    print(f"  err    = {results[best]['err_pct']:+.4f}%")

    # Also search a CONTINUOUS range for the optimal a_K
    import numpy as np
    grid = np.linspace(-2, 2, 4001)
    errs = []
    for a in grid:
        try:
            B = predict_with_factor(Z, N, a)
            errs.append((a, B, (B - B_AME) / B_AME * 100))
        except Exception:
            pass
    # Best continuous
    best_cont = min(errs, key=lambda e: abs(e[2]))
    print()
    print(f"Continuous search in a_K ∈ [-2, 2]:")
    print(f"  optimal a_K = {best_cont[0]:.6f}")
    print(f"  B_pred     = {best_cont[1]:.6f} MeV")
    print(f"  err        = {best_cont[2]:+.6f}%")

    # Try to express the optimal a_K as a simple q-integer combination
    a_opt = best_cont[0]
    print()
    print("Candidate q-integer expressions for optimal a_K:")
    h_val = float(h)
    attempts = {
        "1 − h²/2": 1 - h_val**2 / 2,
        "1 − h − h²": 1 - h_val - h_val**2,
        "(2 − h)/2": (2 - h_val) / 2,
        "q⁻¹": 1 / Q0,
        "1/(1 + h/2)": 1 / (1 + h_val/2),
        "h²/2 − h + 1": h_val**2 / 2 - h_val + 1,
    }
    for name, val in attempts.items():
        B = predict_with_factor(Z, N, float(val))
        err = (B - B_AME) / B_AME * 100
        print(f"  {name:<25} = {float(val):.6f}  → B_pred = {B:.4f}  err = {err:+.4f}%")

    witness = {
        "computation": "d-chirality-probe",
        "description": (
            "Probe alternative chirality factors for D, testing which "
            "a_K in B_K = a_K · B_bulk + h·[2]_q · B_Z matches B_AME(D) "
            "= 2.225 MeV.  Paper's (1+h) gives -353% error; this script "
            "searches alternatives."
        ),
        "reference_blocks": [
            "prop:figure-eight-bw-coefficients",
            "rem:deuteron-first-principles",
        ],
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "parameters": {
            "q_0": Q0,
            "h_q": float(h),
            "m_e_MeV": M_E_MEV,
            "B_AME_MeV": B_AME,
        },
        "candidates": results,
        "best_discrete": {
            "name": best,
            "a_K": results[best]["a_K"],
            "err_pct": results[best]["err_pct"],
        },
        "continuous_optimal": {
            "a_K": best_cont[0],
            "B_pred_MeV": best_cont[1],
            "err_pct": best_cont[2],
        },
    }
    out = Path(__file__).parent / "d-chirality-probe.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\nWitness: {out}")
