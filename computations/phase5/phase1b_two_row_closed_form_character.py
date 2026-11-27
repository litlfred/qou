#!/usr/bin/env python3
"""
Phase 1b: closed-form Hecke character for 2-row partitions via
transfer-matrix method.

For a 2-row partition λ = [n-k, k] of n, the standard Young tableaux
are in bijection with ballot paths (sequences of +1/−1 steps staying
≥ 0). The Hoefsmit seminormal representation is TRIDIAGONAL in this
basis: σ_i acts on the (i−1)-th step of the path.

Key insight: for 2-row partitions, the content difference between
cells i and i+1 of a standard Young tableau depends only on which
ROW the entries are in. If entries i, i+1 are both in row 1 (path
goes +1 then +1 at steps i−1, i), the axial distance ρ > 0. If i
is in row 2 and i+1 in row 1, ρ < 0. If they're in the same column,
it's a 1×1 block.

For a PRODUCT of operators Π_j (c_j·σ_{g_j} + d_j·I), the trace
can be computed via a transfer-matrix approach:

  χ^λ(T_w) = Σ_{paths} Π_{j} M_j(path, step_at_g_j)

where M_j is the diagonal entry of the j-th factor in the
seminormal basis. This avoids the full d_λ × d_λ matrix product.

For 2-row [n-k, k], the SYT are indexed by positions of the k
entries in row 2. The axial distance at position i is:
  ρ(t, i) = c(t, i+1) − c(t, i)
where c(t, j) = (column of j) − (row of j) in tableau t.

This script derives the transfer-matrix formula and verifies it
matches the full matrix computation.

Audit-only.
"""
from __future__ import annotations


# Path bridge (subdirectory refactor — Phase 3, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the cluster subdirectory. The bridge module
# also puts every other cluster subdir on sys.path so cross-
# cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import sys
import time
from pathlib import Path

import mpmath as mp
import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

from _precision import set_compute_dps  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402
from hecke_characters import standard_young_tableaux, build_seminormal_matrices  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402


def syt_two_row(n, k):
    """Enumerate SYT of shape [n-k, k] as sequences of row assignments.

    Returns list of tuples where row_assign[j] ∈ {0, 1} means entry j+1
    is in row 0 (top) or row 1 (bottom). The constraint is that at every
    prefix, #(row 0) ≥ #(row 1) (ballot condition) and total row 1 = k.
    """
    results = []

    def backtrack(pos, r0_count, r1_count, assignment):
        if pos == n:
            if r1_count == k:
                results.append(tuple(assignment))
            return
        # Try row 0
        if r0_count < n - k:
            backtrack(pos + 1, r0_count + 1, r1_count, assignment + [0])
        # Try row 1 (ballot: r1_count + 1 ≤ r0_count)
        if r1_count < k and r1_count + 1 <= r0_count:
            backtrack(pos + 1, r0_count, r1_count + 1, assignment + [1])

    backtrack(0, 0, 0, [])
    return results


def content_from_row_assign(row_assign):
    """Compute content c(j) = col(j) − row(j) for each entry j.

    Entry j is placed in the next available column of its assigned row.
    Contents are 0-indexed: c(j) for entry j+1.
    """
    n = len(row_assign)
    row_fill = [0, 0]  # next column in each row
    contents = [0] * n
    for j in range(n):
        r = row_assign[j]
        col = row_fill[r]
        contents[j] = col - r
        row_fill[r] += 1
    return contents


def axial_distance(contents, i):
    """ρ(i) = c(i+1) − c(i), the axial distance at position i (0-indexed)."""
    return contents[i + 1] - contents[i]


def trace_via_transfer(shape, q_val, braid_pattern):
    """Compute χ^λ(T_w) via per-tableau diagonal-entry product.

    For each SYT t, and each factor (c, d_mult, g) in the braid word,
    compute the DIAGONAL entry of (c·σ_g + d·I) at tableau t:
      entry_t = c · a_ρ(t,g) + d
    where a_ρ = h/(1 − q^{−2ρ}).

    The trace is Σ_t Π_factors entry_t(factors).

    WARNING: this is ONLY exact when the braid word doesn't mix
    off-diagonal paths. For a GENERAL braid word, different SYT
    can exchange amplitude through the off-diagonal b terms. The
    full formula requires tracking all 2^L paths through L off-diagonal
    blocks, not just the diagonal entries.

    For the ⁴He braid word, this "diagonal-only" approximation should
    be checked against the full matrix computation.
    """
    n_val, k_val = shape[0], shape[1] if len(shape) > 1 else 0
    n = n_val + k_val
    q_f = float(q_val)
    h_val = q_f - 1.0 / q_f

    syts = syt_two_row(n, k_val)
    total = 0.0

    for row_assign in syts:
        contents = content_from_row_assign(row_assign)
        product = 1.0

        for (c, d_mult, g) in braid_pattern:
            d = d_mult * h_val
            # g is the generator index (0-based), swaps entries g+1 and g+2
            # Axial distance at generator g: ρ = c(g+2) − c(g+1) = contents[g+1] − contents[g]
            if g >= n - 1:
                continue
            rho = contents[g + 1] - contents[g]
            a_rho = h_val / (1.0 - q_f**(-2 * rho))
            product *= (c * a_rho + d)

        total += product

    return total


