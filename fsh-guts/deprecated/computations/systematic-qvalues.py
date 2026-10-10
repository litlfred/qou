#!/usr/bin/env python3
"""
Systematic beta decay Q-values from scratch.

Start from hydrogen. Build each nucleus by tracking every
operator applied. Use prime factorization for mixing operators.
T_{3,5} is ONLY the weak vertex. All mixing uses T_{2,n}.

For large n: factorize into primes, apply T_{2,p_i^k_i} sequentially.
Each T_{2,p^k} is computed via Chebyshev recurrence (no blowup).

The Q-value is:
  Q = Q_bare × |tr(mix_dau · T_{3,5} · mix_par⁻¹)|

where mix = ∏ T_{2,p_i^k_i} from prime factorization of the
outer shell occupancy.

Usage:
    python3 systematic-qvalues.py
"""

import math
from q_parameter import Q as q, Q_INV as qi, E_CROSS, HBAR_Q
from hecke_division import HeckeDivision, HeckeElement
from experimental_constants import *

div = HeckeDivision(q_val=q)
HA = q - qi; Z_m = 1/(q**0.5 + qi**0.5)
LN_Q = math.log(q); mu_0 = M_E_MEV / (3 * E_CROSS)

def log_q(x):
    return math.log(abs(x)) / LN_Q if x > 0 else float('-inf')

def sigma(i):
    return HeckeElement({(i,): 1.0})
def sigma_inv(i):
    return HeckeElement({(i,): 1.0, (): -HA})

# ── OPERATOR BUILDERS ──────────────────────────────────────────

def build_t2n(n):
    """T_{2,n} = σ₀ⁿ in H₂ ⊂ H₃. Chebyshev recurrence, O(n)."""
    e = HeckeElement.identity()
    for _ in range(n):
        e = e * sigma(0)
        e, _ = div.reduce(e)  # reduce at each step to prevent blowup
    return e

def build_t2n_inv(n):
    """T_{2,n}⁻¹ = (σ₀⁻¹)ⁿ."""
    e = HeckeElement.identity()
    for _ in range(n):
        e = e * sigma_inv(0)
        e, _ = div.reduce(e)
    return e

# T_{3,5} = (σ₀σ₁)⁵ — the weak vertex (ONLY used for the conversion)
T35 = HeckeElement.identity()
for _ in range(5):
    T35 = T35 * sigma(0) * sigma(1)
T35, _ = div.reduce(T35)

# ── PRIME FACTORIZATION ────────────────────────────────────────

def prime_powers(n):
    """Return list of prime powers in the factorization of n.
    E.g., 12 = 2²×3 → [4, 3]. 60 = 2²×3×5 → [4, 3, 5]."""
    if n <= 1:
        return []
    powers = []
    for p in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]:
        pk = 1
        while n % p == 0:
            n //= p
            pk *= p
        if pk > 1:
            powers.append(pk)
    if n > 1:
        powers.append(n)  # remaining prime
    return powers

# ── MIXING OPERATOR FROM PRIME FACTORIZATION ───────────────────

def mixing_op(n):
    """Build mixing operator for n nucleons.

    Factorize n into prime powers p_i^k_i.
    Apply T_{2,p_i^k_i} for each factor.
    These commute (different prime levels) so order doesn't matter.

    For n=1: identity (single nucleon, no mixing).
    """
    if n <= 1:
        return HeckeElement.identity()

    pps = prime_powers(n)
    elem = HeckeElement.identity()
    for pk in pps:
        t = build_t2n(pk)
        elem = elem * t
        elem, _ = div.reduce(elem)
    return elem

def mixing_op_inv(n):
    """Inverse of mixing operator."""
    if n <= 1:
        return HeckeElement.identity()

    pps = prime_powers(n)
    elem = HeckeElement.identity()
    # Apply inverses in REVERSE order
    for pk in reversed(pps):
        t = build_t2n_inv(pk)
        elem = elem * t
        elem, _ = div.reduce(elem)
    return elem

# ── BARE Q-VALUE ───────────────────────────────────────────────

def crossing_coeffs(ti, tj):
    if ti == 'p' and tj == 'p': return 1.0, 0.0
    elif ti == 'n' and tj == 'n': return 1.0, -HA
    else: return 1.0, -HA/2

def T_mat(c, d):
    return [[c*HA+d, c], [c, d]]
def mat_mul(A, B):
    return [[A[0][0]*B[0][0]+A[0][1]*B[1][0], A[0][0]*B[0][1]+A[0][1]*B[1][1]],
            [A[1][0]*B[0][0]+A[1][1]*B[1][0], A[1][0]*B[0][1]+A[1][1]*B[1][1]]]
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

# ── OUTER SHELL OCCUPANCY ─────────────────────────────────────

magic = [0, 2, 8, 20, 28, 50, 82, 126]

def outer_occ(X):
    """Number of nucleons in the outermost (possibly open) shell.
    If X is magic: returns the FULL shell size (not 0)."""
    m_leq = 0
    for mi in magic:
        if mi <= X: m_leq = mi
    occ = X - m_leq
    if occ == 0 and X > 0:
        # X is magic — use the shell size
        prev = 0
        for mi in magic:
            if mi < X: prev = mi
        return X - prev
    return occ

# ── OPERATOR CHAIN TRACE ──────────────────────────────────────

