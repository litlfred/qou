#!/usr/bin/env python3
"""Generic Jones-Markov atlas for H_n(q) — infrastructure for all atoms.

Per author direction 2026-05-25: "put in all infra for all nucleotides" +
"can we use inverse gram basis and crystal basis and partition
embeddings/repn?"

## Module purpose

Provides `solve_jones_markov_h_n(n, q)` — generic Jones-Markov weight
solver for arbitrary H_n(q) Hecke algebra. Returns per-partition y_λ
weights satisfying the Markov axiom.

## Method

For n with p(n) partitions:
  - p(n) partitions of n ↔ p(n) conjugacy classes of S_n ↔ p(n) cycle types
  - For each cycle type λ = (c_1, ..., c_r), build representative braid
    word: cycle (c_i) ↦ σ_a σ_{a+1} ... σ_{a+c_i-2}, concatenated with
    fresh strand offset per cycle
  - Markov axiom: tr_M(rep braid for cycle type λ) = z^{n - r(λ)}
    where r(λ) = number of parts, z = 1/(√q + 1/√q)
  - Build p(n)×p(n) q-Hecke character matrix A: A[i,j] = χ_{λ_j}(rep_i)
    via pyhecke_native.chi_lambda_braid (just-wired tier-3 infra)
  - Solve A · y = b where b[i] = z^{n - r(λ_i)} → y is Jones-Markov

The character matrix A is the q-deformed S_n character table —
invertible by Schur orthogonality at generic q (and at q = q_0 well-
conditioned per `alpha_k_jones_markov_h{3,4}.py` precedents).

## Feasibility per atom

| Atom | A | n = 3A | partitions | matrix entries | est. time |
|------|---|--------|------------|-----------------|-----------|
| 2H   | 2 | 6      | 11         | 121             | < 1 s     |
| 3H,3He | 3 | 9    | 30         | 900             | ~ 2 s     |
| 4He  | 4 | 12     | 77         | 5929            | ~ 10 s    |
| 5Li  | 5 | 15     | 176        | 30976           | ~ 40 s    |
| 6Li  | 6 | 18     | 385        | 148225          | ~ 4 min   |
| 7Li  | 7 | 21     | 792        | 627264          | ~ 15 min  |
| 8Be  | 8 | 24     | 1575       | 2.5M            | ~ 40 min  |

For A > 8 (12C onwards) — partition count blows up; need closed-form
q-Schur principal specialization (not implemented in this module).
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — bridge: reads a witness that co-moved into a cluster subdir
import _path_bridge as _pb  # noqa: E402 — cross-cluster witness lookup
import json
import sys
import time
from pathlib import Path

import mpmath as mp
import numpy as np
import pyhecke_native as pn
from sympy.utilities.iterables import partitions

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

Q_PIN = _pb.witness_path("q-pinning-50-digit.witness.json", HERE)
Q0_MPF = mp.mpf(json.load(Q_PIN.open())["derived_50_digit"]["q"])
Q0_F64 = float(Q0_MPF)


def partitions_of_descending(n: int) -> list[list[int]]:
    """All partitions of n as descending-sorted lists."""
    shapes = []
    for p in partitions(n):
        parts = sorted(p.items(), reverse=True)
        expanded = []
        for size, count in parts:
            expanded.extend([size] * count)
        shapes.append(expanded)
    return shapes


def cycle_type_braid(parts: list[int]) -> list[tuple[int, int]]:
    """Build a representative braid for cycle type `parts`.

    Each cycle of length c uses generators σ_a, σ_{a+1}, ..., σ_{a+c-2}
    on a fresh strand range. Total braid length = n - r(parts).

    Format: list of (sign, gen_1based) pairs per pyhecke_native.
    """
    word = []
    offset = 0
    for c in parts:
        for k in range(c - 1):
            word.append((1, offset + 1 + k))
        offset += c
    return word


def solve_jones_markov_h_n(n: int, q: float = Q0_F64, verbose: bool = False) -> dict:
    """Solve Jones-Markov y_λ at H_n(q) via cycle-type linear system.

    Returns:
        dict with keys:
            n, q, num_partitions, partitions, y_lambda, dims,
            condition_number, sum_y_dim, elapsed_seconds
    """
    shapes = partitions_of_descending(n)
    P = len(shapes)

    z_mark = 1 / (mp.sqrt(q) + 1 / mp.sqrt(q))

    if verbose:
        print(f"  H_{n}(q): {P} partitions, building {P}×{P} χ-matrix (rayon-parallel)...")
    t_start = time.time()

    # Build χ-matrix using batched chi_lambdas_braid (rayon-parallel over partitions per row)
    # A[i, j] = χ_{λ_j}(rep braid for λ_i)
    A = np.zeros((P, P), dtype=np.float64)
    for i, row_lam in enumerate(shapes):
        word = cycle_type_braid(row_lam)
        chi_row = pn.chi_lambdas_braid(shapes, word, q)
        A[i, :] = chi_row
        if verbose and (i + 1) % max(1, P // 10) == 0:
            print(f"    row {i+1}/{P} ({time.time() - t_start:.1f}s)")

    # RHS: tr_M(rep for λ) = z^{n - r(λ)}
    b = np.array([float(z_mark ** (n - len(sh))) for sh in shapes])

    # Solve
    cond = float(np.linalg.cond(A))
    try:
        y = np.linalg.solve(A, b)
    except np.linalg.LinAlgError:
        y, *_ = np.linalg.lstsq(A, b, rcond=None)

    # Verify: Σ y_λ · dim_λ ≈ 1
    dims_arr = pn.chi_lambdas_braid(shapes, [], q)
    dims = [int(d + 0.5) for d in dims_arr]
    sum_y_dim = float(sum(y[i] * dims[i] for i in range(P)))

    elapsed = time.time() - t_start

    return {
        "n": n,
        "q": q,
        "num_partitions": P,
        "partitions": [list(sh) for sh in shapes],
        "y_lambda": y.tolist(),
        "dims_classical": dims,
        "condition_number": cond,
        "sum_y_dim": sum_y_dim,
        "elapsed_seconds": elapsed,
    }


def tr_M_via_atlas(atlas: dict, word: list[tuple[int, int]], q: float = None) -> float:
    """Apply the Jones-Markov atlas to compute tr_M for an arbitrary braid word.

    Returns Σ_λ y_λ · χ_λ(word) at q.
    """
    if q is None:
        q = atlas["q"]
    y = atlas["y_lambda"]
    shapes = atlas["partitions"]
    chi_vals = pn.chi_lambdas_braid(shapes, word, q)
    return float(sum(y[i] * chi_vals[i] for i in range(len(shapes))))


# ---- demo: solve H_6 (2H deuteron) on import for sanity ----
if __name__ == "__main__":
    print("=" * 80)
    print("Jones-Markov atlas — demo at H_6 (2H deuteron)")
    print("=" * 80)
    atlas = solve_jones_markov_h_n(6, verbose=True)
    print()
    print(f"  num_partitions = {atlas['num_partitions']}")
    print(f"  condition number = {atlas['condition_number']:.3e}")
    print(f"  Σ y_λ · dim_λ = {atlas['sum_y_dim']:.10f}  (expected 1.0)")
    print(f"  elapsed = {atlas['elapsed_seconds']:.3f}s")
    print()
    print("  Sample y_λ:")
    for sh, d, yv in zip(atlas["partitions"][:5], atlas["dims_classical"][:5], atlas["y_lambda"][:5]):
        print(f"    {tuple(sh)} (dim {d}): y = {yv:+.10f}")
