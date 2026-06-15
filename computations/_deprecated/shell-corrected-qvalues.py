#!/usr/bin/env python3
"""
Shell-corrected Q-values using T_{3,5} · B₃⁻¹ renormalization.

The shell operator T_{3,5} · B₃⁻¹ has trace 1.555 in H₃(q).
Each Borromean triple at a shell boundary that changes composition
(when one nucleon converts n→p) contributes a correction of
Δln = 0.944 to the Skein polynomial log ratio.

The number of affected triples at the converting subshell is
floor((2j+1)/3) where j is the subshell angular momentum.

Usage:
    python3 shell-corrected-qvalues.py
"""

import math
from q_parameter import Q as q, Q_INV as qi, E_CROSS
from hecke_division import HeckeDivision, HeckeElement

div = HeckeDivision(q_val=q)
HA = q - qi
Z_m = 1.0 / (q**0.5 + q**(-0.5))
mu_0 = 0.51100 / (3 * E_CROSS)

# ── Compute shell correction from T_{3,5} · B₃⁻¹ ──────────────

def sigma(i):
    return HeckeElement({(i,): 1.0})

def sigma_inv(i):
    return HeckeElement({(i,): 1.0, (): -HA})

# B₃ and B₃⁻¹
B3 = sigma(0) * sigma_inv(1) * sigma(0) * sigma_inv(1)
B3_red, _ = div.reduce(B3)
B3_inv = sigma(1) * sigma_inv(0) * sigma(1) * sigma_inv(0)
B3_inv_red, _ = div.reduce(B3_inv)

# T_{3,5}
T35 = HeckeElement.identity()
for _ in range(5):
    T35 = T35 * sigma(0) * sigma(1)
T35_red, _ = div.reduce(T35)

# Shell operator
shell_op = T35_red * B3_inv_red
shell_op_red, _ = div.reduce(shell_op)

# Neutron and shelled neutron
neutron = div.crossing_mixed(0) * div.crossing_mixed(0) * div.crossing_negative(1)
neutron_red, _ = div.reduce(neutron)
neutron_trace = div.markov_trace(neutron_red, 3)

shelled = neutron_red * shell_op_red
shelled_red, _ = div.reduce(shelled)
shelled_trace = div.markov_trace(shelled_red, 3)

ln_q = math.log(q)
R = shelled_trace / neutron_trace
SHELL_CORR_LN = math.log(R)            # classical ln(R) — WRONG framework
SHELL_CORR = math.log(R) / ln_q         # log_q(R) — correct q-logarithm

print(f"Shell correction (q-log):")
print(f"  R = tr(shelled)/tr(bare) = {R:.10f}")
print(f"  log_q(R) = ln(R)/ln(q) = {SHELL_CORR:.6f}")
print(f"  (NOT ln(R) = {SHELL_CORR_LN:.6f} �� that's the classical limit)")
print(f"  (from T_{{3,5}} · B₃⁻¹ acting on neutron)")
print()

# ── Mayer-Jensen subshell data ──────────────────────────────────

SUBSHELLS = [
    # (label, 2j+1, cumulative)
    ("1s1/2",  2,   2),
    ("1p3/2",  4,   6),
    ("1p1/2",  2,   8),
    ("1d5/2",  6,  14),
    ("2s1/2",  2,  16),
    ("1d3/2",  4,  20),
    ("1f7/2",  8,  28),
    ("2p3/2",  4,  32),
    ("1f5/2",  6,  38),
    ("2p1/2",  2,  40),
    ("1g9/2", 10,  50),
    ("1g7/2",  8,  58),
    ("2d5/2",  6,  64),
    ("2d3/2",  4,  68),
    ("3s1/2",  2,  70),
    ("1h11/2",12,  82),
    ("1h9/2", 10,  92),
    ("2f7/2",  8, 100),
    ("2f5/2",  6, 106),
    ("3p3/2",  4, 110),
    ("3p1/2",  2, 112),
    ("1i13/2",14, 126),
]

