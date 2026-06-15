#!/usr/bin/env python3
"""
Correct Young symmetrizer idempotents for H₃(q).

The q-Young symmetrizer for the symmetric representation uses:
  e_{(n)} = Σ_{w∈S_n} q^{ℓ(w)} T_w / P_n(q²)

where P_n(t) = Σ_{w∈S_n} t^{ℓ(w)} is the Poincaré polynomial of S_n.

For S₃: P₃(t) = 1 + 2t + 2t² + t³ = (1+t)(1+t+t²)

The key identity: T_w · e_{(n)} = q^{ℓ(w)} e_{(n)} for all w ∈ S_n.

For the alternating representation:
  e_{(1^n)} = Σ_{w∈S_n} (-q⁻¹)^{ℓ(w)} T_w / P_n(q⁻²)

Usage:
    python3 weight-space-correct.py
"""

import math
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

# ── S₃ ELEMENTS ───────────────────────────────────────────────

# (word, length) pairs for all 6 elements of S₃
S3 = [
    ((), 0),        # e
    ((0,), 1),      # s₁
    ((1,), 1),      # s₂
    ((0,1), 2),     # s₁s₂
    ((1,0), 2),     # s₂s₁
    ((0,1,0), 3),   # w₀ (longest)
]

# ── POINCARÉ POLYNOMIALS ──────────────────────────────────────

# P₃(t) = Σ t^{ℓ(w)} = 1 + 2t + 2t² + t³
def poincare_S3(t):
    return 1 + 2*t + 2*t**2 + t**3

P3_q2 = poincare_S3(q**2)    # for symmetric idempotent
P3_qi2 = poincare_S3(qi**2)  # for alternating idempotent

print(f"q = {q:.10f}")
print(f"P₃(q²) = {P3_q2:.10f}")
print(f"P₃(q⁻²) = {P3_qi2:.10f}")
print()

# ── SYMMETRIC IDEMPOTENT ──────────────────────────────────────

# e_{(3)} = Σ q^{ℓ(w)} T_w / P₃(q²)
e_sym = HeckeElement.zero()
for word, length in S3:
    coeff = q**length / P3_q2
    e_sym = e_sym + HeckeElement({word: coeff})
e_sym, _ = div.reduce(e_sym)

# ── ALTERNATING IDEMPOTENT ────────────────────────────────────

# e_{(1,1,1)} = Σ (-q⁻¹)^{ℓ(w)} T_w / P₃(q⁻²)
e_alt = HeckeElement.zero()
for word, length in S3:
    coeff = (-qi)**length / P3_qi2
    e_alt = e_alt + HeckeElement({word: coeff})
e_alt, _ = div.reduce(e_alt)

# ── STANDARD IDEMPOTENT ──────────────────────────────────────

e_std = HeckeElement.identity()
e_std = e_std + e_sym.scale(-1.0)
e_std = e_std + e_alt.scale(-1.0)
e_std, _ = div.reduce(e_std)

# ── VERIFICATION ──────────────────────────────────────────────

print("Young symmetrizer idempotents (corrected normalization):")
for name, e in [("e_{(3)}", e_sym), ("e_{(1,1,1)}", e_alt), ("e_{(2,1)}", e_std)]:
    tr = div.markov_trace(e, 3)
    print(f"  {name}: {e.n_terms()} terms, tr = {tr:.10f}")
    for w, c in sorted(e.terms.items(), key=lambda x: (len(x[0]), x[0])):
        ws = '.'.join(f'σ{i}' for i in w) if w else '1'
        print(f"    {c:+.10f} · {ws}")

