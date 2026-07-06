#!/usr/bin/env python3
"""
T_beta dual action on nuclear ground states.

The weak vertex operator T_beta = L_+ - h*sigma_0 acts on nuclei
via the Frobenius dual:

    T_beta^vee = T_beta . G^{-1}

where G is the Gram matrix G_{ij} = tr_M(b_i . b_j).

This script:
  1. Builds nuclear ground states in H_3(q) NF basis
  2. Computes T_beta and T_beta^vee
  3. Acts T_beta^vee on nuclear NF vectors
  4. Decomposes the result: daughter nucleus + emitted particles
  5. Extracts Q-values from the electron channel amplitude

Key identity: tr_M(T_beta^vee) = 0  (the dual action is traceless)

Usage:
    cd computations && python3 tbeta-dual-action.py
"""
import math
import json
import sys
import numpy as np
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q as q, Q_INV as qi, HA as h
# z/NF_BASIS/TR_M now owned by pyhecke.gram (M2b inversion). Keep local
# bootstrap for dev mode; the installed-pyhecke path is preferred.
import sys as _sys, pathlib as _pl
_sys.path.insert(0, str(_pl.Path(__file__).resolve().parents[2] / "tools" / "pyhecke" / "python"))
from pyhecke.gram import z as _PG_Z, NF_BASIS as _PG_NF_BASIS, TR_M as _PG_TR_M  # noqa: E402


z = _PG_Z  # moved to pyhecke.gram
m_e = 0.51099895  # electron mass in MeV

print(f"q  = {q:.10f}")
print(f"h  = q - q^-1 = {h:.10f}")
print(f"z  = {z:.10f}")


# ══════════════════════════════════════════════════════════════════
#  HECKE ALGEBRA ENGINE (H_3(q), 2 generators sigma_0, sigma_1)
# ══════════════════════════════════════════════════════════════════

NF_BASIS = _PG_NF_BASIS  # moved to pyhecke.gram
NF_NAMES = ["gamma", "sigma0", "sigma1", "L+", "L-", "e-"]
NF_DISPLAY = ["\u03b3", "\u03c3\u2080", "\u03c3\u2081", "L\u208a", "L\u208b", "e\u207b"]

# Markov traces of basis elements
TR_M = list(_PG_TR_M)  # moved to pyhecke.gram
def hecke_mul(t1, t2):
    """Multiply two elements in the free algebra."""
    result = {}
    for w1, c1 in t1.items():
        for w2, c2 in t2.items():
            w = w1 + w2
            result[w] = result.get(w, 0.0) + c1 * c2
    return {w: c for w, c in result.items() if abs(c) > 1e-15}


def reduce_nf(terms):
    """Reduce to Garside-Shirshov normal form."""
    changed = True
    while changed:
        changed = False
        new_terms = {}
        for word, coeff in terms.items():
            if abs(coeff) < 1e-15:
                continue
            done = False
            # Hecke relation: sigma_i^2 = h*sigma_i + 1
            for pos in range(len(word) - 1):
                if word[pos] == word[pos + 1]:
                    pre, suf = word[:pos], word[pos + 2:]
                    w1 = pre + (word[pos],) + suf
                    w2 = pre + suf
                    new_terms[w1] = new_terms.get(w1, 0.0) + coeff * h
                    new_terms[w2] = new_terms.get(w2, 0.0) + coeff
                    done = changed = True
                    break
            if done:
                continue
            # Braid relation: sigma_i sigma_j sigma_i = sigma_j sigma_i sigma_j
            for pos in range(len(word) - 2):
                a, b, c = word[pos], word[pos + 1], word[pos + 2]
                if a == c and abs(a - b) == 1:
                    new_trip = (b, a, b)
                    if new_trip < (a, b, a):
                        nw = word[:pos] + new_trip + word[pos + 3:]
                        new_terms[nw] = new_terms.get(nw, 0.0) + coeff
                        done = changed = True
                        break
            if not done:
                new_terms[word] = new_terms.get(word, 0.0) + coeff
        terms = {w: c for w, c in new_terms.items() if abs(c) > 1e-15}
    return terms


def to_vec(terms):
    """Convert NF terms dict to 6-vector."""
    return np.array([terms.get(b, 0.0) for b in NF_BASIS])


def from_vec(v):
    """Convert 6-vector back to NF terms dict."""
    return {NF_BASIS[i]: v[i] for i in range(6) if abs(v[i]) > 1e-15}


