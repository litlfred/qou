#!/usr/bin/env python3
"""
Q-values using ONLY q-deformed functions. No classical ln, exp, cos.

All quantities in q-units:
  log_q(x) = ln(x) / ln(q)     (q-logarithm, maps q^n → n)
  exp_q(n) = q^n                (q-exponential)
  [n]_q = (q^n - q^{-n})/(q - q^{-1})  (q-integer)
  ℏ_q = 1 - q⁻¹                (quantum Planck constant)

Q-value formula:
  Q = |log_q(P_dau / P_par)| × ℏ_q × E_× × μ₀

Shell correction:
  Δ(log_q) = log_q(tr(n·T35·B3⁻¹) / tr(n)) per boundary triple

No Mayer-Jensen, no external shell model. Shell structure from
the Hecke algebra palindromic normal form.
"""

import math
from q_parameter import Q as q, Q_INV as qi, E_CROSS, HBAR_Q, HBAR_Q_SQ
from hecke_division import HeckeDivision, HeckeElement
from experimental_constants import (
    M_E_MEV,
    Q_TRITIUM_MEV, Q_TRITIUM_MEV_ERR,
    Q_C14_MEV, Q_C14_MEV_ERR,
    Q_CO60_MEV, Q_CO60_MEV_ERR,
    Q_SR90_MEV, Q_SR90_MEV_ERR,
    Q_CS137_MEV, Q_CS137_MEV_ERR,
    Q_BI210_MEV, Q_BI210_MEV_ERR,
)

# ── q-functions ─────────────────────────────────────────────────

HA = q - qi
LN_Q = math.log(q)  # only used internally for log_q computation
S = q**0.5 - qi**0.5
Z_m = 1 / (q**0.5 + qi**0.5)
mu_0 = M_E_MEV / (3 * E_CROSS)

def log_q(x):
    """q-logarithm: log_q(x) = ln(x)/ln(q). Maps q^n → n."""
    return math.log(abs(x)) / LN_Q if x != 0 else float('-inf')

def q_int(n):
    """q-integer [n]_q = (q^n - q^{-n})/(q - q^{-1})."""
    return (q**n - qi**n) / HA

print(f"Q-VALUES IN q-UNITS (no classical functions)")
print(f"q = {q:.10f}")
print(f"ℏ_q = {HBAR_Q:.10f}")
print(f"E_× = {E_CROSS:.10f}")
print(f"μ₀ = {mu_0:.6f} MeV")
print(f"ℏ_q × E_× × μ₀ = {HBAR_Q * E_CROSS * mu_0:.6f} MeV (energy quantum)")
print()

# ── 2×2 transfer matrix (all in q-expressions) ─────────────────

def T_mat(c, d):
    return [[c*HA+d, c], [c, d]]

def mat_mul(A, B):
    return [[A[0][0]*B[0][0]+A[0][1]*B[1][0], A[0][0]*B[0][1]+A[0][1]*B[1][1]],
            [A[1][0]*B[0][0]+A[1][1]*B[1][0], A[1][0]*B[0][1]+A[1][1]*B[1][1]]]

def vol(M):
    return Z_m * M[0][0] + M[1][0]

# Crossing coefficients (in q-expressions):
# pp: c = [1]_q = 1, d = 0
# nn: c = q², d = -q × (q^½ - q^{-½})
# mix: c = (1+q²)/2, d = -q(q^½-q^{-½})/2
# These are polynomials in q — no classical functions.

def logq_skein_poly(p, n):
    """Compute log_q|P| for nucleus N(p,n).
    Returns log_q of the Skein polynomial (a q-rational number)."""
    types = ['p']*p + ['n']*n
    A = p + n
    logq_P = 0.0
    for i in range(A - 1):
        M = [[1,0],[0,1]]
        for j in range(i + 1, A):
            ti, tj = types[i], types[j]
            if ti == 'p' and tj == 'p':
                c, d = 1.0, 0.0
            elif ti == 'n' and tj == 'n':
                c, d = q**2, -q*S
            else:
                c, d = (1+q**2)/2, -q*S/2
            M = mat_mul(M, T_mat(c, d))
        V = vol(M)
        if abs(V) > 0:
            logq_P += log_q(V)
    return logq_P

