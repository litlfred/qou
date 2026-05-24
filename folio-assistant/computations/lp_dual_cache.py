#!/usr/bin/env python3
# archimedean_by_design: thin LRU wrapper around scipy's LP/SDP
#   solver. Scipy uses float64 internally; this module's float type
#   signatures reflect that boundary. Substrate-precision callers
#   convert to mp.mpf at the boundary.
"""
LRU cache for the operator-selection LP / SDP solver.

``solve_operator_selection_lp`` is called repeatedly across compute
sweeps with overlapping (t, G, n_target) triples — every Wedderburn
block hit during a parameter sweep, every shadow-price re-evaluation
in run_pipeline.py, every CI re-run that doesn't have a witness
hash hit.  This module wraps the core solver with a content-addressed
LRU cache so that repeated calls return in O(hash) time.

Public API
----------
``cached_solve_operator_selection_lp(t, G, n_target, **kwargs)``
    Cached wrapper around ``lp_dual_solver.solve_operator_selection_lp``.

``cached_solve_psd_operator_selection_sdp(t, G, n_target)``
    Cached wrapper around the SDP variant.

``lp_cache_info()``
    Dict: ``{lp_hits, lp_misses, sdp_hits, sdp_misses}``.

``clear_lp_cache()``
    Drop both caches (use after schema / Gram-matrix convention changes).

Design notes
------------
* The cache key is the bytes representation of (t, G, n_target,
  sorted(kwargs)).  This makes the cache content-addressed: identical
  numeric inputs hit, even across processes if you pickle the result.
* The cache is **opt-in** — existing callers of
  ``solve_operator_selection_lp`` are untouched.  Only call sites that
  benefit from memoization (sweeps, batch witnesses) should switch to
  the cached entry point.
* Default ``maxsize=1024`` covers a typical n=6..8 Wedderburn sweep
  comfortably.  Override via ``set_lp_cache_size(n)`` for larger sweeps.
"""
from __future__ import annotations

import hashlib
import json
from typing import Any

import numpy as np

from lp_dual_solver import (
    LpDualResult,
    SdpDualResult,
    solve_operator_selection_lp,
    solve_psd_operator_selection_sdp,
)

# Module-level state (kept tiny; the heavy data lives inside the caches).
_lp_cache_maxsize = 1024
_sdp_cache_maxsize = 256


def _array_key(arr: np.ndarray) -> bytes:
    """Stable bytes key for a numpy array (shape + dtype + raw bytes)."""
    a = np.ascontiguousarray(np.asarray(arr, dtype=np.float64))
    return (
        repr(a.shape).encode()
        + b"|"
        + a.dtype.str.encode()
        + b"|"
        + hashlib.blake2b(a.tobytes(), digest_size=16).digest()
    )


def _kwargs_key(kw: dict[str, Any]) -> bytes:
    """Stable bytes key for a kwargs dict."""
    return json.dumps(kw, sort_keys=True, default=str).encode()


# ── LP cache ───────────────────────────────────────────────────

_LP_RESULTS: dict[bytes, dict] = {}
_LP_HITS = 0
_LP_MISSES = 0


def cached_solve_operator_selection_lp(
    t: np.ndarray,
    G: np.ndarray,
    n_target: float,
    **kwargs: Any,
) -> LpDualResult:
    """Cached wrapper around ``solve_operator_selection_lp``.

    Returns a fresh ``LpDualResult`` reconstructed from the cached
    ``to_dict()`` payload, so callers may mutate it without leaking
    into the cache.
    """
    global _LP_HITS, _LP_MISSES
    key = (
        _array_key(t)
        + b"||"
        + _array_key(G)
        + b"||"
        + repr(float(n_target)).encode()
        + b"||"
        + _kwargs_key(kwargs)
    )
    payload = _LP_RESULTS.get(key)
    if payload is None:
        _LP_MISSES += 1
        result = solve_operator_selection_lp(t, G, n_target, **kwargs)
        payload = result.to_dict()
        _LP_RESULTS[key] = payload
        _evict_if_oversize(_LP_RESULTS, _lp_cache_maxsize)
    else:
        _LP_HITS += 1
    return LpDualResult(
        x_star=list(payload["x_star"]),
        y0_star=float(payload["y0_star"]),
        y_star=list(payload["y_star"]),
        active_set=list(payload["active_set"]),
        primal_obj=float(payload["primal_obj"]),
        dual_obj=float(payload["dual_obj"]),
        duality_gap=float(payload["duality_gap"]),
        feasible=bool(payload["feasible"]),
    )


# ── SDP cache (smaller, since cvxpy solves are heavier and rarer) ─

_SDP_RESULTS: dict[bytes, dict] = {}
_SDP_HITS = 0
_SDP_MISSES = 0


