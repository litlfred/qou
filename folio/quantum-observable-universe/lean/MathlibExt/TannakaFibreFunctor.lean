/-
Copyright (c) 2026 litlfred. All rights reserved.
Released under Apache 2.0 license.
-/
import MathlibExt.TannakaCoendOneObject
import Mathlib.CategoryTheory.Monoidal.Category
import Mathlib.Algebra.Category.ModuleCat.Basic
import Mathlib.Algebra.Category.ModuleCat.Monoidal.Basic
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

**Monoidal compatibility** (`coaction_monoidal`, `coaction_monoidal_μ`). Suppose the word
bases are the product bases through maps `τ V ⊗ τ (V^{⊗m}) → τ (V^{⊗(m+1)})`, for example
the tensorator `μ` of a lax monoidal structure on `τ`. Then the coaction on `τ (V^{⊗(m+1)})`
is the tensor product of the coactions on `τ V` and `τ (V^{⊗m})`.
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

/-! ## Monoidal compatibility

Suppose `τ (V^{⊗(m+1)}) = τ (V ⊗ V^{⊗m})` receives a map `e m` from `τ V ⊗ τ (V^{⊗m})`, for
instance the tensorator `μ` of a monoidal structure on `τ`. Suppose also that the word
bases are the **product bases**: `bas (m+1) (i :: v) = e m (b i ⊗ bas m v)` for a basis `b`
of `τ V`. Then the coaction on `τ (V^{⊗(m+1)})` is the tensor product of the coaction on
`τ V` and the coaction on `τ (V^{⊗m})`, pushed through `e m` (`coaction_monoidal`). That is
what makes the coend's comodules a monoidal category, compatibly with `τ`. -/

section Monoidal

variable {A : Type*} [Ring A] [Algebra R A]

/-- The tensor product of two coactions:
`m ⊗ n ↦ ∑ (m₀ ⊗ n₀) ⊗ m₁ n₁`. -/
def tensorCoaction {M N : Type*} [AddCommGroup M] [Module R M] [AddCommGroup N] [Module R N]
    (ρ : M →ₗ[R] M ⊗[R] A) (ρ' : N →ₗ[R] N ⊗[R] A) : M ⊗[R] N →ₗ[R] (M ⊗[R] N) ⊗[R] A :=
  (LinearMap.lTensor (M ⊗[R] N) (LinearMap.mul' R A)) ∘ₗ
    (TensorProduct.tensorTensorTensorComm R M A N A).toLinearMap ∘ₗ TensorProduct.map ρ ρ'

theorem tensorCoaction_tmul {M N : Type*} [AddCommGroup M] [Module R M]
    [AddCommGroup N] [Module R N] (ρ : M →ₗ[R] M ⊗[R] A) (ρ' : N →ₗ[R] N ⊗[R] A)
    (x : M) (y : N) (m₀ : M) (a : A) (n₀ : N) (a' : A)
    (hx : ρ x = m₀ ⊗ₜ a) (hy : ρ' y = n₀ ⊗ₜ a') :
    tensorCoaction ρ ρ' (x ⊗ₜ y) = (m₀ ⊗ₜ n₀) ⊗ₜ (a * a') := by
  simp [tensorCoaction, hx, hy]

variable (b : Basis n R (τ.obj V))

/-- The coaction on `τ V`: `b_j ↦ ∑ i, b_i ⊗ u i j`. -/
def coactionV : τ.obj V →ₗ[R] τ.obj V ⊗[R] Coend (fibreData V τ bas) :=
  b.constr R fun j => ∑ i, b i ⊗ₜ[R] coendMat (fibreData V τ bas) i j

@[simp] theorem coactionV_basis (j : n) :
    coactionV V τ bas b (b j) = ∑ i, b i ⊗ₜ[R] coendMat (fibreData V τ bas) i j := by
  simp [coactionV, Basis.constr_basis]

/-- **Monoidal compatibility.** With product bases, the coaction on `τ (V^{⊗(m+1)})` is the
tensor product of the coactions on `τ V` and `τ (V^{⊗m})`. -/
theorem coaction_monoidal (m : ℕ)
    (e : τ.obj V ⊗[R] τ.obj (tensorPow V m) →ₗ[R] τ.obj (tensorPow V (m + 1)))
    (hb : ∀ (i : n) (v : Fin m → n), bas (m + 1) (Fin.cons i v) = e (b i ⊗ₜ bas m v)) :
    coaction V τ bas (m + 1) ∘ₗ e =
      (e.rTensor (Coend (fibreData V τ bas))) ∘ₗ
        tensorCoaction (coactionV V τ bas b) (coaction V τ bas m) := by
  apply TensorProduct.ext
  apply b.ext
  intro i
  apply (bas m).ext
  intro w
  simp only [LinearMap.compr₂_apply, TensorProduct.mk_apply, LinearMap.coe_comp,
    Function.comp_apply]
  rw [← hb, coaction_basis, ← (Fin.consEquiv fun _ => n).sum_comp, Fintype.sum_prod_type]
  simp only [Fin.consEquiv, Equiv.coe_fn_mk, tpow_succ, Fin.cons_zero, Fin.tail_cons, hb]
  simp only [tensorCoaction, LinearMap.coe_comp, Function.comp_apply, TensorProduct.map_tmul,
    coactionV_basis, coaction_basis, sum_tmul, tmul_sum, map_sum,
    LinearEquiv.coe_coe, TensorProduct.tensorTensorTensorComm_tmul, LinearMap.lTensor_tmul,
    LinearMap.mul'_apply, LinearMap.rTensor_tmul]
  rw [Finset.sum_comm]

end Monoidal

section MonoidalFunctor

variable {R : Type v} [CommRing R] (V : C) (τ : C ⥤ ModuleCat.{v} R) [τ.LaxMonoidal]
  (bas : FibreBases V τ n) (b : Basis n R (τ.obj V))

/-- `coaction_monoidal` for the tensorator `μ` of a (lax) monoidal structure on `τ`:
when the word bases are the `μ`-product bases, the coend's coaction is monoidal. -/
theorem coaction_monoidal_μ (m : ℕ)
    (hb : ∀ (i : n) (v : Fin m → n), bas (m + 1) (Fin.cons i v) =
      (Functor.LaxMonoidal.μ τ V (tensorPow V m)).hom (b i ⊗ₜ bas m v)) :
    coaction V τ bas (m + 1) ∘ₗ (Functor.LaxMonoidal.μ τ V (tensorPow V m)).hom =
      ((Functor.LaxMonoidal.μ τ V (tensorPow V m)).hom.rTensor
          (Coend (fibreData V τ bas))) ∘ₗ
        tensorCoaction (coactionV V τ bas b) (coaction V τ bas m) :=
  coaction_monoidal V τ bas b m _ hb

end MonoidalFunctor

end

end QOU.Coproduct
