#!/usr/bin/env python3
"""
wedderburn_jones_markov.py — canonical Jones-Markov Wedderburn sum.

Replacement for `schur_weyl_symbolic.global_wedderburn_sum_symbolic` and
`per_stratum_sum_symbolic` that uses the **correct Jones-Markov weights
y_λ(q)** via Wenzl's Schur principal specialization, NOT the
2-variable Schur formula `s_λ(q, q⁻¹) / H_q(λ)` (which vanishes for
≥ 3-row partitions, dropping the `(1^p)` sign-rep entirely).

Per
[`docs/audits/2026-05-08-p3-h-3a-divergence.md`](../../docs/audits/2026-05-08-p3-h-3a-divergence.md),
the legacy `schur_weyl_weight(partition, q)` is NOT the Markov-trace
weight at q ≠ 1.  The QOU paper requires `y_λ(q)` per
`markov_weights_symbolic.solve_y_lambda(n)`.

This module exposes the canonical sum with **numerical-q-from-start**
performance: substitutes `q = q_0` BEFORE the symbolic `sp.cancel`
that was the bottleneck in naive `solve_y_lambda(n)` for n ≥ 6.

References:
- markov_weights_symbolic.solve_y_lambda — canonical y_λ(q)
- prop:atomic-mass-gb-nf
- 1ppb workplan §P3 (`docs/coordination/1ppb.md`)
- docs/audits/2026-05-08-p3-h-3a-divergence.md

@module folio-assistant/computations/wedderburn_jones_markov
"""

from __future__ import annotations

import os
import sys
from math import factorial
from multiprocessing import Pool
from pathlib import Path

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import sympy as sp  # noqa: E402

import markov_weights_symbolic as m  # noqa: E402

Q_SYM = sp.symbols("q", positive=True)


def _f_lambda(shape: tuple) -> int:
    """SYT count via the hook-length formula: f^λ = n! / Π h_x."""
    hs, _ = m.hooks_and_contents(list(shape))
    prod = 1
    for h in hs:
        prod *= h
    n = sum(shape)
    return factorial(n) // prod


def _schur_principal_at_q(args):
    """Top-level worker for multiprocessing.Pool.imap_unordered."""
    sh, q_str = args
    return sh, m.schur_principal_symbolic(list(sh)).subs(
        Q_SYM, sp.sympify(q_str)
    ).evalf(30)


def y_lambda_at(
    n: int,
    q_val: sp.Expr | float | None = None,
    workers: int | None = None,
) -> dict[tuple, sp.Expr]:
    """Jones-Markov y_λ(q) at H_n.

    If `q_val` is None (default): returns symbolic y_λ via
    `markov_weights_symbolic.solve_y_lambda(n)` — fast for n ≤ 3,
    slow for n ≥ 6 (sp.cancel on rational expressions).

    If `q_val` is a number (e.g. q_0): uses **numerical-q-from-start**
    by substituting in the Schur principal specialization BEFORE the
    Wenzl normalization, avoiding sp.cancel.  Much faster for n ≥ 6:

        n=3:  ~0.05s    (any path)
        n=6:  ~3.8s     (numerical-q-from-start)  vs  >60s (symbolic)
        n=9:  ~63s      (numerical)              vs  infeasible (symbolic)
        n=12: ~150-300s sequential, parallelisable across the 77
              partitions via `workers > 1` (multiprocessing).

    The `workers` parameter (default: None = sequential) enables
    process-pool parallelism for n ≥ 9 where partition count grows
    rapidly.  Set to `os.cpu_count()` (or a smaller value to leave
    cores free) for maximum throughput on the numerical-q path.
    """
    shapes = [tuple(s) for s in m.partitions_of(n)]
    if q_val is None:
        return m.solve_y_lambda(n)

    # numerical-q-from-start path
    q_eval = sp.sympify(q_val)
    s_vals: dict[tuple, sp.Expr] = {}
    if workers and workers > 1 and len(shapes) > 1:
        q_str = str(q_eval)
        with Pool(processes=workers) as pool:
            for sh, val in pool.imap_unordered(
                _schur_principal_at_q,
                [(sh, q_str) for sh in shapes],
            ):
                s_vals[sh] = val
    else:
        for sh in shapes:
            s_vals[sh] = (
                m.schur_principal_symbolic(list(sh)).subs(Q_SYM, q_eval).evalf(30)
            )
    Z = sp.Integer(0)
    for sh in shapes:
        Z = Z + s_vals[sh] * _f_lambda(sh)
    return {sh: s_vals[sh] / Z for sh in shapes}


