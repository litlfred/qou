#!/usr/bin/env python3
"""
Mass from Gröbner-Shirshov REDUCTION COST.

The NF is a destination. The mass is in the JOURNEY — how much
algebraic work the Hecke algebra does to reduce the braid word.

Three GS reduction rules, each with a physical interpretation:

  HECKE:  σᵢ² → HA·σᵢ + 1
    Cost: the squared crossing splits into (q-q⁻¹)×crossing + identity.
    This is the fundamental mass-generation step: a self-interaction
    (σ²) creates a q-weighted contribution (HA = q-q⁻¹) plus vacuum.
    Each Hecke reduction deposits HA of energy.

  YANG-BAXTER:  σᵢσⱼσᵢ → σⱼσᵢσⱼ  (|i-j|=1)
    Cost: zero coefficient change, but reorders the crossing pattern.
    This is a topological rearrangement — no energy deposited, but
    the braid isotopy class is preserved. Physically: gauge invariance.

  FAR-COMMUTATIVITY:  σᵢσⱼ → σⱼσᵢ  (|i-j|≥2)
    Cost: zero. Distant crossings commute. This is locality —
    crossings far apart don't interact.

The MASS FUNCTIONAL should count the total HA deposited by
Hecke reductions:

  𝔪_GS(𝒜) = Σ (HA × |coefficient|) over all Hecke reduction steps

This is the TOTAL q-ENERGY deposited during reduction: each σᵢ²
that fires creates HA of mass. The more self-interactions the
braid word has, the more mass.

We also track:
  - N_hecke:  number of Hecke reduction steps
  - N_yb:    number of Yang-Baxter rearrangements
  - N_fc:    number of far-commutativity swaps
  - E_hecke: total |coefficient × HA| deposited by Hecke steps
  - Word length of unreduced braid vs NF

Usage:
    python3 folio-assistant/computations/atom_mass_gs_cost.py
"""

import math
import sys
import time
from pathlib import Path
from dataclasses import dataclass, asdict

sys.path.insert(0, str(Path(__file__).parent))

from q_parameter import Q as q0, HA as HA_val
from experimental_constants import M_P_MEV, M_N_MEV, M_E_MEV
from witness_base import WitnessBuilder


# ══════════════════════════════════════════════════════════════
# §1  INSTRUMENTED GS REDUCTION
# ══════════════════════════════════════════════════════════════

HA = HA_val
z = 1.0 / (q0**0.5 + q0**(-0.5))


@dataclass
class GSStats:
    n_hecke: int = 0        # number of Hecke reductions
    n_yb: int = 0           # number of Yang-Baxter rearrangements
    n_fc: int = 0           # number of far-commutativity swaps
    e_hecke: float = 0.0    # total |coeff × HA| deposited by Hecke
    e_hecke_signed: float = 0.0  # signed sum of coeff × HA
    initial_word_count: int = 0
    final_term_count: int = 0


def reduce_nf_instrumented(terms):
    """GS reduction with full cost tracking."""
    stats = GSStats()
    stats.initial_word_count = len(terms)

    changed = True
    while changed:
        changed = False
        new_terms = {}
        for word, coeff in terms.items():
            if abs(coeff) < 1e-15:
                continue
            done = False

            # HECKE: σᵢ² → HA·σᵢ + 1
            for pos in range(len(word) - 1):
                if word[pos] == word[pos + 1]:
                    i = word[pos]
                    pre, suf = word[:pos], word[pos + 2:]
                    ha_deposit = coeff * HA
                    new_terms[pre + (i,) + suf] = new_terms.get(pre + (i,) + suf, 0.0) + ha_deposit
                    new_terms[pre + suf] = new_terms.get(pre + suf, 0.0) + coeff
                    stats.n_hecke += 1
                    stats.e_hecke += abs(ha_deposit)
                    stats.e_hecke_signed += ha_deposit
                    done = changed = True
                    break

            if done:
                continue

            # YANG-BAXTER: σᵢσⱼσᵢ → σⱼσᵢσⱼ (|i-j|=1)
            for pos in range(len(word) - 2):
                a, b, c = word[pos], word[pos + 1], word[pos + 2]
                if a == c and abs(a - b) == 1:
                    new_trip = (b, a, b)
                    if new_trip < (a, b, a):
                        nw = word[:pos] + new_trip + word[pos + 3:]
                        new_terms[nw] = new_terms.get(nw, 0.0) + coeff
                        stats.n_yb += 1
                        done = changed = True
                        break

            if done:
                continue

            # FAR-COMMUTATIVITY: σᵢσⱼ → σⱼσᵢ (|i-j|≥2)
            for pos in range(len(word) - 1):
                a, b = word[pos], word[pos + 1]
                if abs(a - b) >= 2 and a > b:
                    nw = word[:pos] + (b, a) + word[pos + 2:]
                    new_terms[nw] = new_terms.get(nw, 0.0) + coeff
                    stats.n_fc += 1
                    done = changed = True
                    break

            if not done:
                new_terms[word] = new_terms.get(word, 0.0) + coeff

        terms = {w: c for w, c in new_terms.items() if abs(c) > 1e-15}

    stats.final_term_count = len(terms)
    return terms, stats


