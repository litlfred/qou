#!/usr/bin/env python3
"""y_lambda_pole_order_cache.py — precompute ord_{u=0}(y_λ(u²)) for
every height-≤6 partition λ ⊢ n.

The default n-set tracks the upstream Wenzl-bridge witness
[`y-lambda-wenzl-bridge-symbolic-witness.json`](./y-lambda-wenzl-bridge-symbolic-witness.json),
which currently provides symbolic y_λ tables for n ∈ {2, 3, …, 12}.
At n = 12 there are 58 height-≤6 partitions (out of 77 total).

To extend coverage to n ∈ {15, 18} (⁵Li, ⁶Li): first extend the
upstream Wenzl-bridge witness.  The script will pick up any newly-
present n automatically when its `--n` argument names them; trying
to cache an n the upstream witness lacks is a no-op (script logs a
"no Wenzl-bridge data, skipping" line).

Runs once per n, writes `y-lambda-pole-order-cache.json`.
Downstream consumers (`per_irrep_pole_atom_crystal.py`) read the
cache instead of re-sympifying the long Wenzl-bridge expressions
(which are exponentially-nested in n and require a bumped Python
recursion limit at n ≥ 12).

Multi-processed via `multiprocessing.Pool` across partitions
(per-partition sympify is independent).

Usage:
    python3 y_lambda_pole_order_cache.py [--n N1,N2,...] [--workers W]
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import sympy as sp

# n=12 y_λ expressions are nested products of 12 (1 - q^k/D)-style
# terms; sympify hits Python's default 1000-frame recursion cap.
# Bump globally and re-bump inside multiprocessing workers.
sys.setrecursionlimit(50000)

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from hecke_characters import partitions_of  # noqa: E402

WENZL = HERE / "y-lambda-wenzl-bridge-symbolic-witness.json"
CACHE = HERE / "y-lambda-pole-order-cache.json"

Q = sp.Symbol("q")
U = sp.Symbol("u", positive=True)


def ord_u_eq_0(expr_q: sp.Expr) -> int | None:
    """Lowest power of `u` in `expr_q.subs(q, u**2)`."""
    expr_u = sp.simplify(expr_q.subs(Q, U ** 2))
    if expr_u == 0:
        return None
    n_, d_ = sp.fraction(expr_u)
    n_poly = sp.Poly(n_, U)
    d_poly = sp.Poly(d_, U)
    n_low = min(m[0] for m in n_poly.monoms()) if n_poly.monoms() else 0
    d_low = min(m[0] for m in d_poly.monoms()) if d_poly.monoms() else 0
    return n_low - d_low


def _worker(args: tuple[list[int], str]) -> tuple[list[int], int | None, float]:
    """Multiprocessing worker: compute ord_y for one shape.  Returns
    `(shape, ord_y, elapsed)`.  Re-imports inside the worker because
    sympy state isn't always picklable across spawn."""
    import time as _time
    import sys as _sys
    _sys.setrecursionlimit(50000)  # n=12 expressions exceed 1000 frames
    shape_list, y_str = args
    t0 = _time.time()
    y_q = sp.sympify(y_str)
    ord_y = ord_u_eq_0(y_q)
    return shape_list, ord_y, _time.time() - t0


def main(argv: list[str]) -> int:
    only_ns = None
    if "--n" in argv:
        only_ns = [int(x) for x in argv[argv.index("--n") + 1].split(",")]
    workers = 1
    if "--workers" in argv:
        workers = int(argv[argv.index("--workers") + 1])

    print(f"Loading Wenzl-bridge witness: {WENZL.name}", flush=True)
    w = json.loads(WENZL.read_text())
    tabs = w["tables_by_n"]

    if CACHE.exists():
        existing = json.loads(CACHE.read_text())
    else:
        existing = {"by_n": {}}

    # Default target ns are tied to what the upstream Wenzl-bridge
    # witness actually provides.  Out-of-range entries are no-ops
    # (logged but skipped); to extend, first extend the upstream
    # witness (see module docstring).
    target_ns = only_ns if only_ns else [3, 6, 9, 12]

    for n in target_ns:
        n_key = str(n)
        if n_key not in tabs:
            print(f"  n={n}: no Wenzl-bridge data, skipping", flush=True)
            continue
        # Skip if already cached at this n.
        if n_key in existing["by_n"]:
            cached_count = len(existing["by_n"][n_key]["partitions"])
            ht6_count = sum(1 for p in partitions_of(n) if len(p) <= 6)
            if cached_count >= ht6_count:
                print(f"  n={n}: already cached "
                      f"({cached_count} partitions)", flush=True)
                continue

        rows = tabs[n_key]["weights"]
        out_partitions: list[dict] = []
        t_start = time.time()
        print(f"  n={n}: processing {len(rows)} y_λ entries with "
              f"{workers} worker(s)...", flush=True)
        # Filter to height-≤6 only (the only ones we need).
        worker_args = [
            (r["partition"], r["y_lambda_symbolic"])
            for r in rows if len(r["partition"]) <= 6
        ]
        if workers > 1:
            from multiprocessing import Pool
            with Pool(workers) as pool:
                for shape_list, ord_y, dt in pool.imap_unordered(
                        _worker, worker_args):
                    print(f"    λ={tuple(shape_list)}  ord_y={ord_y}  "
                          f"({dt:.1f}s)", flush=True)
                    out_partitions.append({
                        "partition": shape_list,
                        "ord_y_at_u_eq_0": ord_y,
                    })
        else:
            for shape_list, y_str in worker_args:
                shape, ord_y, dt = _worker((shape_list, y_str))
                print(f"    λ={tuple(shape)}  ord_y={ord_y}  "
                      f"({dt:.1f}s)", flush=True)
                out_partitions.append({
                    "partition": shape,
                    "ord_y_at_u_eq_0": ord_y,
                })
        existing["by_n"][n_key] = {
            "n": n,
            "n_partitions_height_le_6": len(out_partitions),
            "partitions": out_partitions,
            "compute_time_sec": time.time() - t_start,
        }
        # Save after each n so a kill mid-run preserves work.
        CACHE.write_text(json.dumps(existing, indent=2))
        print(f"  n={n} cache saved "
              f"({time.time() - t_start:.1f}s)", flush=True)

    print(f"\n✓ Cache: {CACHE}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
