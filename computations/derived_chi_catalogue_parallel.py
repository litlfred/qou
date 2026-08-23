#!/usr/bin/env python3
"""derived_chi_catalogue_parallel.py — parallel wrapper around
pyhecke_native.chi_q_via_gp for the catalogue sweep.

## Backends

Two backends are available; `parallel_chi_q_via_gp_batch` auto-detects
which to use at first call (and caches the choice):

  - **ThreadPoolExecutor** (preferred when available)
    Requires pyhecke_native >= 0.9.0 with the `py.allow_threads` GIL
    release on `chi_q_via_gp` (see
    `docs/audits/2026-06-07-pyhecke-native-gil-release-patch.md`).
    Lightweight: no IPC, shared memory.

  - **ProcessPoolExecutor** (fallback)
    Sidesteps the GIL by spawning subprocesses. Works with any
    pyhecke_native version but ~10-20% slower due to IPC + fork
    overhead. Used automatically when the GIL-release detection
    fails (older pyhecke_native installed).

## Auto-detection

On first call, we measure a tiny probe: sequential vs 2-thread time
on a 4-partition slice. If threads give > 1.3× speedup, the GIL is
released and threads are the better choice. The result is cached for
the lifetime of the process.

## Usage

    from derived_chi_catalogue_parallel import parallel_chi_q_via_gp_batch
    results = parallel_chi_q_via_gp_batch(
        partitions=parts,
        n_strands=n,
        word=word,
        workers=os.cpu_count(),
    )
    # results: dict[tuple[int,...], list[tuple[int, str]]]
"""
from __future__ import annotations

import os
import sys
import time
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
from pathlib import Path
from typing import Iterable

# ── pyhecke_native import (shared across backends) ────────────────

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

# ── GIL-release auto-detection (cached after first call) ──────────

_BACKEND_DETECTED: str | None = None
"""'threads' if the installed pyhecke_native releases the GIL on
chi_q_via_gp; 'processes' otherwise. None until first call."""


def detect_backend(
    probe_partitions: list[tuple[int, ...]] | None = None,
    probe_n: int = 6,
    probe_word: list[tuple[int, int]] | None = None,
) -> str:
    """Empirically detect whether threads scale on this pyhecke_native
    install. Caches the result globally."""
    global _BACKEND_DETECTED
    if _BACKEND_DETECTED is not None:
        return _BACKEND_DETECTED

    # Build a small probe: deuteron-like braid, all 11 partitions of 6.
    if probe_partitions is None:
        probe_partitions = [tuple(p) for p in ph.partitions_of(probe_n)]
    if probe_word is None:
        # Trivial 4-crossing word in B_6 — enough compute to measure but
        # fast enough that detection adds < 0.1 s.
        probe_word = [(1, 1), (1, 3), (1, 5), (-1, 2)]

    def _one(lam: tuple[int, ...]) -> object:
        return ph.chi_q_via_gp(list(lam), probe_n, list(probe_word))

    # Repeat probe to reduce noise.
    repeats = 4
    t0 = time.monotonic()
    for _ in range(repeats):
        for p in probe_partitions:
            _one(p)
    seq_time = (time.monotonic() - t0) / repeats

    t0 = time.monotonic()
    for _ in range(repeats):
        with ThreadPoolExecutor(max_workers=2) as ex:
            list(ex.map(_one, probe_partitions))
    thr_time = (time.monotonic() - t0) / repeats

    speedup = seq_time / thr_time if thr_time > 0 else 1.0
    # Threshold 1.3x — comfortably above noise, below the ~2x theoretical.
    _BACKEND_DETECTED = "threads" if speedup > 1.3 else "processes"
    return _BACKEND_DETECTED


# ── Worker for ProcessPoolExecutor (must be picklable) ────────────


