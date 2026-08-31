#!/usr/bin/env python3
"""Hoefsmit block structure built DIRECTLY, without a dense d x d matrix.

WHY. `shell_closure_compute.py` dies at Hecke level k = 12 -- OOM-killed at
12.6 GB in a 16 GB container, silently, after k = 11 (measured: k=9 8.7s,
k=10 30.9s, k=11 129.4s, k=12 killed). `observations/k12-barrier-bypass.md`
attributes that to the partition count growing combinatorially, and that is not
the cause: k = 12 has only 77 partitions. The cause is that
`level_k_binding._seminormal_matrix_cached` allocates `np.zeros((d, d))` per
partition and `shell_closure_compute` holds every partition's structure at once,
so the transient requirement is

    sum_lambda d_lambda^2  =  n!   =  479,001,600 at n = 12
                               ->  3.83 GB per generator, 7.66 GB for both

plus numpy temporaries -- which matches the 12.6 GB observed.

THE POINT. That dense array is never needed. Read the construction: it walks
standard Young tableaux and writes only `M[i,i] = q0` (same row), `M[i,i] = -qi`
(same column), or a 2x2 block on `(i, j)` where `j` indexes the a<->b swapped
tableau. Gen 0 is pure diagonal and gen 1 is 2x2 blocks plus diagonal -- exactly
the structure `_extract_blocks` then REDISCOVERS by scanning the dense matrix it
just built, with an O(dim^2) Python double loop (59M iterations per partition at
k = 12). The sparse structure is known at construction time and is thrown away.

Emitting it directly makes the requirement

    sum_lambda d_lambda  =  140,152 at n = 12   ->  ~5.6 MB at 50 dps

a factor of n!/sum(d) ~ 3,400 smaller at k = 12, and removes the O(dim^2) scan.

CONTRACT. `extract_blocks_direct(shape, gen)` returns the same 4-tuple
`(diag, blocks, singleton_mask, dim)` as `shell_closure_compute._extract_blocks`,
so it is a drop-in replacement. Verified equal on every partition of every level
the current code can reach -- see `--verify`.

SCOPE. This removes an implementation barrier. It does NOT by itself say the
homological bypass in `k12-barrier-bypass.md` is unnecessary -- that claim would
need the re-scoped k >= 12 results in hand, and may rest on other grounds this
does not touch.
"""
from __future__ import annotations

import sys
from pathlib import Path

import numpy as np

_HERE = Path(__file__).resolve().parent
for _p in (_HERE, _HERE / "_deprecated", _HERE / "substrate"):
    if str(_p) not in sys.path:
        sys.path.insert(0, str(_p))

from level_k_binding import (                      # noqa: E402
    standard_young_tableaux, content_of, q_number, q0, qi, HA,
)


def extract_blocks_direct(shape: tuple, gen: int):
    """Block structure of the Hoefsmit sigma_gen, with no dense allocation.

    Mirrors `level_k_binding._seminormal_matrix_cached` decision-for-decision,
    then emits what `_extract_blocks` would have found, without ever forming
    the d x d matrix or scanning it.

    Returns (diag, blocks, singleton_mask, dim) -- the `_extract_blocks`
    contract. `blocks` entries are (i, j, a, b, c, d) for the 2x2 at (i, j).
    """
    tabs = standard_young_tableaux(shape)
    dim = len(tabs)
    if dim == 0:
        return np.array([]), [], np.ones(0, dtype=bool), 0

    tab_index = {T: i for i, T in enumerate(tabs)}
    diag = np.zeros(dim)
    singleton_mask = np.ones(dim, dtype=bool)
    blocks = []
    processed = set()

    a_, b_ = gen + 1, gen + 2
    for i, T in enumerate(tabs):
        if i in processed:
            continue
        rho = content_of(T, b_) - content_of(T, a_)
        if rho == 0:
            # left at 0 by _seminormal_matrix_cached; a singleton with value 0
            continue

        same_row = any(a_ in row and b_ in row for row in T)
        same_col = False
        max_cols = max(len(row) for row in T) if T else 0
        for c_idx in range(max_cols):
            col_vals = [T[r][c_idx] for r in range(len(T)) if c_idx < len(T[r])]
            if a_ in col_vals and b_ in col_vals:
                same_col = True

        if same_row:
            diag[i] = q0
            processed.add(i)
        elif same_col:
            diag[i] = -qi
            processed.add(i)
        else:
            T_swap = tuple(
                tuple(b_ if v == a_ else (a_ if v == b_ else v) for v in row)
                for row in T
            )
            j = tab_index.get(T_swap)
            if j is None or j == i:
                diag[i] = q0 if rho > 0 else -qi
                processed.add(i)
            else:
                qr = q_number(rho)
                diag_val = HA / qr
                off_sq = 1.0 - diag_val ** 2
                off = float(np.sqrt(abs(off_sq))) if off_sq > 0 else 0.0
                # the 2x2 block on (i, j); _extract_blocks reports the pair
                # with the LOWER index first, which is i here since we walk
                # in order and skip processed entries.
                blocks.append((i, j, diag_val, off, off, HA - diag_val))
                singleton_mask[i] = False
                singleton_mask[j] = False
                processed.add(i)
                processed.add(j)
    return diag, blocks, singleton_mask, dim


def _verify(kmax: int = 9) -> int:
    """Assert equality with the dense path on every partition up to kmax."""
    import json
    from shell_closure_compute import _extract_blocks
    wit = json.load(open(_HERE / "hoefsmit_witness.json"))
    checked = mism = 0
    for k in range(3, kmax + 1):
        for entry in wit["levels"].get(str(k), []):
            shape = tuple(entry["shape"])
            for gen in (0, 1):
                d0, b0, s0, n0 = _extract_blocks(shape, gen)
                d1, b1, s1, n1 = extract_blocks_direct(shape, gen)
                ok = (n0 == n1
                      and np.allclose(np.asarray(d0), np.asarray(d1), atol=1e-12)
                      and bool(np.array_equal(np.asarray(s0), np.asarray(s1)))
                      and sorted((x[0], x[1]) for x in b0)
                          == sorted((x[0], x[1]) for x in b1)
                      and np.allclose(
                          sorted(tuple(round(float(v), 12) for v in x[2:]) for x in b0),
                          sorted(tuple(round(float(v), 12) for v in x[2:]) for x in b1),
                          atol=1e-10))
                checked += 1
                if not ok:
                    mism += 1
                    print(f"  MISMATCH k={k} shape={shape} gen={gen} dim={n0}")
        print(f"  k={k:>2d}: cumulative {checked} (shape, gen) pairs, {mism} mismatch")
    print(f"\nchecked {checked} (shape, gen) pairs, {mism} mismatches")
    return 1 if mism else 0


if __name__ == "__main__":
    raise SystemExit(_verify(int(sys.argv[1]) if len(sys.argv) > 1 else 9))
