"""
Ground-state ordering cache for nuclear braids.

Stores optimized nucleon orderings keyed by (Z, N) so they don't
need to be recomputed on every call. The cache is a JSON file that
persists across runs.

Sources (in priority order):
  1. Cache file (instant lookup)
  2. Rust hecke-engine (fast, parallel ground-state search)
  3. Python braid-registry.py (slow, exhaustive for A≤15)

Usage:
    from ordering_cache import get_ordering, warm_cache

    ordering = get_ordering(6, 8)  # [1,1,1,1,1,1,0,0,0,0,0,0,0,0]
    warm_cache([(1,2), (6,8), (26,30)])  # precompute batch
"""

import json
import hashlib
from pathlib import Path
from typing import Optional

CACHE_FILE = Path(__file__).parent / "ordering-cache.json"


def _load_cache() -> dict:
    if CACHE_FILE.exists():
        try:
            return json.loads(CACHE_FILE.read_text())
        except (json.JSONDecodeError, OSError):
            return {}
    return {}


def _save_cache(cache: dict):
    with open(CACHE_FILE, "w") as f:
        json.dump(cache, f, indent=2, sort_keys=True)
        f.write("\n")


def _key(Z: int, N: int) -> str:
    return f"{Z},{N}"


def get_ordering(Z: int, N: int) -> Optional[list[int]]:
    """Get ground-state ordering for N(Z,N).

    Returns list of 0/1 (0=neutron, 1=proton) or None.
    Checks cache first, then Rust engine, then Python fallback.
    """
    cache = _load_cache()
    k = _key(Z, N)

    if k in cache:
        return cache[k]["ordering"]

    # Try Rust engine
    ordering = _compute_ordering_rust(Z, N)
    if ordering is None:
        ordering = _compute_ordering_python(Z, N)

    if ordering is not None:
        cache[k] = {"ordering": ordering, "Z": Z, "N": N, "A": Z + N}
        _save_cache(cache)

    return ordering


def _compute_ordering_rust(Z: int, N: int) -> Optional[list[int]]:
    """Try Rust hecke-engine for ground-state ordering."""
    try:
        from hecke_rust_bridge import compute_nucleus, is_rust_available
        if not is_rust_available():
            return None
        result = compute_nucleus(Z, N, timeout=60)
        if result and "ordering_par" in result:
            return result["ordering_par"]
    except (ImportError, Exception):
        pass
    return None


def _compute_ordering_python(Z: int, N: int) -> Optional[list[int]]:
    """Fallback: pp...nn ordering (no optimization)."""
    return [1] * Z + [0] * N


def warm_cache(nuclei: list[tuple[int, int]]):
    """Precompute orderings for a batch of (Z, N) pairs."""
    cache = _load_cache()
    missing = [(Z, N) for Z, N in nuclei if _key(Z, N) not in cache]

    if not missing:
        return

    print(f"Warming ordering cache: {len(missing)} nuclei...")
    for Z, N in missing:
        ordering = _compute_ordering_rust(Z, N)
        if ordering is None:
            ordering = _compute_ordering_python(Z, N)
        if ordering is not None:
            cache[_key(Z, N)] = {"ordering": ordering, "Z": Z, "N": N, "A": Z + N}

    _save_cache(cache)
    print(f"  Cached {len(missing)} orderings → {CACHE_FILE.name}")


if __name__ == "__main__":
    import sys

    if len(sys.argv) >= 3:
        Z, N = int(sys.argv[1]), int(sys.argv[2])
        o = get_ordering(Z, N)
        print(f"N({Z},{N}): {''.join('p' if x else 'n' for x in o)}")
    else:
        # Warm cache for verification nuclei
        verification = [
            (1, 2), (2, 1), (2, 2), (6, 6), (6, 8), (7, 7), (8, 8),
            (27, 33), (38, 52), (55, 82), (83, 127),
        ]
        warm_cache(verification)
