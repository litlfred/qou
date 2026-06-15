#!/usr/bin/env python3
"""
Level 1 Q-value for ¹⁴C (42 quark strands, 861 crossings).

Tests whether quark-level resolution improves the Level 0
Q-value prediction (4.6% error for ¹⁴C).

At Level 1: each nucleon has 3 quark strands.
¹⁴C has A=14 nucleons → 42 strands, C(42,2) = 861 crossings.
¹⁴N (daughter) has same A → same strand count.

Uses the transfer matrix chain approach (not full Hecke reduction)
to keep computation tractable: O(A²) per generator, A-1 generators.

Usage:
    cd folio-assistant/computations
    python3 level1-c14.py
"""

import json
import math
import time
from datetime import datetime, timezone
from pathlib import Path

from q_parameter import (Q as q, Q_INV as qi, E_CROSS)
from experimental_constants import (Q_C14_MEV, Q_C14_MEV_ERR,
                                     HALFLIFE_C14_YR, HALFLIFE_C14_YR_ERR,
                                     M_E_MEV)

# ── Parameters ──────────────────────────────────────────────────
HA = q - qi                        # Hecke amplitude q - q⁻¹
Z_m = 1.0 / (q**0.5 + q**(-0.5))
mu_0 = M_E_MEV / (3 * E_CROSS)

print(f"Level 1 Q-value computation for ¹⁴C")
print(f"q = {q:.10f}")
print()

# ── Quark types ─────────────────────────────────────────────────
# ¹⁴C: 6 protons + 8 neutrons
# Proton quarks: u, u, d
# Neutron quarks: u, d, d

def build_quark_types(p, n):
    """Build quark type list: 1=u, 0=d for each strand."""
    quarks = []
    for _ in range(p):
        quarks.extend([1, 1, 0])  # proton: u, u, d
    for _ in range(n):
        quarks.extend([1, 0, 0])  # neutron: u, d, d
    return quarks

# ¹⁴C: 6p + 8n → 42 quarks
c14_quarks = build_quark_types(6, 8)
# ¹⁴N: 7p + 7n → 42 quarks
n14_quarks = build_quark_types(7, 7)

n_strands = len(c14_quarks)
n_crossings = n_strands * (n_strands - 1) // 2
n_generators = n_strands - 1

print(f"  ¹⁴C: {n_strands} strands, {n_crossings} crossings, {n_generators} generators")
print(f"  Quarks: {''.join('u' if x else 'd' for x in c14_quarks)}")
print()

# ── Transfer matrix chain per generator ─────────────────────────
# For each generator σ_i (strand i), compute the chain of crossings
# with all strands j > i, reducing via Hecke at each step.
#
# The chain at generator i: multiply T(c_j, d_j) for j = i+1, ..., n-1
# where (c_j, d_j) depends on quark types (quarks[i], quarks[j]).
#
# After chain reduction: (a_i, b_i) where the element is a_i σ_i + b_i.
# Traced volume: V̂_i = Z · a_i + b_i.

def mat_mul(A, B):
    return [[A[0][0]*B[0][0]+A[0][1]*B[1][0], A[0][0]*B[0][1]+A[0][1]*B[1][1]],
            [A[1][0]*B[0][0]+A[1][1]*B[1][0], A[1][0]*B[0][1]+A[1][1]*B[1][1]]]

def T_mat(c, d):
    """2×2 transfer matrix T(c,d) = [[c·ha+d, c], [c, d]]"""
    return [[c*HA+d, c], [c, d]]

def traced_vol(M):
    """V̂ = z·M₁₁ + M₂₁"""
    return Z_m * M[0][0] + M[1][0]

def crossing_coeffs(qi_type, qj_type):
    """Crossing coefficients (c, d) from quark types."""
    if qi_type == 1 and qj_type == 1:  # u-u
        return 1.0, 0.0
    elif qi_type == 0 and qj_type == 0:  # d-d
        return 1.0, -HA
    else:  # u-d or d-u (mixed)
        return 1.0, -HA / 2

def skein_poly_level1(quarks):
    """Compute log Skein polynomial using 2×2 transfer matrix chain.

    This is the CORRECT approach: multiply full 2×2 matrices,
    then take V̂_i = z·M₁₁ + M₂₁ (Markov-traced volume).
    """
    n = len(quarks)
    log_P = 0.0
    for i in range(n - 1):
        M = [[1,0],[0,1]]  # identity
        for j in range(i + 1, n):
            c, d = crossing_coeffs(quarks[i], quarks[j])
            T = T_mat(c, d)
            M = mat_mul(M, T)
        V = traced_vol(M)
        if V != 0:
            log_P += math.log(abs(V))
        else:
            return float('-inf')
    return log_P

# ── Compute ─────────────────────────────────────────────────────

print("Computing Level 1 Skein polynomials...")
t0 = time.time()

log_P_c14 = skein_poly_level1(c14_quarks)
t1 = time.time()
print(f"  log P(¹⁴C) = {log_P_c14:.10f}  ({t1-t0:.2f}s)")

log_P_n14 = skein_poly_level1(n14_quarks)
t2 = time.time()
print(f"  log P(¹⁴N) = {log_P_n14:.10f}  ({t2-t1:.2f}s)")

ln_ratio = log_P_n14 - log_P_c14
Q_pred = abs(ln_ratio) * E_CROSS * mu_0

