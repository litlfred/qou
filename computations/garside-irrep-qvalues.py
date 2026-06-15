#!/usr/bin/env python3
"""
Per-irrep Garside Q-values at the QUARK level.

Key difference from vertex-volume approach: instead of factoring the
Markov trace into per-generator vertex volumes (which loses non-local
correlations), compute the FULL Garside product in each irrep.

For quark-level H_{3A}(q), the Garside element Δ has C(3A,2) crossings.
Each crossing is typed by quark flavors: d(u,u)=0, d(d,d)=-h, d(u,d)=-h/2.

The irrep trace tr(ρ_λ(Δ)) captures the full non-local product.
Changing one quark d→u affects ALL crossing matrices involving that quark,
not just O(1) vertex volumes.

For 2-letter quark alphabet {u,d}, Schur-Weyl duality restricts to
2-row partitions (k, n-k), reducing the number of irreps from p(n) to
floor(n/2)+1.

Fluid dynamics connection:
  - tr(ρ_λ(Δ)) = partition function in channel λ
  - Each irrep = flow pattern (symmetric, antisymmetric, mixed)
  - Narrower vortex tubes → smaller partition function in that channel
  - Q = |Σ_λ w_λ × Δtr_λ| × energy_scale

Usage:
    cd folio-assistant/computations && python3 garside-irrep-qvalues.py
"""

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import math
import json
import sys
import time
import numpy as np
from mpmath import mp
from datetime import datetime, timezone
from pathlib import Path
from itertools import combinations

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q as q0, Q_INV as qi0, HA as h_val, LN_Q
from experimental_constants import M_E_MEV, Q_TRITIUM_MEV, Q_NEUTRON_MEV
from partition_utils import hook_lengths  # noqa: E402

z = 1.0 / (q0**0.5 + q0**(-0.5))


# ══════════════════════════════════════════════════════════════
#  YOUNG TABLEAUX AND SEMINORMAL FORM
# ══════════════════════════════════════════════════════════════

def standard_young_tableaux(partition):
    """Generate all standard Young tableaux for a partition."""
    n = sum(partition)
    rows = len(partition)

    def fill(tableau, remaining, row_lengths):
        if not remaining:
            yield [row[:] for row in tableau]
            return
        val = n - len(remaining) + 1
        for r in range(rows):
            if row_lengths[r] < partition[r]:
                if r > 0 and row_lengths[r] >= row_lengths[r-1]:
                    continue
                tableau[r].append(val)
                new_remaining = remaining[1:]
                new_lengths = row_lengths[:]
                new_lengths[r] += 1
                yield from fill(tableau, new_remaining, new_lengths)
                tableau[r].pop()

    initial = [[] for _ in range(rows)]
    yield from fill(initial, list(range(1, n+1)), [0]*rows)


def content(tableau, val):
    """Content of box containing val: column - row."""
    for r, row in enumerate(tableau):
        for c, v in enumerate(row):
            if v == val:
                return c - r
    raise ValueError(f"{val} not in tableau")


def axial_distance(tableau, k):
    """Axial distance for (k, k+1): content(k+1) - content(k)."""
    return content(tableau, k+1) - content(tableau, k)


def swap_in_tableau(tableau, k):
    """Return tableau with k and k+1 swapped, or None if not standard."""
    new_tab = [row[:] for row in tableau]
    pos_k = pos_k1 = None
    for r, row in enumerate(new_tab):
        for c, v in enumerate(row):
            if v == k: pos_k = (r, c)
            if v == k+1: pos_k1 = (r, c)
    if pos_k is None or pos_k1 is None:
        return None
    new_tab[pos_k[0]][pos_k[1]] = k+1
    new_tab[pos_k1[0]][pos_k1[1]] = k
    for r, row in enumerate(new_tab):
        for c in range(len(row)-1):
            if row[c] >= row[c+1]: return None
        if r > 0:
            for c in range(min(len(new_tab[r]), len(new_tab[r-1]))):
                if new_tab[r][c] <= new_tab[r-1][c]: return None
    return new_tab


