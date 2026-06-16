#!/usr/bin/env python3
"""
Q-values from full Garside NF + Gram weights.

Uses the atom mass engine's NF infrastructure but computes
Q = (Σ w_k^G × Δ_k) × N × m_e
starting from the typed Garside staircase (all C(A,2) crossings).

Usage:
    cd computations && python3 qvalue-garside-gram.py
"""
import math
import json
import sys
import numpy as np
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q as q, Q_INV as qi, HA as h, HBAR_Q
# z/NF_BASIS/TR_M now owned by pyhecke.gram (M2b inversion). Keep local
# bootstrap for dev mode; the installed-pyhecke path is preferred.
import sys as _sys, pathlib as _pl
_sys.path.insert(0, str(_pl.Path(__file__).resolve().parents[2] / "tools" / "pyhecke" / "python"))
from pyhecke.gram import z as _PG_Z, NF_BASIS as _PG_NF_BASIS, TR_M as _PG_TR_M  # noqa: E402

from experimental_constants import (
    M_E_MEV, Q_TRITIUM_MEV, Q_C14_MEV, Q_CO60_MEV,
    Q_SR90_MEV, Q_CS137_MEV, Q_BI210_MEV, Q_NEUTRON_MEV,
)

z = _PG_Z  # moved to pyhecke.gram
#  HECKE ENGINE (reuse from existing scripts)
# ══════════════════════════════════════════════════════════════

def hecke_mul(t1, t2):
    r = {}
    for w1, c1 in t1.items():
        for w2, c2 in t2.items():
            w = w1 + w2
            r[w] = r.get(w, 0.0) + c1 * c2
    return {w: c for w, c in r.items() if abs(c) > 1e-14}


def reduce_nf(terms):
    changed = True
    its = 0
    while changed:
        changed = False
        its += 1
        if its > 200000:
            break
        new = {}
        for word, coeff in terms.items():
            if abs(coeff) < 1e-14:
                continue
            done = False
            for p in range(len(word) - 1):
                if word[p] == word[p + 1]:
                    pre, suf = word[:p], word[p + 2:]
                    new[pre + (word[p],) + suf] = new.get(pre + (word[p],) + suf, 0) + coeff * h
                    new[pre + suf] = new.get(pre + suf, 0) + coeff
                    done = changed = True
                    break
            if done:
                continue
            for p in range(len(word) - 2):
                a, b, c = word[p], word[p + 1], word[p + 2]
                if a == c and abs(a - b) == 1:
                    nt = (b, a, b)
                    if nt < (a, b, c):
                        nw = word[:p] + nt + word[p + 3:]
                        new[nw] = new.get(nw, 0) + coeff
                        done = changed = True
                        break
            if done:
                continue
            for p in range(len(word) - 1):
                if word[p] > word[p + 1] and abs(word[p] - word[p + 1]) > 1:
                    nw = word[:p] + (word[p + 1], word[p]) + word[p + 2:]
                    new[nw] = new.get(nw, 0) + coeff
                    done = changed = True
                    break
            if not done:
                new[word] = new.get(word, 0) + coeff
        terms = {w: c for w, c in new.items() if abs(c) > 1e-14}
    return terms


def markov_trace_word(word, n):
    if not word:
        return 1.0
    if n <= 1:
        return 1.0
    top = n - 1
    if not word or max(word) < top:
        return markov_trace_word(word, n - 1)
    pos = len(word) - 1
    while pos >= 0 and word[pos] != top:
        pos -= 1
    if pos == len(word) - 1:
        return z * markov_trace_word(word[:pos], n)
    A, B = word[:pos], word[pos + 1:]
    nt = hecke_mul({B: 1.0}, {A: 1.0})
    nt = reduce_nf(nt)
    return z * sum(c * markov_trace_word(w, n) for w, c in nt.items())


def markov_trace_elt(terms, n):
    return sum(c * markov_trace_word(w, n) for w, c in terms.items())


def l1_norm(terms):
    return sum(abs(c) for c in terms.values())


# ══════════════════════════════════════════════════════════════
#  TYPED GARSIDE STAIRCASE
# ══════════════════════════════════════════════════════════════

def typed_d(ti, tj):
    if ti == 1 and tj == 1:
        return 0.0
    elif ti == 0 and tj == 0:
        return -h
    else:
        return -h / 2


def build_garside_nf(ordering):
    """Build typed Garside element and reduce to NF.

    All C(A,2) pairwise crossings via staircase construction.
    Each crossing typed by the actual nucleon pair.
    """
    A = len(ordering)
    result = {(): 1.0}
    for level in range(A - 1):
        for sweep in range(level, -1, -1):
            d = typed_d(ordering[sweep], ordering[level + 1])
            factor = {(sweep,): 1.0}
            if abs(d) > 1e-15:
                factor[()] = d
            result = hecke_mul(result, factor)
            result = reduce_nf(result)
    return result


