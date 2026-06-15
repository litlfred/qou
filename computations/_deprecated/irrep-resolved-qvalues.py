#!/usr/bin/env python3
"""
Irrep-resolved Q-values from torus knot representation theory.

The Q-value correction factor comes from the Schur-Weyl decomposition
of the shell occupation state under the 3-strand Iwahori--Hecke algebra H₃(q).

For a shell of size n with k occupied fermions, the weak vertex (a 3-strand
braid) acts on 3 positions within the shell. The fermion antisymmetry
constrains which H₃(q) irreps contribute:

  P(3 occupied) → alternating irrep (fully antisymmetric)
  P(2 occupied) → standard irrep (mixed symmetry)
  P(1 occupied) → symmetric ⊕ standard (no constraint from 1 particle)
  P(0 occupied) → no contribution

The combinatorial weights are:
  w₃ = C(k,3)/C(n,3)
  w₂ = C(k,2)·(n-k)/C(n,3)
  w₁ = k·C(n-k,2)/C(n,3)
  w₀ = C(n-k,3)/C(n,3)

The effective operator average of Δ_mix in the shell is:
  ⟨Δ⟩_eff = w₃·tr_alt + w₂·tr_std + w₁·(tr_sym/3 + 2·tr_std/3)

For degree-d shells (d ≥ 2), the knot correction multiplies:
  Q = Q_bare × ⟨Δ⟩_eff/⟨Δ⟩_full × F_knot(d)

where F_knot(d) = tr(T_knot · Δ_mix) for the degree-d torus knot.

Usage:
    python3 irrep-resolved-qvalues.py
"""

import math
from math import comb
from q_parameter import Q as q, Q_INV as qi, E_CROSS, HBAR_Q, q_int
from hecke_division import HeckeDivision, HeckeElement
from experimental_constants import *

div = HeckeDivision(q_val=q)
HA = q - qi
LN_Q = math.log(q)
mu_0 = M_E_MEV / (3 * E_CROSS)

def sigma(i):
    return HeckeElement({(i,): 1.0})
def sigma_inv(i):
    return HeckeElement({(i,): 1.0, (): -HA})

# ── YOUNG SYMMETRIZER IDEMPOTENTS ─────────────────────────────

S3 = [
    ((), 0), ((0,), 1), ((1,), 1),
    ((0,1), 2), ((1,0), 2), ((0,1,0), 3),
]

def poincare_S3(t):
    return 1 + 2*t + 2*t**2 + t**3

P3_q2 = poincare_S3(q**2)
P3_qi2 = poincare_S3(qi**2)

# Symmetric idempotent
e_sym = HeckeElement.zero()
for word, length in S3:
    e_sym = e_sym + HeckeElement({word: q**length / P3_q2})
e_sym, _ = div.reduce(e_sym)

# Alternating idempotent
e_alt = HeckeElement.zero()
for word, length in S3:
    e_alt = e_alt + HeckeElement({word: (-qi)**length / P3_qi2})
e_alt, _ = div.reduce(e_alt)

# Standard idempotent
e_std = HeckeElement.identity() + e_sym.scale(-1.0) + e_alt.scale(-1.0)
e_std, _ = div.reduce(e_std)

# ── Δ_mix AND IRREP TRACES ───────────────────────────────────

DELTA_MIX = sigma(0) * sigma_inv(1)
DELTA_MIX, _ = div.reduce(DELTA_MIX)
tr_delta = div.markov_trace(DELTA_MIX, 3)

# Irrep-resolved traces of Δ_mix
irrep_traces = {}
for name, e_lam in [("sym", e_sym), ("std", e_std), ("alt", e_alt)]:
    proj = e_lam * DELTA_MIX * e_lam
    proj, _ = div.reduce(proj)
    irrep_traces[name] = div.markov_trace(proj, 3)

tr_sym = irrep_traces["sym"]
tr_std = irrep_traces["std"]
tr_alt = irrep_traces["alt"]

print(f"q = {q:.10f}")
print(f"Δ_mix irrep traces:")
print(f"  tr_sym = {tr_sym:+.10f}")
print(f"  tr_std = {tr_std:+.10f}")
print(f"  tr_alt = {tr_alt:+.10f}")
print(f"  total  = {tr_delta:+.10f}")
print()