print()
print("Idempotent verification (e² = e):")
for name, e in [("e_{(3)}", e_sym), ("e_{(1,1,1)}", e_alt), ("e_{(2,1)}", e_std)]:
    e2 = e * e
    e2, _ = div.reduce(e2)
    diff = HeckeElement.zero()
    for w, c in e.terms.items():
        diff.terms[w] = diff.terms.get(w, 0.0) - c
    for w, c in e2.terms.items():
        diff.terms[w] = diff.terms.get(w, 0.0) + c
    diff._clean()
    max_err = max(abs(c) for c in diff.terms.values()) if diff.terms else 0
    print(f"  {name}: max|e²-e| = {max_err:.2e} {'✓' if max_err < 1e-8 else '✗'}")

print()
print("Orthogonality verification (e_i · e_j = 0):")
for (n1, e1), (n2, e2) in [
    (("(3)", e_sym), ("(1,1,1)", e_alt)),
    (("(3)", e_sym), ("(2,1)", e_std)),
    (("(1,1,1)", e_alt), ("(2,1)", e_std)),
]:
    prod = e1 * e2
    prod, _ = div.reduce(prod)
    max_val = max(abs(c) for c in prod.terms.values()) if prod.terms else 0
    print(f"  e_{n1}·e_{n2}: max|coeff| = {max_val:.2e} {'✓' if max_val < 1e-8 else '✗'}")

print()
print("Completeness: e_{(3)} + e_{(1,1,1)} + e_{(2,1)} = 1:")
total = e_sym + e_alt + e_std
total, _ = div.reduce(total)
for w, c in sorted(total.terms.items(), key=lambda x: (len(x[0]), x[0])):
    ws = '.'.join(f'σ{i}' for i in w) if w else '1'
    if abs(c) > 1e-12:
        print(f"  {c:+.10f} · {ws}")

# ── Δ_mix DECOMPOSITION ──────────────────────────────────────

print()
print("=" * 70)
print("Δ_mix = σ₀ · σ₁⁻¹ DECOMPOSITION (corrected)")
print()

DELTA_MIX = sigma(0) * sigma_inv(1)
DELTA_MIX, _ = div.reduce(DELTA_MIX)
tr_delta = div.markov_trace(DELTA_MIX, 3)
print(f"Δ_mix: tr = {tr_delta:.10f}")
print()

# Project onto each irrep
print("Irrep projections of Δ_mix:")
total_check = 0.0
TWO_Q = q + qi

for name, e_lam, dim_q in [
    ("(3) sym", e_sym, 1.0),
    ("(2,1) std", e_std, TWO_Q),
    ("(1,1,1) alt", e_alt, 1.0),
]:
    # Double-sided projection: e_λ · Δ_mix · e_λ
    proj = e_lam * DELTA_MIX * e_lam
    proj, _ = div.reduce(proj)
    tr_proj = div.markov_trace(proj, 3)

    # Single-sided: tr(Δ_mix · e_λ)
    single = DELTA_MIX * e_lam
    single, _ = div.reduce(single)
    tr_single = div.markov_trace(single, 3)

    total_check += tr_proj
    print(f"  λ={name}: tr(e·Δ·e) = {tr_proj:.10f}, tr(Δ·e) = {tr_single:.10f}, "
          f"d_λ = {dim_q:.4f}")

print(f"  Σ tr(e·Δ·e) = {total_check:.10f} (should = tr(Δ) = {tr_delta:.10f})")

# ── TORUS KNOT · Δ_mix PROJECTIONS ────────────────────────────

print()
print("=" * 70)
print("TORUS KNOT · Δ_mix: IRREP PROJECTIONS")
print()

def build_torus_knot(r, s):
    e = HeckeElement.identity()
    for _ in range(s):
        for i in range(r - 1):
            e = e * sigma(i)
        e, _ = div.reduce(e)
    return e

EMBEDDABLE = [
    (2, 3, 1, "trefoil"),
    (2, 5, 1, "2nd gen"),
    (2, 7, 1, "3rd gen"),
    (3, 5, 1, "weak"),
    (2, 9, 2, "strong"),
    (3, 4, 2, "Hopf²"),
]

