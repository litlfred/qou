#!/usr/bin/env python3
"""
Symbolic hadron mass derivation from the substrate parameter q.

Keeps q symbolic as long as possible using sympy, then evaluates
at q₀ derived from CODATA.  The full chain:

    Vol(4_1), m_μ/m_e  →  ℏ_q  →  q  →  HA, E_×  →  transfer matrices
    →  V̂_i(q)  →  P_p(q), P_n(q)  →  m_p(q), m_n(q)

Crossing coefficients for A=3 (proton/neutron):
    uu → (c=1, d=0)
    dd → (c=q², d=-q·s)   where s = q^{1/2} - q^{-1/2}
    ud → (c=(1+q²)/2, d=-q·s/2)

Transfer matrix:
    T(c,d) = [[c·HA + d,  c],
              [c,          d]]     where HA = q - q⁻¹

Markov-traced volume at generator σ_i:
    V̂_i = z·M[0,0] + M[1,0]      where z = 1/(√q + 1/√q)

Skein polynomial:
    P_N(q) = ∏_i V̂_i(q)

Mass:
    𝔪(N) = P_N(q) · 𝔪_e          where 𝔪_e is the electron mass scale

Usage:
    cd folio-assistant/computations
    python3 mass-from-q-symbolic.py

References:
    [kock2004] https://doi.org/10.1017/CBO9780511615443
    [jones1985] https://doi.org/10.1090/S0273-0979-1985-15304-2
"""

import sys
import os

import sympy as sp
from sympy import sqrt, Rational, simplify, expand, factor, Matrix, latex

# ── Import numerical values from canonical sources ───────────────
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from q_parameter import (
    VOL_FIGURE_EIGHT, MASS_RATIO_MU_E,
    Q as Q0, HBAR_Q as HBAR_Q0, HBAR_Q_SQ as HBAR_Q_SQ0,
    HA as HA0, E_CROSS as E_CROSS0, S_SKEIN as S_SKEIN0,
)
from experimental_constants import M_E_MEV, M_P_MEV, M_N_MEV


# ═══════════════════════════════════════════════════════════════════
# §1  SYMBOLIC SETUP
# ═══════════════════════════════════════════════════════════════════

q = sp.Symbol('q', positive=True)
q_inv = 1 / q
q_half = sqrt(q)
q_half_inv = 1 / sqrt(q)

# Fundamental symbolic quantities
hbar_q = 1 - q_inv                          # ℏ_q = 1 - q⁻¹
HA = q - q_inv                              # Hecke amplitude
s = q_half - q_half_inv                     # Skein amplitude
z = 1 / (q_half + q_half_inv)              # Markov parameter
E_cross = HA / 2                            # Crossing energy

# Symbolic Vol(4_1) and m_μ/m_e (kept as symbols for display)
V41 = sp.Symbol('V_{4_1}', positive=True)
R_mu_e = sp.Symbol('R_{\\mu/e}', positive=True)

# The defining relation: R_mu_e = V41 / hbar_q^2
# => hbar_q^2 = V41 / R_mu_e
# => hbar_q = sqrt(V41 / R_mu_e)
# => q = 1 / (1 - sqrt(V41 / R_mu_e))
hbar_q_from_data = sp.sqrt(V41 / R_mu_e)
q_from_data = 1 / (1 - hbar_q_from_data)


# ═══════════════════════════════════════════════════════════════════
# §2  TRANSFER MATRIX CONSTRUCTION (symbolic in q)
# ═══════════════════════════════════════════════════════════════════

def symbolic_transfer_matrix(c, d):
    """Build the 2x2 transfer matrix T(c,d) symbolically.

    T(c,d) = [[c·(q - q⁻¹) + d,  c],
              [c,                  d]]
    """
    return Matrix([
        [expand(c * HA + d), c],
        [c,                  d],
    ])


def markov_traced_volume(M):
    """Markov-traced volume: V̂ = z·M[0,0] + M[1,0]."""
    return expand(z * M[0, 0] + M[1, 0])


# Crossing coefficients for quark types (u = proton-like, d = neutron-like)
# These map directly to the nuclear crossing types:
#   uu ↔ pp:  c = 1,           d = 0
#   dd ↔ nn:  c = q²,          d = -q·s
#   ud ↔ mix: c = (1+q²)/2,    d = -q·s/2

CROSSING_COEFFS = {
    ('u', 'u'): (sp.Integer(1), sp.Integer(0)),
    ('d', 'd'): (q**2, -q * s),
    ('u', 'd'): ((1 + q**2) / 2, -q * s / 2),
    ('d', 'u'): ((1 + q**2) / 2, -q * s / 2),
}


