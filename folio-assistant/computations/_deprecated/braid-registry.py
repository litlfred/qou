#!/usr/bin/env python3
"""
Nuclear braid registry: ground-state computation and witness generation.

For each nucleus N(p,n), computes:
  1. Ground-state ordering (minimum Φ_q over all braid representatives)
  2. Sign and log of the Markov trace (sign × exp(Φ_q))
  3. Generator volumes V̂_i at each position
  4. Negative generator positions
  5. Daughter trace and signed difference
  6. e(I)/e(R) at converting generator

Stores results in folio-assistant/computations/braid-registry/
as individual JSON witness files per nucleus.

Usage:
    python3 folio-assistant/computations/braid-registry.py

For A ≤ 14: exhaustive ground-state search over C(A,p) orderings.
For A > 14: Yang-Baxter optimization from alternating seed.
"""

import json
import math
import os
import sys
import time
from datetime import datetime, timezone
from itertools import combinations
from pathlib import Path

# ── Parameters (derived from q = 1.110, no free parameters) ─────

Q_VAL = 1.110
Q_INV = 1.0 / Q_VAL
Q_HALF = Q_VAL**0.5
Z_MARKOV = 1.0 / (Q_HALF + 1.0 / Q_HALF)
HA = Q_VAL - Q_INV
SKEIN_AMP = Q_HALF - 1.0 / Q_HALF
HBAR_Q = 1.0 - Q_INV
HBAR_Q2 = HBAR_Q**2
M_TOTAL = 12 * math.pi / HBAR_Q2  # bundle mass = 2π|χ|/ℏ_q²

REGISTRY_DIR = Path(__file__).parent / "braid-registry"


def crossing_coeffs(ti, tj):
    if ti == 1 and tj == 1: return 1.0, 0.0
    elif ti == 0 and tj == 0: return 1.0, -HA
    else: return 1.0, -HA / 2


def trace_sign_log_full(ordering):
    """Compute sign, log|tr|, and per-generator data for an ordering.

    Returns: (sign, log_abs, generators)
    where generators is a list of dicts with a_i, b_i, V̂_i, sign_i, log|V̂_i|.
    """
    A = len(ordering)
    sign = 1
    log_abs = 0.0
    generators = []

    for i in range(A - 1):
        a, b = 0.0, 1.0
        crossings = []
        for j in range(i + 1, A):
            c, d = crossing_coeffs(ordering[i], ordering[j])
            # Track the Hecke step sign
            ac = a * c
            step_sign = 1 if ac >= 0 else -1
            a, b = a * c * HA + a * d + b * c, a * c + b * d
            crossings.append({
                'j': j, 'type_i': ordering[i], 'type_j': ordering[j],
                'ac': ac, 'step_sign': step_sign,
            })

        v = Z_MARKOV * a + b
        v_sign = 1 if v >= 0 else -1
        if v < 0:
            sign *= -1

        log_v = math.log(abs(v)) if abs(v) > 1e-300 else -999
        log_abs += log_v

        generators.append({
            'i': i,
            'a': a, 'b': b,
            'V_hat': v,
            'sign': v_sign,
            'log_abs_V': log_v,
            'n_crossings': len(crossings),
        })

    return sign, log_abs, generators


def find_ground_state(p, n, max_orderings=10000):
    """Find the minimum-Φ_q ordering for N(p,n).

    For C(A,p) ≤ max_orderings: exhaustive search.
    Otherwise: Yang-Baxter optimization from alternating seed.
    """
    A = p + n
    n_total = math.comb(A, p)

    if n_total <= max_orderings:
        # Exhaustive
        best_phi = float('inf')
        best_ordering = None
        for positions in combinations(range(A), p):
            ordering = [0] * A
            for pos in positions:
                ordering[pos] = 1
            s, phi, _ = trace_sign_log_full(ordering)
            if phi < best_phi:
                best_phi = phi
                best_ordering = list(ordering)
        return best_ordering, best_phi, 'exhaustive', n_total

    # Yang-Baxter optimization from alternating seed
    ordering = _alternating_ordering(p, n)
    best_phi = trace_sign_log_full(ordering)[1]
    improved = True
    yb_steps = 0

    while improved:
        improved = False
        for i in range(A - 1):
            # Try swapping adjacent nucleons (a Yang-Baxter move)
            if ordering[i] != ordering[i + 1]:
                ordering[i], ordering[i + 1] = ordering[i + 1], ordering[i]
                _, phi, _ = trace_sign_log_full(ordering)
                if phi < best_phi:
                    best_phi = phi
                    improved = True
                    yb_steps += 1
                else:
                    ordering[i], ordering[i + 1] = ordering[i + 1], ordering[i]

    return list(ordering), best_phi, f'yb-optimized({yb_steps})', n_total