# ── TORUS KNOT TRACES ────────────────────────────────────────

def build_torus_knot(r, s):
    e = HeckeElement.identity()
    for _ in range(s):
        for i in range(r - 1):
            e = e * sigma(i)
        e, _ = div.reduce(e)
    return e

# Compute T·Δ traces for all 6 embeddable knots
KNOTS = [
    (2, 3, 1, "T₂₃"),
    (2, 5, 1, "T₂₅"),
    (2, 7, 1, "T₂₇"),
    (3, 5, 1, "T₃₅"),
    (2, 9, 2, "T₂₉"),
    (3, 4, 2, "T₃₄"),
]

knot_traces = {}
knot_irrep = {}
print("Torus knot · Δ_mix traces:")
for r, s, deg, label in KNOTS:
    T = build_torus_knot(r, s)
    T_delta = T * DELTA_MIX
    T_delta, _ = div.reduce(T_delta)
    tr_Td = div.markov_trace(T_delta, 3)
    knot_traces[(r, s)] = tr_Td

    # Irrep decomposition of T·Δ
    traces = {}
    for name, e_lam in [("sym", e_sym), ("std", e_std), ("alt", e_alt)]:
        proj = e_lam * T_delta * e_lam
        proj, _ = div.reduce(proj)
        traces[name] = div.markov_trace(proj, 3)
    knot_irrep[(r, s)] = traces

    print(f"  {label} (deg {deg}): tr = {tr_Td:.10f}")
    print(f"    sym={traces['sym']:+.10f}, std={traces['std']:+.10f}, alt={traces['alt']:+.10f}")

print()

# ── SHELL STRUCTURE ──────────────────────────────────────────

# Magic numbers derived from 6 embeddable torus knots on Σ₄
MAGIC = [2, 8, 20, 28, 50, 82, 126]

# Shell assignments: (start, end, size, torus_knot, degree)
SHELLS = [
    (0,   2,  2,  (2, 3), 1),  # Shell 1: trefoil
    (2,   8,  6,  (2, 5), 1),  # Shell 2
    (8,  20, 12,  (2, 7), 1),  # Shell 3
    (20, 28,  8,  (3, 5), 1),  # Shell 4: weak vertex
    (28, 50, 22,  (2, 9), 2),  # Shell 5: degree-2
    (50, 82, 32,  (3, 4), 2),  # Shell 6: degree-2
    (82,126, 44,  (2, 9), 2),  # Shell 7: degree-2 tower
]

def get_shell_info(X):
    """Return (shell_index, shell_start, shell_end, shell_size, knot, degree, occupancy)
    for a nucleon number X."""
    for i, (start, end, size, knot, deg) in enumerate(SHELLS):
        if start < X <= end:
            return i, start, end, size, knot, deg, X - start
        elif X == 0:
            return 0, 0, 2, 2, (2, 3), 1, 0
    # Beyond shell 7
    if X > 126:
        return 7, 126, 184, 58, (3, 4), 2, X - 126
    return 0, 0, 2, 2, (2, 3), 1, X

def is_magic(X):
    return X in MAGIC

# ── SCHUR-WEYL OCCUPATION WEIGHTS ────────────────────────────