def seminormal_generator_matrix(tableaux, tab_to_idx, gen_idx, q_val):
    """Matrix of σ_{gen_idx} in Young's seminormal form.

    gen_idx is 0-based: σ_0 transposes positions 1 and 2.
    """
    dim = len(tableaux)
    qq = q_val
    qi = 1.0 / qq
    ha = qq - qi
    k = gen_idx + 1  # transposing values k and k+1

    # dtype=object preserves mpmath scalars in matrix entries (the
    # off-diagonal sqrt fills below need substrate precision; default
    # float64 dtype would silently coerce — Copilot #2050).
    mat = np.zeros((dim, dim), dtype=object)

    for i, T in enumerate(tableaux):
        d = axial_distance(T, k)
        if d == 0:
            raise ValueError(f"d=0 for tableau {T}, k={k}")

        if abs(d) == 1:
            mat[i, i] = qq if d == 1 else -qi
        else:
            qd = qq**d
            qdi = qq**(-d)
            denom = qd - qdi
            diag = ha / denom
            mat[i, i] = diag

            T_swapped = swap_in_tableau(T, k)
            if T_swapped is not None:
                key = tuple(tuple(row) for row in T_swapped)
                if key in tab_to_idx:
                    j = tab_to_idx[key]
                    off_diag_sq = 1.0 - diag**2
                    # Keep mp.mpf precision in the matrix entries —
                    # MUST be a dtype=object numpy array (per Copilot
                    # #2050) otherwise float64 dtype silently coerces.
                    # The caller now allocates with dtype=object.
                    if off_diag_sq > 0:
                        mat[i, j] = mp.sqrt(off_diag_sq)
                    else:
                        mat[i, j] = -mp.sqrt(-off_diag_sq)

    return mat


# ══════════════════════════════════════════════════════════════
#  TYPED CROSSING COEFFICIENT
# ══════════════════════════════════════════════════════════════

def typed_d(fi, fj):
    """Crossing coefficient d(f_i, f_j)."""
    if fi == 'u' and fj == 'u':
        return 0.0
    elif fi == 'd' and fj == 'd':
        return -h_val
    else:
        return -h_val / 2


# ══════════════════════════════════════════════════════════════
#  FULL GARSIDE PRODUCT IN ONE IRREP
# ══════════════════════════════════════════════════════════════

def garside_trace_irrep(quark_ordering, partition, q_val):
    """Compute tr(ρ_λ(Δ_A)) for the FULL Garside product.

    The Garside staircase Δ_n = (σ_1)(σ_2 σ_1)(σ_3 σ_2 σ_1)...
    Each crossing is typed: C(f_i, f_j; σ_k) = ρ(σ_k) + d(f_i,f_j)×I.

    Right-to-left sweep: for level L from 1 to n-1, sweep k from L-1 down to 0.
    At each step, quark[k] crosses quark[L].

    Returns (trace, dim, matrix_if_small).
    """
    n = len(quark_ordering)
    assert n == sum(partition)

    tableaux = list(standard_young_tableaux(partition))
    dim = len(tableaux)

    if dim == 0:
        return 0.0, 0, None

    tab_to_idx = {}
    for i, t in enumerate(tableaux):
        key = tuple(tuple(row) for row in t)
        tab_to_idx[key] = i

    # Precompute generator matrices
    gen_matrices = {}
    for k in range(n - 1):
        gen_matrices[k] = seminormal_generator_matrix(
            tableaux, tab_to_idx, k, q_val)

    # Build the FULL Garside product
    result = np.eye(dim)

    # Garside staircase: right-to-left sweep
    # Level L: for k from L-1 down to 0, crossing σ_k between quarks[k] and quarks[L]
    for L in range(1, n):
        for k in range(L - 1, -1, -1):
            d_coeff = typed_d(quark_ordering[k], quark_ordering[L])
            crossing = gen_matrices[k] + d_coeff * np.eye(dim)
            result = result @ crossing

    tr_val = np.trace(result).real
    return tr_val, dim, result


# ══════════════════════════════════════════════════════════════
#  TWO-ROW PARTITIONS (SCHUR-WEYL REDUCTION)
# ══════════════════════════════════════════════════════════════

