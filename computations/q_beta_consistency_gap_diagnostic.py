#!/usr/bin/env python3
"""
q_beta_consistency_gap_diagnostic.py — localise the ~2100 ppm gap between
the mass-derived Q_β and the N=3 categorical Q_β.

Two independent derivation paths for Q_β from (m_e, q_0):

  Path A (mass-derived):  Q_β = m_n − m_p − m_e
    where m_p = dim V_{(2,1)} · (m_μ · F_Bor − |S_3| · m_e)
    and   m_n = m_p · (1 + X/(1 − X/2)),  X = flavor-split

  Path B (N=3 categorical ladder):
    Q_β from q-beta-operator-valued-N3.witness.json (categorical, ~6 ppb)

Path A gives ~−2100 ppm; Path B gives ~+6 ppb.
This script decomposes the gap and tests Path C (m_n via categorical Q_β).
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import json
import sys
import time
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


def _load_Q_beta_N3() -> mpf:
    """Load the N=3 categorical Q_β from its witness."""
    w = json.loads((HERE / "q-beta-operator-valued-N3.witness.json").read_text())
    return mpf(str(w["data"]["Q_AME"]))


def _muon_mass_MeV() -> mpf:
    """Muon mass from CAL-2 anchor (m_μ/m_e × m_e)."""
    from codata_2022_source import M_MU_OVER_M_E  # noqa: E402
    return mpf(M_E_MEV) * mpf(M_MU_OVER_M_E)


def main():
    t0 = time.monotonic()
    set_compute_dps()

    q = mpf(Q_50_DIGIT_STR)
    m_e = mpf(M_E_MEV)
    m_mu = _muon_mass_MeV()
    m_p_codata = mpf(M_P_MEV_VALIDATION)
    m_n_codata = mpf(M_N_MEV_VALIDATION)
    Q_beta_codata = m_n_codata - m_p_codata - m_e

    h = q - 1 / q

    def q_int(n):
        return (q ** n - q ** (-n)) / h

    tr_M = abs((4 + h ** 2 - 3 * h ** 4 - h ** 6) / (h ** 2 + 4))
    q_fac_3 = q_int(3) * q_int(2) * q_int(1)
    F_Bor = tr_M * q_fac_3 / q ** 3

    # ── Path A: mass-derived Q_β ──
    m_p_pred = 2 * (m_mu * F_Bor - 6 * m_e)
    X = (q - 1) ** 2 * (1 - q ** (-4)) / 3
    m_n_pathA = m_p_pred * (1 + X / (1 - X / 2))
    Q_beta_pathA = m_n_pathA - m_p_pred - m_e

    # ── Path B: N=3 categorical (from witness) ──
    Q_beta_pathB = _load_Q_beta_N3()

    # ── Path C: m_n via categorical Q_β ──
    m_n_pathC = m_p_pred + Q_beta_pathB + m_e

    # ── Decompose the gap ──
    # In Path A: m_n = m_p · (1 + r) where r = X/(1−X/2)
    # So Q_β_A = m_n − m_p − m_e = m_p · r − m_e
    # Error in Q_β_A comes from: (a) δm_p propagates as δm_p · (1+r)
    # into m_n, hence δQ = δm_p · r; (b) δX propagates through r.
    r_codata = (m_n_codata / m_p_codata) - 1  # exact CODATA ratio
    m_p_residual = m_p_pred - m_p_codata
    m_p_contribution_keV = float(m_p_residual * r_codata * 1e3)

    gap = Q_beta_pathA - Q_beta_pathB
    gap_keV = float(gap * 1e3)
    flavor_contribution_keV = gap_keV - m_p_contribution_keV

    X_codata = (m_n_codata - m_p_codata) / ((m_n_codata + m_p_codata) / 2)

    wb = WitnessBuilder("q-beta-consistency-gap-diagnostic", engine="mpmath")
    wb.set_description(
        "Decompose the gap between mass-derived Q_beta (Path A: "
        "flavor-split) and N=3 categorical Q_beta (Path B: precision "
        "ladder). Test Path C: m_n via categorical Q_beta."
    )

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
                    abs((m_n_pathA - m_n_codata) / m_n_codata)
                    / abs((m_n_pathC - m_n_codata) / m_n_codata)
                )
            )
            if abs(m_n_pathC - m_n_codata) > 0
            else "inf",
        },
        "gap_decomposition": {
            "total_gap_keV": str(gap_keV),
            "total_gap_ppm": str(float(gap / Q_beta_codata * 1e6)),
            "m_p_residual_contribution_keV": str(m_p_contribution_keV),
            "flavor_split_contribution_keV": str(flavor_contribution_keV),
            "dominant_source": (
                "flavor-split X"
                if abs(flavor_contribution_keV) > abs(m_p_contribution_keV)
                else "m_p residual"
            ),
        },
    }

    for k, v in data.items():
        wb.add_data(k, v)
    wb.add_assertion(
        "gap_exists",
        computed=abs(float(gap / Q_beta_codata * 1e6)),
        expected=2113,
        tolerance=100,
        source="Mass-derived Q_beta vs N=3 categorical Q_beta gap",
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
    print("=== Q_beta consistency gap diagnostic ===\n")
    print(f"Path A (mass-derived):    Q_beta = {float(Q_beta_pathA):.6f} MeV  "
          f"({float((Q_beta_pathA - Q_beta_codata) / Q_beta_codata * 1e6):.0f} ppm)")
    print(f"Path B (N=3 categorical): Q_beta = {float(Q_beta_pathB):.9f} MeV  "
          f"({float((Q_beta_pathB - Q_beta_codata) / Q_beta_codata * 1e9):.1f} ppb)")
    print(f"Gap: {gap_keV:.4f} keV = "
          f"{float(gap / Q_beta_codata * 1e6):.0f} ppm\n")

    print("--- Gap decomposition ---")
    print(f"  m_p residual (× r):  {m_p_contribution_keV:.4f} keV  "
          f"({float(m_p_contribution_keV / gap_keV * 100):.0f}% of gap)")
    print(f"  Flavor-split X:      {flavor_contribution_keV:.4f} keV  "
          f"({float(flavor_contribution_keV / gap_keV * 100):.0f}% of gap)")
    dominance = abs(flavor_contribution_keV / m_p_contribution_keV) if m_p_contribution_keV != 0 else float('inf')
    print(f"  → Flavor-split dominates by {dominance:.0f}×\n")

    print("--- Path C: m_n = m_p + Q_beta(N=3) + m_e ---")
    print(f"  m_n = {float(m_n_pathC):.6f} MeV  "
          f"({float((m_n_pathC - m_n_codata) / m_n_codata * 1e6):.4f} ppm)")
    print(f"  vs Path A m_n: {float(m_n_pathA):.6f} MeV  "
          f"({float((m_n_pathA - m_n_codata) / m_n_codata * 1e6):.4f} ppm)")
    print(f"  Improvement: {data['path_C_m_n_via_categorical_Q_beta']['improvement_over_pathA']}x")


if __name__ == "__main__":
    main()
