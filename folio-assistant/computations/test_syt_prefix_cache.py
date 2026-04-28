"""pytest for Track 1 — shared SYT-prefix cache for Hoefsmit matrices.

Cached build must produce matrices IDENTICAL to the legacy build
(same generators, same numerical values, to 1e-12) for all partitions
of n = 4..8.  Characters at sample braid words must also match.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))


def _mat_max_abs_diff(A, B):
    """Max |A-B| for numpy arrays or scipy sparse."""
    import numpy as np
    from scipy.sparse import issparse
    if issparse(A) or issparse(B):
        A = A.toarray() if issparse(A) else A
        B = B.toarray() if issparse(B) else B
    return float(np.max(np.abs(A - B)))


def test_cached_matrices_match_legacy_n4_n8():
    """For each λ ⊢ n (n = 4..8), cached build must match legacy
    build of every Hoefsmit matrix to 1e-12."""
    from hecke_characters import (partitions_of, build_seminormal_matrices)
    from syt_prefix_cache import BlockCache, build_seminormal_matrices_cached
    from q_parameter import Q as Q0, HA as H0

    cache = BlockCache(Q0, H0)
    for n in [4, 5, 6, 7, 8]:
        for lam in partitions_of(n):
            lam = tuple(lam)
            s_legacy, d_l, _ = build_seminormal_matrices(lam)
            s_cached, d_c, _ = build_seminormal_matrices_cached(
                lam, cache=cache)
            assert d_l == d_c
            assert len(s_legacy) == len(s_cached)
            for k, (A, B) in enumerate(zip(s_legacy, s_cached)):
                diff = _mat_max_abs_diff(A, B)
                assert diff < 1e-12, (
                    f"λ={lam} σ_{k+1}: max diff = {diff:.3e}")
    # Cache should have had more hits than misses across this sweep
    # (many shapes re-use the same ρ values).
    assert cache.hits > 0, "BlockCache had no hits"


def test_cached_matrices_match_at_qinv():
    """Rebuild matrices at q → 1/q (Track 2 path) — cached build
    must match legacy build at that alternate q."""
    from hecke_characters import partitions_of
    from conjugate_symmetry import _build_seminormal_at_q
    from syt_prefix_cache import BlockCache, build_seminormal_matrices_cached
    from q_parameter import Q as Q0, HA as H0

    cache = BlockCache(Q0, H0)
    q_alt = 1.0 / Q0
    for n in [4, 5, 6]:
        for lam in partitions_of(n):
            lam = tuple(lam)
            s_legacy, d_l = _build_seminormal_at_q(lam, q_alt)
            s_cached, d_c, _ = build_seminormal_matrices_cached(
                lam, cache=cache, q_val=q_alt)
            assert d_l == d_c
            for A, B in zip(s_legacy, s_cached):
                diff = _mat_max_abs_diff(A, B)
                assert diff < 1e-12


def test_cached_character_match_for_sample_words():
    """For λ = (3,2) at n=5 and λ = (2,2,1) at n=5, character of a
    sample braid word must match between cached and legacy paths."""
    import numpy as np
    from hecke_characters import build_seminormal_matrices
    from syt_prefix_cache import BlockCache, build_seminormal_matrices_cached
    from q_parameter import Q as Q0, HA as H0

    cache = BlockCache(Q0, H0)
    words = [(0, 1, 2, 3), (0, 2), (1, 3), (1, 2, 1, 3)]
    for lam in [(3, 2), (2, 2, 1)]:
        s_legacy, d_l, _ = build_seminormal_matrices(lam)
        s_cached, d_c, _ = build_seminormal_matrices_cached(
            lam, cache=cache)
        for w in words:
            if any(g >= len(s_legacy) for g in w):
                continue
            prod_l = np.eye(d_l)
            prod_c = np.eye(d_c)
            for g in w:
                prod_l = prod_l @ s_legacy[g]
                prod_c = prod_c @ s_cached[g]
            chi_l = float(np.trace(prod_l))
            chi_c = float(np.trace(prod_c))
            assert abs(chi_l - chi_c) < 1e-12, (
                f"λ={lam} w={w}: legacy={chi_l} cached={chi_c}")


def test_cache_hits_increase_across_partitions():
    """A single cache reused across all partitions at n=8 should have
    many hits (same ρ values reused)."""
    from hecke_characters import partitions_of
    from syt_prefix_cache import BlockCache, build_seminormal_matrices_cached
    from q_parameter import Q as Q0, HA as H0

    cache = BlockCache(Q0, H0)
    for lam in partitions_of(8):
        build_seminormal_matrices_cached(tuple(lam), cache=cache)
    total = cache.hits + cache.misses
    assert total > 0
    # ρ values are bounded by ±(n-1); each shape uses a small subset.
    # Hit ratio should be substantial after one pass through 22 shapes.
    assert cache.hits > cache.misses, (
        f"Expected hits > misses; got {cache.hits} hits, "
        f"{cache.misses} misses")
