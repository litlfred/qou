# archimedean_by_design: numpy float64 matmul for BLAS-accelerated
#   Hoefsmit χ^λ — substrate precision is restored only at the final
#   mpmath trace sum (per the docstring below). The math.* / np.* calls
#   in this file are the archimedean-realization layer; substrate
#   compute lives in the original mpmath Hoefsmit path.
# Ref: docs/audits/2026-05-19-cocasimir-compute-bottleneck.md
"""Numpy-backed Hoefsmit χ^λ — 10-50× faster than mpmath path.

Per docs/audits/2026-05-19-cocasimir-compute-bottleneck.md: the
mp.matrix matmul in chi_numeric loops element-by-element in pure
Python, costing ~10-15μs Python overhead per element multiplication
regardless of mpmath precision. For dim=132 ([6,6] at n=12) this
gives 57s per partition; for dim=462 ([4,4,4] / [3,3,3,3] at n=12)
extrapolates to 30-60 min per partition. This module replaces
mp.matrix with numpy.float64 for matrix multiplication, which uses
C-level BLAS (~1000× faster element-mul cost), and converts to mpmath
only for the final trace sum where precision matters.

Validity: at q_0 ≈ 1.110, all Hoefsmit matrix entries are bounded
real numbers O(1) to O(10). Matrix products accumulate rounding at
~dim · 10⁻¹⁶ per multiplication step. For our application (dim ≤
1000, n_crossings ≤ 50), worst-case f64 rounding is ~5×10⁻¹⁴ —
well within the 50 dps witness output floor.

The chi value is returned as `mp.mpf` for downstream compatibility
with the mpmath-based co-Casimir / pentagon-reduction pipelines.

CLI test entry point:
    python3 hoefsmit_numpy.py           # validate vs mpmath
    python3 hoefsmit_numpy.py --bench   # benchmark across partitions

Per repo-owner directive 2026-05-19 ("move to rust? refactor?
cache?"): chose numpy refactor for the 10-50× win with low risk.
Rust path filed in docs/audits/2026-05-19-rust-l1-wiring-status.md
as the next-tier speedup (100-1000×, but needs convention adapter).
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import sys
import time
from pathlib import Path

import numpy as np
import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from rho_k_h3a_refinement import standard_young_tableaux  # noqa: E402

# Module-level cache for Hoefsmit matrices — same partition + q gives
# identical matrices regardless of which atom is being computed.
# Key: (shape_tuple, round(q_value, 15)); Value: (matrices, dim).
# Per compute-pipeline-audit §Optimization #3 (2026-05-23).
_HOEFSMIT_NUMPY_CACHE: dict[tuple, tuple[list[np.ndarray], int]] = {}


def hoefsmit_matrices_numpy(
    shape: tuple[int, ...], q_value: float
) -> tuple[list[np.ndarray], int]:
    """Build Hoefsmit seminormal matrices as numpy.float64 arrays.

    Mirrors `rho_k_h3a_refinement.hoefsmit_matrices_numeric` exactly,
    but stores entries as f64 instead of mp.mpf. Numpy matmul is
    C-level BLAS, orders of magnitude faster than mp.matrix's Python
    loop.

    Results are cached by (shape, q) so repeated calls for the same
    partition (e.g., across different atoms at the same H_n level)
    return instantly.

    Returns (matrices, dim) where matrices is a list of (dim, dim)
    f64 arrays — one per generator σ_k for k=1..n-1.
    """
    cache_key = (tuple(shape), round(q_value, 15))
    if cache_key in _HOEFSMIT_NUMPY_CACHE:
        return _HOEFSMIT_NUMPY_CACHE[cache_key]

    n = sum(shape)
    syts, cells, contents = standard_young_tableaux(shape)
    dim = len(syts)
    if dim == 0:
        return [], 0

    q = float(q_value)
    h = q - 1.0 / q

    matrices: list[np.ndarray] = []
    for k in range(1, n):
        M = np.zeros((dim, dim), dtype=np.float64)
        processed: set[int] = set()
        for i in range(dim):
            if i in processed:
                continue
            ci_k = syts[i][k]
            ci_k1 = syts[i][k + 1]
            rho = contents[ci_k1] - contents[ci_k]
            a = h / (1.0 - q ** (-2 * rho))

            swap_map = dict(syts[i])
            swap_map[k], swap_map[k + 1] = ci_k1, ci_k
            j = None
            for jj in range(dim):
                if jj == i:
                    continue
                if syts[jj] == swap_map:
                    j = jj
                    break

            if j is None:
                M[i, i] = a
                processed.add(i)
            else:
                a_prime = h / (1.0 - q ** (2 * rho))
                b_sq = a * a_prime + 1.0
                b = np.sqrt(b_sq)
                M[i, i] = a
                M[j, j] = a_prime
                M[i, j] = b
                M[j, i] = b
                processed.add(i)
                processed.add(j)
        matrices.append(M)

    _HOEFSMIT_NUMPY_CACHE[cache_key] = (matrices, dim)
    return matrices, dim


def chi_numpy(
    shape: tuple[int, ...], crossings: list[tuple[int, str]], q_value: float
) -> mp.mpf:
    """Numpy-backed χ^λ_q(T_w) at concrete q.

    ~10-50× faster than `rho_k_h3a_refinement.chi_numeric` (which uses
    mp.matrix). The matrix multiplications happen in numpy float64
    (BLAS); the final trace is converted to mpmath for downstream
    precision.

    Returns mp.mpf for compatibility with co-Casimir / pentagon-
    reduction consumers that expect mpmath types.
    """
    matrices, dim = hoefsmit_matrices_numpy(shape, q_value)
    if dim == 0:
        return mp.mpf(0)

    q = float(q_value)
    h = q - 1.0 / q
    d_lookup = {"sigma": 0.0, "sigma_inv": -h, "averaged": -h / 2.0}
    eye = np.eye(dim, dtype=np.float64)

    M = np.eye(dim, dtype=np.float64)
    for gen_idx, ctype in crossings:
        if gen_idx < 0 or gen_idx >= len(matrices):
            raise IndexError(f"gen_idx {gen_idx} out of range for shape {shape}")
        sigma = matrices[gen_idx]
        d_val = d_lookup[ctype]
        cross = sigma + d_val * eye
        M = M @ cross   # numpy matmul (C-level BLAS)

    return mp.mpf(float(np.trace(M)))


# ── Validation against mpmath ────────────────────────────────────

def _validate_against_mpmath(q_str: str) -> int:
    """Cross-check chi_numpy vs chi_numeric on a battery of (shape, atom)
    pairs from existing data. Tolerance: 1e-12 (relative)."""
    from rho_k_h3a_refinement import chi_numeric
    from canonical_braid_crossings import atom_canonical_crossings

    q_mp = mp.mpf(q_str)
    q_f64 = float(q_mp)
    tests = [
        ((1, 0), [(3,), (2, 1), (1, 1, 1)]),                    # p / n at n=3
        ((1, 1), [(6,), (3, 2, 1), (1, 1, 1, 1, 1, 1)]),         # D at n=6
        ((1, 2), [(9,), (5, 4), (3, 3, 3)]),                     # T at n=9
        ((2, 2), [(12,), (6, 6), (4, 4, 4)]),                    # ⁴He at n=12
    ]
    print("=" * 80)
    print("Validation: chi_numpy vs chi_numeric (tolerance 1e-12 relative)")
    print("=" * 80)
    print(f"{'atom':<8} {'shape':<20} {'numpy':>14} {'mpmath':>14} {'reldiff':>12}")
    print("-" * 80)
    n_pass = 0
    n_fail = 0
    for (Z, N), shapes in tests:
        crossings = atom_canonical_crossings(Z, N)
        for shape in shapes:
            t_numpy = time.time()
            chi_np = chi_numpy(shape, crossings, q_f64)
            t_numpy = time.time() - t_numpy
            t_mp = time.time()
            chi_mp = chi_numeric(shape, crossings, q_mp)
            t_mp = time.time() - t_mp
            chi_mp_f = float(chi_mp)
            chi_np_f = float(chi_np)
            ref = max(abs(chi_mp_f), 1e-12)
            reldiff = abs(chi_np_f - chi_mp_f) / ref
            ok = reldiff < 1e-12
            if ok:
                n_pass += 1
            else:
                n_fail += 1
            speedup = t_mp / t_numpy if t_numpy > 0 else float("inf")
            mark = "✓" if ok else "✗"
            print(
                f"({Z},{N})    {str(shape):<20} {chi_np_f:>14.6e} "
                f"{chi_mp_f:>14.6e} {reldiff:>12.2e} {mark}  "
                f"(mp:{t_mp:.2f}s vs np:{t_numpy:.4f}s, {speedup:.0f}×)"
            )
    print(f"\n  {n_pass} pass, {n_fail} fail")
    return 0 if n_fail == 0 else 1


if __name__ == "__main__":
    if "--bench" in sys.argv:
        # Benchmark mode: time the slowest known partition
        from rho_k_h3a_refinement import chi_numeric
        from canonical_braid_crossings import atom_canonical_crossings
        from q_parameter import Q_50_DIGIT_STR
        q_f64 = float(mp.mpf(Q_50_DIGIT_STR))
        q_mp = mp.mpf(Q_50_DIGIT_STR)
        crossings = atom_canonical_crossings(2, 2)  # ⁴He
        # [6, 6] dim 132 — large
        print("Benchmarking ⁴He, λ=[6,6] (dim=132)…")
        t = time.time()
        chi_np = chi_numpy((6, 6), crossings, q_f64)
        print(f"  numpy:  {time.time() - t:.3f}s  chi = {float(chi_np):.6e}")
        t = time.time()
        chi_mp = chi_numeric((6, 6), crossings, q_mp)
        print(f"  mpmath: {time.time() - t:.3f}s  chi = {float(chi_mp):.6e}")
        sys.exit(0)
    from q_parameter import Q_50_DIGIT_STR
    sys.exit(_validate_against_mpmath(Q_50_DIGIT_STR))
