#!/usr/bin/env python3
"""
Extract per-generator volumes from T_{3,5}-modified tritium braid.

The physical matrix element is:
  |M_q|² = ∏_i |V̂_i^par / V̂_i^dau|²

where V̂_i = z·a_i + b_i is the Markov-traced generator volume,
and the product runs over ALL generators (not just the converting one).

This script:
1. Builds parent (³H) and daughter (³He) braids at Level 0
2. Builds parent · T_{3,5} at Level 0
3. Extracts per-generator (a_i, b_i) and V̂_i for each
4. Computes the product of volume ratios
5. Derives the matrix element and half-life

Also does the Level 1 (quark-level) generator volume extraction.

Usage:
    cd folio-assistant/computations
    python3 t35-generator-volumes.py
"""

import json
import math
from datetime import datetime, timezone
from pathlib import Path
from fractions import Fraction

from q_parameter import (Q as q, Q_INV as qi, S_SKEIN as s,
                         E_CROSS, TWO_Q, HBAR_Q, HBAR_Q_SQ)
from hecke_engine import HeckeEngine, HeckeRational

# ═══════════════════════════════════════════════════════════════════
# STEP 1: Level 0 generator volumes (exact rational, HeckeEngine)
# ═══════════════════════════════════════════════════════════════════

print("=" * 70)
print("GENERATOR VOLUMES: Level 0 (nucleon-level)")
print("=" * 70)

engine = HeckeEngine()
qr = engine.qr  # exact rational arithmetic

# Tritium: N(1,2) → N(2,1)
# Parent ordering: ground state for (p=1, n=2)
ord_par, method_par = engine.ground_state_ordering(1, 2)
ord_dau, method_dau = engine.ground_state_ordering(2, 1)

print(f"\n  Parent ³H ordering:  {''.join('p' if x else 'n' for x in ord_par)} ({method_par})")
print(f"  Daughter ³He ordering: {''.join('p' if x else 'n' for x in ord_dau)} ({method_dau})")

A = 3
print(f"\n  Generator volumes (Level 0, A={A}, {A-1} generators):")
print(f"  {'Gen':>4} {'a_par':>14} {'b_par':>14} {'V̂_par':>14} {'a_dau':>14} {'b_dau':>14} {'V̂_dau':>14} {'V̂_par/V̂_dau':>14}")
print("  " + "-" * 100)

vol_ratios = []
for i in range(A - 1):
    a_p, b_p = qr.chain_reduce(i, ord_par)
    V_p = qr.traced_volume(i, ord_par)

    a_d, b_d = qr.chain_reduce(i, ord_dau)
    V_d = qr.traced_volume(i, ord_dau)

    ratio = float(V_p) / float(V_d) if float(V_d) != 0 else float('inf')
    vol_ratios.append(ratio)

    print(f"  σ_{i:>2} {float(a_p):14.8f} {float(b_p):14.8f} {float(V_p):14.8f} "
          f"{float(a_d):14.8f} {float(b_d):14.8f} {float(V_d):14.8f} {ratio:14.8f}")

P_par = math.prod(float(qr.traced_volume(i, ord_par)) for i in range(A-1))
P_dau = math.prod(float(qr.traced_volume(i, ord_dau)) for i in range(A-1))
M_sq_L0 = math.prod(r**2 for r in vol_ratios)

print(f"\n  P_par = ∏V̂_i^par = {P_par:.10f}")
print(f"  P_dau = ∏V̂_i^dau = {P_dau:.10f}")
print(f"  P_dau/P_par = {P_dau/P_par:.10f}")
print(f"  |M_q|² = ∏|V̂_par/V̂_dau|² = {M_sq_L0:.10f}")
print(f"  ln(P_dau/P_par) = {math.log(P_dau/P_par):.10f}")


# ═══════════════════════════════════════════════════════════════════
# STEP 2: Level 1 generator volumes (quark-level, 9 strands)
# ═══════════════════════════════════════════════════════════════════

print()
print("=" * 70)
print("GENERATOR VOLUMES: Level 1 (quark-level, 9 strands)")
print("=" * 70)

# Quark orderings: 1 = u (proton-like), 0 = d (neutron-like)
# ³H: proton(u,u,d) + neutron₁(u,d,d) + neutron₂(u,d,d)
# Encoding: u=1, d=0
ord_par_L1 = [1,1,0, 1,0,0, 1,0,0]  # ³H quarks
ord_dau_L1 = [1,1,0, 1,1,0, 1,0,0]  # ³He quarks (neutron₁ → proton₂)

n_strands = 9
n_gens = n_strands - 1  # 8 generators

print(f"\n  Parent ³H quarks:  {''.join('u' if x else 'd' for x in ord_par_L1)}")
print(f"  Daughter ³He quarks: {''.join('u' if x else 'd' for x in ord_dau_L1)}")

# Use HeckeRational for exact computation at quark level
qr_L1 = HeckeRational(111, 100)  # q = 1.11 (rational approximation)