def occupation_weights(k, n):
    """Compute the Schur-Weyl occupation weights for k fermions in n positions.

    Returns (w_sym, w_std, w_alt): the weight of each H₃(q) irrep
    from the combinatorial structure of the occupation.
    """
    if n < 3:
        # Shell too small for full S₃ action
        if n == 2:
            if k == 2:
                # 2 fermions in 2 positions: fully antisymmetric pair
                # S₃ on 2 positions: only S₂ subgroup acts
                # Result: standard representation dominates
                return (0.0, 1.0, 0.0)
            elif k == 1:
                return (1.0, 0.0, 0.0)
            else:
                return (1.0, 0.0, 0.0)
        else:
            return (1.0, 0.0, 0.0)

    if k == 0:
        return (1.0, 0.0, 0.0)

    cn3 = comb(n, 3)

    # P(3 of the 3 positions are occupied) → alternating
    w3 = comb(k, 3) / cn3 if k >= 3 else 0.0

    # P(2 of the 3 positions are occupied) → standard
    w2 = comb(k, 2) * (n - k) / cn3 if k >= 2 else 0.0

    # P(1 of the 3 positions are occupied) → 1/3 sym + 2/3 std
    w1 = k * comb(n - k, 2) / cn3 if n - k >= 2 else 0.0

    # P(0 of the 3 positions are occupied) → trivial/no action
    w0 = comb(n - k, 3) / cn3 if n - k >= 3 else 0.0

    # Normalize to get irrep weights (excluding w₀)
    # w₁ decomposes as: 1/3 symmetric + 2/3 standard (from ℂ³ = triv ⊕ std)
    w_alt = w3
    w_std = w2 + (2.0 / 3.0) * w1
    w_sym = (1.0 / 3.0) * w1 + w0

    # Verify: w_alt + w_std + w_sym should = 1
    total = w_alt + w_std + w_sym
    if total > 0:
        w_alt /= total
        w_std /= total
        w_sym /= total

    return (w_sym, w_std, w_alt)


def effective_trace(k, n, knot=None):
    """Compute the effective operator average ⟨Δ_mix⟩_eff for a shell
    with k occupied fermions out of n positions.

    If knot is given, uses the knot·Δ traces. Otherwise uses bare Δ.
    """
    w_sym, w_std, w_alt = occupation_weights(k, n)

    if knot and knot in knot_irrep:
        tr_s = knot_irrep[knot]["sym"]
        tr_d = knot_irrep[knot]["std"]
        tr_a = knot_irrep[knot]["alt"]
    else:
        tr_s = tr_sym
        tr_d = tr_std
        tr_a = tr_alt

    return w_sym * tr_s + w_std * tr_d + w_alt * tr_a


# ── TRANSFER MATRIX Q_bare ───────────────────────────────────

def crossing_coeffs(ti, tj):
    if ti == 'p' and tj == 'p': return 1.0, 0.0
    elif ti == 'n' and tj == 'n': return 1.0, -(q - qi)
    else: return 1.0, -(q - qi)/2

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

def bare_Q(Z, N):
    return abs(_log_skein(Z+1, N-1) - _log_skein(Z, N)) * E_CROSS * mu_0


def valence_Q(Z, N):
    """Q computed from valence nucleons only (above last closed shell)."""
    # Find proton and neutron cores
    Z_core = 0
    for m in MAGIC:
        if m <= Z: Z_core = m
    N_core = 0
    for m in MAGIC:
        if m <= N: N_core = m

    Z_val = Z - Z_core
    N_val = N - N_core

    # If one of the valence counts is 0, use the previous shell
    if N_val == 0 and N > 0:
        # N is exactly magic — the converting neutron comes from this shell
        prev = 0
        for m in MAGIC:
            if m < N: prev = m
        N_core = prev
        N_val = N - prev

    if Z_val == 0 and Z > 0:
        prev = 0
        for m in MAGIC:
            if m < Z: prev = m
        Z_core = prev
        Z_val = Z - prev

    # Daughter: Z+1, N-1
    # For the daughter, valence changes by ±1
    # But the daughter may have a different core structure
    Z_d = Z + 1
    N_d = N - 1
    Z_core_d = 0
    for m in MAGIC:
        if m <= Z_d: Z_core_d = m
    N_core_d = 0
    for m in MAGIC:
        if m <= N_d: N_core_d = m

    Z_val_d = Z_d - Z_core_d
    N_val_d = N_d - N_core_d

    if N_val_d == 0 and N_d > 0:
        prev = 0
        for m in MAGIC:
            if m < N_d: prev = m
        N_core_d = prev
        N_val_d = N_d - prev

    if Z_val_d == 0 and Z_d > 0:
        prev = 0
        for m in MAGIC:
            if m < Z_d: prev = m
        Z_core_d = prev
        Z_val_d = Z_d - prev

    # Compute Q from valence nucleons
    def log_skein_valence(p, n):
        types = ['p']*p + ['n']*n; A = p+n; logP = 0.0
        for i in range(A-1):
            M = [[1,0],[0,1]]
            for j in range(i+1, A):
                c, d = crossing_coeffs(types[i], types[j])
                M = mat_mul(M, T_mat(c, d))
            V = vol(M)
            if abs(V) > 0: logP += math.log(abs(V))
        return logP

    log_par = log_skein_valence(Z_val, N_val)
    log_dau = log_skein_valence(Z_val_d, N_val_d)

    return abs(log_dau - log_par) * E_CROSS * mu_0, Z_val, N_val, Z_val_d, N_val_d