def build_generator_volume(i, ordering):
    """Compute V̂_i(q) for generator σ_i in a baryon with given quark ordering.

    For A quarks, generator σ_i interacts quark i with quarks i+1, ..., A-1.
    The transfer matrix at σ_i is M_i = ∏_{j=i+1}^{A-1} T(c_{ij}, d_{ij}).
    The traced volume is V̂_i = z·M_i[0,0] + M_i[1,0].
    """
    A = len(ordering)
    M = sp.eye(2)
    for j in range(i + 1, A):
        c, d = CROSSING_COEFFS[(ordering[i], ordering[j])]
        T = symbolic_transfer_matrix(c, d)
        M = M * T
    return markov_traced_volume(M), M


def build_skein_polynomial(ordering, name=""):
    """Build P_N(q) = ∏_i V̂_i(q) for a baryon with given quark ordering.

    Returns (volumes_list, P_N_symbolic, name).
    """
    A = len(ordering)
    volumes = []
    P = sp.Integer(1)
    for i in range(A - 1):
        V_i, _ = build_generator_volume(i, ordering)
        V_i = simplify(V_i)
        volumes.append(V_i)
        P = expand(P * V_i)
    return volumes, P, name


# ═══════════════════════════════════════════════════════════════════
# §3  PROTON AND NEUTRON
# ═══════════════════════════════════════════════════════════════════

# Proton: uud (Z=2 up quarks, N=1 down quark)
proton_ordering = ['u', 'u', 'd']
proton_vols, P_proton, _ = build_skein_polynomial(proton_ordering, "proton")

# Neutron: udd (Z=1 up quark, N=2 down quarks)
neutron_ordering = ['u', 'd', 'd']
neutron_vols, P_neutron, _ = build_skein_polynomial(neutron_ordering, "neutron")


# ═══════════════════════════════════════════════════════════════════
# §4  DISPLAY SYMBOLIC RESULTS
# ═══════════════════════════════════════════════════════════════════

def fmt_sym(expr):
    """Format a sympy expression for display, simplifying."""
    return simplify(expr)


print("=" * 72)
print("SYMBOLIC MASS DERIVATION FROM SUBSTRATE PARAMETER q")
print("=" * 72)

# ── Step 1: q from CODATA ─────────────────────────────────────────

print()
print("─── Step 1: Substrate parameter q from CODATA ───")
print()
print("  Defining relation:")
print(f"    m_μ/m_e = Vol(4_1) / ℏ_q²")
print(f"    ℏ_q = 1 - q⁻¹")
print(f"    ⟹  q = 1 / (1 - √(Vol(4_1) / (m_μ/m_e)))")
print()
print(f"  Inputs:")
print(f"    Vol(4_1)  = {VOL_FIGURE_EIGHT}")
print(f"    m_μ/m_e   = {MASS_RATIO_MU_E} (CODATA 2022)")
print()
print(f"  Derived:")
print(f"    ℏ_q²      ≈ {HBAR_Q_SQ0:.15f}")
print(f"    ℏ_q       ≈ {HBAR_Q0:.15f}")
print(f"    q₀        ≈ {Q0:.15f}")

# ── Step 2: Fundamental quantities ────────────────────────────────

print()
print("─── Step 2: Fundamental quantities (symbolic in q) ───")
print()
print(f"    ℏ_q         = 1 - 1/q")
print(f"    HA          = q - 1/q")
print(f"    s           = √q - 1/√q")
print(f"    z           = 1/(√q + 1/√q)")
print(f"    E_×         = HA/2 = (q - 1/q)/2")
print()
print(f"  At q₀:")
print(f"    HA(q₀)      ≈ {HA0:.15f}")
print(f"    s(q₀)       ≈ {S_SKEIN0:.15f}")
print(f"    E_×(q₀)     ≈ {E_CROSS0:.15f}")

# ── Step 3: Transfer matrices ─────────────────────────────────────

print()
print("─── Step 3: Crossing coefficients and transfer matrices ───")
print()
print("  Quark crossing types:")
print("    uu: c = 1,           d = 0")
print("    dd: c = q²,          d = -q·s = -q·(√q - 1/√q)")
print("    ud: c = (1+q²)/2,    d = -q·s/2")
print()
print("  Transfer matrix T(c,d):")
print("    [[c·(q - q⁻¹) + d,   c],")
print("     [c,                  d]]")

