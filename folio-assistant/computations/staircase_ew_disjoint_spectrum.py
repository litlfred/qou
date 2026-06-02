#!/usr/bin/env python3
"""
Staircase EW residual conjecture — restored k=3..5 probe.

This script studies the disjoint electroweak braid

    β_EW = σ₁⁴ · σ₃⁶ · σ₅⁸

on staircase partitions ρ_k = (k, k-1, ..., 1).

Current verified behaviour in this checkout:
  - k=3 (ρ₃ = (3,2,1), dim 16): exact 8-bucket spectrum, 2 each
  - k=4 (ρ₄ = (4,3,2,1), dim 768): exact 8-bucket spectrum, 96 each
  - k=5 (ρ₅ = (5,4,3,2,1), dim 292,864): full diagonalization is skipped;
    we count the diagonal "pure" sector where σ₁, σ₃, σ₅ are each row/col
    eigenstates.  This sector has 52,224 tableaux in 8 exact buckets.

Because σ₁, σ₃, σ₅ are pairwise far-commuting and each has eigenvalues
q or -q⁻¹, the simple disjoint braid has only the exact bucket values

    q^{±18}, q^{±10}, q^{±6}, q^{±2}.

So any putative q^(1/(2k-1)) residual must come from a non-disjoint
EW interface contribution (for example Δ_I), not from β_EW alone.
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
from collections import Counter
from functools import lru_cache
from pathlib import Path
import sys

import numpy as np

sys.path.insert(0, str(Path(__file__).parent))

from q_parameter import Q as q0, HA
from witness_base import WitnessBuilder
# F6 (PR #582): wire numerical-q Hoefsmit through BlockCache.
from syt_prefix_cache import BlockCache, build_seminormal_matrices_cached


EW_EXPONENTS = (18, 10, 6, 2, -2, -6, -10, -18)
_BLOCK_CACHE = BlockCache(q0, HA)


def staircase_partition(k: int) -> tuple[int, ...]:
    return tuple(range(k, 0, -1))


def expected_bucket_counter(q: float, multiplicity: int) -> Counter:
    return Counter({round(float(q ** exp), 12): multiplicity for exp in EW_EXPONENTS})


def beta_ew_matrix(shape: tuple[int, ...]) -> np.ndarray:
    sigmas, dim, _ = build_seminormal_matrices_cached(
        shape, cache=_BLOCK_CACHE, sparse=False, q_val=float(q0),
    )
    if dim == 0:
        return np.zeros((0, 0))
    return (
        np.linalg.matrix_power(sigmas[0], 4)
        @ np.linalg.matrix_power(sigmas[2], 6)
        @ np.linalg.matrix_power(sigmas[4], 8)
    )


def eigen_bucket_counter(shape: tuple[int, ...]) -> tuple[int, Counter, list[float], dict[str, float]]:
    matrix = beta_ew_matrix(shape)
    eigvals = np.linalg.eigvals(matrix)
    eigvals = np.real(np.real_if_close(eigvals, tol=1000))
    eigvals = [float(v) for v in eigvals]
    counter = Counter(round(v, 12) for v in eigvals)
    sorted_vals = sorted(eigvals, reverse=True)

    target = float(q0 ** (1 / (2 * len(shape) - 1)))
    best = None
    for i in range(len(sorted_vals)):
        for j in range(i + 1, len(sorted_vals)):
            if abs(sorted_vals[j]) < 1e-14:
                continue
            ratio = sorted_vals[i] / sorted_vals[j]
            rel_err = abs(ratio - target) / target
            if best is None or rel_err < best["relativeError"]:
                best = {
                    "relativeError": float(rel_err),
                    "ratio": float(ratio),
                    "target": target,
                    "numeratorIndex": i,
                    "denominatorIndex": j,
                }
    return len(sorted_vals), counter, sorted_vals, best


@lru_cache(None)
def _k5_counts() -> tuple[int, dict[int, int]]:
    shape = staircase_partition(5)
    cells: list[tuple[int, int]] = []
    for r, row_len in enumerate(shape):
        for c in range(row_len):
            cells.append((r, c))
    idx = {cell: i for i, cell in enumerate(cells)}
    n_cells = len(cells)
    full_mask = (1 << n_cells) - 1

    pred = [0] * n_cells
    for i, (r, c) in enumerate(cells):
        mask = 0
        if c > 0:
            mask |= 1 << idx[(r, c - 1)]
        if r > 0 and c < shape[r - 1]:
            mask |= 1 << idx[(r - 1, c)]
        pred[i] = mask

    @lru_cache(None)
    def completion_count(mask: int) -> int:
        if mask == full_mask:
            return 1
        total = 0
        for i in range(n_cells):
            if (mask >> i) & 1:
                continue
            if pred[i] & ~mask:
                continue
            total += completion_count(mask | (1 << i))
        return total

    bucket_counts: Counter[int] = Counter()
    pair_weight = {2: 4, 4: 6, 6: 8}

    def dfs(next_num: int, mask: int, positions: list[int], exponent_sum: int) -> None:
        if next_num == 7:
            bucket_counts[exponent_sum] += completion_count(mask)
            return
        for i, (r, c) in enumerate(cells):
            if (mask >> i) & 1:
                continue
            if pred[i] & ~mask:
                continue
            new_positions = positions + [i]
            new_exponent_sum = exponent_sum
            if next_num in (2, 4, 6):
                prev_i = new_positions[next_num - 2]
                r0, c0 = cells[prev_i]
                if r0 == r:
                    new_exponent_sum += pair_weight[next_num]
                elif c0 == c:
                    new_exponent_sum -= pair_weight[next_num]
                else:
                    continue
            dfs(next_num + 1, mask | (1 << i), new_positions, new_exponent_sum)

    total = completion_count(0)
    dfs(1, 0, [], 0)
    return total, dict(bucket_counts)


def main() -> int:
    w = WitnessBuilder("staircase-ew-disjoint-spectrum", engine="numpy")
    w.set_description(
        "Restored staircase EW probe for the disjoint braid β_EW = σ₁⁴σ₃⁶σ₅⁸ on ρ₃, ρ₄, and the diagonal sector of ρ₅."
    )
    w.set_audit_only("docs/audits/2026-05-07-staircase-ew-disjoint-spectrum.md")
    w.add_parameter("q", float(q0))
    w.add_parameter("betaEWWord", "σ₁^4 · σ₃^6 · σ₅^8")

    k3_dim, k3_counter, _, k3_best = eigen_bucket_counter(staircase_partition(3))
    k4_dim, k4_counter, _, k4_best = eigen_bucket_counter(staircase_partition(4))
    k5_total, k5_bucket_exponents = _k5_counts()
    k5_value_counter = {
        round(float(q0 ** exp), 12): mult
        for exp, mult in sorted(k5_bucket_exponents.items(), reverse=True)
    }
    k5_pure_total = sum(k5_bucket_exponents.values())

    w.add_assertion("rho_3 dimension", k3_dim, 16)
    w.add_assertion("rho_3 exact 8-bucket spectrum", k3_counter == expected_bucket_counter(q0, 2), True)
    w.add_assertion("rho_4 dimension", k4_dim, 768)
    w.add_assertion("rho_4 exact 8-bucket spectrum", k4_counter == expected_bucket_counter(q0, 96), True)
    w.add_assertion("rho_5 total SYT count", k5_total, 292864)
    w.add_assertion("rho_5 pure diagonal sector", k5_pure_total, 52224)

    w.add_data("rho3", {
        "shape": staircase_partition(3),
        "dimension": k3_dim,
        "bucketCounts": dict(k3_counter),
        "bestResidualScan": k3_best,
    })
    w.add_data("rho4", {
        "shape": staircase_partition(4),
        "dimension": k4_dim,
        "bucketCounts": dict(k4_counter),
        "bestResidualScan": k4_best,
    })
    w.add_data("rho5", {
        "shape": staircase_partition(5),
        "dimension": k5_total,
        "pureDiagonalCount": k5_pure_total,
        "bucketExponents": k5_bucket_exponents,
        "bucketCounts": k5_value_counter,
        "note": "Only the diagonal pure sector is counted at k=5; the exact disjoint β_EW buckets remain q^{±18}, q^{±10}, q^{±6}, q^{±2}.",
    })

    w.add_caveat("The stale q^(1/(2k-1)) residual claim is not reproduced for the current disjoint β_EW implementation.")
    w.add_caveat("Any nontrivial residual must come from an interface contribution such as Δ_I, not from σ₁⁴σ₃⁶σ₅⁸ alone.")

    out = w.save()
    print(f"Wrote {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
