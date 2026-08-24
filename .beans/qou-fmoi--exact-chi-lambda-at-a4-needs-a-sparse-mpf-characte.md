---
# qou-fmoi
title: Exact chi_lambda at A=4 needs a sparse-mpf character product (dense mpmath is ~571 h)
status: todo
type: task
created_at: 2026-08-24T09:11:25Z
updated_at: 2026-08-24T09:11:25Z
---


## The incompatibility

`su4_1111_markov_trace_probe` (PROBE 2b, the genuine Schur-Weyl [1⁴] A=4
object) has been dead on `main` with

    ValueError: scipy.sparse does not support dtype object

Not a scipy bug and not a probe bug in isolation — the two halves disagree
about precision:

- `mass_at_3A_proper.atom_braid_word_3A` carries **exact `mpf`** offsets by
  default (`allow_float64=False`, an explicit precision gate). Measured on the
  A=4 word: **25 of 47** crossings carry an `mpf` — 22 `(int, mpf)`, 3
  `(mpf, mpf)`.
- `mass_at_3A_proper.chi_lambda_of_word` builds the product in **scipy sparse**
  and returns `float(...)`. It is a float64 routine by construction.

So a precision upgrade upstream silently killed a downstream consumer. Same
mechanism as the mpf-f-string class in `qou-geqa`, one layer up: there the
`TypeError` was in formatting, here it is in the linear algebra.

## Why the obvious fixes do not work

**`float(c)`** makes it exit 0 in 0.01 s and emit entirely plausible numbers.
Banned — AGENTS.md §"PROBES ARE NOT EXEMPT" names "note it as a limitation and
ship" as the wrong move, and this probe's own verdict discipline turns on
whether a scale-free ratio lands at ×2.093.

**`hoefsmit_mpmath.chi_lambda_of_word_mp`** is the correct exact route — dense
mpmath, same accumulation order, already in the corpus. It is unaffordable
here, measured rather than estimated:

| irrep | dim | exact χ cost |
|---|---|---|
| (6,6) — smallest of ten | 132 | **65.7 s** (measured) |
| (5,3,3,1) — largest | 4158 | **~571 h** (cubic scaling) |

One irrep of ten, for one isotope.

## What the conditioning measurement does and does not say

At dim=132, against the 50-dps exact reference, the float64 character agrees to
**15 digits** (rel. err 1.7e-16) — so this word is well conditioned and float64
loses nothing to cancellation *there*.

Two things that is not. It is not permission to ship float64. And it is not a
statement about dim=4158, where the 47-factor product is far denser and was not
tested — testing it requires the exact value, which is the thing that costs
571 h.

## The actual route

Neither cast nor dense mpmath. The seminormal σ_i carry **at most 2 nonzeros
per row** (1×1 and 2×2 blocks), so:

1. **Sparse mpf product** — dict-of-rows, cost bounded by `nnz` per step rather
   than `dim³`; or
2. **Trace-only row propagation** — `tr(ΠM) = Σ_i e_iᵀ (ΠM) e_i`, propagating one
   sparse row vector through the 47 factors. Rough order: 47 × dim × 2 mpf ops
   per row × dim rows ≈ 5e8 for dim=4158 — hours, not centuries, and exact.

Both stay in exact arithmetic. Either would also unblock any other A≥4 consumer
of the exact word, so this is infrastructure rather than a one-probe fix.

## Interim state (this branch)

The probe now **refuses explicitly** rather than dying inside scipy: a guard
`ExactCharacterInfeasible` naming the dim, the cost, the required fix and the
rule. It exits non-zero — correctly, in the same category as
`low_isotope_mass_table` and `qbeta_braid_nf_sdp_offset_probe`. The A=4 [1⁴]
question stays **unanswered**, which is the honest state; it was not previously
answered either, only opaque.
