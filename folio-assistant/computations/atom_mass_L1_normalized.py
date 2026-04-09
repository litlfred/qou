#!/usr/bin/env python3
"""
Normalized L¹ mass functionals — testing which normalization
maps L¹(atom_NF) → physical mass.

Tests:
  F_a = L¹ / C(A,2)         — per crossing pair
  F_b = L¹ / A              — per nucleon
  F_c = L¹ / A²             — per nucleon²
  F_d = L¹ / (A-1)          — per generator (transfer matrix count)
  F_e = L¹ / NF_terms       — per NF basis element
  F_f = log(L¹) / log(A)    — log-log scaling exponent

Also: q-dependence study — does the best functional change with q?
Sweep q from 1.05 to 1.20 and check if the ratio F(atom)/F(proton)
is stable or q-sensitive.

Usage:
    python3 folio-assistant/computations/atom_mass_L1_normalized.py
"""

import math
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from q_parameter import Q as q0_default
from experimental_constants import M_P_MEV, M_N_MEV, M_E_MEV
from witness_base import WitnessBuilder

# We need to rebuild the Hecke engine at variable q.
# Import the structural functions, but override HA and z.


def make_engine(q_val):
    """Create a complete Hecke engine at a given q value."""
    q_inv_val = 1.0 / q_val
    ha = q_val - q_inv_val
    z_val = 1.0 / (q_val**0.5 + q_val**(-0.5))

    def crossing_coeffs(ti, tj):
        if ti == 1 and tj == 1:
            return 1.0, 0.0
        elif ti == 0 and tj == 0:
            return 1.0, -ha
        else:
            return 1.0, -ha / 2

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
                        new_terms[pre + (i,) + suf] = new_terms.get(pre + (i,) + suf, 0.0) + coeff * ha
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
                    new_terms[w] = new_terms.get(w, 0.0) - c * ha
            terms = {w: c for w, c in new_terms.items() if abs(c) > 1e-15}
        return terms

    def quark_crossing(type_i, type_j, gen):
        if type_i == type_j == 'u':
            return {(gen,): 1.0}
        elif type_i == type_j == 'd':
            return {(gen,): 1.0, (): -ha}
        else:
            return {(gen,): 1.0, (): -ha / 2}

    def nuclear_crossing(type_i, type_j, gen):
        if type_i == type_j == 'p':
            return {(gen,): 1.0}
        elif type_i == type_j == 'n':
            return {(gen,): 1.0, (): -ha}
        else:
            return {(gen,): 1.0, (): -ha / 2}

    def build_nucleon(quark_types):
        b3_raw = expand_inverse((0, -2, 0, -2, 0, -2))
        b3_nf = reduce_nf(b3_raw)
        elem = dict(b3_nf)
        for i in range(3):
            for j in range(i + 1, 3):
                gen = min(i, j)
                if gen > 1:
                    gen = 1
                cx = quark_crossing(quark_types[i], quark_types[j], gen)
                elem = hecke_mul(elem, cx)
                elem = reduce_nf(elem)
        return elem

    def build_atom(Z, N):
        A = Z + N
        types = ['p'] * Z + ['n'] * N
        proton_nf = build_nucleon(['u', 'u', 'd'])
        neutron_nf = build_nucleon(['u', 'd', 'd'])
        nfs = [dict(proton_nf) if t == 'p' else dict(neutron_nf) for t in types]
        if A == 0:
            return {(): 1.0}
        elem = dict(nfs[0])
        for k in range(1, A):
            gen = min(k - 1, max(A - 2, 0))
            cx = nuclear_crossing(types[k - 1], types[k], gen)
            temp = hecke_mul(elem, cx)
            temp = hecke_mul(temp, nfs[k])
            elem = reduce_nf(temp)
        # Add electrons
        electron = {(0, 1, 0): 1.0}
        for e_idx in range(Z):
            gen = e_idx % max(A - 1, 1)
            hopf = {(gen,): 1.0}
            temp = hecke_mul(elem, hopf)
            temp = hecke_mul(temp, electron)
            elem = reduce_nf(temp)
        return elem

    def L1(terms):
        return sum(abs(c) for c in terms.values())

    def net(terms):
        return sum(terms.values())

    return {
        'build_nucleon': build_nucleon,
        'build_atom': build_atom,
        'L1': L1,
        'net': net,
        'q': q_val,
        'ha': ha,
        'z': z_val,
    }


