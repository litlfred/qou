#!/usr/bin/env python3
"""
Volume from FROBENIUS PAIRING between crossings.

The Frobenius pairing ⟨a, b⟩_F = ∫_A μ(a ⊗ b) = tr_M(a · b)
mediates between the horizontal (crossing) and vertical (mass)
directions in the Hecke algebra.

For a nucleus with crossings {C₁, ..., C_k} where each Cⱼ is
a typed Hecke element (c·σ + d), the Frobenius volume is:

  Vol_F = Σ_{i≤j} ⟨Cᵢ, Cⱼ⟩_F = Σ_{i≤j} tr_M(Cᵢ · Cⱼ)

This is the quadratic form of the Gram matrix on the crossing
elements — NOT on the final NF, but on the individual crossings
themselves.

Each crossing Cⱼ = cⱼσ_g + dⱼ acts at generator g with:
  pp: (c=1, d=0)         → σ_g
  nn: (c=1, d=-HA)       → σ_g - HA
  pn: (c=1, d=-HA/2)     → σ_g - HA/2

The Frobenius pairing captures SHARED VOLUME between crossings:
two crossings at the same generator interact strongly, while
crossings at distant generators are nearly orthogonal.

Usage:
    python3 folio-assistant/computations/atom_frobenius_volume.py
"""

import math
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from q_parameter import Q as q0, HBAR_Q_SQ
from experimental_constants import M_P_MEV
from witness_base import WitnessBuilder

import snappy

HA = q0 - 1.0 / q0
z = 1.0 / (q0**0.5 + q0**(-0.5))
hbar_q_sq = HBAR_Q_SQ

# H₃ NF basis and Markov traces
NF_BASIS = [(), (0,), (1,), (0, 1), (1, 0), (0, 1, 0)]
TR_M = [1.0, z, z, z**2, z**2, z**3]


def hecke_mul(t1, t2):
    result = {}
    for w1, c1 in t1.items():
        for w2, c2 in t2.items():
            w = w1 + w2
            result[w] = result.get(w, 0.0) + c1 * c2
    return {w: c for w, c in result.items() if abs(c) > 1e-15}


def reduce_nf(terms):
    changed = True
    while changed:
        changed = False
        new_terms = {}
        for word, coeff in terms.items():
            if abs(coeff) < 1e-15:
                continue
            done = False
            for pos in range(len(word) - 1):
                if word[pos] == word[pos + 1]:
                    i = word[pos]
                    pre, suf = word[:pos], word[pos + 2:]
                    new_terms[pre + (i,) + suf] = new_terms.get(pre + (i,) + suf, 0.0) + coeff * HA
                    new_terms[pre + suf] = new_terms.get(pre + suf, 0.0) + coeff
                    done = changed = True
                    break
            if done:
                continue
            for pos in range(len(word) - 2):
                a, b, c = word[pos], word[pos + 1], word[pos + 2]
                if a == c and abs(a - b) == 1:
                    new_trip = (b, a, b)
                    if new_trip < (a, b, a):
                        nw = word[:pos] + new_trip + word[pos + 3:]
                        new_terms[nw] = new_terms.get(nw, 0.0) + coeff
                        done = changed = True
                        break
            if done:
                continue
            for pos in range(len(word) - 1):
                a, b = word[pos], word[pos + 1]
                if abs(a - b) >= 2 and a > b:
                    nw = word[:pos] + (b, a) + word[pos + 2:]
                    new_terms[nw] = new_terms.get(nw, 0.0) + coeff
                    done = changed = True
                    break
            if not done:
                new_terms[word] = new_terms.get(word, 0.0) + coeff
        terms = {w: c for w, c in new_terms.items() if abs(c) > 1e-15}
    return terms


def markov_trace(terms):
    """Markov trace: tr_M(x) = Σ c_w × z^{ℓ(w)} for reduced words."""
    total = 0.0
    for word, coeff in terms.items():
        if word in NF_BASIS:
            idx = NF_BASIS.index(word)
            total += coeff * TR_M[idx]
        else:
            total += coeff * z ** len(word)
    return total


def frobenius_pairing(a_terms, b_terms):
    """⟨a, b⟩_F = tr_M(a · b)."""
    product = hecke_mul(a_terms, b_terms)
    product_nf = reduce_nf(product)
    return markov_trace(product_nf)


# ══════════════════════════════════════════════════════════════
# §1  CROSSING ELEMENTS
# ══════════════════════════════════════════════════════════════

def crossing_element(type_i, type_j, gen):
    """Typed crossing as Hecke element on generator gen (0-indexed)."""
    if type_i == 'p' and type_j == 'p':
        return {(gen,): 1.0}
    elif type_i == 'n' and type_j == 'n':
        return {(gen,): 1.0, (): -HA}
    else:
        return {(gen,): 1.0, (): -HA / 2}


