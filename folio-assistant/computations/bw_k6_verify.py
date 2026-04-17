"""
Verify k=6 BW corrections via seminormal matrix traces.

Builds the nuclear crossing chain for each nucleus (Z,N) and
computes the per-partition trace in H₆(q). This gives the ACTUAL
per-irrep contribution — not guessed scaling functions.

Method:
  1. For each partition λ ⊢ 6, build the Hoefsmit seminormal matrices
  2. Construct the nuclear braid crossing chain for (Z,N):
     - Z protons × N neutrons, with pp/nn/pn crossings
     - Each crossing maps to σ_gen or σ_gen - h/2 depending on type
  3. Compute tr(Π crossings) in each irrep → per-partition character
  4. The k=6 BW correction = Σ_λ w_λ × f(χ_λ(Z,N))

The per-partition χ_λ(Z,N) as a FUNCTION of (Z,N) determines the
scaling function S_λ.

Usage:
    python3 bw_k6_verify.py
"""

import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

import numpy as np
from q_parameter import Q as q0, Q_INV as qi, HA
from experimental_constants import M_E_MEV
from level_k_binding import seminormal_matrix, standard_young_tableaux
from hoefsmit_witness import load_witness
from hecke_core import binding_energy_bw


def crossing_matrix(shape, gen, crossing_type):
    """Crossing matrix for one crossing in irrep `shape`.

    crossing_type:
      'pp' → σ_gen (positive eigenvalue channel)
      'nn' → σ_gen - h·I (negative eigenvalue channel)
      'pn' → σ_gen - (h/2)·I (mixed channel)
    """
    M = seminormal_matrix(shape, gen)
    d = M.shape[0]
    if crossing_type == 'pp':
        return M
    elif crossing_type == 'nn':
        return M - HA * np.eye(d)
    elif crossing_type == 'pn':
        return M - (HA / 2) * np.eye(d)
    return np.eye(d)


def nuclear_chain(Z, N, gen):
    """Build nuclear crossing chain for a nucleus (Z,N).

    The nuclear braid at level k consists of:
      - Nucleon crossings (B₃ structure per nucleon)
      - Inter-nucleon crossings (pp, nn, pn pairs)

    Returns list of crossing types for one generator.
    """
    chain = []
    ordering = ['p'] * Z + ['n'] * N

    # Per-nucleon B₃ crossings
    for nuc in ordering:
        if gen == 0:
            chain.extend(['pp'] * 3)
            if nuc == 'p':
                chain.extend(['pp', 'pp'])
            else:
                chain.extend(['pn', 'pn'])
        else:
            chain.extend(['nn'] * 3)
            chain.append('pn' if nuc == 'p' else 'nn')

    # Inter-nucleon crossings (gen 0 only)
    if gen == 0:
        A = Z + N
        for i in range(A):
            for j in range(i + 1, A):
                ti, tj = ordering[i], ordering[j]
                if ti == 'p' and tj == 'p':
                    chain.append('pp')
                elif ti == 'n' and tj == 'n':
                    chain.append('nn')
                else:
                    chain.append('pn')

    return chain


def nuclear_trace(shape, Z, N):
    """Compute tr(nuclear braid) in irrep `shape` for nucleus (Z,N).

    Multiplies the crossing matrices for both generators and
    returns the trace.
    """
    tabs = standard_young_tableaux(shape)
    d = len(tabs)
    if d == 0:
        return 0.0, d

    total_trace = 0.0
    for gen in [0, 1]:
        chain = nuclear_chain(Z, N, gen)
        M = np.eye(d)
        for ct in chain:
            M = M @ crossing_matrix(shape, gen, ct)
        total_trace += float(np.trace(M))

    return total_trace, d


AME = [
    (1, 1, 2, 1.1121, "D"), (2, 2, 4, 7.0739, "⁴He"),
    (3, 4, 7, 5.6063, "⁷Li"), (6, 6, 12, 7.6801, "¹²C"),
    (8, 8, 16, 7.9762, "¹⁶O"), (14, 14, 28, 8.4477, "²⁸Si"),
    (20, 20, 40, 8.5513, "⁴⁰Ca"), (26, 30, 56, 8.7904, "⁵⁶Fe"),
]


if __name__ == "__main__":
    print("k=6 BW verification via seminormal matrix traces")
    print(f"q₀ = {q0:.10f}, h = {HA:.6f}")
    print()

    witness = load_witness()

    # Compute per-partition nuclear traces at k=6 for each nucleus
    level = witness['levels'].get('6', [])
    if not level:
        print("No k=6 data in witness. Run hoefsmit_witness first.")
        sys.exit(1)

    print(f"{'λ':>14s}", end="")
    for _, _, A, _, name in AME:
        print(f" {name:>10s}", end="")
    print()
    print("-" * (15 + 11 * len(AME)))

    partition_traces = {}
    for entry in level:
        shape = tuple(entry['shape'])
        w = entry['w']
        dim = entry['dim']
        if dim > 50:
            continue

        traces = {}
        print(f"{str(shape):>14s}", end="")
        for Z, N, A, BperA, name in AME:
            tr, d = nuclear_trace(shape, Z, N)
            traces[name] = tr
            # Show log|tr| to see scaling
            if abs(tr) > 1e-300:
                print(f" {math.log(abs(tr)):>10.3f}", end="")
            else:
                print(f" {'0':>10s}", end="")
        print()
        partition_traces[shape] = {'w': w, 'dim': dim, 'traces': traces}

    # The BW contribution from each partition:
    # B_λ = w_λ × f(tr_λ) × scale
    # Compare to k=5 residuals to see if this explains them
    print()
    print("k=5 residuals vs per-partition ln|tr| structure:")
    print(f"{'El':>6s} {'err(k=5)':>9s}", end="")
    for shape in partition_traces:
        print(f" {str(shape):>10s}", end="")
    print()

    for Z, N, A, BperA, name in AME:
        B_ame = A * BperA
        B5 = binding_energy_bw(Z, N, k=5)
        err = B5 - B_ame
        print(f"{name:>6s} {err:>+9.2f}", end="")
        for shape, data in partition_traces.items():
            tr = data['traces'].get(name, 0)
            if abs(tr) > 1e-300:
                # Normalized: ln|tr|/dim
                print(f" {math.log(abs(tr))/data['dim']:>10.4f}", end="")
            else:
                print(f" {'0':>10s}", end="")
        print()

    print()
    print("If a per-partition ln|tr|/dim correlates with the k=5")
    print("residuals, that partition's scaling function matches the")
    print("residual pattern and can serve as a k=6 correction.")
