"""
Canonical substrate parameter q — single source of truth.

All witness computations import q from here. When a better
measurement of m_μ/m_e or Vol(4_1) becomes available, update
THIS file and re-run all witnesses.

Derivation:
    ℏ_q² = Vol(4_1) / (m_μ/m_e)
    ℏ_q = 1 - q⁻¹
    q = 1 / (1 - ℏ_q)

Sources:
    Vol(4_1) = 2.029883212819307  (SnapPy 3.3.2, verified)
    m_μ/m_e  = 206.7682830        (CODATA 2022)
"""

import math

# ── Input measurements with uncertainties ────────────────────────
VOL_FIGURE_EIGHT     = 2.029883212819307   # SnapPy 3.3.2 (verified to 15 digits)
VOL_FIGURE_EIGHT_ERR = 1e-12               # numerical precision of SnapPy

MASS_RATIO_MU_E      = 206.7682830         # CODATA 2022
MASS_RATIO_MU_E_ERR  = 0.0000046           # CODATA 2022 uncertainty

# ── Derived substrate parameter ──────────────────────────────────
HBAR_Q_SQ = VOL_FIGURE_EIGHT / MASS_RATIO_MU_E
HBAR_Q    = math.sqrt(HBAR_Q_SQ)
Q         = 1.0 / (1.0 - HBAR_Q)

# ── Uncertainty propagation ──────────────────────────────────────
# q = 1/(1 - sqrt(V/R)) where V = Vol(4_1), R = m_μ/m_e
# dq/dR = q² × sqrt(V/R) / (2R)
# dq/dV = -q² × 1/(2R × sqrt(V/R)) ... but Vol is exact to 1e-12
# Dominant uncertainty comes from CODATA mass ratio:
_dq_dR = Q**2 * math.sqrt(VOL_FIGURE_EIGHT / MASS_RATIO_MU_E) / (2 * MASS_RATIO_MU_E)
Q_ERR  = _dq_dR * MASS_RATIO_MU_E_ERR  # ~ 1.3e-8

# ── Derived constants from q ─────────────────────────────────────
Q_INV     = 1.0 / Q
HA        = Q - Q_INV                        # q - q⁻¹
E_CROSS   = 0.5 * HA                         # crossing energy ½(q - q⁻¹)
S_SKEIN   = math.sqrt(Q) - 1.0/math.sqrt(Q)  # Skein amplitude q^½ - q^{-½}
TWO_Q     = Q + Q_INV                        # [2]_q = q + q⁻¹
TANH_LN_Q = HA / TWO_Q                      # tanh(ln q)

def q_int(n):
    """Quantum integer [n]_q = (q^n - q^{-n}) / (q - q^{-1})."""
    return (Q**n - Q_INV**n) / HA

# ── Error propagation for derived constants ──────────────────────
# All errors are δX = |dX/dq| × Q_ERR
Q_INV_ERR     = Q_ERR / Q**2
HA_ERR        = Q_ERR * (1 + Q_INV**2)          # d(q-q⁻¹)/dq = 1+q⁻²
E_CROSS_ERR   = 0.5 * HA_ERR
S_SKEIN_ERR   = Q_ERR * 0.5 * (Q**(-0.5) + Q**(-1.5))
TWO_Q_ERR     = Q_ERR * abs(1 - Q_INV**2)
TANH_LN_Q_ERR = Q_ERR * 2.0 / TWO_Q**2         # d(tanh)/dq

def q_int_err(n):
    """Uncertainty in [n]_q from Q_ERR."""
    # d[n]_q/dq = (n q^{n-1} + n q^{-n-1}) / (q-q⁻¹)
    #           - (q^n - q^{-n})(1+q⁻²) / (q-q⁻¹)²
    num_deriv = n * (Q**(n-1) + Q_INV**(n+1))
    denom_corr = (Q**n - Q_INV**n) * (1 + Q_INV**2) / HA
    return abs(num_deriv / HA - denom_corr / HA) * Q_ERR

# ── For hecke_engine (exact rational arithmetic) ─────────────────
# The engine uses Fraction(p_num, p_den) where q = p_num/p_den.
# We provide the best rational approximation at the engine's precision.
# 11099786 / 10000000 gives q to 7 significant figures.
Q_RAT_NUM = 11099786
Q_RAT_DEN = 10000000

if __name__ == "__main__":
    print(f"Substrate parameter q (canonical)")
    print(f"  Vol(4_1)   = {VOL_FIGURE_EIGHT} ± {VOL_FIGURE_EIGHT_ERR}")
    print(f"  m_μ/m_e    = {MASS_RATIO_MU_E} ± {MASS_RATIO_MU_E_ERR}")
    print(f"  ℏ_q²       = {HBAR_Q_SQ:.15f}")
    print(f"  ℏ_q        = {HBAR_Q:.15f}")
    print(f"  q          = {Q:.15f} ± {Q_ERR:.2e}")
    print(f"  q⁻¹        = {Q_INV:.15f} ± {Q_INV_ERR:.2e}")
    print(f"  q - q⁻¹    = {HA:.15f} ± {HA_ERR:.2e}")
    print(f"  E_×        = {E_CROSS:.15f} ± {E_CROSS_ERR:.2e}")
    print(f"  s          = {S_SKEIN:.15f} ± {S_SKEIN_ERR:.2e}")
    print(f"  [2]_q      = {TWO_Q:.15f} ± {TWO_Q_ERR:.2e}")
    print(f"  tanh(ln q) = {TANH_LN_Q:.15f} ± {TANH_LN_Q_ERR:.2e}")
    print(f"  [9]_q      = {q_int(9):.10f} ± {q_int_err(9):.2e}")
    print(f"  [10]_q     = {q_int(10):.10f} ± {q_int_err(10):.2e}")
    alpha = Q_INV / (q_int(9) * q_int(10))
    inv_alpha = 1.0 / alpha
    # α error: dα/dq involves all three factors
    alpha_err = alpha * math.sqrt((Q_INV_ERR/Q_INV)**2
                                  + (q_int_err(9)/q_int(9))**2
                                  + (q_int_err(10)/q_int(10))**2)
    print(f"  α          = {alpha:.10f} ± {alpha_err:.2e}")
    print(f"  1/α        = {inv_alpha:.6f} ± {inv_alpha**2 * alpha_err:.4f}")
    print(f"  CODATA 1/α = 137.035999084 ± 0.000000021")
    print(f"  Rational:    {Q_RAT_NUM}/{Q_RAT_DEN}")
