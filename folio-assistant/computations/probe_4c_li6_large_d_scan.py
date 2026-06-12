#!/usr/bin/env python3
"""
Probe (4c): extend the ⁶Li falsification scan to the large-d_λ tail.

Probe (4b) covered 16 shapes with d_λ ≤ 150k. This script extends to
several non-rectangular shapes with d_λ ∈ [150k, 1M] that were
specifically flagged as "near-rectangular" candidates that could
potentially beat the rectangle's −96.52:

  (5, 5, 5, 3)       d_λ = 875,160  ← near-rect, 3-row + tail
  (4, 4, 4, 3, 3)    d_λ = 875,160  ← near-rect, 3-row + 2-row tail
  (3, 3, 3, 3, 2, 2, 2)  d_λ = 364,650  ← near-transpose
  (10, 4, 4)         d_λ = 259,896  ← 3-row asymmetric
  (8, 8, 2)          d_λ = 136,136  ← already in (4b), included for comparison

Lanczos matvec cost scales O(|word| · nnz) per call; for d_λ ≈ 1M
this is ~1-2 sec/matvec, ~1-2 min/shape including build.

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


def main():
    word = atom_braid_word_3A(3, 3)
    print(f"⁶Li T_w: {len(word)} crossings on B_18")

    candidates = [
        (5, 5, 5, 3),
        (4, 4, 4, 3, 3),
        (3, 3, 3, 3, 2, 2, 2),
        (10, 4, 4),
    ]

    print(f"\n{'shape':>22s}  {'d_λ':>8s}  {'build':>8s}  {'eig':>8s}  {'min_eig':>10s}  {'max_eig':>10s}  beats -96.52?")

    results = []
    for shape in candidates:
        t0 = time.time()
        sigmas, dim = build_seminormal_fast(shape, float(q0))
        sigmas_T = [sg.T.tocsr() for sg in sigmas]
        t_b = time.time() - t0

        def matvec(v):
            return 0.5 * (apply_T_w(v, sigmas, word, 0.0)
                          + apply_T_w_T(v, sigmas_T, word, 0.0))

        L = LinearOperator((dim, dim), matvec=matvec, dtype=np.float64)
        t1 = time.time()
        w_min = eigsh(L, k=1, which="SA", maxiter=2000, tol=1e-6, return_eigenvectors=False)
        w_max = eigsh(L, k=1, which="LA", maxiter=2000, tol=1e-6, return_eigenvectors=False)
        t_e = time.time() - t1

        beats = float(w_min[0]) < -96.52
        marker = "  ← FALSIFIES" if beats else ""
        print(f"{str(list(shape)):>22s}  {dim:>8d}  {t_b:>7.1f}s  {t_e:>7.1f}s  {float(w_min[0]):+10.4f}  {float(w_max[0]):+10.4f}  {beats}{marker}")
        results.append({
            "shape": list(shape),
            "dim": dim,
            "min_eig": float(w_min[0]),
            "max_eig": float(w_max[0]),
            "build_s": t_b,
            "eig_s": t_e,
            "beats_rectangular": beats,
        })

    any_falsifies = any(r["beats_rectangular"] for r in results)
    print(f"\nVerdict: {'FALSIFIED' if any_falsifies else 'CONSISTENT with rectangular conjecture'}")

    out = WitnessBuilder("probe-4c-li6-large-d-scan", engine="python")
    out.set_description(
        "Extends Probe (4b) to ⁶Li non-rectangular shapes with d_λ in "
        "[150k, 1M]. Tests whether any near-rectangular shape with a "
        "small defect (extra row or partial-rectangle tail) beats the "
        "(A,A,A) rectangle's −96.52 min_eig."
    )
    out.set_audit_only(
        "docs/audits/2026-05-25-dominant-partition-nucleon-structure.md"
    )
    out.set_content_block("conj:atom-braid-exterior-algebra")
    out.add_data("scanned_partitions", results)
    out.add_data("benchmark_rectangular_min_eig", -96.52)
    out.add_assertion(
        name="no_large_d_non_rectangular_beats_rectangular",
        computed=str(int(not any_falsifies)),
        expected="1",
        tolerance=0,
        source=f"Scanned {len(results)} large-d non-rect; {sum(r['beats_rectangular'] for r in results)} falsify.",
    )

    out.add_data("lean_uniqueness_ref", lean_uniqueness_ref("⁶Li"))
    out_path = out.save()
    print(f"\nWitness: {out_path}")


if __name__ == "__main__":
    main()
