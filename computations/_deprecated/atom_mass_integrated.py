#!/usr/bin/env python3
"""
INTEGRATED MASS: Three-channel Wedderburn + Gram character from certificates.

Combines:
1. Three-channel Wedderburn traces (sym/std/alt) from Python engine
2. Gram character correction (F_Pauli) from Rust engine certificates
3. Full Gram matrix for small atoms (A ≤ 4)
4. Bare Φ_q as fallback for atoms without certificates

The mass functional:
  Φ_integrated = Φ_bare + β × ln(F_Pauli)

where F_Pauli = |tr_alt/net| from the Rust certificate encodes
the character content that bare Φ_q misses.

For atoms without certificates: F_Pauli is INTERPOLATED from the
crossing asymmetry (n_nn - n_pp) / C(A,2), which correlates with
F_Pauli for atoms with certificates.

Usage:
    python3 folio-assistant/computations/atom_mass_integrated.py
"""

import json, math, sys, time, glob
from fractions import Fraction
from itertools import combinations
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q as q0, HBAR_Q_SQ
from witness_base import WitnessBuilder

VOL_NEUTRON = 13.9484177283
HA = q0 - 1.0/q0
# z moved to pyhecke.gram via M2b inversion — re-import canonically.
from pyhecke.gram import z  # noqa: E402
m_n = VOL_NEUTRON / HBAR_Q_SQ


# ══════════════════════════════════════════════════════════════
# §1  LOAD RUST CERTIFICATES
# ══════════════════════════════════════════════════════════════

CERT_DIR = Path(__file__).parent.parent.parent / "tools" / "hecke-engine"

def load_certificate(Z, N):
    """Load Rust engine certificate for isotope (Z, N).
    Returns dict with f_pauli, tr_alt, net, etc. or None."""
    A = Z + N
    # Try common naming patterns
    from experimental_constants import M_E_MEV
    element_names = {
        1:'h', 2:'he', 3:'li', 4:'be', 5:'b', 6:'c', 7:'n', 8:'o',
        9:'f', 10:'ne', 11:'na', 12:'mg', 13:'al', 14:'si', 15:'p',
        16:'s', 17:'cl', 18:'ar', 19:'k', 20:'ca',
    }
    sym = element_names.get(Z, f'z{Z}')
    patterns = [
        f"certificate-{A}{sym}.json",
        f"certificate-{A}{sym.lower()}.json",
    ]
    for pat in patterns:
        fpath = CERT_DIR / pat
        if fpath.exists():
            try:
                d = json.load(open(fpath))
                return {
                    'f_pauli': d.get('f_pauli_f64', 1.0),
                    'tr_alt': d.get('tr_alt_f64', 0.0),
                    'net': d.get('net_f64', 0.0),
                    'tr_markov': d.get('tr_markov_f64', 0.0),
                    'source': str(fpath.name),
                }
            except:
                pass
    return None


# ══════════════════════════════════════════════════════════════
# §2  HECKE ENGINE (Python)
# ══════════════════════════════════════════════════════════════

def compute_Phi(ordering):
    A = len(ordering)
    if A <= 1: return 0.0
    Phi = 0.0
    for gen in range(A - 1):
        a, b = 0.0, 1.0
        for j in range(gen + 1, A):
            ti, tj = ordering[gen], ordering[j]
            if ti == 1 and tj == 1: d = 0.0
            elif ti == 0 and tj == 0: d = -HA
            else: d = -HA / 2
            a, b = a * HA + a * d + b, a + b * d
        V = z * a + b
        if abs(V) < 1e-300: return float('inf')
        Phi += math.log(abs(V))
    return Phi


def three_channel_traces(ordering):
    """Compute sym, std, alt traces (numeric at q₀)."""
    A = len(ordering)
    if A <= 1: return 1.0, 1.0, 1.0
    tr_sym = 1.0
    tr_std = 1.0
    tr_alt = 1.0
    for i in range(A - 1):
        sym_prod = 1.0
        alt_prod = 1.0
        a, b = 0.0, 1.0
        for j in range(i + 1, A):
            ti, tj = ordering[i], ordering[j]
            if ti == 1 and tj == 1:
                c, d = 1.0, 0.0
            elif ti == 0 and tj == 0:
                c, d = 1.0, -HA
            else:
                c, d = 1.0, -HA / 2
            sym_prod *= (c * q0 + d)
            alt_prod *= (-c / q0 + d)
            a, b = a * c * HA + a * d + b * c, a * c + b * d
        tr_sym *= sym_prod
        tr_std *= (z * a + b)
        tr_alt *= alt_prod
    return tr_sym, tr_std, tr_alt


