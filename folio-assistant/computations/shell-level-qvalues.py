#!/usr/bin/env python3
"""
Shell-level Q-values: H_K(q) with K shells instead of H_A(q).

Each shell is a "super-nucleon" with (p_i, n_i) proton/neutron
content. The inter-shell crossing coefficient is a COMPOSITE:
  T_shell(I, J) = T_pp^{p_I·p_J} × T_nn^{n_I·n_J} × T_mix^{p_I·n_J + n_I·p_J}

This reduces A=210 (bismuth) to K=7 shells: O(K²) = O(49) instead of O(A²) = O(44100).

The shell filling follows the Mayer-Jensen sequence:
  1s₁/₂(2), 1p₃/₂(4), 1p₁/₂(2), 1d₅/₂(6), 2s₁/₂(2), 1d₃/₂(4),
  1f₇/₂(8), 2p₃/₂(4), 1f₅/₂(6), 2p₁/₂(2), 1g₉/₂(10), ...

Magic numbers arise at cumulative: 2, 8, 20, 28, 50, 82, 126.

Usage:
    python3 shell-level-qvalues.py
"""

import json
import math
import time
from datetime import datetime, timezone
from pathlib import Path

from q_parameter import Q as q, Q_INV as qi, E_CROSS, HBAR_Q
from experimental_constants import (
    M_E_MEV, Q_TRITIUM_MEV, Q_TRITIUM_MEV_ERR,
    Q_C14_MEV, Q_C14_MEV_ERR, Q_CO60_MEV, Q_CO60_MEV_ERR,
    Q_SR90_MEV, Q_SR90_MEV_ERR, Q_CS137_MEV, Q_CS137_MEV_ERR,
    Q_BI210_MEV, Q_BI210_MEV_ERR,
)

HA = q - qi
Z_m = 1.0 / (q**0.5 + q**(-0.5))
mu_0 = M_E_MEV / (3 * E_CROSS)
ln_q = math.log(q)

def q_int(n):
    return (q**n - qi**n) / HA

print(f"Shell-level Q-values")
print(f"q = {q:.10f}")
print()

# ── Mayer-Jensen shell filling ──────────────────────────────────

# Subshell capacities in filling order
# (label, capacity, cumulative = magic if at closure)
SUBSHELLS = [
    ("1s1/2",  2,   2),   # magic 2
    ("1p3/2",  4,   6),
    ("1p1/2",  2,   8),   # magic 8
    ("1d5/2",  6,  14),
    ("2s1/2",  2,  16),
    ("1d3/2",  4,  20),   # magic 20
    ("1f7/2",  8,  28),   # magic 28
    ("2p3/2",  4,  32),
    ("1f5/2",  6,  38),
    ("2p1/2",  2,  40),
    ("1g9/2", 10,  50),   # magic 50
    ("1g7/2",  8,  58),
    ("2d5/2",  6,  64),
    ("2d3/2",  4,  68),
    ("3s1/2",  2,  70),
    ("1h11/2",12,  82),   # magic 82
    ("1h9/2", 10,  92),
    ("2f7/2",  8, 100),
    ("2f5/2",  6, 106),
    ("3p3/2",  4, 110),
    ("3p1/2",  2, 112),
    ("1i13/2",14, 126),   # magic 126
    ("1i11/2",12, 138),
    ("2g9/2", 10, 148),
    ("2g7/2",  8, 156),
]

MAGIC = {2, 8, 20, 28, 50, 82, 126}

def fill_shells(N):
    """Fill N nucleons into Mayer-Jensen shells.
    Returns list of (label, occupancy, capacity) for each subshell."""
    remaining = N
    filled = []
    for label, cap, cumul in SUBSHELLS:
        occ = min(remaining, cap)
        if occ > 0:
            filled.append((label, occ, cap))
        remaining -= occ
        if remaining <= 0:
            break
    return filled

def group_into_major_shells(filled):
    """Group subshells into major shells at magic closures.
    Returns list of (shell_label, total_occupancy) where closures
    define shell boundaries."""
    shells = []
    current_occ = 0
    current_labels = []
    cumul = 0
    for label, occ, cap in filled:
        current_occ += occ
        current_labels.append(label)
        cumul += occ
        if cumul in MAGIC or occ < cap:  # magic closure or partially filled
            shells.append(('/'.join(current_labels), current_occ))
            current_occ = 0
            current_labels = []
    if current_occ > 0:
        shells.append(('/'.join(current_labels), current_occ))
    return shells

# ── 2×2 transfer matrix ────────────────────────────────────────

def T_mat(c, d):
    return [[c*HA+d, c], [c, d]]

def mat_mul(A, B):
    return [[A[0][0]*B[0][0]+A[0][1]*B[1][0], A[0][0]*B[0][1]+A[0][1]*B[1][1]],
            [A[1][0]*B[0][0]+A[1][1]*B[1][0], A[1][0]*B[0][1]+A[1][1]*B[1][1]]]

