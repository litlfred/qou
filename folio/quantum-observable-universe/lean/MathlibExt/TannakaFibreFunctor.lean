/-
Copyright (c) 2026 litlfred. All rights reserved.
Released under Apache 2.0 license.
-/
import MathlibExt.TannakaCoendOneObject
import Mathlib.CategoryTheory.Monoidal.Category
import Mathlib.Algebra.Category.ModuleCat.Basic
import Mathlib.LinearAlgebra.Matrix.ToLin

/-!
# The one-object coend of a fibre functor

Let `C` be a monoidal category, `V : C` an object, and `τ : C ⥤ ModuleCat R` a functor whose
values on the tensor powers `V^{⊗m}` are free, with chosen bases indexed by words
`Fin m → n`. Every morphism `f : V^{⊗a} ⟶ V^{⊗b}` gives the matrix of `τ f`.
`fibreData` collects all of them as `IntertwinerData`, so `Coend (fibreData …)` is the
coend of `τ` restricted to the full subcategory on the tensor powers of `V`, and it is a
bialgebra by `MathlibExt/TannakaCoendOneObject.lean`.

`coaction_natural` is the defining property of a coend: the coaction
`b_w ↦ ∑ v, b_v ⊗ u^{⊗m}_{v w}` on each `τ (V^{⊗m})` commutes with `τ f` for every `f`.
It is proved from the intertwining relations; nothing is assumed.

**Scope.** The bialgebra theorem and naturality hold for every choice of bases. The
monoidal reading, i.e. that the coaction on `τ (V ⊗ W)` is the tensor product of the
coactions, needs the bases of `τ (V^{⊗m})` to be the product bases through a monoidal
structure on `τ`. That compatibility is not stated here.
-/

set_option linter.unusedSectionVars false

namespace QOU.Coproduct

open CategoryTheory MonoidalCategory TensorProduct Module

noncomputable section

universe v u

variable {C : Type u} [Category.{v} C] [MonoidalCategory C]

/-- The tensor powers `V^{⊗0} = 𝟙`, `V^{⊗(m+1)} = V ⊗ V^{⊗m}`. -/
def tensorPow (V : C) : ℕ → C
  | 0 => 𝟙_ C
  | m + 1 => V ⊗ tensorPow V m

variable {R : Type*} [CommRing R] {n : Type*} [Fintype n] [DecidableEq n]

/-- Word bases of the fibres `τ (V^{⊗m})`. -/
abbrev FibreBases (V : C) (τ : C ⥤ ModuleCat.{v} R) (n : Type*) :=
  ∀ m, Basis (Fin m → n) R (τ.obj (tensorPow V m))

variable (V : C) (τ : C ⥤ ModuleCat.{v} R) (bas : FibreBases V τ n)

/-- Every morphism between tensor powers of `V`, with the matrix of `τ f`. -/
def fibreData : IntertwinerData.{v} R n where
  ι := Σ a b : ℕ, tensorPow V a ⟶ tensorPow V b
  src f := f.1
  tgt f := f.2.1
  mat f := LinearMap.toMatrix (bas f.1) (bas f.2.1) (τ.map f.2.2).hom

/-- The coaction of the coend on `τ (V^{⊗m})`: `b_w ↦ ∑ v, b_v ⊗ u^{⊗m}_{v w}`. -/
def coaction (m : ℕ) :
    τ.obj (tensorPow V m) →ₗ[R] τ.obj (tensorPow V m) ⊗[R] Coend (fibreData V τ bas) :=
  (bas m).constr R fun w => ∑ v, bas m v ⊗ₜ[R] tpow (coendMat (fibreData V τ bas)) m v w

@[simp] theorem coaction_basis (m : ℕ) (w : Fin m → n) :
    coaction V τ bas m (bas m w) =
      ∑ v, bas m v ⊗ₜ[R] tpow (coendMat (fibreData V τ bas)) m v w := by
  simp [coaction, Basis.constr_basis]

/-- **The coaction is natural**: for every `f : V^{⊗a} ⟶ V^{⊗b}`,
`(τ f ⊗ id) ∘ ρ_a = ρ_b ∘ τ f`. -/
theorem coaction_natural {a b : ℕ} (f : tensorPow V a ⟶ tensorPow V b) :
    (LinearMap.rTensor (Coend (fibreData V τ bas)) (τ.map f).hom) ∘ₗ coaction V τ bas a =
      coaction V τ bas b ∘ₗ (τ.map f).hom := by
  set D := fibreData V τ bas
  set F := LinearMap.toMatrix (bas a) (bas b) (τ.map f).hom with hF
  have hτ : ∀ v, (τ.map f).hom (bas a v) = ∑ w, F w v • bas b w := fun v => by
    conv_lhs => rw [← Matrix.toLin_toMatrix (bas a) (bas b) (τ.map f).hom]
    rw [Matrix.toLin_self]
  have hI := coendMat_intertwines D ⟨a, b, f⟩
  apply (bas a).ext
  intro w'
  simp only [LinearMap.coe_comp, Function.comp_apply, coaction_basis, map_sum,
    LinearMap.rTensor_tmul, hτ, map_smul, sum_tmul, smul_tmul', Finset.smul_sum]
  calc ∑ v, ∑ w, (F w v • bas b w) ⊗ₜ[R] tpow (coendMat D) a v w'
      = ∑ w, bas b w ⊗ₜ[R] ∑ v, F w v • tpow (coendMat D) a v w' := by
        rw [Finset.sum_comm]
        simp only [tmul_sum, smul_tmul]
    _ = ∑ w, bas b w ⊗ₜ[R] ∑ v, F v w' • tpow (coendMat D) b w v :=
        Finset.sum_congr rfl fun w _ => congrArg _ (hI w w')
    _ = ∑ v, ∑ w, F v w' • bas b w ⊗ₜ[R] tpow (coendMat D) b w v := by
        rw [Finset.sum_comm]
        simp only [tmul_sum, tmul_smul]

end

end QOU.Coproduct
