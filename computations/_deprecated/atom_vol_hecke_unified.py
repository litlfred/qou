#!/usr/bin/env python3
"""
UNIFIED: Hyperbolic volume + GS reduction cost + crossing structure.

The chain we're tracing:

  Hecke algebra H_A(q)
    → typed crossings (c,d) per nucleon pair
    → braid word (sequence of σ_i^±1)
    → GS reduction (Hecke firings deposit HA each)
    → braid closure → hyperbolic 3-manifold
    → Vol(closure) → mass via 𝔪 = Vol/ℏ_q²

We compute ALL of these for each atom and look for the functional
relationship:  Vol = f(crossing data, HA, q)

Key quantities per atom:
  n_cross:  total crossing count = C(A,2) nucleon pairs + Z electrons
  n_pp:     proton-proton crossings (eigenvalue q)
  n_nn:     neutron-neutron crossings (eigenvalue -q⁻¹)
  n_pn:     mixed crossings (eigenvalue (q-q⁻¹)/2)
  n_pos:    positive generators in braid word
  n_neg:    negative generators (inverses)
  writhe:   n_pos - n_neg (signed crossing count)
  E_hecke:  total HA deposited during GS reduction
  Vol:      hyperbolic volume of braid closure (SnapPy)
  M_obs:    observed mass (AME2020)

Usage:
    python3 folio-assistant/computations/atom_vol_hecke_unified.py
"""

import math
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from q_parameter import Q as q0, HBAR_Q, HBAR_Q_SQ
from experimental_constants import M_P_MEV, M_N_MEV, M_E_MEV
from witness_base import WitnessBuilder

import snappy

HA = q0 - 1.0 / q0
z = 1.0 / (q0**0.5 + q0**(-0.5))
hbar_q_sq = HBAR_Q_SQ


# ══════════════════════════════════════════════════════════════
# §1  BRAID CONSTRUCTION WITH FULL CROSSING ACCOUNTING
# ══════════════════════════════════════════════════════════════

def b3_word():
    """B₃ = (σ₁σ₂⁻¹)³ (1-indexed for SnapPy)."""
    return [1, -2, 1, -2, 1, -2]


def build_nuclear_braid(Z, N):
    """Build the nuclear braid word with full crossing accounting.

    Returns: (word, stats) where stats has all crossing data.
    """
    A = Z + N
    types = ['p'] * Z + ['n'] * N

    word = []
    n_pp = 0
    n_nn = 0
    n_pn = 0
    n_pos = 0
    n_neg = 0

    # Nucleon internal braids: B₃ + quark crossings for each nucleon
    # (these are on 3 internal strands, contributing to internal volume)
    nucleon_words = []
    for k in range(A):
        # B₃ confinement
        nw = list(b3_word())
        # Quark crossings
        if types[k] == 'p':  # uud
            quarks = ['u', 'u', 'd']
        else:  # udd
            quarks = ['u', 'd', 'd']
        for i in range(3):
            for j in range(i + 1, 3):
                gen = min(i, j) + 1
                if gen > 2:
                    gen = 2
                if quarks[i] == quarks[j] == 'u':
                    nw.append(gen)
                elif quarks[i] == quarks[j] == 'd':
                    nw.append(-gen)
                else:
                    nw.append(gen)  # mixed: positive
        nucleon_words.append(nw)

    # Inter-nucleon crossings: all C(A,2) pairs
    nuclear_word = []
    for i in range(A):
        for j in range(i + 1, A):
            gen = min(i, j) + 1
            if gen > max(A - 1, 1):
                gen = max(A - 1, 1)
            if types[i] == 'p' and types[j] == 'p':
                nuclear_word.append(gen)
                n_pp += 1
                n_pos += 1
            elif types[i] == 'n' and types[j] == 'n':
                nuclear_word.append(-gen)
                n_nn += 1
                n_neg += 1
            else:
                nuclear_word.append(gen)  # mixed: positive
                n_pn += 1
                n_pos += 1

    # Electron crossings: Z Hopf + trefoil
    n_electron_crossings = 0
    for e in range(Z):
        gen = (e % max(A - 1, 1)) + 1
        nuclear_word.append(gen)
        n_pos += 1
        n_electron_crossings += 1
        if gen < max(A - 1, 1):
            nuclear_word.extend([gen, gen + 1, gen])
            n_pos += 3
            n_electron_crossings += 3

    writhe = n_pos - n_neg

    stats = {
        'A': A, 'Z': Z, 'N': N,
        'n_pp': n_pp, 'n_nn': n_nn, 'n_pn': n_pn,
        'n_nucleon_pairs': n_pp + n_nn + n_pn,
        'n_electron_crossings': n_electron_crossings,
        'n_pos': n_pos, 'n_neg': n_neg,
        'writhe': writhe,
        'nuclear_word_len': len(nuclear_word),
        'nucleon_words': nucleon_words,
    }
    return nuclear_word, stats


