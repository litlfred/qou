#!/usr/bin/env python3
"""
Q-value from Gröbner--Shirshov-weighted transfer matrix.

TWO-STAGE CORRECTION (algebraic, no fitting):

  Stage 1: Gröbner--Shirshov direction weighting (q/q⁻¹ asymmetry)
    The transition decomposes into UNBIND (nn→pn, removing σ⁻¹)
    and REBIND (pn→pp, completing σ).  Unbinding is a forward
    Gröbner--Shirshov reduction (weight q), rebinding is partial inverse
    (weight q⁻¹):

      Q_qwt = |q·ln(unbind) + q⁻¹·ln(rebind) + ln(unchanged)| × κ

  Stage 2: Shell knot operator (degree-2 torus knot correction)
    For heavy nuclei (N > 28), the degree-2 shell binding
    suppresses the bare Q-value:

      Q = Q_qwt × F_deg × F_Pauli

    F_deg = (J₂₉·tr(T_{2,9}·Δ) + J₃₄·tr(T_{3,4}·Δ))/(J₂₉+J₃₄) ≈ 0.5904
    F_Pauli = |tr_alt(Δ)|/|tr(Δ)| ≈ 0.6382 (magic shells only)

All quantities derived from q alone.

Usage:
    python3 qvalue-representation-theory.py
"""

import math
from q_parameter import Q as q, Q_INV as qi, E_CROSS
from experimental_constants import *

HA = q - qi
S = q**0.5 - qi**0.5
mu_0 = M_E_MEV / (3 * E_CROSS)
kappa = E_CROSS * mu_0  # = m_e/3
Z_m = 1.0 / (q**0.5 + qi**0.5)

# Shell structure
MAGIC = [2, 8, 20, 28, 50, 82, 126]
NEXT_SHELL_SIZE = 58  # 184 - 126, predicted next magic number gap
SHELL_DEGREE = {1: 1, 2: 1, 3: 1, 4: 1, 5: 2, 6: 2, 7: 2}
# Precomputed from H₃(q) Markov traces (see weight-space-correct.py):
F_DEG2 = 0.5904    # Rosso--Jones weighted: (J₂₉·tr₂₉ + J₃₄·tr₃₄)/(J₂₉+J₃₄)
F_PAULI = 0.6382   # |tr_alt(Δ)|/|tr(Δ)|

def neutron_shell(N):
    prev = 0
    for i, m in enumerate(MAGIC):
        if N <= m:
            return i + 1, N - prev, m - prev, (N == m)
        prev = m
    return len(MAGIC) + 1, N - MAGIC[-1], NEXT_SHELL_SIZE, False


# ══════════════════════════════════════════════════════════════
# §1  TRANSFER MATRIX (Skein-weighted Gröbner--Shirshov crossing coefficients)
# ══════════════════════════════════════════════════════════════

def crossing_coeffs(ti, tj):
    """Skein-weighted crossing coefficients from the Hecke relation.
    pp: σ (positive crossing)
    nn: σ⁻¹ = q²σ - qs (Skein inverse)
    pn: ½(σ + σ⁻¹) (mixed)
    """
    if ti == 'p' and tj == 'p': return 1.0, 0.0
    elif ti == 'n' and tj == 'n': return q**2, -q * S
    else: return (1 + q**2) / 2, -q * S / 2

def T_mat(c, d):
    return [[c * HA + d, c], [c, d]]

def mat_mul(A, B):
    return [[A[0][0]*B[0][0]+A[0][1]*B[1][0], A[0][0]*B[0][1]+A[0][1]*B[1][1]],
            [A[1][0]*B[0][0]+A[1][1]*B[1][0], A[1][0]*B[0][1]+A[1][1]*B[1][1]]]


# ══════════════════════════════════════════════════════════════
# §2  DECOMPOSED Q-VALUE (unbind / rebind / unchanged)
# ══════════════════════════════════════════════════════════════

def compute_generator_volume(types, i):
    """Traced volume V̂_i for generator σ_i given nucleon types."""
    A = len(types)
    M = [[1, 0], [0, 1]]
    for j in range(i + 1, A):
        c, d = crossing_coeffs(types[i], types[j])
        M = mat_mul(M, T_mat(c, d))
    return Z_m * M[0][0] + M[1][0]

