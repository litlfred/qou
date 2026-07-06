"""
Canonical substrate parameter q for Sage scripts.

Load in any .sage file with:
    load("computations/q_parameter.sage")

Sources:
    Vol(4_1) = 2.029883212819307  (SnapPy 3.3.2)
    m_μ/m_e  = 206.7682830        (CODATA 2022)
"""

VOL_FIGURE_EIGHT = 2.029883212819307
MASS_RATIO_MU_E  = 206.7682830
HBAR_Q_SQ = VOL_FIGURE_EIGHT / MASS_RATIO_MU_E
HBAR_Q    = sqrt(HBAR_Q_SQ)
q_num     = 1.0 / (1.0 - HBAR_Q)  # = 1.109978595554181