for r, s, deg, label in EMBEDDABLE:
    T = build_torus_knot(r, s)
    T_delta = T * DELTA_MIX
    T_delta, _ = div.reduce(T_delta)
    tr_Td = div.markov_trace(T_delta, 3)

    print(f"T_{{{r},{s}}}·Δ ({label}, deg {deg}): tr = {tr_Td:.10f}")

    for name, e_lam, dim_q in [
        ("sym", e_sym, 1.0),
        ("std", e_std, TWO_Q),
        ("alt", e_alt, 1.0),
    ]:
        proj = e_lam * T_delta * e_lam
        proj, _ = div.reduce(proj)
        tr_proj = div.markov_trace(proj, 3)
        pct = tr_proj / tr_Td * 100 if abs(tr_Td) > 1e-15 else 0
        print(f"    {name}: {tr_proj:+.10f} ({pct:+.1f}%)")
    print()

# ── ATTEMPT: IRREP-RESOLVED Q-VALUE ──────────────────────────

print("=" * 70)
print("IRREP-RESOLVED Q-VALUE")
print()
print("For each irrep λ, compute the contribution to the decay:")
print("  Q_λ = |tr(e_λ · T_shell · Δ_mix · e_λ)| × E_× × μ₀ × nuclear_factor")
print()

# The nuclear factor from the transfer matrix
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

def bare_Q(Z, N):
    def log_skein(p, n):
        types = ['p']*p + ['n']*n; A = p+n; logP = 0.0
        for i in range(A-1):
            M = [[1,0],[0,1]]
            for j in range(i+1, A):
                c, d = crossing_coeffs(types[i], types[j])
                M = mat_mul(M, T_mat(c, d))
            V = vol(M)
            if abs(V) > 0: logP += math.log(abs(V))
        return logP
    return abs(log_skein(Z+1, N-1) - log_skein(Z, N)) * E_CROSS * mu_0

nuclei = [
    (1,   2,   "³H",    Q_TRITIUM_MEV, Q_TRITIUM_MEV_ERR),
    (6,   8,   "¹⁴C",   Q_C14_MEV, Q_C14_MEV_ERR),
    (27,  33,  "⁶⁰Co",  Q_CO60_MEV, Q_CO60_MEV_ERR),
    (38,  52,  "⁹⁰Sr",  Q_SR90_MEV, Q_SR90_MEV_ERR),
    (55,  82,  "¹³⁷Cs", Q_CS137_MEV, Q_CS137_MEV_ERR),
    (83,  127, "²¹⁰Bi", Q_BI210_MEV, Q_BI210_MEV_ERR),
]

magic = [0, 2, 8, 20, 28, 50, 82, 126]
def outer_occ(X):
    m_leq = 0
    for mi in magic:
        if mi <= X: m_leq = mi
    occ = X - m_leq
    if occ == 0 and X > 0:
        prev = 0
        for mi in magic:
            if mi < X: prev = mi
        return X - prev
    return occ

# ── FINAL Q-VALUES WITH ALL APPROACHES ────────────────────────

print("=" * 70)
print("COMPARISON OF ALL APPROACHES")
print("=" * 70)
print()

# Approach A: Q_bare only (transfer matrix)
# Approach B: Q_bare × |tr(T_{3,4}·Δ)| for shells ≥ 8
# Approach C: Q_bare × |tr(T_{2,9}·Δ)| for shells ≥ 9
# Approach D: Q_bare × Σ_λ tr(e_λ · (T_{2,9}+T_{3,4}) · Δ · e_λ) (irrep-resolved)

# Precompute traces for degree-2 knots
T29 = build_torus_knot(2, 9)
T34 = build_torus_knot(3, 4)
T29_delta = T29 * DELTA_MIX
T29_delta, _ = div.reduce(T29_delta)
T34_delta = T34 * DELTA_MIX
T34_delta, _ = div.reduce(T34_delta)

