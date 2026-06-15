#!/usr/bin/env python3
"""
Probe (4b): scan several non-rectangular ⁶Li partitions and test
whether any has min_eig < (3,3,3,3,3,3)'s −96.52.

This complements Probe (4): the rectangular pair (6,6,6) / (3,3,3,3,3,3)
both have min_eig ≈ −96. If ANY non-rectangular partition has
min_eig < −96.52, the rectangular-form conjecture is falsified at
A=6 (the dominant block is not rectangular). If all non-rectangular
candidates have less-negative min_eig, the conjecture is
*structurally* supported.

Strategy: pick a handful of representative shapes with d_λ in the
tractable range (≤ ~25000 for Lanczos in <60 sec each):

  - Near-rectangular: (5,5,5,3), (4,4,4,3,3), (3,3,3,3,2,2,2)
  - Staircase-like: (6,5,4,3), (5,4,3,3,3)
  - Long-row: (8,4,3,3), (10,4,4)
  - Hook-like: (7,5,1,1,1,1,1,1)

Audit-only.
"""

from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import sys
import time
from pathlib import Path

import numpy as np
from scipy.sparse.linalg import LinearOperator, eigsh

sys.path.insert(0, str(Path(__file__).resolve().parent))
from witness_base import WitnessBuilder
from lean_uniqueness_refs import lean_uniqueness_ref  # noqa: E402
from mass_at_3A_proper import atom_braid_word_3A
from q_parameter import Q as q0
from probe_4_li6_rectangular_python import build_seminormal_fast, apply_T_w, apply_T_w_T


def hook_dim(partition):
    from math import factorial
    n = sum(partition)
    hooks = []
    for i, row_len in enumerate(partition):
        for j in range(row_len):
            below = sum(1 for k in range(i + 1, len(partition)) if partition[k] > j)
            right = row_len - j - 1
            hooks.append(below + right + 1)
    d = factorial(n)
    for h in hooks:
        d //= h
    return d


def compute_min_eig(shape, word, q):
    t0 = time.time()
    sigmas, dim = build_seminormal_fast(shape, q)
    sigmas_T = [sg.T.tocsr() for sg in sigmas]
    t_build = time.time() - t0

    def matvec(v):
        return 0.5 * (apply_T_w(v, sigmas, word, 0.0)
                      + apply_T_w_T(v, sigmas_T, word, 0.0))

    L = LinearOperator((dim, dim), matvec=matvec, dtype=np.float64)
    t1 = time.time()
    w_min = eigsh(L, k=1, which="SA", maxiter=2000, tol=1e-6, return_eigenvectors=False)
    w_max = eigsh(L, k=1, which="LA", maxiter=2000, tol=1e-6, return_eigenvectors=False)
    t_eig = time.time() - t1

    return {
        "shape": list(shape),
        "dim": dim,
        "min_eig": float(w_min[0]),
        "max_eig": float(w_max[0]),
        "build_s": t_build,
        "eig_s": t_eig,
    }


def main():
    word = atom_braid_word_3A(3, 3)
    print(f"⁶Li T_w: {len(word)} crossings on B_18")
    print(f"\nBenchmark (from Probe (4)):")
    print(f"  (6,6,6):       d_λ = 87,516   min_eig = -95.72")
    print(f"  (3,3,3,3,3,3): d_λ = 87,516   min_eig = -96.52  ← current dominant candidate")

    # Curated candidates spanning rectangle / near-rect / unbalanced
    candidates = [
        # OTHER RECTANGLES (test: is "rectangular" broader than (A,A,A)?)
        (9, 9),                       # 2-row rectangle, d=4862
        (2, 2, 2, 2, 2, 2, 2, 2, 2),  # 9-row rectangle (transpose of (9,9)), d=4862
        # NEAR-RECTANGULAR 2-row (test: does balance suffice?)
        (10, 8),                      # d=11934
        (11, 7),                      # d=13260
        (12, 6),                      # d=9996
        # 3-row almost-rectangle (test: original conjecture clause (b))
        (13, 4, 1),                   # d=22848
        (13, 3, 2),                   # d=29172
        (13, 2, 2, 1),                # d=29835
        # Unbalanced controls (should have less-negative min_eig)
        (16, 2),                      # d=135 (very unbalanced)
        (15, 3),                      # d=663
        (14, 4),                      # d=2244
        (16, 1, 1),                   # d=136 (hook shape)
        # 2-row rect-like with moderate balance
        (8, 8, 2),                    # d=136136 (slightly over cap)
        (12, 3, 3),                   # d=56100 (3-row near-rect)
        (12, 2, 2, 2),                # d=58344 (4-row near-rect)
        (12, 5, 1),                   # d=53040
    ]

    # Filter by d_λ — skip anything d > 150,000 (Lanczos < 2 min each)
    feasible = []
    for shape in candidates:
        d = hook_dim(shape)
        if d <= 150000:
            feasible.append((shape, d))
        else:
            print(f"  SKIP {shape} (d_λ = {d} > 150k cap)")

    print(f"\nScanning {len(feasible)} non-rectangular ⁶Li shapes …")
    print(f"{'shape':>30s}  {'d_λ':>6s}  {'min_eig':>10s}  {'max_eig':>10s}  {'beats -96.52?'}")

    results = []
    for shape, d in feasible:
        r = compute_min_eig(shape, word, float(q0))
        beats = r["min_eig"] < -96.52
        marker = "  ← FALSIFIES" if beats else ""
        print(f"{str(list(shape)):>30s}  {d:>6d}  {r['min_eig']:>+10.4f}  {r['max_eig']:>+10.4f}  {beats}{marker}")
        results.append({**r, "beats_rectangular": beats})

    any_falsifies = any(r["beats_rectangular"] for r in results)
    print()
    print(f"Verdict: {'FALSIFIED — non-rectangular beats rectangular' if any_falsifies else 'CONSISTENT — no scanned non-rectangular beats rectangular'}")

    out = WitnessBuilder("probe-4b-li6-non-rectangular-scan", engine="python")
    out.set_description(
        "Scans a curated set of non-rectangular ⁶Li partitions and "
        "tests whether any has min_eig more negative than the "
        "rectangular pair's −96.52. Strengthens or falsifies the "
        "rectangular-form conjecture at A=6 with a finite cheap scan."
    )
    out.set_audit_only(
        "docs/audits/2026-05-25-dominant-partition-nucleon-structure.md"
    )
    out.set_content_block("conj:atom-braid-exterior-algebra")
    out.add_data("scanned_partitions", results)
    out.add_data("benchmark_rectangular_min_eig", -96.52)
    out.add_assertion(
        name="no_non_rectangular_beats_rectangular_at_a6",
        computed=str(int(not any_falsifies)),
        expected="1",
        tolerance=0,
        source=f"Scanned {len(results)} non-rectangular shapes; {sum(r['beats_rectangular'] for r in results)} beat -96.52.",
    )
    out.add_caveat(
        f"Scan covers {len(feasible)} of p(18)=385 partitions. Skipped "
        f"shapes with d_λ > 30,000 (too slow for Lanczos at >60s each). "
        "Cannot strictly confirm rectangular is THE dominant; only that "
        "no scanned non-rectangular beats it."
    )
    out.add_data("lean_uniqueness_ref", lean_uniqueness_ref("⁶Li"))
    out_path = out.save()
    print(f"\nWitness: {out_path}")


if __name__ == "__main__":
    main()
