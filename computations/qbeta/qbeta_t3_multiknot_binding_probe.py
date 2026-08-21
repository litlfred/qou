#!/usr/bin/env python3
"""
T3 MULTI-KNOT PROBE: Compute S_K = A_ω · κ_K · (ln²q₀ − ϑ_K²) for different knots.

Particle-knot assignments from the QOU manuscript:
  electron  → trefoil 3₁ (torus knot, Vol = 0, non-hyperbolic)
  muon      → figure-eight 4₁ (hyperbolic, Vol = 2.02988)
  proton    → Borromean baryon 𝔹₃ (3-component hyperbolic link, Vol = 7.32772)
  neutron   → Borromean baryon 𝔹₃ (same topology, different Hecke coefficients)

Key data:
  - cusp modulus κ_K = Im(τ_K)/4 where τ_K is the cusp shape parameter
  - A_ω is the GGM Stokes constant (knot-dependent integer)
  - ϑ_K is the angular deformation on the character variety (particle-specific)

For 4₁: τ = -i√3, κ = √3/4, A_ω = 3 (GGM)
For 3₁: torus knot — cusp shape τ = 6i, κ = 6/4 = 3/2... but non-hyperbolic
For 𝔹₃: τ_cusp ≈ -0.5 + i√3/2 (per-component), Vol = 7.32772
"""

import math
import cmath
import sys
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from qbeta_t4_anchors import theta_t4, q0 as _q0_canonical  # noqa: E402

# =============================================================
# Physical constants -- READ from the registry, never typed, exactly as the
# substrate q0 below already is (bean qou-vbw1). This block was honestly
# labelled "(CODATA 2018)" and carried the 2018 values while the rest of the
# corpus is on 2022; reading codata_constants removes both the transcription
# and the edition question. Drain qou-7ot6-a.
# =============================================================
from codata_constants import (  # noqa: E402
    M_E_MEV as _M_E_MEV,
    M_MU_MEV_VALIDATION as _M_MU_MEV,
    M_P_MEV_VALIDATION as _M_P_MEV,
    M_N_MEV_VALIDATION as _M_N_MEV,
)

m_e = float(_M_E_MEV)     # was 0.51099895000 (truncated)
m_mu = float(_M_MU_MEV)   # was 105.6583745   (CODATA-2018)
m_p = float(_M_P_MEV)     # was 938.27208816  (CODATA-2018)
m_n = float(_M_N_MEV)     # was 939.56542052  (CODATA-2018)

# Substrate — READ from the canonical constant, never typed (bean qou-vbw1).
# The former literal `1.10997859` was an 8-digit truncation; the substrate
# quantities below are carried in mpmath and narrowed to float only at the
# print boundary. (The CODATA masses and the ratio prints further down remain
# float64 display arithmetic — out of scope for this bean, worth its own pass.)
mp.mp.dps = 50
q0 = _q0_canonical()
ln_q0 = mp.log(q0)

print("=" * 70)
print("T3 MULTI-KNOT BINDING PROBE")
print("=" * 70)
print(f"\nSubstrate q₀ = {mp.nstr(q0, 20)}  (canonical proton pin, read not typed)")
print(f"ln q₀ = {mp.nstr(ln_q0, 10)}")
print(f"ln²q₀ = {mp.nstr(ln_q0**2, 12)}")
print()

# =============================================================
# 1. FIGURE-EIGHT KNOT 4₁ (muon carrier)
# =============================================================
print("─" * 70)
print("1. FIGURE-EIGHT KNOT 4₁  (muon)")
print("─" * 70)

# Cusp shape τ₄₁ = -i√3 (i.e. purely imaginary, modulus √3)
# In the conventions: Im V₄₁(u) = (√3/4)(Re²u - Im²u)
# cusp modulus κ₄₁ = √3/4
tau_41 = complex(0, -math.sqrt(3))
kappa_41 = mp.sqrt(3) / 4
Vol_41 = 2.0298832128

# GGM Stokes constant for 4₁
A_omega_41 = 3  # Integer, from Garoufalidis-Gu-Mariño

print(f"  τ₄₁ = {tau_41}")
print(f"  κ₄₁ = √3/4 = {mp.nstr(kappa_41, 10)}")
print(f"  Vol(4₁) = {Vol_41:.10f}")
print(f"  A_ω(4₁) = {A_omega_41}")
print()

# Scan: what ϑ gives S consistent with muon mass binding?
# S_muon is a small correction. From the probe:
# The binding formula: S = A_ω · κ · (ln²q₀ - ϑ²)
# This is the NZ-deformation contribution to the mass correction.

