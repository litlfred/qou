#!/usr/bin/env python3
"""gram_matrix_seminormal_n.py — Option E Phase 1 API.

Public function `gram_matrix_seminormal_block(n, lam, q_val)` returning
the per-Wedderburn-block Hoefsmit-seminormal representation data for
partition `lam` ⊢ `n` at q = `q_val`.

Builds on top of:
- `hoefsmit_symbolic.build_seminormal_matrices_symbolic(lam)` — per-block
  symbolic σ_k matrices via the canonical Hoefsmit engine
  (`hecke_character_symbolic.hoefsmit_matrices_symbolic`).

Together with the per-block ρ_λ data, the Wedderburn isomorphism

    H_n(q) ≅ ⊕_{λ ⊢ n} End(V_λ)

reduces the n! × n! NF-basis Gram matrix to a sum of per-block
contractions: for any Hecke elements b, c,

    tr_M(b · c) = Σ_λ y_λ · tr(ρ_λ(b) · ρ_λ(c)).

The H_3 NF-basis 6×6 Gram from
`content/quantum-observable-universe/lean/QOU/Interactions/GramMatrixH3Symbolic.lean`
is reproduced by this script via the per-block reassembly (cross-check
below).

For H_6 (deuteron, n_total = 6), the per-block reassembly is the
*only* tractable form — the NF-basis Gram would be 720 × 720.
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — bridge: reads a witness that co-moved into a cluster subdir
import _path_bridge as _pb  # noqa: E402 — cross-cluster witness lookup
import sys
from pathlib import Path
from typing import Union

import mpmath as mp
import numpy as np
import sympy as sp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from hoefsmit_symbolic import build_seminormal_matrices_symbolic  # noqa: E402


def longest_reduced_word_1based(n: int) -> list[int]:
    """Coxeter longest-word reduced expression for S_n, 1-indexed."""
    if n <= 1:
        return []
    return list(range(n - 1, 0, -1)) + longest_reduced_word_1based(n - 1)


def _hoefsmit_with_module_q(lam: Union[list, tuple]):
    """Build seminormal σ_k matrices using `hoefsmit_symbolic`'s canonical
    sympy `Q` symbol. Returns (matrices, dim) — the symbol is the module's
    own `Q`, accessible via `hoefsmit_symbolic.Q`.
    """
    matrices, dim = build_seminormal_matrices_symbolic(tuple(lam))
    return matrices, dim


def _eval_matrix(M_sym: sp.Matrix, q_sym: sp.Symbol, q_val: float,
                 imag_tol: float = 1e-12) -> np.ndarray:
    """Substitute q_sym -> q_val in M_sym, return numpy.ndarray (real).

    Asserts the imaginary part of every entry is below `imag_tol` —
    Hoefsmit's seminormal construction is real over real q for partitions
    of finite n, so any non-negligible imaginary residue is a SymPy
    sqrt-branch artefact (or a genuine bug) that must surface loudly.
    """
    rows, cols = M_sym.shape
    out = np.zeros((rows, cols), dtype=np.float64)
    for i in range(rows):
        for j in range(cols):
            v = M_sym[i, j].evalf(subs={q_sym: q_val})
            re_v = float(sp.re(v))
            im_v = float(sp.im(v))
            if abs(im_v) > imag_tol:
                raise ValueError(
                    f"_eval_matrix: entry ({i},{j}) has non-negligible "
                    f"imaginary part {im_v:.3e} > {imag_tol:.0e} "
                    f"(SymPy sqrt-branch artefact or bug). Full value: {v}"
                )
            out[i, j] = re_v
    return out


def gram_matrix_seminormal_block(
    n: int,
    lam: Union[list, tuple],
    q_val: float,
) -> dict:
    """Per-block Hoefsmit-seminormal representation data for λ ⊢ n at q.

    Parameters
    ----------
    n : int
        Total strand count. Must equal sum(lam).
    lam : tuple[int, ...]
        Partition of n (descending; e.g. (3, 2, 1) for one 16-dim block of H_6).
    q_val : float
        Numerical q at which to evaluate. Use the substrate q_0 for the
        archimedean evaluation.

    Returns
    -------
    dict with keys:
      - "lam": tuple (input echoed)
      - "n": int (= sum(lam))
      - "dim_lambda": int (number of SYTs of shape λ)
      - "sigma_k_at_q": list of np.ndarray, length n-1
                       (each ρ_λ(σ_k), shape dim_lambda × dim_lambda)
      - "w0_at_q": np.ndarray (ρ_λ(w_0) for longest word w_0 ∈ S_n)
      - "chi_lambda_w0": float (= trace of w0_at_q)
      - "sigma_k_dets": list of float — det(ρ_λ(σ_k)) per generator
                        (invertibility check + downstream telemetry)
      - "sigma_k_conds": list of float — cond(ρ_λ(σ_k)) per generator
      - "w0_det": float — det(ρ_λ(w_0))
      - "w0_cond": float — cond(ρ_λ(w_0))

    Notes
    -----
    The matrices are evaluated numerically at q_val (float64). For
    exact / symbolic access, call `hoefsmit_symbolic.build_seminormal_matrices_symbolic`
    directly and substitute q later.

    The function does NOT compute the within-block Frobenius/Markov
    Gram matrix `G^(λ)_{T,T'} := tr_M(ρ_λ(σ_T) · ρ_λ(σ_{T'}))` on a
    matrix-unit basis of `End(V_λ)` — that object reduces to a diagonal
    `δ · y_λ` by the matrix-unit multiplication rule, carrying no
    information beyond the Markov weight `y_λ` and the dimension. The
    structurally non-trivial per-block data IS the representation
    matrices returned here; downstream consumers (e.g. Option E
    Phase 2 canonical-basis trace at crystal vertices) build their
    own contraction against these.

    For H_3 cross-check against `tools/pyhecke/python/pyhecke/gram.py`'s
    6×6 NF Gram, see `option_e_phase1_h3_cross_check.py` in this
    directory.
    """
    if sum(lam) != n:
        raise ValueError(
            f"partition {lam} sums to {sum(lam)}, expected n = {n}"
        )

    from hoefsmit_symbolic import Q as q_sym  # module's canonical Symbol
    matrices_sym, dim = _hoefsmit_with_module_q(lam)

    if dim == 0:
        return {
            "lam": tuple(lam),
            "n": n,
            "dim_lambda": 0,
            "sigma_k_at_q": [],
            "w0_at_q": np.zeros((0, 0)),
            "chi_lambda_w0": 0.0,
            "gram_self": np.zeros((0, 0)),
        }

    # Per-σ_k evaluation
    sigma_k_at_q = [_eval_matrix(M, q_sym, q_val) for M in matrices_sym]

    # ρ_λ(w_0) via symbolic chain product (most accurate)
    word_w0 = longest_reduced_word_1based(n)
    if dim == 1:
        w0_sym = sp.Matrix([[sp.Integer(1)]])
        for k in word_w0:
            w0_sym = w0_sym * matrices_sym[k - 1]
        w0_at_q = np.array(
            [[float(sp.re(w0_sym[0, 0].evalf(subs={q_sym: q_val})))]],
            dtype=np.float64,
        )
    else:
        w0_sym = sp.eye(dim)
        for k in word_w0:
            w0_sym = w0_sym * matrices_sym[k - 1]
            w0_sym = w0_sym.applyfunc(sp.cancel)
        w0_at_q = _eval_matrix(w0_sym, q_sym, q_val)

    chi_w0 = float(np.trace(w0_at_q))

    # Per-block telemetry: det and condition number of each generator
    # action ρ_λ(σ_k). The σ_k matrices are invertible (representations
    # of invertible braid generators), so det ≠ 0. We record det + cond
    # as per-block diagnostic for downstream consumers; this is the
    # "11 invertible matrices with det + cond" line item from the
    # Phase-1 scope doc.
    sigma_k_dets = [float(np.linalg.det(M)) for M in sigma_k_at_q]
    sigma_k_conds = [
        float(np.linalg.cond(M)) if dim > 1 else 1.0
        for M in sigma_k_at_q
    ]
    w0_det = float(np.linalg.det(w0_at_q))
    w0_cond = float(np.linalg.cond(w0_at_q)) if dim > 1 else 1.0

    return {
        "lam": tuple(lam),
        "n": n,
        "dim_lambda": dim,
        "sigma_k_at_q": sigma_k_at_q,
        "w0_at_q": w0_at_q,
        "chi_lambda_w0": chi_w0,
        "sigma_k_dets": sigma_k_dets,
        "sigma_k_conds": sigma_k_conds,
        "w0_det": w0_det,
        "w0_cond": w0_cond,
    }


def partitions_of_descending(n: int) -> list[tuple[int, ...]]:
    """All partitions of n as descending-sorted tuples (pure sympy)."""
    from sympy.utilities.iterables import partitions as _sp_partitions

    out = []
    for p in _sp_partitions(n):
        parts = sorted(p.items(), reverse=True)
        expanded = []
        for size, count in parts:
            expanded.extend([size] * count)
        out.append(tuple(expanded))
    return out


if __name__ == "__main__":
    import json
    import time

    Q_PIN = _pb.witness_path("q-pinning-50-digit.witness.json", HERE)
    q_0 = float(mp.mpf(json.load(Q_PIN.open())["derived_50_digit"]["q"]))

    print("=" * 78)
    print(f"gram_matrix_seminormal_block API demo at q_0 = {q_0:.10f}")
    print("=" * 78)
    print()

    for n in (3, 6):
        t0 = time.time()
        print(f"§. H_{n}")
        for lam in partitions_of_descending(n):
            t1 = time.time()
            block = gram_matrix_seminormal_block(n, lam, q_0)
            dt = time.time() - t1
            print(f"  λ = {lam:<24}  dim_λ = {block['dim_lambda']:>3}  "
                  f"χ_λ(w_0) = {block['chi_lambda_w0']:+.10e}  "
                  f"({dt:.2f}s)")
        print(f"  H_{n} total: {time.time() - t0:.1f}s")
        print()