def markov_trace(v):
    """tr_M of an NF vector."""
    return sum(v[i] * TR_M[i] for i in range(6))


def nf_mul(v1, v2):
    """Multiply two NF vectors, return NF of product."""
    t1 = from_vec(v1)
    t2 = from_vec(v2)
    prod = hecke_mul(t1, t2)
    nf = reduce_nf(prod)
    return to_vec(nf)


# ══════════════════════════════════════════════════════════════════
#  GRAM MATRIX
# ══════════════════════════════════════════════════════════════════

print("\n" + "=" * 72)
print("  GRAM MATRIX  G_{ij} = tr_M(b_i . b_j)")
print("=" * 72)

G = np.zeros((6, 6))
for i in range(6):
    for j in range(6):
        ei = {NF_BASIS[i]: 1.0}
        ej = {NF_BASIS[j]: 1.0}
        prod = hecke_mul(ei, ej)
        nf = reduce_nf(prod)
        vec = to_vec(nf)
        G[i, j] = markov_trace(vec)

G_inv = np.linalg.inv(G)
eigvals = np.linalg.eigvals(G).real

print(f"  det(G) = {np.linalg.det(G):.10f}")
print(f"  eigenvalues = {sorted(eigvals)}")
print(f"  condition number = {max(eigvals)/min(eigvals):.4f}")

# Print G
hdr = f"  {'':8s}" + "".join(f" {n:>10s}" for n in NF_DISPLAY)
print(hdr)
for i in range(6):
    row = f"  {NF_DISPLAY[i]:8s}" + "".join(f" {G[i,j]:>10.6f}" for j in range(6))
    print(row)


# ══════════════════════════════════════════════════════════════════
#  T_BETA: WEAK VERTEX OPERATOR
# ══════════════════════════════════════════════════════════════════

print("\n" + "=" * 72)
print("  T_BETA: WEAK VERTEX OPERATOR")
print("=" * 72)

# T_beta = L_+ - h * sigma_0
# In NF basis: [gamma, sigma0, sigma1, L+, L-, e-]
#              [  0,    -h,      0,     1,   0,  0 ]
T_beta = np.array([0.0, -h, 0.0, 1.0, 0.0, 0.0])

print(f"  T_beta = L_+ - h*sigma_0")
print(f"  NF vector: {T_beta}")
print(f"  tr_M(T_beta) = {markov_trace(T_beta):.10f}")

# T_beta^vee = T_beta . G^{-1}  (Frobenius dual)
T_beta_dual = T_beta @ G_inv

print(f"\n  T_beta^vee = T_beta . G^{{-1}}")
print(f"  Dual vector: {T_beta_dual}")
print(f"  tr_M(T_beta^vee) = {markov_trace(T_beta_dual):.10f}")

# Verify: <T_beta^vee, b_i>_F = T_beta_i
print(f"\n  Verify <T_beta^vee, b_i>_F = T_beta_i:")
for i in range(6):
    pairing = T_beta_dual @ G[:, i]
    print(f"    i={i} ({NF_DISPLAY[i]}): pairing = {pairing:+.6f}, T_beta_i = {T_beta[i]:+.6f}")

# Frobenius norm of T_beta
frob_norm = math.sqrt(abs(T_beta @ G @ T_beta))
print(f"\n  ||T_beta||_F = sqrt(T_beta . G . T_beta) = {frob_norm:.10f}")


# ══════════════════════════════════════════════════════════════════
#  NUCLEAR GROUND STATES (from transfer matrix chain)
# ══════════════════════════════════════════════════════════════════

print("\n" + "=" * 72)
print("  NUCLEAR GROUND STATES IN NF BASIS")
print("=" * 72)


def chain_V(ordering, gen):
    """Vertex volume V_hat at generator position gen.

    The transfer matrix chain for generator gen is the product of
    typed crossing matrices T_{t_gen, t_j} for j > gen.
    Returns (a, b) where the result is a*z + b.
    """
    a, b = 0.0, 1.0
    A = len(ordering)
    for j in range(gen + 1, A):
        ti, tj = ordering[gen], ordering[j]
        if ti == 1 and tj == 1:  # pp
            d = 0.0
        elif ti == 0 and tj == 0:  # nn
            d = -h
        else:  # pn or np
            d = -h / 2
        new_a = a * h + a * d + b
        new_b = a + b * d
        a, b = new_a, new_b
    return z * a + b


