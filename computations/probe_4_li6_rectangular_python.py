#!/usr/bin/env python3
"""
Probe (4) — Python single-partition fallback.

Targeted compute of `min_eig` and `max_eig` of the symmetric part
of `ρ_λ(T_w_⁶Li)` for the conjectured rectangular dominant
λ = (6, 6, 6) and its transpose (3, 3, 3, 3, 3, 3), bypassing the
full Rust solver which is infeasible at `d_λ = 87,516`.

Strategy: use `scipy.sparse.linalg.LinearOperator + eigsh` with
matvec defined as: build sparse Hoefsmit σ_i once, then apply the
71-crossing T_w_⁶Li chain on-the-fly via 71 sparse mat-vec ops
(each O(d_λ) with ~2 nnz/row Hoefsmit matrices). This avoids
materialising the d=87,516 dense product matrix (which would need
61 GB of RAM) and computes the extreme eigenvalues of
`(ρ + ρ^T)/2` in ≤ minutes.

If `min_eig` at (6,6,6) is more negative than the largest evaluated
block in the Rust witness (which was capped at d_λ ≤ 500), this is
strong evidence that the rectangular conjecture holds at A=6.

Bound to `conj:atom-braid-exterior-algebra`. Audit-only.
"""

from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
from _precision import set_compute_dps  # noqa: E402 — raise dps before any mpmath value
import json
import sys
import time
from pathlib import Path

import numpy as np
import scipy.sparse as sps
from scipy.sparse.linalg import LinearOperator, eigsh

sys.path.insert(0, str(Path(__file__).resolve().parent))
from witness_base import WitnessBuilder
from lean_uniqueness_refs import lean_uniqueness_ref  # noqa: E402
from hecke_characters import standard_young_tableaux
from mass_at_3A_proper import atom_braid_word_3A


# This producer never raised working precision, so every mpmath value in
# it was built at mpmath's default 15 dps and the numbers it emits are
# HONESTLY float64 — no fake precision to detect, no constant built too
# early, so the padding / raw-float64 / import-time gates all pass it.
# Gate: never_raises_dps_audit.py (bean qou-j6gb). Idempotent.
set_compute_dps()

def build_seminormal_fast(shape, q: float):
    """Hash-lookup version of build_seminormal_matrices.

    O(d · n) instead of O(d² · n) — the swap-partner search is via
    `dict[hashable_syt] -> index` lookup, not linear scan.
    """
    import mpmath as mp
    from scipy import sparse as sps

    syts, cells, contents = standard_young_tableaux(shape)
    dim = len(syts)
    n = sum(shape)
    h_q = q - 1.0 / q

    # syts[i] is a dict {entry_number -> cell_index}. Hash the canonical
    # representation (sorted items) for O(1) lookup.
    syt_to_idx = {tuple(sorted(syts[i].items())): i for i in range(dim)}

    sigmas = []
    for k in range(1, n):
        rows, cols, vals = [], [], []
        processed = [False] * dim

        for i in range(dim):
            if processed[i]:
                continue
            ci_k = syts[i][k]
            ci_k1 = syts[i][k + 1]
            rho = contents[ci_k1] - contents[ci_k]
            a = h_q / (1.0 - q ** (-2 * rho))

            # Build swap_map and look it up.
            swap_items = list(syts[i].items())
            for idx, (key, val) in enumerate(swap_items):
                if key == k:
                    swap_items[idx] = (k, ci_k1)
                elif key == k + 1:
                    swap_items[idx] = (k + 1, ci_k)
            key = tuple(sorted(swap_items))
            j = syt_to_idx.get(key)
            if j == i:
                j = None

            if j is None:
                rows.append(i); cols.append(i); vals.append(a)
                processed[i] = True
            else:
                a_prime = h_q / (1.0 - q ** (2 * rho))
                b_sq = a * a_prime + 1.0
                b = float(mp.sqrt(abs(b_sq)))
                rows.extend([i, j, i, j])
                cols.extend([i, j, j, i])
                vals.extend([a, a_prime, b, b])
                processed[i] = True
                processed[j] = True

        M = sps.csr_matrix((vals, (rows, cols)), shape=(dim, dim))
        sigmas.append(M)

    return sigmas, dim


