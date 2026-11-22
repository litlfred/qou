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

## Where it lives (migrated 2026-11-22 onto the shared branch-cache layer)

  The `mn-chi-cache` family declared in qou.json: one orphan branch
  `cat/qou/mn-chi-cache/mn-chi-q-<engine-key>`, where the engine key is the
  wheel-cache / trace-cache source key (git trees of tools/pyhecke-native and
  tools/hecke-engine). Locally, an fsync'd journal under
  `$QOU_MN_CHI_CACHE_DIR` (default `~/.cache/qou/mn-chi-cache/<member>/`).
  Entries: `{"l": "2,1", "m": "3", "v": [[q_degree, "coeff"], ...]}`, the
  producer's exact coefficient strings. See computations/_branch_cache.py.

  Before the migration the cache was one in-tree file,
  `computations/.derived-chi-mn-cache.json`, keyed by (λ, μ) ALONE: an entry
  written by one engine build was served to every later build. It was neither
  tracked nor gitignored. That file is no longer read or written.

  A dirty engine tree has no key, so the branch store is off for the run
  (values are still memoised in-process). Before serving any loaded entry, a
  sample (`QOU_MN_CHI_CACHE_VERIFY`, default 4) is recomputed with the live
  binary and compared exactly; one mismatch refuses the whole cache.

## Usage

    from derived_chi_catalogue_mn_disk_cache import get_mn_chi_q

    poly = get_mn_chi_q((2, 1), (3,))  # cached lookup; computes + saves on miss

The store is opened on first call (restore + verification), every new
entry is appended to the local journal at once, and, only when
`QOU_MN_CHI_CACHE_PUSH=1` is set, the unpublished entries are seeded to the
branch as one shard at exit (or on `force_save()`). Pushing to origin is off by
default; restoring from the branch is on (`QOU_MN_CHI_CACHE_RESTORE=0` turns it
off).
Concurrent writers are safe: shards are content-addressed and a seed that
loses the race refetches and re-applies.

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
_PYHECKE_PATH = str(HERE.parent.parent / "tools" / "pyhecke-native" / "python")
if _PYHECKE_PATH not in sys.path:
    sys.path.insert(0, _PYHECKE_PATH)

import pyhecke_native as ph  # noqa: E402


# ── Branch-cache store (shared layer: computations/_branch_cache.py) ──

import os  # noqa: E402
import random  # noqa: E402

sys.path.insert(0, str(HERE))
import _branch_cache as _bc  # noqa: E402

KIND = "mn-chi-cache"
_ENGINE_SRCS = ("tools/pyhecke-native", "tools/hecke-engine")  # wheel-cache's order


def _encode_key(lam: tuple[int, ...], mu: tuple[int, ...]) -> str:
    return f"{','.join(str(x) for x in lam)}|{','.join(str(x) for x in mu)}"


def _decode_key(key: str) -> tuple[tuple[int, ...], tuple[int, ...]]:
    lam_s, mu_s = key.split("|")
    return (
        tuple(int(x) for x in lam_s.split(",")) if lam_s else (),
        tuple(int(x) for x in mu_s.split(",")) if mu_s else (),
    )


def _member():
    key, why = _bc.source_key("engine sources", _ENGINE_SRCS)
    return (f"mn-chi-q-{key}", "") if key else (None, why)


def _open_store() -> "_bc.ShardedCache":
    store = _bc.ShardedCache(
        KIND,
        member_fn=_member,
        restore_argv=lambda m, d: ["bash", str(_bc.CLI), "shard-restore", KIND, m, d],
        seed_argv=lambda m, p: _seed_argv(store, m, p),
        key_of=lambda rec: (rec["l"], rec["m"]),
        rec_of=lambda k, v: {"l": k[0], "m": k[1], "v": v},
        env="QOU_MN_CHI_CACHE", log=lambda msg: print(msg, file=sys.stderr))
    _verify(store)
    return store