def braid_volume(word):
    """Compute Vol(closure(word)) via SnapPy."""
    if len(word) == 0:
        return 0.0
    try:
        L = snappy.Link(braid_closure=word)
        M = L.exterior()
        return float(M.volume())
    except Exception:
        return float('nan')


# ══════════════════════════════════════════════════════════════
# §2  GS REDUCTION COST (from atom_mass_gs_cost.py engine)
# ══════════════════════════════════════════════════════════════

def reduce_nf_with_cost(terms):
    """GS reduction returning (nf_terms, n_hecke, e_hecke)."""
    n_hecke = 0
    e_hecke = 0.0
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
                    deposit = coeff * HA
                    new_terms[pre + (i,) + suf] = new_terms.get(pre + (i,) + suf, 0.0) + deposit
                    new_terms[pre + suf] = new_terms.get(pre + suf, 0.0) + coeff
                    n_hecke += 1
                    e_hecke += abs(deposit)
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
    return terms, n_hecke, e_hecke


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


def build_atom_gs(Z, N):
    """Build atom NF with GS cost, matching the braid construction."""
    b3_raw = expand_inverse((0, -2, 0, -2, 0, -2))
    b3_nf, n_h0, e_h0 = reduce_nf_with_cost(b3_raw)
    total_n_hecke = 0
    total_e_hecke = 0.0

    def qcx(ti, tj, gen):
        if ti == tj == 'u':
            return {(gen,): 1.0}
        elif ti == tj == 'd':
            return {(gen,): 1.0, (): -HA}
        else:
            return {(gen,): 1.0, (): -HA / 2}

    def nucx(ti, tj, gen):
        if ti == tj == 'p':
            return {(gen,): 1.0}
        elif ti == tj == 'n':
            return {(gen,): 1.0, (): -HA}
        else:
            return {(gen,): 1.0, (): -HA / 2}

    def build_nucleon(quarks):
        nonlocal total_n_hecke, total_e_hecke
        total_n_hecke += n_h0
        total_e_hecke += e_h0
        elem = dict(b3_nf)
        for i in range(3):
            for j in range(i + 1, 3):
                gen = min(i, j)
                if gen > 1: gen = 1
                temp = hecke_mul(elem, qcx(quarks[i], quarks[j], gen))
                elem, nh, eh = reduce_nf_with_cost(temp)
                total_n_hecke += nh
                total_e_hecke += eh
        return elem

    A = Z + N
    types = ['p'] * Z + ['n'] * N
    proton_nf = build_nucleon(['u', 'u', 'd'])
    neutron_nf = build_nucleon(['u', 'd', 'd'])
    nfs = [dict(proton_nf) if t == 'p' else dict(neutron_nf) for t in types]

    # Count ALL nucleon constructions
    for k in range(1, A):
        if types[k] == 'p':
            build_nucleon(['u', 'u', 'd'])
        else:
            build_nucleon(['u', 'd', 'd'])

    elem = dict(nfs[0])
    for k in range(1, A):
        gen = min(k - 1, max(A - 2, 0))
        temp = hecke_mul(elem, nucx(types[k-1], types[k], gen))
        temp = hecke_mul(temp, nfs[k])
        elem, nh, eh = reduce_nf_with_cost(temp)
        total_n_hecke += nh
        total_e_hecke += eh

    electron = {(0, 1, 0): 1.0}
    for e in range(Z):
        gen = e % max(A - 1, 1)
        temp = hecke_mul(elem, {(gen,): 1.0})
        temp = hecke_mul(temp, electron)
        elem, nh, eh = reduce_nf_with_cost(temp)
        total_n_hecke += nh
        total_e_hecke += eh

    L1 = sum(abs(c) for c in elem.values())
    return L1, total_n_hecke, total_e_hecke