def mat_pow(M, k):
    """Matrix power M^k via repeated squaring."""
    if k == 0:
        return [[1,0],[0,1]]
    if k == 1:
        return [row[:] for row in M]
    if k % 2 == 0:
        half = mat_pow(M, k // 2)
        return mat_mul(half, half)
    else:
        return mat_mul(M, mat_pow(M, k - 1))

def vol(M):
    return Z_m * M[0][0] + M[1][0]

T_pp = T_mat(1.0, 0.0)
T_nn = T_mat(1.0, -HA)
T_mix = T_mat(1.0, -HA/2)

# ── Shell-level Skein polynomial ────────────────────────────────

def shell_log_skein(p, n):
    """Compute log|P| at the SHELL level.

    Group nucleons by shell. Each shell I has (p_I, n_I).
    Inter-shell crossing between I and J (I < J):
      p_I·p_J pp crossings + n_I·n_J nn crossings + (p_I·n_J + n_I·p_J) mix crossings
    These all act at the same shell-level generator σ_I.

    The composite transfer matrix:
      T_composite(I,J) = T_pp^{pp_count} × T_nn^{nn_count} × T_mix^{mix_count}
    """
    # Fill proton and neutron shells independently
    p_shells = fill_shells(p)
    n_shells = fill_shells(n)

    # Group into major shells
    p_major = group_into_major_shells(p_shells)
    n_major = group_into_major_shells(n_shells)

    # Merge into combined shells: each major shell has (p_i, n_i)
    # Align by magic number boundaries
    all_magic = sorted(MAGIC)

    combined = []
    p_idx, n_idx = 0, 0
    p_cumul, n_cumul = 0, 0

    for magic in all_magic:
        shell_p = 0
        while p_idx < len(p_major) and p_cumul + p_major[p_idx][1] <= magic:
            shell_p += p_major[p_idx][1]
            p_cumul += p_major[p_idx][1]
            p_idx += 1
        # Partial fill
        if p_idx < len(p_major) and p_cumul < magic:
            partial = min(p_major[p_idx][1], magic - p_cumul)
            shell_p += partial
            # Don't advance p_idx (partially consumed)
            p_cumul += partial
            if partial == p_major[p_idx][1]:
                p_idx += 1

        shell_n = 0
        while n_idx < len(n_major) and n_cumul + n_major[n_idx][1] <= magic:
            shell_n += n_major[n_idx][1]
            n_cumul += n_major[n_idx][1]
            n_idx += 1
        if n_idx < len(n_major) and n_cumul < magic:
            partial = min(n_major[n_idx][1], magic - n_cumul)
            shell_n += partial
            n_cumul += partial
            if partial == n_major[n_idx][1]:
                n_idx += 1

        if shell_p > 0 or shell_n > 0:
            combined.append((shell_p, shell_n))

    # Remaining nucleons beyond magic 126
    rem_p = p - p_cumul
    rem_n = n - n_cumul
    if rem_p > 0 or rem_n > 0:
        combined.append((rem_p, rem_n))

    K = len(combined)

    # Compute shell-level transfer matrix chain
    log_P = 0.0
    for I in range(K - 1):
        M = [[1,0],[0,1]]
        for J in range(I + 1, K):
            pI, nI = combined[I]
            pJ, nJ = combined[J]

            # Crossing counts between shells I and J
            n_pp = pI * pJ
            n_nn = nI * nJ
            n_mix = pI * nJ + nI * pJ

            # Composite transfer matrix: T_pp^{n_pp} × T_nn^{n_nn} × T_mix^{n_mix}
            if n_pp > 0:
                M = mat_mul(M, mat_pow(T_pp, n_pp))
            if n_nn > 0:
                M = mat_mul(M, mat_pow(T_nn, n_nn))
            if n_mix > 0:
                M = mat_mul(M, mat_pow(T_mix, n_mix))

        V = vol(M)
        if abs(V) > 0:
            log_P += math.log(abs(V))
        else:
            return float('-inf'), combined

    return log_P, combined

# ── Also compute naive Level 0 for comparison ──────────────────

def nucleon_log_skein(ordering):
    """Nucleon-level transfer matrix with any ordering."""
    A = len(ordering)
    log_P = 0.0
    for i in range(A - 1):
        M = [[1,0],[0,1]]
        for j in range(i + 1, A):
            ti, tj = ordering[i], ordering[j]
            if ti == 'p' and tj == 'p': c, d = 1.0, 0.0
            elif ti == 'n' and tj == 'n': c, d = 1.0, -HA
            else: c, d = 1.0, -HA/2
            T = T_mat(c, d)
            M = mat_mul(M, T)
        V = vol(M)
        if abs(V) > 0:
            log_P += math.log(abs(V))
    return log_P

def naive_log_skein(p, n):
    return nucleon_log_skein(['p']*p + ['n']*n)

def shell_ordering(p, n):
    """Mayer-Jensen shell ordering: nucleons grouped by shell,
    alternating p/n within each shell.

    Returns list of 'p'/'n' of length A = p+n.
    """
    p_shells = fill_shells(p)
    n_shells = fill_shells(n)

    # Build ordered nucleon list: for each subshell,
    # interleave protons and neutrons
    ordering = []

    # Track how many p and n remain in each subshell
    p_by_sub = {label: occ for label, occ, _ in p_shells}
    n_by_sub = {label: occ for label, occ, _ in n_shells}

    for label, cap, cumul in SUBSHELLS:
        pi = p_by_sub.get(label, 0)
        ni = n_by_sub.get(label, 0)
        if pi == 0 and ni == 0:
            continue
        # Interleave p and n within this subshell
        pj, nj = 0, 0
        for k in range(pi + ni):
            if pj < pi and (nj >= ni or k % 2 == 0):
                ordering.append('p')
                pj += 1
            else:
                ordering.append('n')
                nj += 1

    assert len(ordering) == p + n, f"ordering length {len(ordering)} != {p+n}"
    assert ordering.count('p') == p
    assert ordering.count('n') == n
    return ordering

def shell_ordered_log_skein(p, n):
    """Nucleon-level transfer matrix with Mayer-Jensen shell ordering."""
    return nucleon_log_skein(shell_ordering(p, n))

# ── All 6 nuclei ────────────────────────────────────────────────

nuclei = [
    (1,   2,   "³H",    Q_TRITIUM_MEV, Q_TRITIUM_MEV_ERR),
    (6,   8,   "¹⁴C",   Q_C14_MEV, Q_C14_MEV_ERR),
    (27,  33,  "⁶⁰Co",  Q_CO60_MEV, Q_CO60_MEV_ERR),
    (38,  52,  "⁹⁰Sr",  Q_SR90_MEV, Q_SR90_MEV_ERR),
    (55,  82,  "¹³⁷Cs", Q_CS137_MEV, Q_CS137_MEV_ERR),
    (83,  127, "²¹⁰Bi", Q_BI210_MEV, Q_BI210_MEV_ERR),
]

print(f"{'Nuc':>6} {'Q_naive':>9} {'Q_shord':>9} {'Q_shlvl':>9} {'Q_exp±δ':>12} "
      f"{'err_n':>7} {'err_o':>7} {'err_l':>7} {'time':>6}")
print("-" * 85)

results = []
for p, n, name, Q_exp, Q_err in nuclei:
    t0 = time.time()

    # Shell level
    lp_par_s, shells_par = shell_log_skein(p, n)
    lp_dau_s, shells_dau = shell_log_skein(p + 1, n - 1)
    K_par = len(shells_par)
    K_dau = len(shells_dau)

    ln_shell = lp_dau_s - lp_par_s
    logq_shell = ln_shell / ln_q
    Q_shell = abs(ln_shell) * E_CROSS * mu_0

    # Shell-ordered nucleon level
    lp_par_o = shell_ordered_log_skein(p, n)
    lp_dau_o = shell_ordered_log_skein(p + 1, n - 1)
    ln_shord = lp_dau_o - lp_par_o
    Q_shord = abs(ln_shord) * E_CROSS * mu_0

    # Naive level 0
    lp_par_n = naive_log_skein(p, n)
    lp_dau_n = naive_log_skein(p + 1, n - 1)
    ln_naive = lp_dau_n - lp_par_n
    Q_naive = abs(ln_naive) * E_CROSS * mu_0

    elapsed = time.time() - t0

    err_n = (Q_naive - Q_exp) / Q_exp * 100
    err_o = (Q_shord - Q_exp) / Q_exp * 100
    err_s = (Q_shell - Q_exp) / Q_exp * 100

    print(f"{name:>6} {Q_naive:>9.5f} {Q_shord:>9.5f} {Q_shell:>9.5f} "
          f"{Q_exp:>7.5f}±{Q_err:.0e} "
          f"{err_n:>+6.1f}% {err_o:>+6.1f}% {err_s:>+6.1f}% {elapsed:>5.2f}s")

    results.append({
        "name": name, "p": p, "n": n, "A": p+n,
        "K_par": K_par, "K_dau": K_dau,
        "shells_par": shells_par, "shells_dau": shells_dau,
        "Q_naive": Q_naive, "Q_shell": Q_shell,
        "Q_exp": Q_exp, "Q_err": Q_err,
        "Q_shord": Q_shord, "err_shord": err_o,
        "err_naive": err_n, "err_shell": err_s,
    })

# Show shell structure for each nucleus
print()
print("Shell structures:")
for r in results:
    print(f"  {r['name']}: parent shells = {r['shells_par']}")
    print(f"  {' '*len(r['name'])}  daughter    = {r['shells_dau']}")

# ── Witness ─────────────────────────────────────────────────────

witness = {
    "computation": "shell-level-qvalues",
    "timestamp": datetime.now(timezone.utc).isoformat(),
    "parameters": {"q": q, "E_cross": E_CROSS, "mu_0": mu_0},
    "results": results,
}
out = Path(__file__).parent / "shell-level-qvalues.witness.json"
with open(out, "w") as f:
    json.dump(witness, f, indent=2)
print(f"\nWitness: {out}")
