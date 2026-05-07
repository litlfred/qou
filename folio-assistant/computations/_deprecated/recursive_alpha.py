#!/usr/bin/env python3
"""
Recursive α_EM computation: level k feeds level k+1.

At each level k, the coupling receives a correction from the
NEW partitions' Wedderburn weight redistribution on the force
carrier braids T_{2,9} and T_{3,5}.

The recursive formula:
  1/α(k) = 1/α(k-1) + δ(k)

where δ(k) comes from the new generator σ_{k-1} acting on
the force carrier braids via the k-level partition structure.

The force carriers have FIXED crossing structure:
  T_{2,9} = σ₁⁹ in H₂ (9 crossings on 2 strands)
  T_{3,5} = (σ₁σ₂)⁵ in H₃ (10 crossings on 3 strands)

At level k, we embed these into H_k and compute the correction
from the new partitions' seminormal matrices at σ_{k-1}.

Witness statements at each k allow resuming at k+1 without
recomputing lower levels.

Usage:
    python3 recursive_alpha.py --max-k 10
    python3 recursive_alpha.py --resume-from k7-alpha-witness.json --max-k 12
"""
import math
import json
import sys
import time
import numpy as np
from pathlib import Path
from datetime import datetime, timezone

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q, Q_INV, HA, q_int, HBAR_Q, Q_ERR
from experimental_constants import M_E_MEV, ALPHA_EM_INV, ALPHA_EM_INV_ERR
from hecke_characters import (build_seminormal_matrices, partitions_of,
                               dim_q, qfac)

q0 = Q; qi0 = Q_INV; h = HA; me = M_E_MEV
z = 1.0 / (q0**0.5 + qi0**0.5)
hbar_q2 = HBAR_Q**2

# Chern-Simons invariants of force carrier torus knots
CS_T29 = math.pi**2 * 10.0/9.0       # CS(T_{2,9})
CS_T35 = math.pi**2 * 16.0/15.0      # CS(T_{3,5})


# ══════════════════════════════════════════════════════════════
# LEVEL-k CORRECTION TO α
# ══════════════════════════════════════════════════════════════

def conjugate(p):
    if not p: return ()
    return tuple(sum(1 for r in p if r > j) for j in range(p[0]))


def compute_alpha_correction_at_k(k, prev_witness=None):
    """Compute the correction to 1/α at Hecke level k.

    The correction comes from the new generator σ_{k-1} acting
    on the force carrier braids through the new partitions at
    level k.

    For each NEW partition λ at level k (not inherited from k-1):
      1. Build seminormal matrix for σ_{k-1}
      2. The force carrier braid word at generator k-1 gives
         eigenvalues that modify the coupling
      3. The correction = w_λ × (eigenvalue product - 1) × base

    Returns: (delta_k, witness_data)
    """
    nfac = qfac(k)
    n_gens = k - 1

    # Build all partition data at level k
    partition_data = []
    for shape in partitions_of(k):
        c = conjugate(shape)
        sigmas, dim, syts = build_seminormal_matrices(shape)
        if dim == 0: continue
        d_q = dim_q(shape)
        w = d_q**2 / nfac
        partition_data.append({
            'shape': shape,
            'dim': dim,
            'dim_q': d_q,
            'weight': w,
            'sigmas': sigmas,
            'is_extremal': shape == (k,) or shape == tuple([1]*k),
        })

    # The force carrier braids embedded at generator k-1:
    # T_{2,9}: σ_{k-1}⁹ — the 9th power of the new generator
    # T_{3,5}: needs embedding of (σ_aσ_b)⁵ where a,b include k-1

    # For each partition: compute the eigenvalue product of σ_{k-1}⁹
    # in that partition's representation

    delta_k = 0.0
    partition_corrections = []

    for pd in partition_data:
        if pd['is_extremal']:
            continue

        shape = pd['shape']
        sigmas = pd['sigmas']
        dim = pd['dim']
        w = pd['weight']

        if n_gens - 1 >= len(sigmas):
            continue  # generator k-1 doesn't exist for this partition

        sigma_new = sigmas[n_gens - 1]  # σ_{k-1}

        # T_{2,9}: σ_{k-1}⁹
        power9 = np.linalg.matrix_power(sigma_new, 9)
        tr_t29 = np.trace(power9)

        # T_{3,5}: need σ_{k-2} and σ_{k-1} for the 3-strand embedding
        # (σ_{k-2}σ_{k-1})⁵
        if n_gens >= 2:
            sigma_prev = sigmas[n_gens - 2]
            prod_t35 = np.eye(dim)
            for _ in range(5):
                prod_t35 = prod_t35 @ sigma_prev @ sigma_new
            tr_t35 = np.trace(prod_t35)
        else:
            tr_t35 = 0.0

        # The correction from this partition:
        # δ_λ = w_λ × (tr_{k-1}(T29) × tr_{k-1}(T35) / dim² - 1)
        # normalized by the Markov parameter z^(number of new crossings)

        # The per-partition eigenvalue contribution to the coupling:
        # In the bare formula, each q-integer [n]_q comes from the
        # trace of σⁿ in the standard rep. At level k, the new
        # partition λ adds a correction to this trace.

        # The correction to [9]_q from partition λ at level k:
        delta_9 = w * (tr_t29 / dim - q_int(9)) / q_int(9)

        # The correction to [10]_q (using T_{3,5} trace):
        delta_10 = w * (tr_t35 / dim - q_int(10)) / q_int(10) if abs(q_int(10)) > 0 else 0

        # Total correction to 1/α from this partition:
        # 1/α ≈ q·[9]·[10]·(1 + δ₉)(1 + δ₁₀)
        # δ(1/α) ≈ q·[9]·[10]·(δ₉ + δ₁₀)
        bare = q0 * q_int(9) * q_int(10)
        correction = bare * (delta_9 + delta_10)

        delta_k += correction

        partition_corrections.append({
            'shape': str(shape),
            'dim': dim,
            'weight': round(w, 10),
            'tr_T29': round(tr_t29, 10),
            'tr_T35': round(tr_t35, 10),
            'delta_9': round(delta_9, 12),
            'delta_10': round(delta_10, 12),
            'correction': round(correction, 12),
        })

    witness = {
        'level': k,
        'n_partitions': len(partition_data),
        'n_non_extremal': sum(1 for pd in partition_data if not pd['is_extremal']),
        'delta_k': round(delta_k, 12),
        'partition_corrections': partition_corrections,
        'cumulative_note': 'Add delta_k to previous level 1/α to get this level.',
    }

    return delta_k, witness


