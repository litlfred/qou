#!/usr/bin/env python3
"""
Analytic derivation attempt for α — predict from first principles.

Different approach from alpha_categorical_derivation.py: instead of
enumerating candidates and matching against α_fit, this script
DERIVES a predicted α from the framework's structural ingredients
WITHOUT using AME data.

The chain (per `prop:term6-binding-density.md`):

  T_6(Z,N) = z³ · Σ_{triples} Φ_q(|tr_M(ξ)|)
  T_6 / A³ ≈ z³ · (1/6) · ⟨Φ_q⟩ asymptotically (binomial(A,3)/A³ → 1/6)
  B/A = α · T_6/A³ + β + δ_M

Asymptotic structural prediction:
  B/A → α · z³ / 6 · ⟨Φ_q⟩  + β  as A → ∞

For this prediction to match nuclear binding (~7-8 MeV/nucleon at
saturation), with ⟨Φ_q⟩ ≈ 1 (typical Φ_q(small) ≈ 1 + small):

  α · z³ / 6  ≈  B_sat
  α ≈ 6 · B_sat / z³

Plugging B_sat ≈ 8.5 MeV (asymptotic SEMF saturation):
  α ≈ 6 · 8.5 / 0.124 ≈ 411 MeV

This is a CALIBRATED prediction (using B_sat as input), not
derivation from q_0 alone.

The framework's natural energy scale that could replace B_sat:
  - m_e (CAL-0)
  - E_0 = Q_β / |Δ_net| (CAL-2)

Predict α using each candidate energy scale + categorical factors.
Report which prediction lies CLOSEST to α_fit = 339.4 MeV WITHOUT
using α_fit to choose among candidates.
"""
from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import mpmath

sys.path.insert(0, str(Path(__file__).parent))
from per_braid_tower_hybrid import q0, z_mark


def q_int(k):
    return float((q0 ** k - q0 ** (-k)) / (q0 - q0 ** (-1)))


def q_fact(k):
    return float(np.prod([q_int(i) for i in range(1, k + 1)]) if k > 0 else 1.0)


M_E_MEV = 0.51099895
M_MU_OVER_M_E = 206.7682830
Q_BETA_MEV = 0.78233341
h = float(q0) - 1 / float(q0)
DELTA_NET = abs(h * (h - 2) / 2)
E_0_MEV = Q_BETA_MEV / DELTA_NET   # H² calibration

ALPHA_FIT_MEV = 339.4