def self_pairing(type_i, type_j, gen):
    """⟨C, C⟩_F = tr_M(C²) for a single crossing."""
    C = crossing_element(type_i, type_j, gen)
    return frobenius_pairing(C, C)


# ══════════════════════════════════════════════════════════════
# §2  FROBENIUS VOLUME COMPUTATION
# ══════════════════════════════════════════════════════════════

def compute_frobenius_volume(Z, N):
    """Compute Vol_F = Σ_{i≤j} ⟨Cᵢ, Cⱼ⟩_F over all crossing pairs.

    Returns (vol_F, vol_self, vol_cross, details).
    """
    A = Z + N
    types = ['p'] * Z + ['n'] * N

    # Build list of all crossings: (type_i, type_j, generator)
    crossings = []
    for i in range(A):
        for j in range(i + 1, A):
            gen = min(i, j) % max(A - 1, 1)  # wrap generator index
            crossings.append((types[i], types[j], gen))

    n_cross = len(crossings)

    # Build crossing elements
    c_elems = [crossing_element(ti, tj, g) for ti, tj, g in crossings]

    # Compute full Frobenius volume: Gram quadratic form on crossings
    vol_self = 0.0    # diagonal: ⟨Cᵢ, Cᵢ⟩_F
    vol_cross = 0.0   # off-diagonal: ⟨Cᵢ, Cⱼ⟩_F (i≠j)

    for i in range(n_cross):
        # Self-pairing
        fp_ii = frobenius_pairing(c_elems[i], c_elems[i])
        vol_self += fp_ii

        # Cross-pairings
        for j in range(i + 1, n_cross):
            fp_ij = frobenius_pairing(c_elems[i], c_elems[j])
            vol_cross += fp_ij

    vol_F = vol_self + 2 * vol_cross  # full quadratic form
    vol_abs = abs(vol_self) + 2 * sum(
        abs(frobenius_pairing(c_elems[i], c_elems[j]))
        for i in range(n_cross) for j in range(i + 1, n_cross)
    )

    return vol_F, vol_self, vol_cross, vol_abs, n_cross


# ══════════════════════════════════════════════════════════════
# §3  SNAPPY VOLUME FOR COMPARISON
# ══════════════════════════════════════════════════════════════

def nuclear_braid_word(Z, N):
    """Build braid word for nuclear link (1-indexed for SnapPy)."""
    A = Z + N
    types = ['p'] * Z + ['n'] * N
    word = []
    for i in range(A):
        for j in range(i + 1, A):
            gen = min(i, j) + 1
            if gen > max(A - 1, 1):
                gen = max(A - 1, 1)
            if types[i] == 'p' and types[j] == 'p':
                word.append(gen)
            elif types[i] == 'n' and types[j] == 'n':
                word.append(-gen)
            else:
                word.append(gen)
    # Electrons
    for e in range(Z):
        gen = (e % max(A - 1, 1)) + 1
        word.append(gen)
        if gen < max(A - 1, 1):
            word.extend([gen, gen + 1, gen])
    return word


def snappy_volume(Z, N):
    """Compute Vol via SnapPy."""
    A = Z + N
    if A <= 1:
        return 0.0
    # Include neutron internal volume
    vol_n = 13.948418
    word = nuclear_braid_word(Z, N)
    try:
        L = snappy.Link(braid_closure=word)
        M = L.exterior()
        vol_nuc = float(M.volume())
    except:
        vol_nuc = float('nan')
    return N * vol_n + vol_nuc


# ══════════════════════════════════════════════════════════════
# §4  MAIN
# ══════════════════════════════════════════════════════════════

ELEMENTS = {
    1:  ("H",   1, 0,  938.783),
    2:  ("He",  2, 2,  3728.401),
    3:  ("Li",  3, 4,  6535.367),
    4:  ("Be",  4, 5,  8394.794),
    5:  ("B",   5, 6,  10255.103),
    6:  ("C",   6, 6,  11177.930),
    7:  ("N",   7, 7,  13043.781),
    8:  ("O",   8, 8,  14899.169),
}


