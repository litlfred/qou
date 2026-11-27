/-
Copyright (c) 2026 litlfred. All rights reserved.
Released under Apache 2.0 license.
-/
import Mathlib.Algebra.TrivSqZeroExt
import Mathlib.RingTheory.TensorProduct.Basic

/-!
# The noncommutative first-order jet and the skew-primitive escape

For a noncommutative `A`, `ker (m : A ⊗ A → A)` is a sub-bimodule but not an ideal, so
`(A ⊗ A)/I²` is not defined. The first-order jet is instead the square-zero extension
`A ⋉ M` of `A` by a bimodule `M` (for the universal one, `M = Ω¹_u(A) = ker m`). In Mathlib
this is `TrivSqZeroExt A M`.

1. **Splitting** (`ncJet_retract_section`): `a ↦ (a, 0)` and `(a, ω) ↦ a` are ring maps with
   `r ∘ ℓ = id`, and every `(0, ω)` squares to zero (`ncJet_inr_sq`).
2. **The commutative obstruction used primitives.** A square-zero *primitive* vanishes in
   characteristic zero for any ring (`QOU.LiftingDescent.eq_zero_of_primitive_sq_eq_zero`
   already takes `[Ring B]`). A square-zero **skew-primitive** need not:
   if `g² = 1`, `g x = − x g` and `x² = 0`, then `Δx := x ⊗ 1 + g ⊗ x` satisfies
   `Δx · Δx = 0 = Δ(x²)` (`skewPrimitive_sq`). This is the relation of Sweedler's
   four-dimensional Hopf algebra.
3. **The universal differential of an involution anticommutes with it**
   (`involution_anticommutes_d`): if `g² = 1` then `g·dg + dg·g = 0`, with `dg = 1 ⊗ g − g ⊗ 1`
   and the bimodule actions `a·ω = (a ⊗ 1) ω`, `ω·a = ω (1 ⊗ a)`.

So for `A = k[ℤ/2]` the jet `A ⋉ Ω¹_u(A)` has the presentation `g² = 1`, `ω g = −g ω`,
`ω² = 0` of Sweedler's Hopf algebra, in which `ℓ` and `r` are Hopf maps. That identification
and the Hopf axioms of Sweedler's algebra are cited, not proved here.

No `sorry`, no axiom beyond Lean's three.

## References
- [leitner2026] §3 Lifting and Descent
-/

namespace QOU.LiftingDescent

open TensorProduct

section Split

variable (A M : Type*) [Ring A] [AddCommGroup M] [Module A M] [Module Aᵐᵒᵖ M]

/-- **The noncommutative jet splits**: `fst ∘ inl = id`. -/
theorem ncJet_retract_section (a : A) :
    (TrivSqZeroExt.inlHom A M a).fst = a := TrivSqZeroExt.fst_inl M a

/-- The section is multiplicative. -/
theorem ncJet_section_mul (a b : A) :
    TrivSqZeroExt.inlHom A M (a * b) =
      TrivSqZeroExt.inlHom A M a * TrivSqZeroExt.inlHom A M b := map_mul _ a b

/-- The retraction is multiplicative. -/
theorem ncJet_retract_mul (x y : TrivSqZeroExt A M) : (x * y).fst = x.fst * y.fst :=
  TrivSqZeroExt.fst_mul x y

/-- The differential part is square-zero. -/
theorem ncJet_inr_sq (ω : M) :
    (TrivSqZeroExt.inr ω : TrivSqZeroExt A M) * TrivSqZeroExt.inr ω = 0 :=
  TrivSqZeroExt.inr_mul_inr A ω ω

end Split

section Skew

variable {k B : Type*} [CommRing k] [Ring B] [Algebra k B]

/-- **A square-zero skew-primitive is consistent**: with `g x = − x g` and `x² = 0`,
`(x ⊗ 1 + g ⊗ x)² = 0`. -/
theorem skewPrimitive_sq (x g : B) (hanti : g * x = -(x * g)) (hx : x * x = 0) :
    (x ⊗ₜ[k] (1 : B) + g ⊗ₜ x) * (x ⊗ₜ[k] (1 : B) + g ⊗ₜ x) = 0 := by
  simp only [add_mul, mul_add, Algebra.TensorProduct.tmul_mul_tmul, mul_one, one_mul, hx,
    TensorProduct.zero_tmul, TensorProduct.tmul_zero, zero_add, add_zero, hanti,
    TensorProduct.neg_tmul]
  abel

end Skew

section Involution

variable {k A : Type*} [CommRing k] [Ring A] [Algebra k A]

/-- **`dg` anticommutes with an involution `g`**: `(g ⊗ 1)·dg + dg·(1 ⊗ g) = 0`
for `dg = 1 ⊗ g − g ⊗ 1`. -/
theorem involution_anticommutes_d (g : A) (hg : g * g = 1) :
    (g ⊗ₜ[k] (1 : A)) * ((1 : A) ⊗ₜ g - g ⊗ₜ 1) + ((1 : A) ⊗ₜ g - g ⊗ₜ 1) * ((1 : A) ⊗ₜ[k] g) =
      0 := by
  simp only [mul_sub, sub_mul, Algebra.TensorProduct.tmul_mul_tmul, mul_one, one_mul, hg]
  abel

end Involution

end QOU.LiftingDescent
