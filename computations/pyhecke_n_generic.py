#!/usr/bin/env python3
"""n-generic Python shim for pyhecke-native — fixes the H_3 hardcoded ABI.

Per author direction 2026-05-25 + infra audit (this branch's PR #1251):
the entire pyhecke-native NF-basis ABI is hardcoded to n=3 (6×6 basis
size for H_3). This module provides **arbitrary-n versions** of:

  - `trace_weights_n(n, q)` — Jones-Markov y_λ on H_n(q) for any n
  - `gram_matrix_n(n, q)` — Gram matrix via Schur orthogonality
  - `gram_inverse_n(n, q)` — REFUSES under convention D (the form is
    singular); see its docstring and bean `qou-cds2`
  - `markov_pairing_n(n, word_a, word_b, q)` — ⟨word_a | word_b⟩ via tr_M

Implementation: routes through `pyhecke_native.chi_lambda_braid` +
`pyhecke_jones_markov_atlas.solve_jones_markov_h_n` (both arbitrary-n,
generic over the entire Hecke tower). Sidesteps the n=3 lock entirely
without requiring Rust ABI refactor.

## Recommended migration

Production scripts currently using the n=3-locked ABI:

```python
# OLD (n=3 only — bug for A>1 atoms)
import pyhecke_native as pn
y = pn.trace_weights(q)               # length-6 only
G = pn.gram_matrix(q)                 # 6×6 only
Ginv = pn.gram_inverse(q)             # 6×6 only — now REMOVED, it raises

# NEW (arbitrary n — fixes the legacy H_3 hardcode)
from pyhecke_n_generic import trace_weights_n, gram_matrix_n, gram_inverse_n
y = trace_weights_n(n=12, q=q_0)      # length 77 (partitions of 12 for 4He)
G = gram_matrix_n(n=12, q=q_0)        # 77×77
# Ginv: there is NO inverse to migrate to. Under convention D the form is
# singular at every n (rank = partitions with <=2 rows, the TL/Catalan
# structure of qou-8iru), so gram_inverse_n RAISES rather than returning
# the 1e16-entry garbage numpy hands back without complaint. The inverse
# lives on the TL_n quotient — tracked under qou-8iru.
```

## Basis choice

The "NF basis" in the n=3 ABI is the Wedderburn block-decomposition
basis (size [n]_q! at q=1 = n!). For n>3 this grows factorially:
6 → 24 → 120 → 720 → ... → 479M for n=12.

This module instead uses the **partition basis** (one row per
partition λ ⊢ n), size p(n):

| n | NF basis (Rust ABI) | Partition basis (this module) |
|---|---------------------|---------------------------------|
| 3 | 6 | 3 |
| 6 | 720 | 11 |
| 9 | 362880 | 30 |
| 12 | 479M | 77 |

Partition basis is exponentially smaller AND matches the natural
Jones-Markov / Wedderburn decomposition (trace_weights = y_λ per
partition). Production scripts should think in terms of partition
basis going forward.

## Caveats

- The `n_strands` parameter is REQUIRED — no default backward-compat
  hack (caller must explicitly choose n).
- For very large n (≥ 12), `gram_matrix_n` may take minutes
  (p(n)² chi evaluations); cache the result.
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — bridge: reads a witness that co-moved into a cluster subdir
import _path_bridge as _pb  # noqa: E402 — cross-cluster witness lookup
from _precision import set_compute_dps  # noqa: E402 — raise dps before any mpmath value
import json
import sys
from pathlib import Path
from typing import Optional

import mpmath as mp
import numpy as np
import pyhecke_native as pn

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from pyhecke_jones_markov_atlas import (  # noqa: E402
    solve_jones_markov_h_n,
    cycle_type_braid,
    partitions_of_descending,
)

Q_PIN = _pb.witness_path("q-pinning-50-digit.witness.json", HERE)
# This producer never raised working precision, so every mpmath value in
# it was built at mpmath's default 15 dps and the numbers it emits are
# HONESTLY float64 — no fake precision to detect, no constant built too
# early, so the padding / raw-float64 / import-time gates all pass it.
# Gate: never_raises_dps_audit.py (bean qou-j6gb). Idempotent.
set_compute_dps()

Q0_F64 = float(mp.mpf(json.load(Q_PIN.open())["derived_50_digit"]["q"]))


def trace_weights_n(n: int, q: float = Q0_F64) -> list[float]:
    """Jones-Markov weights y_λ on H_n(q), one per partition λ ⊢ n.

    n-generic replacement for `pyhecke_native.trace_weights(q)` (which
    is length-6 hardcoded for H_3 only).

    Now delegates to the Rust upstream `pn.trace_weights_n(n, q)`
    landed in pyhecke-native 0.9.0+ (2026-05-25). Falls back to the
    Python atlas if the Rust function is unavailable.

    Returns y_λ in the order produced by `partitions_of_descending(n)`.
    Satisfies the Markov normalization: Σ_λ y_λ · dim_λ = 1 exactly.
    """
    if hasattr(pn, "trace_weights_n"):
        return pn.trace_weights_n(n, q)
    # Python fallback (cycle-type Schur orthogonality LP)
    atlas = solve_jones_markov_h_n(n, q=q)
    return atlas["y_lambda"]


def gram_matrix_n(n: int, q: float = Q0_F64, basis: str = "partition") -> np.ndarray:
    """Gram matrix on H_n(q).

    n-generic replacement for `pyhecke_native.gram_matrix(q)` (which is
    6×6 hardcoded for H_3 only).

    `basis`:
      - "partition" (default) — p(n)×p(n); G[i,j] = δ_{i,j} · y_{λ_i} · dim_{λ_i}
        (diagonal in the Wedderburn basis; this is the bilinear form
        induced by Markov trace on the partition basis)
      - "cycle_type" — p(n)×p(n); G[i,j] = tr_M(rep_i · rep_j)
        (Markov pairing on cycle-type representatives)

    The partition basis is the natural choice for downstream LP / SDP
    formulations.
    """
    shapes = partitions_of_descending(n)
    P = len(shapes)

    if basis == "partition":
        # Diagonal: G_ii = y_{λ_i} · dim_{λ_i}
        atlas = solve_jones_markov_h_n(n, q=q)
        y = atlas["y_lambda"]
        dims = atlas["dims_classical"]
        G = np.zeros((P, P), dtype=np.float64)
        for i in range(P):
            G[i, i] = y[i] * dims[i]
        return G

    elif basis == "cycle_type":
        # G[i, j] = tr_M(rep_i · rep_j) via Markov pairing
        atlas = solve_jones_markov_h_n(n, q=q)
        y = atlas["y_lambda"]
        rep_words = [cycle_type_braid(sh) for sh in shapes]
        # Compute composite words rep_i ⊕ rep_j (concatenation) and apply atlas
        # tr_M(w_i · w_j) = Σ_λ y_λ · χ_λ(w_i · w_j)
        G = np.zeros((P, P), dtype=np.float64)
        for i in range(P):
            for j in range(P):
                composite = rep_words[i] + rep_words[j]
                chi_vals = pn.chi_lambdas_braid(shapes, composite, q)
                G[i, j] = sum(y[k] * chi_vals[k] for k in range(P))
        return G

    else:
        raise ValueError(f"basis must be 'partition' or 'cycle_type', got {basis!r}")


def gram_inverse_n(n: int, q: float = Q0_F64, basis: str = "partition") -> np.ndarray:
    """Gram inverse on H_n(q) — REFUSES under convention D, where G is singular.

    🛑 This is the general-n successor to `pyhecke.gram.gram_inverse`, which was
    DELETED for exactly this reason (bean `qou-cds2`); the guard did not come
    with it. It previously did a bare ``np.linalg.inv(G)``.

    Under convention D the Markov–Gram form is identically singular: its radical
    is the Temperley–Lieb ideal, so the rank is the number of partitions of `n`
    with at most two rows, not `p(n)` (bean `qou-8iru`). Measured here:

        n=3   dim 3   rank 2   corank 1   cond 2.5e16   max|G^-1| 5.03e16
        n=4   dim 5   rank 3   corank 2   cond 1.8e16   max|G^-1| 3.27e16

    and the corank grows fast — 10 at n=4 and 78 at n=5 in the NF basis
    (`qou-cds2`).

    ⚠️ THE OBVIOUS SANITY CHECK DOES NOT CATCH THIS. ``numpy`` raises nothing,
    and the returned matrix satisfies ``‖G·G⁻¹ − I‖ = 1.11e-16`` at n=3 and
    **exactly 0** at n=4 — the entries are so large that the product rounds to
    the identity in float64. A consumer that validates the residual is handed a
    clean bill of health on a meaningless inverse. That is why this raises
    rather than warning: there is no downstream check that would notice.

    The inverse exists on the QUOTIENT `H_n(q)/rad = TL_n(q)`, where the form is
    non-singular for every real q > 0 — proved exactly over ℚ(q) in
    `computations/qbeta/tl3_gram_nonsingular_probe.py`. Building the form there
    is tracked under `qou-8iru`; this function does not do it.
    """
    G = gram_matrix_n(n, q, basis=basis)
    rank = int(np.linalg.matrix_rank(G))
    if rank < G.shape[0]:
        raise NotImplementedError(
            f"gram_inverse_n(n={n}): the convention-D Markov-Gram form is "
            f"SINGULAR — rank {rank} of {G.shape[0]} (corank "
            f"{G.shape[0] - rank}), cond {np.linalg.cond(G):.2e}. numpy would "
            f"return entries of order 1e16 WITHOUT raising, and ||G.G^-1 - I|| "
            f"rounds to ~0, so the residual check does not catch it. The "
            f"inverse exists on the TL_n quotient (bean qou-8iru); use that, or "
            f"a rank-guarded pseudo-inverse if a least-squares solution is what "
            f"you actually want."
        )
    return np.linalg.inv(G)


def markov_pairing_n(
    n: int,
    word_a: list[tuple[int, int]],
    word_b: list[tuple[int, int]],
    q: float = Q0_F64,
) -> float:
    """⟨word_a | word_b⟩_M = tr_M(word_a · word_b) on H_n(q).

    n-generic replacement for the (implicit) Markov pairing in
    `pn.nf_tr` / `pn.hm` (n=3 only).
    """
    atlas = solve_jones_markov_h_n(n, q=q)
    composite = word_a + word_b
    shapes = atlas["partitions"]
    chi_vals = pn.chi_lambdas_braid(shapes, composite, q)
    return float(sum(atlas["y_lambda"][i] * chi_vals[i] for i in range(len(shapes))))


# ---- demo + cross-check vs hardcoded H_3 ABI ----
if __name__ == "__main__":
    print("=" * 80)
    print("pyhecke_n_generic — n-generic shim demo + n=3 cross-check")
    print("=" * 80)
    print()

    print("§1. trace_weights at H_3 — cross-check vs hardcoded pn.trace_weights")
    y3 = trace_weights_n(3)
    y3_pn = pn.trace_weights(Q0_F64)
    shapes3 = partitions_of_descending(3)
    print(f"  n-generic y_λ for H_3 (3 partitions):")
    for sh, yv in zip(shapes3, y3):
        print(f"    λ={tuple(sh)}: y = {yv:+.10f}")
    print(f"  hardcoded pn.trace_weights (length-6 NF basis): {y3_pn[:3]} (first 3)")
    print(f"  NOTE: my y_λ is partition basis (3 values); pn is NF basis (6 values)")
    print(f"  Σ y_λ · dim_λ (my) = {sum(y3[i] * (1, 2, 1)[i] for i in range(3)):.10f}")
    print()

    print("§2. gram_matrix_n(n=3) — partition basis")
    G3 = gram_matrix_n(3)
    print(f"  Shape: {G3.shape}")
    print(f"  Diagonal: {[G3[i, i] for i in range(3)]}")
    print()

    print("§3. trace_weights at H_6 (deuteron) — sizes 11 partitions")
    y6 = trace_weights_n(6)
    shapes6 = partitions_of_descending(6)
    print(f"  y_λ for H_6 ({len(shapes6)} partitions):")
    for sh, yv in zip(shapes6[:5], y6[:5]):
        print(f"    λ={tuple(sh)}: y = {yv:+.10f}")
    print(f"    ... ({len(shapes6)-5} more)")
    dims6 = [int(pn.chi_lambda_braid(sh, [], Q0_F64) + 0.5) for sh in shapes6]
    print(f"  Σ y_λ · dim_λ = {sum(y6[i] * dims6[i] for i in range(11)):.10f}")
    print()

    print("§4. Demonstrating the fix — what production scripts gain")
    print(f"  Old API: pn.gram_matrix(q) returns 6×6 (FIXED H_3)")
    print(f"  New API: gram_matrix_n(n=12, q) returns {(77, 77)} (H_12 for 4He)")
    print(f"         : gram_matrix_n(n=24, q) would return (1575, 1575) (H_24 for 8Be)")
    print()
    print("§5. Migration recipe")
    print("  Replace: from pyhecke_native import trace_weights, gram_matrix")
    print("    With: from pyhecke_n_generic import trace_weights_n, gram_matrix_n")
    print("  gram_inverse has NO migration target: the convention-D form is")
    print("  singular at every n, so gram_inverse_n refuses. See qou-cds2.")
    print("  Pass n_strands explicitly (3A for atom A).")