def find_gs(Z, N):
    """Find ground state ordering by exhaustive search."""
    from itertools import combinations
    A = Z + N
    best = (float('inf'), None)
    for pp in combinations(range(A), Z):
        o = [0] * A
        for p in pp:
            o[p] = 1
        # Use transfer matrix Phi as proxy (fast)
        Phi = 0.0
        ok = True
        for gen in range(A - 1):
            a, b = 0.0, 1.0
            for j in range(gen + 1, A):
                ti, tj = o[gen], o[j]
                d = typed_d(ti, tj)
                new_a = a * h + a * d + b
                new_b = a + b * d
                a, b = new_a, new_b
            V = z * a + b
            if abs(V) < 1e-300:
                ok = False
                break
            Phi += math.log(abs(V))
        if ok and Phi < best[0]:
            best = (Phi, o[:])
    return best[1]


# ══════════════════════════════════════════════════════════════
#  GRAM-WEIGHTED Q-VALUE
# ══════════════════════════════════════════════════════════════

def compute_Q_garside_gram(Z, N, Q_exp, name, verbose=True):
    """Full Gram-weighted Q-value from Garside NF.

    Q = (Σ_k w_k^G × Δ_k) × N × m_e

    where w_k^G = ||δ_k||_F / Σ||δ_j||_F (Frobenius norm weight)
    and Δ_k = ||N_par||_1 - ||N_dau^(k)||_1 (NF reduction cost).
    """
    A = Z + N
    n_strands = A

    # Step 1: Ground state ordering
    if verbose:
        print(f"\n{'━' * 70}")
        print(f"  {name}: (Z={Z}, N={N}) → (Z+1={Z+1}, N-1={N-1})")

    gs_par = find_gs(Z, N)
    if verbose:
        print(f"  Parent GS: {gs_par}")

    # Step 2: Build parent Garside NF
    if verbose:
        print(f"  Building parent Garside ({A*(A-1)//2} crossings)...")
    N_par = build_garside_nf(gs_par)
    L1_par = l1_norm(N_par)
    if verbose:
        print(f"  Parent: {len(N_par)} NF terms, L1 = {L1_par:.4f}")

    # Step 3: Find all neutron positions
    neutron_pos = [i for i in range(A) if gs_par[i] == 0]
    N_neutrons = len(neutron_pos)

    # Step 4: For each neutron, build daughter Garside NF
    dL1s = []
    daughter_nfs = []

    for k_idx, pos in enumerate(neutron_pos):
        dau_ord = gs_par[:]
        dau_ord[pos] = 1
        if verbose:
            print(f"  Daughter k={k_idx} (pos {pos}): {dau_ord}...")
        N_dau = build_garside_nf(dau_ord)
        L1_dau = l1_norm(N_dau)
        dL1 = L1_par - L1_dau
        dL1s.append(dL1)
        daughter_nfs.append(N_dau)
        if verbose:
            print(f"    {len(N_dau)} terms, L1={L1_dau:.4f}, ΔL1={dL1:+.4f}")

    # Step 5: Compute Gram weights from Frobenius norms
    # Collect all NF words from parent + daughters
    all_words_set = set(N_par.keys())
    for nf in daughter_nfs:
        all_words_set.update(nf.keys())
    all_words = sorted(all_words_set, key=lambda w: (len(w), w))
    dim = len(all_words)

    if verbose:
        print(f"  Gram subspace: {dim} basis words")

    # Build Gram matrix
    if verbose:
        print(f"  Computing {dim}×{dim} Gram matrix...")
    G = np.zeros((dim, dim))
    for i in range(dim):
        for j in range(i, dim):
            prod = hecke_mul({all_words[i]: 1.0}, {all_words[j]: 1.0})
            prod = reduce_nf(prod)
            val = markov_trace_elt(prod, n_strands)
            G[i, j] = val
            G[j, i] = val

    # Compute δ_k vectors and Frobenius norms
    vec_par = np.array([N_par.get(w, 0.0) for w in all_words])
    frob_norms = []

    for k_idx in range(N_neutrons):
        vec_dau = np.array([daughter_nfs[k_idx].get(w, 0.0) for w in all_words])
        delta = vec_par - vec_dau
        frob2 = delta @ G @ delta
        frob = math.sqrt(abs(frob2))
        frob_norms.append(frob)

    # Normalize weights
    total_frob = sum(frob_norms)
    if total_frob > 1e-15:
        weights = [f / total_frob for f in frob_norms]
    else:
        weights = [1.0 / N_neutrons] * N_neutrons

    # Step 6: Q = (Σ w_k × ΔL1_k) × N × m_e
    weighted_avg = sum(w * dl for w, dl in zip(weights, dL1s))
    Q_gram = weighted_avg * N_neutrons * M_E_MEV

    # Also compute uniform for comparison
    Q_uniform = sum(dL1s) * M_E_MEV

    # Also compute q^{-k(N-1-k)} weight
    qweights = [qi ** (k * (N_neutrons - 1 - k)) for k in range(N_neutrons)]
    Q_parabolic = sum(w * dl for w, dl in zip(qweights, dL1s)) * M_E_MEV

    err_gram = (Q_gram / Q_exp - 1) * 100 if Q_exp > 0 else float('nan')
    err_uniform = (Q_uniform / Q_exp - 1) * 100 if Q_exp > 0 else float('nan')
    err_parab = (Q_parabolic / Q_exp - 1) * 100 if Q_exp > 0 else float('nan')

    if verbose:
        print(f"\n  Gram weights: [{', '.join(f'{w:.4f}' for w in weights)}]")
        print(f"  q-parabolic:  [{', '.join(f'{w:.4f}' for w in qweights)}]")
        print(f"  ΔL1:          [{', '.join(f'{dl:.4f}' for dl in dL1s)}]")
        print(f"\n  Q_gram      = {Q_gram:.4f} MeV  ({err_gram:+.1f}%)")
        print(f"  Q_uniform   = {Q_uniform:.4f} MeV  ({err_uniform:+.1f}%)")
        print(f"  Q_parabolic = {Q_parabolic:.4f} MeV  ({err_parab:+.1f}%)")
        print(f"  Q_exp       = {Q_exp:.4f} MeV")

    return {
        'name': name, 'Z': Z, 'N': N, 'A': A,
        'Q_gram': Q_gram, 'Q_uniform': Q_uniform, 'Q_parabolic': Q_parabolic,
        'Q_exp': Q_exp,
        'err_gram': err_gram, 'err_uniform': err_uniform, 'err_parab': err_parab,
        'weights': weights, 'dL1s': dL1s, 'L1_par': L1_par,
        'n_terms_par': len(N_par), 'dim_gram': dim,
    }