def crossing_counts(ordering):
    A = len(ordering)
    n_pp, n_nn, n_pn = 0, 0, 0
    for i in range(A):
        for j in range(i + 1, A):
            if ordering[i] == 1 and ordering[j] == 1: n_pp += 1
            elif ordering[i] == 0 and ordering[j] == 0: n_nn += 1
            else: n_pn += 1
    return n_pp, n_nn, n_pn


def find_gs(Z, N):
    A = Z + N
    if A <= 1: return [1] if Z > 0 else [0]
    total = math.comb(A, Z)
    if total <= 50000:
        best_Phi, best_o = float('inf'), None
        for pos in combinations(range(A), Z):
            o = [0]*A
            for p in pos: o[p] = 1
            Phi = compute_Phi(o)
            if Phi < best_Phi: best_Phi, best_o = Phi, list(o)
        return best_o
    best_global = (float('inf'), None)
    o1 = [0]*A
    for k in range(min(Z,N)):
        idx = 2*k+1 if Z<=N else 2*k
        if idx < A: o1[idx] = 1
    placed = sum(o1)
    for k in range(A):
        if placed >= Z: break
        if o1[k] == 0: o1[k] = 1; placed += 1
    for start in [list(o1), list(reversed(o1)), [1]*Z+[0]*N, [0]*N+[1]*Z]:
        if sum(start) != Z: continue
        o = list(start); Phi = compute_Phi(o)
        improved = True
        while improved:
            improved = False
            best_swap, best_delta = None, 0.0
            for pi in [i for i in range(A) if o[i]==1]:
                for ni in [i for i in range(A) if o[i]==0]:
                    o[pi], o[ni] = 0, 1
                    new_Phi = compute_Phi(o)
                    delta = new_Phi - Phi
                    o[pi], o[ni] = 1, 0
                    if delta < best_delta - 1e-12:
                        best_delta = delta; best_swap = (pi, ni)
            if best_swap:
                pi, ni = best_swap; o[pi], o[ni] = 0, 1; Phi += best_delta; improved = True
        if Phi < best_global[0]: best_global = (Phi, list(o))
    return best_global[1]


# ══════════════════════════════════════════════════════════════
# §3  F_PAULI INTERPOLATION
# ══════════════════════════════════════════════════════════════

def interpolate_f_pauli(Z, N, n_pp, n_nn, n_pn, known_atoms):
    """Interpolate F_Pauli from crossing asymmetry for atoms without certificates.

    F_Pauli correlates with the nn/pp asymmetry of the nucleus.
    Fit: ln(F_Pauli) = a × (n_nn - n_pp)/C(A,2) + b
    from atoms with known F_Pauli.
    """
    A = Z + N
    total = n_pp + n_nn + n_pn
    if total == 0:
        return 1.0

    asym = (n_nn - n_pp) / total

    # Fit from known atoms
    xs, ys = [], []
    for a in known_atoms:
        if a['cert'] is not None and a['A'] > 1:
            fp = a['cert']['f_pauli']
            if fp > 0.001 and fp < 100:  # exclude outliers like Ca
                a_total = a['n_pp'] + a['n_nn'] + a['n_pn']
                if a_total > 0:
                    xs.append((a['n_nn'] - a['n_pp']) / a_total)
                    ys.append(math.log(fp))

    if len(xs) < 2:
        return 1.0

    # Simple linear regression
    import numpy as np
    xs, ys = np.array(xs), np.array(ys)
    A_mat = np.vstack([xs, np.ones(len(xs))]).T
    result = np.linalg.lstsq(A_mat, ys, rcond=None)
    slope, intercept = result[0]

    ln_fp = slope * asym + intercept
    return math.exp(ln_fp)


# ══════════════════════════════════════════════════════════════
# §4  FULL GRAM MATRIX (small atoms)
# ══════════════════════════════════════════════════════════════