# ── Step 4: Per-generator volumes ─────────────────────────────────

print()
print("─── Step 4: Per-generator traced volumes V̂_i(q) ───")
print()

print("  PROTON (uud):  ordering = [u, u, d]")
print("  ────────────")
for i, V in enumerate(proton_vols):
    V_simplified = fmt_sym(V)
    V_num = float(V.subs(q, Q0))
    print(f"    V̂_{i}(q) = {V_simplified}")
    print(f"    V̂_{i}(q₀) ≈ {V_num:.10f}")
    print()

print("  NEUTRON (udd):  ordering = [u, d, d]")
print("  ──────────────")
for i, V in enumerate(neutron_vols):
    V_simplified = fmt_sym(V)
    V_num = float(V.subs(q, Q0))
    print(f"    V̂_{i}(q) = {V_simplified}")
    print(f"    V̂_{i}(q₀) ≈ {V_num:.10f}")
    print()

# ── Step 5: Skein polynomials ─────────────────────────────────────

print()
print("─── Step 5: Skein polynomials P(q) = ∏ V̂_i(q) ───")
print()

P_p_simplified = fmt_sym(P_proton)
P_n_simplified = fmt_sym(P_neutron)

print(f"  P_proton(q) = {P_p_simplified}")
print()
print(f"  P_neutron(q) = {P_n_simplified}")
print()

P_p_num = float(P_proton.subs(q, Q0))
P_n_num = float(P_neutron.subs(q, Q0))

print(f"  P_proton(q₀)  ≈ {P_p_num:.10f}")
print(f"  P_neutron(q₀) ≈ {P_n_num:.10f}")
print(f"  P_n/P_p       ≈ {P_n_num / P_p_num:.10f}")

# ── Step 6: Symbolic ratio P_n / P_p ─────────────────────────────

print()
print("─── Step 6: Neutron-to-proton Skein ratio ───")
print()

ratio_sym = simplify(P_neutron / P_proton)
print(f"  P_n(q)/P_p(q) = {ratio_sym}")
print()

ratio_factored = factor(P_neutron) / factor(P_proton)
print(f"  Factored form:")
print(f"    P_n(q) = {factor(P_neutron)}")
print(f"    P_p(q) = {factor(P_proton)}")

# ── Step 7: Mass predictions ──────────────────────────────────────

print()
print("=" * 72)
print("MASS PREDICTIONS (numerical evaluation at q₀)")
print("=" * 72)
print()

# The mass scale: m_e sets the unit.
# In the transfer matrix formalism, the Skein polynomial P_N(q) gives
# the mass ratio m_N / m_e (modulo the Borromean volume factor).
#
# More precisely:
#   m_p = P_proton(q) × (Vol(B_3) / ℏ_q²) × m_e_scale
# where Vol(B_3) = 7.32772... is the Borromean link volume
# and m_e_scale converts from natural units to MeV.
#
# But since we're computing RATIOS, the scale cancels and we need:
#   m_p/m_e ≈ P_p(q₀) × Vol(B_3) / ℏ_q²

VOL_BORROMEAN = 7.327724753846269  # SnapPy: Vol(Borromean rings)

# Mass ratio via Borromean volume + Skein polynomial
borromean_mass_unit = VOL_BORROMEAN / HBAR_Q_SQ0  # ≈ in electron mass units

print("  Mass derivation chain:")
print(f"    Vol(𝔅₃) = {VOL_BORROMEAN} (Borromean link volume)")
print(f"    ℏ_q²    ≈ {HBAR_Q_SQ0:.15f}")
print(f"    Vol(𝔅₃)/ℏ_q² ≈ {borromean_mass_unit:.6f} (Borromean mass in electron units)")
print()

# The proton/neutron masses from the Skein polynomial:
# m_N = |P_N(q₀)| × m_e (MeV)
# where P_N already encodes the Borromean volume via the transfer matrix crossings.

# The transfer matrix product P_N(q) IS the full mass ratio m_N/m_e
# when the crossing coefficients encode the Borromean linking geometry.
# This follows from the terminal resolution (Prop. terminal-resolution).

m_p_pred = abs(P_p_num) * M_E_MEV
m_n_pred = abs(P_n_num) * M_E_MEV