print(f"\n  ln(P_dau/P_par) = {ln_ratio:.10f}")
print(f"  Q_pred = |ln| × E_× × μ₀ = {Q_pred:.6f} MeV")
print(f"  Q_exp  = {Q_C14_MEV} ± {Q_C14_MEV_ERR} MeV")
print(f"  Error  = {(Q_pred - Q_C14_MEV)/Q_C14_MEV * 100:+.2f}%")

# ── Also compute Level 0 for comparison ─────────────────────────

def build_nucleon_types(p, n):
    return [1]*p + [0]*n

c14_nucleons = build_nucleon_types(6, 8)
n14_nucleons = build_nucleon_types(7, 7)

def crossing_coeffs_nucleon(ni, nj):
    if ni == 1 and nj == 1: return 1.0, 0.0
    elif ni == 0 and nj == 0: return 1.0, -HA
    else: return 1.0, -HA/2

def skein_poly_level0(nucleons):
    """Level 0 Skein polynomial using 2×2 transfer matrix chain."""
    n = len(nucleons)
    log_P = 0.0
    for i in range(n - 1):
        M = [[1,0],[0,1]]
        for j in range(i + 1, n):
            c, d = crossing_coeffs_nucleon(nucleons[i], nucleons[j])
            T = T_mat(c, d)
            M = mat_mul(M, T)
        V = traced_vol(M)
        if V != 0:
            log_P += math.log(abs(V))
        else:
            return float('-inf')
    return log_P

log_P_c14_L0 = skein_poly_level0(c14_nucleons)
log_P_n14_L0 = skein_poly_level0(n14_nucleons)
ln_ratio_L0 = log_P_n14_L0 - log_P_c14_L0
Q_pred_L0 = abs(ln_ratio_L0) * E_CROSS * mu_0

print(f"\n  Level 0 comparison:")
print(f"  ln(P_dau/P_par) L0 = {ln_ratio_L0:.10f}")
print(f"  Q_pred L0 = {Q_pred_L0:.6f} MeV")
print(f"  Q_exp     = {Q_C14_MEV} ± {Q_C14_MEV_ERR} MeV")
print(f"  Error L0  = {(Q_pred_L0 - Q_C14_MEV)/Q_C14_MEV * 100:+.2f}%")
print(f"  Error L1  = {(Q_pred - Q_C14_MEV)/Q_C14_MEV * 100:+.2f}%")

# ── Also do tritium at both levels for consistency check ────────

print(f"\n  Tritium consistency check:")
h3_L1 = build_quark_types(1, 2)
he3_L1 = build_quark_types(2, 1)
log_h3 = skein_poly_level1(h3_L1)
log_he3 = skein_poly_level1(he3_L1)
ln_trit_L1 = log_he3 - log_h3
Q_trit_L1 = abs(ln_trit_L1) * E_CROSS * mu_0

h3_L0 = build_nucleon_types(1, 2)
he3_L0 = build_nucleon_types(2, 1)
log_h3_0 = skein_poly_level0(h3_L0)
log_he3_0 = skein_poly_level0(he3_L0)
ln_trit_L0 = log_he3_0 - log_h3_0
Q_trit_L0 = abs(ln_trit_L0) * E_CROSS * mu_0

from experimental_constants import Q_TRITIUM_MEV, Q_TRITIUM_MEV_ERR

print(f"  L0: Q_pred = {Q_trit_L0:.6f} MeV, error = {(Q_trit_L0-Q_TRITIUM_MEV)/Q_TRITIUM_MEV*100:+.2f}%")
print(f"  L1: Q_pred = {Q_trit_L1:.6f} MeV, error = {(Q_trit_L1-Q_TRITIUM_MEV)/Q_TRITIUM_MEV*100:+.2f}%")
print(f"  Exp: Q = {Q_TRITIUM_MEV} ± {Q_TRITIUM_MEV_ERR} MeV")

# ── Witness ─────────────────────────────────────────────────────

witness = {
    "computation": "level1-c14",
    "timestamp": datetime.now(timezone.utc).isoformat(),
    "description": "Level 1 (quark-level) Q-value for ¹⁴C → ¹⁴N beta decay",
    "parameters": {"q": q, "E_cross": E_CROSS, "mu_0": mu_0, "n_strands": n_strands},
    "c14": {
        "level0": {"log_P_par": log_P_c14_L0, "log_P_dau": log_P_n14_L0,
                    "ln_ratio": ln_ratio_L0, "Q_pred": Q_pred_L0,
                    "Q_exp": Q_C14_MEV, "Q_exp_err": Q_C14_MEV_ERR,
                    "error_pct": (Q_pred_L0-Q_C14_MEV)/Q_C14_MEV*100},
        "level1": {"log_P_par": log_P_c14, "log_P_dau": log_P_n14,
                    "ln_ratio": ln_ratio, "Q_pred": Q_pred,
                    "Q_exp": Q_C14_MEV, "Q_exp_err": Q_C14_MEV_ERR,
                    "error_pct": (Q_pred-Q_C14_MEV)/Q_C14_MEV*100},
    },
    "tritium": {
        "level0": {"Q_pred": Q_trit_L0, "error_pct": (Q_trit_L0-Q_TRITIUM_MEV)/Q_TRITIUM_MEV*100},
        "level1": {"Q_pred": Q_trit_L1, "error_pct": (Q_trit_L1-Q_TRITIUM_MEV)/Q_TRITIUM_MEV*100},
        "Q_exp": Q_TRITIUM_MEV, "Q_exp_err": Q_TRITIUM_MEV_ERR,
    },
}

out = Path(__file__).parent / "level1-c14.witness.json"
with open(out, "w") as f:
    json.dump(witness, f, indent=2)
print(f"\nWitness: {out}")