from pyhecke.gram import NF_BASIS as NF_BASIS_3, TR_M as _TR_M_NATIVE  # noqa: E402
TR_M_3 = list(_TR_M_NATIVE)  # local mutable-list copy for back-compat

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
            if abs(coeff) < 1e-15: continue
            done = False
            for pos in range(len(word) - 1):
                if word[pos] == word[pos + 1]:
                    i = word[pos]; pre, suf = word[:pos], word[pos + 2:]
                    new_terms[pre + (i,) + suf] = new_terms.get(pre + (i,) + suf, 0.0) + coeff * HA
                    new_terms[pre + suf] = new_terms.get(pre + suf, 0.0) + coeff
                    done = changed = True; break
            if done: continue
            for pos in range(len(word) - 2):
                a, b, c = word[pos], word[pos + 1], word[pos + 2]
                if a == c and abs(a - b) == 1:
                    nt = (b, a, b)
                    if nt < (a, b, c):
                        nw = word[:pos] + nt + word[pos + 3:]
                        new_terms[nw] = new_terms.get(nw, 0.0) + coeff
                        done = changed = True; break
            if done: continue
            for pos in range(len(word) - 1):
                a, b = word[pos], word[pos + 1]
                if abs(a - b) >= 2 and a > b:
                    nw = word[:pos] + (b, a) + word[pos + 2:]
                    new_terms[nw] = new_terms.get(nw, 0.0) + coeff
                    done = changed = True; break
            if not done:
                new_terms[word] = new_terms.get(word, 0.0) + coeff
        terms = {w: c for w, c in new_terms.items() if abs(c) > 1e-15}
    return terms

def markov_trace_general(terms):
    total = 0.0
    for word, coeff in terms.items():
        if word in NF_BASIS_3:
            idx = NF_BASIS_3.index(word)
            total += coeff * TR_M_3[idx]
        else:
            total += coeff * z ** len(word)
    return total

def compute_gram_norm(ordering):
    """Compute Gram norm ||N||_G for small atoms via full NF multiplication."""
    A = len(ordering)
    if A > 6:  # too large for Python NF engine
        return float('nan')

    # Build the nuclear element in H_A(q)
    elem = {(): 1.0}
    for i in range(A - 1):
        ti, tj = ordering[i], ordering[i + 1]
        if ti == 1 and tj == 1:
            factor = {(i,): 1.0}
        elif ti == 0 and tj == 0:
            factor = {(i,): 1.0, (): -HA}
        else:
            factor = {(i,): 1.0, (): -HA / 2}
        elem = hecke_mul(elem, factor)
        elem = reduce_nf(elem)

    # ||N||_G² = tr_M(N · N) = Σ_{w1,w2} c_w1 c_w2 tr_M(w1·w2)
    gram_sq = 0.0
    for w1, c1 in elem.items():
        for w2, c2 in elem.items():
            prod = hecke_mul({w1: 1.0}, {w2: 1.0})
            prod_nf = reduce_nf(prod)
            gram_sq += c1 * c2 * markov_trace_general(prod_nf)

    return math.sqrt(abs(gram_sq))


# ══════════════════════════════════════════════════════════════
# §5  MAIN
# ══════════════════════════════════════════════════════════════

ELEMENTS = [
    ("H",  "¹H",  1, 0,  938.783),  ("He", "⁴He", 2, 2,  3728.401),
    ("Li", "⁷Li", 3, 4,  6535.367), ("Be", "⁹Be", 4, 5,  8394.794),
    ("B",  "¹¹B", 5, 6,  10255.103),("C",  "¹²C", 6, 6,  11177.930),
    ("N",  "¹⁴N", 7, 7,  13043.781),("O",  "¹⁶O", 8, 8,  14899.169),
    ("F",  "¹⁹F", 9, 10, 17696.901),("Ne", "²⁰Ne",10,10, 18622.835),
    ("Na", "²³Na",11,12, 21414.830),("Mg", "²⁴Mg",12,12, 22341.908),
    ("Al", "²⁷Al",13,14, 25133.143),("Si", "²⁸Si",14,14, 26060.344),
    ("P",  "³¹P", 15,16, 28851.873),("S",  "³²S", 16,16, 29781.800),
    ("Cl", "³⁵Cl",17,18, 32573.283),("Ar", "⁴⁰Ar",18,22, 37224.719),
    ("K",  "³⁹K", 19,20, 36294.464),("Ca", "⁴⁰Ca",20,20, 37213.777),
]