def nuclear_nf_vector(ordering):
    """Project a nuclear state into H_3(q) NF basis.

    The nuclear braid in H_A(q) projects to H_3(q) via sigma_i -> sigma_{i mod 2}.
    The NF vector components come from the vertex volumes V_hat_i.

    For the transfer matrix chain, each generator contributes to the
    NF via its vertex volume. The full NF is the sum over all generators.
    """
    A = len(ordering)
    if A <= 1:
        return np.array([1.0, 0.0, 0.0, 0.0, 0.0, 0.0])

    # Each generator sigma_i maps to sigma_{i mod 2} in H_3.
    # The NF contribution is determined by the transfer matrix eigenstructure.
    # We build the NF vector from the vertex volumes.

    # Method: The nuclear Skein polynomial is prod_i V_hat_i.
    # But for the NF 6-vector, we need the projection into each basis element.
    # The Markov trace is tr_M = prod V_hat_i (up to normalization).

    # For the FULL 6-component decomposition, we need to track which
    # generator pairs contribute to which NF basis element.

    # Generator i (in H_A) maps to sigma_{i mod 2} in H_3.
    # The word sigma_0 sigma_1 sigma_0 sigma_1 ... reduces to NF.
    # Let's build the actual word and reduce.

    # The nuclear braid word: for ordering [t_0, ..., t_{A-1}],
    # the braid word is sigma_0 sigma_1 sigma_2 ... sigma_{A-2}
    # with typed crossings. After projection sigma_i -> sigma_{i mod 2}:
    word = tuple(i % 2 for i in range(A - 1))

    # But we need to account for the crossing TYPES.
    # pp crossings: T_pp = I (no crossing), so skip
    # nn crossings: T_nn = I (via T_pp.T_nn = I), so skip
    # pn crossings: T_pn contributes a sigma crossing

    # Build the word from typed crossings:
    typed_word = []
    for i in range(A - 1):
        ti, tj = ordering[i], ordering[i + 1]
        if ti != tj:  # only pn or np crossings contribute
            typed_word.append(i % 2)

    if not typed_word:
        return np.array([1.0, 0.0, 0.0, 0.0, 0.0, 0.0])

    # Reduce the projected word to NF
    terms = {tuple(typed_word): 1.0}
    nf = reduce_nf(terms)
    return to_vec(nf)


def nuclear_nf_full(ordering):
    """Full nuclear NF: build the actual product of crossing matrices.

    Each crossing (i, i+1) contributes:
      pp: identity (T_pp)
      nn: identity (T_nn)
      pn/np: sigma_{i mod 2} (the crossing generator)

    The nuclear braid is the concatenation of all crossing generators.
    After projection to H_3(q) and NF reduction, we get the 6-vector.
    """
    A = len(ordering)
    if A <= 1:
        return np.array([1.0, 0.0, 0.0, 0.0, 0.0, 0.0])

    # Build the product incrementally
    # Start with identity
    current = {(): 1.0}

    for i in range(A - 1):
        ti = ordering[i]
        tj = ordering[i + 1]

        if ti == tj:
            # Same type: identity crossing (T_pp or T_nn)
            continue
        else:
            # Mixed crossing: multiply by sigma_{i mod 2}
            gen = i % 2
            gen_term = {(gen,): 1.0}
            current = hecke_mul(current, gen_term)
            current = reduce_nf(current)

    return to_vec(current)


def find_ground_state(Z, N):
    """Find ground state ordering by exhaustive search (small A only)."""
    from itertools import combinations
    A = Z + N
    best_Phi = float('inf')
    best_ord = None

    for pp in combinations(range(A), Z):
        o = [0] * A
        for p in pp:
            o[p] = 1
        # Compute Phi = sum log|V_hat_i|
        Phi = 0.0
        ok = True
        for gen in range(A - 1):
            V = chain_V(o, gen)
            if abs(V) < 1e-300:
                ok = False
                break
            Phi += math.log(abs(V))
        if ok and Phi < best_Phi:
            best_Phi = Phi
            best_ord = o[:]

    return best_ord, best_Phi


