#!/usr/bin/env python3
import sys
import time
import json
from pathlib import Path
import sympy as sp
from mpmath import mp, mpf

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from kazhdan_lusztig import permutations_S_n, kl_polynomial, canonical_basis_C_w
from rho_w_crystal_vertex_trace import atom_canonical_crossings, rho_lambda_of_word, partitions_of, standard_young_tableaux
from _precision import set_compute_dps, fmt

def rsk(w: tuple[int, ...]) -> tuple[list[list[int]], list[list[int]]]:
    """Robinson-Schensted-Knuth correspondence.
    Returns (P, Q) tableaux."""
    P = []
    Q = []
    for i, x in enumerate(w):
        r = 0
        while r < len(P):
            idx = -1
            for c in range(len(P[r])):
                if P[r][c] > x:
                    idx = c
                    break
            if idx == -1:
                P[r].append(x)
                Q[r].append(i + 1)
                break
            else:
                x, P[r][idx] = P[r][idx], x
                r += 1
        if r == len(P):
            P.append([x])
            Q.append([i + 1])
    return P, Q

def get_shape(P: list[list[int]]) -> tuple[int, ...]:
    return tuple(len(row) for row in P)

def syt_to_tuple(T: list[list[int]]) -> tuple[tuple[int, ...], ...]:
    return tuple(tuple(row) for row in T)

def canonical_Q(lam: tuple[int, ...]) -> tuple[tuple[int, ...], ...]:
    """Return the canonical (row-reading) standard Young tableau of shape lam."""
    Q = []
    counter = 1
    for r in lam:
        Q.append(tuple(range(counter, counter + r)))
        counter += r
    return tuple(Q)

def syt_depth(T_dict: dict[int, tuple[int, int]]) -> int:
    """Compute the depth of a SYT from the highest weight.
    For type A, the sum of row indices of the entries (0-indexed)."""
    return sum(r for (r, c) in T_dict.values())

def main():
    set_compute_dps()
    q = mpf("1.1099785955573347198997632204832250266562084087802")
    qi = mpf(1) / q

    print("=== PROBE 4 KL BATCH ===")
    n = 6
    word = atom_canonical_crossings(1, 1)  # Deuteron H_6
    print(f"n = {n}, |word| = {len(word)}")

    perms = permutations_S_n(n)
    print(f"Enumerating S_{n} ({len(perms)} permutations)...")
    
    # 1. Partition S_6 into left cells based on RSK Q-tableau.
    # We will pick the canonical left cell for each lambda.
    left_cells = {}
    for w in perms:
        P, Q = rsk(w)
        lam = get_shape(P)
        Q_tup = syt_to_tuple(Q)
        if lam not in left_cells:
            left_cells[lam] = {}
        if Q_tup not in left_cells[lam]:
            left_cells[lam][Q_tup] = []
        left_cells[lam][Q_tup].append(w)

    print("Computing Kazhdan-Lusztig Betti sums for canonical left cells...")
    # Pre-compute P_{e,w}(1) for the canonical left cell of each lambda
    betti_sums = {}
    for lam, cells in left_cells.items():
        Q_can = canonical_Q(lam)
        # If the canonical Q is not in the cells (it should be!), fallback to any cell.
        if Q_can not in cells:
            Q_can = list(cells.keys())[0]
        cell_w = cells[Q_can]
        
        sum_betti = 0
        for w in cell_w:
            p_poly = kl_polynomial(tuple(range(1, n+1)), w)
            betti = int(p_poly.subs({s: 1 for s in p_poly.free_symbols}))
            sum_betti += betti
        betti_sums[lam] = sum_betti
        print(f"  lambda={lam}, |cell|={len(cell_w)}, Betti sum={sum_betti}")

    # Compute crystal depths
    crystal_depths = {}
    for lam in partitions_of(n):
        syts = standard_young_tableaux(lam)
        s = sum(syt_depth(T) for T in syts)
        crystal_depths[lam] = s
    
    # Let's extract the C_w coefficients. For a left cell, there's a distinguished
    # involution (the longest element in some sense), but actually C_w itself is
    # the canonical basis element. 
    # Option 1 means: sum of the coefficients of T_x in C_w for w in the left cell?
    # Or just taking the dimension f^lam and verifying the magnitudes.

    # We will print the extracted magnitudes vs f^lambda = dim(V_lambda)
    print("\n=== Magnitude Checks ===")
    for lam in partitions_of(n):
        f_lam = len(standard_young_tableaux(lam))
        betti = betti_sums.get(lam, 0)
        depth = crystal_depths.get(lam, 0)
        print(f"lambda={str(lam):16s} f^lambda={f_lam:<3d} | Betti sum={betti:<4d} | Total Depth={depth:<4d}")

    print("\nResult:")
    print("If Betti sum or Depth equals f^lambda (or is proportional to it), it acts as the magnitude supplier.")
    print("Notice the relationship between the computed KL invariants and the required dim(V_lambda) magnitude.")

if __name__ == '__main__':
    main()
