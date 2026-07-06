#!/usr/bin/env python3
"""
Full H_6(q) computation for 6He -> 6Li beta decay.

Instead of projecting to H_3(q), this works in the FULL 6-strand
Hecke algebra H_6(q) with generators sigma_0..sigma_4.

The nuclear element in H_A(q) is:
  N(ordering) = prod_{i=0}^{A-2} (c_i * sigma_i + d_i)
where (c_i, d_i) depends on the crossing type at position i.

Crossing coefficients (from shell-construction-rules.md):
  pp: (c, d) = (1, 0)        -> sigma_i
  nn: (c, d) = (1, -h)       -> sigma_i - h
  mix: (c, d) = (1, -h/2)    -> sigma_i - h/2

The Markov trace in H_n is computed recursively:
  tr_M(1) = 1
  tr_M(w * sigma_{n-1}) = z * tr_M(w)  [Markov II]
  tr_M(ab) = tr_M(ba)  [cyclicity]

For magic shell crossings, the torus knot operators UNWIND and
TWIST the shell structure. At Z=2 (magic), the 1s closure needs:
  - UNWIND operator: T_{2,2}^{-1} to open the closed shell
  - TWIST operator: T_{2,k} to bind into new shell

Usage:
    cd computations && python3 h6-full-computation.py
"""
import math
import json
import sys
import numpy as np
from itertools import combinations
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q as q, Q_INV as qi, HA as h, HBAR_Q, LN_Q, log_q

z = 1.0 / (q**0.5 + q**(-0.5))
m_e = 0.51099895
E_cross = 0.5 * h
mu_0 = m_e / (3 * E_cross)

print(f"q = {q:.10f}, h = {h:.10f}, z = {z:.10f}")
print(f"hbar_q = {HBAR_Q:.10f}, E_cross = {E_cross:.10f}")


# ══════════════════════════════════════════════════════════════════
#  H_n(q) HECKE ALGEBRA ENGINE (arbitrary n)
# ══════════════════════════════════════════════════════════════════

def hecke_mul(t1, t2):
    """Multiply two elements (dicts of {word: coeff})."""
    r = {}
    for w1, c1 in t1.items():
        for w2, c2 in t2.items():
            w = w1 + w2
            r[w] = r.get(w, 0.0) + c1 * c2
    return {w: c for w, c in r.items() if abs(c) > 1e-14}


def reduce_nf(terms):
    """Reduce to NF using Hecke + braid relations. Works for any H_n."""
    changed = True
    iters = 0
    while changed:
        changed = False
        iters += 1
        if iters > 10000:
            break
        new = {}
        for word, coeff in terms.items():
            if abs(coeff) < 1e-14:
                continue
            done = False
            # Hecke: sigma_i^2 = h*sigma_i + 1
            for p in range(len(word) - 1):
                if word[p] == word[p + 1]:
                    pre, suf = word[:p], word[p + 2:]
                    w1 = pre + (word[p],) + suf
                    w2 = pre + suf
                    new[w1] = new.get(w1, 0.0) + coeff * h
                    new[w2] = new.get(w2, 0.0) + coeff
                    done = changed = True
                    break
            if done:
                continue
            # Braid: sigma_i sigma_j sigma_i = sigma_j sigma_i sigma_j (|i-j|=1)
            for p in range(len(word) - 2):
                a, b, c = word[p], word[p + 1], word[p + 2]
                if a == c and abs(a - b) == 1:
                    nt = (b, a, b)
                    if nt < (a, b, a):
                        nw = word[:p] + nt + word[p + 3:]
                        new[nw] = new.get(nw, 0.0) + coeff
                        done = changed = True
                        break
            if done:
                continue
            # Far commutativity: sigma_i sigma_j -> sigma_j sigma_i if j < i and |i-j| > 1
            for p in range(len(word) - 1):
                if word[p] > word[p + 1] and abs(word[p] - word[p + 1]) > 1:
                    nw = word[:p] + (word[p + 1], word[p]) + word[p + 2:]
                    new[nw] = new.get(nw, 0.0) + coeff
                    done = changed = True
                    break
            if not done:
                new[word] = new.get(word, 0.0) + coeff
        terms = {w: c for w, c in new.items() if abs(c) > 1e-14}
    return terms


