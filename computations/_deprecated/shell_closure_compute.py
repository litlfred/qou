#!/usr/bin/env python3
"""
Categorical shell closure — block-diagonal optimized.

Hoefsmit seminormal matrices are:
  Gen 0: PURE DIAGONAL (eigenvalue per SYT)
  Gen 1: block-diagonal (2×2 blocks + diagonal singletons)

This gives O(d) per crossing instead of O(d³), enabling k=10..15
computation in seconds instead of hours.

The shell correction EMERGES from the per-partition weighted
forward δ²(ln|χ_λ|) — no Gaussian, no heat kernel, no bolted-on
function.

Usage:
    python3 shell_closure_compute.py --kmax 15 --zmax 30

Reference: prop:shell-closure-nf-term-count
"""
import json
import math
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

import numpy as np
from level_k_binding import seminormal_matrix, standard_young_tableaux
from hoefsmit_witness import load_witness
from q_parameter import Q as q0, Q_INV as qi, HA
from witness_base import WitnessBuilder


def _extract_blocks(shape, gen):
    """Extract block structure from Hoefsmit seminormal matrix.

    Returns:
      diag: array of diagonal eigenvalues for singleton blocks
      blocks: list of (i, j, a, b, c, d) for 2×2 blocks
              [[a, b], [c, d]] at positions (i,j)
    """
    tabs = standard_young_tableaux(shape)
    dim = len(tabs)
    if dim == 0:
        return np.array([]), []

    M = seminormal_matrix(shape, gen)

    paired = set()
    blocks = []
    for i in range(dim):
        if i in paired:
            continue
        # Find off-diagonal partner
        partner = None
        for j in range(dim):
            if j != i and abs(M[i, j]) > 1e-15:
                partner = j
                break
        if partner is not None:
            j = partner
            blocks.append((i, j, M[i, i], M[i, j], M[j, i], M[j, j]))
            paired.add(i)
            paired.add(j)

    # Singletons
    diag = np.zeros(dim)
    singleton_mask = np.ones(dim, dtype=bool)
    for i, j, a, b, c, d in blocks:
        singleton_mask[i] = False
        singleton_mask[j] = False
    for i in range(dim):
        if singleton_mask[i]:
            diag[i] = M[i, i]

    return diag, blocks, singleton_mask, dim


def _apply_crossing_block(diag, blocks, singleton_mask, dim, ct):
    """Apply one crossing to the block-diagonal state.

    The crossing modifies eigenvalues:
      pp: σ_gen (identity on blocks)
      nn: σ_gen - h·I
      pn: σ_gen - h/2·I

    For diagonal state D and block-diagonal crossing C:
      New state = D × C (element-wise for diag, 2×2 for blocks)
    """
    if ct == 'pp':
        shift = 0.0
    elif ct == 'nn':
        shift = -HA
    elif ct == 'pn':
        shift = -HA / 2
    else:
        shift = 0.0
    return shift


