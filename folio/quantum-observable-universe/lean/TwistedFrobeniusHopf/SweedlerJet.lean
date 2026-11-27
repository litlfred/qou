/-
Copyright (c) 2026 litlfred. All rights reserved.
Released under Apache 2.0 license.
-/
import Mathlib.RingTheory.HopfAlgebra.Basic
import Mathlib.RingTheory.TensorProduct.Basic
import Mathlib.Algebra.RingQuot
import Mathlib.Algebra.FreeAlgebra
import Mathlib.Algebra.TrivSqZeroExt.Basic

/-!
# Sweedler's four-dimensional Hopf algebra as a noncommutative jet

Sweedler's algebra `H₄` over a commutative ring `k` is presented by generators
`g, x` and relations `g² = 1`, `x² = 0`, `x g = -(g x)`. Its comultiplication
is `Δ g = g ⊗ g`, `Δ x = x ⊗ 1 + g ⊗ x`, with `x` a skew-primitive.

This file builds the presentation, the comultiplication and counit, and proves the
bialgebra axioms. In a commutative Hopf algebra over a field of characteristic
zero a square-zero primitive vanishes (`eq_zero_of_primitive_sq_eq_zero`); here
`x² = 0` holds for a nonzero skew-primitive, which is how the noncommutative jet
escapes that obstruction.

## References
- [leitner2026] §3 Lifting and Descent
- M. E. Sweedler, *Hopf Algebras*, Benjamin 1969 (the four-dimensional example).
-/

namespace QOU.LiftingDescent

open TensorProduct
open scoped Pointwise

/-- The two generators of Sweedler's algebra. -/
inductive SweedlerGen
  | g
  | x
  deriving DecidableEq

variable (k : Type*) [CommRing k]

/-- The defining relations `g² = 1`, `x² = 0`, `x g = -(g x)`. -/
inductive SweedlerRel : FreeAlgebra k SweedlerGen → FreeAlgebra k SweedlerGen → Prop
  | g_sq : SweedlerRel (FreeAlgebra.ι k .g * FreeAlgebra.ι k .g) 1
  | x_sq : SweedlerRel (FreeAlgebra.ι k .x * FreeAlgebra.ι k .x) 0
  | anti : SweedlerRel (FreeAlgebra.ι k .x * FreeAlgebra.ι k .g)
      (-(FreeAlgebra.ι k .g * FreeAlgebra.ι k .x))

/-- Sweedler's algebra `H₄ = k⟨g, x⟩ / (g² - 1, x², x g + g x)`.

Port note (Lean v4.35): an `abbrev`, not a `def`; with a `def` synonym instance search no
longer unifies the `Algebra.toModule` path with the `Ring` instance path. -/
abbrev Sweedler : Type _ := RingQuot (SweedlerRel k)

noncomputable instance : Ring (Sweedler k) := RingQuot.instRing _
noncomputable instance : Algebra k (Sweedler k) := RingQuot.instAlgebra _

namespace Sweedler

/-- The quotient map from the free algebra. -/
noncomputable def mk : FreeAlgebra k SweedlerGen →ₐ[k] Sweedler k := RingQuot.mkAlgHom k _

theorem mk_surjective : Function.Surjective (mk k) := RingQuot.mkAlgHom_surjective k _

/-- The group-like generator. -/
noncomputable def G : Sweedler k := mk k (FreeAlgebra.ι k .g)

/-- The skew-primitive generator. -/
noncomputable def X : Sweedler k := mk k (FreeAlgebra.ι k .x)

theorem G_mul_G : G k * G k = 1 := by
  rw [G, ← map_mul, ← map_one (mk k)]
  exact RingQuot.mkAlgHom_rel k (s := SweedlerRel k) SweedlerRel.g_sq

theorem X_mul_X : X k * X k = 0 := by
  rw [X, ← map_mul, ← map_zero (mk k)]
  exact RingQuot.mkAlgHom_rel k (s := SweedlerRel k) SweedlerRel.x_sq

theorem X_mul_G : X k * G k = -(G k * X k) := by
  rw [X, G, ← map_mul, ← map_mul, ← map_neg]
  exact RingQuot.mkAlgHom_rel k (s := SweedlerRel k) SweedlerRel.anti

variable {k}