def _chi_q_via_gp_worker(args: tuple) -> tuple[tuple[int, ...], list[tuple[int, str]]]:
    """Compute one character. Re-imports pyhecke_native inside the
    worker process."""
    partition, n_strands, word = args
    here = Path(__file__).resolve().parent
    pyhecke_path = str(here.parent.parent / "tools" / "pyhecke-native" / "python")
    if pyhecke_path not in sys.path:
        sys.path.insert(0, pyhecke_path)
    import pyhecke_native as ph_local
    laurent = ph_local.chi_q_via_gp(list(partition), n_strands, list(word))
    pairs: list[tuple[int, str]] = sorted(
        (int(d), str(c)) for (d, c) in laurent
    )
    return (tuple(partition), pairs)


# ── Worker for ThreadPoolExecutor (shares process state) ──────────


def _chi_q_via_gp_thread(args: tuple) -> tuple[tuple[int, ...], list[tuple[int, str]]]:
    partition, n_strands, word = args
    laurent = ph.chi_q_via_gp(list(partition), n_strands, list(word))
    pairs: list[tuple[int, str]] = sorted(
        (int(d), str(c)) for (d, c) in laurent
    )
    return (tuple(partition), pairs)


# ── Public API ────────────────────────────────────────────────────


def parallel_chi_q_via_gp_batch(
    partitions: Iterable[tuple[int, ...]],
    n_strands: int,
    word: list[tuple[int, int]],
    *,
    workers: int | None = None,
    chunksize: int = 4,
    force_backend: str | None = None,
) -> dict[tuple[int, ...], list[tuple[int, str]]]:
    """Parallel batch over partitions for a single (n_strands, word).

    Args:
      workers: thread / process pool size. Defaults to `os.cpu_count()`.
      chunksize: ProcessPool chunksize (ignored for ThreadPool).
      force_backend: 'threads' / 'processes' to skip auto-detection.

    Returns dict keyed by partition tuple.

    ## Backend selection

    In order of preference at runtime:

    1. **Thread pool** — primary path when the GIL release on
       `chi_q_via_gp` is present (pyhecke_native v0.9.0+ with Patch 1):
       per-partition calls in Python threads, ~Nx on N-core boxes
       with no IPC overhead.
    2. **Process pool** — fallback for older pyhecke_native installs
       (Patch 1 missing). Sidesteps the GIL via process isolation;
       ~Nx with subprocess + IPC overhead.

    Auto-detection between threads and processes is driven by
    `detect_backend()`, which empirically times threaded vs sequential
    on a small probe and caches the choice for the process lifetime.

    **The Rust batched `chi_lambdas_via_gp` (Patch 2)** is exposed by
    pyhecke_native but **NOT** routed by this function. Measured
    perf on PR #1952: threads + Tier 3 bar-symmetry outperform
    batched-Rayon at medium `n` (5Li 11.1s threaded vs 49.7s batched),
    so the threaded path stays primary. The batched API remains
    available for callers in non-threaded environments (single-core,
    or a future GIL-blocked pyhecke version) and for pure-Rust
    consumers that want a single Rust call.
    """
    if workers is None:
        workers = os.cpu_count() or 1
    part_list = list(partitions)
    if not part_list:
        return {}
    args_list = [(p, n_strands, word) for p in part_list]
    # Note: pyhecke_native.chi_lambdas_via_gp (Patch 2) is available but
    # empirically slower than threaded chi_q_via_gp for medium-n atoms
    # — Rayon overhead + per-(λ,μ) character evaluation dominate the
    # shared-GP saving. We keep the threaded path as the primary
    # backend. The batched API is exposed for non-threaded environments
    # (single-core, GIL-blocked older pyhecke_native) and for any future
    # consumer that wants a pure-Rust batch call.
    if workers == 1 or len(args_list) <= 1:
        return dict(_chi_q_via_gp_thread(a) for a in args_list)

    backend = force_backend or detect_backend()

    if backend == "threads":
        with ThreadPoolExecutor(max_workers=workers) as ex:
            results = list(ex.map(_chi_q_via_gp_thread, args_list))
    else:
        # Processes — re-import inside each worker.
        with ProcessPoolExecutor(max_workers=workers) as ex:
            results = list(ex.map(_chi_q_via_gp_worker, args_list, chunksize=chunksize))
    return dict(results)