print(f"\n  Generator volumes (Level 1, {n_strands} strands, {n_gens} generators):")
print(f"  {'Gen':>4} {'V̂_par':>14} {'V̂_dau':>14} {'ratio':>14} {'changed?':>10}")
print("  " + "-" * 60)

vol_ratios_L1 = []
changed_gens = []
for i in range(n_gens):
    V_p = qr_L1.traced_volume(i, ord_par_L1)
    V_d = qr_L1.traced_volume(i, ord_dau_L1)
    ratio = float(V_p) / float(V_d) if float(V_d) != 0 else float('inf')
    vol_ratios_L1.append(ratio)
    changed = abs(ratio - 1.0) > 1e-10
    if changed:
        changed_gens.append(i)

    print(f"  σ_{i:>2} {float(V_p):14.8f} {float(V_d):14.8f} {ratio:14.8f} {'  ←' if changed else ''}")

P_par_L1 = math.prod(float(qr_L1.traced_volume(i, ord_par_L1)) for i in range(n_gens))
P_dau_L1 = math.prod(float(qr_L1.traced_volume(i, ord_dau_L1)) for i in range(n_gens))
M_sq_L1 = math.prod(r**2 for r in vol_ratios_L1)

print(f"\n  P_par = {P_par_L1:.10f}")
print(f"  P_dau = {P_dau_L1:.10f}")
print(f"  P_dau/P_par = {P_dau_L1/P_par_L1:.10f}")
print(f"  |M_q|² = ∏|V̂_par/V̂_dau|² = {M_sq_L1:.10f}")
print(f"  Changed generators: {changed_gens}")
print(f"  # changed: {len(changed_gens)} out of {n_gens}")

# Product over ONLY changed generators
M_sq_changed = math.prod(vol_ratios_L1[i]**2 for i in changed_gens)
print(f"  |M_q|² (changed only) = {M_sq_changed:.10f}")

# ═══════════════════════════════════════════════════════════════════
# STEP 3: Half-life from generator volumes
# ═══════════════════════════════════════════════════════════════════

print()
print("=" * 70)
print("HALF-LIFE FROM GENERATOR VOLUMES")
print("=" * 70)

# Physical constants
m_e = 0.51100  # MeV
mu_0 = m_e / (3 * E_CROSS)
G_F = 1.1664e-11  # MeV⁻² (CODATA, open: derive from T_{3,5})
hbar = 6.582119569e-22  # MeV·s

Q_tritium = 0.01861  # MeV (experimental)

# Phase space integral (exact, not Sargent approximation)
# f(Z, Q) = ∫₁^{1+Q/m_e} F(Z,W) √(W²-1) W (W₀-W)² dW
# For Q << m_e (tritium): numerical integration
def phase_space_integral(Z, Q_MeV, n_steps=10000):
    """Exact numerical phase space integral."""
    W0 = 1.0 + Q_MeV / m_e
    if W0 <= 1.0:
        return 0.0
    dW = (W0 - 1.0) / n_steps
    total = 0.0
    # alpha for Coulomb
    def q_int(n):
        return (q**n - qi**n) / (q - qi)
    alpha = qi / (q_int(9) * q_int(10))

    for k in range(n_steps):
        W = 1.0 + (k + 0.5) * dW
        p_e = math.sqrt(W**2 - 1) if W > 1 else 0
        if p_e <= 0:
            continue
        beta = p_e / W
        # Fermi function
        eta = alpha * Z / beta
        if abs(eta) < 1e-10:
            F = 1.0
        else:
            F = 2 * math.pi * eta / (1 - math.exp(-2 * math.pi * eta))
        integrand = F * p_e * W * (W0 - W)**2
        total += integrand * dW
    return total

# Tritium: Z_daughter = 2
Z_d = 2
f_tritium = phase_space_integral(Z_d, Q_tritium)
print(f"\n  Phase space integral f(Z={Z_d}, Q={Q_tritium} MeV) = {f_tritium:.6e}")
print(f"  (Sargent approx (Q/m_e)⁵/30 = {(Q_tritium/m_e)**5/30:.6e})")

# Rate: Γ = (G_F² m_e⁵ / 2π³) × |M|² × f × [2]_q
rate_base = G_F**2 * m_e**5 / (2 * math.pi**3 * hbar)  # s⁻¹

print(f"\n  Rate base G_F²m_e⁵/(2π³ℏ) = {rate_base:.6e} s⁻¹")

# Try different matrix element formulas:
sec_per_yr = 3.15576e7

print(f"\n  HALF-LIFE PREDICTIONS FOR TRITIUM:")
print(f"  {'Formula':40s} {'|M|²':>12} {'t_1/2 (yr)':>12} {'Obs: 12.32 yr':>14}")
print("  " + "-" * 82)

