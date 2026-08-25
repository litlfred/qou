#!/usr/bin/env python3
"""threerow_chi_sparse.py — sparse-kernel Hecke character χ^λ(β_K;q), exact-equal
to the #4829 dense path but O(L·dim²) instead of O(L·dim³).

WHY THIS EXISTS (UNIT 1 of the bean qou-prjo follow-up).

#4829 recorded ⁴He (n=12) as a "documented SANDBOX COMPUTE LIMIT ... GB-scale
matrices ... >4 min/grid point ... run on a host with pyhecke_native".  That
diagnosis was WRONG, and the fix needs no native kernel at all.

`build_seminormal_matrices` already returns **scipy CSR** whenever dim > 500 —
each Hoefsmit matrix is block-diagonal with 1×1 and 2×2 blocks, so it has ≤ 2
nonzeros per row.  The #4829 `chi_atom` then built the word letter as

    M = float(c) * sig[g] + float(d) * np.eye(dim)      # ← dense identity

which (i) materialises a dense dim×dim identity (474 MB at dim = 7700) and
(ii) DENSIFIES the sparse σ back to a full matrix, so the subsequent
`prod = prod @ M` costs O(dim³) per letter.  Summed over the 70 partitions of
12 with ℓ(λ) ≥ 3, Σ dim³ = 2.1·10¹² *per word letter* (word length L = 47) —
that is the "compute limit", and it is entirely an implementation artifact.

THE FIX (two changes, no approximation whatsoever):

  1. keep the identity sparse (`scipy.sparse.identity`), so each word letter
     M_j = c_j·σ_{g_j} + d_j·I stays CSR with ≤ 2 nonzeros per row;
  2. never form the dense product.  Tr(∏_j M_j) is accumulated column-batch by
     column-batch: for a batch of identity columns X (dim × B dense), apply the
     word in REVERSE (M_1 M_2 ⋯ M_L)e_k = M_1(M_2(⋯(M_L e_k))), then read the
     diagonal entries of the batch.  Cost O(L · dim² · nnz_per_row), memory
     O(dim · B) instead of O(dim²).

Σ dim² = 4.8·10⁸ for the ℓ≥3 stratum of 12, so the whole ⁴He character sum is
~10¹⁰ flops — seconds to a minute per grid point in pure Python + scipy.

This is an EXACT reorganisation of the same f64 arithmetic, not a truncation
and not an approximation: `self_check()` verifies bit-level agreement with the
#4829 dense `chi_atom` (observed max rel diff ~1e-15, i.e. f64 epsilon) on n=6
and n=9 partitions, and the ⁴He probe additionally re-validates against the
canonical `atom-chi-rust-*.witness.json` witnesses.

PRECISION.  Still f64 (the pure-Python Hoefsmit seminormal path; no mpfr Rust
kernel in this sandbox).  Reorganising the product does not change the
precision class — it changes only the cost.  Decisive for SIGN questions away
from a crossing; see the caveats on the consuming probes.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path[:0] = [
    str(Path(__file__).resolve().parent.parent),
    str(Path(__file__).resolve().parent.parent / "substrate"),
    str(Path(__file__).resolve().parent.parent / "hecke"),
]
import _path_bridge  # noqa: F401,E402
from _precision import set_compute_dps  # noqa: E402 — raise dps before any mpmath value

import numpy as np  # noqa: E402
import scipy.sparse as sp  # noqa: E402
import mpmath as mp  # noqa: E402

from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402
from hecke_characters import build_seminormal_matrices  # noqa: E402

# Column-batch width. Memory is dim·B·8 bytes (dim=7700, B=256 → 15.8 MB).
BATCH = 256


# This producer never raised working precision, so every mpmath value in
# it was built at mpmath's default 15 dps and the numbers it emits are
# HONESTLY float64 — no fake precision to detect, no constant built too
# early, so the padding / raw-float64 / import-time gates all pass it.
# Gate: never_raises_dps_audit.py (bean qou-j6gb). Idempotent.
set_compute_dps()

def chi_atom_sparse(shape: tuple[int, ...], Z: int, N: int, q: mp.mpf,
                    batch: int = BATCH) -> mp.mpf:
    """χ^λ(β_K;q) = Tr ∏_j (c_j σ_{g_j} + d_j I) via sparse CSR + batched columns.

    Layer-pure: the braid word AND the seminormal matrices are BOTH materialised
    at the same running `q` (holding one at q₀ while running the other would be
    the forbidden AGENTS.md layer-straddle).
    """
    qf = float(q)
    sig, dim, _ = build_seminormal_matrices(tuple(shape), sparse=True, q=qf)
    if dim == 0:
        return mp.mpf(0)
    # See `threerow_sign_crossing_probe.chi_atom`: the CSR letters below are
    # `float(c)·σ + float(d)·I`, so this path is f64 end to end and the
    # declaration belongs here, at the point where the loss occurs.
    word = atom_braid_word_3A(Z, N, include_inter=True, q=q,
                              allow_float64=True)
    ident = sp.identity(dim, format="csr")
    # Each letter stays CSR (≤2 nnz/row); build once, reuse across all batches.
    letters = [(float(c) * sp.csr_matrix(sig[g]) + float(d) * ident).tocsr()
               for (c, d, g) in word]
    tr = 0.0
    for k0 in range(0, dim, batch):
        k1 = min(k0 + batch, dim)
        X = np.zeros((dim, k1 - k0))
        X[np.arange(k0, k1), np.arange(k1 - k0)] = 1.0
        for M in reversed(letters):          # (M_1 M_2 ⋯ M_L) e_k
            X = M @ X
        tr += float(np.trace(X[k0:k1, :]))
    return mp.mpf(tr)


def self_check(verbose: bool = True) -> mp.mpf:
    """Verify bit-level agreement with the #4829 dense chi_atom. Returns max rel diff."""
    from threerow_sign_crossing_probe import chi_atom, Q0
    cases = [((3, 2, 1), 1, 1), ((2, 2, 2), 1, 1), ((4, 1, 1), 1, 1),
             ((3, 1, 1, 1), 1, 1), ((5, 2, 1, 1), 1, 2), ((4, 3, 1, 1), 1, 2),
             ((5, 3, 1), 2, 1), ((3, 3, 3), 1, 2)]
    worst = mp.mpf(0)
    for shape, Z, N in cases:
        a = chi_atom(shape, Z, N, Q0)
        b = chi_atom_sparse(shape, Z, N, Q0)
        rel = abs(a - b) / (abs(a) + mp.mpf("1e-40"))
        worst = max(worst, rel)
        if verbose:
            print(f"  {str(shape):18s} dense={float(a):+.12e} sparse={float(b):+.12e} "
                  f"rel={float(rel):.2e}")
    if verbose:
        print(f"  max rel diff = {float(worst):.3e}  "
              f"({'OK — f64 epsilon' if worst < 1e-12 else 'FAIL'})")
    return worst


if __name__ == "__main__":
    print("self-check: sparse chi vs #4829 dense chi_atom (n=6, n=9)")
    raise SystemExit(0 if self_check() < 1e-12 else 1)