# Build ground states for key nuclei
nuclei = {
    '3H':  {'Z': 1, 'N': 2, 'Q_exp': 0.018592},
    '3He': {'Z': 2, 'N': 1, 'Q_exp': None},
    '6He': {'Z': 2, 'N': 4, 'Q_exp': 3.508},
    '6Li': {'Z': 3, 'N': 3, 'Q_exp': None},
    '14C': {'Z': 6, 'N': 8, 'Q_exp': 0.156476},
    '14N': {'Z': 7, 'N': 7, 'Q_exp': None},
}

gs_cache = {}
for name, info in nuclei.items():
    Z, N = info['Z'], info['N']
    A = Z + N
    print(f"\n  {name}: Z={Z}, N={N}, A={A}")
    gs, Phi = find_ground_state(Z, N)
    gs_cache[name] = gs
    print(f"    GS = {gs}")
    print(f"    Phi = {Phi:+.6f}")

    # NF vector
    nf = nuclear_nf_full(gs)
    print(f"    NF = [{', '.join(f'{v:+.4f}' for v in nf)}]")
    print(f"    tr_M = {markov_trace(nf):.8f}")

    # Also show via vertex volumes
    if A >= 2:
        vols = [chain_V(gs, i) for i in range(A - 1)]
        print(f"    V_hat = [{', '.join(f'{v:+.4f}' for v in vols)}]")
        print(f"    prod|V| = {math.exp(Phi):.8f}")


# ══════════════════════════════════════════════════════════════════
#  T_BETA DUAL ACTION ON NUCLEI
# ══════════════════════════════════════════════════════════════════

print("\n" + "=" * 72)
print("  T_BETA DUAL ACTION ON NUCLEI")
print("=" * 72)
print("  T_beta^vee acts on NF(nucleus) by right multiplication:")
print("  result = NF(nucleus . T_beta^vee)")
print()
print("  For beta- decay (Z,N) -> (Z+1,N-1) + e- + nu_bar:")
print("  The difference NF(result) - NF(daughter) should give emitted particles")


def act_tbeta(nucleus_vec, action='right', dual=True):
    """Act T_beta (or T_beta^vee) on a nuclear NF vector.

    action='right': NF(nucleus . T_beta)
    action='left':  NF(T_beta . nucleus)
    dual=True: use T_beta^vee instead of T_beta
    """
    op = T_beta_dual if dual else T_beta
    op_terms = from_vec(op)
    nuc_terms = from_vec(nucleus_vec)

    if action == 'right':
        prod = hecke_mul(nuc_terms, op_terms)
    else:
        prod = hecke_mul(op_terms, nuc_terms)

    nf = reduce_nf(prod)
    return to_vec(nf)


def analyze_decay(parent_name, daughter_name):
    """Full analysis of beta- decay via T_beta dual action."""
    parent_info = nuclei[parent_name]
    daughter_info = nuclei[daughter_name]

    parent_gs = gs_cache[parent_name]
    daughter_gs = gs_cache[daughter_name]

    parent_nf = nuclear_nf_full(parent_gs)
    daughter_nf = nuclear_nf_full(daughter_gs)

    print(f"\n{'━' * 72}")
    print(f"  DECAY: {parent_name} -> {daughter_name} + e- + nu_bar")
    print(f"{'━' * 72}")

    print(f"\n  Parent  NF({parent_name}):  [{', '.join(f'{v:+.6f}' for v in parent_nf)}]")
    print(f"  Daughter NF({daughter_name}): [{', '.join(f'{v:+.6f}' for v in daughter_nf)}]")
    print(f"  tr_M(parent)   = {markov_trace(parent_nf):.10f}")
    print(f"  tr_M(daughter) = {markov_trace(daughter_nf):.10f}")

    # Act T_beta on parent (4 variants)
    variants = [
        ('right, T_beta',      'right', False),
        ('right, T_beta^vee',  'right', True),
        ('left,  T_beta',      'left',  False),
        ('left,  T_beta^vee',  'left',  True),
    ]

    results = {}
    for label, action, dual in variants:
        result = act_tbeta(parent_nf, action=action, dual=dual)
        tr = markov_trace(result)
        results[label] = result

        print(f"\n  --- {label} ---")
        print(f"  Result:  [{', '.join(f'{v:+.6f}' for v in result)}]")
        print(f"  tr_M     = {tr:.10f}")

        # Decompose: result = daughter + emitted
        emitted = result - daughter_nf
        emitted_tr = markov_trace(emitted)
        print(f"  Emitted: [{', '.join(f'{v:+.6f}' for v in emitted)}]")
        print(f"  tr_M(emitted) = {emitted_tr:.10f}")

        # Component analysis
        print(f"  Component breakdown:")
        for i in range(6):
            if abs(emitted[i]) > 1e-10:
                print(f"    {NF_DISPLAY[i]:5s}: {emitted[i]:+.6f}")

        # Frobenius norm of emitted
        frob = math.sqrt(abs(emitted @ G @ emitted))
        print(f"  ||emitted||_F = {frob:.10f}")

        # Q-value candidates
        # (a) From electron channel
        e_coeff = result[5]  # e- component of result
        Q_electron = abs(e_coeff) * z**2 * m_e
        print(f"  Q from |e- coeff| * z^2 * m_e = {Q_electron:.6f} MeV")

        # (b) From Frobenius norm of emitted
        Q_frob = frob * z**2 * m_e
        print(f"  Q from ||emitted||_F * z^2 * m_e = {Q_frob:.6f} MeV")

        # (c) From trace difference
        tr_diff = abs(tr - markov_trace(daughter_nf))
        Q_trace = tr_diff * m_e
        print(f"  Q from |tr diff| * m_e = {Q_trace:.6f} MeV")

        # (d) From Gram pairing <emitted, T_beta>_F
        gram_pairing = emitted @ G @ T_beta
        Q_gram = abs(gram_pairing) * m_e
        print(f"  Q from |<emitted, T_beta>_F| * m_e = {Q_gram:.6f} MeV")

    if parent_info['Q_exp']:
        print(f"\n  CODATA Q_exp = {parent_info['Q_exp']:.6f} MeV")

    return results