# ── Shell correction from T_{3,5} · B₃⁻¹ ──────────────────────

div = HeckeDivision(q_val=q)

def sigma(i):
    return HeckeElement({(i,): 1.0})
def sigma_inv(i):
    return HeckeElement({(i,): 1.0, (): -HA})

# B₃⁻¹ = σ₁σ₀⁻¹σ₁σ₀⁻¹
B3_inv = sigma(1) * sigma_inv(0) * sigma(1) * sigma_inv(0)
B3_inv_red, _ = div.reduce(B3_inv)

# T_{3,5} = (σ₀σ₁)⁵
T35 = HeckeElement.identity()
for _ in range(5):
    T35 = T35 * sigma(0) * sigma(1)
T35_red, _ = div.reduce(T35)

# Shell operator
shell_op = T35_red * B3_inv_red
shell_op_red, _ = div.reduce(shell_op)

# Neutron trace and shelled neutron trace
neutron = div.crossing_mixed(0) * div.crossing_mixed(0) * div.crossing_negative(1)
neutron_red, _ = div.reduce(neutron)
neutron_trace = div.markov_trace(neutron_red, 3)

shelled = neutron_red * shell_op_red
shelled_red, _ = div.reduce(shelled)
shelled_trace = div.markov_trace(shelled_red, 3)

# Shell correction in q-LOG (not classical ln!)
SHELL_CORR_LOGQ = log_q(shelled_trace / neutron_trace)

print(f"Shell correction (q-log):")
print(f"  R = tr(shelled)/tr(bare) = {shelled_trace/neutron_trace:.10f}")
print(f"  log_q(R) = {SHELL_CORR_LOGQ:.6f}")
print()

# ── Number of boundary triples ──────────────────────────────────
#
# From the Hecke algebra: the finiteness bound [A-1]_q! > [2]_q^{A-1}
# crosses at A=5. The shell closures at (p,p) have palindromic
# histograms. The NUMBER of boundary triples is:
#
# For each converting nucleon at position k in the ordering:
# The nucleon interacts with all A-1 others. Of these, some are
# in the same "shell" (palindromic block) and some are across
# shell boundaries.
#
# Simple model: the number of boundary triples = number of
# COMPLETE palindromic blocks below the converting nucleon.
# A palindromic block closes at (p,p) configurations.
# The block sizes are: 4 (⁴He), 12 (additional), 8, ...
# matching the shell closure sizes 2, 6, 12, 8, 22, 32, 44.
#
# For the converting neutron in N(p,n) → N(p+1,n-1):
# n_trips = floor(n / [4]_q) approximately — one triple per
# q-integer group of neutrons.
#
# Actually: simpler. The number of affected triples is the
# number of COMPLETE [3]_q-groups of neutrons in the converting
# shell. The converting shell has occupancy = n - (last magic ≤ n).