/-- Two algebra maps out of `H₄` agree if they agree on `G` and `X`. -/
theorem algHom_ext {B : Type*} [Semiring B] [Algebra k B] {f f' : Sweedler k →ₐ[k] B}
    (hg : f (G k) = f' (G k)) (hx : f (X k) = f' (X k)) : f = f' := by
  apply RingQuot.ringQuot_ext' (S := k) (s := SweedlerRel k)
  apply FreeAlgebra.hom_ext
  funext s
  cases s
  · exact hg
  · exact hx

/-- The universal property: elements `a, b` of a `k`-algebra with `a² = 1`, `b² = 0`,
`b a = -(a b)` define an algebra map `H₄ → B`. -/
noncomputable def lift {B : Type*} [Ring B] [Algebra k B] (a b : B)
    (h1 : a * a = 1) (h2 : b * b = 0) (h3 : b * a = -(a * b)) : Sweedler k →ₐ[k] B :=
  RingQuot.liftAlgHom k (s := SweedlerRel k) ⟨FreeAlgebra.lift k (fun s => match s with | .g => a | .x => b),
    fun _ _ h => by
      cases h <;> simp [h1, h2, h3]⟩

section lift
variable {B : Type*} [Ring B] [Algebra k B] (a b : B)
    (h1 : a * a = 1) (h2 : b * b = 0) (h3 : b * a = -(a * b))

@[simp] theorem lift_G : lift a b h1 h2 h3 (G k) = a := by
  exact (RingQuot.liftAlgHom_mkAlgHom_apply _ _ _ _).trans (FreeAlgebra.lift_ι_apply _ _)

@[simp] theorem lift_X : lift a b h1 h2 h3 (X k) = b := by
  exact (RingQuot.liftAlgHom_mkAlgHom_apply _ _ _ _).trans (FreeAlgebra.lift_ι_apply _ _)

end lift

section Hopf

open Algebra.TensorProduct in
theorem comulG_sq (k : Type*) [CommRing k] : (G k ⊗ₜ[k] G k) * (G k ⊗ₜ[k] G k) = 1 := by
  rw [tmul_mul_tmul, G_mul_G]; rfl

open Algebra.TensorProduct in
theorem comulX_sq (k : Type*) [CommRing k] :
    (X k ⊗ₜ[k] (1 : Sweedler k) + G k ⊗ₜ X k) * (X k ⊗ₜ[k] (1 : Sweedler k) + G k ⊗ₜ X k) = 0 := by
  simp only [add_mul, mul_add, tmul_mul_tmul, X_mul_X, G_mul_G, X_mul_G, mul_one, one_mul,
    zero_tmul, tmul_zero, zero_add, add_zero, neg_tmul]
  abel

open Algebra.TensorProduct in
theorem comul_anti (k : Type*) [CommRing k] :
    (X k ⊗ₜ[k] (1 : Sweedler k) + G k ⊗ₜ X k) * (G k ⊗ₜ[k] G k) =
      -((G k ⊗ₜ[k] G k) * (X k ⊗ₜ[k] (1 : Sweedler k) + G k ⊗ₜ X k)) := by
  simp only [add_mul, mul_add, tmul_mul_tmul, G_mul_G, X_mul_G, mul_one, one_mul, neg_tmul,
    tmul_neg]
  abel

/-- The comultiplication `Δ G = G ⊗ G`, `Δ X = X ⊗ 1 + G ⊗ X`. -/
noncomputable def comul : Sweedler k →ₐ[k] Sweedler k ⊗[k] Sweedler k :=
  lift (B := Sweedler k ⊗[k] Sweedler k) (G k ⊗ₜ[k] G k) (X k ⊗ₜ[k] 1 + G k ⊗ₜ[k] X k)
    (comulG_sq k) (comulX_sq k) (comul_anti k)

/-- The counit `ε G = 1`, `ε X = 0`. -/
noncomputable def counit : Sweedler k →ₐ[k] k :=
  lift (1 : k) 0 (by simp) (by simp) (by simp)

@[simp] theorem comul_G : comul (G k) = G k ⊗ₜ[k] G k := by simp [comul]
@[simp] theorem comul_X : comul (X k) = X k ⊗ₜ[k] 1 + G k ⊗ₜ[k] X k := by simp [comul]
@[simp] theorem counit_G : counit (G k) = 1 := by simp [counit]
@[simp] theorem counit_X : counit (X k) = 0 := by simp [counit]

/-- **Sweedler's algebra is a bialgebra.** Coassociativity and both counit laws are
checked on the generators; `algHom_ext` extends them. -/
noncomputable instance instBialgebra : Bialgebra k (Sweedler k) :=
  Bialgebra.ofAlgHom comul counit
    (algHom_ext (by simp) (by simp [tmul_add, add_tmul, add_assoc, Algebra.TensorProduct.one_def]))
    (algHom_ext (by simp) (by simp))
    (algHom_ext (by simp) (by simp))

@[simp] theorem coalgebra_comul_G :
    CoalgebraStruct.comul (R := k) (G k) = G k ⊗ₜ[k] G k := comul_G
@[simp] theorem coalgebra_comul_X :
    CoalgebraStruct.comul (R := k) (X k) = X k ⊗ₜ[k] 1 + G k ⊗ₜ[k] X k := comul_X
@[simp] theorem coalgebra_counit_G : CoalgebraStruct.counit (R := k) (G k) = 1 := counit_G
@[simp] theorem coalgebra_counit_X : CoalgebraStruct.counit (R := k) (X k) = 0 := counit_X

end Hopf

section Span

variable (k)

/-- The spanning set `{1, G, X, G X}`. -/
def basisSet : Set (Sweedler k) := {1, G k, X k, G k * X k}

theorem G_mul_GX : G k * (G k * X k) = X k := by rw [← mul_assoc, G_mul_G, one_mul]
theorem X_mul_GX : X k * (G k * X k) = 0 := by
  rw [← mul_assoc, X_mul_G, neg_mul, mul_assoc, X_mul_X, mul_zero, neg_zero]
theorem GX_mul_G : G k * X k * G k = -X k := by
  rw [mul_assoc, X_mul_G, mul_neg, ← mul_assoc, G_mul_G, one_mul]
theorem GX_mul_X : G k * X k * X k = 0 := by rw [mul_assoc, X_mul_X, mul_zero]
theorem GX_mul_GX : G k * X k * (G k * X k) = 0 := by rw [mul_assoc, X_mul_GX, mul_zero]

theorem basisSet_mul_subset :
    (basisSet k * basisSet k : Set (Sweedler k)) ⊆ (Submodule.span k (basisSet k) : Set (Sweedler k)) := by
  rintro _ ⟨a, ha, b, hb, rfl⟩
  have h1 : (1 : Sweedler k) ∈ Submodule.span k (basisSet k) := Submodule.subset_span (by simp [basisSet])
  have hG : G k ∈ Submodule.span k (basisSet k) := Submodule.subset_span (by simp [basisSet])
  have hX : X k ∈ Submodule.span k (basisSet k) := Submodule.subset_span (by simp [basisSet])
  have hGX : G k * X k ∈ Submodule.span k (basisSet k) :=
    Submodule.subset_span (by simp [basisSet])
  simp only [basisSet, Set.mem_insert_iff, Set.mem_singleton_iff] at ha hb
  rcases ha with rfl | rfl | rfl | rfl <;> rcases hb with rfl | rfl | rfl | rfl <;>
    simp only [SetLike.mem_coe, one_mul, mul_one, G_mul_G, X_mul_X, X_mul_G, G_mul_GX, X_mul_GX,
      GX_mul_G, GX_mul_X, GX_mul_GX, Submodule.neg_mem_iff, Submodule.zero_mem, h1, hG, hX, hGX]

theorem span_basisSet : Submodule.span k (basisSet k) = ⊤ := by
  have hmul : ∀ a b, a ∈ Submodule.span k (basisSet k) → b ∈ Submodule.span k (basisSet k) →
      a * b ∈ Submodule.span k (basisSet k) := by
    intro a b ha hb
    have : a * b ∈ Submodule.span k (basisSet k) * Submodule.span k (basisSet k) :=
      Submodule.mul_mem_mul ha hb
    rw [Submodule.span_mul_span] at this
    exact (Submodule.span_le.mpr (basisSet_mul_subset k)) this
  refine eq_top_iff.mpr fun a _ => ?_
  obtain ⟨a, rfl⟩ := mk_surjective k a
  clear * - hmul
  induction a using FreeAlgebra.induction with
  | grade0 r =>
    rw [AlgHom.commutes, Algebra.algebraMap_eq_smul_one]
    exact Submodule.smul_mem _ _ (Submodule.subset_span (by simp [basisSet]))
  | grade1 s =>
    cases s
    · exact Submodule.subset_span (by simp [basisSet, G, mk])
    · exact Submodule.subset_span (by simp [basisSet, X, mk])
  | mul a b ha hb => rw [map_mul]; exact hmul _ _ ha hb
  | add a b ha hb => rw [map_add]; exact Submodule.add_mem _ ha hb

end Span

section Antipode

variable (k)

/-- The antipode as an algebra map to the opposite algebra:
`S G = G`, `S X = -(G X)`. -/
noncomputable def antipodeOp : Sweedler k →ₐ[k] (Sweedler k)ᵐᵒᵖ :=
  lift (B := (Sweedler k)ᵐᵒᵖ) (MulOpposite.op (G k)) (MulOpposite.op (-(G k * X k)))
    (by rw [← MulOpposite.op_mul, G_mul_G, MulOpposite.op_one])
    (by rw [← MulOpposite.op_mul, neg_mul_neg, mul_assoc, X_mul_GX, mul_zero,
          MulOpposite.op_zero])
    (by rw [← MulOpposite.op_mul, ← MulOpposite.op_mul, ← MulOpposite.op_neg, mul_neg,
          G_mul_GX, neg_mul, GX_mul_G, neg_neg])

/-- The antipode `S : H₄ → H₄`, a `k`-linear anti-algebra map. -/
noncomputable def antipode : Sweedler k →ₗ[k] Sweedler k :=
  (MulOpposite.opLinearEquiv k).symm.toLinearMap ∘ₗ (antipodeOp k).toLinearMap

theorem antipode_mul (a b : Sweedler k) : antipode k (a * b) = antipode k b * antipode k a := by
  simp [antipode]

@[simp] theorem antipode_one : antipode k 1 = 1 := by simp [antipode]
@[simp] theorem antipode_G : antipode k (G k) = G k := by simp [antipode, antipodeOp]
@[simp] theorem antipode_X : antipode k (X k) = -(G k * X k) := by
  simp [antipode, antipodeOp]
@[simp] theorem antipode_GX : antipode k (G k * X k) = X k := by
  rw [antipode_mul, antipode_X, antipode_G, neg_mul, GX_mul_G, neg_neg]

/-- **Sweedler's algebra is a Hopf algebra.** The antipode axioms are linear, so they are
checked on the spanning set `{1, G, X, G X}` (`span_basisSet`). -/
noncomputable instance instHopfAlgebra : HopfAlgebra k (Sweedler k) where
  antipode := antipode k
  mul_antipode_rTensor_comul := by
    refine LinearMap.ext_on (span_basisSet k) ?_
    rintro a ha
    simp only [basisSet, Set.mem_insert_iff, Set.mem_singleton_iff] at ha
    rcases ha with rfl | rfl | rfl | rfl
    · simp [Algebra.TensorProduct.one_def]
    · simp [G_mul_G]
    · simp
    · simp [Algebra.TensorProduct.tmul_mul_tmul, mul_add, G_mul_G, X_mul_G]
  mul_antipode_lTensor_comul := by
    refine LinearMap.ext_on (span_basisSet k) ?_
    rintro a ha
    simp only [basisSet, Set.mem_insert_iff, Set.mem_singleton_iff] at ha
    rcases ha with rfl | rfl | rfl | rfl
    · simp [Algebra.TensorProduct.one_def]
    · simp [G_mul_G]
    · simp [G_mul_GX]
    · simp [Algebra.TensorProduct.tmul_mul_tmul, mul_add, G_mul_G, GX_mul_G]

end Antipode

section Jet

/-! ### Sweedler's algebra inside a square-zero (jet) extension

Let `A` be a `k`-algebra and `M` an `A`-bimodule, and form the square-zero extension
`A ⋉ M = TrivSqZeroExt A M`, the noncommutative first-order jet. An involution `g ∈ A`
and an element `m ∈ M` with `m · g = -(g · m)` give elements `inl g`, `inr m` satisfying
Sweedler's relations, hence an algebra map `H₄ → A ⋉ M`. Its composite with the
retraction `fst : A ⋉ M → A` kills `X`: the differential part is exactly what the
retraction forgets. -/

variable {A M : Type*} [Ring A] [Algebra k A] [AddCommGroup M] [Module k M] [Module A M]
  [Module Aᵐᵒᵖ M] [SMulCommClass A Aᵐᵒᵖ M] [IsScalarTower k A M] [IsScalarTower k Aᵐᵒᵖ M]

/-- The map `H₄ → A ⋉ M`, `G ↦ inl g`, `X ↦ inr m`. -/
noncomputable def toJet (g : A) (m : M) (hg : g * g = 1)
    (hm : MulOpposite.op g • m = -(g • m)) : Sweedler k →ₐ[k] TrivSqZeroExt A M :=
  lift (TrivSqZeroExt.inl g) (TrivSqZeroExt.inr m)
    (by rw [← TrivSqZeroExt.inl_mul, hg, TrivSqZeroExt.inl_one])
    (TrivSqZeroExt.inr_mul_inr A m m)
    (by
      rw [TrivSqZeroExt.inr_mul_inl, TrivSqZeroExt.inl_mul_inr, hm, TrivSqZeroExt.inr_neg])

theorem toJet_G (g : A) (m : M) (hg : g * g = 1) (hm : MulOpposite.op g • m = -(g • m)) :
    toJet g m hg hm (G k) = TrivSqZeroExt.inl g := lift_G ..

theorem toJet_X (g : A) (m : M) (hg : g * g = 1) (hm : MulOpposite.op g • m = -(g • m)) :
    toJet g m hg hm (X k) = TrivSqZeroExt.inr m := lift_X ..

/-- The retraction `fst` sends the image of `X` to `0` and the image of `G` to `g`. -/
theorem fst_toJet_X (g : A) (m : M) (hg : g * g = 1) (hm : MulOpposite.op g • m = -(g • m)) :
    (toJet g m hg hm (X k)).fst = 0 := by
  rw [toJet_X, TrivSqZeroExt.fst_inr]

end Jet

end Sweedler

end QOU.LiftingDescent