def two_row_partitions(n):
    """Generate 2-row partitions of n: (k, n-k) for k >= ceil(n/2)."""
    parts = []
    for k in range(n, (n-1)//2, -1):
        m = n - k
        if m == 0:
            parts.append((n,))
        else:
            parts.append((k, m))
    return parts


def hook_length_dim(partition):
    """Dimension of irrep via hook-length formula."""
    n = sum(partition)
    dim = math.factorial(n)
    for h in hook_lengths(partition):
        dim //= h
    return dim


# ══════════════════════════════════════════════════════════════
#  QUARK ORDERINGS
# ══════════════════════════════════════════════════════════════

def nucleus_quark_ordering(Z, N):
    """Standard quark ordering: Z protons (uud) then N neutrons (udd)."""
    quarks = []
    for _ in range(Z):
        quarks.extend(['u', 'u', 'd'])
    for _ in range(N):
        quarks.extend(['u', 'd', 'd'])
    return quarks


def all_nucleon_permutations(Z, N):
    """Generate all nucleon permutations as quark orderings."""
    A = Z + N
    for proton_positions in combinations(range(A), Z):
        quarks = []
        for i in range(A):
            if i in proton_positions:
                quarks.extend(['u', 'u', 'd'])
            else:
                quarks.extend(['u', 'd', 'd'])
        yield quarks


# ══════════════════════════════════════════════════════════════
#  GROUND STATE SEARCH (simplified: test all nucleon permutations)
# ══════════════════════════════════════════════════════════════

def find_ground_state_fast(Z, N):
    """Find ground state ordering using vertex-volume free energy.

    Uses the fast O(n²) vertex-volume computation as a proxy for
    the full per-irrep ground state search (which is too expensive
    for all orderings).
    """
    def vertex_vol(ordering, i):
        n = len(ordering)
        a, b = 0.0, 1.0
        for j in range(i + 1, n):
            d = typed_d(ordering[i], ordering[j])
            new_a = a * h_val + a * d + b
            new_b = a + b * d
            a, b = new_a, new_b
        return z * a + b

    def phi(ordering):
        n = len(ordering)
        total = 0.0
        for i in range(n - 1):
            V = vertex_vol(ordering, i)
            if abs(V) < 1e-300:
                return float('-inf')
            total += mp.log(abs(V))
        return total

    best_phi = float('-inf')
    best_ord = None
    for quarks in all_nucleon_permutations(Z, N):
        p = phi(quarks)
        if p > best_phi:
            best_phi = p
            best_ord = quarks

    return best_ord, best_phi


# ══════════════════════════════════════════════════════════════
#  MAIN COMPUTATION
# ══════════════════════════════════════════════════════════════

if __name__ == '__main__':
    print("PER-IRREP GARSIDE Q-VALUES (QUARK LEVEL)")
    print(f"  q₀ = {q0:.15f}")
    print(f"  h  = {h_val:.15f}")
    print(f"  z  = {z:.15f}")
    print(f"  m_e = {M_E_MEV} MeV")
    print("=" * 72)

    decays = [
        # (Z_par, N_par, Z_dau, N_dau, Q_exp, name)
        (0, 1, 1, 0, Q_NEUTRON_MEV,  'n→p'),
        (1, 2, 2, 1, Q_TRITIUM_MEV,  '³H→³He'),
        (2, 4, 3, 3, 3.508,          '⁶He→⁶Li'),
    ]

    all_results = []

    for Z_par, N_par, Z_dau, N_dau, Q_exp, name in decays:
        A = Z_par + N_par
        n_quarks = 3 * A
        n_crossings = n_quarks * (n_quarks - 1) // 2

        print(f"\n{'━' * 72}")
        print(f"  {name}  (A={A}, {3*A} quarks, {n_crossings} crossings)")
        print(f"{'━' * 72}")

        # Ground state orderings
        t0 = time.time()
        gs_par, phi_par = find_ground_state_fast(Z_par, N_par)
        gs_dau, phi_dau = find_ground_state_fast(Z_dau, N_dau)
        t_gs = time.time() - t0

        n_u_par = gs_par.count('u')
        n_d_par = gs_par.count('d')
        n_u_dau = gs_dau.count('u')
        n_d_dau = gs_dau.count('d')

        print(f"  Parent:   {''.join(gs_par)} ({n_u_par}u+{n_d_par}d)")
        print(f"  Daughter: {''.join(gs_dau)} ({n_u_dau}u+{n_d_dau}d)")
        print(f"  GS search: {t_gs:.2f}s")

        # Two-row partitions
        parts = two_row_partitions(n_quarks)
        print(f"\n  Two-row partitions of {n_quarks}: {len(parts)}")

        # Compute per-irrep traces
        irrep_results = []
        max_feasible_dim = 500  # skip partitions with dim > this (Python too slow)

        for part in parts:
            dim = hook_length_dim(part)
            if dim > max_feasible_dim:
                print(f"    λ={part}: dim={dim} — SKIPPING (dim > {max_feasible_dim})")
                irrep_results.append({
                    'partition': part, 'dim': dim,
                    'tr_par': None, 'tr_dau': None, 'skipped': True
                })
                continue

            t1 = time.time()
            tr_par, _, _ = garside_trace_irrep(gs_par, part, q0)
            tr_dau, _, _ = garside_trace_irrep(gs_dau, part, q0)
            elapsed = time.time() - t1

            weight = dim**2 / math.factorial(n_quarks)
            dtr = tr_dau - tr_par
            weighted_dtr = weight * dtr

            print(f"    λ={str(part):>10s}: dim={dim:>5d}, tr_par={tr_par:>+14.4f}, "
                  f"tr_dau={tr_dau:>+14.4f}, Δtr={dtr:>+14.4f}, "
                  f"w×Δtr={weighted_dtr:>+12.6f}  ({elapsed:.1f}s)")

            irrep_results.append({
                'partition': part, 'dim': dim,
                'tr_par': tr_par, 'tr_dau': tr_dau,
                'dtr': dtr, 'weight': weight, 'weighted_dtr': weighted_dtr,
                'skipped': False
            })

        # Sum over computed irreps
        computed = [r for r in irrep_results if not r['skipped']]
        skipped = [r for r in irrep_results if r['skipped']]

        sum_weighted_dtr = sum(r['weighted_dtr'] for r in computed)
        sum_dtr = sum(r['dtr'] for r in computed)
        sum_abs_weighted_dtr = sum(abs(r['weighted_dtr']) for r in computed)

        total_weight_computed = sum(r['weight'] for r in computed)
        total_weight_skipped = sum(r['dim']**2 / math.factorial(n_quarks)
                                   for r in skipped)

        print(f"\n  Computed irreps: {len(computed)}/{len(parts)}")
        print(f"  Weight coverage: {total_weight_computed:.4f} / {total_weight_computed + total_weight_skipped:.4f}")
        print(f"  Σ w_λ × Δtr_λ = {sum_weighted_dtr:+.8f}")
        print(f"  Σ Δtr_λ       = {sum_dtr:+.8f}")
        print(f"  Σ |w_λ × Δtr_λ| = {sum_abs_weighted_dtr:.8f}")

        # Test various Q-value formulas
        print(f"\n  Q-VALUE CANDIDATES:")

        candidates = [
            ('|Σ w Δtr| × m_e',
             abs(sum_weighted_dtr) * M_E_MEV),
            ('|Σ w Δtr| × h × m_e',
             abs(sum_weighted_dtr) * h_val * M_E_MEV),
            ('|Σ w Δtr| × z² × m_e',
             abs(sum_weighted_dtr) * z**2 * M_E_MEV),
            ('|Σ w Δtr| × ln(q) × m_e',
             abs(sum_weighted_dtr) * LN_Q * M_E_MEV),
            ('|Σ Δtr| × m_e / n!',
             abs(sum_dtr) * M_E_MEV / math.factorial(n_quarks)),
            ('|Σ Δtr| × ln(q) × m_e / n!',
             abs(sum_dtr) * LN_Q * M_E_MEV / math.factorial(n_quarks)),
            ('|Σ |w Δtr|| × ln(q) × m_e',
             sum_abs_weighted_dtr * LN_Q * M_E_MEV),
        ]

        for label, Q_calc in candidates:
            if Q_exp > 0 and Q_calc > 1e-30:
                err = (Q_calc / Q_exp - 1) * 100
                print(f"    {label:>35s} = {Q_calc:12.6f} MeV ({err:+.1f}%)")
            else:
                print(f"    {label:>35s} = {Q_calc:12.6f} MeV")

        print(f"    {'Q_exp':>35s} = {Q_exp:12.6f} MeV")

        all_results.append({
            'name': name, 'A': A, 'n_quarks': n_quarks,
            'Z_par': Z_par, 'N_par': N_par,
            'Z_dau': Z_dau, 'N_dau': N_dau,
            'Q_exp': Q_exp,
            'sum_weighted_dtr': sum_weighted_dtr,
            'sum_dtr': sum_dtr,
            'sum_abs_weighted_dtr': sum_abs_weighted_dtr,
            'weight_coverage': total_weight_computed / (total_weight_computed + total_weight_skipped)
                              if (total_weight_computed + total_weight_skipped) > 0 else 0,
            'irreps': [{
                'partition': list(r['partition']),
                'dim': r['dim'],
                'tr_par': r.get('tr_par'),
                'tr_dau': r.get('tr_dau'),
                'skipped': r['skipped'],
            } for r in irrep_results],
        })

    # Summary
    print("\n" + "=" * 72)
    print("  SUMMARY")
    print("=" * 72)
    print(f"\n  {'Decay':>12s} | {'nq':>4s} | {'coverage':>8s} | {'Σ w×Δtr':>12s} | {'Q_exp':>10s}")
    print(f"  {'':->55s}")
    for r in all_results:
        print(f"  {r['name']:>12s} | {r['n_quarks']:>4d} | {r['weight_coverage']:>7.1%} | "
              f"{r['sum_weighted_dtr']:>+12.4f} | {r['Q_exp']:>10.6f}")

    # Write witness
    witness = {
        'title': 'Per-irrep Garside Q-values (quark level, 2-row)',
        'parameters': {'q': q0, 'h': h_val, 'z': z, 'm_e_MeV': M_E_MEV},
        'decays': all_results,
        'timestamp': datetime.now(timezone.utc).isoformat(),
    }

    witness_path = Path(__file__).parent / 'garside-irrep-qvalues.witness.json'
    with open(witness_path, 'w') as f:
        json.dump(witness, f, indent=2, default=str)
    print(f"\nWitness: {witness_path.name}")