def markov_trace_word(word, n_strands):
    """Markov trace of a single NF word in H_n(q).

    Recursive: peel off the highest generator using Markov II.
    For a word containing sigma_{n-1}: use cyclicity to move it
    to the right end, then tr_M(w * sigma_{n-1}) = z * tr_M(w).
    """
    if not word:
        return 1.0
    if n_strands <= 1:
        return 1.0

    max_gen = max(word)
    top = n_strands - 1  # highest generator index

    if max_gen < top:
        # Word lives in H_{n-1}
        return markov_trace_word(word, n_strands - 1)

    # Find rightmost occurrence of sigma_{top}
    pos = len(word) - 1
    while pos >= 0 and word[pos] != top:
        pos -= 1

    if pos == len(word) - 1:
        # sigma_{top} is at the right end: Markov II
        return z * markov_trace_word(word[:pos], n_strands)

    # sigma_{top} not at right end. Use cyclicity:
    # tr(A sigma_{top} B) = tr(B A sigma_{top}) = z * tr(B A)
    # BUT: B A needs to be reduced before computing trace
    A = word[:pos]
    B = word[pos + 1:]
    new_word_terms = hecke_mul({B: 1.0}, {A: 1.0})
    new_word_terms = reduce_nf(new_word_terms)
    return z * markov_trace_element(new_word_terms, n_strands)


def markov_trace_element(terms, n_strands):
    """Markov trace of an element (dict of {word: coeff}) in H_n(q)."""
    total = 0.0
    for word, coeff in terms.items():
        total += coeff * markov_trace_word(word, n_strands)
    return total


# ══════════════════════════════════════════════════════════════════
#  NUCLEAR ELEMENTS IN H_6(q)
# ══════════════════════════════════════════════════════════════════

print("\n" + "=" * 72)
print("  NUCLEAR ELEMENTS IN FULL H_6(q)")
print("=" * 72)


def nuclear_element_Hn(ordering):
    """Build nuclear element in H_A(q) from ordering.

    N(ordering) = prod_{i=0}^{A-2} (c_i * sigma_i + d_i)

    Crossing coefficients:
      pp: sigma_i          (c=1, d=0)
      nn: sigma_i - h      (c=1, d=-h)
      mix: sigma_i - h/2   (c=1, d=-h/2)
    """
    A = len(ordering)
    result = {(): 1.0}  # start with identity

    for i in range(A - 1):
        ti, tj = ordering[i], ordering[i + 1]
        if ti == 1 and tj == 1:  # pp
            factor = {(i,): 1.0}
        elif ti == 0 and tj == 0:  # nn
            factor = {(i,): 1.0, (): -h}
        else:  # mix
            factor = {(i,): 1.0, (): -h / 2}

        result = hecke_mul(result, factor)
        result = reduce_nf(result)

    return result


# Find ground states
def find_gs(Z, N):
    A = Z + N
    best = (float('inf'), None)
    for pp in combinations(range(A), Z):
        o = [0] * A
        for p in pp:
            o[p] = 1
        # Use transfer matrix Phi
        a_val, b_val = 0.0, 1.0
        Phi = 0.0
        ok = True
        for gen in range(A - 1):
            a_v, b_v = 0.0, 1.0
            for j in range(gen + 1, A):
                ti, tj = o[gen], o[j]
                if ti == 1 and tj == 1:
                    d_val = 0.0
                elif ti == 0 and tj == 0:
                    d_val = -h
                else:
                    d_val = -h / 2
                na = a_v * h + a_v * d_val + b_v
                nb = a_v + b_v * d_val
                a_v, b_v = na, nb
            V = z * a_v + b_v
            if abs(V) < 1e-300:
                ok = False
                break
            Phi += math.log(abs(V))
        if ok and Phi < best[0]:
            best = (Phi, o[:])
    return best[1], best[0]


gs_6he, phi_6he = find_gs(2, 4)
gs_6li, phi_6li = find_gs(3, 3)

print(f"\n  6He GS = {gs_6he}, Phi = {phi_6he:+.6f}")
print(f"  6Li GS = {gs_6li}, Phi = {phi_6li:+.6f}")

# Build nuclear elements in H_6(q)
N_6he = nuclear_element_Hn(gs_6he)
N_6li = nuclear_element_Hn(gs_6li)

n_strands = 6

# Show the elements
print(f"\n  N(6He) in H_6(q): {len(N_6he)} terms")
for word, coeff in sorted(N_6he.items(), key=lambda x: (-abs(x[1]))):
    if abs(coeff) > 1e-10:
        w_str = ''.join(f'σ{g}' for g in word) if word else '1'
        print(f"    {coeff:+.6f} * {w_str}")

print(f"\n  N(6Li) in H_6(q): {len(N_6li)} terms")
for word, coeff in sorted(N_6li.items(), key=lambda x: (-abs(x[1]))):
    if abs(coeff) > 1e-10:
        w_str = ''.join(f'σ{g}' for g in word) if word else '1'
        print(f"    {coeff:+.6f} * {w_str}")

