---
# qou-ah2l
title: trSummand from seminormalRepFin — the general-n rep is PROVED, so this is small
status: todo
type: task
priority: normal
created_at: 2026-09-04T10:41:57Z
updated_at: 2026-09-04T10:42:37Z
---

Split out of `qou-t5ve` once the corpus-grep established that the general-`n`
seminormal representation is **already proved** (see that bean's 2026-09-04
correction). Scoped accordingly — this is smaller than the "formalise the
seminormal construction" job I had described.

## What exists

* `QOU.SchurWeyl.hoefsmit_seminormal_rep` (`HoefsmitRepGeneral.lean`,
  sorry-free): for every `λ ⊢ N` at real `q ≠ 0` not a root of unity,
  `∃ ρ : Hecke ℝ q q⁻¹ (N-1) →ₐ[ℝ] Matrix (Fin dλ) (Fin dλ) ℝ`, non-scalar
  when `dλ ≥ 2`.
* `SeminormalRep.seminormalRepFin` — the underlying construction, a
  *function*, not an existential.
* `QOU.Archimedean.rhoMixedSigma2_conj_S1` (`qou-t5ve`) — the gauge relating
  the library's square-root-free basis to the orthogonal basis
  `pyhecke_native` returns. **Read this before wiring anything to the Rust
  numbers**: only trace, determinant, spectrum and the relations transfer
  entry-free.

## What is missing

`DescartesMarkovTrace.trSummand` is still free data constrained only by
`tr_eq_sum_summands`. To tie it to the mathematics:

1. Define `chiLambda λ (w : word) : ℝ := Matrix.trace (seminormalRepFin … w)`
   — the character as a function. `hoefsmit_seminormal_rep`'s existential form
   is not directly usable for this; `seminormalRepFin` is.
2. Instantiate `trSummand n i x` from it, with the summand index `i` ranging
   over the `≤ 2`-row partitions of `n` (the SU_q(2) constraint).
3. Discharge `tr_eq_sum_summands` — the Wedderburn decomposition of the trace,
   which is the real content and may already be reachable from
   `HeckeWedderburnGeneral` / `MarkovAssembly` in the same directory.

Step 3 is the one that could still be large. Steps 1–2 are plumbing.

## Do not repeat

Four times in this arc I asserted something was missing and the corpus-grep
found it present: the general-`n` characters (Rust, months old), `S0`
(duplicated outright), the "21 sorries" (zero), and the general-`n` rep
(proved). **Run the six paths against `QOU/SchurWeyl/` — 73 files — before
writing a line of Lean here.**
