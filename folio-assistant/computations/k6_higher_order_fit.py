#!/usr/bin/env python3
"""
k=6 higher-order structure extraction.

Computes the nuclear character χ_λ(q₀) for each partition λ⊢6 and
each test nucleus, using the inter-nucleon crossing chain
  Π_{i<j} (σ_g + d_ij · I)
where d_ij ∈ {0, -h, -h/2} is the crossing-type shift and
g = (i+j) mod (k-1).  This matches symbolic_k6_characters.py.

Goal: compare the actual per-partition Markov contribution
      m_λ(Z,N) = w_λ · χ_λ(Z,N) / dim_λ · m_e
against the first-order scaling used in hecke_core.py:
  [3,2,1]:     ZN / A^{4/3}
  [4,1,1]+[3,1,1,1]: (N-Z)² / (4 A^{4/3})
  [4,2]+[2,2,1,1]:   Z(Z-1) / A^{4/3}

Any residual = higher-order structure captured by exact character.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))

import numpy as np
from q_parameter import Q as q0, Q_INV as qi, HA
from experimental_constants import M_E_MEV
from level_k_binding import standard_young_tableaux, seminormal_matrix
from hoefsmit_witness import load_witness


def nuclear_ordering(Z, N):
    """Interleaved p/n ordering matching symbolic_k6_characters."""
    ordering = []
    pc = nc = 0
    for k in range(Z + N):
        if (k % 2 == 0 and pc < Z) or nc >= N:
            ordering.append(1)  # proton
            pc += 1
        else:
            ordering.append(0)  # neutron
            nc += 1
    return ordering


def crossing_cd(ti, tj):
    """(c, d) for crossing between nucleons of type ti, tj."""
    if ti == 1 and tj == 1:
        return 1.0, 0.0          # pp: σ
    if ti == 0 and tj == 0:
        return 1.0, -HA           # nn: σ⁻¹ = σ - h
    return 1.0, -HA / 2           # pn: ½(σ+σ⁻¹) = σ - h/2


def chi_inter_nucleon(shape, Z, N, n_gens):
    """χ_λ on inter-nucleon crossing chain.

    Chain: Π_{0≤i<j<A} (σ_g + d_ij·I) with g = (i+j) mod n_gens.
    """
    A = Z + N
    if A <= 1:
        tabs = standard_young_tableaux(shape)
        return float(len(tabs))

    tabs = standard_young_tableaux(shape)
    d = len(tabs)
    if d == 0:
        return 0.0

    sigmas = [seminormal_matrix(shape, g) for g in range(n_gens)]
    I = np.eye(d)
    M = np.eye(d)
    ordering = nuclear_ordering(Z, N)

    for i in range(A - 1):
        for j in range(i + 1, A):
            c, shift = crossing_cd(ordering[i], ordering[j])
            g = (i + j) % n_gens
            M = M @ (c * sigmas[g] + shift * I)

    return float(np.trace(M))


def main():
    k = 6
    n_gens = k - 1
    witness = load_witness()
    level = witness['levels'].get(str(k), [])

    # Test nuclei — small, where characters are exactly tractable
    nuclei = [
        ('D',    1, 1),
        ('3H',   1, 2),
        ('3He',  2, 1),
        ('4He',  2, 2),
        ('6Li',  3, 3),  # A=6, tests balanced
        ('7Li',  3, 4),
        ('8Be',  4, 4),
        ('12C',  6, 6),
    ]

    print(f"{'='*88}")
    print(f"k=6 PER-PARTITION MARKOV CONTRIBUTION  m_λ(Z,N) = w_λ · χ_λ / dim · m_e [MeV]")
    print(f"{'='*88}")
    print(f"q₀ = {q0:.10f}, h = {HA:.6f}, m_e = {M_E_MEV:.6f} MeV\n")

    # Per-partition characters
    partitions = [tuple(e['shape']) for e in level]
    p_info = {tuple(e['shape']): (e['dim'], e['w']) for e in level}

    chi_table = {}   # (shape, name) → χ
    m_table = {}     # (shape, name) → m_λ in MeV
    for shape in partitions:
        dim, w = p_info[shape]
        for name, Z, N in nuclei:
            chi = chi_inter_nucleon(shape, Z, N, n_gens)
            chi_table[(shape, name)] = chi
            m_table[(shape, name)] = w * chi / dim * M_E_MEV

    # Print table of m_λ
    print(f"{'λ':>12s} {'dim':>4s} {'w_λ':>10s}", end="")
    for name, _, _ in nuclei:
        print(f" {name:>10s}", end="")
    print()
    print("-" * (28 + 11 * len(nuclei)))

    for shape in partitions:
        dim, w = p_info[shape]
        print(f"{str(shape):>12s} {dim:>4d} {w:>10.6f}", end="")
        for name, Z, N in nuclei:
            m = m_table[(shape, name)]
            print(f" {m*1e3:>10.4f}", end="")  # keV
        print()

    print("\n(values in keV; positive = binding contribution)\n")

    # ── First-order approximations (current hecke_core.py) ────────
    print(f"{'='*88}")
    print("COMPARE EXACT vs FIRST-ORDER APPROXIMATIONS (groups used in hecke_core.py)")
    print(f"{'='*88}\n")

    # Groups used at k=6:
    # A: [3,2,1]            → DELTA_W2  × Z*N / A^{4/3}
    # B: [4,1,1]+[3,1,1,1]  → DELTA_411 × (N-Z)²/(4 A^{4/3})
    # C: [4,2]+[2,2,1,1]    → DELTA_42  × Z(Z-1)/A^{4/3}
    # D: remaining 5 partitions: [(6), (5,1), (3,3), (2,2,2), (2,1,1,1,1), (1,1,1,1,1,1)]
    #    — currently NOT accounted for in hecke_core.py!

    groups = {
        'A [321]': [(3,2,1)],
        'B [411]+[3111]': [(4,1,1), (3,1,1,1)],
        'C [42]+[2211]': [(4,2), (2,2,1,1)],
        'D_rem': [(6,), (5,1), (3,3), (2,2,2), (2,1,1,1,1), (1,1,1,1,1,1)],
    }

    print(f"{'nucleus':>8s}  {'A [321]':>12s} {'B [411]+[3111]':>15s} "
          f"{'C [42]+[2211]':>15s} {'D remaining 5':>15s} {'total k=6':>12s}")
    print("-" * 84)
    for name, Z, N in nuclei:
        A = Z + N
        totals = {g: sum(m_table[(s, name)] for s in shapes)
                  for g, shapes in groups.items()}
        total = sum(totals.values())
        print(f"{name:>8s}  {totals['A [321]']*1e3:>12.4f} "
              f"{totals['B [411]+[3111]']*1e3:>15.4f} "
              f"{totals['C [42]+[2211]']*1e3:>15.4f} "
              f"{totals['D_rem']*1e3:>15.4f} "
              f"{total*1e3:>12.4f}")

    print("\n(values in keV)\n")

    # ── Test first-order fit ─────────────────────────────────────
    print(f"{'='*88}")
    print("FIRST-ORDER FIT: y = C × f(Z,N,A)")
    print(f"{'='*88}\n")

    def first_order_fit(group_key, kernel):
        """kernel(Z,N,A) → expected first-order shape."""
        xs, ys = [], []
        for name, Z, N in nuclei:
            A = Z + N
            if A < 2:
                continue
            k_val = kernel(Z, N, A)
            if abs(k_val) < 1e-12:
                continue
            actual = sum(m_table[(s, name)] for s in groups[group_key])
            xs.append(k_val)
            ys.append(actual)
        if not xs:
            return None
        xs = np.array(xs); ys = np.array(ys)
        C = float(np.sum(xs*ys) / np.sum(xs*xs))
        residuals = ys - C * xs
        rel_res = residuals / (np.abs(ys) + 1e-12)
        print(f"Group {group_key}: kernel best-fit C = {C*1e3:.4f} keV")
        print(f"  nuclei: {[n for n,_,_ in nuclei]}")
        print(f"  exact  [keV]: {ys*1e3}")
        print(f"  fit    [keV]: {C*xs*1e3}")
        print(f"  resid  [keV]: {residuals*1e3}")
        print(f"  max rel res: {np.max(np.abs(rel_res))*100:.2f}%")
        return C, residuals

    print("Group A [3,2,1]  — current kernel Z*N / A^{4/3}:")
    first_order_fit('A [321]', lambda Z,N,A: Z*N / A**(4/3))

    print("\nGroup A [3,2,1]  — alt kernel (Z-N)*(A-1) / A^{4/3}:")
    first_order_fit('A [321]', lambda Z,N,A: (Z-N)*(A-1) / A**(4/3))

    print("\nGroup B [4,1,1]+[3,1,1,1]  — current kernel (N-Z)²/(4 A^{4/3}):")
    first_order_fit('B [411]+[3111]', lambda Z,N,A: (N-Z)**2 / (4*A**(4/3)))

    print("\nGroup C [4,2]+[2,2,1,1]  — current kernel Z(Z-1)/A^{4/3}:")
    first_order_fit('C [42]+[2211]', lambda Z,N,A: Z*(Z-1) / A**(4/3))

    # ── Two-parameter refinement: first order + cross term ───────
    print(f"\n{'='*88}")
    print("TWO-PARAMETER FIT: y = C₁ · f(Z,N,A) + C₂ · g(Z,N,A)")
    print(f"{'='*88}\n")

    def two_param_fit(group_key, f_kernel, g_kernel, f_name, g_name):
        xs_f, xs_g, ys = [], [], []
        for name, Z, N in nuclei:
            A = Z + N
            if A < 2:
                continue
            actual = sum(m_table[(s, name)] for s in groups[group_key])
            xs_f.append(f_kernel(Z, N, A))
            xs_g.append(g_kernel(Z, N, A))
            ys.append(actual)
        X = np.array([xs_f, xs_g]).T
        y = np.array(ys)
        coef, *_ = np.linalg.lstsq(X, y, rcond=None)
        C1, C2 = coef
        fit = X @ coef
        residuals = y - fit
        print(f"Group {group_key}:")
        print(f"  f = {f_name}, g = {g_name}")
        print(f"  C₁ = {C1*1e3:.6f} keV   C₂ = {C2*1e3:.6f} keV")
        print(f"  exact [keV]: {y*1e3}")
        print(f"  fit   [keV]: {fit*1e3}")
        print(f"  resid [keV]: {residuals*1e3}")
        print(f"  max |resid|: {np.max(np.abs(residuals))*1e3:.4f} keV")
        return C1, C2

    # For [3,2,1]: test if higher-order structure is ZN(Z+N)/A^{4/3}
    #   or an A-dependent correction
    print("Group A [3,2,1]: f=ZN/A^{4/3}, g=ZN(A-4)/A^{7/3}  (A-dependent)")
    two_param_fit('A [321]',
                  lambda Z,N,A: Z*N / A**(4/3),
                  lambda Z,N,A: Z*N*(A-4) / A**(7/3),
                  'ZN/A^{4/3}', 'ZN(A-4)/A^{7/3}')

    print("\nGroup A [3,2,1]: f=ZN/A^{4/3}, g=(N-Z)²/(4·A^{4/3})  (isospin cross)")
    two_param_fit('A [321]',
                  lambda Z,N,A: Z*N / A**(4/3),
                  lambda Z,N,A: (N-Z)**2 / (4 * A**(4/3)),
                  'ZN/A^{4/3}', '(N-Z)²/(4A^{4/3})')

    print("\nGroup B [4,1,1]+[3,1,1,1]: f=(N-Z)²/(4·A^{4/3}), g=Z·N/A^{4/3}")
    two_param_fit('B [411]+[3111]',
                  lambda Z,N,A: (N-Z)**2 / (4*A**(4/3)),
                  lambda Z,N,A: Z*N / A**(4/3),
                  '(N-Z)²/(4A^{4/3})', 'ZN/A^{4/3}')

    print("\nGroup C [4,2]+[2,2,1,1]: f=Z(Z-1)/A^{4/3}, g=N(N-1)/A^{4/3}")
    two_param_fit('C [42]+[2211]',
                  lambda Z,N,A: Z*(Z-1) / A**(4/3),
                  lambda Z,N,A: N*(N-1) / A**(4/3),
                  'Z(Z-1)/A^{4/3}', 'N(N-1)/A^{4/3}')

    print("\nDone.")


if __name__ == "__main__":
    main()
