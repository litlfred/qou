#!/usr/bin/env python3
"""
Honest validation of the 2-parameter sym/alt mirror fit.

The previous probe (sym_alt_mirror_probe.py) ran a 3-coefficient
LSQ on 4 data points and reported 0.01-0.03% residuals on the
last two atoms.  With only 4 atoms and 3 params, that "fit" has
1 degree of freedom — it's interpolation, not prediction.

This probe runs leave-one-out cross-validation:
  For each atom, fit coefficients on the OTHER 3 atoms,
  then predict the held-out atom.  Report held-out residual.

If held-out residuals stay ~0.01%, the fit captures real structure.
If held-out residuals are %-scale, the 2-param model is just
interpolation.
"""
from __future__ import annotations

import json
from pathlib import Path
from datetime import datetime, timezone

import numpy as np

# Data from sym_alt_mirror_probe.py run
ROWS = [
    # (name, dev_pct, ln|J(q₀²)|, χ_sym − χ_alt)
    ("D",   -1.079,  +0.1912, +2.2367),
    ("T",   +0.156,  +0.3175, +2.2611),
    ("3He", +3.059,  -2.7447, +2.8443),
    ("4He", -5.541, -10.9788, +2.8754),
]


def fit_and_predict(train_rows, test_row):
    """Fit dev% = a·ln|J| + b·(χ_sym-χ_alt) + c on train_rows,
    predict dev% for test_row."""
    X = np.array([[r[2], r[3], 1.0] for r in train_rows])
    y = np.array([r[1] for r in train_rows])
    coeffs, *_ = np.linalg.lstsq(X, y, rcond=None)
    x_test = np.array([test_row[2], test_row[3], 1.0])
    pred = float(x_test @ coeffs)
    return coeffs, pred


if __name__ == "__main__":
    print("=" * 90)
    print("LEAVE-ONE-OUT CROSS-VALIDATION of 2-parameter mirror fit")
    print("  dev% = a·ln|J(q₀²)| + b·(χ_sym − χ_alt) + c")
    print("=" * 90)

    print(f"\n  {'held-out':>10} {'obs':>8} {'pred':>8} "
          f"{'resid':>8} {'|resid|':>10} "
          f"{'a':>8} {'b':>8} {'c':>10}")
    results = []
    for i, held in enumerate(ROWS):
        train = ROWS[:i] + ROWS[i+1:]
        coeffs, pred = fit_and_predict(train, held)
        resid = pred - held[1]
        print(f"  {held[0]:>10} {held[1]:>+7.3f}% "
              f"{pred:>+7.3f}% {resid:>+7.3f}% "
              f"{abs(resid):>9.3f}% "
              f"{coeffs[0]:>+7.3f} {coeffs[1]:>+7.3f} "
              f"{coeffs[2]:>+10.3f}")
        results.append({
            "held_out": held[0],
            "observed_pct": held[1],
            "predicted_pct": pred,
            "residual_pct": resid,
            "abs_residual_pct": abs(resid),
            "fit_a": float(coeffs[0]),
            "fit_b": float(coeffs[1]),
            "fit_c": float(coeffs[2]),
        })

    mean_abs = sum(r["abs_residual_pct"] for r in results) / len(results)
    max_abs = max(r["abs_residual_pct"] for r in results)
    print(f"\n  Mean |held-out residual|: {mean_abs:.3f}%")
    print(f"  Max  |held-out residual|: {max_abs:.3f}%")

    # Also run the SAME fit on all 4 (for comparison — the in-sample fit)
    print(f"\n{'=' * 90}")
    print("In-sample fit on ALL 4 atoms (reference)")
    print("=" * 90)
    X_full = np.array([[r[2], r[3], 1.0] for r in ROWS])
    y_full = np.array([r[1] for r in ROWS])
    coeffs_full, *_ = np.linalg.lstsq(X_full, y_full, rcond=None)
    pred_full = X_full @ coeffs_full
    print(f"  Fitted: dev% = {coeffs_full[0]:+.3f}·ln|J| "
          f"+ {coeffs_full[1]:+.3f}·(χ_s−χ_a) {coeffs_full[2]:+.3f}")
    print(f"  {'atom':>4} {'obs':>8} {'pred':>8} {'resid':>8}")
    for row, p in zip(ROWS, pred_full):
        resid = p - row[1]
        print(f"  {row[0]:>4} {row[1]:>+7.3f}% {p:>+7.3f}% "
              f"{resid:>+7.3f}%")

    # Coefficient stability across LOO folds
    print(f"\n{'=' * 90}")
    print("Coefficient stability across LOO folds")
    print("=" * 90)
    a_vals = [r["fit_a"] for r in results]
    b_vals = [r["fit_b"] for r in results]
    c_vals = [r["fit_c"] for r in results]
    for name, vals in [("a (ln|J|)", a_vals), ("b (χ_s−χ_a)", b_vals),
                         ("c (intercept)", c_vals)]:
        mn = sum(vals) / len(vals)
        spread = max(vals) - min(vals)
        rel_var = spread / abs(mn) if mn != 0 else float("inf")
        print(f"  {name:>15}: values={[f'{v:+.3f}' for v in vals]}  "
              f"mean={mn:+.3f}  spread={spread:.3f}  rel_var={rel_var:.2%}")

    witness = {
        "computation": "sym-alt-loo-validation",
        "description": (
            "Leave-one-out cross-validation of the 2-parameter "
            "dev% = a·ln|J(q₀²)| + b·(χ_sym − χ_alt) + c fit.  "
            "If held-out residuals ~0.01%, fit captures real structure. "
            "If %-scale, it's just interpolation with 1 DoF remaining "
            "from 4 data points × 3 fitted params."
        ),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "input_rows": ROWS,
        "loo_results": results,
        "in_sample_fit_all_4": {
            "a": float(coeffs_full[0]),
            "b": float(coeffs_full[1]),
            "c": float(coeffs_full[2]),
        },
        "mean_abs_residual_pct": mean_abs,
        "max_abs_residual_pct": max_abs,
    }
    out = Path(__file__).parent / "sym-alt-loo-validation.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\nWitness: {out}")