# ── TEST NUCLEI ──────────────────────────────────────────────

nuclei = [
    (1,   2,   "³H",    Q_TRITIUM_MEV, Q_TRITIUM_MEV_ERR),
    (6,   8,   "¹⁴C",   Q_C14_MEV, Q_C14_MEV_ERR),
    (27,  33,  "⁶⁰Co",  Q_CO60_MEV, Q_CO60_MEV_ERR),
    (38,  52,  "⁹⁰Sr",  Q_SR90_MEV, Q_SR90_MEV_ERR),
    (55,  82,  "¹³⁷Cs", Q_CS137_MEV, Q_CS137_MEV_ERR),
    (83,  127, "²¹⁰Bi", Q_BI210_MEV, Q_BI210_MEV_ERR),
]

# ── APPROACH 1: VALENCE-ONLY Q ───────────────────────────────

print("=" * 80)
print("APPROACH 1: VALENCE-ONLY Q")
print("(Only count crossings among valence nucleons, above the last closed shell)")
print("=" * 80)
print()

for Z, N, name, Q_exp, Q_err in nuclei:
    Q_v, Zv, Nv, Zvd, Nvd = valence_Q(Z, N)
    Qb = bare_Q(Z, N)
    err_bare = (Qb - Q_exp) / Q_exp * 100
    err_val = (Q_v - Q_exp) / Q_exp * 100
    print(f"  {name:>5}: Z={Z},N={N} → valence par({Zv}p,{Nv}n) dau({Zvd}p,{Nvd}n)")
    print(f"         Q_bare={Qb:.5f} ({err_bare:+.1f}%), Q_val={Q_v:.5f} ({err_val:+.1f}%), Q_exp={Q_exp:.5f}")

print()

# ── APPROACH 2: SCHUR-WEYL OCCUPATION WEIGHTS ────────────────

print("=" * 80)
print("APPROACH 2: SCHUR-WEYL OCCUPATION WEIGHTS")
print("(Irrep weights from fermion occupation of converting neutron's shell)")
print("=" * 80)
print()

for Z, N, name, Q_exp, Q_err in nuclei:
    # Get the converting neutron's shell info
    si, start, end, size, knot, deg, occ = get_shell_info(N)
    w_sym, w_std, w_alt = occupation_weights(occ, size)

    # Effective operator average using knot traces
    tr_eff_knot = effective_trace(occ, size, knot)
    tr_eff_bare = effective_trace(occ, size, None)

    print(f"  {name:>5}: N={N}, shell {si+1} ({start}-{end}), size={size}, "
          f"occ={occ}/{size} ({occ/size:.2f})")
    print(f"         knot T_{{{knot[0]},{knot[1]}}}, deg {deg}")
    print(f"         weights: sym={w_sym:.4f}, std={w_std:.4f}, alt={w_alt:.4f}")
    print(f"         ⟨Δ⟩_eff(bare) = {tr_eff_bare:.10f}")
    print(f"         ⟨Δ⟩_eff(knot) = {tr_eff_knot:.10f}")
    print(f"         ⟨Δ⟩_full = {tr_delta:.10f}")
    print()

# ── APPROACH 3: COMBINED Q_bare × OCCUPATION CORRECTION ──────

print("=" * 80)
print("APPROACH 3: Q_bare × occupation-corrected operator average")
print("=" * 80)
print()

print(f"  {'Nuc':>5} {'Q_bare':>8} {'F_occ':>8} {'Q_corr':>8} {'Q_exp':>8} "
      f"{'err_bare':>8} {'err_corr':>8}")
print("  " + "-" * 70)