def cached_solve_psd_operator_selection_sdp(
    t: np.ndarray,
    G: np.ndarray,
    n_target: float,
) -> SdpDualResult:
    """Cached wrapper around ``solve_psd_operator_selection_sdp``."""
    global _SDP_HITS, _SDP_MISSES
    key = (
        _array_key(t)
        + b"||"
        + _array_key(G)
        + b"||"
        + repr(float(n_target)).encode()
    )
    payload = _SDP_RESULTS.get(key)
    if payload is None:
        _SDP_MISSES += 1
        result = solve_psd_operator_selection_sdp(t, G, n_target)
        payload = result.to_dict()
        _SDP_RESULTS[key] = payload
        _evict_if_oversize(_SDP_RESULTS, _sdp_cache_maxsize)
    else:
        _SDP_HITS += 1
    return SdpDualResult(
        X_star=list(payload["X_star"]),
        Z_star=list(payload["Z_star"]),
        primal_obj=float(payload["primal_obj"]),
        dual_obj=float(payload["dual_obj"]),
        duality_gap=float(payload["duality_gap"]),
        eigenvalues=list(payload["eigenvalues"]),
        feasible=bool(payload["feasible"]),
    )


# ── Cache management ──────────────────────────────────────────

def _evict_if_oversize(d: dict, maxsize: int) -> None:
    """Trim ``d`` to ``maxsize`` entries by FIFO order (cheap LRU
    surrogate; Python ≥3.7 dicts preserve insertion order)."""
    while len(d) > maxsize:
        d.pop(next(iter(d)))


def set_lp_cache_size(n: int) -> None:
    """Reset the LP cache capacity (default 1024)."""
    global _lp_cache_maxsize
    _lp_cache_maxsize = max(1, int(n))
    _evict_if_oversize(_LP_RESULTS, _lp_cache_maxsize)


def set_sdp_cache_size(n: int) -> None:
    """Reset the SDP cache capacity (default 256)."""
    global _sdp_cache_maxsize
    _sdp_cache_maxsize = max(1, int(n))
    _evict_if_oversize(_SDP_RESULTS, _sdp_cache_maxsize)


def lp_cache_info() -> dict:
    """Return current cache hit / miss counters and sizes."""
    return {
        "lp_hits": _LP_HITS,
        "lp_misses": _LP_MISSES,
        "lp_size": len(_LP_RESULTS),
        "lp_maxsize": _lp_cache_maxsize,
        "sdp_hits": _SDP_HITS,
        "sdp_misses": _SDP_MISSES,
        "sdp_size": len(_SDP_RESULTS),
        "sdp_maxsize": _sdp_cache_maxsize,
    }


def clear_lp_cache() -> None:
    """Drop both LP and SDP caches and reset counters."""
    global _LP_HITS, _LP_MISSES, _SDP_HITS, _SDP_MISSES
    _LP_RESULTS.clear()
    _SDP_RESULTS.clear()
    _LP_HITS = _LP_MISSES = 0
    _SDP_HITS = _SDP_MISSES = 0


# ── CLI: smoke + hit-rate demo ──────────────────────────────

if __name__ == "__main__":
    print("=" * 70)
    print("LP-cache smoke test")
    print("=" * 70)
    t = np.array([1.0, 0.5, 0.3])
    G = np.array([[1.0, 0.2, 0.1],
                  [0.2, 1.0, 0.3],
                  [0.1, 0.3, 1.0]])
    n_target = 1.0

    clear_lp_cache()
    # First call: miss
    r1 = cached_solve_operator_selection_lp(t, G, n_target)
    # Subsequent identical calls: hits
    for _ in range(99):
        cached_solve_operator_selection_lp(t, G, n_target)
    info = lp_cache_info()
    print(f"  After 100 identical LP calls: "
          f"hits={info['lp_hits']} misses={info['lp_misses']} "
          f"size={info['lp_size']}")
    assert info["lp_hits"] == 99 and info["lp_misses"] == 1, \
        f"Cache not behaving: {info}"

    # Slightly perturb t → cache miss
    t2 = t.copy()
    t2[0] += 1e-12  # different bytes, even if numerically identical
    cached_solve_operator_selection_lp(t2, G, n_target)
    info = lp_cache_info()
    print(f"  After 1 perturbed call:        "
          f"hits={info['lp_hits']} misses={info['lp_misses']} "
          f"size={info['lp_size']}")
    assert info["lp_misses"] == 2

    # Result equivalence
    r2 = cached_solve_operator_selection_lp(t, G, n_target)
    assert r1.to_dict() == r2.to_dict(), "cached result drift"
    print("  ✓ Cache returns equivalent LpDualResult on hit")
    print()
    print(f"  Final: {lp_cache_info()}")
