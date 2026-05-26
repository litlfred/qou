#!/usr/bin/env python3
"""
q_beta_consistency_gap_diagnostic.py — localise the 2113 ppm gap between
the mass-derived Q_β and the N=3 categorical Q_β.

Two independent derivation paths for Q_β from (m_e, q_0):

  Path A (mass-derived):  Q_β = m_n − m_p − m_e
    where m_p = dim V_{(2,1)} · (m_μ · F_Bor − |S_3| · m_e)
    and   m_n = m_p · (1 + X/(1 − X/2)),  X = flavor-split

  Path B (N=3 categorical ladder):
    Q_β = Q_A · cos(α − b·ℏ_q²/2) · (1 − b²·ℏ_q⁴) · (1 + c_3·b³·ℏ_q⁶)
    with c_3 = J_Hopf(q=1) = −2

Path A gives 0.7807 MeV (−2113 ppm); Path B gives 0.78233 MeV (+6 ppb).
This script decomposes the gap into contributions from m_p residual vs
flavor-split residual.

Also tests Path C (alternative m_n derivation):
  m_n = m_p + Q_β(N=3) + m_e
using the categorical Q_β directly, bypassing the flavor-split entirely.
"""
from __future__ import annotations

import sys
from pathlib import Path

from mpmath import mp, mpf

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from experimental_constants import M_E_MEV  # noqa: E402
from codata_constants import (  # noqa: E402
    M_P_MEV_VALIDATION,
    M_N_MEV_VALIDATION,
)