# Markov traces
tr_6he = markov_trace_element(N_6he, n_strands)
tr_6li = markov_trace_element(N_6li, n_strands)

print(f"\n  tr_M(6He) in H_6 = {tr_6he:.10f}")
print(f"  tr_M(6Li) in H_6 = {tr_6li:.10f}")
print(f"  Difference = {tr_6li - tr_6he:.10f}")
print(f"  |diff| * m_e = {abs(tr_6li - tr_6he) * m_e:.6f} MeV")


# ══════════════════════════════════════════════════════════════════
#  GRAM MATRIX IN H_6(q) (restricted to nuclear subspace)
# ══════════════════════════════════════════════════════════════════

print("\n" + "=" * 72)
print("  GRAM MATRIX IN H_6(q) NUCLEAR SUBSPACE")
print("=" * 72)

# Collect all NF basis words that appear in 6He and 6Li
all_words = set()
for terms in [N_6he, N_6li]:
    for word in terms:
        all_words.add(word)

all_words = sorted(all_words)
dim = len(all_words)
word_idx = {w: i for i, w in enumerate(all_words)}

print(f"  Subspace dimension: {dim}")
print(f"  Basis words:")
for i, w in enumerate(all_words):
    w_str = ''.join(f'σ{g}' for g in w) if w else '1'
    print(f"    [{i}] {w_str}")

# Gram matrix: G_{ij} = tr_M(b_i * b_j)
G6 = np.zeros((dim, dim))
for i, wi in enumerate(all_words):
    for j, wj in enumerate(all_words):
        prod = hecke_mul({wi: 1.0}, {wj: 1.0})
        prod = reduce_nf(prod)
        G6[i, j] = markov_trace_element(prod, n_strands)

print(f"\n  Gram matrix G ({dim}x{dim}):")
for i in range(dim):
    w_str = ''.join(f'σ{g}' for g in all_words[i]) if all_words[i] else '1'
    row = '  '.join(f'{G6[i,j]:+.6f}' for j in range(dim))
    print(f"    {w_str:>20s} | {row}")

det_G6 = np.linalg.det(G6)
eigvals_G6 = np.linalg.eigvalsh(G6)
print(f"\n  det(G) = {det_G6:.10f}")
print(f"  eigenvalues = {sorted(eigvals_G6)}")

# Vectors for 6He and 6Li in this basis
vec_6he = np.array([N_6he.get(w, 0.0) for w in all_words])
vec_6li = np.array([N_6li.get(w, 0.0) for w in all_words])
delta = vec_6li - vec_6he

print(f"\n  vec(6He) = [{', '.join(f'{v:+.6f}' for v in vec_6he)}]")
print(f"  vec(6Li) = [{', '.join(f'{v:+.6f}' for v in vec_6li)}]")
print(f"  delta    = [{', '.join(f'{v:+.6f}' for v in delta)}]")

# Frobenius norm of delta
frob2 = delta @ G6 @ delta
print(f"\n  delta . G . delta = {frob2:+.10f}")
print(f"  ||delta||_F = {math.sqrt(abs(frob2)):.10f}")


# ══════════════════════════════════════════════════════════════════
#  KNOT OPERATORS IN H_6(q) — UNWIND + TWIST
# ══════════════════════════════════════════════════════════════════

print("\n" + "=" * 72)
print("  KNOT OPERATORS IN H_6(q)")
print("=" * 72)
print("  For magic shell crossing, we need:")
print("  UNWIND: T_{2,2}^{-1} to open the 1s closed shell")
print("  TWIST: T_{2,k} to bind into new shell structure")

# T_beta at each position in H_6
# The weak vertex at position i converts nucleon i from n->p
# T_beta_i = sigma_i - h/2 * 1 (mixed crossing replacement)
# But the FULL weak vertex also includes the shell operators