# ══════════════════════════════════════════════════════════════
# §2  HECKE ENGINE WITH COST TRACKING
# ══════════════════════════════════════════════════════════════

def hecke_mul(t1, t2):
    result = {}
    for w1, c1 in t1.items():
        for w2, c2 in t2.items():
            w = w1 + w2
            result[w] = result.get(w, 0.0) + c1 * c2
    return {w: c for w, c in result.items() if abs(c) > 1e-15}


def expand_inverse(word):
    terms = {(): 1.0}
    for g in word:
        new_terms = {}
        if g >= 0:
            for w, c in terms.items():
                nw = w + (g,)
                new_terms[nw] = new_terms.get(nw, 0.0) + c
        else:
            i = -g - 1
            for w, c in terms.items():
                nw = w + (i,)
                new_terms[nw] = new_terms.get(nw, 0.0) + c
                new_terms[w] = new_terms.get(w, 0.0) - c * HA
        terms = {w: c for w, c in new_terms.items() if abs(c) > 1e-15}
    return terms


def quark_crossing(type_i, type_j, gen):
    if type_i == type_j == 'u':
        return {(gen,): 1.0}
    elif type_i == type_j == 'd':
        return {(gen,): 1.0, (): -HA}
    else:
        return {(gen,): 1.0, (): -HA / 2}


def nuclear_crossing(type_i, type_j, gen):
    if type_i == type_j == 'p':
        return {(gen,): 1.0}
    elif type_i == type_j == 'n':
        return {(gen,): 1.0, (): -HA}
    else:
        return {(gen,): 1.0, (): -HA / 2}


def L1(terms):
    return sum(abs(c) for c in terms.values())


def net(terms):
    return sum(terms.values())


# ══════════════════════════════════════════════════════════════
# §3  BUILD ATOMS WITH CUMULATIVE GS STATS
# ══════════════════════════════════════════════════════════════

def build_atom_with_stats(Z, N):
    """Build atom tracking GS reduction cost at every step."""
    A = Z + N
    types = ['p'] * Z + ['n'] * N

    # Build B₃
    b3_raw = expand_inverse((0, -2, 0, -2, 0, -2))
    b3_nf, b3_stats = reduce_nf_instrumented(b3_raw)

    # Build nucleons
    total_stats = GSStats()

    def accumulate(s):
        total_stats.n_hecke += s.n_hecke
        total_stats.n_yb += s.n_yb
        total_stats.n_fc += s.n_fc
        total_stats.e_hecke += s.e_hecke
        total_stats.e_hecke_signed += s.e_hecke_signed

    def build_nucleon(quark_types):
        elem = dict(b3_nf)
        accumulate(b3_stats)
        for i in range(3):
            for j in range(i + 1, 3):
                gen = min(i, j)
                if gen > 1:
                    gen = 1
                cx = quark_crossing(quark_types[i], quark_types[j], gen)
                unreduced = hecke_mul(elem, cx)
                elem, s = reduce_nf_instrumented(unreduced)
                accumulate(s)
        return elem

    proton_nf = build_nucleon(['u', 'u', 'd'])
    neutron_nf = build_nucleon(['u', 'd', 'd'])

    nfs = [dict(proton_nf) if t == 'p' else dict(neutron_nf) for t in types]

    if A == 0:
        return {(): 1.0}, total_stats

    # Nuclear assembly — inductive with stats
    elem = dict(nfs[0])
    # Count nucleon construction cost for nucleons 2..A
    for k in range(1, A):
        # Rebuild nucleon (with stats)
        if types[k] == 'p':
            build_nucleon(['u', 'u', 'd'])
        else:
            build_nucleon(['u', 'd', 'd'])

        gen = min(k - 1, max(A - 2, 0))
        cx = nuclear_crossing(types[k - 1], types[k], gen)
        temp = hecke_mul(elem, cx)
        temp = hecke_mul(temp, nfs[k])
        elem, s = reduce_nf_instrumented(temp)
        accumulate(s)

    # Electrons
    electron = {(0, 1, 0): 1.0}
    for e_idx in range(Z):
        gen = e_idx % max(A - 1, 1)
        hopf = {(gen,): 1.0}
        temp = hecke_mul(elem, hopf)
        temp = hecke_mul(temp, electron)
        elem, s = reduce_nf_instrumented(temp)
        accumulate(s)

    total_stats.final_term_count = len(elem)
    return elem, total_stats


