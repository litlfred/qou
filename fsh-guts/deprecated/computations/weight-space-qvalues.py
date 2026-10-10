#!/usr/bin/env python3
"""
Weight space decomposition of Δ_mix and torus knot operators.

Project operators in H₃(q) onto irreducible representations
using Young symmetrizer idempotents.

H₃(q) has 3 irreps indexed by partitions of 3:
  (3)     — trivial (symmetric), dim 1
  (2,1)   — standard, dim [2]_q
  (1,1,1) — sign (alternating), dim 1

Young symmetrizer idempotents (q-deformed):
  e_{(3)}     = (1/[3]_q!) Σ_{w∈S₃} q^{ℓ(w)} T_w
  e_{(1,1,1)} = (1/[3]_q!) Σ_{w∈S₃} (-q⁻¹)^{ℓ(w)} T_w
  e_{(2,1)}   = 1 - e_{(3)} - e_{(1,1,1)}

The Q-value is:
  Q = E_× · μ₀ · |Σ_λ d_λ(q) · ⟨λ| full_operator |λ⟩|

where ⟨λ| O |λ⟩ is the irrep-projected trace.

Usage:
    python3 weight-space-qvalues.py
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

# ── S₃ ELEMENTS IN H₃(q) ─────────────────────────────────────

# S₃ has 6 elements: e, s₁, s₂, s₁s₂, s₂s₁, s₁s₂s₁
# In braid/Hecke notation:
#   e    → 1         (length 0)
#   s₁   → σ₀        (length 1)
#   s₂   → σ₁        (length 1)
#   s₁s₂ → σ₀σ₁      (length 2)
#   s₂s₁ → σ₁σ₀      (length 2)
#   s₁s₂s₁ → σ₀σ₁σ₀ = σ₁σ₀σ₁  (length 3)

S3_ELEMENTS = {
    'e':     ((), 0),
    's1':    ((0,), 1),
    's2':    ((1,), 1),
    's1s2':  ((0,1), 2),
    's2s1':  ((1,0), 2),
    'w0':    ((0,1,0), 3),  # = (1,0,1) by YB, longest element
}

# ── YOUNG SYMMETRIZER IDEMPOTENTS ──────────────────────────────

# [n]_q = (q^n - q^{-n}) / (q - q^{-1})
q1 = q_int(1)  # = 1
q2 = q_int(2)  # = q + q⁻¹
q3 = q_int(3)  # = q² + 1 + q⁻²

# [3]_q! = [1]_q · [2]_q · [3]_q
q3_fact = q1 * q2 * q3

print(f"q = {q:.10f}")
print(f"[1]_q = {q1:.10f}")
print(f"[2]_q = {q2:.10f}")
print(f"[3]_q = {q3:.10f}")
print(f"[3]_q! = {q3_fact:.10f}")
print()

def build_young_sym():
    """Build the three Young symmetrizer idempotents of H₃(q)."""

    # e_{(3)} = (1/[3]_q!) Σ q^{ℓ(w)} T_w
    e_sym = HeckeElement.zero()
    for name, (word, length) in S3_ELEMENTS.items():
        coeff = q**length / q3_fact
        e_sym = e_sym + HeckeElement({word: coeff})
    e_sym, _ = div.reduce(e_sym)

    # e_{(1,1,1)} = (1/[3]_q!) Σ (-q⁻¹)^{ℓ(w)} T_w
    e_alt = HeckeElement.zero()
    for name, (word, length) in S3_ELEMENTS.items():
        coeff = (-qi)**length / q3_fact
        e_alt = e_alt + HeckeElement({word: coeff})
    e_alt, _ = div.reduce(e_alt)

    # e_{(2,1)} = 1 - e_{(3)} - e_{(1,1,1)}
    e_std = HeckeElement.identity()
    e_std = e_std + e_sym.scale(-1.0)
    e_std = e_std + e_alt.scale(-1.0)
    e_std, _ = div.reduce(e_std)

    return e_sym, e_alt, e_std

e_sym, e_alt, e_std = build_young_sym()

print("Young symmetrizer idempotents:")
for name, e in [("e_{(3)}", e_sym), ("e_{(1,1,1)}", e_alt), ("e_{(2,1)}", e_std)]:
    tr = div.markov_trace(e, 3)
    print(f"  {name}: {e.n_terms()} terms, tr = {tr:.10f}")
    for w, c in sorted(e.terms.items(), key=lambda x: (len(x[0]), x[0])):
        ws = '.'.join(f'σ{i}' for i in w) if w else '1'
        print(f"    {c:+.8f} · {ws}")

# Verify: e_i² = e_i (idempotent)
print("\nIdempotent verification (e² = e):")
for name, e in [("e_{(3)}", e_sym), ("e_{(1,1,1)}", e_alt), ("e_{(2,1)}", e_std)]:
    e2 = e * e
    e2, _ = div.reduce(e2)
    # Check if e2 ≈ e
    diff = HeckeElement.zero()
    for w, c in e.terms.items():
        diff.terms[w] = diff.terms.get(w, 0.0) - c
    for w, c in e2.terms.items():
        diff.terms[w] = diff.terms.get(w, 0.0) + c
    diff._clean()
    max_err = max(abs(c) for c in diff.terms.values()) if diff.terms else 0
    print(f"  {name}: max|e²-e| = {max_err:.2e} {'✓' if max_err < 1e-8 else '✗'}")

# Verify: e_i · e_j = 0 for i ≠ j (orthogonal)
print("\nOrthogonality verification (e_i · e_j = 0):")
for (n1, e1), (n2, e2) in [
    (("(3)", e_sym), ("(1,1,1)", e_alt)),
    (("(3)", e_sym), ("(2,1)", e_std)),
    (("(1,1,1)", e_alt), ("(2,1)", e_std)),
]:
    prod = e1 * e2
    prod, _ = div.reduce(prod)
    max_val = max(abs(c) for c in prod.terms.values()) if prod.terms else 0
    print(f"  e_{n1}·e_{n2}: max|coeff| = {max_val:.2e} {'✓' if max_val < 1e-8 else '✗'}")

# ── Δ_mix AND ITS IRREP DECOMPOSITION ─────────────────────────

print()
print("=" * 70)
print("Δ_mix = σ₀ · σ₁⁻¹ decomposed by irrep")
print()

DELTA_MIX = sigma(0) * sigma_inv(1)
DELTA_MIX, _ = div.reduce(DELTA_MIX)
tr_delta = div.markov_trace(DELTA_MIX, 3)
print(f"Δ_mix: {DELTA_MIX.n_terms()} terms, tr = {tr_delta:.10f}")

# Project Δ_mix onto each irrep: e_λ · Δ_mix · e_λ
for name, e_lam, dim_q in [
    ("(3)", e_sym, 1.0),
    ("(2,1)", e_std, q2),
    ("(1,1,1)", e_alt, 1.0),
]:
    proj = e_lam * DELTA_MIX * e_lam
    proj, _ = div.reduce(proj)
    tr_proj = div.markov_trace(proj, 3)
    # The "weight" of Δ_mix in this irrep
    print(f"  e_{name} · Δ_mix · e_{name}: tr = {tr_proj:.10f}, "
          f"dim_q = {dim_q:.4f}, weighted = {dim_q * tr_proj:.10f}")

# Also: left projection only (the character)
print()
print("Left projection (character): tr(e_λ · Δ_mix)")
for name, e_lam, dim_q in [
    ("(3)", e_sym, 1.0),
    ("(2,1)", e_std, q2),
    ("(1,1,1)", e_alt, 1.0),
]:
    proj = e_lam * DELTA_MIX
    proj, _ = div.reduce(proj)
    tr_proj = div.markov_trace(proj, 3)
    print(f"  tr(e_{name} · Δ_mix) = {tr_proj:.10f}")

# ── TORUS KNOT OPERATORS DECOMPOSED BY IRREP ──────────────────

print()
print("=" * 70)
print("TORUS KNOT OPERATORS decomposed by irrep")
print()

def build_torus_knot(r, s):
    e = HeckeElement.identity()
    for _ in range(s):
        for i in range(r - 1):
            e = e * sigma(i)
        e, _ = div.reduce(e)
    return e

EMBEDDABLE = [
    (2, 3, 1), (2, 5, 1), (2, 7, 1), (3, 5, 1),
    (2, 9, 2), (3, 4, 2),
]

for r, s, deg in EMBEDDABLE:
    T = build_torus_knot(r, s)
    tr_T = div.markov_trace(T, 3)
    print(f"T_{{{r},{s}}} (degree {deg}): tr = {tr_T:.10f}")

    for name, e_lam, dim_q in [
        ("(3)", e_sym, 1.0),
        ("(2,1)", e_std, q2),
        ("(1,1,1)", e_alt, 1.0),
    ]:
        proj = e_lam * T * e_lam
        proj, _ = div.reduce(proj)
        tr_proj = div.markov_trace(proj, 3)
        print(f"  e_{name} · T · e_{name}: tr = {tr_proj:.10f}")
    print()

# ── T · Δ_mix DECOMPOSED BY IRREP ─────────────────────────────

print("=" * 70)
print("T · Δ_mix decomposed by irrep")
print("(This is what enters the Q-value formula)")
print()

for r, s, deg in EMBEDDABLE:
    T = build_torus_knot(r, s)
    T_delta = T * DELTA_MIX
    T_delta, _ = div.reduce(T_delta)
    tr_Td = div.markov_trace(T_delta, 3)
    print(f"T_{{{r},{s}}} · Δ_mix: tr = {tr_Td:.10f}")

    total_weighted = 0.0
    for name, e_lam, dim_q in [
        ("(3)", e_sym, 1.0),
        ("(2,1)", e_std, q2),
        ("(1,1,1)", e_alt, 1.0),
    ]:
        proj = e_lam * T_delta * e_lam
        proj, _ = div.reduce(proj)
        tr_proj = div.markov_trace(proj, 3)
        weighted = dim_q * tr_proj
        total_weighted += weighted
        pct = tr_proj / tr_Td * 100 if abs(tr_Td) > 1e-15 else 0
        print(f"  λ={name}: tr_proj = {tr_proj:.10f} ({pct:+.1f}%), "
              f"d_λ·tr = {weighted:.10f}")
    print(f"  Sum of weighted projections: {total_weighted:.10f}")
    print(f"  Direct trace:                {tr_Td:.10f}")
    print()

# ── TRY: Q = Σ_λ d_λ · ⟨λ|decay_op|λ⟩ ────────────────────────

print("=" * 70)
print("Q-VALUE ATTEMPT: irrep-weighted sum")
print()
print("Hypothesis: Q = E_× · μ₀ · |Σ_λ d_λ · tr(e_λ · T_shell · Δ_mix · e_λ)|")
print("where T_shell = product of applicable torus knots")
print()

# For each nucleus, the "decay operator" is:
# D = T_shell · Δ_mix  (where T_shell encodes the shell's knot structure)

# First: just Δ_mix alone (the bare case)
print("Bare case (T_shell = I):")
Q_factor_bare = 0.0
for name, e_lam, dim_q in [
    ("(3)", e_sym, 1.0),
    ("(2,1)", e_std, q2),
    ("(1,1,1)", e_alt, 1.0),
]:
    proj = e_lam * DELTA_MIX * e_lam
    proj, _ = div.reduce(proj)
    tr_proj = div.markov_trace(proj, 3)
    Q_factor_bare += dim_q * tr_proj
    print(f"  λ={name}: d_λ·⟨λ|Δ|λ⟩ = {dim_q * tr_proj:.10f}")
print(f"  Total: {Q_factor_bare:.10f}")
print(f"  |Total| × E_× × μ₀ = {abs(Q_factor_bare) * E_CROSS * mu_0:.5f}")
print()

# With T_{2,3} (trefoil = SU₂ structure)
print("With T_{2,3}:")
T23 = build_torus_knot(2, 3)
T23_delta = T23 * DELTA_MIX
T23_delta, _ = div.reduce(T23_delta)
Q_factor = 0.0
for name, e_lam, dim_q in [
    ("(3)", e_sym, 1.0),
    ("(2,1)", e_std, q2),
    ("(1,1,1)", e_alt, 1.0),
]:
    proj = e_lam * T23_delta * e_lam
    proj, _ = div.reduce(proj)
    tr_proj = div.markov_trace(proj, 3)
    Q_factor += dim_q * tr_proj
print(f"  Total: {Q_factor:.10f}")
print(f"  Ratio to bare: {Q_factor / Q_factor_bare:.6f}")
print()

# With T_{3,5} (weak vertex)
print("With T_{3,5}:")
T35 = build_torus_knot(3, 5)
T35_delta = T35 * DELTA_MIX
T35_delta, _ = div.reduce(T35_delta)
Q_factor_35 = 0.0
for name, e_lam, dim_q in [
    ("(3)", e_sym, 1.0),
    ("(2,1)", e_std, q2),
    ("(1,1,1)", e_alt, 1.0),
]:
    proj = e_lam * T35_delta * e_lam
    proj, _ = div.reduce(proj)
    tr_proj = div.markov_trace(proj, 3)
    Q_factor_35 += dim_q * tr_proj
print(f"  Total: {Q_factor_35:.10f}")
print(f"  Ratio to bare: {Q_factor_35 / Q_factor_bare:.6f}")
print()

# ── TRANSFER MATRIX Q_bare FOR COMPARISON ─────────────────────

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

print("=" * 70)
print("Q-VALUES: transfer matrix Q_bare × Markov trace corrections")
print()
print("Previous best: Q = Q_bare × |tr(T_{deg2} · Δ_mix)|")
print()

for Z, N, name, Q_exp, Q_err in nuclei:
    Qb = bare_Q(Z, N)
    print(f"  {name:>5}: Q_bare = {Qb:.5f}, Q_exp = {Q_exp:.5f}, "
          f"bare_err = {(Qb - Q_exp)/Q_exp*100:+.1f}%")

print()
print("Key insight: Q_bare = Σ_crossings log(volume)")
print("This is a LOG-SUM, not a product of traces.")
print("The transfer matrix already captures degree-0 and degree-1 structure.")
print("The torus knot corrections at degree ≥ 2 are multiplicative modulations.")