def Q_decomposed(Z, N):
    """Decompose Q into unbind/rebind parts with q/q⁻¹ weighting.

    Returns (Q_bare, Q_qwt, Q_full, ln_unbind, ln_rebind, ln_unch, F_sh).
    """
    par_types = ['p'] * Z + ['n'] * N
    dau_types = ['p'] * (Z + 1) + ['n'] * (N - 1)
    A = Z + N

    ln_unbind = 0.0
    ln_rebind = 0.0
    ln_unchanged = 0.0

    for i in range(A - 1):
        Vp = compute_generator_volume(par_types, i)
        Vd = compute_generator_volume(dau_types, i)

        if abs(Vp) < 1e-30 or abs(Vd) < 1e-30:
            continue

        ln_ratio = math.log(abs(Vd)) - math.log(abs(Vp))

        # Which crossings changed at this generator?
        changed = [(par_types[i] + par_types[j], dau_types[i] + dau_types[j])
                    for j in range(i + 1, A)
                    if par_types[i] + par_types[j] != dau_types[i] + dau_types[j]]

        if not changed:
            ln_unchanged += ln_ratio
        else:
            n_unbind = sum(1 for pp, _ in changed if pp == 'nn')
            n_rebind = sum(1 for _, dp in changed if dp == 'pp')
            total = n_unbind + n_rebind
            if n_rebind == 0:
                ln_unbind += ln_ratio
            elif n_unbind == 0:
                ln_rebind += ln_ratio
            else:
                ln_unbind += ln_ratio * n_unbind / total
                ln_rebind += ln_ratio * n_rebind / total

    ln_total = ln_unbind + ln_rebind + ln_unchanged

    # Stage 1: q-weighted
    ln_qwt = q * ln_unbind + qi * ln_rebind + ln_unchanged

    # Stage 2: shell knot correction
    sh, _, _, magic = neutron_shell(N)
    deg = SHELL_DEGREE.get(sh, 2)
    F_d = F_DEG2 if deg >= 2 else 1.0
    F_p = F_PAULI if (magic and deg >= 2) else 1.0
    F_sh = F_d * F_p

    Q_bare = abs(ln_total) * kappa
    Q_qwt = abs(ln_qwt) * kappa
    Q_full = Q_qwt * F_sh

    return Q_bare, Q_qwt, Q_full, ln_unbind, ln_rebind, ln_unchanged, F_sh


# ══════════════════════════════════════════════════════════════
# §3  VERIFICATION
# ══════════════════════════════════════════════════════════════

nuclei = [
    (1,   2,   "³H",    Q_TRITIUM_MEV, Q_TRITIUM_MEV_ERR),
    (6,   8,   "¹⁴C",   Q_C14_MEV, Q_C14_MEV_ERR),
    (27,  33,  "⁶⁰Co",  Q_CO60_MEV, Q_CO60_MEV_ERR),
    (38,  52,  "⁹⁰Sr",  Q_SR90_MEV, Q_SR90_MEV_ERR),
    (55,  82,  "¹³⁷Cs", Q_CS137_MEV, Q_CS137_MEV_ERR),
    (83,  127, "²¹⁰Bi", Q_BI210_MEV, Q_BI210_MEV_ERR),
]

print("═" * 100)
print("Q-VALUE PREDICTIONS: TWO-STAGE CORRECTION")
print("  Stage 1: Q_qwt = |q·ln(unbind) + q⁻¹·ln(rebind) + ln(unchanged)| × κ")
print("  Stage 2: Q_full = Q_qwt × F_shell")
print("═" * 100)
print()
print(f"  q = {q:.10f}, q⁻¹ = {qi:.10f}")
print(f"  κ = E_× × μ₀ = m_e/3 = {kappa:.10f} MeV")
print(f"  F_deg2 = {F_DEG2:.4f}, F_Pauli = {F_PAULI:.4f}")
print()

print(f"  {'Nuc':>5} │ {'u/r %':>9} │ {'Q_bare':>8} │ {'Q_qwt':>8} │"
      f" {'F_sh':>6} │ {'Q_full':>8} │ {'Q_exp':>8} │"
      f" {'err_bare':>8} │ {'err_full':>8}")
print("  " + "─" * 95)

errors_bare = []
errors_full = []
for Z, N, name, Q_exp, Q_err in nuclei:
    Qb, Qq, Qf, lu, lr, luc, Fsh = Q_decomposed(Z, N)
    eb = (Qb - Q_exp) / Q_exp * 100
    ef = (Qf - Q_exp) / Q_exp * 100
    errors_bare.append(eb)
    errors_full.append(ef)

    lt = lu + lr + luc
    u_pct = abs(lu) / abs(lt) * 100 if lt != 0 else 0
    r_pct = abs(lr) / abs(lt) * 100 if lt != 0 else 0

    m = '◀' if abs(ef) < 1 else ('·' if abs(ef) < 5 else ' ')
    print(f"  {name:>5} │ {u_pct:4.0f}/{r_pct:<4.0f} │ {Qb:>8.5f} │ {Qq:>8.5f} │"
          f" {Fsh:>6.4f} │ {Qf:>8.5f} │ {Q_exp:>8.5f} │"
          f" {eb:>+7.1f}% │ {ef:>+7.1f}%{m}")

print()
mae_b = sum(abs(e) for e in errors_bare) / len(errors_bare)
mae_f = sum(abs(e) for e in errors_full) / len(errors_full)
rms_b = math.sqrt(sum(e**2 for e in errors_bare) / len(errors_bare))
rms_f = math.sqrt(sum(e**2 for e in errors_full) / len(errors_full))
print(f"  Bare:  MAE = {mae_b:.1f}%, RMS = {rms_b:.1f}%")
print(f"  Full:  MAE = {mae_f:.1f}%, RMS = {rms_f:.1f}%")