def main():
    print("=" * 120)
    print("INTEGRATED MASS: Three-channel + Gram character + certificates")
    print(f"q₀ = {q0:.10f}  HA = {HA:.10f}")
    print("=" * 120)
    print()

    # Phase 1: Build all atom data
    atoms = []
    for name, label, Z, N, M_obs in ELEMENTS:
        A = Z + N
        t0 = time.time()
        ordering = find_gs(Z, N)
        phi = compute_Phi(ordering)
        tr_sym, tr_std, tr_alt = three_channel_traces(ordering)
        n_pp, n_nn, n_pn = crossing_counts(ordering)
        cert = load_certificate(Z, N)
        elapsed = time.time() - t0

        atoms.append({
            'label': label, 'Z': Z, 'N': N, 'A': A, 'M_obs': M_obs,
            'phi': phi, 'ordering': ordering,
            'tr_sym': tr_sym, 'tr_std': tr_std, 'tr_alt': tr_alt,
            'n_pp': n_pp, 'n_nn': n_nn, 'n_pn': n_pn,
            'cert': cert, 'elapsed': elapsed,
        })

        cert_str = f"F_P={cert['f_pauli']:.4f}" if cert else "no cert"
        print(f"  {label:>5} A={A:2d}: Φ={phi:+.4f}  {cert_str}  [{elapsed:.1f}s]")

    # Phase 2: Interpolate F_Pauli for atoms without certificates
    print()
    print("F_Pauli interpolation:")
    for a in atoms:
        if a['cert'] is not None:
            fp = a['cert']['f_pauli']
            a['f_pauli'] = fp
            a['fp_source'] = 'certificate'
        else:
            fp = interpolate_f_pauli(a['Z'], a['N'], a['n_pp'], a['n_nn'], a['n_pn'], atoms)
            a['f_pauli'] = fp
            a['fp_source'] = 'interpolated'
        print(f"  {a['label']:>5}: F_Pauli = {a['f_pauli']:.4f} ({a['fp_source']})")

    # Phase 3: Compute Gram norm for small atoms
    print()
    print("Gram norms (A ≤ 6):")
    for a in atoms:
        if a['A'] <= 6:
            gram = compute_gram_norm(a['ordering'])
            a['gram_norm'] = gram
            print(f"  {a['label']:>5}: ||N||_G = {gram:.6f}")
        else:
            a['gram_norm'] = float('nan')

    # Phase 4: Calibrate and predict with multiple variants
    M_H = atoms[0]['M_obs']
    M_He = atoms[1]['M_obs']
    M_C = atoms[5]['M_obs']
    lhs1 = M_He - 2 * M_H
    lhs2 = M_C - 6 * M_H

    print()
    print("=" * 120)
    print("MASS FORMULA VARIANTS")
    print("=" * 120)

    variants = {
        'Bare Φ_q': lambda a: a['phi'],
        'Φ + ln(F_P)': lambda a: a['phi'] + math.log(a['f_pauli']) if a['f_pauli'] > 0.001 else a['phi'],
        'Φ × ln(F_P)': lambda a: a['phi'] * math.log(a['f_pauli']) if a['f_pauli'] > 0.001 and abs(math.log(a['f_pauli'])) > 0.001 else a['phi'],
        'Φ × F_P': lambda a: a['phi'] * a['f_pauli'],
    }

    for vname, vfunc in variants.items():
        f_he = vfunc(atoms[1])
        f_c = vfunc(atoms[5])
        denom = f_he * lhs2 - f_c * lhs1
        if abs(denom) < 1e-10:
            print(f"\n  {vname}: DEGENERATE")
            continue
        alpha = m_n * (6*lhs1 - 2*lhs2) / denom
        E0 = lhs1 / (2*m_n + alpha*f_he)
        mp = M_H / E0

        print(f"\n  {vname}: α={alpha:.4f}, E₀={E0:.6f}")
        print(f"  {'Atom':>5} | {'M_pred':>12} | {'M_obs':>12} | {'Δ%':>8} | {'F_P':>6} | {'src':>6}")
        print(f"  {'─'*70}")
        errors = []
        for a in atoms:
            f_val = vfunc(a)
            M_pred = E0 * (a['Z']*mp + a['N']*m_n + alpha*f_val)
            pct = (M_pred - a['M_obs']) / a['M_obs'] * 100
            cal = "CAL" if a['label'] in ['¹H', '⁴He', '¹²C'] else ""
            fp_str = f"{a['f_pauli']:.3f}" if a['f_pauli'] != 1.0 else "  —  "
            src = a['fp_source'][:4] if 'fp_source' in a else ""
            print(f"  {a['label']:>5} | {M_pred:12.3f} | {a['M_obs']:12.3f} | {pct:+7.3f}% | {fp_str} | {src} {cal}")
            if not cal: errors.append(abs(pct))
        print(f"  {len(errors)} predictions: mean = {sum(errors)/len(errors):.4f}%, max = {max(errors):.4f}%")

    # Witness
    w = WitnessBuilder("atom-mass-integrated", engine="python")
    w.set_description(
        "Integrated mass: three-channel + Gram character (F_Pauli) from "
        "Rust certificates + interpolation for missing atoms."
    )
    w.add_parameter("q0", str(q0))
    w.add_data("atoms", [
        {'label': a['label'], 'Z': a['Z'], 'N': a['N'],
         'phi': a['phi'], 'f_pauli': a['f_pauli'],
         'fp_source': a.get('fp_source', ''),
         'cert': a['cert'] is not None}
        for a in atoms
    ])
    w.save()


if __name__ == "__main__":
    main()