def _alternating_ordering(p, n):
    A = p + n
    ordering = []
    pi, ni = 0, 0
    for k in range(A):
        if pi < p and (ni >= n or k % 2 == 0):
            ordering.append(1); pi += 1
        else:
            ordering.append(0); ni += 1
    return ordering


def compute_nucleus_witness(name, p, n, Q_exp=None, t_obs=None, t_unit=None):
    """Full witness computation for one nucleus."""
    A = p + n
    t0 = time.time()

    print(f"  {name}: N({p},{n}), A={A}...", end=" ", flush=True)

    # Ground state — parent
    ord_par, phi_par, method_par, n_searched = find_ground_state(p, n)
    sign_par, log_par, gens_par = trace_sign_log_full(ord_par)

    # Ground state — daughter (skip if n < 1)
    if n < 1:
        ord_dau = None
        phi_dau = None
        method_dau = 'none'
    else:
        ord_dau, phi_dau, method_dau, _ = find_ground_state(p + 1, n - 1)
    if ord_dau is not None:
        sign_dau, log_dau, gens_dau = trace_sign_log_full(ord_dau)
    else:
        sign_dau, log_dau, gens_dau = 0, 0, []

    # Negative generators
    neg_par = [g['i'] for g in gens_par if g['sign'] < 0]
    neg_dau = [g['i'] for g in gens_dau if g['sign'] < 0] if gens_dau else []

    # Sign structure and transition data (only if daughter exists)
    if ord_dau is not None:
        same_sign = (sign_par == sign_dau)
        delta_phi = log_par - log_dau

        phi_max = max(log_par, log_dau)
        phi_min = min(log_par, log_dau)
        if same_sign:
            intensive_delta = abs(1 - math.exp(phi_min - phi_max))
        else:
            intensive_delta = 1 + math.exp(phi_min - phi_max)

        conv = -1
        for k in range(A):
            if ord_par[k] == 0 and ord_dau[k] == 1:
                conv = k
                break

        eIeR = None
        if conv >= 0 and conv < len(gens_par) and conv < len(gens_dau):
            Vp = gens_par[conv]['V_hat']
            _, _, gens_dau_recomp = trace_sign_log_full(ord_dau)
            if conv < len(gens_dau_recomp):
                Vd = gens_dau_recomp[conv]['V_hat']
                if abs(Vp) > 1e-30:
                    eIeR = abs(Vp - Vd) / abs(Vp)
    else:
        same_sign = None
        delta_phi = None
        intensive_delta = None
        conv = -1
        eIeR = None

    elapsed = time.time() - t0
    print(f"{elapsed:.1f}s ({method_par})")

    witness = {
        'nucleus': name,
        'p': p, 'n': n, 'A': A,
        'q': Q_VAL,
        'timestamp': datetime.now(timezone.utc).isoformat(),

        'parent': {
            'ordering': ord_par,
            'ordering_visual': ''.join('●' if x else '○' for x in ord_par),
            'sign': sign_par,
            'log_trace': log_par,
            'trace_numerical': sign_par * math.exp(log_par) if abs(log_par) < 700 else None,
            'n_negative_generators': len(neg_par),
            'negative_generator_positions': neg_par,
            'ground_state_method': method_par,
            'n_orderings_searched': n_searched,
            'generator_volumes': [
                {'i': g['i'], 'V_hat': g['V_hat'], 'sign': g['sign'],
                 'log_abs': g['log_abs_V'], 'n_crossings': g['n_crossings']}
                for g in gens_par
            ],
        },

        'daughter': {
            'p': p + 1, 'n': n - 1,
            'ordering': ord_dau,
            'ordering_visual': ''.join('●' if x else '○' for x in ord_dau) if ord_dau else None,
            'sign': sign_dau if ord_dau else None,
            'log_trace': log_dau if ord_dau else None,
            'trace_numerical': sign_dau * math.exp(log_dau) if ord_dau and abs(log_dau) < 700 else None,
            'n_negative_generators': len(neg_dau),
            'negative_generator_positions': neg_dau,
            'ground_state_method': method_dau,
        } if n >= 1 else None,

        'transition': {
            'same_sign': same_sign,
            'delta_phi': delta_phi,
            'intensive_delta_tr': intensive_delta,
            'converting_position': conv,
            'eIeR': eIeR,
        },

        'experimental': {
            'Q_exp_MeV': Q_exp,
            't_obs': t_obs,
            't_unit': t_unit,
        },

        'computation': {
            'elapsed_s': elapsed,
            'engine': 'braid-registry.py',
            'factored_trace_theorem': 'thm:markov-trace-factorization',
            'parameters': {
                'z_markov': Z_MARKOV,
                'ha': HA,
                'hbar_q2': HBAR_Q2,
                'M_total_MeV': M_TOTAL,
            },
        },
    }

    return witness


