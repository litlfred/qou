#!/usr/bin/env python3
"""derived_chi_catalogue_memoize.py — Tier 4 optimization.

Memoization of the pyhecke_native primitives that are class-function
invariants (depend only on partition shape, not on a specific braid
or atom). Within a single multi-atom sweep, the same (λ, μ) inputs
recur often; an in-memory cache turns those into ~free lookups.

## What gets cached

  - `mn_chi_q(λ, μ)` — q-Murnaghan-Nakayama Hecke character on the
    cycle-type-class basis. Pure class function; same value across
    every atom.
  - `partitions_of(n)` — partition enumeration. p(n) entries; tiny
    but called per-atom in the sweep loop.

## Cache scope

In-memory `functools.lru_cache` (unbounded). Within a single Python
process, full hit rate after warmup. Across processes — no persistence
(by design; the disk cache lives in `derived_chi_catalogue_mn_table.py`
as the Tier 2 layer).

## Usage

    from derived_chi_catalogue_memoize import (
        mn_chi_q_cached, partitions_of_cached, cache_info_summary,
    )
    poly = mn_chi_q_cached((2, 1), (2, 1))  # tuple inputs for hashability
    ...
    print(cache_info_summary())
"""
from __future__ import annotations

import functools
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
# Repo root by LANDMARK SEARCH, not by counting `.parent`s: the fixed
# count was off by one and resolved OUTSIDE the repo, so this bootstrap
# never fired -- masked because `_path_bridge`/PYTHONPATH already supplies
# the same directory in every in-repo run. Bean qou-rug0.
_QOU_REPO_ROOT = next(
    (_a for _a in Path(__file__).resolve().parents
     if (_a / "tools").is_dir() and (_a / "computations").is_dir()),
    Path(__file__).resolve().parent,
)
_PYHECKE_PATH = str(_QOU_REPO_ROOT / "tools" / "pyhecke-native" / "python")
if _PYHECKE_PATH not in sys.path:
    sys.path.insert(0, _PYHECKE_PATH)

import pyhecke_native as ph  # noqa: E402


# ── Memoized wrappers (tuple inputs so they hash) ─────────────────


@functools.lru_cache(maxsize=None)
def mn_chi_q_cached(
    lambda_tup: tuple[int, ...],
    mu_tup: tuple[int, ...],
) -> tuple[tuple[int, str], ...]:
    """Cached q-Murnaghan-Nakayama character.

    Returns a tuple-of-tuples (so the cached value is itself hashable);
    callers convert back to list as needed."""
    result = ph.mn_chi_q(list(lambda_tup), list(mu_tup))
    return tuple((int(d), str(c)) for (d, c) in result)


@functools.lru_cache(maxsize=None)
def partitions_of_cached(n: int) -> tuple[tuple[int, ...], ...]:
    """Cached partition enumeration. Returns tuple-of-tuples for
    cheap immutability."""
    return tuple(tuple(p) for p in ph.partitions_of(n))


# ── Diagnostics ────────────────────────────────────────────────────


def cache_info_summary() -> str:
    """Return a one-line summary of every cached primitive's hit-rate."""
    parts = []
    for fn in (mn_chi_q_cached, partitions_of_cached):
        info = fn.cache_info()
        hit_rate = (
            100.0 * info.hits / (info.hits + info.misses)
            if (info.hits + info.misses) > 0 else 0.0
        )
        parts.append(
            f"{fn.__name__}: {info.hits} hits / {info.hits + info.misses} calls "
            f"({hit_rate:.1f}% hit) — {info.currsize} cached"
        )
    return " | ".join(parts)


def clear_caches() -> None:
    """Drop every cached value. Useful for benchmarks and testing."""
    mn_chi_q_cached.cache_clear()
    partitions_of_cached.cache_clear()


# ── Quick self-test on import (no side effects in production) ─────


if __name__ == "__main__":
    # Smoke-test the cache works and matches pyhecke_native directly.
    direct = ph.mn_chi_q([2, 1], [2, 1])
    cached_a = mn_chi_q_cached((2, 1), (2, 1))
    cached_b = mn_chi_q_cached((2, 1), (2, 1))  # cache hit
    print(f"direct  : {direct}")
    print(f"cached  : {list(cached_a)}")
    assert list(cached_a) == direct, "memoization mismatch!"
    assert cached_a is cached_b, "cache hit returned a different object"
    print(f"cache state: {cache_info_summary()}")
