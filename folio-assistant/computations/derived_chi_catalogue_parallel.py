#!/usr/bin/env python3
"""derived_chi_catalogue_parallel.py — multiprocessing wrapper around
pyhecke_native.chi_q_via_gp for the catalogue sweep.

Per the GIL diagnosis in
`docs/audits/2026-06-07-pyhecke-native-gil-release-patch.md`,
`pyhecke_native.chi_q_via_gp` currently holds the GIL during the
internal Geck-Pfeiffer compute. ThreadPoolExecutor gives 0× speedup
as a result. ProcessPoolExecutor sidesteps the GIL by spawning
separate Python interpreters, giving near-linear speedup (~3× on a
4-core box measured 2026-06-07).

## Usage

    from derived_chi_catalogue_parallel import parallel_chi_q_via_gp_batch
    results = parallel_chi_q_via_gp_batch(
        partitions=parts,
        n_strands=n,
        word=word,
        workers=os.cpu_count(),
    )
    # results: dict[tuple[int,...], list[tuple[int, str]]]

## Notes

- Worker re-imports pyhecke_native inside the spawned process (PyO3
  extensions are NOT picklable through the fork-default route on
  some platforms; an import-on-entry is safe and cheap).
- The `chunksize` parameter is tuned for ~10ms per chunk so the IPC
  overhead amortises well.
- When the Rust-side GIL-release + batched-GP patches land
  (see audit doc), this wrapper becomes redundant — but the sweep
  caller doesn't have to change. Just import a different backend.
"""
from __future__ import annotations

import os
import sys
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path
from typing import Iterable


# ── Top-level worker (must be picklable for ProcessPoolExecutor) ──


def _chi_q_via_gp_worker(args: tuple) -> tuple[tuple[int, ...], list[tuple[int, str]]]:
    """Compute one character. Re-import inside the worker so the
    pyhecke_native extension is loaded fresh in each spawned process."""
    partition, n_strands, word = args
    # Ensure the worker can find pyhecke_native — system install + our local path.
    here = Path(__file__).resolve().parent
    pyhecke_path = str(here.parent.parent / "tools" / "pyhecke-native" / "python")
    if pyhecke_path not in sys.path:
        sys.path.insert(0, pyhecke_path)
    import pyhecke_native as ph  # noqa: E402
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
) -> dict[tuple[int, ...], list[tuple[int, str]]]:
    """Parallel batch over partitions for a single (n_strands, word).

    Returns a dict keyed by partition tuple. Workers default to
    `os.cpu_count()`. The Rust call must be CPU-bound (which it is)
    for ProcessPoolExecutor to win — we use it instead of
    ThreadPoolExecutor because the current pyhecke_native binding
    holds the GIL during the Geck-Pfeiffer compute.
    """
    if workers is None:
        workers = os.cpu_count() or 1
    args_list = [(p, n_strands, word) for p in partitions]
    if workers == 1 or len(args_list) <= 1:
        # No point spawning processes; sequential fallback.
        return dict(_chi_q_via_gp_worker(a) for a in args_list)
    with ProcessPoolExecutor(max_workers=workers) as ex:
        results = list(ex.map(_chi_q_via_gp_worker, args_list, chunksize=chunksize))
    return dict(results)