# From the T4 inversion — DERIVED from the canonical q₀, not typed (qou-vbw1).
# These are A_ω-CONDITIONED readings: they invert the channel at A_ω = 3, which
# is imported from GGM and not derived here. Round-tripping them back through
# the same channel (below) recovers the measured S by construction — that is a
# consistency check, NOT evidence for A_ω = 3.
theta_muon_T4 = theta_t4("muon")
theta_proton_T4 = theta_t4("proton")

S_muon_T4 = A_omega_41 * kappa_41 * (ln_q0**2 - theta_muon_T4**2)
S_proton_T4 = A_omega_41 * kappa_41 * (ln_q0**2 - theta_proton_T4**2)

print(f"  T4-inverted values (derived at canonical q₀; A_ω-conditioned):")
print(f"    ϑ(muon)   = {mp.nstr(theta_muon_T4, 10)} rad")
print(f"    ϑ(proton) = {mp.nstr(theta_proton_T4, 10)} rad")
print(f"    S(muon)   = {mp.nstr(S_muon_T4, 10)}   [round-trip of the input]")
print(f"    S(proton) = {mp.nstr(S_proton_T4, 10)}   [round-trip of the input]")
print(f"    S(p)/S(μ) = {mp.nstr(S_proton_T4/S_muon_T4, 8)}")
print()

# Cusp lattice values (geodesic winding classes):
print(f"  Cusp lattice unit: √3/2 · ln q₀ = {mp.nstr(mp.sqrt(3)/2*ln_q0, 10)}")
print()
print(f"  {'(m,ℓ)':<10} {'ϑ':>10} {'G':>6} {'S':>12} {'particle?':>15}")
print(f"  {'-'*55}")
interesting = [
    (1, 0, "meridian"),
    (0, 1, "longitude"),
    (-1, 1, ""),
    (1, 1, ""),
    (-1, 2, ""),
    (0, 2, ""),
]
for m, ell, label in interesting:
    theta_lat = ell * mp.sqrt(3)/2 * ln_q0
    G = (2*m + ell)**2 - 3*ell**2
    S = A_omega_41 * (mp.sqrt(3)/16) * ln_q0**2 * G
    print(f"  ({m},{ell}){'':<5} {mp.nstr(theta_lat, 8):>10} {G:>+6d} "
          f"{mp.nstr(S, 8):>13} {label:>15}")

# =============================================================
# 2. TREFOIL KNOT 3₁ (electron carrier)
# =============================================================
print()
print("─" * 70)
print("2. TREFOIL KNOT 3₁  (electron)")
print("─" * 70)

# The trefoil is a TORUS KNOT — NOT hyperbolic.
# Vol(3₁) = 0. The complement is Seifert-fibred.
# Cusp shape: τ₃₁ = 6i (standard framing) or 6 (depending on convention)
# The cusp torus has shape parameter with |τ| = 6.
#
# Key question: does the binding formula still apply?
# For torus knots, the quantum dilogarithm / resurgence structure
# is different — the Borel plane has singularities at rational
# multiples of 2πi, not at the complex volume.
#
# GGM Stokes constant for 3₁: from the Kashaev invariant
# J_N(3₁; q=e^{2πi/N}) ~ exp(N · 0) × poly(N) — NO exponential growth
# because Vol = 0. The Stokes constant concept doesn't apply directly.

tau_31 = complex(0, 6)
kappa_31 = 6.0 / 4  # = 3/2
Vol_31 = 0.0

print(f"  τ₃₁ = {tau_31}")
print(f"  κ₃₁ = 6/4 = {kappa_31:.4f}")
print(f"  Vol(3₁) = {Vol_31}")
print()
print("  WARNING: Trefoil is a torus knot (non-hyperbolic).")
print("  The cusp deformation / Borel resurgence framework assumes")
print("  hyperbolic geometry. For Vol=0, the Kashaev invariant has")
print("  polynomial (not exponential) growth → no Stokes constant A_ω.")
print()

# IF we naively apply the formula with κ = 3/2 and A_ω = 1 (minimal):
A_omega_31_naive = 1
print(f"  NAIVE computation (A_ω = 1, κ = 3/2):")
for label, theta in [("ϑ = 0", 0), ("ϑ = ln q₀ / 2", ln_q0/2)]:
    S_naive = A_omega_31_naive * kappa_31 * (ln_q0**2 - theta**2)
    print(f"    {label}: S = {mp.nstr(S_naive, 8)}")

print()
print("  CONCLUSION: The binding formula may not apply to torus knots.")
print("  The electron mass arises from vacuum drag / quantum dilogarithm")
print("  tower, NOT from hyperbolic volume deformation.")

# =============================================================
# 3. BORROMEAN LINK 𝔹₃ (proton/neutron carrier)
# =============================================================
print()
print("─" * 70)
print("3. BORROMEAN LINK 𝔹₃  (proton / neutron)")
print("─" * 70)

