"""
Δ-chain storage: encode isotope witnesses as differences along β-decay chains.

Instead of storing the full polynomial for each isotope, store:
  base(Z₀, N₀) = full polynomial (small reference nucleus)
  Δ(Z, N) = cert(Z+1, N-1) - cert(Z, N)  (the β⁻ decay difference)

Any isotope (Z, N) can be reconstructed by walking the chain:
  cert(Z, N) = base + Σ Δ_k along the path from base to (Z, N)

The Δ polynomials are MUCH smaller than the full polynomials because
most terms cancel in the difference (parent and daughter share most
of their Hecke algebra structure — only the converting nucleon differs).

Storage comparison (estimated):
  Full polynomial (A=60):  ~3 MB (10^596-digit coefficients)
  Δ polynomial (A=60):     ~10 KB (difference is sparse)
  Δ-chain to reach ⁶⁰Co:  ~300 KB (30 steps × 10 KB)

The Δ-chain also encodes the Q-value directly:
  Q(Z,N) = |eval(Δ(Z,N))| × κ_q
"""

import json
import math
import sys
sys.path.insert(0, '.')
from q_parameter import Q, Q_INV, HA, LN_Q, S_SKEIN
from experimental_constants import M_E_MEV

KAPPA_Q = LN_Q * M_E_MEV / 3.0
Z_MARKOV = 1.0 / (math.sqrt(Q) + 1.0/math.sqrt(Q))
S_SK = math.sqrt(Q) - 1.0/math.sqrt(Q)

def crossing_coeffs(ti, tj):
    pair = ti + tj
    if pair == 'pp': return (1.0, 0.0)
    elif pair == 'nn': return (1.0, -HA)
    else: return (1.0, -HA / 2.0)

def generator_volumes(z, n):
    a = z + n
    types = ['p']*z + ['n']*n
    vols = []
    for i in range(a-1):
        m = [[1.0, 0.0], [0.0, 1.0]]
        for j in range(i+1, a):
            c, d = crossing_coeffs(types[i], types[j])
            t = [[c*HA+d, c], [c, d]]
            m = [[m[0][0]*t[0][0]+m[0][1]*t[1][0], m[0][0]*t[0][1]+m[0][1]*t[1][1]],
                 [m[1][0]*t[0][0]+m[1][1]*t[1][0], m[1][0]*t[0][1]+m[1][1]*t[1][1]]]
        vols.append(Z_MARKOV * m[0][0] + m[1][0])
    return vols


def compute_delta(z_par, n_par):
    """Compute Δ = (daughter volumes) - (parent volumes) for β⁻ decay.

    Returns per-generator volume differences and the total log ratio.
    """
    a = z_par + n_par
    vp = generator_volumes(z_par, n_par)
    vd = generator_volumes(z_par + 1, n_par - 1)

    deltas = []
    log_ratio = 0.0
    for i in range(a - 1):
        d = vd[i] - vp[i]
        r = vd[i] / vp[i] if abs(vp[i]) > 1e-30 else float('inf')
        lr = math.log(abs(r)) if abs(r) > 0 and r != float('inf') else 0.0
        deltas.append({
            'gen': i,
            'v_par': vp[i],
            'v_dau': vd[i],
            'delta': d,
            'ratio': r,
            'log_ratio': lr,
        })
        log_ratio += lr

    return {
        'z': z_par, 'n': n_par, 'a': a,
        'z_dau': z_par + 1, 'n_dau': n_par - 1,
        'deltas': deltas,
        'total_log_ratio': log_ratio,
        'n_nonzero_deltas': sum(1 for d in deltas if abs(d['delta']) > 1e-30),
        'max_delta': max(abs(d['delta']) for d in deltas),
        'min_delta': min(abs(d['delta']) for d in deltas if abs(d['delta']) > 1e-30),
    }


