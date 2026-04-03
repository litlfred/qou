#!/usr/bin/env python3
"""
Q-value from transfer matrix Skein polynomial ratio.

FORMULA (algebraic, no fitting):

  Q = |ln(P_dau / P_par)| × E_× × μ₀

where:
  P = ∏ V̂_i(q)  is the Skein polynomial (product of traced volumes)
  E_× = ½(q - q⁻¹)  is the crossing energy
  μ₀ = m_e / (3 E_×)  is the dimensional scale

The transfer matrix encodes the full nuclear braid structure:
each nucleon pair (i,j) contributes a 2×2 matrix T(c,d) with
crossing coefficients depending on the pair type (pp, nn, pn).

All quantities derived from q alone — no shell corrections,
no Gröbner normalization, no fitting parameters.

Usage:
    python3 qvalue-representation-theory.py
"""

import math
from q_parameter import Q as q, Q_INV as qi, E_CROSS, HBAR_Q, q_int
from experimental_constants import *

HA = q - qi
mu_0 = M_E_MEV / (3 * E_CROSS)

# ══════════════════════════════════════════════════════════════
# §1  TRANSFER MATRIX Q-VALUE (Level 0)
# ══════════════════════════════════════════════════════════════

def crossing_coeffs(ti, tj):
    if ti == 'p' and tj == 'p': return 1.0, 0.0
    elif ti == 'n' and tj == 'n': return q**2, -q*(q**0.5 - qi**0.5)
    else: return (1+q**2)/2, -q*(q**0.5 - qi**0.5)/2

def T_mat(c, d):
    return [[c*HA+d, c], [c, d]]
def mat_mul(A, B):
    return [[A[0][0]*B[0][0]+A[0][1]*B[1][0], A[0][0]*B[0][1]+A[0][1]*B[1][1]],
            [A[1][0]*B[0][0]+A[1][1]*B[1][0], A[1][0]*B[0][1]+A[1][1]*B[1][1]]]
Z_m = 1.0 / (q**0.5 + qi**0.5)
def vol(M):
    return Z_m * M[0][0] + M[1][0]

def _log_skein(p, n):
    """Log of Skein polynomial for nucleus (p protons, n neutrons)."""
    types = ['p']*p + ['n']*n; A = p+n; logP = 0.0
    for i in range(A-1):
        M = [[1,0],[0,1]]
        for j in range(i+1, A):
            c, d = crossing_coeffs(types[i], types[j])
            M = mat_mul(M, T_mat(c, d))
        V = vol(M)
        if abs(V) > 0: logP += math.log(abs(V))
    return logP

def Q_predicted(Z, N):
    """Q = |ln(P_dau / P_par)| × E_× × μ₀  — pure transfer matrix, no corrections."""
    return abs(_log_skein(Z+1, N-1) - _log_skein(Z, N)) * E_CROSS * mu_0


# ══════════════════════════════════════════════════════════════
# §2  VERIFICATION
# ══════════════════════════════════════════════════════════════

nuclei = [
    (1,   2,   "³H",    Q_TRITIUM_MEV, Q_TRITIUM_MEV_ERR),
    (6,   8,   "¹⁴C",   Q_C14_MEV, Q_C14_MEV_ERR),
    (27,  33,  "⁶⁰Co",  Q_CO60_MEV, Q_CO60_MEV_ERR),
    (38,  52,  "⁹⁰Sr",  Q_SR90_MEV, Q_SR90_MEV_ERR),
    (55,  82,  "¹³⁷Cs", Q_CS137_MEV, Q_CS137_MEV_ERR),
    (83,  127, "²¹⁰Bi", Q_BI210_MEV, Q_BI210_MEV_ERR),
]

print("═" * 70)
print("Q-VALUE PREDICTIONS")
print("Q = |ln(P_dau / P_par)| × E_× × μ₀")
print("Pure transfer matrix — no shell corrections, no Gröbner normalization")
print("═" * 70)
print()
print(f"  q = {q:.10f}")
print(f"  E_× = {E_CROSS:.10f}")
print(f"  μ₀ = {mu_0:.10f} MeV")
print(f"  E_× × μ₀ = m_e/3 = {E_CROSS * mu_0:.10f} MeV")
print()

print(f"  {'Nuc':>5} │ {'Q_pred':>8} │ {'Q_exp':>8} │ {'err':>7}")
print("  " + "─" * 40)

errors = []
for Z, N, name, Q_exp, Q_err in nuclei:
    Q = Q_predicted(Z, N)
    err = (Q - Q_exp) / Q_exp * 100
    errors.append(err)
    print(f"  {name:>5} │ {Q:>8.5f} │ {Q_exp:>8.5f} │ {err:>+6.1f}%")

print()
print(f"  Mean absolute error: {sum(abs(e) for e in errors)/len(errors):.1f}%")
print(f"  Max  absolute error: {max(abs(e) for e in errors):.1f}%")
print(f"  RMS error:           {math.sqrt(sum(e**2 for e in errors)/len(errors)):.1f}%")
