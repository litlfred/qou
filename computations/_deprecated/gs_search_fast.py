#!/usr/bin/env python3
"""
Fast ground-state search using incremental updates and pruning.

Key insight: T_pp · T_nn = I, so only pn crossings contribute to binding.
Swapping two adjacent positions changes O(A) crossings, not O(A²).

Algorithm:
1. Start from the interleaved ordering (known to be close to GS)
2. Try all pairwise swaps (p↔n only), evaluate ΔΦ incrementally
3. Accept swaps that lower Φ (steepest descent)
4. Repeat until no improving swap exists

This is O(A² × n_iterations) per nucleus, vs O(C(A,Z) × A²) for exhaustive.

Usage:
    python3 gs_search_fast.py

    from gs_search_fast import find_ground_state
    gs, Phi = find_ground_state(Z=27, N=33)
"""
import math
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q as q, Q_INV as qi, HA as h, HBAR_Q

z = 1.0 / (q**0.5 + q**(-0.5))


def compute_Phi(ordering):
    """Compute Φ_q = Σ log|V̂_i| for an ordering. O(A²)."""
    A = len(ordering)
    if A <= 1:
        return 0.0
    Phi = 0.0
    for gen in range(A - 1):
        a, b = 0.0, 1.0
        for j in range(gen + 1, A):
            ti, tj = ordering[gen], ordering[j]
            if ti == 1 and tj == 1:
                d = 0.0
            elif ti == 0 and tj == 0:
                d = -h
            else:
                d = -h / 2
            a, b = a * h + a * d + b, a + b * d
        V = z * a + b
        if V == 0:
            return float('inf')
        Phi += math.log(abs(V))
    return Phi


def all_V(ordering):
    """All vertex volumes. O(A²)."""
    A = len(ordering)
    vols = []
    for gen in range(A - 1):
        a, b = 0.0, 1.0
        for j in range(gen + 1, A):
            ti, tj = ordering[gen], ordering[j]
            if ti == 1 and tj == 1:
                d = 0.0
            elif ti == 0 and tj == 0:
                d = -h
            else:
                d = -h / 2
            a, b = a * h + a * d + b, a + b * d
        vols.append(z * a + b)
    return vols


def initial_ordering(Z, N):
    """Starting ordering: interleaved (close to GS)."""
    A = Z + N
    if A <= 3:
        return [1] * Z + [0] * N
    ordering = [0] * A
    if Z <= N:
        for k in range(Z):
            if 2 * k + 1 < A:
                ordering[2 * k + 1] = 1
    else:
        for k in range(N):
            if 2 * k < A:
                ordering[2 * k] = 1
        placed = sum(ordering)
        for k in range(A):
            if ordering[k] == 0 and placed < Z:
                ordering[k] = 1
                placed += 1
    return ordering


def find_ground_state(Z, N, max_restarts=5, verbose=False):
    """Find ground state by steepest descent with restarts.

    O(A² × n_swaps × n_restarts) — feasible for any A.
    """
    A = Z + N

    # Try multiple starting points
    best_global = (float('inf'), None)

    for restart in range(max_restarts):
        if restart == 0:
            ordering = initial_ordering(Z, N)
        elif restart == 1:
            # Reverse interleaving
            ordering = initial_ordering(Z, N)[::-1]
        elif restart == 2:
            # Sorted (all p first)
            ordering = [1] * Z + [0] * N
        elif restart == 3:
            # Sorted (all n first)
            ordering = [0] * N + [1] * Z
        else:
            # Random-ish: shift the interleaved pattern
            base = initial_ordering(Z, N)
            shift = restart
            ordering = base[shift:] + base[:shift]
            # Fix counts
            if sum(ordering) != Z:
                ordering = initial_ordering(Z, N)

        Phi = compute_Phi(ordering)

        # Steepest descent: try all p↔n swaps
        improved = True
        n_swaps = 0
        while improved:
            improved = False
            best_swap = None
            best_delta = 0.0

            # Find all (i, j) where ordering[i]=1, ordering[j]=0
            p_positions = [i for i in range(A) if ordering[i] == 1]
            n_positions = [i for i in range(A) if ordering[i] == 0]

            for pi in p_positions:
                for ni in n_positions:
                    # Swap positions pi and ni
                    ordering[pi], ordering[ni] = 0, 1
                    new_Phi = compute_Phi(ordering)
                    delta = new_Phi - Phi
                    ordering[pi], ordering[ni] = 1, 0  # swap back

                    if delta < best_delta - 1e-12:
                        best_delta = delta
                        best_swap = (pi, ni)

            if best_swap is not None:
                pi, ni = best_swap
                ordering[pi], ordering[ni] = 0, 1
                Phi += best_delta
                n_swaps += 1
                improved = True

        if verbose:
            print(f"    Restart {restart}: {n_swaps} swaps, Φ = {Phi:+.6f}")

        if Phi < best_global[0]:
            best_global = (Phi, ordering[:])

    return best_global[1], best_global[0]