def decay_trace(np_par, nn_par, np_dau, nn_dau):
    """Compute tr(mix_dau · T_{3,5} · mix_par⁻¹).

    Operator chain:
      1. mix_par_p⁻¹: undo parent proton shell mixing
      2. mix_par_n⁻¹: undo parent neutron shell mixing
      3. T_{3,5}: weak vertex (the conversion)
      4. mix_dau_n: redo daughter neutron shell mixing
      5. mix_dau_p: redo daughter proton shell mixing
    """
    # Build operators
    mix_par_p_inv = mixing_op_inv(np_par)
    mix_par_n_inv = mixing_op_inv(nn_par)
    mix_dau_p = mixing_op(np_dau)
    mix_dau_n = mixing_op(nn_dau)

    # Chain: read right to left
    O = mix_par_p_inv
    O = mix_par_n_inv * O; O, _ = div.reduce(O)
    O = T35 * O; O, _ = div.reduce(O)
    O = mix_dau_n * O; O, _ = div.reduce(O)
    O = mix_dau_p * O; O, _ = div.reduce(O)

    return div.markov_trace(O, 3), O

# ── SYSTEMATIC COMPUTATION ────────────────────────────────────

nuclei = [
    (1,   2,   "³H",    Q_TRITIUM_MEV, Q_TRITIUM_MEV_ERR),
    (6,   8,   "¹⁴C",   Q_C14_MEV, Q_C14_MEV_ERR),
    (27,  33,  "⁶⁰Co",  Q_CO60_MEV, Q_CO60_MEV_ERR),
    (38,  52,  "⁹⁰Sr",  Q_SR90_MEV, Q_SR90_MEV_ERR),
    (55,  82,  "¹³⁷Cs", Q_CS137_MEV, Q_CS137_MEV_ERR),
    (83,  127, "²¹⁰Bi", Q_BI210_MEV, Q_BI210_MEV_ERR),
]

print("SYSTEMATIC Q-VALUES FROM PRIME-FACTORED OPERATORS")
print(f"q = {q:.10f}")
print()
print("Formula: Q = Q_bare × |tr(mix_dau · T_{{3,5}} · mix_par⁻¹)|")
print("  mix(n) = ∏ T_{{2, p_i^k_i}} from n = ∏ p_i^k_i")
print("  T_{{3,5}} = weak vertex only")
print()

for Z, N, name, Q_exp, Q_err in nuclei:
    np_p = outer_occ(Z)
    nn_p = outer_occ(N)
    np_d = outer_occ(Z + 1)
    nn_d = outer_occ(N - 1)

    print(f"{'='*70}")
    print(f"{name}: Z={Z}→{Z+1}, N={N}→{N-1}")
    print(f"  Outer shells: proton {np_p}→{np_d}, neutron {nn_p}→{nn_d}")
    print(f"  Prime factorizations:")
    print(f"    par_p: {np_p} = {prime_powers(np_p)}")
    print(f"    par_n: {nn_p} = {prime_powers(nn_p)}")
    print(f"    dau_p: {np_d} = {prime_powers(np_d)}")
    print(f"    dau_n: {nn_d} = {prime_powers(nn_d)}")

    # Build mixing operators and show their traces
    for label, n_occ in [("par_p", np_p), ("par_n", nn_p), ("dau_p", np_d), ("dau_n", nn_d)]:
        op = mixing_op(n_occ)
        tr = div.markov_trace(op, 3)
        print(f"    mix({label}, n={n_occ}): tr = {tr:.6f}, log_q = {log_q(abs(tr)):+.4f}")

    # Decay trace
    tr_decay, O_elem = decay_trace(np_p, nn_p, np_d, nn_d)

    print(f"  Decay operator trace: {tr_decay:.10f}")
    print(f"    sign = {'+'if tr_decay>0 else '-'}, |tr| = {abs(tr_decay):.10f}")

    # Reduced form
    print(f"    O reduced ({O_elem.n_terms()} terms):")
    for w, c in sorted(O_elem.terms.items(), key=lambda x: (len(x[0]), x[0])):
        ws = '.'.join(f'g{i}' for i in w) if w else '1'
        print(f"      {c:+.6f} × {ws}")

    # Q-value
    Qb = bare_Q(Z, N)
    Qp = Qb * abs(tr_decay)
    err = (Qp - Q_exp) / Q_exp * 100

    print(f"  Q_bare = {Qb:.5f} MeV")
    print(f"  Q_pred = Q_bare × |tr| = {Qb:.5f} × {abs(tr_decay):.6f} = {Qp:.5f} MeV")
    print(f"  Q_exp  = {Q_exp:.5f} ± {Q_err:.0e} MeV")
    print(f"  Error  = {err:+.1f}%")
    print()

# ── SUMMARY TABLE ──────────────────────────────────────────────

print("=" * 70)
print("SUMMARY")
print("=" * 70)
print()
print(f"  {'Nuc':>5} {'p→d':>8} {'n→d':>8} {'|tr|':>8} {'Q_bare':>8} {'Q_pred':>8} {'Q_exp':>8} {'err':>7}")
print("  " + "-" * 62)

for Z, N, name, Q_exp, Q_err in nuclei:
    np_p = outer_occ(Z)
    nn_p = outer_occ(N)
    np_d = outer_occ(Z + 1)
    nn_d = outer_occ(N - 1)

    tr_decay, _ = decay_trace(np_p, nn_p, np_d, nn_d)
    Qb = bare_Q(Z, N)
    Qp = Qb * abs(tr_decay)
    err = (Qp - Q_exp) / Q_exp * 100

    print(f"  {name:>5} {np_p}→{np_d:>3} {nn_p}→{nn_d:>3} "
          f"{abs(tr_decay):>8.4f} {Qb:>8.5f} {Qp:>8.5f} {Q_exp:>8.5f} {err:>+6.1f}%")
