---
# qou-dr1c
title: division-ring collapse for k[S_n] (residual item 1 of sn_isotypic_specht_split)
status: completed
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-10T03:55:00Z
updated_at: 2026-10-04T15:12:22Z
---

Residual item 1 from PR #4876: prove the Wedderburn division rings of `k[S_n]`
collapse, `𝔇 i ≃ R`, for a characteristic-zero field.

Scoped 2026-08-10 —
`docs/audits/2026-08-10-sn-division-ring-collapse-scoping.md`. The item is
cheaper than the residual list implies, and less independent of item 2.

Already owned, sorry-free (verified by `#print axioms`):
- `SpechtIrreducible.specht_isSimple` — S^μ simple over an ARBITRARY char-0
  field, which is the absolute-irreducibility input, not just the ℚ/ℂ case.
- `SpechtBaseChange` — Specht data defined over ℤ functorially; span transfer.

Genuinely remaining:
1. tensor comparison `S^μ_k ⊗_k K ≅ S^μ_K` as K[S_n]-modules;
2. bijectivity of `Module.End.baseChangeHom` for f.d. modules — Mathlib has
   the algebra hom only, no bijectivity lemma; this is the load-bearing step;
3. linkage `𝔇 i ≃ End(S_i)ᵒᵖ` from Wedderburn's existential — shared with
   items 2 and 3, so those three are coupled, not separable.

Preferred route: build `k[S_n] ≃ₐ[k] ∏_λ Matrix (d_λ) k` directly from the
Specht modules, which never introduces the opaque `𝔇 i` and folds items 1-3
into one construction.

Mathlib has nothing upstream (all 6990 modules scanned): 0 for `Specht`,
`AbsolutelyIrreducible`, `SchurIndex`, `numSYT`.

## 2026-08-10 — remaining item 2 landed (the module-level rung)

`QOU.MathlibExt.EndBaseChange` proves
`A ⊗[R] End R M ≃ₐ[R] End A (A ⊗[R] M)` for finite free `M`, sorry-free
(`[propext, Classical.choice, Quot.sound]` on all three declarations), with
`endBaseChangeEquiv_tmul` identifying it with the canonical map
`a ⊗ₜ f ↦ a • f.baseChange A` so it is wireable rather than a bare existence
claim. Built through matrices (`toMatrixAlgEquiv` / `matrixEquivTensor`), so
every step is an existing Mathlib equivalence.

Still open for item 1, in order:
- the EQUIVARIANT version `K ⊗_k End_{k[G]}(V) ≅ End_{K[G]}(K ⊗_k V)`. Does
  NOT follow formally from the module-level rung: it needs that G-invariants
  commute with the base change. For finite G in char 0 the averaging idempotent
  should give it, since extension of scalars preserves the image of an
  idempotent. This is the next concrete step.
- the tensor comparison `S^mu_k ⊗_k K ≅ S^mu_K`;
- the linkage `D i ≃ End(S_i)^op`, shared with residual items 2 and 3.

## 2026-08-10 (later) — second rung: invariants cross the base change

`QOU.MathlibExt.IdempotentBaseChange` proves
`A ⊗[R] range e ≃ₗ[A] range (e.baseChange A)` for idempotent `e`, sorry-free.
No finiteness, freeness or flatness hypothesis: the argument is purely formal
(`e` splits as `subtype ∘ₗ proj`; base change is functorial; a split injection
stays one).

This is the step that carries G-invariants across the base change, since for
finite G in char 0 the equivariant endomorphisms are the image of the averaging
idempotent on `End_k V`.

Remaining for the EQUIVARIANT statement, and hence for item 1:
- identify `range (averaging idempotent) = End_{k[G]}(V)`;
- show that under `EndBaseChange.endBaseChangeEquiv` the averaging idempotent
  for V corresponds to the averaging idempotent for K ⊗_k V. This is the
  fiddly one -- it needs the representation base change to interact correctly
  with the conjugation action.
Then the two rungs compose to give the equivariant iso.

Still open beyond that: the tensor comparison `S^mu_k ⊗_k K ≅ S^mu_K`, and the
linkage `D i ≃ End(S_i)^op` shared with residual items 2 and 3.



## Summary of Changes

Closed 2026-10-04 in the work-plan reorganisation: the work has landed on main. Evidence: [M] division-ring collapse (sn split done): target decl/file sorry-free on main 2026-10-03; [B] sp00 completed epic lists bricks axiom-clean (#print axioms). Conditional-in-form only on SnIsotypicSpec