# First: act T_beta embedded at each position
print("\n  T_beta embedded at each nucleon position:")
for pos in range(5):  # positions 0..4 in H_6
    # T_beta at position pos: replace the crossing at position pos
    # with the weak vertex operator
    T_beta_pos = {(pos,): 1.0, (): -h}  # sigma_pos - h (like nn->mix transition)
    T_beta_pos = reduce_nf(T_beta_pos)

    # Act on 6He: NF(6He * T_beta_pos)
    result = hecke_mul(N_6he, T_beta_pos)
    result = reduce_nf(result)
    tr_result = markov_trace_element(result, n_strands)

    # Also try left action
    result_L = hecke_mul(T_beta_pos, N_6he)
    result_L = reduce_nf(result_L)
    tr_result_L = markov_trace_element(result_L, n_strands)

    print(f"\n  Position {pos}: T_beta = sigma_{pos} - h")
    print(f"    RIGHT: tr_M(6He * T_beta_{pos}) = {tr_result:.10f}")
    print(f"    LEFT:  tr_M(T_beta_{pos} * 6He) = {tr_result_L:.10f}")
    print(f"    |tr_R - tr_6Li| * m_e = {abs(tr_result - tr_6li) * m_e:.6f} MeV")
    print(f"    |tr_L - tr_6Li| * m_e = {abs(tr_result_L - tr_6li) * m_e:.6f} MeV")


# ══════════════════════════════════════════════════════════════════
#  DUAL ACTION VIA G^{-1} IN H_6
# ══════════════════════════════════════════════════════════════════

print("\n" + "=" * 72)
print("  FROBENIUS DUAL ACTION IN H_6(q)")
print("=" * 72)

if abs(det_G6) > 1e-15:
    G6_inv = np.linalg.inv(G6)

    # Frobenius dual of each knot operator
    # Project knot into the nuclear subspace, then apply G^{-1}

    knot_ops = [
        ("T_beta_3", {(3,): 1.0, (): -h}),       # at position 3 (mix crossing)
        ("T_beta_4", {(4,): 1.0, (): -h}),       # at position 4 (nn crossing)
        ("T_{2,2}_01", {(0, 0): 1.0}),            # Hopf at positions 0-1
        ("T_{2,2}_12", {(1, 1): 1.0}),            # Hopf at positions 1-2
        ("T_{2,2}_34", {(3, 3): 1.0}),            # Hopf at positions 3-4
        ("T_{2,3}_012", {(0, 1, 0): 1.0}),        # trefoil at 0-1-2
        ("T_{2,3}_234", {(2, 3, 2): 1.0}),        # trefoil at 2-3-4
        ("T_{2,5}_01234", {(0, 1, 0, 1, 0): 1.0}), # cinquefoil spanning all
        ("unwind_T22", {(0,): 1.0, (): -h}),      # T_{2,2}^{-1} = sigma - h (unwind)
        ("twist_T23", {(0, 1, 0): 1.0}),          # T_{2,3} (twist to new shell)
    ]

    for name, raw_op in knot_ops:
        op = reduce_nf(raw_op)

        # Project operator into nuclear subspace
        op_vec = np.array([op.get(w, 0.0) for w in all_words])

        # Check if operator has support in the subspace
        if np.linalg.norm(op_vec) < 1e-14:
            # Operator lives outside the nuclear subspace
            # Need to expand the basis. For now, compute trace directly.
            result = hecke_mul(N_6he, op)
            result = reduce_nf(result)
            tr_result = markov_trace_element(result, n_strands)
            print(f"\n  {name}: (outside subspace)")
            print(f"    tr_M(6He * K) = {tr_result:.10f}")
            print(f"    |tr - tr_6Li| * m_e = {abs(tr_result - tr_6li)*m_e:.6f} MeV")
            continue

        # Frobenius dual: K^vee = op_vec . G^{-1}
        dual_vec = op_vec @ G6_inv

        # Reconstruct dual as Hecke element
        dual_terms = {}
        for i, w in enumerate(all_words):
            if abs(dual_vec[i]) > 1e-14:
                dual_terms[w] = dual_vec[i]

        # Act on 6He
        result = hecke_mul(N_6he, dual_terms)
        result = reduce_nf(result)
        tr_result = markov_trace_element(result, n_strands)

        # Project result into subspace
        result_vec = np.array([result.get(w, 0.0) for w in all_words])
        emitted_vec = result_vec - vec_6li

        # Frobenius norm
        frob2_em = emitted_vec @ G6 @ emitted_vec
        frob_em = math.sqrt(abs(frob2_em))

        Q_frob = frob_em * z**2 * m_e
        Q_tr = abs(tr_result - tr_6li) * m_e

        print(f"\n  {name}:")
        print(f"    op_vec = [{', '.join(f'{v:+.4f}' for v in op_vec)}]")
        print(f"    dual   = [{', '.join(f'{v:+.4f}' for v in dual_vec)}]")
        print(f"    tr_M(6He * K^vee) = {tr_result:.10f}")
        print(f"    ||emitted||_F = {frob_em:.6f}")
        print(f"    Q_frob = {Q_frob:.6f} MeV")
        print(f"    Q_tr   = {Q_tr:.6f} MeV")