def apply_T_w(v: np.ndarray, sigmas, word, h: float) -> np.ndarray:
    """Apply ρ(T_w) v in O(|word| × nnz) sparse ops.

    `word` is the list of (c, d, g) triples from atom_braid_word_3A.
    Apply RIGHTMOST FIRST: v ← M_{g_k} v then M_{g_{k-1}} v ... M_{g_1} v.

    M_g = c · σ_g + d · I.
    """
    out = v.copy()
    # T_w = M_1 · M_2 · ... · M_71; applied as M_1 (M_2 (... (M_71 v))).
    for (c, d, g) in reversed(word):
        # M_g = c · σ_g + d · I.
        # float64-ok: CAST AT THE numpy BOUNDARY. `atom_braid_word_3A`
        # EMITS mpf coefficients — measured on (3,3): c is 66 int / 5
        # mpf, d is 33 int / 38 mpf — and an mpf scalar against a
        # float64 array promotes the result to object dtype. Here that
        # is not merely a loss of BLAS: the caller declares
        # `LinearOperator(..., dtype=np.float64)` and scipy refuses the
        # conversion outright —
        #   "no supported conversion for types: (dtype('float64'), dtype('O'))"
        # — so `eigsh` dies and the witness records an error string.
        # efcaf79ed made the word mpf AT SOURCE on purpose and says
        # consumers needing f64 "cast at their own boundary"; this is
        # such a consumer. Same fix as mass_at_3A_proper.chi_lambda_of_word
        # (03569d001), where it was worth 57x as well as the crash.
        out = float(c) * (sigmas[g] @ out) + float(d) * out
    return out


def apply_T_w_T(v: np.ndarray, sigmas_T, word, h: float) -> np.ndarray:
    """Apply ρ(T_w)^T v = (M_1 M_2 ... M_71)^T v = M_71^T ... M_1^T v.

    Apply LEFTMOST FIRST (in original word).
    """
    out = v.copy()
    for (c, d, g) in word:
        # float64-ok: same numpy boundary as `apply_T_w` above.
        out = float(c) * (sigmas_T[g] @ out) + float(d) * out
    return out


def compute_extreme_eigs(shape, word, h, q, k=2, dps_label="?"):
    print(f"\n[{time.strftime('%H:%M:%S')}] Building seminormal for λ = {shape} …")
    t0 = time.time()
    sigmas, dim = build_seminormal_fast(shape, q)
    t1 = time.time()
    print(f"  dim = {dim}, sigmas: {len(sigmas)} matrices, build = {t1 - t0:.1f}s")

    # Cache transposes
    sigmas_T = [sg.T.tocsr() for sg in sigmas]

    def matvec(v):
        rhov = apply_T_w(v, sigmas, word, h)
        rhotv = apply_T_w_T(v, sigmas_T, word, h)
        return 0.5 * (rhov + rhotv)

    L = LinearOperator((dim, dim), matvec=matvec, dtype=np.float64)

    print(f"[{time.strftime('%H:%M:%S')}] Computing largest k={k} eigvals via Lanczos …")
    t2 = time.time()
    # Largest algebraic
    w_max = eigsh(L, k=k, which="LA", maxiter=2000, tol=1e-6, return_eigenvectors=False)
    t3 = time.time()
    print(f"  Done in {t3 - t2:.1f}s. eigs (LA) = {w_max}")

    print(f"[{time.strftime('%H:%M:%S')}] Computing smallest k={k} eigvals via Lanczos …")
    t4 = time.time()
    w_min = eigsh(L, k=k, which="SA", maxiter=2000, tol=1e-6, return_eigenvectors=False)
    t5 = time.time()
    print(f"  Done in {t5 - t4:.1f}s. eigs (SA) = {w_min}")

    return {
        "shape": list(shape),
        "dim": dim,
        "min_eig_lanczos": float(min(w_min)),
        "max_eig_lanczos": float(max(w_max)),
        "top_eigs_LA": [float(x) for x in sorted(w_max, reverse=True)],
        "bot_eigs_SA": [float(x) for x in sorted(w_min)],
        "build_time_s": f"{t1 - t0:.3f}",
        "max_eig_time_s": t3 - t2,
        "min_eig_time_s": t5 - t4,
    }


