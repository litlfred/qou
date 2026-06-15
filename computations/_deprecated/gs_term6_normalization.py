#!/usr/bin/env python3
"""
GS-filtration Term 6 — per-nucleon / per-triple normalization.

The raw Term 6 from gs_filtration_e2_probe.py grows combinatorially
(0, 1, 4, 20, 84, 220, 560 for A = 2..16) while binding/nucleon
saturates at ~7 MeV. This script tests three normalizations and
fits a calibration coefficient.

Normalizations:
  N1 = Term6 / A                — per-nucleon density
  N2 = Term6 / (A choose 3)     — per-triple density
  N3 = Term6 / A^(2/3)           — surface-like scaling

For each, fit  binding/nucleon ≈ a · N(Z, N) + b  via least-
squares and report residual std vs raw correlation.

If any normalization gives ≥ 0.9 correlation AND a clean
intercept-and-slope fit, that's evidence the GS Term 6 captures
the binding-energy structure with calibrated coupling.
"""
from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import mpmath

sys.path.insert(0, str(Path(__file__).parent))


def load_term6() -> list:
    p = Path(__file__).parent.parent.parent / "docs/audits/2026-05-02-gs-filtration-E2-probe.witness.json"
    return json.loads(p.read_text())["atoms"]


def fit(name: str, x: np.ndarray, y: np.ndarray) -> dict:
    """Linear LS fit y = a x + b; return slope, intercept, R, residual std."""
    if len(x) < 2:
        return {"name": name, "slope": float("nan")}
    coef = np.polyfit(x, y, 1)
    pred = np.polyval(coef, x)
    resid = y - pred
    R = np.corrcoef(x, y)[0, 1]
    return {
        "name": name,
        "slope": float(coef[0]),
        "intercept": float(coef[1]),
        "R": float(R),
        "R_sq": float(R ** 2),
        "residual_std": float(resid.std()),
        "max_abs_resid": float(np.max(np.abs(resid))),
    }


if __name__ == "__main__":
    print("=" * 88)
    print("GS Term 6 — per-nucleon normalization probes")
    print("=" * 88)

    rows = load_term6()
    # Drop atoms where Term6 is zero (D, etc.)
    valid = [r for r in rows
             if isinstance(r.get("term6_z3_sum_PhiQ"), (int, float))
             and r["term6_z3_sum_PhiQ"] > 0]

    A_arr = np.array([r["A"] for r in valid])
    T6 = np.array([r["term6_z3_sum_PhiQ"] for r in valid])
    bn = np.array([r["binding_per_nucleon"] for r in valid])

    n_choose_3 = (A_arr * (A_arr - 1) * (A_arr - 2)) / 6
    A_23 = A_arr ** (2 / 3)

    norms = {
        "raw_T6":        T6,
        "T6_over_A":     T6 / A_arr,
        "T6_over_C(A,3)": T6 / np.maximum(n_choose_3, 1),
        "T6_over_A23":   T6 / A_23,
        "T6_over_A2":    T6 / A_arr ** 2,
        "T6_over_A3":    T6 / A_arr ** 3,
    }

    results = []
    for name, x in norms.items():
        r = fit(name, x, bn)
        results.append(r)

    print(f"  {'normalization':<18} {'slope':>14} {'intercept':>12} "
          f"{'R':>8} {'R²':>8} {'resid σ':>10}")
    print("  " + "-" * 80)
    for r in results:
        print(f"  {r['name']:<18} {r['slope']:>14.4e} {r['intercept']:>12.4f} "
              f"{r['R']:>8.4f} {r['R_sq']:>8.4f} {r['residual_std']:>10.4f}")

    # Show per-atom values for the best fit
    best = max(results, key=lambda r: r["R_sq"])
    print()
    print(f"  Best fit: {best['name']}  R² = {best['R_sq']:.4f}")
    print(f"  binding/nucleon ≈ {best['slope']:.4e} · {best['name']} + {best['intercept']:.4f}")
    print()
    print(f"  {'atom':>5} {'A':>3} {'Term6':>14} {'normalized':>14} "
          f"{'B/A actual':>12} {'B/A predicted':>15} {'resid':>9}")
    print("  " + "-" * 84)
    x_best = norms[best['name']]
    for atom_row, x_val in zip(valid, x_best):
        pred = best['slope'] * x_val + best['intercept']
        resid = atom_row["binding_per_nucleon"] - pred
        print(f"  {atom_row['atom']:>5} {atom_row['A']:>3} "
              f"{atom_row['term6_z3_sum_PhiQ']:>14.4e} {x_val:>14.4e} "
              f"{atom_row['binding_per_nucleon']:>12.4f} {pred:>15.4f} "
              f"{resid:>+9.4f}")

    out = {
        "computation": "gs-filtration-Term6-normalization",
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "normalizations": [r["name"] for r in results],
        "fits": results,
        "best_fit": best,
        "interpretation": (
            "Tests several normalizations of the GS Term 6 against "
            "AME binding/nucleon. The best R² indicates which functional "
            "form of the level-3 stratum captures the binding-energy "
            "structure. Term 6 / A^k for various k separates the "
            "combinatorial growth from the per-nucleon density."
        ),
    }
    out_path = (Path(__file__).parent.parent.parent
                / "docs/audits/2026-05-02-Term6-normalization.witness.json")
    out_path.write_text(json.dumps(out, indent=2, default=str))
    print()
    print(f"Witness: {out_path.relative_to(Path(__file__).parent.parent.parent)}")
