#!/usr/bin/env python3
"""
Validation script for `probe_4_li6_rectangular_python.py`'s
Lanczos approach.

Computes `min_eig` and `max_eig` of the symmetric part of
`ρ_(4,4,4)(T_w_⁴He)` via Python LinearOperator + scipy eigsh,
then compares against the existing Rust-witness values:

  Rust witness:
    λ = (4,4,4), d_λ = 462
    min_eig = -1.9836e+01
    max_eig = +2.0735e+01

If Python-Lanczos matches Rust dense-LAPACK to ~5+ digits, the
Lanczos approach is validated for ⁶Li.

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
from probe_4_li6_rectangular_python import build_seminormal_fast
from mass_at_3A_proper import atom_braid_word_3A
from q_parameter import Q as q0


def apply_T_w(v, sigmas, word):
    out = v.copy()
    for (c, d, g) in reversed(word):
        # float64-ok: cast at the numpy boundary — `atom_braid_word_3A`
        # emits mpf, which promotes a float64 array to object dtype and
        # makes scipy refuse the conversion. See probe_4_li6_rectangular_
        # python.apply_T_w for the measurement.
        out = float(c) * (sigmas[g] @ out) + float(d) * out
    return out


def apply_T_w_T(v, sigmas_T, word):
    out = v.copy()
    for (c, d, g) in word:
        # float64-ok: same numpy boundary as `apply_T_w` above.
        out = float(c) * (sigmas_T[g] @ out) + float(d) * out
    return out


def main():
    h = float(q0) - 1.0 / float(q0)
    word = atom_braid_word_3A(2, 2)  # ⁴He
    print(f"⁴He T_w: {len(word)} crossings on B_12, h = {h:.10f}")

    shape = (4, 4, 4)
    print(f"\nBuilding seminormal for λ = {shape} …")
    t0 = time.time()
    sigmas, dim = build_seminormal_fast(shape, float(q0))
    sigmas_T = [sg.T.tocsr() for sg in sigmas]
    print(f"  dim = {dim}, build = {time.time() - t0:.2f}s")

    def matvec(v):
        return 0.5 * (apply_T_w(v, sigmas, word) + apply_T_w_T(v, sigmas_T, word))

    L = LinearOperator((dim, dim), matvec=matvec, dtype=np.float64)

    print("\nComputing top-2 eigvals (LA) …")
    t1 = time.time()
    w_max = eigsh(L, k=2, which="LA", maxiter=2000, tol=1e-8, return_eigenvectors=False)
    print(f"  done in {time.time() - t1:.2f}s. top-2 = {sorted(w_max, reverse=True)}")

    print("\nComputing bottom-2 eigvals (SA) …")
    t2 = time.time()
    w_min = eigsh(L, k=2, which="SA", maxiter=2000, tol=1e-8, return_eigenvectors=False)
    print(f"  done in {time.time() - t2:.2f}s. bottom-2 = {sorted(w_min)}")

    print("\n=== Cross-check vs Rust witness ===")
    print(f"  Python min_eig (Lanczos):  {float(min(w_min)):+.6e}")
    print(f"  Rust    min_eig (dense):   -1.983589e+01  (witness)")
    print(f"  Python max_eig (Lanczos):  {float(max(w_max)):+.6e}")
    print(f"  Rust    max_eig (dense):   +2.073531e+01  (witness)")
    print()
    print(f"  Δmin = {float(min(w_min)) - (-19.835887443514437):+.4e}")
    print(f"  Δmax = {float(max(w_max)) - 20.735310518978903:+.4e}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