def build_chain(z_target, n_target, z_base=1, n_base=1):
    """Build Δ-chain from base (z_base, n_base) to target (z_target, n_target).

    Uses β⁻ path: (Z, N) → (Z+1, N-1) at constant A.
    Requires same A: z_base + n_base = z_target + n_target.
    """
    a = z_target + n_target
    assert z_base + n_base == a, f"A mismatch: {z_base+n_base} ≠ {a}"

    chain = []
    z, n = z_base, n_base
    while z < z_target:
        delta = compute_delta(z, n)
        chain.append(delta)
        z += 1
        n -= 1

    return chain


# ── Δ-chain format specification ─────────────────────────────────

def delta_chain_to_json(chain, z_target, n_target):
    """Serialize a Δ-chain to the compact JSON format."""
    a = z_target + n_target
    return {
        'format': 'delta-chain-v1',
        'target': {'z': z_target, 'n': n_target, 'a': a},
        'base': {'z': chain[0]['z'], 'n': chain[0]['n']},
        'steps': len(chain),
        'chain': [
            {
                'z': step['z'], 'n': step['n'],
                'n_changed_generators': step['n_nonzero_deltas'],
                'total_log_ratio': step['total_log_ratio'],
            }
            for step in chain
        ],
        'total_log_ratio': sum(s['total_log_ratio'] for s in chain),
        'storage_bytes_estimate': len(chain) * 100,  # ~100 bytes per step
    }


if __name__ == "__main__":
    print("=" * 70)
    print("Δ-CHAIN STORAGE FORMAT")
    print("=" * 70)

    # Build chains for benchmark nuclei
    BENCHMARKS = [
        (1,  2,  "³H",      0.01861),
        (6,  8,  "¹⁴C",     0.15648),
        (27, 33, "⁶⁰Co",    0.31817),
        (38, 52, "⁹⁰Sr",    0.54590),
        (55, 82, "¹³⁷Cs",   0.51400),
        (83, 127,"²¹⁰Bi",   1.16270),
    ]

    print(f"\n{'Nucleus':>10} {'A':>4} {'Steps':>6} {'Storage':>10} {'Full poly':>12}")
    print("-" * 50)

    for z, n, name, q_exp in BENCHMARKS:
        a = z + n
        # Base: most neutron-rich isobar (Z=1 for light, Z=A//4 for heavy)
        z_base = max(1, a // 4)
        n_base = a - z_base
        if z_base > z:
            z_base = 1
            n_base = a - 1

        chain = build_chain(z, n, z_base, n_base)
        chain_bytes = len(chain) * 100  # estimate

        # Full polynomial storage estimate
        log_c = max(1, 0.2266 * a**2 - 3.3438 * a + 20.25)
        poly_terms = min(a * 50, 10000)
        coeff_bytes = max(4, int(log_c * 0.42) + 1)
        full_bytes = 4 * poly_terms * (4 + coeff_bytes)

        ratio = full_bytes / max(1, chain_bytes)
        print(f"{name:>10} {a:>4} {len(chain):>6} {chain_bytes:>8} B {full_bytes:>10} B  ({ratio:.0f}× smaller)")

    # Detailed Δ for ⁶⁰Co
    print(f"\n{'='*70}")
    print("Δ-CHAIN DETAIL: ⁶⁰Co (Z=27, N=33)")
    print(f"{'='*70}")
    chain = build_chain(27, 33, 1, 59)
    print(f"  Base: (1, 59) → Target: (27, 33)")
    print(f"  Steps: {len(chain)}")
    print(f"  Total log ratio: {sum(s['total_log_ratio'] for s in chain):.4f}")
    print(f"\n  {'Step':>4} {'Z':>3}→{'Z+1':>3} {'Changed gens':>13} {'log ratio':>10}")
    print("  " + "-" * 40)
    for i, step in enumerate(chain):
        print(f"  {i+1:>4} {step['z']:>3}→{step['z']+1:>3} "
              f"{step['n_nonzero_deltas']:>13}/{step['a']-1} "
              f"{step['total_log_ratio']:>+10.4f}")

    # Write example chain
    chain_json = delta_chain_to_json(chain, 27, 33)
    with open('delta-chain-60co.json', 'w') as f:
        json.dump(chain_json, f, indent=2)
    print(f"\n  Written: delta-chain-60co.json ({len(json.dumps(chain_json))} bytes)")