for Z, N, name, Q_exp, Q_err in nuclei:
    Qb = bare_Q(Z, N)
    si, start, end, size, knot, deg, occ = get_shell_info(N)

    # The correction factor: ratio of effective trace to full trace
    tr_eff = effective_trace(occ, size, knot if deg >= 2 else None)
    F_occ = abs(tr_eff) / abs(tr_delta) if abs(tr_delta) > 0 else 1.0

    # For degree-1 shells, the knot correction is already in Q_bare
    # For degree-2 shells, apply knot × occupation correction
    if deg >= 2:
        Q_corr = Qb * abs(knot_traces[knot]) * F_occ
    else:
        Q_corr = Qb * F_occ

    err_bare = (Qb - Q_exp) / Q_exp * 100
    err_corr = (Q_corr - Q_exp) / Q_exp * 100
    print(f"  {name:>5} {Qb:>8.5f} {F_occ:>8.4f} {Q_corr:>8.5f} {Q_exp:>8.5f} "
          f"{err_bare:>+7.1f}% {err_corr:>+7.1f}%")

print()

# ── APPROACH 4: PRODUCT OVER DEGREES ─────────────────────────

print("=" * 80)
print("APPROACH 4: Q = Q_bare × Π_d F_d (product over degree corrections)")
print("At each degree d, F_d = ⟨Δ⟩_eff / ⟨Δ⟩_full for the shells at that degree")
print("Degree 1: no correction (already in transfer matrix)")
print("Degree 2: from T_{2,9}, T_{3,4} representation theory")
print("=" * 80)
print()

print(f"  {'Nuc':>5} {'Q_bare':>8} {'F_deg':>8} {'Q_pred':>8} {'Q_exp':>8} "
      f"{'err_bare':>8} {'err_pred':>8} {'shell':>12}")
print("  " + "-" * 80)

for Z, N, name, Q_exp, Q_err in nuclei:
    Qb = bare_Q(Z, N)
    si_n, _, _, size_n, knot_n, deg_n, occ_n = get_shell_info(N)
    si_z, _, _, size_z, knot_z, deg_z, occ_z = get_shell_info(Z)

    # Daughter shell info
    si_nd, _, _, size_nd, knot_nd, deg_nd, occ_nd = get_shell_info(N - 1)
    si_zd, _, _, size_zd, knot_zd, deg_zd, occ_zd = get_shell_info(Z + 1)

    # Degree correction: product over shells involved in the transition
    F = 1.0
    shell_desc = f"N:sh{si_n+1}"

    # Neutron shell contribution (the converting neutron's shell)
    if deg_n >= 2:
        tr_eff_n = effective_trace(occ_n, size_n, knot_n)
        F_n = abs(tr_eff_n) / abs(tr_delta)
        F *= F_n
        shell_desc += f"(d{deg_n})"
    else:
        shell_desc += "(d1)"

    # Proton shell contribution (where the new proton goes)
    if deg_zd >= 2 and deg_zd != deg_n:
        # Different degree shell for proton destination
        tr_eff_zd = effective_trace(occ_zd, size_zd, knot_zd)
        F_zd = abs(tr_eff_zd) / abs(tr_delta)
        F *= F_zd
        shell_desc += f" Z:sh{si_zd+1}(d{deg_zd})"

    Q_pred = Qb * F
    err_bare = (Qb - Q_exp) / Q_exp * 100
    err_pred = (Q_pred - Q_exp) / Q_exp * 100
    print(f"  {name:>5} {Qb:>8.5f} {F:>8.4f} {Q_pred:>8.5f} {Q_exp:>8.5f} "
          f"{err_bare:>+7.1f}% {err_pred:>+7.1f}% {shell_desc:>12}")

print()

# ── APPROACH 5: VALENCE Q × KNOT CORRECTION ──────────────────

print("=" * 80)
print("APPROACH 5: VALENCE-ONLY Q × torus knot operator average")
print("= strip core, compute valence crossings, apply knot correction")
print("=" * 80)
print()

print(f"  {'Nuc':>5} {'Q_val':>8} {'knot':>6} {'tr_knot':>8} {'Q_pred':>8} "
      f"{'Q_exp':>8} {'err':>8}")
print("  " + "-" * 65)