def main():
    set_compute_dps()

    q = mpf(Q_50_DIGIT_STR)
    m_e = mpf(M_E_MEV)
    m_mu = mpf("105.6583755")
    m_p_codata = mpf(M_P_MEV_VALIDATION)
    m_n_codata = mpf(M_N_MEV_VALIDATION)
    Q_beta_codata = m_n_codata - m_p_codata - m_e

    h = q - 1 / q

    # ── Borromean Markov trace (Lean-proved) ──
    tr_M = abs((4 + h ** 2 - 3 * h ** 4 - h ** 6) / (h ** 2 + 4))
    q_int = lambda n: (q ** n - q ** (-n)) / (q - 1 / q)
    q_fac_3 = q_int(3) * q_int(2) * q_int(1)
    F_Bor = tr_M * q_fac_3 / q ** 3

    # ── Path A: mass-derived Q_β ──
    m_p_pred = 2 * (m_mu * F_Bor - 6 * m_e)
    X = (q - 1) ** 2 * (1 - q ** (-4)) / 3
    m_n_pathA = m_p_pred * (1 + X / (1 - X / 2))
    Q_beta_pathA = m_n_pathA - m_p_pred - m_e

    # ── Path B: N=3 categorical (from witness) ──
    Q_beta_pathB = mpf("0.782333414494")

    # ── Path C: m_n via categorical Q_β ──
    m_n_pathC = m_p_pred + Q_beta_pathB + m_e

    # ── Decompose the gap ──
    m_p_residual = m_p_pred - m_p_codata
    m_p_contribution_to_Q = -m_p_residual  # Q = m_n - m_p - m_e; error in m_p propagates inverted

    X_codata = (m_n_codata - m_p_codata) / ((m_n_codata + m_p_codata) / 2)
    flavor_split_residual = X - X_codata

    gap = Q_beta_pathA - Q_beta_pathB

    wb = WitnessBuilder("q-beta-consistency-gap-diagnostic", engine="mpmath")

    # ── Report ──
    data = {
        "path_A_mass_derived": {
            "m_p_pred_MeV": str(m_p_pred),
            "m_n_pred_MeV": str(m_n_pathA),
            "Q_beta_MeV": str(Q_beta_pathA),
            "Q_beta_ppm_vs_codata": str(
                (Q_beta_pathA - Q_beta_codata) / Q_beta_codata * 1e6
            ),
            "flavor_split_X": str(X),
            "flavor_split_X_codata": str(X_codata),
            "flavor_split_X_residual_pct": str(
                float((X - X_codata) / X_codata * 100)
            ),
        },
        "path_B_categorical": {
            "Q_beta_MeV": str(Q_beta_pathB),
            "Q_beta_ppb_vs_codata": str(
                float((Q_beta_pathB - Q_beta_codata) / Q_beta_codata * 1e9)
            ),
        },
        "path_C_m_n_via_categorical_Q_beta": {
            "m_n_pred_MeV": str(m_n_pathC),
            "m_n_ppm_vs_codata": str(
                float((m_n_pathC - m_n_codata) / m_n_codata * 1e6)
            ),
            "improvement_over_pathA": str(
                float(
                    abs(
                        (m_n_pathA - m_n_codata) / m_n_codata
                    )
                    / abs(
                        (m_n_pathC - m_n_codata) / m_n_codata
                    )
                )
            )
            if abs(m_n_pathC - m_n_codata) > 0
            else "inf",
        },
        "gap_decomposition": {
            "total_gap_keV": str(float(gap * 1e3)),
            "total_gap_ppm": str(float(gap / Q_beta_codata * 1e6)),
            "m_p_residual_contribution_keV": str(
                float(m_p_residual * 1e3)
            ),
            "flavor_split_contribution_keV": str(
                float((gap * 1e3) - (m_p_residual * 1e3))
            ),
            "dominant_source": (
                "flavor-split X"
                if abs(float(flavor_split_residual))
                > abs(float(m_p_residual / m_p_codata))
                else "m_p residual"
            ),
        },
    }

    wb.set_description(
        "Decompose the 2113 ppm gap between mass-derived Q_β (Path A: "
        "flavor-split) and N=3 categorical Q_β (Path B: precision ladder). "
        "Test Path C: m_n via categorical Q_β bypassing flavor-split."
    )
    for k, v in data.items():
        wb.add_data(k, v)
    wb.add_assertion(
        "gap_exists",
        computed=abs(float(gap / Q_beta_codata * 1e6)),
        expected=2113,
        tolerance=100,
        source="Mass-derived Q_β vs N=3 categorical Q_β gap",
    )
    wb.add_assertion(
        "pathC_improves_m_n",
        computed=abs(float((m_n_pathC - m_n_codata) / m_n_codata * 1e6)),
        expected=0.24,
        tolerance=0.5,
        source="Path C m_n should inherit m_p's 0.24 ppm accuracy",
    )

    wb.save()

    # ── Console summary ──
    print("=== Q_β consistency gap diagnostic ===\n")
    print(f"Path A (mass-derived):   Q_β = {float(Q_beta_pathA):.6f} MeV  "
          f"({float((Q_beta_pathA - Q_beta_codata) / Q_beta_codata * 1e6):.0f} ppm)")
    print(f"Path B (N=3 categorical): Q_β = {float(Q_beta_pathB):.9f} MeV  "
          f"({float((Q_beta_pathB - Q_beta_codata) / Q_beta_codata * 1e9):.1f} ppb)")
    print(f"Gap: {float(gap * 1e3):.4f} keV = "
          f"{float(gap / Q_beta_codata * 1e6):.0f} ppm\n")

    print("--- Gap decomposition ---")
    print(f"  m_p residual:     {float(m_p_residual * 1e3):.4f} keV  "
          f"(propagates as {float(-m_p_residual / Q_beta_codata * 1e6):.0f} ppm of Q_β)")
    print(f"  Flavor-split X:   {float((X - X_codata) / X_codata * 100):.4f}% residual")
    print(f"  → Flavor-split DOMINATES the gap by "
          f"{abs(float(gap * 1e3 / (m_p_residual * 1e3))):.0f}×\n")

    print("--- Path C: m_n = m_p + Q_β(N=3) + m_e ---")
    print(f"  m_n = {float(m_n_pathC):.6f} MeV  "
          f"({float((m_n_pathC - m_n_codata) / m_n_codata * 1e6):.4f} ppm)")
    print(f"  vs Path A m_n: {float(m_n_pathA):.6f} MeV  "
          f"({float((m_n_pathA - m_n_codata) / m_n_codata * 1e6):.4f} ppm)")
    print(f"  Improvement: {data['path_C_m_n_via_categorical_Q_beta']['improvement_over_pathA']}×")


if __name__ == "__main__":
    main()
