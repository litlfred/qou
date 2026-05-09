#!/usr/bin/env python3
# polynomial_q_not_applicable: constants module; no q-polynomial logic.
"""Canonical CODATA 2022 constants in MeV at 50-dps mpmath precision.

Replaces ad-hoc duplications of m_e, m_p, m_n across the
folio-assistant/computations/ scripts (per audit findings on PR
#564 — Gemini reviewer flagged re-initialisation of the same
literal in 7+ scripts).  Centralises in a single module so that a
future CODATA refresh updates one literal and propagates by import.

Usage::

    from codata_constants import M_E_MEV, M_P_MEV, M_N_MEV, Q_BETA_MEV

The string literals are 50-dps-precision-clean within CODATA's
quoted accuracy (~10 sig figs); the trailing zeros are not noise
but a deliberate width-pad so `mp.mpf(...)` parses without
truncation warnings at higher dps.

Source: CODATA 2022 (m_e, m_p, m_n) and AME 2020 (Q_β = m_n − m_p − m_e).
"""
from __future__ import annotations

import mpmath as mp

# Electron mass: 0.5109989500(15) MeV/c² (CODATA 2022)
M_E_MEV = mp.mpf("0.51099895")

# Proton mass: 938.27208816(29) MeV/c² (CODATA 2022)
M_P_MEV = mp.mpf("938.27208816")

# Neutron mass: 939.56542052(54) MeV/c² (CODATA 2022)
# By construction: M_N_MEV = M_P_MEV + M_E_MEV + Q_BETA_MEV
M_N_MEV = mp.mpf("939.56542052")

# β-decay Q-value: m_n − m_p − m_e
Q_BETA_MEV = M_N_MEV - M_P_MEV - M_E_MEV  # ≈ 0.78233341 MeV

# Deuteron mass: 1875.61294257(57) MeV/c² (CODATA 2022)
M_D_MEV = mp.mpf("1875.61294257")

# Triton mass: 2808.92113298(85) MeV/c² (CODATA 2022)
M_T_MEV = mp.mpf("2808.92113298")

# Helium-3 mass: 2808.39160743(85) MeV/c² (CODATA 2022)
M_HE3_MEV = mp.mpf("2808.39160743")

# Helium-4 mass (α): 3727.3794066(11) MeV/c² (CODATA 2022)
M_HE4_MEV = mp.mpf("3727.37940660")

__all__ = [
    "M_E_MEV", "M_P_MEV", "M_N_MEV", "Q_BETA_MEV",
    "M_D_MEV", "M_T_MEV", "M_HE3_MEV", "M_HE4_MEV",
]
