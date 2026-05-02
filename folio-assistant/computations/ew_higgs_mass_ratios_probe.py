#!/usr/bin/env python3
"""Test of `conj:electroweak-higgs-torus-link-triplet`: do the
torus-link assignments W↔T(2,4), Z↔T(2,6), H↔T(2,8) reproduce
PDG mass ratios?

The conjecture asserts mass ordering 4 < 6 < 8 maps monotonically
to W < Z < H, but it does NOT specify the absolute scale (the ρ
prefactor for force-carriers is open).

What we CAN check: ratio predictions independent of ρ.

For T(2, 2k) = ̂(σ_1^{2k}) ∈ closure(B_2), the Wedderburn-block
characters are χ_sym = q^{2k}, χ_alt = q^{-2k}, and the Markov
trace at q_0 is

    tr_M(σ_1^{2k}) = y_sym · q^{2k} + y_alt · q^{-2k}

with y_sym, y_alt determined by the H_2 Markov closure conditions
(tr_M(1) = 1, tr_M(σ_1) = z = 1/(q^{1/2}+q^{-1/2})):

    y_sym = (z + q^{-1}) / (q + q^{-1})
    y_alt = 1 - y_sym

If the categorical mass formula is m ∝ tr_M (with the same ρ for
all force-carriers), the predicted mass ratios are

    m_Z / m_W  =  tr_M(σ_1^6) / tr_M(σ_1^4)
    m_H / m_W  =  tr_M(σ_1^8) / tr_M(σ_1^4)

This script computes them and compares to PDG/CODATA.

Refs:
  - conj:electroweak-higgs-torus-link-triplet
  - prop:atom-knot-mass-derivation §"Mass identity"
"""
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

import mpmath as mp


def tr_M_h2_torus(k: int, q: mp.mpf) -> mp.mpf:
    """tr_M(σ_1^{2k}) at H_2 with q ∈ ℝ_{>0}."""
    sqrt_q = mp.sqrt(q)
    z = 1 / (sqrt_q + 1 / sqrt_q)
    inv_q = 1 / q
    # y_sym + y_alt = 1 ; y_sym·q + y_alt·(-1/q) = z
    # solve:  y_sym = (z + 1/q) / (q + 1/q)
    y_sym = (z + inv_q) / (q + inv_q)
    y_alt = 1 - y_sym
    return y_sym * q ** (2 * k) + y_alt * inv_q ** (2 * k)


