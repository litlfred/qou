---
# qou-sgd1
title: Re-prove specht_gram_diag + Stage-1 nondegeneracy (LinearOrderedField)
status: completed
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-06T00:00:00Z
updated_at: 2026-10-04T15:23:13Z
---

## Context

`specht_gram_orthogonal` was refuted (see `qou-tup9`). Three true-but-orphaned
lemmas were removed from `QOU/BraidKnot/SpechtIrreducible.lean` to get the
module back to 0 errors: `specht_gram_diag`, `kap_of_clash_eq_zero`,
`sagan_row_col_clash`. Recover from git history (`git log -S specht_gram_diag`).

## What to do

1. **Stage 1 — the cheap win, do this first.** `bilinM` is by construction the
   Euclidean form in the tabloid basis (`bilinM_apply`,
   `bilinM_single_single`). Over a `LinearOrderedField` it is positive definite
   on all of `M^mu`: `<x,x> = sum_d (x d)^2 = 0` forces `x = 0`. So
   `S^mu ⊓ (S^mu)^perp = ⊥` follows with **no Gram theory and no standard
   tableaux at all**. State it as a separate theorem
   `specht_form_nondegenerate_of_linearOrderedField`. This should be short and
   it covers the archimedean evaluation the framework actually uses.

2. **Re-prove `specht_gram_diag`** (`<e_T, e_T> = |C_T|`). True — confirmed by
   enumeration for every `mu ⊢ n`, `n <= 5`. The removed body had an
   application type mismatch after the namespace repair.

3. **Stage 2 — general `CharZero`** (the remaining `sorry`). The bilinear form
   is not definite over ℂ, so Stage 1 does not transfer. Route: the standard
   polytabloids are defined over ℤ, so the Gram matrix `G` has integer entries;
   by Stage 1 over ℚ it is the Gram matrix of a linearly independent set for a
   positive-definite form, so `det G > 0`; a nonzero integer is invertible in
   any characteristic-zero field. Needs standard-basis linear independence plus
   a ℤ→k base-change lemma.

## Do not

Do not restate `specht_gram_orthogonal` in any form. It is false, not hard.



## Summary of Changes

Closed 2026-10-04 in the work-plan reorganisation: the work has landed on main. Evidence: [M] specht gram / nondegeneracy: target decl/file sorry-free on main 2026-10-03; [B] sp00 completed epic lists bricks axiom-clean (#print axioms). Conditional-in-form only on SnIsotypicSpechtSplit, wh