for Z, N, name, Q_exp, Q_err in nuclei:
    Q_v, Zv, Nv, Zvd, Nvd = valence_Q(Z, N)
    si, _, _, size, knot, deg, occ = get_shell_info(N)

    if deg >= 2:
        # Apply knot × occupation correction
        tr_k = knot_traces[knot]
        Q_pred = Q_v * abs(tr_k)
    else:
        Q_pred = Q_v

    err = (Q_pred - Q_exp) / Q_exp * 100
    knot_str = f"T{knot[0]}{knot[1]}" if deg >= 2 else "—"
    tr_str = f"{abs(knot_traces.get(knot, 0)):.4f}" if deg >= 2 else "—"
    print(f"  {name:>5} {Q_v:>8.5f} {knot_str:>6} {tr_str:>8} {Q_pred:>8.5f} "
          f"{Q_exp:>8.5f} {err:>+7.1f}%")

print()

# ── APPROACH 6: GEOMETRIC MEAN OF KNOT TRACES ────────────────

print("=" * 80)
print("APPROACH 6: Q = Q_bare × geometric_mean(T_k · Δ) over active shells")
print("Active shells = shells that differ between parent and daughter")
print("=" * 80)
print()

for Z, N, name, Q_exp, Q_err in nuclei:
    Qb = bare_Q(Z, N)

    # Collect all shells involved in the transition
    active_traces = []
    active_labels = []

    # Neutron shell (converting neutron leaves)
    si_n, _, _, size_n, knot_n, deg_n, occ_n = get_shell_info(N)
    if deg_n >= 2:
        w_sym_n, w_std_n, w_alt_n = occupation_weights(occ_n, size_n)
        tr_eff_n = effective_trace(occ_n, size_n, knot_n)
        active_traces.append(abs(tr_eff_n))
        active_labels.append(f"N:sh{si_n+1}(k={occ_n}/{size_n})")

    # Proton shell (new proton enters)
    si_z, _, _, size_z, knot_z, deg_z, occ_z = get_shell_info(Z + 1)
    if deg_z >= 2:
        w_sym_z, w_std_z, w_alt_z = occupation_weights(occ_z, size_z)
        tr_eff_z = effective_trace(occ_z, size_z, knot_z)
        active_traces.append(abs(tr_eff_z))
        active_labels.append(f"Z:sh{si_z+1}(k={occ_z}/{size_z})")

    if active_traces:
        geo_mean = 1.0
        for t in active_traces:
            geo_mean *= t
        geo_mean = geo_mean ** (1.0 / len(active_traces))
        Q_pred = Qb * geo_mean
    else:
        Q_pred = Qb
        geo_mean = 1.0

    err = (Q_pred - Q_exp) / Q_exp * 100
    labels = " & ".join(active_labels) if active_labels else "degree 1 only"
    print(f"  {name:>5}: Q_bare={Qb:.5f}, geo={geo_mean:.6f}, "
          f"Q_pred={Q_pred:.5f}, Q_exp={Q_exp:.5f} ({err:+.1f}%)")
    print(f"         active: {labels}")

print()

# ── SUMMARY: NEEDED vs AVAILABLE CORRECTION FACTORS ──────────

print("=" * 80)
print("SUMMARY: What correction factor is needed?")
print("=" * 80)
print()

print(f"  {'Nuc':>5} {'Q_bare':>8} {'Q_exp':>8} {'F_need':>8} "
      f"{'N_shell':>8} {'N_occ':>8} {'Z_shell':>8}")
print("  " + "-" * 65)

for Z, N, name, Q_exp, Q_err in nuclei:
    Qb = bare_Q(Z, N)
    F_need = Q_exp / Qb
    si_n, _, _, size_n, knot_n, deg_n, occ_n = get_shell_info(N)
    si_z, _, _, size_z, knot_z, deg_z, occ_z = get_shell_info(Z)
    print(f"  {name:>5} {Qb:>8.5f} {Q_exp:>8.5f} {F_need:>8.4f} "
          f"{'sh'+str(si_n+1)+'/'+str(occ_n)+'/'+str(size_n):>8} "
          f"{'d'+str(deg_n):>8} "
          f"{'sh'+str(si_z+1)+'/'+str(occ_z)+'/'+str(size_z):>8}")