# ══════════════════════════════════════════════════════════════
# §4  MAIN
# ══════════════════════════════════════════════════════════════

ELEMENTS = {
    1:  ("H",   1, 0),
    2:  ("He",  2, 2),
    3:  ("Li",  3, 4),
    4:  ("Be",  4, 5),
    5:  ("B",   5, 6),
    6:  ("C",   6, 6),
    7:  ("N",   7, 7),
    8:  ("O",   8, 8),
}

AME2020_MASS = {
    (1, 0): 938.783,     (2, 2): 3728.401,   (3, 4): 6535.367,
    (4, 5): 8394.794,    (5, 6): 10255.103,  (6, 6): 11177.930,
    (7, 7): 13043.781,   (8, 8): 14899.169,
}


def main():
    print("=" * 130)
    print("MASS FROM GRÖBNER-SHIRSHOV REDUCTION COST")
    print(f"q₀ = {q0:.10f}   HA = {HA:.10f}   z = {z:.10f}")
    print("=" * 130)
    print()
    print("Three reduction rules, each with physical meaning:")
    print("  HECKE  σᵢ² → HA·σᵢ + 1    — self-interaction deposits HA of energy")
    print("  YB     σᵢσⱼσᵢ → σⱼσᵢσⱼ    — topological rearrangement (zero cost)")
    print("  FC     σᵢσⱼ → σⱼσᵢ (|i-j|≥2) — locality (zero cost)")
    print()
    print("Mass candidates from GS stats:")
    print("  E_hecke:  total |coeff × HA| deposited by Hecke reductions")
    print("  N_hecke:  count of Hecke reduction steps")
    print("  L¹:       sum of |coeff| in final NF")
    print()

    rows = []
    for Z_elem in sorted(ELEMENTS.keys()):
        name, Z, N = ELEMENTS[Z_elem]
        A = Z + N
        M_obs = AME2020_MASS.get((Z, N), 0.0)

        t0 = time.time()
        atom_nf, stats = build_atom_with_stats(Z, N)
        elapsed = time.time() - t0

        l1 = L1(atom_nf)
        nt = net(atom_nf)

        row = {
            'name': name, 'Z': Z, 'N': N, 'A': A,
            'n_hecke': stats.n_hecke,
            'n_yb': stats.n_yb,
            'n_fc': stats.n_fc,
            'e_hecke': stats.e_hecke,
            'e_hecke_signed': stats.e_hecke_signed,
            'L1': l1,
            'net': nt,
            'terms': stats.final_term_count,
            'M_obs': M_obs,
            'elapsed': elapsed,
        }
        rows.append(row)

        print(f"{'─' * 130}")
        print(f"  {name} (Z={Z}, N={N}, A={A}): {elapsed:.1f}s")
        print(f"    GS steps: Hecke={stats.n_hecke:,d}  YB={stats.n_yb:,d}  FC={stats.n_fc:,d}  total={stats.n_hecke+stats.n_yb+stats.n_fc:,d}")
        print(f"    E_hecke (Σ|c·HA|) = {stats.e_hecke:.4f}")
        print(f"    E_hecke_signed    = {stats.e_hecke_signed:+.4f}")
        print(f"    L¹ = {l1:.4f}   net = {nt:+.4f}   NF terms = {stats.final_term_count}")
        print(f"    M_obs = {M_obs:.1f} MeV")

    # Summary: scaling check
    print()
    print("=" * 130)
    print("SCALING: F(atom)/F(H) vs M(atom)/m_p")
    print("=" * 130)

    h = rows[0]
    print()
    print(f"{'Atom':>4} | {'A':>3} | {'M/m_p':>8} | {'E_hk/E_hk_H':>12} | {'N_hk/N_hk_H':>12} | "
          f"{'L¹/L¹_H':>10} | {'E_hk^⅔/E_H^⅔':>14} | {'N_hk^⅔/N_H^⅔':>14}")
    print("─" * 130)

    for r in rows:
        m_ratio = r['M_obs'] / M_P_MEV
        e_ratio = r['e_hecke'] / h['e_hecke'] if h['e_hecke'] > 0 else 0
        n_ratio = r['n_hecke'] / h['n_hecke'] if h['n_hecke'] > 0 else 0
        l1_ratio = r['L1'] / h['L1'] if h['L1'] > 0 else 0
        e23_ratio = (r['e_hecke']**(2/3)) / (h['e_hecke']**(2/3)) if h['e_hecke'] > 0 else 0
        n23_ratio = (r['n_hecke']**(2/3)) / (h['n_hecke']**(2/3)) if h['n_hecke'] > 0 else 0

        print(f"{r['name']:>4} | {r['A']:3d} | {m_ratio:8.3f} | {e_ratio:12.4f} | {n_ratio:12.4f} | "
              f"{l1_ratio:10.4f} | {e23_ratio:14.4f} | {n23_ratio:14.4f}")

    # Best fit
    print()
    print("=" * 130)
    print("BEST FIT: mean |log(F_ratio / M_ratio)|")
    print("=" * 130)

    functionals = {
        'E_hecke':      lambda r: r['e_hecke'],
        'N_hecke':      lambda r: float(r['n_hecke']),
        'L¹':           lambda r: r['L1'],
        'E_hecke^(2/3)':lambda r: r['e_hecke']**(2/3) if r['e_hecke'] > 0 else 0,
        'N_hecke^(2/3)':lambda r: float(r['n_hecke'])**(2/3) if r['n_hecke'] > 0 else 0,
        'E_hecke^(1/2)':lambda r: r['e_hecke']**0.5 if r['e_hecke'] > 0 else 0,
        'N_hecke^(1/2)':lambda r: float(r['n_hecke'])**0.5 if r['n_hecke'] > 0 else 0,
        'log(E_hecke)': lambda r: math.log(r['e_hecke']) if r['e_hecke'] > 0 else 0,
        'log(N_hecke)': lambda r: math.log(float(r['n_hecke'])) if r['n_hecke'] > 0 else 0,
    }

    for fname, fn in functionals.items():
        h_val = fn(h)
        if h_val <= 0:
            print(f"  {fname:>18}: (skipped, H value = 0)")
            continue
        errors = []
        for r in rows:
            if r['M_obs'] <= 0:
                continue
            f_val = fn(r)
            m_ratio = r['M_obs'] / M_P_MEV
            f_ratio = f_val / h_val if h_val > 0 else 0
            if f_ratio > 0 and m_ratio > 0:
                errors.append(abs(math.log(f_ratio / m_ratio)))
        mean_err = sum(errors) / len(errors) if errors else float('inf')
        print(f"  {fname:>18}: mean |log(F/M)| = {mean_err:.4f}")

    # Witness
    w = WitnessBuilder("atom-mass-gs-cost", engine="python")
    w.set_description(
        "Mass from GS reduction cost: E_hecke = total |coeff×HA| deposited "
        "by Hecke reductions during atom construction. Tracks N_hecke, N_yb, N_fc."
    )
    w.add_parameter("q0", str(q0))
    w.add_parameter("HA", str(HA))
    w.add_data("results", rows)
    w.save()


if __name__ == "__main__":
    main()