# ══════════════════════════════════════════════════════════════
#  RUN BENCHMARKS
# ══════════════════════════════════════════════════════════════

if __name__ == '__main__':
    print(f"Q-VALUE FROM FULL GARSIDE NF + GRAM WEIGHTS")
    print(f"q = {q:.10f}, m_e = {M_E_MEV:.6f} MeV")
    print(f"Formula: Q = (Σ w_k^G × ΔL1_k) × N × m_e")
    print(f"Starting from typed Garside NF (all C(A,2) crossings)")

    decays = [
        (1, 2, Q_TRITIUM_MEV, '3H→3He'),
        (2, 4, 3.508, '6He→6Li'),
    ]

    # Only do A ≤ 6 for now (Garside + Gram is expensive)
    results = []
    for Z, N, Q_exp, name in decays:
        r = compute_Q_garside_gram(Z, N, Q_exp, name)
        results.append(r)

    # Summary
    print(f"\n{'=' * 70}")
    print(f"  SUMMARY")
    print(f"{'=' * 70}")
    print(f"  {'Decay':>12s} | {'NF terms':>8s} | {'Q_gram':>8s} | {'Q_unif':>8s} | {'Q_parab':>8s} | {'Q_exp':>8s} | {'err_G':>7s}")
    print(f"  {'-' * 75}")
    for r in results:
        print(f"  {r['name']:>12s} | {r['n_terms_par']:>8d} | {r['Q_gram']:>8.4f} | {r['Q_uniform']:>8.4f} | {r['Q_parabolic']:>8.4f} | {r['Q_exp']:>8.4f} | {r['err_gram']:>+6.1f}%")

    # Witness
    witness = {
        'name': 'qvalue-garside-gram',
        'timestamp': datetime.now(timezone.utc).isoformat(),
        'q': q, 'm_e': M_E_MEV,
        'formula': 'Q = (sum w_k^G * dL1_k) * N * m_e',
        'results': [{k: v for k, v in r.items() if not isinstance(v, np.ndarray)} for r in results],
    }
    out = Path(__file__).with_suffix('.witness.json')
    out.write_text(json.dumps(witness, indent=2, default=float))
    print(f"\n  Witness: {out.name}")