print("  Direct Skein polynomial masses:")
print(f"    m_p(q₀) = |P_p(q₀)| × m_e")
print(f"            ≈ {abs(P_p_num):.6f} × {M_E_MEV} MeV")
print(f"            ≈ {m_p_pred:.3f} MeV")
print(f"    m_p(exp)≈ {M_P_MEV:.3f} MeV")
print(f"    ratio    ≈ {m_p_pred / M_P_MEV:.6f}")
print()
print(f"    m_n(q₀) = |P_n(q₀)| × m_e")
print(f"            ≈ {abs(P_n_num):.6f} × {M_E_MEV} MeV")
print(f"            ≈ {m_n_pred:.3f} MeV")
print(f"    m_n(exp)≈ {M_N_MEV:.3f} MeV")
print(f"    ratio    ≈ {m_n_pred / M_N_MEV:.6f}")
print()

# Neutron-proton mass difference
delta_m_pred = m_n_pred - m_p_pred
delta_m_exp = M_N_MEV - M_P_MEV
print(f"  Neutron-proton mass difference:")
print(f"    Δm(q₀) = m_n - m_p ≈ {delta_m_pred:.3f} MeV")
print(f"    Δm(exp)              ≈ {delta_m_exp:.3f} MeV")
print(f"    ratio                ≈ {delta_m_pred / delta_m_exp:.4f}")
print()

# Mass ratio m_n / m_p
print(f"  Mass ratio m_n/m_p:")
print(f"    Predicted ≈ {abs(P_n_num) / abs(P_p_num):.10f}")
print(f"    CODATA    ≈ {M_N_MEV / M_P_MEV:.10f}")

# ── Step 8: LaTeX-ready symbolic expressions ──────────────────────

print()
print("=" * 72)
print("LaTeX EXPRESSIONS (for paper)")
print("=" * 72)
print()
print("  Proton Skein polynomial:")
print(f"    $P_{{\\mathfrak{{p}}}}(q) = {latex(P_p_simplified)}$")
print()
print("  Neutron Skein polynomial:")
print(f"    $P_{{\\mathfrak{{n}}}}(q) = {latex(P_n_simplified)}$")
print()
print("  Per-generator volumes (proton):")
for i, V in enumerate(proton_vols):
    print(f"    $\\hat{{V}}_{i}^{{\\mathfrak{{p}}}}(q) = {latex(fmt_sym(V))}$")
print()
print("  Per-generator volumes (neutron):")
for i, V in enumerate(neutron_vols):
    print(f"    $\\hat{{V}}_{i}^{{\\mathfrak{{n}}}}(q) = {latex(fmt_sym(V))}$")


# ═══════════════════════════════════════════════════════════════════
# §5  FULL DERIVATION CHAIN SUMMARY
# ═══════════════════════════════════════════════════════════════════

print()
print("=" * 72)
print("FULL DERIVATION CHAIN: Vol(4_1) + m_μ/m_e → hadron masses")
print("=" * 72)
print()
print("  (1)  ℏ_q² = Vol(4_1) / (m_μ/m_e)")
print(f"       ≈ {VOL_FIGURE_EIGHT} / {MASS_RATIO_MU_E}")
print(f"       ≈ {HBAR_Q_SQ0:.15f}")
print()
print("  (2)  ℏ_q = √(ℏ_q²)")
print(f"       ≈ {HBAR_Q0:.15f}")
print()
print("  (3)  q = 1 / (1 - ℏ_q)")
print(f"       ≈ {Q0:.15f}")
print()
print(f"  (4)  HA = q - q⁻¹ ≈ {HA0:.15f}")
print(f"       E_× = HA/2   ≈ {E_CROSS0:.15f}")
print(f"       s = √q-1/√q  ≈ {S_SKEIN0:.15f}")
print()
print(f"  (5)  Proton (uud): P_p(q₀) ≈ {P_p_num:.10f}")
print(f"       Neutron (udd): P_n(q₀) ≈ {P_n_num:.10f}")
print()
print(f"  (6)  𝔪_p(q₀) = |P_p(q₀)| × m_e ≈ {m_p_pred:.3f} MeV")
print(f"       𝔪_n(q₀) = |P_n(q₀)| × m_e ≈ {m_n_pred:.3f} MeV")
print()
print(f"  (7)  Experimental comparison (CODATA 2022):")
print(f"       m_p ≈ {M_P_MEV:.6f} MeV    (pred/exp ≈ {m_p_pred/M_P_MEV:.6f})")
print(f"       m_n ≈ {M_N_MEV:.6f} MeV    (pred/exp ≈ {m_n_pred/M_N_MEV:.6f})")
print()
print("  NOTE: All derived values use ≈, never =.")
print("  Exact algebraic identities (ℏ_q = 1 - 1/q, etc.) use =.")
