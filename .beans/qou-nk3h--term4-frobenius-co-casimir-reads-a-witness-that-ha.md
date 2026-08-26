---
# qou-nk3h
title: term4 Frobenius co-Casimir reads a witness that has NEVER existed — two producers silently fall back to a constant
status: todo
type: task
priority: normal
created_at: 2026-08-26T16:53:01Z
updated_at: 2026-08-26T16:53:40Z
---

Found 2026-08-26 while answering "are the low-isotope dashboard's witnesses
updated?". Not the question that was asked, and worse than the answer.

## The finding

`computations/probe-term4-conventions.witness.json` **has never existed in this
repository**, and **no producer in the tree writes it.**

    git log --oneline --diff-filter=AD --all -- '*probe-term4-conventions*'
    (empty)

Two producers read it, with an identical loader that swallows the failure twice:

    computations/unified_low_isotope_predictor.py:88   _load_sigma_3A
    computations/mass_formula_6term.py:73             _load_sigma_3A_table

        if not path.exists():
            return {}
        try:
            ...
        except Exception:
            return {}

No warning on either path. A third file, `rho_k_h3a_co_casimir.py:4`, cites the
same witness in a source comment as its data source.

## What it costs

In `unified_low_isotope_predictor`, `term4_frobenius` is documented as
*"m_e · Σ_{λ⊢3A} 1/dim_q(λ), per prop:frobenius-codim-universal"* with
*"Coverage: witness covers A ∈ {1..7} exactly"*. With the table empty it takes
its `A >= 8` fallback for **every** isotope, so T4 is the constant
`m_e · 2.05 = 1.0475 MeV` from D to 16O. That is visible in the producer's own
output and nobody had looked:

    sym   A        T1        T4        T5    T6       k>=3   Δshell
    D     2    3.1857    1.0475    0.0000  0.00 -261785.13   0.0435
    T     3    2.1264    1.0475    8.7501  0.00 -340659.01   0.0435
    3He   3    2.5104    1.0475    8.2429  0.00      0.0000  0.0435
    4He   4    0.0000    1.0475   22.5467  0.00      0.0000  0.0435

The docstring describes an algebraic per-3A trace; the code returns a literal.

## Fixed here (the guard), NOT fixed here (the table)

Both loaders now warn on stderr and name this bean; `unified_low_isotope_
predictor` also records `_SIGMA_3A_UNAVAILABLE`, and its `term4_frobenius`
fallback comment says plainly that it is taken for every A. The docstrings that
claimed coverage are corrected.

**The table is deliberately not reconstructed.** `Σ_{λ⊢3A} 1/dim_q(λ)` is
computable — but there are **ten LIVE `dim_q` implementations** under
`computations/` with differing signatures (`phase5/phase5_n8_dim_q_table.py`,
`delta_lambda_empirical_tabulation.dim_q_at_q0`, `term7_chi5_basis.dim_q`,
`chirality_avg_content_atomic.dim_q`, four under `deltalambda/`, ...), so
building it is a **choice among conventions**, not a computation. Picking one
silently is the same failure as the one being fixed. Whoever takes this should
name the implementation and say why.

**Correction to my own first pass, recorded because it is the same error class:**
I initially reported that every `dim_q` was deprecated and concluded the
machinery was gone. That came from reading `head -8` of a grep whose output
happened to sort `_deprecated/` first. Ten live ones exist. Truncated view,
confident conclusion — check the whole listing.

## Also fixed in the same commit (small, same file)

- `import numpy as np` with **zero** `np.` uses, and the witness declaring
  `engine="python+numpy"`. Removed the import; engine is now `python+mpmath`.
- `term4_frobenius` returned a Python float literal `2.05`; now `mp.mpf("2.05")`.
  This is the NO-FLOAT64 discipline at the one site the fix touched — it does
  **not** address the producer's other 70 raw-float64 payload fields, which are
  `qou-syit`.

## Not in scope

Whether `B_pred_MeV = -261780` for deuterium means anything. It does not, but
that is the producer's physics, and the k>=3 tail rather than term 4.
