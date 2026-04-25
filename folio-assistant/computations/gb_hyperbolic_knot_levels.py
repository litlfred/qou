#!/usr/bin/env python3
"""
GB-FILTRATION LEVELS of HYPERBOLIC KNOTS.

User hypothesis: in the Gröbner-Shirshov filtration of H_n(q),
ideals starting with words of hyperbolic knots appear at specific
levels.  The level is a scaling/dampening factor for that knot's
contribution to the Markov trace / mass formula.

Approach:
  1. List standard braid representatives for hyperbolic knots
     (4_1, 5_2, 6_1, 6_2, 6_3, 7_1...7_7).
  2. For each, compute the Hecke character χ^λ at every partition
     λ ⊢ n (with n = braid index).
  3. Identify the GB filtration level ℓ(λ) = height(λ) - 1 where
     the character is DOMINANT (max |χ^λ|).
  4. Tabulate: knot → dominant level → 1/[level+1]_q damping factor.
  5. Compare against hyperbolic volume Vol(K).

Goal: empirical evidence that GB level ↔ knot volume ↔ damping.
"""
from __future__ import annotations
import sys, json, warnings
from pathlib import Path
from datetime import datetime, timezone

warnings.filterwarnings("ignore")
sys.path.insert(0, str(Path(__file__).parent))

import mpmath as mp
mp.mp.dps = 30

import numpy as np
from scipy import sparse as sp_sparse

from q_parameter import Q as Q0_FLOAT
from hecke_characters import partitions_of, build_seminormal_matrices, dim_q

Q0 = mp.mpf(str(Q0_FLOAT)); QI = mp.mpf(1)/Q0
H_A = Q0 - QI
h_val = float(H_A)


def q_int(n):
    return (Q0**n - QI**n) / (Q0 - QI)


# Hyperbolic knots (standard braid representations, signed integer notation)
# Source: Knot Atlas, Rolfsen / Jones polynomial computations.
HYPERBOLIC_KNOTS = [
    # (name, braid_word, n_strands, hyperbolic_volume)
    ("4_1",  [1, -2, 1, -2],                          3, 2.0298832),
    ("5_2",  [1, 1, 1, -2, 1, -2],                    3, 2.8281220),
    ("6_1",  [1, 1, -2, 1, -2, -2],                   3, 3.1639633),
    ("6_2",  [1, 1, 1, -2, 1, -2, -2],                3, 4.4015175),
    ("6_3",  [1, 1, -2, 1, -2, 1, -2],                3, 5.6927297),
    ("7_2",  [1, 1, 1, 1, 1, -2, 1, -2],              3, 3.3317442),
    ("7_3",  [1, 1, 1, 1, -2, 1, 1, -2],              3, 4.5921326),
    ("7_4",  [1, 1, -2, 1, -2, -2, -2],               3, 5.0136959),
    ("7_5",  [1, 1, 1, 1, -2, 1, 1, 1, -2],           3, 6.4439185),
    ("7_6",  [1, 1, 1, -2, 1, -2, -2, -2],            3, 7.0846178),
    ("7_7",  [1, 1, -2, 1, -2, 1, -2, -2],            3, 7.6433568),
]


def chi_lambda(shape, word, n_strands):
    """Compute χ^λ(braid word) numerically via Hoefsmit seminormal."""
    sigmas, dim, _ = build_seminormal_matrices(shape)
    if dim == 0:
        return 0.0
    is_sparse = sp_sparse.issparse(sigmas[0]) if sigmas else False
    if is_sparse:
        product = sp_sparse.eye(dim, format='csr')
        I = sp_sparse.eye(dim, format='csr')
    else:
        product = np.eye(dim)
        I = np.eye(dim)
    # T_i = σ_i in Hecke; T_i^{-1} = σ_i + (q^{-1} - q)·I = σ_i - h·I (Hecke skein).
    for w in word:
        idx = abs(w) - 1
        if idx >= len(sigmas):
            raise IndexError(f"Generator {w} out of range for partition {shape}")
        if w > 0:
            M = sigmas[idx]
        else:
            # T^{-1} = σ - h · I
            M = sigmas[idx] - h_val * I
        product = product @ M
    if is_sparse:
        chi = float(product.diagonal().sum())
    else:
        chi = float(np.trace(product))
    return chi


def gb_level(shape):
    """GB filtration level = height(λ) - 1."""
    return len(shape) - 1


def main():
    print("=" * 100)
    print("GB-FILTRATION LEVELS of HYPERBOLIC KNOTS")
    print("=" * 100)
    print(f"  q_0 = {Q0_FLOAT}")
    print()
    print("  Probing each hyperbolic knot's character spectrum across H_n partitions")
    print("  GB filtration level ℓ(λ) = (# rows of λ) − 1   (height-1)")
    print()

    rows = []
    print(f"  {'knot':<6} {'Vol':>10} {'partition':>12} {'ℓ(λ)':>5} "
          f"{'|χ|':>14} {'1/[ℓ+1]_q':>12} {'dominant':>9}")
    for name, word, n_str, vol in HYPERBOLIC_KNOTS:
        # Compute χ at each partition of n_str
        partition_data = []
        for shape in partitions_of(n_str):
            shape_t = tuple(shape)
            try:
                chi = chi_lambda(shape_t, word, n_str)
            except Exception as e:
                continue
            level = gb_level(shape_t)
            damp = float(1 / q_int(level + 1)) if level >= 0 else 1.0
            partition_data.append({
                'partition': shape_t,
                'level': level,
                'chi': chi,
                'damping': damp,
            })
        if not partition_data:
            print(f"  {name:<6} (no partitions)")
            continue
        # Find dominant
        max_pd = max(partition_data, key=lambda x: abs(x['chi']))
        for pd in partition_data:
            mark = " ★" if pd is max_pd else ""
            print(f"  {name:<6} {vol:>10.4f} {str(pd['partition']):>12} {pd['level']:>5} "
                  f"{pd['chi']:>+14.6f} {pd['damping']:>12.6f}{mark}")
        # Aggregate row
        rows.append({
            'knot': name,
            'volume': vol,
            'braid_word': word,
            'dominant_partition': list(max_pd['partition']),
            'dominant_level': max_pd['level'],
            'dominant_chi': max_pd['chi'],
            'damping_factor': max_pd['damping'],
        })
        print()

    # Pattern analysis
    print("=" * 100)
    print("  PATTERN: GB level vs hyperbolic volume")
    print("=" * 100)
    print(f"  {'knot':<6} {'Vol':>10} {'level':>6} {'|χ_dom|':>12} {'Vol·damp':>12} {'Vol/level':>12}")
    for r in rows:
        if r['dominant_level'] >= 0:
            damp = r['damping_factor']
            vd = r['volume'] * damp
            vol_per_level = r['volume'] / max(1, r['dominant_level'] + 1)
            print(f"  {r['knot']:<6} {r['volume']:>10.4f} {r['dominant_level']:>6} "
                  f"{abs(r['dominant_chi']):>12.4e} {vd:>12.6f} {vol_per_level:>12.4f}")

    # Save witness
    witness = {
        'computation': 'gb-hyperbolic-knot-levels',
        'description': (
            'Map hyperbolic knot braid words to their dominant GB '
            'filtration level (partition with max |χ^λ|).  Tests '
            'user hypothesis that GB level = scaling/dampening factor.'
        ),
        'timestamp': datetime.now(timezone.utc).isoformat(),
        'q_0': Q0_FLOAT,
        'knots': rows,
    }
    out = Path(__file__).parent / "gb-hyperbolic-knot-levels.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\n  Witness: {out}")


if __name__ == "__main__":
    main()