# ══════════════════════════════════════════════════════════════════
#  UNWIND + TWIST: COMPOSITE OPERATORS
# ══════════════════════════════════════════════════════════════════

print("\n" + "=" * 72)
print("  COMPOSITE OPERATORS: UNWIND + TWIST")
print("=" * 72)
print("  For Z=2 magic shell breaking:")
print("  Step 1: UNWIND T_{2,2}^{-1} (open the 1s closure)")
print("  Step 2: TWIST T_{2,k} (rebind into new shell)")

# Unwind: T_{2,2}^{-1} at positions touching the proton shell
# T_{2,2}^{-1} = (sigma^2)^{-1} = sigma^{-2} = (sigma - h)^2
# = sigma^2 - 2h*sigma + h^2 = (h*sigma + 1) - 2h*sigma + h^2
# = 1 + h^2 - h*sigma
unwind_raw = {(): 1.0 + h**2, (0,): -h}
unwind = reduce_nf(unwind_raw)

# Various twist operators
twist_ops = [
    ("T_{2,2}", {(0, 0): 1.0}),
    ("T_{2,3}", {(0, 1, 0): 1.0}),
    ("T_{2,5}", {(0, 1, 0, 1, 0): 1.0}),
]

for twist_name, twist_raw in twist_ops:
    twist = reduce_nf(twist_raw)

    # Composite: unwind * twist
    composite = hecke_mul(unwind, twist)
    composite = reduce_nf(composite)

    # Act on 6He
    result = hecke_mul(N_6he, composite)
    result = reduce_nf(result)
    tr_result = markov_trace_element(result, n_strands)

    # Also: twist * unwind (other order)
    composite2 = hecke_mul(twist, unwind)
    composite2 = reduce_nf(composite2)
    result2 = hecke_mul(N_6he, composite2)
    result2 = reduce_nf(result2)
    tr_result2 = markov_trace_element(result2, n_strands)

    # For doubly-magic: apply TWICE (one per shell)
    double = hecke_mul(composite, composite)
    double = reduce_nf(double)
    result_dbl = hecke_mul(N_6he, double)
    result_dbl = reduce_nf(result_dbl)
    tr_dbl = markov_trace_element(result_dbl, n_strands)

    Q_single = abs(tr_result - tr_6li) * m_e
    Q_single2 = abs(tr_result2 - tr_6li) * m_e
    Q_double = abs(tr_dbl - tr_6li) * m_e

    print(f"\n  UNWIND * {twist_name}:")
    print(f"    tr_M(6He * (U*T)) = {tr_result:.8f}, Q = {Q_single:.4f} MeV")
    print(f"    tr_M(6He * (T*U)) = {tr_result2:.8f}, Q = {Q_single2:.4f} MeV")
    print(f"    tr_M(6He * (U*T)^2) = {tr_dbl:.8f}, Q_double = {Q_double:.4f} MeV")
    print(f"    Q_exp = 3.508 MeV")


# ══════════════════════════════════════════════════════════════════
#  FACTOR DECOMPOSITION OF MAGIC NUMBERS
# ══════════════════════════════════════════════════════════════════

print("\n" + "=" * 72)
print("  MAGIC NUMBER FACTOR DECOMPOSITION")
print("=" * 72)
print("  Each magic number's factors determine the operators needed")

magic = [2, 8, 20, 28, 50, 82, 126]
for m in magic:
    # Prime factorization
    factors = []
    n = m
    for p in [2, 3, 5, 7, 11, 13]:
        while n % p == 0:
            factors.append(p)
            n //= p
    if n > 1:
        factors.append(n)
    print(f"  {m:>4d} = {'×'.join(str(f) for f in factors):>12s}  ({len(factors)} factors → {len(factors)} operators)")


# ══════════════════════════════════════════════════════════════════
#  WITNESS
# ══════════════════════════════════════════════════════════════════

witness = {
    'name': 'h6-full-computation',
    'timestamp': datetime.now(timezone.utc).isoformat(),
    'q': q, 'n_strands': n_strands,
    'gs_6he': gs_6he, 'gs_6li': gs_6li,
    'tr_6he': tr_6he, 'tr_6li': tr_6li,
    'gram_det': det_G6,
    'gram_eigenvalues': eigvals_G6.tolist(),
    'subspace_dim': dim,
}
out = Path(__file__).with_suffix('.witness.json')
out.write_text(json.dumps(witness, indent=2, default=float))
print(f"\n  Witness: {out.name}")