def compute_recursive_alpha(max_k=10, resume_witness=None):
    """Compute 1/α recursively from k=3 to max_k.

    At each level: 1/α(k) = 1/α(k-1) + δ(k) + CS correction

    The CS correction (from Chern-Simons of force carriers on Bring's surface)
    is a GLOBAL correction applied once (not per-level), captured by the
    geometric resummation 1/(1-δ_CS).
    """
    # Base: bare coupling
    bare = q0 * q_int(9) * q_int(10)

    # CS correction (global, level-independent)
    n2 = q_int(2)
    cs_sum = CS_T29 + CS_T35
    delta_cs = cs_sum * (n2/2) * hbar_q2 / bare
    alpha_inv_cs = bare / (1 - delta_cs)

    print("="*90)
    print(f"RECURSIVE 1/α COMPUTATION: k=3 to k={max_k}")
    print("="*90)
    print(f"\n  Base: q·[9]·[10] = {bare:.9f}")
    print(f"  CS correction: /(1-δ) = {alpha_inv_cs:.9f}")
    print(f"  Observed: {ALPHA_EM_INV:.9f}")
    print(f"  Gap after CS: {ALPHA_EM_INV - alpha_inv_cs:.9f}")

    cumulative = 0.0
    all_witnesses = []

    print(f"\n  {'k':>3} {'δ(k)':>14} {'Cumulative':>14} {'1/α':>14} {'Error':>10} {'Time':>6}")
    print("  "+"-"*68)

    for k in range(3, max_k + 1):
        t0 = time.time()
        delta_k, witness = compute_alpha_correction_at_k(k)
        dt = time.time() - t0

        cumulative += delta_k
        alpha_inv_k = alpha_inv_cs + cumulative
        error = (alpha_inv_k - ALPHA_EM_INV) / ALPHA_EM_INV * 100

        witness['alpha_inv_at_level'] = round(alpha_inv_k, 12)
        witness['error_pct'] = round(error, 8)
        witness['cumulative_delta'] = round(cumulative, 12)
        witness['timestamp'] = datetime.now(timezone.utc).isoformat()
        all_witnesses.append(witness)

        print(f"  {k:>3} {delta_k:>+14.9f} {cumulative:>+14.9f} {alpha_inv_k:>14.9f} {error:>+9.6f}% {dt:>5.2f}s")

    # Final summary
    print(f"\n  FINAL: 1/α = {alpha_inv_cs + cumulative:.9f}")
    print(f"  Observed:    {ALPHA_EM_INV:.9f}")
    print(f"  Error:       {(alpha_inv_cs + cumulative - ALPHA_EM_INV)/ALPHA_EM_INV*100:+.7f}%")

    return alpha_inv_cs + cumulative, all_witnesses


# ══════════════════════════════════════════════════════════════
# MAIN
# ══════════════════════════════════════════════════════════════

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Recursive α computation")
    parser.add_argument("--max-k", type=int, default=10)
    parser.add_argument("--resume-from", type=str, default=None)
    parser.add_argument("--output", "-o", type=str, default="recursive-alpha.witness.json")
    args = parser.parse_args()

    alpha_inv, witnesses = compute_recursive_alpha(max_k=args.max_k)

    # Save witness
    out = {
        'computation': 'recursive-alpha',
        'max_k': args.max_k,
        'alpha_inv_final': alpha_inv,
        'alpha_inv_observed': ALPHA_EM_INV,
        'error_pct': (alpha_inv - ALPHA_EM_INV) / ALPHA_EM_INV * 100,
        'levels': witnesses,
        'formula': '1/α = q·[9]·[10]/(1-δ_CS) + Σ_k δ(k)',
        'inputs': {
            'q0': Q,
            'CS_T29': CS_T29,
            'CS_T35': CS_T35,
            'hbar_q2': hbar_q2,
        },
    }

    outpath = Path(__file__).parent / args.output
    with open(outpath, 'w') as f:
        json.dump(out, f, indent=2, default=str)
    print(f"\n  Witness: {outpath.name}")
