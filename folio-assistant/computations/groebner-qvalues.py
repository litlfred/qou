#!/usr/bin/env python3
"""
Q-values directly from Gröbner--Shirshov basis reduction energy.

The mass of a hadron IS the Gröbner-Shirshov energy:
  E_h = (total Hecke reduction cost to reach normal form)

The Q-value is:
  Q = (E_par - E_dau - E_e) × μ₀

At each generator σ_i, the transfer matrix chain multiplies
crossings one at a time. Each multiplication creates a σ²
term that the Hecke relation eliminates:
  σ² = (q - q⁻¹)σ + 1

The energy of this step = |a × c| × (q - q⁻¹)
where a = current σ-coefficient, c = new crossing's σ-coefficient.

This is O(A²) — same as the transfer matrix, no blowup.

Usage:
    python3 groebner-qvalues.py
"""

import math
from q_parameter import Q as q, Q_INV as qi, E_CROSS, HBAR_Q
from experimental_constants import *

HA = q - qi
Z_m = 1/(q**0.5 + qi**0.5)
LN_Q = math.log(q)
mu_0 = M_E_MEV / (3 * E_CROSS)

def log_q(x):
    return math.log(abs(x)) / LN_Q if x > 0 else float('-inf')

def crossing_coeffs(ti, tj):
    """Crossing coefficients (c, d) from nucleon types."""
    if ti == 'p' and tj == 'p': return 1.0, 0.0
    elif ti == 'n' and tj == 'n': return 1.0, -HA
    else: return 1.0, -HA/2

def groebner_energy(p, n):
    """Compute the Gröbner-Shirshov energy for N(p,n).

    For each generator σ_i, process crossings one at a time.
    Track the running (a, b) state where the element = aσ_i + b.
    Each crossing multiplication:
      (aσ + b)(cσ + d) = ac·σ² + (ad+bc)σ + bd
                       = ac·(ha·σ+1) + (ad+bc)σ + bd
                       = (ac·ha + ad + bc)σ + (ac + bd)

    The Hecke energy from this step = |ac| × ha (the σ² coefficient
    times the Hecke eigenvalue).

    Returns (total_energy, log_skein_poly).
    """
    types = ['p'] * p + ['n'] * n
    A = p + n
    total_energy = 0.0
    log_P = 0.0

    for i in range(A - 1):
        a = 0.0  # σ coefficient
        b = 1.0  # constant (identity)
        gen_energy = 0.0

        for j in range(i + 1, A):
            c, d = crossing_coeffs(types[i], types[j])

            # Hecke energy from the σ² term: |a × c| × ha
            hecke_cost = abs(a * c) * HA
            gen_energy += hecke_cost

            # Update (a, b) after Hecke reduction
            new_a = a * c * HA + a * d + b * c
            new_b = a * c + b * d
            a, b = new_a, new_b

        total_energy += gen_energy

        # Traced volume for the Skein polynomial
        V = Z_m * (a * HA + b) + a
        if abs(V) > 0:
            log_P += math.log(abs(V))

    return total_energy, log_P

# ── Compute for all 6 nuclei ───────────────────────────────────

nuclei = [
    (1,   2,   "³H",    Q_TRITIUM_MEV, Q_TRITIUM_MEV_ERR),
    (6,   8,   "¹⁴C",   Q_C14_MEV, Q_C14_MEV_ERR),
    (27,  33,  "⁶⁰Co",  Q_CO60_MEV, Q_CO60_MEV_ERR),
    (38,  52,  "⁹⁰Sr",  Q_SR90_MEV, Q_SR90_MEV_ERR),
    (55,  82,  "¹³⁷Cs", Q_CS137_MEV, Q_CS137_MEV_ERR),
    (83,  127, "²¹⁰Bi", Q_BI210_MEV, Q_BI210_MEV_ERR),
]

print(f"Q-VALUES FROM GRÖBNER BASIS REDUCTION ENERGY")
print(f"q = {q:.10f}, ha = {HA:.10f}")
print(f"μ₀ = {mu_0:.6f} MeV, E_× = {E_CROSS:.6f}")
print(f"ℏ_q = {HBAR_Q:.10f}")
print()

# Electron energy: 3 crossings of T_{2,3}
# σ³ in H₂: σ·σ² = σ·(ha·σ+1) → Hecke cost = 1×1×ha = ha
# Then (ha·σ+1)·σ → Hecke cost = ha×1×ha = ha²
# Total: ha + ha² ... let me just compute it
E_electron, _ = groebner_energy(1, 0)  # proton = 0 crossings, but electron is T_{2,3}
# Actually electron isn't a nucleus. E_e = 3 crossings of trefoil.
# Compute directly:
a_e, b_e = 0.0, 1.0
E_e = 0.0
for _ in range(3):
    E_e += abs(a_e * 1.0) * HA  # pp crossing, c=1
    new_a = a_e * 1.0 * HA + a_e * 0.0 + b_e * 1.0
    new_b = a_e * 1.0 + b_e * 0.0
    a_e, b_e = new_a, new_b
print(f"Electron (trefoil) Gröbner--Shirshov energy: {E_e:.10f}")
print(f"  = {E_e:.6f} Hecke units = {E_e * mu_0:.6f} MeV")
print()

print(f"  {'Nuc':>6} {'A':>4} {'E_par':>12} {'E_dau':>12} {'ΔE':>10} "
      f"{'Q_grob':>9} {'Q_skein':>9} {'Q_exp±δ':>14} {'err_g':>7} {'err_s':>7}")
print("  " + "-" * 100)

for p, n, name, Q_exp, Q_err in nuclei:
    E_par, logP_par = groebner_energy(p, n)
    E_dau, logP_dau = groebner_energy(p + 1, n - 1)

    delta_E = E_par - E_dau

    # Q from Gröbner--Shirshov energy: Q = ΔE × μ₀
    # (The energy is already in units of Skein crossings × ha)
    # Converting: E_hecke is in units of Σ|ac|×ha.
    # To MeV: multiply by μ₀ (MeV per Skein unit)
    Q_groebner = abs(delta_E) * mu_0

    # Q from Skein polynomial (for comparison)
    ln_ratio = logP_dau - logP_par
    Q_skein = abs(ln_ratio) * E_CROSS * mu_0  # old method

    err_g = (Q_groebner - Q_exp) / Q_exp * 100
    err_s = (Q_skein - Q_exp) / Q_exp * 100

    print(f"  {name:>6} {p+n:>4} {E_par:>12.4f} {E_dau:>12.4f} {delta_E:>+10.4f} "
          f"{Q_groebner:>9.5f} {Q_skein:>9.5f} {Q_exp:>8.5f}±{Q_err:.0e} "
          f"{err_g:>+6.1f}% {err_s:>+6.1f}%")

print()
print(f"  Q_groebner = |ΔE_Hecke| × μ₀")
print(f"  Q_skein = |ln(P_dau/P_par)| × E_× × μ₀")
