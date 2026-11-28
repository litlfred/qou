import QOU.BraidsAndKnots.HAdicDrinfeld.ModuleCategory
import QOU.BraidsAndKnots.HAdicDrinfeld.QuasiBialgebra
import Mathlib.CategoryTheory.Iso

/-!
# The associator on modules over a Casimir datum

Epic `qou-dk7p`, step B of `docs/audits/2026-11-27-kz-trio-strangler-plan.md`.

For three representations `X, Y, Z` of `A` (`ModuleCategory.lean`), the associator of the
h-adic Drinfeld category is

  `α_{X,Y,Z} = a ∘ ρ(Φ) : (X ⊗ Y) ⊗ Z → X ⊗ (Y ⊗ Z)`,

where `a` is the linear associator and `ρ(Φ)` is the action of `Φ = φ(c t₁₂, c t₂₃) ∈ A^{⊗3}`.
This file proves that it is an isomorphism of representations, natural in all three variables.

* `action3`, `action3'`: the actions of `(A ⊗ A) ⊗ A` on `(X ⊗ Y) ⊗ Z` and of `A ⊗ (A ⊗ A)` on
  `X ⊗ (Y ⊗ Z)`; `tensor_tensor_ρ`, `tensor_tensor_ρ'` express the module structures through
  them; `assoc_action3` says `a` intertwines them;
* `associatorHom`: `α` is `A`-linear. This is where quasi-coassociativity
  `(id ⊗ Δ)Δ(a) · Φ = Φ · (Δ ⊗ id)Δ(a)` (`CasimirData.quasiCoassoc`) is used;
* `associator`: with the inverse `ρ(Φ⁻¹) ∘ a⁻¹`, `α` is an isomorphism;
* `associator_naturality`.

Over an arbitrary commutative `ℚ`-algebra `k`; no analysis, no numerical value.
-/

namespace QOU.BraidsAndKnots.HAdicDrinfeld

open scoped TensorProduct
open CategoryTheory
open QOU.HeckeTemperleyLieb.QuasiYangBaxterFromHexagon
open QOU.BraidsAndKnots.RationalAssociator

set_option linter.unusedSectionVars false

universe u w v

variable {k : Type u} {A : Type w} [CommRing k] [Algebra ℚ k] [Ring A] [Algebra k A]
  [Algebra ℚ A] [IsScalarTower ℚ k A]

namespace Rep

variable {D : CasimirData k A}

/-- The action of `(A ⊗ A) ⊗ A` on `(X ⊗ Y) ⊗ Z`. -/
noncomputable def action3 (X Y Z : Rep.{u, w, v} D) :
    T3 k A →ₐ[k] Module.End k ((X.V ⊗[k] Y.V) ⊗[k] Z.V) :=
  (Module.endTensorEndAlgHom (R := k) (S := k) (A := k)).comp
    (Algebra.TensorProduct.map (pairAction X Y) Z.ρ)

/-- The action of `A ⊗ (A ⊗ A)` on `X ⊗ (Y ⊗ Z)`. -/
noncomputable def action3' (X Y Z : Rep.{u, w, v} D) :
    A ⊗[k] (A ⊗[k] A) →ₐ[k] Module.End k (X.V ⊗[k] (Y.V ⊗[k] Z.V)) :=
  (Module.endTensorEndAlgHom (R := k) (S := k) (A := k)).comp
    (Algebra.TensorProduct.map X.ρ (pairAction Y Z))

theorem action3_tmul (X Y Z : Rep.{u, w, v} D) (a b c : A) :
    action3 X Y Z ((a ⊗ₜ b) ⊗ₜ c) =
      TensorProduct.map (TensorProduct.map (X.ρ a) (Y.ρ b)) (Z.ρ c) := rfl

theorem action3'_tmul (X Y Z : Rep.{u, w, v} D) (a b c : A) :
    action3' X Y Z (a ⊗ₜ (b ⊗ₜ c)) =
      TensorProduct.map (X.ρ a) (TensorProduct.map (Y.ρ b) (Z.ρ c)) := rfl

/-- The module structure of `(X ⊗ Y) ⊗ Z` is `action3 ∘ (Δ ⊗ id) ∘ Δ`. -/
theorem tensor_tensor_ρ (X Y Z : Rep.{u, w, v} D) (a : A) :
    (tensorObj (tensorObj X Y) Z).ρ a = action3 X Y Z (D.coprod3 a) := by
  rw [tensorObj_ρ, CasimirData.coprod3]
  induction D.Δ a using TensorProduct.induction_on with
  | zero => simp
  | tmul x y => rfl
  | add x y hx hy => rw [map_add, hx, hy, map_add, map_add]

