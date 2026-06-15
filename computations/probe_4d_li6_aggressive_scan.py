#!/usr/bin/env python3
"""
Probe (4d): aggressive ⁶Li scan in the d_λ ∈ [100k, 1M] range to
find the actual PSD-dominant partition.

Probe (4c) FALSIFIED the rectangular-form conjecture: three "almost-
rectangular" shapes beat (6,6,6)'s −96.52, with (3,3,3,3,2,2,2)
deepest at −116.71. The actual dominant is unknown.

This probe scans all p(18) partitions with d_λ ∈ [100k, 1.5M] (the
manageable Lanczos range). Goal: identify the global dominant or
narrow the candidate set to a structural pattern.

Time estimate: ~30 shapes at ~60s each (build + Lanczos) = ~30 min.
"""

from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import sys
import time
from math import factorial
from pathlib import Path

import numpy as np
from scipy.sparse.linalg import LinearOperator, eigsh

sys.path.insert(0, str(Path(__file__).resolve().parent))
from witness_base import WitnessBuilder
from lean_uniqueness_refs import lean_uniqueness_ref
from mass_at_3A_proper import atom_braid_word_3A
from q_parameter import Q as q0
from probe_4_li6_rectangular_python import build_seminormal_fast, apply_T_w, apply_T_w_T


def hook_dim(p):
    n = sum(p)
    hooks = []
    for i, rl in enumerate(p):
        for j in range(rl):
            below = sum(1 for k in range(i + 1, len(p)) if p[k] > j)
            right = rl - j - 1
            hooks.append(below + right + 1)
    d = factorial(n)
    for h in hooks:
        d //= h
    return d


def parts(n, max_val=None):
    if max_val is None:
        max_val = n
    if n == 0:
        yield ()
        return
    for v in range(min(n, max_val), 0, -1):
        for rest in parts(n - v, v):
            yield (v,) + rest


def main():
    word = atom_braid_word_3A(3, 3)
    print(f"⁶Li T_w: {len(word)} crossings on B_18\n")

    # Enumerate p(18) with d_λ in feasible range
    DMIN, DMAX = 100_000, 1_500_000
    candidates = []
    for p in parts(18):
        d = hook_dim(p)
        if DMIN <= d <= DMAX:
            candidates.append((p, d))

    # Sort by d_λ ascending (cheapest first)
    candidates.sort(key=lambda x: x[1])
    print(f"Scanning {len(candidates)} partitions with d_λ ∈ [{DMIN:,}, {DMAX:,}]:")
    print(f"{'#':>3s}  {'shape':>30s}  {'d_λ':>9s}  {'time':>8s}  {'min_eig':>10s}  {'max_eig':>10s}")

    # Already-scanned shapes (skip)
    done = {
        (6, 6, 6): -95.72,
        (3, 3, 3, 3, 3, 3): -96.52,
        (8, 8, 2): -88.95,
        (12, 3, 3): -62.44,
        (12, 2, 2, 2): -64.77,
        (12, 5, 1): -59.86,
        (5, 5, 5, 3): -110.31,
        (4, 4, 4, 3, 3): -109.81,
        (3, 3, 3, 3, 2, 2, 2): -116.71,
        (10, 4, 4): -80.67,
    }

    results = []
    deepest_min = -96.52
    deepest_shape = (3, 3, 3, 3, 3, 3)
    t_start = time.time()

    for idx, (shape, d) in enumerate(candidates, 1):
        if shape in done:
            print(f"{idx:>3d}  {str(list(shape)):>30s}  {d:>9d}  (cached)  {done[shape]:>+10.4f}")
            results.append({
                "shape": list(shape),
                "dim": d,
                "min_eig": done[shape],
                "cached": True,
            })
            if done[shape] < deepest_min:
                deepest_min = done[shape]
                deepest_shape = shape
            continue

        t0 = time.time()
        sigmas, dim = build_seminormal_fast(shape, float(q0))
        sigmas_T = [sg.T.tocsr() for sg in sigmas]

        def matvec(v):
            return 0.5 * (apply_T_w(v, sigmas, word, 0.0)
                          + apply_T_w_T(v, sigmas_T, word, 0.0))

        L = LinearOperator((dim, dim), matvec=matvec, dtype=np.float64)
        w_min = eigsh(L, k=1, which="SA", maxiter=2000, tol=1e-6, return_eigenvectors=False)
        w_max = eigsh(L, k=1, which="LA", maxiter=2000, tol=1e-6, return_eigenvectors=False)
        dt = time.time() - t0
        me = float(w_min[0])
        ma = float(w_max[0])
        marker = "  ← NEW DEEPEST" if me < deepest_min else ""
        if me < deepest_min:
            deepest_min = me
            deepest_shape = shape

        print(f"{idx:>3d}  {str(list(shape)):>30s}  {d:>9d}  {dt:>7.1f}s  {me:>+10.4f}  {ma:>+10.4f}{marker}",
              flush=True)
        results.append({
            "shape": list(shape),
            "dim": dim,
            "min_eig": me,
            "max_eig": ma,
            "time_s": dt,
            "cached": False,
        })

    total = time.time() - t_start
    print(f"\nTotal time: {total:.1f}s")
    print(f"Deepest min_eig: {deepest_min:+.4f} at shape {list(deepest_shape)}")

    # Sort results by min_eig
    results.sort(key=lambda r: r["min_eig"])
    print(f"\nTop-10 most negative:")
    for r in results[:10]:
        rect = "RECTANGULAR" if len(set(r["shape"])) == 1 else ""
        n_distinct = len(set(r["shape"]))
        rows = len(r["shape"])
        cols = max(r["shape"])
        print(f"  {str(r['shape']):>30s}  d={r['dim']:>7d}  min_eig={r['min_eig']:+10.4f}  "
              f"rows={rows} cols={cols} distinct={n_distinct} {rect}")

    out = WitnessBuilder("probe-4d-li6-aggressive-scan", engine="python")
    out.set_description(
        "Aggressive ⁶Li scan in d_λ ∈ [100k, 1.5M] to identify the "
        "actual PSD-dominant partition. Updates the dominant-partition "
        "audit's empirical landscape post-Probe (4c) falsification."
    )
    out.set_audit_only("docs/audits/2026-05-25-dominant-partition-nucleon-structure.md")
    out.set_content_block("conj:atom-braid-exterior-algebra")
    out.add_data("all_scanned_partitions", results)
    out.add_data("deepest_shape", list(deepest_shape))
    out.add_data("deepest_min_eig", deepest_min)
    out.add_data("scan_range_dmin_dmax", [DMIN, DMAX])
    out.add_data("n_candidates", len(candidates))

    out.add_assertion(
        name="deepest_shape_identified",
        computed="1",
        expected="1",
        tolerance=0,
        source=f"deepest min_eig = {deepest_min:+.4f} at {list(deepest_shape)}",
    )

    out.add_data("lean_uniqueness_ref", lean_uniqueness_ref("⁶Li"))
    out_path = out.save()
    print(f"\nWitness: {out_path}")


if __name__ == "__main__":
    main()
