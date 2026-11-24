import Mathlib.RingTheory.TensorProduct.Basic
import Mathlib.LinearAlgebra.TensorProduct.Tower

/-!
# QOU.MathlibExt.IdempotentBaseChange — base change preserves the image of an idempotent

For an idempotent `e : Module.End R M` and an `R`-algebra `A`,

`A ⊗[R] (LinearMap.range e) ≃ₗ[A] LinearMap.range (e.baseChange A)`.

No finiteness, freeness, or flatness hypothesis is needed: the image of an
idempotent is a direct summand, and the argument below is purely formal —
`e` splits as `subtype ∘ₗ proj`, base change is functorial, and a split
injection stays a split injection.

## Why this file exists

It is the second rung toward the `k[S_n]` division-ring collapse, residual item
1 of `SnWedderburnPartitionBridge.sn_isotypic_specht_split`, scoped in
[`docs/audits/2026-08-10-sn-division-ring-collapse-scoping.md`](../../../../../docs/audits/2026-08-10-sn-division-ring-collapse-scoping.md)
(bean `qou-dr1c`).

The collapse needs the *equivariant* base-change statement
`K ⊗_k End_{k[G]}(V) ≅ End_{K[G]}(K ⊗_k V)`, which does not follow from the
module-level `A ⊗[R] End R M ≃ End A (A ⊗[R] M)` of
[`EndBaseChange`](EndBaseChange.lean) alone — it additionally needs `G`-invariants
to commute with the base change. For a finite group in characteristic zero the
invariants are the image of the averaging idempotent
`f ↦ |G|⁻¹ • Σ_σ ρ σ ∘ₗ f ∘ₗ ρ σ⁻¹` on `End_k V`, so *this* file supplies the
step that carries invariants across.

**What is still missing** for the equivariant statement, and hence for item 1:

1. the identification `range (averaging idempotent) = End_{k[G]}(V)`;
2. the compatibility — that under `EndBaseChange.endBaseChangeEquiv` the
   averaging idempotent for `V` corresponds to the averaging idempotent for
   `K ⊗_k V`.

Neither is proved here. This file is a rung, not the item.

## Construction

`e` idempotent splits through its image: with `proj e : M →ₗ[R] range e` the
corestriction and `(range e).subtype` the inclusion,

* `subtype ∘ₗ proj e = e` (definitionally),
* `proj e ∘ₗ subtype = id` (needs idempotence),
* `e ∘ₗ subtype = subtype` (needs idempotence).

Applying `LinearMap.baseChange` — which preserves composition and the identity —
carries all three to `A`, making `subtype.baseChange A` injective with image
`range (e.baseChange A)`.
-/

open TensorProduct

namespace QOU.MathlibExt

variable {R A M : Type} [CommRing R] [CommRing A] [Algebra R A]
  [AddCommGroup M] [Module R M]

/-- Corestriction of an endomorphism to its own image. -/
noncomputable def proj (e : Module.End R M) : M →ₗ[R] (LinearMap.range e) :=
  e.codRestrict (LinearMap.range e) (fun x => ⟨x, rfl⟩)

/-- An idempotent acts as the identity on its image. -/
theorem eq_self_of_mem_range {e : Module.End R M} (he : e ∘ₗ e = e)
    {y : M} (hy : y ∈ LinearMap.range e) : e y = y := by
  obtain ⟨x, hx⟩ := hy
  rw [← hx]
  exact LinearMap.congr_fun he x

theorem proj_comp_subtype (e : Module.End R M) (he : e ∘ₗ e = e) :
    proj e ∘ₗ (LinearMap.range e).subtype = LinearMap.id := by
  ext y; exact eq_self_of_mem_range he y.2

theorem comp_subtype (e : Module.End R M) (he : e ∘ₗ e = e) :
    e ∘ₗ (LinearMap.range e).subtype = (LinearMap.range e).subtype := by
  ext y; exact eq_self_of_mem_range he y.2

theorem baseChange_proj_comp_subtype (e : Module.End R M) (he : e ∘ₗ e = e) :
    ((proj e).baseChange A) ∘ₗ (((LinearMap.range e).subtype).baseChange A)
      = LinearMap.id := by
  rw [← LinearMap.baseChange_comp, proj_comp_subtype e he, LinearMap.baseChange_id]

theorem baseChange_subtype_comp_proj (e : Module.End R M) :
    (((LinearMap.range e).subtype).baseChange A) ∘ₗ ((proj e).baseChange A)
      = e.baseChange A := by
  rw [← LinearMap.baseChange_comp]; rfl

theorem baseChange_comp_subtype (e : Module.End R M) (he : e ∘ₗ e = e) :
    (e.baseChange A) ∘ₗ (((LinearMap.range e).subtype).baseChange A)
      = ((LinearMap.range e).subtype).baseChange A := by
  rw [← LinearMap.baseChange_comp, comp_subtype e he]

theorem baseChange_subtype_injective (e : Module.End R M) (he : e ∘ₗ e = e) :
    Function.Injective (((LinearMap.range e).subtype).baseChange A) :=
  Function.LeftInverse.injective (g := ((proj e).baseChange A))
    (fun x => by
      rw [← LinearMap.comp_apply, baseChange_proj_comp_subtype (A := A) e he,
        LinearMap.id_apply])

theorem range_baseChange_subtype (e : Module.End R M) (he : e ∘ₗ e = e) :
    LinearMap.range (((LinearMap.range e).subtype).baseChange A)
      = LinearMap.range (e.baseChange (A := A)) := by
  apply le_antisymm
  · rintro _ ⟨z, rfl⟩
    exact ⟨((LinearMap.range e).subtype).baseChange A z, by
      rw [← LinearMap.comp_apply, baseChange_comp_subtype e he]⟩
  · rintro _ ⟨z, rfl⟩
    exact ⟨(proj e).baseChange A z, by
      rw [← LinearMap.comp_apply, baseChange_subtype_comp_proj]⟩

/-- **Base change preserves the image of an idempotent.** For idempotent `e`,
extension of scalars along `R → A` carries `range e` to `range (e.baseChange A)`.
No finiteness or freeness hypothesis is required. -/
noncomputable def rangeBaseChangeEquiv (e : Module.End R M) (he : e ∘ₗ e = e) :
    A ⊗[R] (LinearMap.range e) ≃ₗ[A] LinearMap.range (e.baseChange (A := A)) :=
  (LinearEquiv.ofInjective _ (baseChange_subtype_injective (A := A) e he)).trans
    (LinearEquiv.ofEq _ _ (range_baseChange_subtype (A := A) e he))

end QOU.MathlibExt