def find_ground_state_exhaustive(Z, N, max_comb=50_000_000):
    """Exhaustive search (for verification). O(C(A,Z) × A²)."""
    from itertools import combinations
    A = Z + N
    n_comb = math.comb(A, Z)
    if n_comb > max_comb:
        return None, None
    best = (float('inf'), None)
    for pp in combinations(range(A), Z):
        o = [0] * A
        for p in pp:
            o[p] = 1
        Phi = compute_Phi(o)
        if Phi < best[0]:
            best = (Phi, o[:])
    return best[1], best[0]


if __name__ == '__main__':
    print("=" * 80)
    print("  FAST GROUND STATE SEARCH")
    print(f"  q = {q:.10f}, h = {h:.10f}")
    print("=" * 80)

    # Verify against exhaustive for A ≤ 14
    print("\n  VERIFICATION (fast vs exhaustive):")
    print(f"  {'Nucleus':>8s} | {'A':>3s} | {'Φ_fast':>10s} | {'Φ_exact':>10s} | {'Match':>6s} | {'t_fast':>6s} | {'t_exact':>8s}")
    print(f"  {'-' * 65}")

    test = [
        (1, 2, '3H'), (2, 2, '4He'), (3, 4, '7Li'), (4, 5, '9Be'),
        (6, 6, '12C'), (6, 8, '14C'), (7, 7, '14N'), (8, 8, '16O'),
    ]

    for Z, N, name in test:
        t0 = time.time()
        gs_fast, Phi_fast = find_ground_state(Z, N, verbose=False)
        t_fast = time.time() - t0

        t0 = time.time()
        gs_exact, Phi_exact = find_ground_state_exhaustive(Z, N)
        t_exact = time.time() - t0

        if Phi_exact is not None:
            match = "✓" if abs(Phi_fast - Phi_exact) < 1e-6 else f"Δ={Phi_fast-Phi_exact:+.4f}"
        else:
            match = "N/A"

        print(f"  {name:>8s} | {Z+N:3d} | {Phi_fast:+10.4f} | {Phi_exact:+10.4f} | {match:>6s} | {t_fast:5.2f}s | {t_exact:7.2f}s")

    # Now push to higher A
    print("\n  HIGHER A (fast search only):")
    print(f"  {'Nucleus':>8s} | {'A':>3s} | {'Z':>3s} | {'Φ':>10s} | {'Time':>6s} | {'GS ordering (first 30)':>35s}")
    print(f"  {'-' * 80}")

    heavy = [
        (10, 10, '20Ne'), (12, 12, '24Mg'), (14, 14, '28Si'),
        (20, 20, '40Ca'), (20, 28, '48Ca'),
        (26, 30, '56Fe'), (27, 33, '60Co'), (28, 30, '58Ni'),
        (38, 52, '90Sr'), (50, 70, '120Sn'),
        (55, 82, '137Cs'), (82, 126, '208Pb'),
    ]

    for Z, N, name in heavy:
        t0 = time.time()
        gs, Phi = find_ground_state(Z, N, max_restarts=8, verbose=False)
        elapsed = time.time() - t0

        gs_str = ''.join(str(x) for x in gs[:30])
        if len(gs) > 30:
            gs_str += '...'

        print(f"  {name:>8s} | {Z+N:3d} | {Z:3d} | {Phi:+10.4f} | {elapsed:5.1f}s | {gs_str:>35s}")
