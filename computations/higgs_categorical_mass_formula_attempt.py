"""Construct a categorical mass formula for the Higgs (T(2, 8)) — Task 1 attempt.

Per user direction + structural finding from this branch's h^4 probe:
the scalar/gauge ratio refined identity is

  scalar/gauge ≈ (6/5) · (1 - h_0^4 · 2G)

with G = Catalan and h_0 = q_0 - q_0⁻¹.

This probe attempts to CONSTRUCT a categorical mass formula for the
Higgs from substrate, using the m_W as a known anchor and deriving
m_H structurally via:

  m_H = m_W · (m_H / m_W)
      = m_W · (P_4(h_0) / P_2(h_0)) · (scalar/gauge)
      = m_W · (P_4 / P_2) · (6/5) · (1 - h_0^4 · 2G)

where P_m(h_0) = Σ_{j=0}^m C(m+j, 2j)/2 · h_0^{2j} (sibling PR #1125
binomial pattern, sympy-proved).

If this matches m_H to high precision, the categorical formula is:

  m_H = m_W · [P_4(h_0) / P_2(h_0)] · [|S_3|/|partitions(4)|] · [1 - h_0^4 · Vol(B_3)/4]

where every term has structural categorical origin.

Status: EXPLORATORY (categorical formula CONSTRUCTION attempt).
"""
import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import json
import subprocess
import sys
from fractions import Fraction
from math import comb
from pathlib import Path

import mpmath as mp
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from mpmath import mpf

mp.mp.dps = 50

# Substrate
Q_0 = mpf(Q_50_DIGIT_STR)  # canonical 50-digit substrate pin
H_0 = Q_0 - mpf(1) / Q_0
HBAR_Q = (Q_0 - 1) / Q_0
VOL_B3 = 8 * mp.catalan
G_CATALAN = mp.catalan

# SM
M_W_GEV = mpf("80.379")
M_Z_GEV = mpf("91.1876")
M_H_GEV = mpf("125.10")


def c_2j_binomial(m: int, j: int) -> mpf:
    """Sibling PR #1125: c_{2j}(T(2, 2m)) = C(m+j, 2j) / 2."""
    return mpf(comb(m + j, 2 * j)) / 2


def trace_polynomial(m: int, h: mpf) -> mpf:
    """P_m(h) = Σ_{j=0}^m c_{2j} · h^{2j}."""
    return sum(c_2j_binomial(m, j) * h ** (2 * j) for j in range(m + 1))


