#!/usr/bin/env python3
"""Prefix-cache infrastructure for atomic-braid Markov-trace compute.

When computing `tr_M(β_K)` for a series of atoms (mass-table sweep
or any user-driven sequence), the atoms' signed words often share
prefixes — most notably, **⁵Li IS a strict prefix of ⁶Li**, and
3He IS a strict prefix of 4He, etc.  See the empirical prefix-
structure check in `markov_peel_rust_bridge` (2026-05-22).

When a new atom is computed, the longest cached signed-word prefix
that matches the new atom's word is identified.  The cached
*reduced* LaurentHeckeElement at that prefix is loaded, and only
the SUFFIX (the additional crossings) is reduced — collapsing the
exponential term-count growth that dominates the wall on heavy
atoms.

Cache format: one JSON file per cached prefix, keyed by SHA-256 of
the signed-word prefix.  Contents:
  - `cache_version`: bumps on any incompatible algorithm change
  - `signed_word_prefix`: the prefix (for prefix-match comparison)
  - `state_ffi`: serialised LaurentHeckeElement (per `to_ffi()`)
  - `n_strands_at_prefix`: H_n the state lives in
  - `wall_seconds_to_reach`: wall to reduce from scratch (for analytics)
  - `created_at`: ISO timestamp

Tier 1.A / Tier 1.D follow-up from
`docs/audits/2026-05-20-compute-optimization-roadmap.md`.
"""
from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

# Bump this any time the LaurentHeckeElement FFI format or the
# reduce-rules algorithm changes in a way that invalidates cached
# states (e.g., new rule, changed rule order, GCD policy switch).
CACHE_FORMAT_VERSION = "0.8.0-laurent-q-rust-r1+r2+r3+gcd-defer+fxhash"

CACHE_DIR = Path(__file__).resolve().parent / "atomic-prefix-cache"


def _hash_prefix(signed_word_prefix: list[tuple[int, int]]) -> str:
    """Stable hex hash of a signed-word prefix.  16 hex chars
    (~64 bits) is more than enough to avoid collisions at our
    cache scale (≤ thousands of entries)."""
    payload = json.dumps(
        [list(t) for t in signed_word_prefix], sort_keys=True
    ).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()[:16]


def _cache_path(prefix_hash: str) -> Path:
    # `.prefix.cache.json` (not `.witness.json`) — the witness
    # naming is reserved for WitnessBuilder-emitted JSON tracked by
    # the compute-audit P30 check (Copilot review r3291263635).
    return CACHE_DIR / f"{prefix_hash}.prefix.cache.json"


def save_prefix_state(
    signed_word_prefix: list[tuple[int, int]],
    state_ffi: Any,
    n_strands_at_prefix: int,
    wall_seconds: float,
) -> Path:
    """Persist a reduced state for a signed-word prefix.

    `state_ffi` is whatever `pyhecke_native.tr_m_atomic_mpfr_with_state`
    returned as the second element (the FFI shape of the final
    LaurentHeckeElement).
    """
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    h = _hash_prefix(signed_word_prefix)
    path = _cache_path(h)
    data = {
        "cache_version": CACHE_FORMAT_VERSION,
        "signed_word_prefix": [list(t) for t in signed_word_prefix],
        "prefix_len": len(signed_word_prefix),
        "n_strands_at_prefix": n_strands_at_prefix,
        "state_ffi": state_ffi,
        "wall_seconds_to_reach": float(wall_seconds),
        "created_at": datetime.now(timezone.utc).isoformat(),
    }
    # Write atomically via a temp file + rename so a partial write
    # never leaves a corrupt cache entry.
    tmp = path.with_suffix(".tmp")
    tmp.write_text(json.dumps(data))
    tmp.replace(path)
    return path


def _restore_ffi_tuples(state_ffi_json: list) -> list:
    """JSON-roundtrip converts inner tuples to lists; PyO3 requires
    tuples for `Vec<(Vec<i32>, Vec<(i32, String, String)>)>`.
    Restore the tuple structure expected by the FFI."""
    return [
        (
            list(entry[0]),
            [tuple(t) for t in entry[1]],
        )
        for entry in state_ffi_json
    ]


