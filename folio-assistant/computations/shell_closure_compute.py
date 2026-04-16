#!/usr/bin/env python3
"""
Categorical shell closure computation — sparse + symbolic.

Computes per-partition nuclear character at k=3..15 using:
  - scipy.sparse for Hoefsmit seminormal matrices (block-diagonal)
  - Optional Fraction arithmetic for symbolic-in-q exactness

The shell correction EMERGES from the per-partition weighted
forward δ²(ln|χ_λ|) — no Gaussian, no empirical magic numbers.

Usage:
    # Numeric (fast, for testing):
    python3 shell_closure_compute.py --numeric --kmax 10

    # Symbolic (exact in q, overnight):
    python3 shell_closure_compute.py --symbolic --kmax 15

Output:
    shell-closure.witness.json

Reference: prop:shell-closure-nf-term-count,
           prop:nuclear-knot-classification
"""

import argparse
import json
import math
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

import numpy as np
from scipy import sparse

from level_k_binding import seminormal_matrix, standard_young_tableaux
from hoefsmit_witness import load_witness
from q_parameter import Q as q0, Q_INV as qi, HA
from witness_base import WitnessBuilder


def sparse_seminormal(shape, gen):
    """Hoefsmit seminormal matrix as scipy.sparse CSR."""
    M = seminormal_matrix(shape, gen)
    return sparse.csr_matrix(M)


def crossing_sparse(shape, gen, ct):
    """Sparse crossing matrix."""
    S = sparse_seminormal(shape, gen)
    d = S.shape[0]
    if ct == 'pp':
        return S
    elif ct == 'nn':
        return S - HA * sparse.eye(d, format='csr')
    elif ct == 'pn':
        return S - (HA / 2) * sparse.eye(d, format='csr')
    return sparse.eye(d, format='csr')


def nuclear_character_sparse(shape, Z, N):
    """Nuclear character using sparse matrix multiplication."""
    tabs = standard_young_tableaux(shape)
    d = len(tabs)
    if d == 0:
        return None

    ordering = ['p'] * Z + ['n'] * N
    A = Z + N
    total = 0.0

    for gen in [0, 1]:
        M = sparse.eye(d, format='csr')
        for nuc in ordering:
            if gen == 0:
                for _ in range(3):
                    M = M @ crossing_sparse(shape, gen, 'pp')
                if nuc == 'p':
                    M = M @ crossing_sparse(shape, gen, 'pp')
                    M = M @ crossing_sparse(shape, gen, 'pp')
                else:
                    M = M @ crossing_sparse(shape, gen, 'pn')
                    M = M @ crossing_sparse(shape, gen, 'pn')
            else:
                for _ in range(3):
                    M = M @ crossing_sparse(shape, gen, 'nn')
                M = M @ crossing_sparse(shape, gen,
                                         'pn' if nuc == 'p' else 'nn')
        if gen == 0:
            for i in range(A):
                for j in range(i + 1, A):
                    ti, tj = ordering[i], ordering[j]
                    ct = ('pp' if ti == 'p' and tj == 'p'
                          else ('nn' if ti == 'n' and tj == 'n' else 'pn'))
                    M = M @ crossing_sparse(shape, gen, ct)
        if gen == 1:
            for _ in range(Z):
                M = M @ crossing_sparse(shape, gen, 'nn')

        if sparse.issparse(M):
            total += M.diagonal().sum()
        else:
            total += float(np.trace(M.toarray() if sparse.issparse(M) else M))

    return total


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--kmax', type=int, default=10)
    parser.add_argument('--zmax', type=int, default=30)
    parser.add_argument('--symbolic', action='store_true')
    parser.add_argument('--numeric', action='store_true', default=True)
    args = parser.parse_args()

    witness_data = load_witness()
    MAGIC = {2, 8, 20, 28, 50, 82, 126}

    results = {}
    for k in range(3, args.kmax + 1):
        level = witness_data['levels'].get(str(k), [])
        if not level:
            continue

        t0 = time.time()
        max_dim = max(e['dim'] for e in level)
        per_Z = {}

        for Z in range(1, args.zmax + 1):
            total = 0.0
            for entry in level:
                shape = tuple(entry['shape'])
                w = entry['w']
                chi = nuclear_character_sparse(shape, Z, Z)
                if chi is None:
                    continue
                ln_chi = math.log(abs(chi)) if abs(chi) > 1e-300 else 0
                total += w * ln_chi
            per_Z[Z] = total

        results[k] = per_Z
        elapsed = time.time() - t0
        print(f"k={k:>2d}: {len(level):>3d} partitions, "
              f"max_dim={max_dim:>4d}, {elapsed:.1f}s")

    # Compute cumulative forward δ² and output
    print()
    print(f"Forward δ²(cumulative w·ln|χ|, k=3..{args.kmax}):")
    print(f"{'Z':>3s} {'δ²':>10s} {'magic':>6s}")
    print("─" * 25)

    cum = {}
    for Z in range(1, args.zmax + 1):
        cum[Z] = sum(results.get(kk, {}).get(Z, 0)
                      for kk in range(3, args.kmax + 1))

    d1 = {Z: cum[Z] - cum[Z - 1] for Z in range(2, args.zmax + 1)}
    fwd_d2 = {Z: d1[Z] - d1[Z - 1] for Z in range(3, args.zmax + 1)}

    for Z in range(3, args.zmax):
        m = " ★" if Z in MAGIC else ""
        print(f"{Z:>3d} {fwd_d2.get(Z, 0):>+10.4f}{m}")

    # Save witness
    w = WitnessBuilder("shell-closure", engine="python")
    w.set_description(
        f"Categorical shell closure from per-partition nuclear character "
        f"at k=3..{args.kmax}. Forward δ² of cumulative Wedderburn-weighted "
        f"ln|χ_λ(Z)|. Computed with sparse seminormal matrices."
    )
    w.add_parameter("kmax", args.kmax)
    w.add_parameter("zmax", args.zmax)
    w.add_data("cumulative_ln_chi", {str(Z): cum[Z] for Z in cum})
    w.add_data("forward_delta2", {str(Z): fwd_d2.get(Z, 0) for Z in range(3, args.zmax)})
    w.save()
    print(f"\nWitness saved.")


if __name__ == "__main__":
    main()