# Run the decays
print("\n" + "=" * 72)
print("  DECAY ANALYSIS")
print("=" * 72)

# Tritium -> He-3
results_3H = analyze_decay('3H', '3He')

# He-6 -> Li-6
results_6He = analyze_decay('6He', '6Li')

# C-14 -> N-14
results_14C = analyze_decay('14C', '14N')


# ══════════════════════════════════════════════════════════════════
#  GRAM MATRIX Q-VALUE (the established working formula)
# ══════════════════════════════════════════════════════════════════

print("\n" + "=" * 72)
print("  COMPARISON: GRAM MATRIX Q-VALUE (vertex volume method)")
print("=" * 72)

E_gram = z**2 * m_e

decays = [
    ('3H', '3He', 0.018592),
    ('6He', '6Li', 3.508),
    ('14C', '14N', 0.156476),
]

print(f"\n  E_gram = z^2 * m_e = {E_gram:.8f} MeV")
print(f"\n  {'Decay':>12s} | {'Q_gram':>10s} | {'Q_exp':>10s} | {'Error':>8s}")
print(f"  {'':->48s}")

for par, dau, Q_exp in decays:
    gs_par = gs_cache[par]
    gs_dau = gs_cache[dau]
    A = len(gs_par)

    V_par = [chain_V(gs_par, i) for i in range(A - 1)]
    V_dau = [chain_V(gs_dau, i) for i in range(A - 1)]

    sum_dV = sum(V_dau[i] - V_par[i] for i in range(A - 1))
    Q_pred = abs(sum_dV) * E_gram

    err = (Q_pred / Q_exp - 1) * 100
    print(f"  {par:>4s}->{dau:<4s}  | {Q_pred:>10.6f} | {Q_exp:>10.6f} | {err:>+7.1f}%")


# ══════════════════════════════════════════════════════════════════
#  EIGENSPACE DECOMPOSITION OF G
# ══════════════════════════════════════════════════════════════════

print("\n" + "=" * 72)
print("  EIGENSPACE DECOMPOSITION OF G")
print("=" * 72)

eigvals_full, eigvecs = np.linalg.eigh(G)
print(f"  Eigenvalues: {eigvals_full}")
print(f"  Eigenvectors (columns):")
for i in range(6):
    evec = eigvecs[:, i]
    label = f"  v_{i} (lam={eigvals_full[i]:.6f})"
    print(f"  {label}: [{', '.join(f'{v:+.4f}' for v in evec)}]")

# Project T_beta into each eigenspace
print(f"\n  T_beta projection into eigenspaces:")
for i in range(6):
    evec = eigvecs[:, i]
    proj = np.dot(T_beta, evec)
    print(f"    eigenspace {i} (lam={eigvals_full[i]:.6f}): proj = {proj:+.6f}")