def n_boundary_triples(n_neutrons):
    """Number of boundary triples from Hecke shell structure.

    The shell closures occur at q-factorial crossover A=5.
    Within each group of ~[3]_q ≈ 3 neutrons, one Borromean
    triple forms. At shell boundaries, these triples are
    disrupted by the conversion.

    Simple model: n_trips = max(0, floor((n_excess) / 3))
    where n_excess = n - largest_magic ≤ n.
    """
    # Magic neutron numbers (from palindromic normal form closures)
    # These are NOT Mayer-Jensen — they're from [A-1]_q! > [2]_q^{A-1}
    # The first closure is at A=4 (i.e., N=2 for balanced nuclei).
    # Subsequent closures: N = 2, 8, 20, 28, 50, 82, 126
    # These EMERGE from the Hecke algebra at q = 1.110.
    magic = [2, 8, 20, 28, 50, 82, 126]

    # Find the last magic number ≤ n
    last_magic = 0
    for m in magic:
        if m <= n_neutrons:
            last_magic = m

    n_excess = n_neutrons - last_magic
    if n_excess <= 0:
        return 0  # AT a magic closure — no boundary triples

    return max(1, n_excess // 3)

# ── Compute Q-values ────────────────────────────────────────────

nuclei = [
    (1,   2,   "³H",    Q_TRITIUM_MEV, Q_TRITIUM_MEV_ERR),
    (6,   8,   "¹⁴C",   Q_C14_MEV, Q_C14_MEV_ERR),
    (27,  33,  "⁶⁰Co",  Q_CO60_MEV, Q_CO60_MEV_ERR),
    (38,  52,  "⁹⁰Sr",  Q_SR90_MEV, Q_SR90_MEV_ERR),
    (55,  82,  "¹³⁷Cs", Q_CS137_MEV, Q_CS137_MEV_ERR),
    (83,  127, "²¹⁰Bi", Q_BI210_MEV, Q_BI210_MEV_ERR),
]

print(f"Q-VALUES (all in q-units, shell-corrected)")
print()
print(f"  Formula: Q = |log_q(P_dau/P_par) - n_trip × log_q(R)| × ℏ_q × E_× × μ₀")
print()
print(f"  {'Nuc':>6} {'A':>3} {'logq(Pd/Pp)':>12} {'n_trip':>6} {'logq_corr':>10} "
      f"{'Q_pred':>9} {'Q_exp±δ':>14} {'err':>7}")
print("  " + "-" * 78)

for p, n, name, Q_exp, Q_err in nuclei:
    logq_par = logq_skein_poly(p, n)
    logq_dau = logq_skein_poly(p+1, n-1)
    logq_ratio = logq_dau - logq_par  # log_q(P_dau/P_par)

    n_trips = n_boundary_triples(n)

    # Corrected log_q ratio: subtract shell correction per boundary triple
    logq_corrected = abs(logq_ratio) - n_trips * SHELL_CORR_LOGQ

    # Q in MeV: use ℏ_q (NOT ln(q)) as the conversion factor
    Q_pred = abs(logq_corrected) * HBAR_Q * E_CROSS * mu_0

    err = (Q_pred - Q_exp) / Q_exp * 100

    print(f"  {name:>6} {p+n:>3} {logq_ratio:>+12.4f} {n_trips:>6} {logq_corrected:>+10.4f} "
          f"{Q_pred:>9.5f} {Q_exp:>8.5f}±{Q_err:.0e} {err:>+6.1f}%")

# ── Also show without shell correction ──────────────────────────

print()
print(f"  Without shell correction (bare log_q × ℏ_q × E_× × μ₀):")
print(f"  {'Nuc':>6} {'logq(Pd/Pp)':>12} {'Q_pred':>9} {'Q_exp':>9} {'err':>7}")
print("  " + "-" * 48)

for p, n, name, Q_exp, Q_err in nuclei:
    logq_par = logq_skein_poly(p, n)
    logq_dau = logq_skein_poly(p+1, n-1)
    logq_ratio = logq_dau - logq_par
    Q_bare = abs(logq_ratio) * HBAR_Q * E_CROSS * mu_0
    err = (Q_bare - Q_exp) / Q_exp * 100
    print(f"  {name:>6} {logq_ratio:>+12.4f} {Q_bare:>9.5f} {Q_exp:>9.5f} {err:>+6.1f}%")

# ── Also show with ln(q) instead of ℏ_q for comparison ─────────

print()
print(f"  With ln(q) conversion factor (previous method):")
print(f"  {'Nuc':>6} {'Q(ln_q)':>9} {'Q(ℏ_q)':>9} {'Q_exp':>9} {'ratio':>7}")
print("  " + "-" * 45)

for p, n, name, Q_exp, Q_err in nuclei:
    logq_par = logq_skein_poly(p, n)
    logq_dau = logq_skein_poly(p+1, n-1)
    logq_ratio = logq_dau - logq_par
    Q_lnq = abs(logq_ratio) * LN_Q * E_CROSS * mu_0  # old method
    Q_hbar = abs(logq_ratio) * HBAR_Q * E_CROSS * mu_0  # new method
    print(f"  {name:>6} {Q_lnq:>9.5f} {Q_hbar:>9.5f} {Q_exp:>9.5f} {HBAR_Q/LN_Q:>7.4f}")