/-- The module structure of `X ⊗ (Y ⊗ Z)` is `action3' ∘ (id ⊗ Δ) ∘ Δ`. -/
theorem tensor_tensor_ρ' (X Y Z : Rep.{u, w, v} D) (a : A) :
    (tensorObj X (tensorObj Y Z)).ρ a =
      action3' X Y Z (Algebra.TensorProduct.map (AlgHom.id k A) D.Δ (D.Δ a)) := by
  rw [tensorObj_ρ]
  induction D.Δ a using TensorProduct.induction_on with
  | zero => simp
  | tmul x y => rfl
  | add x y hx hy => rw [map_add, hx, hy, map_add, map_add]

/-- The linear associator intertwines the two actions. -/
theorem assoc_action3 (X Y Z : Rep.{u, w, v} D) (x : T3 k A) :
    (TensorProduct.assoc k X.V Y.V Z.V).toLinearMap ∘ₗ action3 X Y Z x =
      action3' X Y Z (Algebra.TensorProduct.assoc k k A A A x) ∘ₗ
        (TensorProduct.assoc k X.V Y.V Z.V).toLinearMap := by
  induction x using TensorProduct.induction_on with
  | zero => simp
  | tmul xy c =>
    induction xy using TensorProduct.induction_on with
    | zero => simp
    | tmul a b =>
      rw [action3_tmul, Algebra.TensorProduct.assoc_tmul, action3'_tmul,
        TensorProduct.map_map_comp_assoc_eq]
    | add x y hx hy =>
      rw [TensorProduct.add_tmul, map_add, map_add, map_add, LinearMap.comp_add,
        LinearMap.add_comp, hx, hy]
  | add x y hx hy => rw [map_add, map_add, map_add, LinearMap.comp_add, LinearMap.add_comp, hx, hy]

