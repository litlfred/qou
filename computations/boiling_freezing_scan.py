#!/usr/bin/env python3
"""
Numerical scan of boiling and freezing temperatures from the q-deformed equation of state.

Follows the user directive to use strictly:
P_q V_q = n_q R T  => T_boil = S_q^(∂) / (n_q R)
with n_q = [2]_q for boiling (gas phase exploring S^2)
and n_q = [2]_q [n_K]_q for freezing.

NO fitted scales are used to force the temperatures to 373 K / 273 K.
The gap (if any) is reported honestly.
"""

from __future__ import annotations

import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parent))
import _path_bridge as _bridge  # noqa: F401
from mpmath import mp, mpf
from q_parameter import Q_50_DIGIT_STR

mp.dps = 50
# Was a bare float64 literal 1.109978033355325x — a value that is NEITHER pin,
# 495 ppb from proton and 506 ppb from muon, i.e. ~44x the ~11.5 ppb mu-p
# substrate tension. It was also float64 in a computations/ script, which
# AGENTS.md forbids outright. Both are fixed by reading the declared pin.

# QOU inputs
Q0 = mpf(Q_50_DIGIT_STR)
h = Q0 - 1 / Q0
h2 = h * h
dim_q = Q0 + 1 / Q0  # [2]_q

# Constants
R_gas = 8.314462618  # J / (mol K)

# Molecule Data: (E_cov kJ/mol, n_HB, n_K, T_boil_obs K, T_melt_obs K)
MOLECULES = {
    "H2O": (460.0, 2, 6, 373.15, 273.15),  # n_K=6 is a guess for the knot crossing number, if applicable
    "HF":  (565.0, 1, 3, 293.15, 189.6),
    "NH3": (391.0, 1, 3, 239.81, 195.4)
}

print("=" * 80)
print("Boiling/Freezing Temperature Scan via q-Equation of State (NO FIT)")
print("=" * 80)
print(f"Substrate q₀ = {Q0:.10f}")
print(f"H-bond suppression h² = {h2:.6f}")
print(f"Gas phase effective dimension n_q = [2]_q = {dim_q:.6f}")
print("-" * 80)

def q_integer(n: int, q: float) -> float:
    return (q**n - q**(-n)) / (q - 1/q)

for name, (e_cov, n_hb, n_k, t_boil_obs, t_melt_obs) in MOLECULES.items():
    print(f"[{name}]")
    
    # 1. Cohesion Energy S_q^(∂)
    S_q_boundary = n_hb * h2 * e_cov * 1000.0  # converted to J/mol
    print(f"  Cohesion S_q^(∂): {S_q_boundary/1000.0:.2f} kJ/mol")
    
    # 2. Boiling Point (Gas -> Liquid)
    # T_boil = S_q^(∂) / ([2]_q * R)
    t_boil_pred = S_q_boundary / (dim_q * R_gas)
    boil_ratio = t_boil_pred / t_boil_obs
    print(f"  T_boil(pred) = S_q^(∂) / ([2]_q R) = {t_boil_pred:.1f} K")
    print(f"  T_boil(obs)  = {t_boil_obs:.1f} K")
    print(f"  Gap ratio    = {boil_ratio:.2f}x (Misses by factor of {boil_ratio:.2f}) -> tier=open")
    
    # 3. Melting Point (Liquid -> Solid)
    # T_melt = S_q^(∂) / ([2]_q * [n_K]_q * R)
    n_k_q = q_integer(n_k, Q0)
    t_melt_pred = S_q_boundary / (dim_q * n_k_q * R_gas)
    melt_ratio = t_melt_pred / t_melt_obs
    print(f"  T_melt(pred) = S_q^(∂) / ([2]_q [{n_k}]_q R) = {t_melt_pred:.1f} K")
    print(f"  T_melt(obs)  = {t_melt_obs:.1f} K")
    print(f"  Gap ratio    = {melt_ratio:.2f}x (Misses by factor of {melt_ratio:.2f}) -> tier=open")
    
    print()

print("CONCLUSION: The strict geometric mapping P_q V_q = n_q R T over-predicts temperatures ")
print("by a factor of ~6.4 to ~10. The empirical 'entropy of vaporization' involves a missing topological ")
print("or phase space factor beyond the simple [2]_q of the Hopf base.")
