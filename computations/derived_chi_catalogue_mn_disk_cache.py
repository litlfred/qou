#!/usr/bin/env python3
"""derived_chi_catalogue_mn_disk_cache.py — Tier 2 disk cache.

Persistent on-disk cache for `pyhecke_native.mn_chi_q(λ, μ)` outputs
— the q-Murnaghan-Nakayama Hecke character table. Entries accumulate
across multiple sweep runs and across processes.

## What's cached

  M_n[λ][μ]  =  mn_chi_q(λ, μ)  =  χ^λ(T_{w_μ}) as a q-Laurent.

For each strand count n that the catalogue uses (3, 6, 9, 12, …, 27),
the table has p(n)² entries. Pre-filling the heavy tables (n=24, 27)
is overnight work; the cache lets that cost amortise across runs.

## File layout

  computations/.derived-chi-mn-cache.json
    { "<lambda_str>|<mu_str>": [[q_degree, "coeff"], …], … }

  Keys: `"2,1|3"` for (λ=(2,1), μ=(3,)).
  Values: list of [q_degree, coefficient_string] pairs.

## Usage

    from derived_chi_catalogue_mn_disk_cache import get_mn_chi_q

    poly = get_mn_chi_q((2, 1), (3,))  # cached lookup; computes + saves on miss

The cache file is loaded lazily on first call and written back via
`atexit`. Concurrent processes are safe (read-then-write merges
disk + memory on save).

## Tier 1 hook

The LR / parabolic factorisation (Tier 1 audit doc) needs many
mn_chi_q lookups. This cache is the substrate for that future work:
once Tier 1 lands, every χ^λ(T_β) on an atomic braid becomes a
fast LR-sum over **cached** mn_chi_q entries.
"""
from __future__ import annotations

import atexit
import json
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


# ── Disk cache file ────────────────────────────────────────────────

_CACHE_FILE = HERE / ".derived-chi-mn-cache.json"


def _encode_key(lam: tuple[int, ...], mu: tuple[int, ...]) -> str:
    return f"{','.join(str(x) for x in lam)}|{','.join(str(x) for x in mu)}"


def _decode_key(key: str) -> tuple[tuple[int, ...], tuple[int, ...]]:
    lam_s, mu_s = key.split("|")
    return (
        tuple(int(x) for x in lam_s.split(",")) if lam_s else (),
        tuple(int(x) for x in mu_s.split(",")) if mu_s else (),
    )


def _load() -> dict[str, list[list]]:
    if _CACHE_FILE.exists():
        try:
            return json.loads(_CACHE_FILE.read_text())
        except json.JSONDecodeError:
            return {}
    return {}


_in_memory: dict[str, list[list]] = _load()
_dirty: bool = False


def _save_atexit() -> None:
    global _dirty
    if not _dirty:
        return
    # Read disk fresh and merge — supports concurrent writers (last-writer-wins
    # on individual keys, but we don't lose entries from other processes).
    on_disk = _load()
    merged = {**on_disk, **_in_memory}
    _CACHE_FILE.write_text(json.dumps(merged, separators=(",", ":")) + "\n")
    _dirty = False


atexit.register(_save_atexit)


# ── Public lookup ──────────────────────────────────────────────────


def get_mn_chi_q(
    lam: tuple[int, ...],
    mu: tuple[int, ...],
) -> list[tuple[int, str]]:
    """Cached lookup. Computes + caches on miss; returns list of
    (q_degree, coefficient) pairs."""
    global _dirty
    key = _encode_key(lam, mu)
    cached = _in_memory.get(key)
    if cached is not None:
        return [(int(d), str(c)) for (d, c) in cached]
    raw = ph.mn_chi_q(list(lam), list(mu))
    converted = [(int(d), str(c)) for (d, c) in raw]
    _in_memory[key] = [[d, c] for (d, c) in converted]
    _dirty = True
    return converted


def cache_stats() -> dict[str, int]:
    """Return (n_entries, file_size_kb) for diagnostics."""
    n = len(_in_memory)
    size = _CACHE_FILE.stat().st_size if _CACHE_FILE.exists() else 0
    return {"entries_in_memory": n, "file_size_kb": size // 1024}


def force_save() -> None:
    """Explicit save (e.g. mid-script before a long sleep / crash risk)."""
    global _dirty
    _dirty = True
    _save_atexit()


# ── Pre-fill helper for an entire H_n character table ─────────────


def prefill_for_n(n: int, *, verbose: bool = False) -> int:
    """Compute and cache every (λ, μ) entry for partitions of n.
    Returns the number of NEW entries added (cache hits already present
    aren't double-counted)."""
    import time
    parts = ph.partitions_of(n)
    parts = [tuple(p) for p in parts]
    total = len(parts) ** 2
    new = 0
    t0 = time.monotonic()
    progress_step = max(1, total // 20)
    done = 0
    for lam in parts:
        for mu in parts:
            key = _encode_key(lam, mu)
            if key not in _in_memory:
                _in_memory[key] = [
                    [int(d), str(c)] for (d, c) in ph.mn_chi_q(list(lam), list(mu))
                ]
                new += 1
                global _dirty
                _dirty = True
            done += 1
            if verbose and done % progress_step == 0:
                pct = 100.0 * done / total
                el = time.monotonic() - t0
                eta = el * (total - done) / max(done, 1)
                print(f"  prefill n={n}: {done}/{total} ({pct:.1f}%) — {el:.1f}s "
                      f"elapsed, ETA {eta:.1f}s, {new} new entries", flush=True)
    return new


if __name__ == "__main__":
    # CLI smoke-test: pre-fill n=6 (deuteron) — 11 partitions ⇒ 121 entries.
    import argparse
    parser = argparse.ArgumentParser(
        description="Pre-fill the M_n disk cache for one or more n values."
    )
    parser.add_argument("n_values", type=int, nargs="+", help="n values to prefill")
    parser.add_argument("--verbose", "-v", action="store_true")
    args = parser.parse_args()
    for n in args.n_values:
        new = prefill_for_n(n, verbose=args.verbose)
        print(f"n={n}: {new} new entries added to disk cache")
        force_save()
    print(f"final cache stats: {cache_stats()}")