def trace_via_full_matrix(shape, q_val, braid_pattern):
    """Compute χ^λ(T_w) via full matrix product (reference)."""
    q_f = float(q_val)
    h_val = q_f - 1.0 / q_f

    sigmas, dim, _ = build_seminormal_matrices(shape, q=q_f)
    if dim == 0:
        return 0.0

    product = np.eye(dim)
    I = np.eye(dim)
    for (c, d_mult, g) in braid_pattern:
        d = d_mult * h_val
        if g >= len(sigmas):
            continue
        M = c * sigmas[g] + d * I
        if hasattr(M, 'toarray'):
            M = M.toarray()
        product = product @ M

    return float(np.trace(product))


def main():
    set_compute_dps()
    t0 = time.time()
    print("=" * 70)
    print("  Phase 1b: 2-row closed-form character via transfer matrix")
    print("=" * 70)
    print()

    # Import braid pattern from phase1a
    from phase1a_symbolic_trace_dominant_h_expansion import _HE4_PATTERN

    q0 = float(Q_MP)
    h0 = q0 - 1.0 / q0

    print(f"  q₀ = {q0:.15f}")
    print(f"  h₀ = {h0:.15f}")
    print(f"  Braid word: {len(_HE4_PATTERN)} crossings")
    print()

    # Test partitions: 2-row partitions of 12
    test_shapes = [(11, 1), (10, 2), (9, 3), (8, 4), (7, 5), (6, 6)]
    results = []

    for shape in test_shapes:
        n, k = shape[0], shape[1]
        N = n + k
        from partition_utils import hook_lengths_with_cells
        from math import factorial, prod
        cells = hook_lengths_with_cells(list(shape))
        d = factorial(N) // prod(hk for (_, _, hk) in cells)

        print(f"  λ = [{n},{k}], d_λ = {d}")

        t1 = time.time()

        # Full matrix reference
        chi_full = trace_via_full_matrix(shape, q0, _HE4_PATTERN)

        # Diagonal-only approximation
        chi_diag = trace_via_transfer(shape, q0, _HE4_PATTERN)

        # Compare
        rel_err = abs(chi_diag - chi_full) / max(abs(chi_full), 1e-15)
        wall = time.time() - t1

        print(f"    χ_full   = {chi_full:+.12e}")
        print(f"    χ_diag   = {chi_diag:+.12e}")
        print(f"    rel_err  = {rel_err:.3e}  {'✓ EXACT' if rel_err < 1e-10 else '✗ differs (off-diagonal mixing)'}")
        print(f"    ({wall:.2f}s)")
        print()

        results.append({
            "partition": list(shape),
            "d_lambda": d,
            "chi_full": chi_full,
            "chi_diag_only": chi_diag,
            "rel_error": rel_err,
            "diagonal_exact": rel_err < 1e-10,
        })

    # Summary
    print("=" * 70)
    n_exact = sum(1 for r in results if r["diagonal_exact"])
    print(f"  Diagonal-only exact: {n_exact}/{len(results)}")
    if n_exact == len(results):
        print("  ALL 2-row partitions have diagonal-only character!")
        print("  → Transfer-matrix closed form is EXACT for this braid word")
        print("  → d_λ × d_λ matrix product can be replaced by O(d_λ) sum")
        print("  → speedup factor: d_λ for each partition")
    else:
        print("  Some partitions have off-diagonal mixing — transfer matrix")
        print("  is an approximation for those shapes. Need full matrix there.")

    elapsed = time.time() - t0
    print(f"\n  Total wall time: {elapsed:.1f}s")

    # Witness
    w = WitnessBuilder("phase1b-two-row-transfer-matrix", engine="python")
    w.set_description(
        "Tests whether the diagonal-only transfer-matrix formula "
        "gives the exact Hecke character for 2-row partitions of "
        "⁴He's braid word. If exact, replaces O(d_λ²) matrix "
        "product with O(d_λ) sum — massive speedup for d_λ=297."
    )
    w.set_content_block("conj:psd-trace-orthogonality")
    w.set_audit_only("docs/audits/2026-05-26-phase1b-two-row-transfer-matrix.md")
    w.add_data("results", results)
    w.add_assertion(
        name="diagonal_only_refuted",
        computed=1 if n_exact == 0 else 0,
        expected=1,
        tolerance=0,
        source="Falsification probe: diagonal-only should NOT match (off-diagonal mixing expected)"
    )
    out = w.save()
    print(f"\n  Witness: {out}")


if __name__ == "__main__":
    main()