formulas = [
    ("Level 0: ∏|V̂_par/V̂_dau|²", M_sq_L0),
    ("Level 1: ∏|V̂_par/V̂_dau|² (all)", M_sq_L1),
    ("Level 1: ∏|V̂_par/V̂_dau|² (changed)", M_sq_changed),
    ("s² × eIeR²", s**2 * 0.360**2),
    ("|M_GT|² = 3g_A² = 3×1.27² (experiment)", 3 * 1.27**2),
    ("[2]_q × Level 0 ∏|V̂|²", TWO_Q * M_sq_L0),
    ("[2]_q × Level 1 ∏|V̂|² (changed)", TWO_Q * M_sq_changed),
]

for label, M_sq in formulas:
    Gamma = rate_base * M_sq * f_tritium
    if Gamma > 0:
        t_half = math.log(2) / Gamma / sec_per_yr
    else:
        t_half = float('inf')
    ratio = t_half / 12.32
    print(f"  {label:40s} {M_sq:12.6f} {t_half:12.4f} {ratio:14.4f}")

# ═══════════════════════════════════════════════════════════════════
# STEP 4: All 6 nuclei with Level 0 generator volumes
# ═══════════════════════════════════════════════════════════════════

print()
print("=" * 70)
print("ALL 6 NUCLEI (Level 0 generator volume product)")
print("=" * 70)

nuclei = [
    (1,   2,   0.01861, "³H",    12.32,    "yr", sec_per_yr, 2),
    (6,   8,   0.15648, "¹⁴C",   5730.0,   "yr", sec_per_yr, 7),
    (27,  33,  0.31817, "⁶⁰Co",  5.2714,   "yr", sec_per_yr, 28),
    (38,  52,  0.54590, "⁹⁰Sr",  28.79,    "yr", sec_per_yr, 39),
    (55,  82,  0.51400, "¹³⁷Cs", 30.17,    "yr", sec_per_yr, 56),
    (83,  127, 1.16270, "²¹⁰Bi", 5.012,    "d",  86400.0,    84),
]

print(f"\n  {'Nuc':>6} {'|M|²':>12} {'f(Z,Q)':>12} {'t_pred':>12} {'t_obs':>10} {'ratio':>8}")
print("  " + "-" * 68)

all_results = []
for p, n, Q_exp, name, t_obs, unit, conv_s, Z_d in nuclei:
    A = p + n

    # Generator volume product
    ord_p, _ = engine.ground_state_ordering(p, n)
    ord_d, _ = engine.ground_state_ordering(p+1, n-1)

    # For large A, use log-sum to avoid overflow
    log_prod = 0.0
    for i in range(A - 1):
        Vp = float(qr.traced_volume(i, ord_p))
        Vd = float(qr.traced_volume(i, ord_d))
        if Vd != 0 and Vp != 0:
            log_prod += 2 * math.log(abs(Vp / Vd))

    M_sq = math.exp(log_prod) if abs(log_prod) < 500 else float('inf')

    # Phase space
    f_val = phase_space_integral(Z_d, Q_exp)

    # Rate and half-life
    Gamma = rate_base * M_sq * f_val
    if Gamma > 0 and Gamma < 1e30:
        t_half = math.log(2) / Gamma / conv_s
    else:
        t_half = float('inf') if Gamma <= 0 else 0.0

    ratio = t_half / t_obs if t_obs > 0 and t_half < 1e20 else float('nan')

    print(f"  {name:>6} {M_sq:12.4e} {f_val:12.4e} {t_half:10.4f} {unit:2s} {t_obs:8.3f} {unit:2s} {ratio:8.4f}")

    all_results.append({
        "name": name, "p": p, "n": n, "A": A,
        "M_sq": M_sq, "f_ZQ": f_val,
        "t_pred": t_half, "t_obs": t_obs, "unit": unit,
        "ratio": ratio,
    })

# ═══════════════════════════════════════════════════════════════════
# WITNESS
# ═══════════════════════════════════════════════════════════════════

witness = {
    "computation": "t35-generator-volumes",
    "timestamp": datetime.now(timezone.utc).isoformat(),
    "description": "Per-generator Markov-traced volumes for tritium beta decay",
    "level0": {
        "ordering_par": ord_par,
        "ordering_dau": ord_dau,
        "vol_ratios": vol_ratios,
        "M_sq_product": M_sq_L0,
        "P_par": P_par,
        "P_dau": P_dau,
    },
    "level1": {
        "ordering_par": ord_par_L1,
        "ordering_dau": ord_dau_L1,
        "vol_ratios": vol_ratios_L1,
        "changed_generators": changed_gens,
        "M_sq_all": M_sq_L1,
        "M_sq_changed": M_sq_changed,
    },
    "tritium_halflife_formulas": {
        "f_phase_space": f_tritium,
        "rate_base": rate_base,
    },
    "all_nuclei": all_results,
}

out_path = Path(__file__).parent / "t35-generator-volumes.witness.json"
with open(out_path, "w") as f:
    json.dump(witness, f, indent=2)
print(f"\nWitness: {out_path}")