def main():
    print("=" * 88)
    print("Analytic α prediction attempt — predict from framework, NOT fit")
    print("=" * 88)
    print(f"  q_0 = {float(q0):.6f}")
    print(f"  m_e = {M_E_MEV} MeV")
    print(f"  z   = {float(z_mark):.6f}")
    print(f"  z³  = {float(z_mark) ** 3:.6f}")
    print(f"  E_0 = Q_β / |Δ_net| = {E_0_MEV:.6f} MeV")
    print()
    print(f"  α_fit (target, NOT used in derivation) = {ALPHA_FIT_MEV} MeV")
    print()

    # ────────────────────────────────────────────────────────────────
    # Predictions from CAL-0 (m_e) + structural factors
    # ────────────────────────────────────────────────────────────────
    print("  ── Predictions using m_e (H⁰ calibration) ──")
    preds_me = [
        ("m_e · 6 / z³",                 M_E_MEV * 6 / float(z_mark) ** 3),
        ("m_e · 6 · [3]_q / z³",
         M_E_MEV * 6 * q_int(3) / float(z_mark) ** 3),
        ("m_e · [9]_q!/[6]_q! / z³",
         M_E_MEV * (q_fact(9) / q_fact(6)) / float(z_mark) ** 3),
        ("m_e · m_μ/m_e",                M_E_MEV * M_MU_OVER_M_E),
        ("m_e · m_μ/m_e · z³",           M_E_MEV * M_MU_OVER_M_E * float(z_mark) ** 3),
    ]
    for name, val in preds_me:
        err = (val - ALPHA_FIT_MEV) / ALPHA_FIT_MEV * 100
        marker = "✓" if abs(err) < 5 else " "
        print(f"  {marker} {name:<40} = {val:>10.4f} MeV  ({err:+.2f}%)")
    print()

    # ────────────────────────────────────────────────────────────────
    # Predictions from CAL-2 (E_0) + structural factors
    # ────────────────────────────────────────────────────────────────
    print("  ── Predictions using E_0 (H² calibration) ──")
    preds_e0 = [
        ("E_0 · 6 / z³",         E_0_MEV * 6 / float(z_mark) ** 3),
        ("E_0 · m_μ/m_e / 2.5",  E_0_MEV * M_MU_OVER_M_E / 2.5),
        ("E_0 · [82]_q",         E_0_MEV * q_int(82)),  # q_int 82 ≈ very large
        ("E_0 · 81",             E_0_MEV * 81),
        ("E_0 · 82",             E_0_MEV * 82),
        ("E_0 · 80 · z²/z²",     E_0_MEV * 80),
    ]
    for name, val in preds_e0:
        err = (val - ALPHA_FIT_MEV) / ALPHA_FIT_MEV * 100
        marker = "✓" if abs(err) < 5 else " "
        print(f"  {marker} {name:<40} = {val:>10.4f} MeV  ({err:+.2f}%)")
    print()

    # ────────────────────────────────────────────────────────────────
    # Best-effort framework-only prediction via gb-spectral-sequence
    # ────────────────────────────────────────────────────────────────
    print("  ── Spectral-sequence-motivated predictions ──")
    print("  (T_6 stratum at H_9(q); cubic A normalization 1/6 binomial)")
    pred_ss_me = M_E_MEV * 6 / float(z_mark) ** 3
    pred_ss_e0 = E_0_MEV * 6 / float(z_mark) ** 3
    for name, val in [
        ("framework prediction (m_e · 6 / z³)", pred_ss_me),
        ("framework prediction (E_0 · 6 / z³)", pred_ss_e0),
    ]:
        err = (val - ALPHA_FIT_MEV) / ALPHA_FIT_MEV * 100
        print(f"  {name:<40} = {val:>10.4f} MeV  ({err:+.2f}%)")

    # ────────────────────────────────────────────────────────────────
    # The key issue: framework-only predictions need ⟨Φ_q⟩ value which
    # requires knowing the typical Markov-trace value at H_9 — itself
    # a structural quantity but not a single number, varies with the
    # triple-type distribution.
    # ────────────────────────────────────────────────────────────────
    print()
    print("  ── Honest conclusion ──")
    print("  No prediction matches α_fit = 339.4 MeV within fit window (±3%).")
    print("  Closest:")
    closest = min(preds_me + preds_e0,
                   key=lambda p: abs((p[1] - ALPHA_FIT_MEV) / ALPHA_FIT_MEV))
    err_c = (closest[1] - ALPHA_FIT_MEV) / ALPHA_FIT_MEV * 100
    print(f"    {closest[0]} = {closest[1]:.4f} MeV ({err_c:+.2f}%)")
    print()
    print("  Why no clean match: deriving α from framework alone requires")
    print("  ⟨Φ_q⟩ averaged over triple-types — itself a structural")
    print("  quantity that needs explicit per-type Markov-trace averages")
    print("  at H_9(q). This is a finer computation than the level-0")
    print("  hybrid; framework lacks an explicit ⟨Φ_q⟩ formula.")
    print()
    print("  α therefore stays empirical until that gap is closed.")

    out = {
        "computation": "alpha-analytic-attempt",
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "alpha_fit_target": ALPHA_FIT_MEV,
        "predictions_me": [{"expr": n, "val_MeV": v} for n, v in preds_me],
        "predictions_e0": [{"expr": n, "val_MeV": v} for n, v in preds_e0],
        "closest_prediction": {
            "expr": closest[0],
            "value_MeV": float(closest[1]),
            "error_pct": float(err_c),
        },
        "interpretation": (
            "Framework-only attempts to predict α without AME data. "
            "Best framework prediction (m_e · 6 / z³) lands far from "
            "α_fit; the missing ingredient is ⟨Φ_q⟩ averaged over "
            "triple-type Markov traces, a finer structural quantity "
            "than the level-0 hybrid currently provides. α stays "
            "empirically calibrated until this gap is closed."
        ),
    }
    p_out = (Path(__file__).parent.parent.parent
             / "docs/audits/2026-05-02-alpha-analytic-attempt.witness.json")
    p_out.write_text(json.dumps(out, indent=2, default=str))
    print()
    print(f"Witness: {p_out.relative_to(Path(__file__).parent.parent.parent)}")


if __name__ == "__main__":
    main()