def main():
    print("=" * 130)
    print("FROBENIUS PAIRING VOLUME: Vol_F = Σ_{i≤j} ⟨Cᵢ, Cⱼ⟩_F")
    print(f"q₀ = {q0:.10f}   HA = {HA:.10f}   z = {z:.10f}")
    print("=" * 130)
    print()

    # First: show the Frobenius self-pairings for each crossing type
    print("CROSSING SELF-PAIRINGS ⟨C, C⟩_F = tr_M(C²):")
    for t1, t2, label in [('p', 'p', 'pp'), ('n', 'n', 'nn'), ('p', 'n', 'pn')]:
        fp = self_pairing(t1, t2, 0)
        C = crossing_element(t1, t2, 0)
        print(f"  ⟨{label}, {label}⟩_F = {fp:.6f}   (C = {dict(C)})")

    # Cross-pairings between different crossing types
    print()
    print("CROSSING CROSS-PAIRINGS ⟨Cᵢ, Cⱼ⟩_F:")
    for (t1a, t1b, l1), (t2a, t2b, l2) in [
        (('p','p','pp'), ('n','n','nn')),
        (('p','p','pp'), ('p','n','pn')),
        (('n','n','nn'), ('p','n','pn')),
    ]:
        # Same generator
        fp_same = frobenius_pairing(
            crossing_element(t1a, t1b, 0),
            crossing_element(t2a, t2b, 0))
        # Different generators
        fp_diff = frobenius_pairing(
            crossing_element(t1a, t1b, 0),
            crossing_element(t2a, t2b, 1))
        print(f"  ⟨{l1}, {l2}⟩_F  same gen: {fp_same:.6f}  diff gen: {fp_diff:.6f}")

    print()
    print("=" * 130)
    print("ATOM-BY-ATOM: Frobenius volume vs SnapPy volume vs mass")
    print("=" * 130)
    print()

    rows = []
    print(f"{'Atom':>4} | {'A':>3} | {'n_cross':>7} | {'Vol_F':>10} | {'|Vol_F|':>10} | "
          f"{'Vol_snap':>10} | {'M_obs':>10} | {'Vol_F/M':>8} | {'|V_F|/M':>8} | {'V_sn/M':>8} | {'t':>5}")
    print("─" * 130)

    for Z_elem in sorted(ELEMENTS.keys()):
        name, Z, N, M_obs = ELEMENTS[Z_elem]
        A = Z + N
        t0 = time.time()

        if A <= 1:
            vol_F, vol_self, vol_cross, vol_abs, n_cross = 0.0, 0.0, 0.0, 0.0, 0
        else:
            vol_F, vol_self, vol_cross, vol_abs, n_cross = compute_frobenius_volume(Z, N)

        vol_snap = snappy_volume(Z, N)
        elapsed = time.time() - t0

        vfm = vol_F / M_obs * 1000 if M_obs > 0 else 0
        vam = vol_abs / M_obs * 1000 if M_obs > 0 else 0
        vsm = vol_snap / M_obs * 1000 if M_obs > 0 and not math.isnan(vol_snap) else 0

        row = {
            'name': name, 'Z': Z, 'N': N, 'A': A,
            'n_cross': n_cross,
            'vol_F': vol_F, 'vol_abs': vol_abs,
            'vol_self': vol_self, 'vol_cross': vol_cross,
            'vol_snap': vol_snap, 'M_obs': M_obs,
        }
        rows.append(row)

        print(f"{name:>4} | {A:3d} | {n_cross:7d} | {vol_F:+10.4f} | {vol_abs:10.4f} | "
              f"{vol_snap:10.3f} | {M_obs:10.1f} | {vfm:+8.3f} | {vam:8.3f} | {vsm:8.3f} | {elapsed:5.1f}s")

    # Scaling analysis
    print()
    print("=" * 130)
    print("SCALING: Which Frobenius quantity tracks Vol(SnapPy)?")
    print("=" * 130)
    print()
    print(f"{'Atom':>4} | {'Vol_snap':>10} | {'Vol_F':>10} | {'|Vol_F|':>10} | {'Vol_self':>10} | "
          f"{'2×Vol_cross':>11} | {'V_sn/|V_F|':>11} | {'V_F_self/Vsn':>12}")
    print("─" * 130)
    for r in rows:
        if r['A'] <= 1:
            continue
        ratio1 = r['vol_snap'] / r['vol_abs'] if r['vol_abs'] > 0.01 else 0
        ratio2 = r['vol_self'] / r['vol_snap'] if r['vol_snap'] > 0.01 else 0
        print(f"{r['name']:>4} | {r['vol_snap']:10.3f} | {r['vol_F']:+10.4f} | {r['vol_abs']:10.4f} | "
              f"{r['vol_self']:10.4f} | {2*r['vol_cross']:+11.4f} | {ratio1:11.4f} | {ratio2:12.4f}")

    # Witness
    w = WitnessBuilder("atom-frobenius-volume", engine="snappy")
    w.set_description(
        "Frobenius pairing volume Vol_F = Σ⟨Cᵢ,Cⱼ⟩_F vs SnapPy hyperbolic volume. "
        "Tests whether the Gram quadratic form on crossing elements gives volume."
    )
    w.add_parameter("q0", str(q0))
    w.add_parameter("HA", str(HA))
    w.add_data("results", rows)
    w.save()


if __name__ == "__main__":
    main()