/-- Every element of `(A ⊗ A) ⊗ A` acts naturally. -/
theorem map_comm_action3 {X X' Y Y' Z Z' : Rep.{u, w, v} D} (φ : X ⟶ X') (ψ : Y ⟶ Y')
    (χ : Z ⟶ Z') (x : T3 k A) :
    TensorProduct.map (TensorProduct.map φ.f ψ.f) χ.f ∘ₗ action3 X Y Z x =
      action3 X' Y' Z' x ∘ₗ TensorProduct.map (TensorProduct.map φ.f ψ.f) χ.f := by
  induction x using TensorProduct.induction_on with
  | zero => simp
  | tmul y c =>
    change TensorProduct.map _ _ ∘ₗ TensorProduct.map (pairAction X Y y) (Z.ρ c) =
      TensorProduct.map (pairAction X' Y' y) (Z'.ρ c) ∘ₗ TensorProduct.map _ _
    rw [← TensorProduct.map_comp, ← TensorProduct.map_comp, map_comm_pairAction φ ψ y, χ.comm]
  | add x y hx hy => rw [map_add, map_add, LinearMap.comp_add, LinearMap.add_comp, hx, hy]

variable (c : k) {N : ℕ} (hc : c ^ N = 0) (U : CounitData D) (Φ : FreeAlgebra ℚ (Fin 2))

/-- The associator `a ∘ ρ(Φ)` as a morphism of representations. -/
noncomputable def associatorHom (X Y Z : Rep.{u, w, v} D) :
    tensorObj (tensorObj X Y) Z ⟶ tensorObj X (tensorObj Y Z) :=
  ⟨(TensorProduct.assoc k X.V Y.V Z.V).toLinearMap ∘ₗ action3 X Y Z (D.assoc3 c hc Φ),
    fun a => by
      rw [tensor_tensor_ρ, tensor_tensor_ρ', LinearMap.comp_assoc, ← Module.End.mul_eq_comp,
        ← map_mul (action3 X Y Z), ← D.quasiCoassoc c hc U Φ a, map_mul, Module.End.mul_eq_comp,
        ← LinearMap.comp_assoc, assoc_action3, CasimirData.coprod3', AlgEquiv.apply_symm_apply,
        LinearMap.comp_assoc]⟩

/-- The linear inverse `ρ(Φ⁻¹) ∘ a⁻¹`. -/
noncomputable def associatorInvLin (X Y Z : Rep.{u, w, v} D) :
    X.V ⊗[k] (Y.V ⊗[k] Z.V) →ₗ[k] (X.V ⊗[k] Y.V) ⊗[k] Z.V :=
  action3 X Y Z (D.assoc3Inv c hc Φ) ∘ₗ (TensorProduct.assoc k X.V Y.V Z.V).symm.toLinearMap

variable {Φ}

theorem associatorHom_comp_inv (hΦ : Inv512 (Fil N 1) Φ) (X Y Z : Rep.{u, w, v} D) :
    (associatorHom c hc U Φ X Y Z).f ∘ₗ associatorInvLin c hc Φ X Y Z = LinearMap.id := by
  refine LinearMap.ext fun x => ?_
  change TensorProduct.assoc k X.V Y.V Z.V ((action3 X Y Z (D.assoc3 c hc Φ) *
    action3 X Y Z (D.assoc3Inv c hc Φ)) ((TensorProduct.assoc k X.V Y.V Z.V).symm x)) = x
  rw [← map_mul (action3 X Y Z), D.assoc3_mul_inv c hc hΦ, map_one, Module.End.one_apply,
    LinearEquiv.apply_symm_apply]

theorem associatorInv_comp_hom (hΦ : Inv512 (Fil N 1) Φ) (X Y Z : Rep.{u, w, v} D) :
    associatorInvLin c hc Φ X Y Z ∘ₗ (associatorHom c hc U Φ X Y Z).f = LinearMap.id := by
  refine LinearMap.ext fun x => ?_
  change action3 X Y Z (D.assoc3Inv c hc Φ) ((TensorProduct.assoc k X.V Y.V Z.V).symm
    (TensorProduct.assoc k X.V Y.V Z.V (action3 X Y Z (D.assoc3 c hc Φ) x))) = x
  rw [LinearEquiv.symm_apply_apply, ← Module.End.mul_apply, ← map_mul (action3 X Y Z),
    D.inv_mul_assoc3 c hc hΦ, map_one, Module.End.one_apply]

/-- **The associator** `α_{X,Y,Z} = a ∘ ρ(Φ)`, an isomorphism of representations. -/
noncomputable def associator (hΦ : Inv512 (Fil N 1) Φ) (X Y Z : Rep.{u, w, v} D) :
    tensorObj (tensorObj X Y) Z ≅ tensorObj X (tensorObj Y Z) where
  hom := associatorHom c hc U Φ X Y Z
  inv := ⟨associatorInvLin c hc Φ X Y Z, fun a => by
    have h1 := associatorHom_comp_inv c hc U hΦ X Y Z
    have h2 := associatorInv_comp_hom c hc U hΦ X Y Z
    have hc' := (associatorHom c hc U Φ X Y Z).comm a
    calc associatorInvLin c hc Φ X Y Z ∘ₗ (tensorObj X (tensorObj Y Z)).ρ a
        = associatorInvLin c hc Φ X Y Z ∘ₗ (tensorObj X (tensorObj Y Z)).ρ a ∘ₗ
            ((associatorHom c hc U Φ X Y Z).f ∘ₗ associatorInvLin c hc Φ X Y Z) := by
          rw [h1, LinearMap.comp_id]
      _ = (associatorInvLin c hc Φ X Y Z ∘ₗ (associatorHom c hc U Φ X Y Z).f) ∘ₗ
            (tensorObj (tensorObj X Y) Z).ρ a ∘ₗ associatorInvLin c hc Φ X Y Z := by
          simp only [LinearMap.comp_assoc]
          congr 1
          rw [← LinearMap.comp_assoc, ← hc', LinearMap.comp_assoc]
      _ = _ := by rw [h2, LinearMap.id_comp]⟩
  hom_inv_id := hom_ext (associatorInv_comp_hom c hc U hΦ X Y Z)
  inv_hom_id := hom_ext (associatorHom_comp_inv c hc U hΦ X Y Z)

/-- **Naturality** of the associator. -/
theorem associatorHom_naturality {X X' Y Y' Z Z' : Rep.{u, w, v} D} (φ : X ⟶ X') (ψ : Y ⟶ Y')
    (χ : Z ⟶ Z') :
    tensorHom (tensorHom φ ψ) χ ≫ associatorHom c hc U Φ X' Y' Z' =
      associatorHom c hc U Φ X Y Z ≫ tensorHom φ (tensorHom ψ χ) := by
  ext1
  change ((TensorProduct.assoc k X'.V Y'.V Z'.V).toLinearMap ∘ₗ
      action3 X' Y' Z' (D.assoc3 c hc Φ)) ∘ₗ TensorProduct.map (TensorProduct.map φ.f ψ.f) χ.f =
    TensorProduct.map φ.f (TensorProduct.map ψ.f χ.f) ∘ₗ
      (TensorProduct.assoc k X.V Y.V Z.V).toLinearMap ∘ₗ action3 X Y Z (D.assoc3 c hc Φ)
  rw [LinearMap.comp_assoc, ← map_comm_action3, ← LinearMap.comp_assoc,
    ← TensorProduct.map_map_comp_assoc_eq, LinearMap.comp_assoc]

end Rep

end QOU.BraidsAndKnots.HAdicDrinfeld