def main():
    print("=" * 80)
    print("Task 1: Construct categorical mass formula for Higgs (T(2,8))")
    print("=" * 80)
    print(f"50-dps mpmath; Q_0 = {Q_0}, h_0 = {float(H_0):.10f}, h_0^4 = {float(H_0 ** 4):.10f}")
    print()

    # Compute the trace polynomial values
    P_2 = trace_polynomial(2, H_0)  # W
    P_3 = trace_polynomial(3, H_0)  # Z
    P_4 = trace_polynomial(4, H_0)  # H
    print(f"Trace polynomials at h_0:")
    print(f"  P_2(h_0) = {float(P_2):.10f}  (for T(2,4) = W)")
    print(f"  P_3(h_0) = {float(P_3):.10f}  (for T(2,6) = Z)")
    print(f"  P_4(h_0) = {float(P_4):.10f}  (for T(2,8) = H)")
    print()

    # Cardinality ratio
    SIX_FIFTHS = mpf("6") / mpf("5")
    print(f"Leading-order cardinality ratio:")
    print(f"  6/5 = |S_3| / |partitions(4)| = {float(SIX_FIFTHS):.10f}")
    print()

    # h^4 correction
    correction_factor = 1 - H_0 ** 4 * 2 * G_CATALAN
    print(f"h^4 structural correction:")
    print(f"  (1 - h_0^4 · 2G) = (1 - {float(H_0 ** 4):.6f} · {float(2 * G_CATALAN):.6f})")
    print(f"                  = {float(correction_factor):.10f}")
    print()

    # Refined scalar/gauge ratio
    scalar_gauge_refined = SIX_FIFTHS * correction_factor
    print(f"Refined scalar/gauge ratio:")
    print(f"  (6/5) · (1 - h_0^4 · 2G) = {float(scalar_gauge_refined):.10f}")
    print(f"  Empirical 171/143         = {float(mpf(171) / mpf(143)):.10f}")
    print(f"  Match: {(float(scalar_gauge_refined) - float(mpf(171) / mpf(143))) / float(mpf(171) / mpf(143)) * 100:+.4f}%")
    print()

    # Trace polynomial ratio
    P4_over_P2 = P_4 / P_2
    P4_over_P3 = P_4 / P_3
    print(f"Trace polynomial ratios:")
    print(f"  P_4 / P_2 = {float(P4_over_P2):.10f}  (H/W)")
    print(f"  P_4 / P_3 = {float(P4_over_P3):.10f}  (H/Z)")
    print()

    # Categorical mass formula for Higgs (from W)
    print("=" * 80)
    print("Categorical mass formula: m_H from m_W via substrate quantities")
    print("=" * 80)
    print()
    print("Proposed formula:")
    print("  m_H = m_W · (P_4/P_2) · (6/5) · (1 - h_0^4 · 2G)")
    print()

    m_H_pred_from_W = M_W_GEV * P4_over_P2 * SIX_FIFTHS * correction_factor
    print(f"  Inputs:")
    print(f"    m_W           = {float(M_W_GEV):.4f} GeV (SM measured)")
    print(f"    P_4/P_2       = {float(P4_over_P2):.10f}")
    print(f"    6/5           = {float(SIX_FIFTHS):.10f}")
    print(f"    (1 - h^4·2G)  = {float(correction_factor):.10f}")
    print()
    print(f"  Predicted m_H   = {float(m_H_pred_from_W):.6f} GeV")
    print(f"  Measured m_H    = {float(M_H_GEV):.6f} GeV")
    dev_pct = float((m_H_pred_from_W - M_H_GEV) / M_H_GEV * 100)
    print(f"  Deviation       = {dev_pct:+.4f}%")
    print()

    # Same formula from Z (cross-check)
    print("Cross-check: m_H from m_Z via the SAME formula")
    m_H_pred_from_Z = M_Z_GEV * (P_4 / P_3) * SIX_FIFTHS * correction_factor
    print(f"  Predicted m_H from Z = {float(m_H_pred_from_Z):.6f} GeV")
    dev_pct_z = float((m_H_pred_from_Z - M_H_GEV) / M_H_GEV * 100)
    print(f"  Deviation            = {dev_pct_z:+.4f}%")
    print()

    # Verdict
    print("=" * 80)
    print("VERDICT — Categorical mass formula for Higgs")
    print("=" * 80)
    print()
    if abs(dev_pct) < 1 and abs(dev_pct_z) < 1:
        print("✓ STRONG: m_H predicted from m_W via the formula matches measured m_H within 1%.")
        print("  Cross-check from m_Z also matches within 1%.")
        print()
        print("  The categorical mass formula for Higgs from substrate + W anchor is:")
        print("    m_H = m_W · [P_4(h_0) / P_2(h_0)] · [|S_3|/|partitions(4)|]")
        print("              · [1 - h_0^4 · Vol(B_3)/4]")
        print()
        print("  All factors have categorical origin:")
        print("    P_m       — sibling PR #1125 binomial pattern (sympy-proved)")
        print("    |S_3|, etc — concrete cardinalities")
        print("    Vol(B_3)  — Adams 1985 (= 8·Catalan)")
        print("    h_0       — substrate CAL-2 anchor")
    elif abs(dev_pct) < 5:
        print(f"~ MODERATE: m_H predicted within {abs(dev_pct):.2f}%; structural form correct")
        print("  but possibly a higher-order correction still missing.")
    else:
        print(f"✗ POOR: deviation {dev_pct:.2f}% — formula structure is wrong.")

    # Witness
    witness = {
        "compute": "higgs_categorical_mass_formula_attempt",
        "description": (
            "Constructs a categorical mass formula for the Higgs (T(2,8)) "
            "using substrate quantities: P_4/P_2 (binomial pattern from "
            "PR #1125), 6/5 (cardinality ratio), and 1 - h_0^4 · 2G "
            "(h^4 correction from this branch's probe). Tests whether "
            "m_H = m_W · (P_4/P_2) · (6/5) · (1 - h_0^4 · 2G) matches "
            "the measured Higgs mass."
        ),
        "parameters": {
            "precision": "mpfr",
            "dps": 50,
            "Q_0": str(Q_0),
            "H_0": str(H_0),
            "M_W_GEV": float(M_W_GEV),
            "M_Z_GEV": float(M_Z_GEV),
            "M_H_GEV": float(M_H_GEV),
            "G_CATALAN": str(G_CATALAN),
        },
        "factors": {
            "P_2_at_h0": float(P_2),
            "P_3_at_h0": float(P_3),
            "P_4_at_h0": float(P_4),
            "P_4_over_P_2": float(P4_over_P2),
            "P_4_over_P_3": float(P4_over_P3),
            "six_fifths": float(SIX_FIFTHS),
            "h4_correction_factor": float(correction_factor),
            "scalar_gauge_refined": float(scalar_gauge_refined),
        },
        "predictions": {
            "m_H_from_W_GeV": float(m_H_pred_from_W),
            "m_H_from_Z_GeV": float(m_H_pred_from_Z),
            "m_H_measured_GeV": float(M_H_GEV),
            "deviation_from_W_pct": dev_pct,
            "deviation_from_Z_pct": dev_pct_z,
        },
        "formula": (
            "m_H = m_W · (P_4/P_2) · (6/5) · (1 - h_0^4 · 2G)"
        ),
        "interpretation": (
            "If m_H prediction matches measurement within 1%, the "
            "formula has all categorical components: P_m from "
            "binomial pattern, 6/5 from cardinality ratio, "
            "1 - h_0^4·2G from h^4 correction with Vol(B_3) anchor. "
            "This would be the FIRST constructed categorical mass "
            "formula for a torus-knot particle (Higgs) in the RT-route "
            "chain, using m_W as the anchor."
        ),
        "status": "exploratory",
        "tags": [
            "categorical-mass-formula",
            "higgs-construction",
            "rt-route",
            "torus-knot-mass",
            "categorical-derivation-attempt",
        ],
        "scriptCommitSha": (
            subprocess.check_output(["git", "rev-parse", "HEAD"])
            .decode().strip()
        ),
    }
    out_path = Path(__file__).parent / "higgs-categorical-mass-formula-attempt.witness.json"
    out_path.write_text(json.dumps(witness, indent=2, sort_keys=True) + "\n")
    print(f"\nWitness: {out_path.relative_to(Path.cwd())}")


if __name__ == "__main__":
    main()