def main():
    base = Path(__file__).parent
    mp.mp.dps = 50
    q_0 = mp.mpf('1.1099785955541805')

    # PDG / CODATA values
    M_W = mp.mpf('80.379')      # GeV
    M_Z = mp.mpf('91.1876')
    M_H = mp.mpf('125.25')

    print("══════════════════════════════════════════════════════════════════════")
    print("  EW/Higgs torus-link triplet — mass-ratio test of conj:electroweak-")
    print("  higgs-torus-link-triplet at q_0 ≈ 1.1099786 (50 dps)")
    print("══════════════════════════════════════════════════════════════════════\n")

    # tr_M values
    table = []
    for k in range(1, 8):
        tr = tr_M_h2_torus(k, q_0)
        chi_sym = q_0 ** (2 * k)
        chi_alt = q_0 ** (-2 * k)
        crossings = 2 * k
        genus = k - 1
        role = {1: "Hopf link L_H (binding)", 2: "W^± (conj)", 3: "Z (conj)", 4: "H (conj)"}.get(k, "")
        table.append({
            "k": k, "crossings": crossings, "genus": genus,
            "chi_sym": float(chi_sym), "chi_alt": float(chi_alt),
            "tr_M": float(tr), "role": role
        })
        print(f"  k={k}, T(2,{crossings}), genus={genus}: "
              f"χ_sym={float(chi_sym):.4f}, χ_alt={float(chi_alt):.4f}, "
              f"tr_M={float(tr):.6f}  [{role}]")

    tr_W = tr_M_h2_torus(2, q_0)
    tr_Z = tr_M_h2_torus(3, q_0)
    tr_H = tr_M_h2_torus(4, q_0)

    print("\n──── mass-ratio predictions (categorical: m ∝ tr_M) ────")
    pred_Z_W = tr_Z / tr_W
    pred_H_W = tr_H / tr_W
    pred_H_Z = tr_H / tr_Z
    obs_Z_W = M_Z / M_W
    obs_H_W = M_H / M_W
    obs_H_Z = M_H / M_Z

    print(f"  m_Z / m_W:  predicted {float(pred_Z_W):.6f}, "
          f"PDG {float(obs_Z_W):.6f}, "
          f"error {float((pred_Z_W - obs_Z_W) / obs_Z_W * 100):+.3f}%")
    print(f"  m_H / m_W:  predicted {float(pred_H_W):.6f}, "
          f"PDG {float(obs_H_W):.6f}, "
          f"error {float((pred_H_W - obs_H_W) / obs_H_W * 100):+.3f}%")
    print(f"  m_H / m_Z:  predicted {float(pred_H_Z):.6f}, "
          f"PDG {float(obs_H_Z):.6f}, "
          f"error {float((pred_H_Z - obs_H_Z) / obs_H_Z * 100):+.3f}%")

    # What k would give right H/W ratio?
    print("\n──── if Higgs ≠ T(2,8): which T(2,2k) matches m_H/m_W exactly? ────")
    for k_test in [4, 5, 6]:
        tr = tr_M_h2_torus(k_test, q_0)
        ratio = tr / tr_W
        err = (ratio - obs_H_W) / obs_H_W * 100
        marker = "  ←" if abs(err) < 5 else ""
        print(f"  k={k_test}, T(2,{2*k_test}): ratio = {float(ratio):.6f}, "
              f"error from m_H/m_W = {float(err):+.3f}%{marker}")

    # Honest finding
    print("\n──── Finding ────")
    err_Z = float((pred_Z_W - obs_Z_W) / obs_Z_W * 100)
    err_H = float((pred_H_W - obs_H_W) / obs_H_W * 100)
    print(f"  m_Z / m_W under categorical m ∝ tr_M: {err_Z:+.3f}% from PDG")
    print(f"    → conjecture's Z ↔ T(2,6) holds at the few-percent level ✓")
    print(f"  m_H / m_W under same: {err_H:+.3f}% from PDG")
    print(f"    → conjecture's H ↔ T(2,8) is OFF by ~12% — too LIGHT")
    print(f"  This is a real signal: either")
    print(f"    (a) H ↔ T(2,10) fits better (k=5 gives ratio ≈ 1.65,")
    print(f"        bracketing PDG 1.559) but breaks U5 monotonic mapping")
    print(f"    (b) Higgs needs a per-particle correction (it's a scalar)")
    print(f"    (c) categorical mass formula for force-carriers includes an")
    print(f"        additional factor specific to even-twist 2-component links")
    print(f"        that depends on Seifert genus")

    out_path = base / "ew-higgs-mass-ratios-probe.witness.json"
    witness = {
        "computation": "ew-higgs-mass-ratios-probe",
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "description": (
            "Quantitative test of conj:electroweak-higgs-torus-link-triplet: "
            "compute mass ratios m_Z/m_W and m_H/m_W under the assumption "
            "m ∝ tr_M(σ_1^{2k}) at q_0, compare to PDG.  Finds m_Z/m_W "
            "agrees to within 3% but m_H/m_W is too low by 12% — a real "
            "constraint on the conjecture."
        ),
        "q_0": float(q_0),
        "table": table,
        "predictions": {
            "m_Z_over_m_W": {"predicted": float(pred_Z_W), "PDG": float(obs_Z_W),
                             "err_pct": float(err_Z)},
            "m_H_over_m_W": {"predicted": float(pred_H_W), "PDG": float(obs_H_W),
                             "err_pct": float(err_H)},
            "m_H_over_m_Z": {"predicted": float(pred_H_Z), "PDG": float(obs_H_Z),
                             "err_pct": float((pred_H_Z - obs_H_Z) / obs_H_Z * 100)},
        },
        "open_questions": [
            "Higgs identification with T(2,8) gives m_H 12% too LIGHT vs PDG. "
            "Either (a) H ↔ T(2,10) fits the ratio (1.65 vs PDG 1.56) but "
            "breaks U5's monotonic mapping; (b) Higgs needs a per-particle "
            "correction; (c) the categorical mass formula includes a "
            "Seifert-genus-dependent factor specific to even-twist 2-component "
            "torus links that we haven't accounted for.",
            "ρ for force-carriers is open: per the conjecture, only ratios are "
            "constrained until ρ_W is structurally derived.",
        ],
        "constraint_on_conjecture": (
            "The 12% m_H deficit at T(2,8) is the largest single quantitative "
            "test of the conjecture available today.  It does not falsify the "
            "framework (the conjecture only asserts monotonic mapping for the "
            "ratio U5, which still holds: tr_M increases with k strictly), "
            "but it does indicate that the simple proportionality m ∝ tr_M "
            "needs at least one structural correction at the Higgs."
        ),
    }
    with open(out_path, "w") as f:
        json.dump(witness, f, indent=2)
    print(f"\n→ wrote {out_path}")


if __name__ == "__main__":
    main()