# ══════════════════════════════════════════════════════════════
# §3  MAIN — UNIFIED TABLE
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
    print("=" * 140)
    print("UNIFIED: VOLUME + HECKE + CROSSING STRUCTURE")
    print(f"q₀ = {q0:.10f}   HA = q-q⁻¹ = {HA:.10f}   ℏ_q² = {hbar_q_sq:.10f}")
    print("=" * 140)
    print()

    # Nucleon volumes
    proton_word = [1, -2, 1, -2, 1, -2, 1, 1, 2]
    neutron_word = [1, -2, 1, -2, 1, -2, 1, 1, -2]
    vol_p = braid_volume(proton_word)
    vol_n = braid_volume(neutron_word)
    print(f"  Vol(proton braid)  = {vol_p:.6f} {'(non-hyperbolic)' if abs(vol_p) < 0.01 else ''}")
    print(f"  Vol(neutron braid) = {vol_n:.6f}")
    print()

    rows = []
    for Z_elem in sorted(ELEMENTS.keys()):
        name, Z, N, M_obs = ELEMENTS[Z_elem]
        A = Z + N
        t0 = time.time()

        # 1. Braid word + crossing stats
        nuc_word, cstats = build_nuclear_braid(Z, N)

        # 2. Volumes
        vol_nuc = braid_volume(nuc_word)
        vol_total = Z * vol_p + N * vol_n + vol_nuc

        # 3. GS reduction cost
        L1, n_hecke, e_hecke = build_atom_gs(Z, N)

        elapsed = time.time() - t0

        row = {
            'name': name, 'Z': Z, 'N': N, 'A': A,
            'n_pp': cstats['n_pp'], 'n_nn': cstats['n_nn'], 'n_pn': cstats['n_pn'],
            'writhe': cstats['writhe'],
            'word_len': cstats['nuclear_word_len'],
            'vol_nuc': vol_nuc, 'vol_total': vol_total,
            'L1': L1, 'n_hecke': n_hecke, 'e_hecke': e_hecke,
            'M_obs': M_obs, 'elapsed': elapsed,
        }
        rows.append(row)

    # ── Print unified table ─────────────────────────────────
    print(f"{'Atom':>4} | {'A':>3} | {'pp':>3} {'nn':>3} {'pn':>3} | {'writhe':>6} | "
          f"{'Vol_nuc':>8} | {'Vol_tot':>8} | {'E_hecke':>8} | {'L¹':>8} | "
          f"{'M_obs':>8} | {'Vol/M×1k':>8} | {'E_hk/M×1k':>10} | {'t':>5}")
    print("─" * 140)
    for r in rows:
        vm = r['vol_total'] / r['M_obs'] * 1000 if r['M_obs'] > 0 and r['vol_total'] > 0.01 else 0
        em = r['e_hecke'] / r['M_obs'] * 1000 if r['M_obs'] > 0 else 0
        print(f"{r['name']:>4} | {r['A']:3d} | {r['n_pp']:3d} {r['n_nn']:3d} {r['n_pn']:3d} | "
              f"{r['writhe']:+6d} | {r['vol_nuc']:8.3f} | {r['vol_total']:8.3f} | "
              f"{r['e_hecke']:8.2f} | {r['L1']:8.2f} | {r['M_obs']:8.1f} | "
              f"{vm:8.3f} | {em:10.4f} | {r['elapsed']:5.1f}s")

    # ── Correlation analysis ────────────────────────────────
    print()
    print("=" * 140)
    print("CORRELATION: Vol vs E_hecke vs crossings")
    print("=" * 140)

    # Vol vs E_hecke
    print()
    print(f"{'Atom':>4} | {'Vol_total':>10} | {'E_hecke':>10} | {'Vol/E_hk':>10} | "
          f"{'n_cross':>7} | {'Vol/n_cross':>11} | {'E_hk/n_cross':>12}")
    print("─" * 100)
    for r in rows:
        nc = r['n_pp'] + r['n_nn'] + r['n_pn']
        ve = r['vol_total'] / r['e_hecke'] if r['e_hecke'] > 0 else 0
        vn = r['vol_total'] / nc if nc > 0 else 0
        en = r['e_hecke'] / nc if nc > 0 else 0
        print(f"{r['name']:>4} | {r['vol_total']:10.3f} | {r['e_hecke']:10.2f} | {ve:10.4f} | "
              f"{nc:7d} | {vn:11.4f} | {en:12.4f}")

    # ── Key relationship: Vol = α × n_cross × HA ──────────
    print()
    print("=" * 140)
    print("TEST: Vol_total ≈ α × C(A,2) × HA?  (volume per crossing ∝ Hecke amplitude)")
    print("=" * 140)
    print()
    for r in rows:
        cA2 = r['A'] * (r['A'] - 1) // 2
        vol_per_crossing_per_HA = r['vol_total'] / (cA2 * HA) if cA2 > 0 else 0
        print(f"  {r['name']:>4}: C(A,2) = {cA2:4d}, Vol/(C×HA) = {vol_per_crossing_per_HA:.4f}")

    # ── Best relationship ──────────────────────────────────
    print()
    print("=" * 140)
    print("BEST FIT: Vol_total = β × f(crossings)")
    print("=" * 140)

    # Try: Vol = β × (N × vol_n + Vol_nuclear)
    # Since vol_p = 0, Vol_total = N × vol_n + Vol_nuclear
    # Check if Vol_nuclear scales with crossing structure
    print()
    print("Vol_nuclear decomposition:")
    print(f"{'Atom':>4} | {'Vol_nuc':>8} | {'n_pp':>4} | {'n_nn':>4} | {'n_pn':>4} | "
          f"{'Vol_nuc/(nn)':>12} | {'Vol_nuc/(pp+pn)':>15}")
    print("─" * 80)
    for r in rows:
        if r['A'] <= 1:
            continue
        vnn = r['vol_nuc'] / r['n_nn'] if r['n_nn'] > 0 else float('inf')
        vpp = r['vol_nuc'] / (r['n_pp'] + r['n_pn']) if (r['n_pp'] + r['n_pn']) > 0 else float('inf')
        print(f"{r['name']:>4} | {r['vol_nuc']:8.3f} | {r['n_pp']:4d} | {r['n_nn']:4d} | {r['n_pn']:4d} | "
              f"{vnn:12.4f} | {vpp:15.4f}")

    # Witness
    w = WitnessBuilder("atom-vol-hecke-unified", engine="snappy")
    w.set_description(
        "Unified volume + Hecke + crossing analysis for Z=1-8. "
        "Tracks Vol, E_hecke, crossing types (pp/nn/pn), writhe."
    )
    w.add_parameter("q0", str(q0))
    w.add_parameter("HA", str(HA))
    w.add_parameter("vol_proton", str(vol_p))
    w.add_parameter("vol_neutron", str(vol_n))
    w.add_data("results", rows)
    w.save()


if __name__ == "__main__":
    main()