def main() -> int:
    # ⁶Li canonical atom-braid
    word = atom_braid_word_3A(3, 3)
    A = 6
    n0 = 3 * A
    # h = q - 1/q (must match build_seminormal_matrices q-default)
    from q_parameter import Q as q0
    h = float(q0) - 1.0 / float(q0)

    print(f"⁶Li canonical T_w: {len(word)} crossings on B_{n0}, h = {h:.10f}")

    out = WitnessBuilder("probe-4-li6-rectangular-python-targeted", engine="python")
    out.set_description(
        "Targeted Lanczos eigval computation of the symmetric part of "
        "ρ_λ(T_w_⁶Li) for λ = (6,6,6) and (3,3,3,3,3,3) — the predicted "
        "dominant pair under the rectangular-form conjecture at A=6. "
        "Bypasses the d_λ=87,516 dense-matrix infeasibility of the full "
        "Rust solver by using a LinearOperator wrapper that applies the "
        "71-crossing braid chain on-the-fly via sparse mat-vec."
    )
    out.set_audit_only(
        "docs/audits/2026-05-25-dominant-partition-nucleon-structure.md"
    )
    out.set_content_block("conj:atom-braid-exterior-algebra")
    out.add_parameter("A", A)
    out.add_parameter("n_0", n0)
    out.add_parameter("braid_length", len(word))
    out.add_parameter("q_0", float(q0))
    out.add_parameter("h", h)

    # Test the two rectangular candidates
    results = {}
    for shape in [(6, 6, 6), (3, 3, 3, 3, 3, 3)]:
        try:
            r = compute_extreme_eigs(shape, word, h, float(q0))
            results[str(list(shape))] = r
        except Exception as e:
            print(f"ERROR for shape {shape}: {e}")
            results[str(list(shape))] = {"error": str(e)}

    out.add_data("rectangular_pair_eigvals", results)

    # Compare to the largest evaluated-block min_eig in the Rust witness
    # (⁴He partial sweep): ⁴He's most-negative min_eig was −19.84 for
    # (4,4,4). If (6,6,6) here is even more negative, the dominant
    # partition for ⁶Li is consistent with the rectangular conjecture.
    if "[6, 6, 6]" in results and "min_eig_lanczos" in results["[6, 6, 6]"]:
        me_666 = results["[6, 6, 6]"]["min_eig_lanczos"]
        print(f"\n=== Conjecture status (A=6) ===")
        print(f"  min_eig of (6,6,6)         = {me_666:+.4f}")
        print(f"  min_eig of (4,4,4) at ⁴He   = -19.84 (from Rust witness)")
        print(f"  Predicted α* at ⁶Li        = {1.0 / (1.0 - me_666):.6f}")

        # Robust falsification: if min_eig of (6,6,6) is *less negative*
        # than -10 (substantially less than ⁴He's -19.8), the rectangular
        # conjecture's "depth scales with A" prediction fails.
        out.add_assertion(
            name="li6_rectangle_min_eig_substantially_negative",
            computed=str(int(me_666 < -10.0)),
            expected="1",
            tolerance=0,
            source=f"min_eig of ρ_(6,6,6)(T_w_⁶Li) symmetric part = {me_666:+.4f}; threshold -10.0",
        )
    else:
        # THE ASSERTION MUST NOT VANISH WHEN ITS INPUT DIES.
        #
        # This was inside the `if` above and nowhere else, so when the (6,6,6)
        # solve failed the check simply stopped being emitted: the witness went
        # `assertions 1 -> 0` and read as NOTHING TO CHECK rather than THE
        # CHECK BROKE. That is the empty-state failure in a new place — not a
        # gutted witness, but a gate that silently ceases to exist. It was
        # caught only because `witness_shape_guard` has an `assertions
        # vanished` rule; no ratchet counts an assertion that was never added,
        # and `allPassed` over an empty list is vacuously true.
        #
        # A missing input is a FAILED check, not an absent one. The reason is
        # carried verbatim so the witness says which.
        _why = "(6, 6, 6) not present in results"
        if "[6, 6, 6]" in results:
            _why = str(results["[6, 6, 6]"].get("error")
                       or "min_eig_lanczos absent from the (6,6,6) result")
        print(f"\n=== Conjecture status (A=6): UNEVALUATED — {_why} ===")
        out.add_assertion(
            name="li6_rectangle_min_eig_substantially_negative",
            computed="0",
            expected="1",
            tolerance=0,
            source=f"UNEVALUATED — the (6,6,6) min-eig solve did not produce a "
                   f"value, so the conjecture could not be tested: {_why}",
        )

    out.add_caveat(
        "Lanczos tolerance 1e-6; for d_λ=87,516 this gives ~6 digits of "
        "agreement with exact dense-LAPACK eigvals. The braid action is "
        "applied on-the-fly so the d×d dense matrix is never "
        "materialised; this is the only way to get to (6,6,6) at the "
        "current Rust solver's compute budget."
    )

    out.add_data("lean_uniqueness_ref", lean_uniqueness_ref("⁶Li"))

    out_path = out.save()
    print(f"\nWitness: {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