def find_converting_subshell(N_parent, N_daughter):
    """Find which subshell the converting nucleon is in.

    For β⁻: one neutron converts to proton.
    The converting neutron is the LAST filled neutron
    (highest subshell with neutron occupancy).

    Returns (subshell_label, capacity, n_borromean_triples).
    """
    # Fill parent neutrons
    remaining = N_parent
    last_sub = None
    last_occ = 0
    for label, cap, cumul in SUBSHELLS:
        occ = min(remaining, cap)
        if occ > 0:
            last_sub = (label, cap)
            last_occ = occ
        remaining -= occ
        if remaining <= 0:
            break

    if last_sub is None:
        return None, 0, 0

    label, cap = last_sub
    # Number of Borromean triples in this subshell
    # that involve the converting nucleon:
    # The converting nucleon pairs with floor((occ-1)/2) other nucleons
    # to form triples. Each triple has 3 members.
    # More precisely: the subshell has `occ` neutrons total.
    # The converting one interacts with the rest.
    # Number of triples containing the converting nucleon:
    n_triples = last_occ // 3  # triples in the subshell
    if n_triples == 0:
        n_triples = 1  # at least one crossing changes

    return label, cap, n_triples

# ── Naive Q-values ──────────────────────────────────────────────

def T_mat(c, d):
    return [[c*HA+d, c], [c, d]]

def mat_mul(A, B):
    return [[A[0][0]*B[0][0]+A[0][1]*B[1][0], A[0][0]*B[0][1]+A[0][1]*B[1][1]],
            [A[1][0]*B[0][0]+A[1][1]*B[1][0], A[1][0]*B[0][1]+A[1][1]*B[1][1]]]

def vol(M):
    return Z_m * M[0][0] + M[1][0]

def naive_log_skein(p, n):
    types = ['p']*p + ['n']*n
    A = p + n
    log_P = 0.0
    for i in range(A - 1):
        M = [[1,0],[0,1]]
        for j in range(i + 1, A):
            ti, tj = types[i], types[j]
            if ti == 'p' and tj == 'p': c, d = 1.0, 0.0
            elif ti == 'n' and tj == 'n': c, d = 1.0, -HA
            else: c, d = 1.0, -HA/2
            M = mat_mul(M, T_mat(c, d))
        V = vol(M)
        if abs(V) > 0:
            log_P += math.log(abs(V))
    return log_P

# ── All 6 nuclei ────────────────────────────────────────────────

from experimental_constants import (
    Q_TRITIUM_MEV, Q_TRITIUM_MEV_ERR,
    Q_C14_MEV, Q_C14_MEV_ERR,
    Q_CO60_MEV, Q_CO60_MEV_ERR,
    Q_SR90_MEV, Q_SR90_MEV_ERR,
    Q_CS137_MEV, Q_CS137_MEV_ERR,
    Q_BI210_MEV, Q_BI210_MEV_ERR,
)

nuclei = [
    (1,   2,   "³H",    Q_TRITIUM_MEV, Q_TRITIUM_MEV_ERR),
    (6,   8,   "¹⁴C",   Q_C14_MEV, Q_C14_MEV_ERR),
    (27,  33,  "⁶⁰Co",  Q_CO60_MEV, Q_CO60_MEV_ERR),
    (38,  52,  "⁹⁰Sr",  Q_SR90_MEV, Q_SR90_MEV_ERR),
    (55,  82,  "¹³⁷Cs", Q_CS137_MEV, Q_CS137_MEV_ERR),
    (83,  127, "²¹⁰Bi", Q_BI210_MEV, Q_BI210_MEV_ERR),
]

print(f"{'Nuc':>6} {'Q_naive':>9} {'sub':>8} {'n_trip':>6} {'Q_corr':>9} "
      f"{'Q_exp±δ':>14} {'err_n':>7} {'err_c':>7}")
print("-" * 78)

for p, n, name, Q_exp, Q_err in nuclei:
    lp = naive_log_skein(p, n)
    ld = naive_log_skein(p+1, n-1)
    logq_naive = (ld - lp) / ln_q  # log_q(P_dau/P_par)
    Q_naive = abs(logq_naive) * ln_q * E_CROSS * mu_0

    # Find converting subshell and number of boundary triples
    sub_label, sub_cap, n_trips = find_converting_subshell(n, n-1)

    # Apply correction in q-log: each boundary triple subtracts SHELL_CORR
    logq_corrected = abs(logq_naive) - n_trips * SHELL_CORR
    Q_corr = abs(logq_corrected) * ln_q * E_CROSS * mu_0

    err_n = (Q_naive - Q_exp) / Q_exp * 100
    err_c = (Q_corr - Q_exp) / Q_exp * 100

    print(f"{name:>6} {Q_naive:>9.5f} {sub_label or '-':>8} {n_trips:>6} {Q_corr:>9.5f} "
          f"{Q_exp:>8.5f}±{Q_err:.0e} {err_n:>+6.1f}% {err_c:>+6.1f}%")