# ══════════════════════════════════════════════════════════════
# §1  NORMALIZED L¹ FUNCTIONALS AT q₀
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
    eng = make_engine(q0_default)

    print("=" * 130)
    print("NORMALIZED L¹ MASS FUNCTIONALS")
    print(f"q₀ = {q0_default:.10f}   HA = {eng['ha']:.10f}   z = {eng['z']:.10f}")
    print("=" * 130)

    # Build all atoms
    atoms = {}
    for Z in sorted(ELEMENTS.keys()):
        name, z_val, N = ELEMENTS[Z]
        A = z_val + N
        t0 = time.time()
        nf = eng['build_atom'](z_val, N)
        elapsed = time.time() - t0
        L1 = eng['L1'](nf)
        nt = eng['net'](nf)
        n_terms = len(nf)
        M_obs = AME2020_MASS.get((z_val, N), 0.0)
        atoms[Z] = {
            'name': name, 'Z': z_val, 'N': N, 'A': A,
            'L1': L1, 'net': nt, 'terms': n_terms,
            'M_obs': M_obs, 'elapsed': elapsed,
        }
        print(f"  Built {name:>3} (A={A:2d}): L¹={L1:12.4f}, net={nt:+.4f}, "
              f"terms={n_terms:6d}, time={elapsed:.1f}s")

    # Proton reference
    proton_nf = eng['build_nucleon'](['u', 'u', 'd'])
    p_L1 = eng['L1'](proton_nf)

    print()
    print("=" * 130)
    print("NORMALIZATION CANDIDATES")
    print("=" * 130)
    print()
    print(f"{'Atom':>4} | {'A':>3} | {'C(A,2)':>7} | {'L¹':>10} | "
          f"{'L¹/C(A,2)':>10} | {'L¹/A':>10} | {'L¹/A²':>10} | "
          f"{'L¹/(A-1)':>10} | {'L¹/terms':>10} | {'M/m_p':>8}")
    print("─" * 130)

    for Z in sorted(atoms.keys()):
        a = atoms[Z]
        A = a['A']
        cA2 = max(A * (A - 1) // 2, 1)
        L1 = a['L1']
        M_ratio = a['M_obs'] / M_P_MEV

        Fa = L1 / cA2
        Fb = L1 / A
        Fc = L1 / (A * A)
        Fd = L1 / max(A - 1, 1)
        Fe = L1 / a['terms'] if a['terms'] > 0 else 0

        print(f"{a['name']:>4} | {A:3d} | {cA2:7d} | {L1:10.4f} | "
              f"{Fa:10.4f} | {Fb:10.4f} | {Fc:10.6f} | "
              f"{Fd:10.4f} | {Fe:10.6f} | {M_ratio:8.3f}")

    # Now calibrate each normalization to proton and check scaling
    print()
    print("=" * 130)
    print("SCALING TEST: F_norm(atom) / F_norm(proton) vs M(atom)/m_p")
    print("=" * 130)

    # For proton: A=1, so C(1,2)=0. Use atom ¹H (A=1, 1 proton + 0 neutrons + 1 electron)
    h = atoms[1]
    h_L1 = h['L1']
    h_A = h['A']

    print()
    print(f"  Reference: ¹H atom, L¹ = {h_L1:.4f}, A = {h_A}")
    print()

    # Different normalizations, calibrated to ¹H
    norms = {
        'L¹/C(A,2)': lambda L1, A, n: L1 / max(A*(A-1)//2, 1),
        'L¹/A':      lambda L1, A, n: L1 / A,
        'L¹/A²':     lambda L1, A, n: L1 / (A*A),
        'L¹/(A-1)':  lambda L1, A, n: L1 / max(A-1, 1),
        'L¹/terms':  lambda L1, A, n: L1 / max(n, 1),
        'L¹^(1/2)':  lambda L1, A, n: L1**0.5,
        'L¹^(2/3)':  lambda L1, A, n: L1**(2/3),
    }

    # Compute reference values for H
    h_refs = {name: fn(h_L1, h_A, h['terms']) for name, fn in norms.items()}

    print(f"{'Atom':>4} | {'M/m_p':>8} |", end="")
    for name in norms:
        print(f" {name:>11} |", end="")
    print()
    print("─" * 130)

    for Z in sorted(atoms.keys()):
        a = atoms[Z]
        ratio_m = a['M_obs'] / M_P_MEV
        print(f"{a['name']:>4} | {ratio_m:8.3f} |", end="")
        for norm_name, fn in norms.items():
            val = fn(a['L1'], a['A'], a['terms'])
            ratio = val / h_refs[norm_name] if h_refs[norm_name] != 0 else 0
            print(f" {ratio:11.4f} |", end="")
        print()

    # Best-fit analysis: which normalization has smallest mean squared relative error?
    print()
    print("=" * 130)
    print("BEST FIT: Mean |log(F_ratio/M_ratio)| across atoms")
    print("=" * 130)

    for norm_name, fn in norms.items():
        ref = h_refs[norm_name]
        errors = []
        for Z in sorted(atoms.keys()):
            a = atoms[Z]
            if a['M_obs'] <= 0:
                continue
            ratio_m = a['M_obs'] / M_P_MEV
            val = fn(a['L1'], a['A'], a['terms'])
            ratio_f = val / ref if ref != 0 else 0
            if ratio_f > 0 and ratio_m > 0:
                errors.append(abs(math.log(ratio_f / ratio_m)))
        mean_err = sum(errors) / len(errors) if errors else float('inf')
        print(f"  {norm_name:>12}: mean |log(F/M)| = {mean_err:.4f}")

    # ══════════════════════════════════════════════════════════════
    # §2  q-DEPENDENCE STUDY
    # ══════════════════════════════════════════════════════════════

    print()
    print("=" * 130)
    print("q-DEPENDENCE: Does the best normalization change with q?")
    print("Sweep q from 1.05 to 1.20, compute L¹(⁴He)/L¹(¹H) and L¹(⁷Li)/L¹(¹H)")
    print("=" * 130)
    print()
    print(f"{'q':>8} | {'HA':>10} | {'L¹(p)':>10} | {'L¹(H)':>10} | {'L¹(He)':>10} | "
          f"{'L¹(Li)':>10} | {'He/H':>8} | {'Li/H':>8} | "
          f"{'He/H/A':>8} | {'Li/H/A':>8}")
    print("─" * 130)

    for q_test in [1.05, 1.08, 1.10, q0_default, 1.12, 1.15, 1.20]:
        e = make_engine(q_test)
        p_nf = e['build_nucleon'](['u', 'u', 'd'])
        h_nf = e['build_atom'](1, 0)
        he_nf = e['build_atom'](2, 2)
        li_nf = e['build_atom'](3, 4)

        p_l1 = e['L1'](p_nf)
        h_l1 = e['L1'](h_nf)
        he_l1 = e['L1'](he_nf)
        li_l1 = e['L1'](li_nf)

        he_ratio = he_l1 / h_l1 if h_l1 > 0 else 0
        li_ratio = li_l1 / h_l1 if h_l1 > 0 else 0

        # Expected mass ratios: He/H ≈ 3.97, Li/H ≈ 6.97
        # Normalized by A: He/H/4 ≈ 0.99, Li/H/7 ≈ 1.00
        he_norm = he_ratio / 4
        li_norm = li_ratio / 7

        marker = " ← q₀" if abs(q_test - q0_default) < 0.001 else ""
        print(f"{q_test:8.4f} | {e['ha']:10.6f} | {p_l1:10.4f} | {h_l1:10.4f} | "
              f"{he_l1:10.4f} | {li_l1:10.4f} | {he_ratio:8.3f} | {li_ratio:8.3f} | "
              f"{he_norm:8.4f} | {li_norm:8.4f}{marker}")

    # Witness
    w = WitnessBuilder("atom-mass-L1-normalized", engine="python")
    w.set_description(
        "Normalized L¹ mass functionals. Tests L¹/C(A,2), L¹/A, L¹/A², "
        "L¹/(A-1), L¹/terms, L¹^(1/2), L¹^(2/3). "
        "q-dependence sweep from 1.05 to 1.20."
    )
    w.add_parameter("q0", str(q0_default))
    w.add_data("atoms", {str(Z): atoms[Z] for Z in atoms})
    w.save()


if __name__ == "__main__":
    main()