def load_prefix_state(
    signed_word_prefix: list[tuple[int, int]],
) -> Any | None:
    """Load the reduced state for `signed_word_prefix` if cached
    AND the cache_version matches the current one.  Stale entries
    are ignored (caller falls through to recompute)."""
    h = _hash_prefix(signed_word_prefix)
    path = _cache_path(h)
    if not path.exists():
        return None
    try:
        data = json.loads(path.read_text())
    except (json.JSONDecodeError, OSError):
        return None
    if data.get("cache_version") != CACHE_FORMAT_VERSION:
        return None
    # Defensive: re-check the prefix matches (collision-paranoia).
    cached_prefix = data.get("signed_word_prefix")
    if cached_prefix != [list(t) for t in signed_word_prefix]:
        return None
    state_ffi_json = data.get("state_ffi")
    if state_ffi_json is None:
        return None
    return _restore_ffi_tuples(state_ffi_json)


def find_longest_cached_prefix(
    signed_word: list[tuple[int, int]],
) -> tuple[int, Any | None]:
    """Scan the cache for the longest signed-word prefix that is a
    *strict prefix* of `signed_word`, return `(prefix_len, state_ffi)`.

    If no cached prefix matches, returns `(0, None)`.

    Scan is O(N · cache_size) — fine for the current scale
    (< 100 atoms, ~50 KB - 50 MB per entry).  Index by first-N-
    elements hash if the cache grows large.
    """
    if not CACHE_DIR.exists():
        return (0, None)
    best_len = 0
    best_state = None
    sw_lists = [list(t) for t in signed_word]
    for path in CACHE_DIR.glob("*.prefix.cache.json"):
        try:
            data = json.loads(path.read_text())
        except (json.JSONDecodeError, OSError):
            continue
        if data.get("cache_version") != CACHE_FORMAT_VERSION:
            continue
        prefix = data.get("signed_word_prefix")
        if not prefix:
            continue
        prefix_len = len(prefix)
        if prefix_len <= best_len:
            continue
        if prefix_len > len(sw_lists):
            continue
        # Strict prefix check.
        if sw_lists[:prefix_len] == prefix:
            best_len = prefix_len
            state_ffi_json = data.get("state_ffi")
            best_state = (
                _restore_ffi_tuples(state_ffi_json)
                if state_ffi_json is not None
                else None
            )
    return (best_len, best_state)


def clear_cache() -> int:
    """Remove all cached prefix witnesses.  Returns count removed."""
    if not CACHE_DIR.exists():
        return 0
    count = 0
    for path in CACHE_DIR.glob("*.prefix.cache.json"):
        try:
            path.unlink()
            count += 1
        except OSError:
            pass
    return count


def stats() -> dict:
    """Summary of the cache contents (for debug + dashboards)."""
    if not CACHE_DIR.exists():
        return {"entries": 0, "total_bytes": 0, "dir": str(CACHE_DIR)}
    entries = []
    total_bytes = 0
    for path in CACHE_DIR.glob("*.prefix.cache.json"):
        size = path.stat().st_size
        total_bytes += size
        try:
            data = json.loads(path.read_text())
            entries.append({
                "prefix_len": data.get("prefix_len", 0),
                "n_strands": data.get("n_strands_at_prefix"),
                "version": data.get("cache_version"),
                "wall_seconds": data.get("wall_seconds_to_reach"),
                "bytes": size,
                "filename": path.name,
            })
        except (json.JSONDecodeError, OSError):
            entries.append({
                "filename": path.name, "bytes": size, "error": "unreadable",
            })
    return {
        "entries": len(entries),
        "total_bytes": total_bytes,
        "dir": str(CACHE_DIR),
        "items": sorted(
            entries, key=lambda e: -e.get("prefix_len", 0) or 0
        ),
    }


__all__ = [
    "CACHE_FORMAT_VERSION",
    "CACHE_DIR",
    "save_prefix_state",
    "load_prefix_state",
    "find_longest_cached_prefix",
    "clear_cache",
    "stats",
]