# Project nuclear NF vectors into eigenspaces
for name in ['3H', '3He', '6He', '6Li', '14C', '14N']:
    nf = nuclear_nf_full(gs_cache[name])
    print(f"\n  {name} NF projection:")
    for i in range(6):
        evec = eigvecs[:, i]
        proj = np.dot(nf, evec)
        if abs(proj) > 1e-10:
            print(f"    eigenspace {i} (lam={eigvals_full[i]:.6f}): {proj:+.6f}")


# ══════════════════════════════════════════════════════════════════
#  T_BETA EMBEDDED AT EACH POSITION
# ══════════════════════════════════════════════════════════════════

print("\n" + "=" * 72)
print("  T_BETA EMBEDDED AT EACH POSITION IN NUCLEAR CHAIN")
print("=" * 72)
print("  For beta- decay at position k in A-nucleon chain:")
print("  Change nucleon k from n->p, modify crossings at that position")
print("  Q_k = |V_hat_k(daughter) - V_hat_k(parent)| * E_gram")


def compute_positional_Q(parent_gs, daughter_gs, Q_exp, name):
    """Compute Q-value by summing vertex volume changes at each position."""
    A = len(parent_gs)
    E_gram_local = z**2 * m_e

    # Find which position changed (n->p)
    changed_pos = [i for i in range(A) if parent_gs[i] != daughter_gs[i]]

    V_par = [chain_V(parent_gs, i) for i in range(A - 1)]
    V_dau = [chain_V(daughter_gs, i) for i in range(A - 1)]

    print(f"\n  --- {name} ---")
    print(f"  Parent GS:   {parent_gs}")
    print(f"  Daughter GS: {daughter_gs}")
    print(f"  Changed positions: {changed_pos}")

    print(f"\n  Per-generator vertex volumes:")
    print(f"  {'Gen':>5s} | {'V_par':>10s} | {'V_dau':>10s} | {'Delta':>10s} | {'|Delta|':>10s}")
    print(f"  {'':->55s}")

    sum_dV = 0.0
    sum_abs_dV = 0.0
    for i in range(A - 1):
        dV = V_dau[i] - V_par[i]
        sum_dV += dV
        sum_abs_dV += abs(dV)
        mark = " <--" if i in changed_pos or (i + 1) in changed_pos else ""
        print(f"  {i:>5d} | {V_par[i]:>10.6f} | {V_dau[i]:>10.6f} | {dV:>+10.6f} | {abs(dV):>10.6f}{mark}")

    Q_linear = abs(sum_dV) * E_gram_local
    Q_sum_abs = sum_abs_dV * E_gram_local

    # Frobenius approach: delta as 6-vector, ||delta||_F via G
    delta_nf = nuclear_nf_full(daughter_gs) - nuclear_nf_full(parent_gs)
    frob_delta = delta_nf @ G @ delta_nf
    Q_frob = math.sqrt(abs(frob_delta)) * E_gram_local

    # Log ratio (Phi difference)
    Phi_par = sum(math.log(abs(v)) for v in V_par)
    Phi_dau = sum(math.log(abs(v)) for v in V_dau)
    dPhi = Phi_dau - Phi_par

    print(f"\n  sum(dV) = {sum_dV:+.8f}")
    print(f"  sum|dV| = {sum_abs_dV:.8f}")
    print(f"  Q_linear  = |sum(dV)| * E_gram = {Q_linear:.6f} MeV")
    print(f"  Q_sum_abs = sum|dV| * E_gram    = {Q_sum_abs:.6f} MeV")
    print(f"  Q_frob    = ||delta||_F * E_gram = {Q_frob:.6f} MeV")
    print(f"  dPhi = Phi_dau - Phi_par = {dPhi:+.8f}")
    print(f"  Q_phi = |dPhi| * m_e = {abs(dPhi) * m_e:.6f} MeV")

    if Q_exp:
        print(f"\n  CODATA Q_exp = {Q_exp:.6f} MeV")
        print(f"  Error (linear):  {(Q_linear/Q_exp - 1)*100:+.1f}%")
        print(f"  Error (sum|dV|): {(Q_sum_abs/Q_exp - 1)*100:+.1f}%")
        print(f"  Error (frob):    {(Q_frob/Q_exp - 1)*100:+.1f}%")
        print(f"  Error (dPhi):    {(abs(dPhi)*m_e/Q_exp - 1)*100:+.1f}%")

    return {
        'Q_linear': Q_linear, 'Q_sum_abs': Q_sum_abs,
        'Q_frob': Q_frob, 'Q_phi': abs(dPhi) * m_e,
        'sum_dV': sum_dV, 'dPhi': dPhi,
    }


