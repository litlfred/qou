"""Shared utilities for the atomic-braid mass-table family of scripts.

Per Gemini PR #548 medium-priority feedback (consolidate `t4_raw`,
`t6_canonical_MeV` previously duplicated between
`atomic_braid_mass_table.py` and `atomic_braid_mass_table_modes_sweep.py`).

All routines preserve the 50-dps precision floor set by the caller's
`mp.mp.dps = 50`; computations use mpmath end-to-end (no SymPy →
mpmath casts).

Dimensionality conventions:
  * Hecke-unit terms (T1, T2, T3, T4) are returned in cat units —
    they get scaled by E_0 (MeV/cat-unit) at the assembly site.
  * T6 is returned in MeV directly; **do not** multiply by E_0 again
    at the assembly site.
"""
from __future__ import annotations

import json
from pathlib import Path

import mpmath as mp

from schur_weyl_symbolic import partitions_of, hook_lengths

HERE = Path(__file__).parent


def t4_raw(A: int, q0_mp: mp.mpf) -> mp.mpf:
    """Term 4 in cat units (without `m_e` scaling): τ(C_dim_q).

    Returns Σ_{λ ⊢ 3A} 1/dim_q(λ) at q = q0_mp.  Caller scales by
    `m_e_hecke` to get the full Term 4 contribution.

    All arithmetic in mpmath; q-factorial computed by direct product
    `[n]_q! = ∏_{k=1..n} (q^k − q^{−k}) / (q − q^{−1})` to preserve
    precision.
    """
    if A < 1:
        return mp.mpf(0)
    n = 3 * A
    denom = q0_mp - 1 / q0_mp
    nfac_val = mp.mpf(1)
    for k in range(1, n + 1):
        nfac_val *= (q0_mp ** k - 1 / q0_mp ** k) / denom
    total = mp.mpf(0)
    for lam in partitions_of(n):
        dim_q = nfac_val
        for h in hook_lengths(lam):
            qh = (q0_mp ** h - 1 / q0_mp ** h) / denom
            dim_q = dim_q / qh
        total += 1 / dim_q
    return total


def t6_canonical_MeV(A: int) -> mp.mpf:
    """**Diagnostic-only — returns 0 by design.**

    The narrative six-term mass formula
    (see `six-term-mass-formula-complete.md`) decomposes the
    Markov trace `|tr_M|` into six conceptual pieces.  By
    Mittag-Leffler complementarity the meromorphic lift
    `tr_M(u²)` splits as

        tr_M(u²) = entire(u) + pp_at_zero(u) + pp_at_roots(u),

    where `pp_at_roots(u)` is the cyclotomic principal-part sum
    that the narrative names **Term 6**.  All three pieces sum to
    `|tr_M|` exactly — they are *complementary*, not
    independently additive.

    The recursive Markov-trace evaluator (`markov_trace_recursive.py`)
    returns the full `|tr_M|`, which therefore **already includes**
    the cyclotomic contribution.  Adding `pp_at_roots(u₀)` again as
    a separate "T6" term would *double-count* the residue piece.

    Status (resolved 2026-05-08, see AUDIT-DEEP-2026-05.md §3.3a):

    * **Option A confirmed:** the mass formula is
      `M(K) = ρ_K · m_e · |tr_M(K)|`, where `ρ_K` is the
      categorical density derived to ≤ 0.1 % residual on
      D / T / ³He via the constituent-mass leading-order ansatz
      (see `rho-k-scaling-structure.witness.json` and
      `markov_trace_axiomatic_multi_atom.py:111`).
    * **Option C provides the rigorous justification:** by the
      Mittag-Leffler complementarity above, T6 is *not* an
      independent additive correction — it is one of three pieces
      of the same `|tr_M|`.

    The canonical script `term6_residues_at_roots.py` and its
    witness `term6-residues-at-roots.witness.json` retain a
    **diagnostic** role (Yekutieli pole structure, partial-fraction
    split, falsifiability checks) — but their output is *not* an
    additive term in the mass-table assembly.

    This function is preserved at the API level for backward
    compatibility but always returns 0.  Returning 0 is now
    *correct by design*, not a bug or a missing-witness fallback.

    Ref: [manuscript] §Mass formula via rho_K, AUDIT-DEEP-2026-05.md §3.3a.
    """
    return mp.mpf(0)