tr_T29_delta = div.markov_trace(T29_delta, 3)
tr_T34_delta = div.markov_trace(T34_delta, 3)

# Irrep-resolved traces for degree-2 combined operator
T_deg2_combined = T29_delta + T34_delta
T_deg2_combined, _ = div.reduce(T_deg2_combined)
tr_deg2_combined = div.markov_trace(T_deg2_combined, 3)

# Project combined onto each irrep
print("Degree-2 combined operator (T_{2,9}+T_{3,4})·Δ_mix:")
print(f"  Total tr = {tr_deg2_combined:.10f}")
irrep_traces = {}
for name, e_lam, dim_q in [
    ("sym", e_sym, 1.0),
    ("std", e_std, TWO_Q),
    ("alt", e_alt, 1.0),
]:
    proj = e_lam * T_deg2_combined * e_lam
    proj, _ = div.reduce(proj)
    tr_proj = div.markov_trace(proj, 3)
    irrep_traces[name] = tr_proj
    print(f"    {name}: {tr_proj:+.10f}")

# The weighted irrep sum
irrep_sum = (irrep_traces['sym'] * 1.0
             + irrep_traces['std'] * TWO_Q
             + irrep_traces['alt'] * 1.0)
print(f"  Σ d_λ · tr_λ = {irrep_sum:.10f}")
print()

# ── TABLE ─────────────────────────────────────────────────────

print(f"  {'Nuc':>5} {'Q_bare':>8} {'×tr29':>8} {'×tr34':>8} "
      f"{'Q_exp':>8} {'err_bare':>8} {'err_29':>8} {'err_34':>8}")
print("  " + "-" * 72)

for Z, N, name, Q_exp, Q_err in nuclei:
    Qb = bare_Q(Z, N)
    np_d = outer_occ(Z + 1)

    Q_29 = Qb * abs(tr_T29_delta)
    Q_34 = Qb * abs(tr_T34_delta)

    err_bare = (Qb - Q_exp) / Q_exp * 100
    err_29 = (Q_29 - Q_exp) / Q_exp * 100
    err_34 = (Q_34 - Q_exp) / Q_exp * 100

    print(f"  {name:>5} {Qb:>8.5f} {Q_29:>8.5f} {Q_34:>8.5f} "
          f"{Q_exp:>8.5f} {err_bare:>+7.1f}% {err_29:>+7.1f}% {err_34:>+7.1f}%")

print()

# ── WHAT IF Q = Q_bare × |tr(Δ_mix)| / |tr_irrep(Δ_mix)| ? ──
# The idea: Q_bare over-counts because it includes ALL channels.
# The decay only goes through ONE channel. Divide by the total
# and multiply by the relevant channel.

print("=" * 70)
print("CHANNEL-SELECTIVE: Q = Q_bare × |tr_λ(Δ)| / |tr(Δ)|")
print()
print(f"  tr(Δ_mix) = {tr_delta:.10f}")

for name, e_lam, dim_q in [
    ("sym", e_sym, 1.0),
    ("std", e_std, TWO_Q),
    ("alt", e_alt, 1.0),
]:
    proj = e_lam * DELTA_MIX * e_lam
    proj, _ = div.reduce(proj)
    tr_proj = div.markov_trace(proj, 3)
    ratio = abs(tr_proj) / abs(tr_delta) if abs(tr_delta) > 0 else 0
    print(f"  λ={name}: |tr_λ|/|tr| = {ratio:.6f}")
    print(f"    Q = Q_bare × {ratio:.6f}:")
    for Z, N, nm, Q_exp, Q_err in nuclei:
        Qb = bare_Q(Z, N)
        Q_pred = Qb * ratio
        err = (Q_pred - Q_exp) / Q_exp * 100
        print(f"      {nm:>5}: {Q_pred:.5f} vs {Q_exp:.5f} ({err:+.1f}%)")
    print()