for par, dau, Q_exp in decays:
    compute_positional_Q(gs_cache[par], gs_cache[dau], Q_exp,
                         f"{par} -> {dau}")


# ══════════════════════════════════════════════════════════════════
#  BRANE TOWER: JET BUNDLE DEGREES 0, 1, 2
# ══════════════════════════════════════════════════════════════════

print("\n" + "=" * 72)
print("  BRANE TOWER: JET BUNDLE DEGREES 0, 1, 2")
print("=" * 72)
print("  Degree 0: identity braid (already computed above)")
print("  Degree 1: 4 torus knots T(2,1), T(2,3), T(2,5), T(2,7)")
print("  Degree 2: 2 torus knots T(2,2), T(2,4)")
print("  Higher degrees: terminated by Sigma_4 quotient")

# Torus knot braids (in H_3)
TORUS_KNOTS = {
    # Degree 1: single-crossing torus knots
    'T(2,1)': [(0,)],  # sigma_0
    'T(2,3)': [(0, 1, 0)],  # sigma_0 sigma_1 sigma_0 = e-
    'T(2,5)': [(0, 1, 0, 1, 0)],  # 5-crossing torus
    'T(2,7)': [(0, 1, 0, 1, 0, 1, 0)],  # 7-crossing torus
    # Degree 2: double-crossing torus knots
    'T(2,2)': [(0, 0)],  # sigma_0^2
    'T(2,4)': [(0, 1, 0, 0)],  # 4-crossing torus
}


def torus_knot_nf(word):
    """Compute NF of a torus knot braid word."""
    terms = {tuple(word): 1.0}
    nf = reduce_nf(terms)
    return to_vec(nf)


print(f"\n  Torus knot NF vectors:")
print(f"  {'Knot':>10s} | {'deg':>3s} | {'NF':>50s} | {'tr_M':>10s}")
print(f"  {'':->80s}")
for name, words in TORUS_KNOTS.items():
    for word in words:
        nf = torus_knot_nf(word)
        tr = markov_trace(nf)
        deg = (len(word) + 1) // 2
        nf_str = ', '.join(f'{v:+.4f}' for v in nf)
        print(f"  {name:>10s} | {deg:>3d} | [{nf_str}] | {tr:>10.6f}")


# Brane tower contribution: at each generator position in the nuclear
# chain, the brane tower wraps a torus knot around the tube.
# The contribution is the quantum dilogarithm Li_2(V_hat_i).

def q_dilog(x):
    """Quantum dilogarithm Li_2(x) = sum_{n=1}^inf x^n / (n * [n]_q)."""
    result = 0.0
    for n in range(1, 100):
        qn = (q**n - qi**n) / h  # [n]_q
        term = x**n / (n * qn)
        result += term
        if abs(term) < 1e-15:
            break
    return result


print(f"\n  Brane tower contributions (quantum dilogarithm):")
for par, dau, Q_exp in decays:
    gs_par = gs_cache[par]
    gs_dau = gs_cache[dau]
    A = len(gs_par)

    V_par = [chain_V(gs_par, i) for i in range(A - 1)]
    V_dau = [chain_V(gs_dau, i) for i in range(A - 1)]

    print(f"\n  --- {par} -> {dau} ---")

    # Degree 0: sum dV (already computed)
    sum_dV_0 = sum(V_dau[i] - V_par[i] for i in range(A - 1))

    # Degree 1: quantum dilogarithm Li_2(V_hat)
    # The spectral coordinate z_i at generator i is V_hat_i
    Li2_par = sum(q_dilog(V_par[i]) for i in range(A - 1))
    Li2_dau = sum(q_dilog(V_dau[i]) for i in range(A - 1))
    sum_dLi2 = Li2_dau - Li2_par

    # Degree 2: Li_2 of squared vertex volumes (next jet)
    Li2_sq_par = sum(q_dilog(V_par[i]**2) for i in range(A - 1) if abs(V_par[i]) < 1)
    Li2_sq_dau = sum(q_dilog(V_dau[i]**2) for i in range(A - 1) if abs(V_dau[i]) < 1)
    sum_dLi2_sq = Li2_sq_dau - Li2_sq_par

    # Total tower sum
    tower_sum = sum_dV_0 + sum_dLi2 + sum_dLi2_sq
    Q_tower = abs(tower_sum) * z**2 * m_e

    print(f"  Degree 0 (dV):     {sum_dV_0:+.8f}")
    print(f"  Degree 1 (dLi2):   {sum_dLi2:+.8f}")
    print(f"  Degree 2 (dLi2²):  {sum_dLi2_sq:+.8f}")
    print(f"  Tower sum:         {tower_sum:+.8f}")
    print(f"  Q_tower = |sum| * z² * m_e = {Q_tower:.6f} MeV")
    if Q_exp:
        print(f"  CODATA Q_exp = {Q_exp:.6f} MeV")
        if Q_tower > 1e-10:
            print(f"  Error: {(Q_tower/Q_exp - 1)*100:+.1f}%")