def _seed_argv(store, member, shard):
    meta = {"function": "mn-chi-q", "engineKey": member.rsplit("-", 1)[1],
            "sourceTrees": _bc.source_trees(_ENGINE_SRCS)}
    readme = (f"# {member}\n\nOne member of qou's `mn-chi-cache` family (declared in "
              "qou.json; kind in `typologies/mn-chi-cache.json`). Exact "
              "`pyhecke_native.mn_chi_q(lambda, mu)` q-Laurent coefficients, keyed by "
              "(lambda, mu). Read and written by "
              "`computations/derived_chi_catalogue_mn_disk_cache.py`. Never edit by hand.")
    return _bc.generic_seed_argv(KIND, meta, readme, store.dir / "local")(member, shard)


def _compute(lam, mu) -> list[list]:
    return [[int(d), str(c)] for (d, c) in ph.mn_chi_q(list(lam), list(mu))]


def _verify(store) -> None:
    if not store.enabled or not store.values:
        return
    k = int(os.environ.get("QOU_MN_CHI_CACHE_VERIFY", "4"))
    if k <= 0:
        store.log(f"  {KIND}: verification sample DISABLED (QOU_MN_CHI_CACHE_VERIFY=0)")
        return
    keys = sorted(store.values, key=lambda t: (len(t[0]), len(t[1]), t))
    sample = keys[:max(k - 1, 1)]
    rest = keys[len(sample):]
    if rest:
        sample.append(random.Random(0).choice(rest))
    for key in sample:
        lam, mu = _decode_key(f"{key[0]}|{key[1]}")
        got = _compute(lam, mu)
        if got != store.values[key]:
            store.refuse()
            raise RuntimeError(
                f"{KIND}: stored mn_chi_q{lam}{mu} disagrees with the installed "
                f"pyhecke_native ({got!r} vs {store.values[key]!r}); the binary was not "
                "built from the keyed sources. Refusing the cache.")
    store.log(f"  {KIND}: verified {len(sample)} stored entries against the live binary "
              "— all identical")


_store = None
_in_memory: dict[str, list[list]] = {}   # in-process memo (works with the store off)


def _get_store():
    global _store
    if _store is None:
        _store = _open_store()
        if _store.enabled:
            for (l, m), v in _store.values.items():
                _in_memory[f"{l}|{m}"] = v
    return _store


def _record(key: str, value: list[list]) -> None:
    _in_memory[key] = value
    lam_s, mu_s = key.split("|")
    _get_store().put_many([((lam_s, mu_s), value)])


def _save_atexit() -> None:
    if _store is not None:
        _store.publish()


atexit.register(_save_atexit)


# ── Public lookup ──────────────────────────────────────────────────


def get_mn_chi_q(
    lam: tuple[int, ...],
    mu: tuple[int, ...],
) -> list[tuple[int, str]]:
    """Cached lookup. Computes + caches on miss; returns list of
    (q_degree, coefficient) pairs."""
    st = _get_store()
    key = _encode_key(lam, mu)
    cached = _in_memory.get(key)
    if cached is not None:
        st.hits += 1
        return [(int(d), str(c)) for (d, c) in cached]
    st.misses += 1
    value = _compute(lam, mu)
    _record(key, value)
    return [(d, c) for (d, c) in value]


def cache_stats() -> dict[str, int]:
    """Return (n_entries, file_size_kb) for diagnostics."""
    st = _get_store()
    size = (sum(f.stat().st_size for f in (st.dir / "local").glob("*.jsonl"))
            if st.enabled else 0)
    return {"entries_in_memory": len(_in_memory), "file_size_kb": size // 1024}


def force_save() -> None:
    """Explicit publish to the branch store (every entry is already in the
    fsync'd local journal, so a crash loses nothing)."""
    _save_atexit()


# ── Pre-fill helper for an entire H_n character table ─────────────


def prefill_for_n(n: int, *, verbose: bool = False) -> int:
    """Compute and cache every (λ, μ) entry for partitions of n.
    Returns the number of NEW entries added (cache hits already present
    aren't double-counted)."""
    import time
    _get_store()
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
                _record(key, _compute(lam, mu))
                new += 1
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
        print(f"n={n}: {new} new entries added to the cache")
        force_save()
    print(f"final cache stats: {cache_stats()}")