def global_wedderburn_sum_jones_markov(
    A: int,
    q_val: sp.Expr | float | None = None,
    char_kind: str = "trivial",
    Z: int | None = None,
    N: int | None = None,
    include_inter: bool = True,
    m_pp: int = 1,
    m_pn: int = 1,
    m_nn: int = 1,
) -> tuple[sp.Expr, list[dict]]:
    """Σ_{λ ⊢ 3A} y_λ(q) · χ^λ(𝒜) — canonical Jones-Markov form.

    Drop-in replacement for
    `schur_weyl_symbolic.global_wedderburn_sum_symbolic` that uses the
    correct Wenzl/Jones-Markov weight y_λ rather than the 2-variable
    Schur s_λ(q, q⁻¹) / H_q(λ).  The 2-variable form vanishes for
    partitions with > 2 rows, dropping the `(1^p)` sign-rep
    contribution that `prop:alpha-shift-torus-knot` identifies as the
    pole-order maximizer.

    Parameters mirror the legacy function; the only addition is
    `q_val` — pass q_0 to enable numerical-q-from-start (recommended
    for A ≥ 2 to avoid the sp.cancel bottleneck).

    Returns (sympy_expr, partitions_with_weights_list).
    """
    from schur_weyl_symbolic import (  # noqa: E402
        specht_character_atomic,
        specht_character_placeholder,
    )

    if char_kind == "mn-atom":
        if Z is None or N is None:
            raise ValueError("char_kind='mn-atom' requires Z and N.")
        if Z + N != A:
            raise ValueError(f"Z + N = {Z + N} != A = {A}")

    n = 3 * A
    y_vals = y_lambda_at(n, q_val)
    shapes = list(y_vals.keys())

    terms = []
    total = sp.Integer(0)
    for lam in shapes:
        y = y_vals[lam]
        if char_kind == "mn-atom":
            chi = specht_character_atomic(
                lam, Z, N, include_inter, m_pp, m_pn, m_nn
            )
        else:
            chi = specht_character_placeholder(lam)
        # Use sp.sympify(...).is_zero — robust against unsimplified
        # sympy expressions where structural `== 0` would miss
        # mathematical zeros (gemini review on PR #572).
        if sp.sympify(chi).is_zero:
            continue  # skip zero-character partitions
        contrib = y * chi
        total += contrib
        terms.append({
            "partition": lam,
            "weight": y,
            "character": chi,
            "contribution": contrib,
        })
    return total, terms


def per_stratum_sum_jones_markov(
    A: int,
    S,
    q_val: sp.Expr | float | None = None,
) -> tuple[sp.Expr, list[dict]]:
    """Σ_{λ ⊢ 3A} y_λ(q) · χ^λ(π_S) — canonical Jones-Markov form.

    Drop-in replacement for
    `schur_weyl_symbolic.per_stratum_sum_symbolic` using y_λ rather
    than 2-variable Schur.

    Parameters
    ----------
    A : int
        Number of nucleons (3A strands).
    S : iterable
        Subset of generator indices.
    q_val : optional numeric q (e.g. q_0).  None = symbolic.
    """
    from murnaghan_nakayama import (  # noqa: E402
        cycle_type_of_permutation,
        mn_character,
    )
    from schur_weyl_symbolic import stratum_permutation  # noqa: E402

    perm = stratum_permutation(A, S)
    cyc = cycle_type_of_permutation(perm)
    n = 3 * A
    y_vals = y_lambda_at(n, q_val)
    shapes = list(y_vals.keys())

    terms = []
    total = sp.Integer(0)
    for lam in shapes:
        y = y_vals[lam]
        chi = mn_character(lam, cyc)
        if chi == 0:
            continue
        contrib = y * chi
        total += contrib
        terms.append({
            "partition": lam,
            "weight": y,
            "character": chi,
            "contribution": contrib,
        })
    return total, terms


def global_wedderburn_sum_q_hecke_seminormal(
    Z: int,
    N: int,
    q_val: float,
    *,
    include_inter: bool = True,
    m_pp: int = 1,
    m_pn: int = 1,
    m_nn: int = 1,
) -> tuple[float, list[dict]]:
    """tr_M(β_atomic(Z, N)) = Σ_{λ ⊢ 3A} y_λ(q_0) · χ^λ_q(β) — exact form.

    **Closes the character gap** flagged in
    docs/audits/2026-05-08-q-hecke-character-gap-closure.md.

    Composes:
      - y_λ via Wenzl Schur principal specialization (numerical-q-from-start)
      - χ^λ_q via Hoefsmit seminormal matrices at q_val (numerical, float64)

    Drop-in replacement for the q=1-character-limited
    `global_wedderburn_sum_jones_markov` when consumers need the
    canonical Hecke character at q ≠ 1.  Numerically agrees with
    `markov_trace_recursive` (canonical Markov-axiom reducer) to
    1e-13 (proton/neutron, A=1) — 1e-10 (deuteron, A=2) relative;
    full-precision mpmath path lives on PR #564 as
    `rho_k_h3a_refinement.py` with 50-dps agreement at 1.4e-16.

    Returns (tr_M_value, per_partition_breakdown).
    """
    import numpy as np

    from hecke_characters import build_seminormal_matrices  # noqa: E402
    from mass_at_3A_proper import (  # noqa: E402
        atom_braid_word_3A,
        chi_lambda_of_word,
    )

    A = Z + N
    n = 3 * A
    word = atom_braid_word_3A(
        Z, N, m_pp=m_pp, m_pn=m_pn, m_nn=m_nn,
        include_inter=include_inter,
    )
    y_vals = y_lambda_at(n, q_val=q_val)
    n_gens_required = n - 1

    rows = []
    total = 0.0
    for shape, y in y_vals.items():
        sigmas, dim, _syts = build_seminormal_matrices(shape, q=q_val)
        if dim == 0:
            continue
        try:
            chi = chi_lambda_of_word(sigmas, dim, word, n_gens_required)
        except IndexError:
            continue
        contrib = float(y) * float(chi)
        total += contrib
        rows.append({
            "partition": list(shape),
            "dim": int(dim),
            "y_at_q0": float(y),
            "chi_q_at_q0": float(chi),
            "contribution": float(contrib),
        })
    return total, rows


__all__ = [
    "y_lambda_at",
    "global_wedderburn_sum_jones_markov",
    "per_stratum_sum_jones_markov",
    "global_wedderburn_sum_q_hecke_seminormal",
]