# Borromean rings: 3-component hyperbolic link
# Vol(𝔹₃) = 7.32772... (= 6 × Catalan's constant)
# This is a LINK, not a knot — it has 3 cusps, one per component.
# Each cusp has its own shape parameter.
#
# Cusp shapes (all three cusps are isometric by symmetry):
# τ = e^{iπ/3} = -1/2 + i√3/2 (hexagonal lattice)
# κ_per_cusp = Im(τ)/4 = (√3/2)/4 = √3/8

Vol_borr = 7.327724753
tau_borr = cmath.exp(1j * math.pi / 3)  # e^{iπ/3}
kappa_borr_per_cusp = tau_borr.imag / 4

print(f"  Vol(𝔹₃) = {Vol_borr:.9f} = 6 × Catalan")
print(f"  τ_cusp = e^(iπ/3) = {tau_borr:.6f}")
print(f"  κ_per_cusp = √3/8 = {kappa_borr_per_cusp:.8f}")
print()

# For a 3-component link, the deformation has 3 meridians (u₁, u₂, u₃).
# The NZ potential is V(u₁, u₂, u₃) with a 3×3 Hessian.
# At the symmetric point u₁ = u₂ = u₃ = u:
#   Im V(u,u,u) = 3 × κ_per_cusp × (Re²u - Im²u) + cross terms

# GGM Stokes constant for Borromean rings: not computed in the literature
# as far as I know. For the proton, the nuclear binding analysis uses
# a different channel (block-trace, Hecke coefficients).

# Simple model: if the 3 cusps contribute independently:
A_omega_borr = 3  # placeholder — NOT derived
kappa_borr_total = 3 * kappa_borr_per_cusp  # 3√3/8

print(f"  Simple symmetric model (3 cusps, each contributing independently):")
print(f"  κ_total = 3 × √3/8 = 3√3/8 = {kappa_borr_total:.8f}")
print(f"  A_ω(𝔹₃) = ? (not derived; using placeholder {A_omega_borr})")
print()

# What ϑ would reproduce the proton mass binding?
# The proton-neutron mass difference is ~1.293 MeV
# The proton mass binding S is much larger — it's the nucleon mass itself
# minus the quark content.
#
# In the QOU framework, the proton mass comes from Vol(𝔹₃)/ℏ_q²,
# NOT from the S deformation. The S deformation is a small correction.
# The relevant S for the proton is S(proton anchor) from the q₀ pinning.

print(f"  NOTE: Proton mass is primarily Vol(𝔹₃)/ℏ_q² ≈ {Vol_borr}")
print(f"  The S deformation is a CORRECTION, not the mass itself.")
print(f"  The binding formula S = A·κ·(ln²q₀ − ϑ²) gives the")
print(f"  departure of ln(m_p/m_e) from its undeformed value.")
print()

# Ratios
print("=" * 70)
print("MASS RATIOS AND KNOT DATA")
print("=" * 70)
print()
print(f"  m_μ/m_e = {m_mu/m_e:.6f}")
print(f"  m_p/m_e = {m_p/m_e:.6f}")
print(f"  m_n/m_e = {m_n/m_e:.6f}")
print(f"  m_n/m_p = {m_n/m_p:.10f}")
print(f"  Δm(n-p) = {(m_n - m_p):.6f} MeV")
print()

# Volume ratios
print(f"  Vol(4₁)/Vol(3₁) = ∞ (3₁ has Vol=0)")
print(f"  Vol(𝔹₃)/Vol(4₁) = {Vol_borr/Vol_41:.6f}")
print(f"  Vol(𝔹₃)/Vol(4₁) ≈ {Vol_borr/Vol_41:.2f}")
print()

# Cusp modulus ratios
print(f"  κ(3₁)/κ(4₁) = {mp.nstr(kappa_31/kappa_41, 8)}")
print(f"  κ(𝔹₃_sym)/κ(4₁) = {mp.nstr(kappa_borr_total/kappa_41, 8)}")
print()

# Key insight: κ ratio
print("=" * 70)
print("KEY OBSERVATION: κ(3₁) / κ(4₁) = (3/2) / (√3/4) = 2√3 ≈ 3.464")
print(f"  Numerical: {mp.nstr(kappa_31/kappa_41, 8)}")
print()
print("If the electron's binding formula were S_e = A_e · κ₃₁ · (ln²q₀ − ϑ_e²)")
print("then the RATIO of binding scales between electron and muon is:")
print(f"  (A_e · κ₃₁) / (A_μ · κ₄₁) = A_e/{A_omega_41} × {mp.nstr(kappa_31/kappa_41, 6)}")
print("=" * 70)