def main():
    REGISTRY_DIR.mkdir(parents=True, exist_ok=True)

    # Load nuclide list if available, otherwise use defaults
    nuclide_list_path = Path(__file__).parent / 'nuclide-list.json'
    if nuclide_list_path.exists():
        with open(nuclide_list_path) as f:
            nuclide_data = json.load(f)
        nuclei = [(d['name'], d['p'], d['n'], None, None, None) for d in nuclide_data]
        # Override with known experimental Q values
        q_exp_data = {
            'H-3': (0.01861, 12.32, 'yr'),
            'C-14': (0.156, 5730, 'yr'),
            'Co-60': (0.318, 5.2714, 'yr'),
            'Sr-90': (0.546, 28.79, 'yr'),
            'Cs-137': (0.514, 30.17, 'yr'),
            'Bi-210': (1.163, 5.012, 'd'),
        }
        nuclei = [(name, p, n, *q_exp_data.get(name, (None, None, None)))
                   for name, p, n, _, _, _ in nuclei]
    else:
        nuclei = [
            ('H-3',   1,   2, 0.01861, 12.32,   'yr'),
            ('He-3',  2,   1, None,    None,     None),
            ('He-4',  2,   2, None,    None,     None),
            ('Li-6',  3,   3, None,    None,     None),
            ('C-12',  6,   6, None,    None,     None),
            ('C-14',  6,   8, 0.156,   5730,     'yr'),
            ('N-14',  7,   7, None,    None,     None),
            ('Co-60', 27, 33, 0.318,   5.2714,   'yr'),
            ('Sr-90', 38, 52, 0.546,   28.79,    'yr'),
            ('Cs-137',55, 82, 0.514,   30.17,    'yr'),
            ('Bi-210',83,127, 1.163,   5.012,    'd'),
        ]

    print(f"Nuclear braid registry — generating witnesses")
    print(f"Output: {REGISTRY_DIR}/")
    print()

    for name, p, n, Q_exp, t_obs, t_unit in nuclei:
        witness = compute_nucleus_witness(name, p, n, Q_exp, t_obs, t_unit)

        # Write witness file
        filename = f"{name.lower()}.json"
        filepath = REGISTRY_DIR / filename
        with open(filepath, 'w') as f:
            json.dump(witness, f, indent=2, default=str)

    # Write index
    index = {
        'registry': 'nuclear-braid-registry',
        'description': 'Ground-state braid orderings and Markov traces for all nuclei',
        'timestamp': datetime.now(timezone.utc).isoformat(),
        'q': Q_VAL,
        'nuclei': [name for name, *_ in nuclei],
        'files': {name.lower(): f"{name.lower()}.json" for name, *_ in nuclei},
    }
    with open(REGISTRY_DIR / 'index.json', 'w') as f:
        json.dump(index, f, indent=2)

    print()
    print(f"Registry: {len(nuclei)} nuclei written to {REGISTRY_DIR}/")


if __name__ == '__main__':
    main()