def nuclear_character_fast(shape, Z, N, gen0_struct, gen1_struct):
    """Fast nuclear character using block-diagonal structure.

    Gen 0: pure diagonal → eigenvalue products
    Gen 1: 2×2 blocks → small matrix products
    """
    ordering = ['p'] * Z + ['n'] * N
    A = Z + N

    # ── Gen 0: diagonal ──
    diag0, _, _, dim = gen0_struct
    if dim == 0:
        return 0.0

    # Start: identity diagonal
    state0 = np.ones(dim)

    # Per-nucleon crossings on gen 0
    for nuc in ordering:
        # B₃: 3× σ₀ (pp)
        for _ in range(3):
            state0 *= diag0  # pp: multiply by eigenvalue

        if nuc == 'p':
            state0 *= diag0  # uu pair: pp
            state0 *= diag0  # uu pair: pp
        else:
            state0 *= (diag0 - HA / 2)  # ud pair: pn
            state0 *= (diag0 - HA / 2)  # ud pair: pn

    # Inter-nucleon crossings on gen 0
    for i in range(A):
        for j in range(i + 1, A):
            ti, tj = ordering[i], ordering[j]
            if ti == 'p' and tj == 'p':
                state0 *= diag0
            elif ti == 'n' and tj == 'n':
                state0 *= (diag0 - HA)
            else:
                state0 *= (diag0 - HA / 2)

    tr_gen0 = np.sum(state0)

    # ── Gen 1: block-diagonal ──
    diag1, blocks1, sing1, dim = gen1_struct

    # State: diagonal part (singletons) + 2×2 blocks
    # Singletons: scalar product chain
    sing_state = np.ones(dim)

    # 2×2 block states: each block tracks a 2×2 matrix
    block_states = []
    for i, j, a, b, c, d in blocks1:
        block_states.append(np.eye(2))

    def apply_gen1_crossing(ct):
        nonlocal sing_state
        if ct == 'nn':
            shift = -HA
        elif ct == 'pn':
            shift = -HA / 2
        else:
            shift = 0.0

        # Singletons
        for idx in range(dim):
            if sing1[idx]:
                sing_state[idx] *= (diag1[idx] + shift)

        # 2×2 blocks
        for bi, (i, j, a, b, c, d) in enumerate(blocks1):
            C = np.array([[a + shift, b], [c, d + shift]])
            block_states[bi] = block_states[bi] @ C

    # Per-nucleon crossings on gen 1
    for nuc in ordering:
        # B₃: 3× σ₁⁻¹ (nn)
        for _ in range(3):
            apply_gen1_crossing('nn')

        if nuc == 'p':
            apply_gen1_crossing('pn')  # ud pair
        else:
            apply_gen1_crossing('nn')  # dd pair

    # Electrons on gen 1
    for _ in range(Z):
        apply_gen1_crossing('nn')  # pe = σ⁻¹

    # Trace
    tr_gen1 = 0.0
    for idx in range(dim):
        if sing1[idx]:
            tr_gen1 += sing_state[idx]
    for bi, (i, j, a, b, c, d) in enumerate(blocks1):
        tr_gen1 += block_states[bi][0, 0] + block_states[bi][1, 1]

    return tr_gen0 + tr_gen1


def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--kmax', type=int, default=15)
    parser.add_argument('--zmax', type=int, default=30)
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

        # Precompute block structures
        structs = {}
        for entry in level:
            shape = tuple(entry['shape'])
            dim = entry['dim']
            structs[shape] = {
                0: _extract_blocks(shape, 0),
                1: _extract_blocks(shape, 1),
            }

        per_Z = {}
        for Z in range(1, args.zmax + 1):
            total = 0.0
            for entry in level:
                shape = tuple(entry['shape'])
                w = entry['w']
                chi = nuclear_character_fast(
                    shape, Z, Z,
                    structs[shape][0],
                    structs[shape][1],
                )
                if chi is None:
                    continue
                ln_chi = math.log(abs(chi)) if abs(chi) > 1e-300 else 0
                total += w * ln_chi
            per_Z[Z] = total

        results[k] = per_Z
        elapsed = time.time() - t0
        print(f"k={k:>2d}: {len(level):>3d} partitions, "
              f"max_dim={max_dim:>5d}, {elapsed:.1f}s")

    # Forward δ²
    print()
    K = args.kmax
    cum = {}
    for Z in range(1, args.zmax + 1):
        cum[Z] = sum(results.get(kk, {}).get(Z, 0) for kk in range(3, K + 1))

    d1 = {Z: cum[Z] - cum[Z - 1] for Z in range(2, args.zmax + 1)}
    fwd_d2 = {Z: d1[Z] - d1[Z - 1] for Z in range(3, args.zmax + 1)}

    print(f"Forward δ²(cumulative k=3..{K}):")
    print(f"{'Z':>3s} {'δ²':>10s} {'magic':>6s}")
    print("─" * 25)
    for Z in range(3, args.zmax):
        m = " ★" if Z in MAGIC else ""
        print(f"{Z:>3d} {fwd_d2.get(Z, 0):>+10.4f}{m}")

    # Save witness
    w = WitnessBuilder("shell-closure", engine="python")
    w.set_description(
        f"Categorical shell closure k=3..{K}. Block-diagonal optimized."
    )
    w.add_parameter("kmax", K)
    w.add_data("forward_delta2",
               {str(Z): round(fwd_d2.get(Z, 0), 10) for Z in range(3, args.zmax)})
    w.save()


if __name__ == "__main__":
    main()
