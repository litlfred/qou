#!/usr/bin/env python3


# polynomial_q_not_applicable: symbolic q output via the markov_peel
# pipeline; this script just parallelises the existing
# habiro_coefficients_extended cases across processes.
"""Parallel runner for the Habiro coefficient extended pipeline.

`habiro_coefficients_extended.py` runs A=2..6 (default) or
A=2..8 (with `HABIRO_EXT_INCLUDE_LI=1
HABIRO_EXT_INCLUDE_HIGHER=1`) atoms **sequentially**. With one
slow atom (⁷Li, ⁷Be, ⁸Be each ~10-30 min on a single core), total
wall time is the sum.

This wrapper farms out the cases to a `multiprocessing.Pool`, so
total wall time becomes `max(per-atom time)`. On an 8-core host
with the full A=2..8 set, expected speedup: ~6× (limited by the
slowest atom).

After all cases complete, merges the per-atom results into the
canonical `habiro-coefficients-extended.witness.json` schema,
preserving keys/order so downstream consumers (the bounded T6
wiring in `mass_formula_6term_mpfr_50dps.term_6_via_habiro_coeffs_mp`
and the 4-way 1ppb cross-check) see no behavioural change.

Usage:

    python3 habiro_coefficients_extended_parallel.py --workers 4
    HABIRO_EXT_INCLUDE_LI=1 HABIRO_EXT_INCLUDE_HIGHER=1 \\
        python3 habiro_coefficients_extended_parallel.py --workers 8
"""
from __future__ import annotations

# Path bridge (subdirectory refactor — Phase 4, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the cluster subdirectory. The bridge module
# also puts every other cluster subdir on sys.path so cross-
# cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import argparse
import json
import os
import sys
import time
from datetime import datetime, timezone
from multiprocessing import Pool, cpu_count
from pathlib import Path

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

# `_analyse_atom` is the per-atom worker from the sequential script
# (no module-level side effects beyond the chi-cache loader); safe
# to call from a worker pool.
from habiro_coefficients_extended import _analyse_atom  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402


def _worker(case: tuple[str, int, int, int]) -> tuple[str, dict]:
    label, Z, N, max_m = case
    t0 = time.time()
    try:
        result = _analyse_atom(label, Z, N, max_m)
    except Exception as exc:  # noqa: BLE001
        result = {"error": f"{type(exc).__name__}: {exc}"}
    elapsed = time.time() - t0
    result.setdefault("timings_sec", {})
    if isinstance(result["timings_sec"], dict):
        result["timings_sec"]["total"] = round(elapsed, 2)
    return label, result


# Same case list as the sequential script — kept verbatim so the two
# scripts emit equivalent witnesses.
DEFAULT_CASES: list[tuple[str, int, int, int]] = [
    ("D (deuteron, A=2)",    1, 1, 18),
    ("T (triton, A=3)",      1, 2, 18),
    ("³He (helion, A=3)",    2, 1, 18),
    ("⁴He (alpha, A=4)",     2, 2, 22),
]

LI_CASES: list[tuple[str, int, int, int]] = [
    ("⁵Li (A=5)", 3, 2, 25),
    ("⁶Li (A=6)", 3, 3, 28),
]

HIGHER_CASES: list[tuple[str, int, int, int]] = [
    ("⁷Li (A=7)", 3, 4, 32),
    ("⁷Be (A=7)", 4, 3, 32),
    ("⁸Be (A=8)", 4, 4, 35),
]


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n", 1)[0])
    ap.add_argument(
        "--workers", type=int, default=max(1, cpu_count() // 2),
        help="Process-pool size (default: cpu_count() // 2).",
    )
    ap.add_argument(
        "--atoms", default=None,
        help="Comma-separated atom labels to run (default: respect "
             "HABIRO_EXT_INCLUDE_LI / HABIRO_EXT_INCLUDE_HIGHER env vars).",
    )
    args = ap.parse_args()

    cases: list[tuple[str, int, int, int]] = list(DEFAULT_CASES)
    if os.environ.get("HABIRO_EXT_INCLUDE_LI") == "1":
        cases.extend(LI_CASES)
    if os.environ.get("HABIRO_EXT_INCLUDE_HIGHER") == "1":
        cases.extend(HIGHER_CASES)
    if args.atoms:
        wanted = {a.strip() for a in args.atoms.split(",") if a.strip()}
        cases = [c for c in cases if c[0] in wanted]

    print(f"Parallel Habiro extension: {len(cases)} atoms × {args.workers} workers")
    print(f"  cases: {[c[0] for c in cases]}")
    print("=" * 76)

    t0 = time.time()
    results: dict[str, dict] = {}
    if args.workers == 1 or len(cases) == 1:
        for case in cases:
            label, r = _worker(case)
            results[label] = r
            print(f"  {label}: done")
    else:
        with Pool(processes=args.workers) as pool:
            for label, r in pool.imap_unordered(_worker, cases):
                results[label] = r
                t = r.get("timings_sec", {}).get("total", "?")
                print(f"  {label}: done ({t} s)")
    elapsed = time.time() - t0
    print(f"\ntotal wall time: {elapsed:.1f} s")

    # Match the existing witness schema bit-for-bit.
    w = WitnessBuilder.wrap_legacy(
        "habiro-coefficients-extended",
        {
            "description": (
                "Cyclotomic Habiro coefficients a_m(u) of tr_M(T_w, q) for "
                "atomic braids A=2..8 via the markov_peel symbolic-q "
                "pipeline. Parallel runner farms cases out to a worker "
                "pool; output schema matches the sequential "
                "habiro_coefficients_extended.py 1-for-1 so downstream "
                "consumers (mass_formula_6term_mpfr_50dps.term_6_via_habiro_coeffs_mp, "
                "the 4-way 1ppb cross-check) see no behavioural change."
            ),
            "auditOnly": "docs/audits/2026-05-17-post-pr-682-followup-plan.md",
            "reference_blocks": [
                "def:habiro-ring",
                "prop:full-pole-structure-mass-trace",
                "thm:knot-mass-formula-unified",
            ],
            "results": results,
        },
        script_path=__file__,
        engine="sympy",
        start_time=t0,
    )
    out = w.save()
    print(f"\nWitness: {Path(out).name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