# ══════════════════════════════════════════════════════════════════
#  SUMMARY TABLE
# ══════════════════════════════════════════════════════════════════

print("\n" + "=" * 72)
print("  SUMMARY: ALL Q-VALUE FORMULAS")
print("=" * 72)

print(f"\n  {'Decay':>12s} | {'Q_exp':>8s} | {'dV*z²me':>8s} | {'dPhi*me':>8s} | {'||dNF||':>8s} | {'tower':>8s}")
print(f"  {'':->65s}")

for par, dau, Q_exp in decays:
    gs_par = gs_cache[par]
    gs_dau = gs_cache[dau]
    A = len(gs_par)
    V_par = [chain_V(gs_par, i) for i in range(A - 1)]
    V_dau = [chain_V(gs_dau, i) for i in range(A - 1)]

    sum_dV = sum(V_dau[i] - V_par[i] for i in range(A - 1))
    Q_dV = abs(sum_dV) * z**2 * m_e

    Phi_par = sum(math.log(abs(v)) for v in V_par)
    Phi_dau = sum(math.log(abs(v)) for v in V_dau)
    Q_phi = abs(Phi_dau - Phi_par) * m_e

    delta_nf = nuclear_nf_full(gs_dau) - nuclear_nf_full(gs_par)
    frob_delta = delta_nf @ G @ delta_nf
    Q_frob = math.sqrt(abs(frob_delta)) * z**2 * m_e

    # Tower
    Li2_par = sum(q_dilog(V_par[i]) for i in range(A - 1))
    Li2_dau = sum(q_dilog(V_dau[i]) for i in range(A - 1))
    Li2_sq_par = sum(q_dilog(V_par[i]**2) for i in range(A - 1) if abs(V_par[i]) < 1)
    Li2_sq_dau = sum(q_dilog(V_dau[i]**2) for i in range(A - 1) if abs(V_dau[i]) < 1)
    tower = sum_dV + (Li2_dau - Li2_par) + (Li2_sq_dau - Li2_sq_par)
    Q_tower = abs(tower) * z**2 * m_e

    print(f"  {par:>4s}->{dau:<4s}  | {Q_exp:>8.4f} | {Q_dV:>8.4f} | {Q_phi:>8.4f} | {Q_frob:>8.4f} | {Q_tower:>8.4f}")


# ══════════════════════════════════════════════════════════════════
#  WITNESS
# ══════════════════════════════════════════════════════════════════

witness = {
    'name': 'tbeta-dual-action',
    'timestamp': datetime.now(timezone.utc).isoformat(),
    'parameters': {'q': q, 'h': h, 'z': z, 'm_e': m_e},
    'T_beta': T_beta.tolist(),
    'T_beta_dual': T_beta_dual.tolist(),
    'tr_T_beta': float(markov_trace(T_beta)),
    'tr_T_beta_dual': float(markov_trace(T_beta_dual)),
    'frob_norm_T_beta': float(frob_norm),
    'gram_matrix': G.tolist(),
    'gram_inverse': G_inv.tolist(),
    'gram_eigenvalues': eigvals_full.tolist(),
    'ground_states': {
        name: {
            'ordering': gs_cache[name],
            'nf': nuclear_nf_full(gs_cache[name]).tolist(),
        } for name in nuclei
    },
}

out_path = Path(__file__).with_suffix('.witness.json')
out_path.write_text(json.dumps(witness, indent=2, default=float))
print(f"\n  Witness: {out_path.name}")
