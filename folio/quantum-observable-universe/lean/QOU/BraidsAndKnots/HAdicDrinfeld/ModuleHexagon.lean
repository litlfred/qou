import QOU.BraidsAndKnots.HAdicDrinfeld.ModuleBraiding
import QOU.BraidsAndKnots.HAdicDrinfeld.ModuleMonoidal
import QOU.BraidsAndKnots.HAdicDrinfeld.SecondHexagon
import Mathlib.CategoryTheory.Monoidal.Braided.Basic

/-!
# The hexagons on representations modulo `h^N`

Epic `qou-dk7p`, step B of `docs/audits/2026-11-27-kz-trio-strangler-plan.md`.

The two hexagons for `α = a ∘ ρ(Φ)` and `β = σ ∘ ρ(R)`, `R = E(c t)`, and the braided
monoidal category they give.

* `CasimirData.hexagon_forward_alg`: `Φ · cycl((id ⊗ Δ)(R) Φ) = cycl(τ₁₂(R₂₃ Φ R₁₂))` in
  `A^{⊗3}`, from the second hexagon `hexagon2`.
* `CasimirData.hexagon_reverse_alg`: `Φ⁻¹ · cycl²((Δ ⊗ id)(R) Φ⁻¹) = τ₁₂(R₁₂ Φ⁻¹ τ₂₃(R₂₃))`,
  from the first hexagon `CasimirData.hexagon`.
* `Rep.hexagon_forward`, `Rep.hexagon_reverse`: the two hexagons on representations, in the
  form Mathlib's `BraidedCategory` asks for. Each is the algebra identity carried along the
  leg permutations (`cycl_action3`, `cycl2_action3`, `flip_action3`, `swap23_action3`) and a
  linear identity for the flips.
* `Rep.braided P`: `BraidedCategory (Rep.{u, w, u} D)` over `Rep.monoidal P.toAssocData`, for
  `P : BraidData D` (an associator in `U4 N` for `E`, `c ^ N = 0`, and `E` with constant
  term 1). A `def`, not an instance, since it depends on `P`.

Everything is over an arbitrary commutative `ℚ`-algebra `k`. No analysis is used.
-/

namespace QOU.BraidsAndKnots.HAdicDrinfeld

open scoped TensorProduct
open CategoryTheory
open QOU.HeckeTemperleyLieb.QuasiYangBaxterFromHexagon
open QOU.BraidsAndKnots.RationalAssociator

set_option linter.unusedSectionVars false
set_option linter.unusedSimpArgs false

universe u w v

variable {k : Type u} {A : Type w} [CommRing k] [Algebra ℚ k] [Ring A] [Algebra k A]
  [Algebra ℚ A] [IsScalarTower ℚ k A]

namespace CasimirData

/-- The cyclic leg permutation `(a ⊗ b) ⊗ c ↦ (b ⊗ c) ⊗ a`. -/
noncomputable def cycl : T3 k A →ₐ[k] T3 k A :=
  (Algebra.TensorProduct.comm k A (A ⊗[k] A)).toAlgHom.comp
    (Algebra.TensorProduct.assoc k k A A A).toAlgHom

theorem cycl_tmul (a b c : A) : cycl ((a ⊗ₜ[k] b) ⊗ₜ[k] c) = (b ⊗ₜ[k] c) ⊗ₜ[k] a := by
  simp [cycl]

theorem cycl_leg12 (x : A ⊗[k] A) :
    cycl (leg12 x) = leg13 (Algebra.TensorProduct.comm k A A x) := by
  induction x using TensorProduct.induction_on with
  | zero => simp [leg12]
  | tmul a b => simp [leg12, leg13, leg23, cycl_tmul]
  | add x y hx hy => rw [CasimirData.leg12_add, map_add, hx, hy, map_add, map_add]

theorem cycl_leg23 (x : A ⊗[k] A) : cycl (leg23 x) = leg12 x := by
  induction x using TensorProduct.induction_on with
  | zero => simp [leg12]
  | tmul a b => simp [leg12, leg13, leg23, cycl_tmul]
  | add x y hx hy => rw [map_add, map_add, hx, hy, CasimirData.leg12_add]

theorem cycl_leg13 (x : A ⊗[k] A) :
    cycl (leg13 x) = leg23 (Algebra.TensorProduct.comm k A A x) := by
  induction x using TensorProduct.induction_on with
  | zero => simp
  | tmul a b => simp [leg12, leg13, leg23, cycl_tmul]
  | add x y hx hy => rw [map_add, map_add, hx, hy, map_add, map_add]

variable (D : CasimirData k A) (E : FreeAlgebra ℚ (Fin 2)) (c : k)

/-- `R = E(c t)` is symmetric. -/
theorem rMatrix_symm : Algebra.TensorProduct.comm k A A (D.rMatrix E c) = D.rMatrix E c := by
  rw [rMatrix]
  refine (map_eval ((Algebra.TensorProduct.comm k A A).toAlgHom.restrictScalars ℚ)
    (c • D.t) 0 E).trans ?_
  simp [D.symm]

variable {N : ℕ} (hc : c ^ N = 0)

theorem assoc3Inv_eq (Φ : FreeAlgebra ℚ (Fin 2)) :
    D.assoc3Inv c hc Φ = eval (c • leg23 D.t) (c • leg12 D.t) Φ := by
  rw [assoc3Inv, map_eval, realize3_t, realize3_t]; rfl

theorem map_eval_k (f : T3 k A →ₐ[k] T3 k A) (a b : T3 k A) (Φ : FreeAlgebra ℚ (Fin 2)) :
    f (eval a b Φ) = eval (f a) (f b) Φ :=
  map_eval (f.restrictScalars ℚ) a b Φ

/-- **The algebraic forward hexagon.** With `Rδ = (id ⊗ Δ)(R)` re-associated and `Φ = assoc3`,
`Φ · cycl(Rδ Φ) = cycl(τ₁₂(R₂₃ Φ R₁₂))`. -/
theorem hexagon_forward_alg {Φ : FreeAlgebra ℚ (Fin 2)} (hΦ : Inv512 (Fil N 1) Φ)
    (hhex : Hexagon Φ E (RationalAssociator.t N 0) (RationalAssociator.t N 1)
      (RationalAssociator.t N 3)) :
    D.assoc3 c hc Φ * cycl ((Algebra.TensorProduct.assoc k k A A A).symm
        (Algebra.TensorProduct.map (AlgHom.id k A) D.Δ (D.rMatrix E c)) * D.assoc3 c hc Φ) =
      cycl (tau12 (leg23 (D.rMatrix E c) * D.assoc3 c hc Φ * leg12 (D.rMatrix E c))) := by
  have hi := D.inv_mul_assoc3 c hc hΦ
  have hi' := D.assoc3_mul_inv c hc hΦ
  rw [assoc3Inv_eq] at hi hi'
  rw [D.hexagon2 E c hc hhex]
  simp only [assoc3_eq] at hi hi' ⊢
  have e1 : eval (c • leg13 D.t) (c • leg23 D.t) Φ * leg13 (D.rMatrix E c) *
      eval (c • leg12 D.t) (c • leg13 D.t) Φ * leg12 (D.rMatrix E c) *
      eval (c • leg23 D.t) (c • leg12 D.t) Φ * eval (c • leg12 D.t) (c • leg23 D.t) Φ =
      eval (c • leg13 D.t) (c • leg23 D.t) Φ * leg13 (D.rMatrix E c) *
      eval (c • leg12 D.t) (c • leg13 D.t) Φ * leg12 (D.rMatrix E c) := by
    rw [mul_assoc _ (eval (c • leg23 D.t) (c • leg12 D.t) Φ), hi, mul_one]
  rw [e1]
  simp only [map_mul, map_eval_k, map_smul, cycl_leg12, cycl_leg13, cycl_leg23, D.symm,
    rMatrix_symm, tau12_leg23, tau12_leg12]
  rw [← mul_assoc, ← mul_assoc, ← mul_assoc, hi', one_mul]

theorem tau12_tmul (a b c : A) : tau12 ((a ⊗ₜ[k] b) ⊗ₜ[k] c) = (b ⊗ₜ[k] a) ⊗ₜ[k] c := by
  simp [tau12]

theorem tau12_tau12 (x : T3 k A) : tau12 (tau12 x) = x := by
  induction x using TensorProduct.induction_on with
  | zero => simp
  | tmul y c =>
    induction y using TensorProduct.induction_on with
    | zero => simp
    | tmul a b => rw [tau12_tmul, tau12_tmul]
    | add y y' hy hy' => rw [TensorProduct.add_tmul, map_add, map_add, hy, hy']
  | add x y hx hy => rw [map_add, map_add, hx, hy]

/-- The swap of the last two legs, `(a ⊗ b) ⊗ c ↦ (a ⊗ c) ⊗ b`. -/
noncomputable def tau23 : T3 k A →ₐ[k] T3 k A :=
  (Algebra.TensorProduct.assoc k k A A A).symm.toAlgHom.comp
    ((Algebra.TensorProduct.map (AlgHom.id k A) (Algebra.TensorProduct.comm k A A).toAlgHom).comp
      (Algebra.TensorProduct.assoc k k A A A).toAlgHom)

theorem tau23_tmul (a b c : A) : tau23 ((a ⊗ₜ[k] b) ⊗ₜ[k] c) = (a ⊗ₜ[k] c) ⊗ₜ[k] b := by
  simp [tau23]

theorem tau23_leg23 (x : A ⊗[k] A) :
    tau23 (leg23 x) = leg23 (Algebra.TensorProduct.comm k A A x) := by
  induction x using TensorProduct.induction_on with
  | zero => simp
  | tmul a b => simp [leg23, tau23_tmul]
  | add x y hx hy => rw [map_add, map_add, hx, hy, map_add, map_add]

variable (D : CasimirData k A) (E : FreeAlgebra ℚ (Fin 2)) (c : k) {N : ℕ} (hc : c ^ N = 0)

/-- **The algebraic reverse hexagon.** With `Rd = (Δ ⊗ id)(R)` and `Φ⁻¹ = assoc3Inv`,
`Φ⁻¹ · cycl²(Rd Φ⁻¹) = τ₁₂(R₁₂ Φ⁻¹ τ₂₃(R₂₃))`. -/
theorem hexagon_reverse_alg {Φ : FreeAlgebra ℚ (Fin 2)} (hΦ : AssocU4 N E Φ) :
    D.assoc3Inv c hc Φ * cycl (cycl (Algebra.TensorProduct.map D.Δ (AlgHom.id k A)
        (D.rMatrix E c) * D.assoc3Inv c hc Φ)) =
      tau12 (leg12 (D.rMatrix E c) * D.assoc3Inv c hc Φ * tau23 (leg23 (D.rMatrix E c))) := by
  have hi := D.inv_mul_assoc3 c hc hΦ.inv
  have hi' := D.assoc3_mul_inv c hc hΦ.inv
  rw [assoc3Inv_eq] at hi hi' ⊢
  simp only [assoc3_eq] at hi hi'
  rw [D.hexagon E c hc hΦ]
  simp only [map_eval, realize3_t]
  simp only [t3, Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.cons_val]
  have e1 : eval (c • leg13 D.t) (c • leg12 D.t) Φ * leg13 (D.rMatrix E c) *
      eval (c • leg23 D.t) (c • leg13 D.t) Φ * leg23 (D.rMatrix E c) *
      eval (c • leg12 D.t) (c • leg23 D.t) Φ * eval (c • leg23 D.t) (c • leg12 D.t) Φ =
      eval (c • leg13 D.t) (c • leg12 D.t) Φ * leg13 (D.rMatrix E c) *
      eval (c • leg23 D.t) (c • leg13 D.t) Φ * leg23 (D.rMatrix E c) := by
    rw [mul_assoc _ (eval (c • leg12 D.t) (c • leg23 D.t) Φ), hi', mul_one]
  rw [e1]
  simp only [map_mul, map_eval_k, map_smul, cycl_leg12, cycl_leg13, cycl_leg23, D.symm,
    rMatrix_symm, tau12_leg23, tau12_leg12, tau23_leg23]
  rw [← mul_assoc, ← mul_assoc, ← mul_assoc, hi, one_mul]

end CasimirData

namespace Rep

variable {D : CasimirData k A}

section Linear

variable (X Y Z : Rep.{u, w, v} D)

/-- The cyclic permutation `(X ⊗ Y) ⊗ Z → (Y ⊗ Z) ⊗ X` intertwines `x` and `cycl x`. -/
theorem cycl_action3 (x : T3 k A) (v : (X.V ⊗[k] Y.V) ⊗[k] Z.V) :
    TensorProduct.comm k X.V (Y.V ⊗[k] Z.V) (TensorProduct.assoc k X.V Y.V Z.V
        (action3 X Y Z x v)) =
      action3 Y Z X (CasimirData.cycl x)
        (TensorProduct.comm k X.V (Y.V ⊗[k] Z.V) (TensorProduct.assoc k X.V Y.V Z.V v)) := by
  suffices h : ((TensorProduct.comm k X.V (Y.V ⊗[k] Z.V)).toLinearMap ∘ₗ
      (TensorProduct.assoc k X.V Y.V Z.V).toLinearMap ∘ₗ action3 X Y Z x) =
      (action3 Y Z X (CasimirData.cycl x) ∘ₗ
      (TensorProduct.comm k X.V (Y.V ⊗[k] Z.V)).toLinearMap ∘ₗ
        (TensorProduct.assoc k X.V Y.V Z.V).toLinearMap) from LinearMap.congr_fun h v
  induction x using TensorProduct.induction_on with
  | zero => simp
  | tmul y c =>
    induction y using TensorProduct.induction_on with
    | zero => simp
    | tmul a b =>
      rw [action3_tmul, CasimirData.cycl_tmul, action3_tmul]
      exact TensorProduct.ext_threefold fun _ _ _ => rfl
    | add y y' hy hy' =>
      rw [TensorProduct.add_tmul, map_add, map_add, map_add, LinearMap.comp_add,
        LinearMap.comp_add, LinearMap.add_comp, hy, hy']
  | add x y hx hy =>
    simp only [map_add, LinearMap.comp_add, LinearMap.add_comp, hx, hy]

/-- The flip of the first two factors intertwines `x` and `τ₁₂ x`. -/
theorem flip_action3 (x : T3 k A) (v : (X.V ⊗[k] Y.V) ⊗[k] Z.V) :
    TensorProduct.map (TensorProduct.comm k X.V Y.V).toLinearMap LinearMap.id
        (action3 X Y Z x v) =
      action3 Y X Z (tau12 x)
        (TensorProduct.map (TensorProduct.comm k X.V Y.V).toLinearMap LinearMap.id v) := by
  suffices h : (TensorProduct.map (TensorProduct.comm k X.V Y.V).toLinearMap
      LinearMap.id ∘ₗ action3 X Y Z x) =
      (action3 Y X Z (tau12 x) ∘ₗ
      TensorProduct.map (TensorProduct.comm k X.V Y.V).toLinearMap LinearMap.id) from LinearMap.congr_fun h v
  induction x using TensorProduct.induction_on with
  | zero => simp
  | tmul y c =>
    induction y using TensorProduct.induction_on with
    | zero => simp
    | tmul a b =>
      rw [action3_tmul, CasimirData.tau12_tmul, action3_tmul]
      exact TensorProduct.ext_threefold fun _ _ _ => rfl
    | add y y' hy hy' =>
      rw [TensorProduct.add_tmul, map_add, map_add, map_add, LinearMap.comp_add,
        LinearMap.add_comp, hy, hy']
  | add x y hx hy =>
    rw [map_add, map_add, map_add, LinearMap.comp_add, LinearMap.add_comp, hx, hy]

/-- `ρ(y)` on `X ⊗ (Y ⊗ Z)` is the action of `(id ⊗ Δ)(y)`. -/
theorem pairAction_tensor_right (y : A ⊗[k] A) :
    pairAction X (tensorObj Y Z) y =
      action3' X Y Z (Algebra.TensorProduct.map (AlgHom.id k A) D.Δ y) := by
  induction y using TensorProduct.induction_on with
  | zero => simp
  | tmul a b => rfl
  | add x y hx hy => rw [map_add, hx, hy, map_add, map_add]

/-- `x ⊗ id` on `(X ⊗ Y) ⊗ Z` is the action of `x₁₂`. -/
theorem action3_leg12 (y : A ⊗[k] A) :
    action3 X Y Z (leg12 y) = TensorProduct.map (pairAction X Y y) LinearMap.id := by
  change TensorProduct.map (pairAction X Y y) (Z.ρ 1) = _
  rw [map_one, Module.End.one_eq_id]

/-- `id ⊗ ρ(y)` on `Y ⊗ (X ⊗ Z)`, pulled back along the associator, is the action of `y₂₃`. -/
theorem assoc_action3_leg23 (y : A ⊗[k] A) (v : (Y.V ⊗[k] X.V) ⊗[k] Z.V) :
    TensorProduct.map LinearMap.id (pairAction X Z y) (TensorProduct.assoc k Y.V X.V Z.V v) =
      TensorProduct.assoc k Y.V X.V Z.V (action3 Y X Z (leg23 y) v) := by
  suffices h : (TensorProduct.map LinearMap.id (pairAction X Z y) ∘ₗ
      (TensorProduct.assoc k Y.V X.V Z.V).toLinearMap) =
      ((TensorProduct.assoc k Y.V X.V Z.V).toLinearMap ∘ₗ action3 Y X Z (leg23 y)) from LinearMap.congr_fun h v
  induction y using TensorProduct.induction_on with
  | zero => simp
  | tmul a b =>
    refine TensorProduct.ext_threefold fun yv xv zv => ?_
    change yv ⊗ₜ[k] (X.ρ a xv ⊗ₜ[k] Z.ρ b zv) =
      TensorProduct.assoc k Y.V X.V Z.V
        (TensorProduct.map (TensorProduct.map (Y.ρ 1) (X.ρ a)) (Z.ρ b) ((yv ⊗ₜ xv) ⊗ₜ zv))
    simp
  | add x y hx hy =>
    simp only [map_add, TensorProduct.map_add_right, LinearMap.comp_add, LinearMap.add_comp,
      hx, hy]

/-- The linear hexagon for the flips: `(id ⊗ σ) ∘ a ∘ (σ ⊗ id) = a ∘ σ ∘ a`. -/
theorem linear_hexagon (v : (X.V ⊗[k] Y.V) ⊗[k] Z.V) :
    TensorProduct.map LinearMap.id (TensorProduct.comm k X.V Z.V).toLinearMap
        (TensorProduct.assoc k Y.V X.V Z.V
          (TensorProduct.map (TensorProduct.comm k X.V Y.V).toLinearMap LinearMap.id v)) =
      TensorProduct.assoc k Y.V Z.V X.V (TensorProduct.comm k X.V (Y.V ⊗[k] Z.V)
        (TensorProduct.assoc k X.V Y.V Z.V v)) := by
  suffices h : (TensorProduct.map LinearMap.id
      (TensorProduct.comm k X.V Z.V).toLinearMap ∘ₗ
      (TensorProduct.assoc k Y.V X.V Z.V).toLinearMap ∘ₗ
      TensorProduct.map (TensorProduct.comm k X.V Y.V).toLinearMap LinearMap.id) =
      ((TensorProduct.assoc k Y.V Z.V X.V).toLinearMap ∘ₗ
      (TensorProduct.comm k X.V (Y.V ⊗[k] Z.V)).toLinearMap ∘ₗ
      (TensorProduct.assoc k X.V Y.V Z.V).toLinearMap) from LinearMap.congr_fun h v
  exact TensorProduct.ext_threefold fun _ _ _ => rfl

/-- `ρ(y)` on `(X ⊗ Y) ⊗ Z` is the action of `(Δ ⊗ id)(y)`. -/
theorem pairAction_tensor_left (y : A ⊗[k] A) :
    pairAction (tensorObj X Y) Z y =
      action3 X Y Z (Algebra.TensorProduct.map D.Δ (AlgHom.id k A) y) := by
  induction y using TensorProduct.induction_on with
  | zero => simp
  | tmul a b => rfl
  | add x y hx hy => rw [map_add, hx, hy, map_add, map_add]

/-- The cyclic permutation `(X ⊗ Y) ⊗ Z → (Z ⊗ X) ⊗ Y` intertwines `x` and `cycl² x`. -/
theorem cycl2_action3 (x : T3 k A) (v : (X.V ⊗[k] Y.V) ⊗[k] Z.V) :
    (TensorProduct.assoc k Z.V X.V Y.V).symm (TensorProduct.comm k (X.V ⊗[k] Y.V) Z.V
        (action3 X Y Z x v)) =
      action3 Z X Y (CasimirData.cycl (CasimirData.cycl x))
        ((TensorProduct.assoc k Z.V X.V Y.V).symm (TensorProduct.comm k (X.V ⊗[k] Y.V) Z.V v)) := by
  suffices h : ((TensorProduct.assoc k Z.V X.V Y.V).symm.toLinearMap ∘ₗ
      (TensorProduct.comm k (X.V ⊗[k] Y.V) Z.V).toLinearMap ∘ₗ action3 X Y Z x) =
      (action3 Z X Y (CasimirData.cycl (CasimirData.cycl x)) ∘ₗ
      (TensorProduct.assoc k Z.V X.V Y.V).symm.toLinearMap ∘ₗ
        (TensorProduct.comm k (X.V ⊗[k] Y.V) Z.V).toLinearMap) from LinearMap.congr_fun h v
  induction x using TensorProduct.induction_on with
  | zero => simp
  | tmul y c =>
    induction y using TensorProduct.induction_on with
    | zero => simp
    | tmul a b =>
      rw [action3_tmul, CasimirData.cycl_tmul, CasimirData.cycl_tmul, action3_tmul]
      exact TensorProduct.ext_threefold fun _ _ _ => rfl
    | add y y' hy hy' =>
      rw [TensorProduct.add_tmul, map_add, map_add, map_add, map_add, LinearMap.comp_add,
        LinearMap.comp_add, LinearMap.add_comp, hy, hy']
  | add x y hx hy =>
    simp only [map_add, LinearMap.comp_add, LinearMap.add_comp, hx, hy]

/-- The flip of the last two factors, `(X ⊗ Y) ⊗ Z → (X ⊗ Z) ⊗ Y`, intertwines `x` and
`τ₂₃ x`. -/
theorem swap23_action3 (x : T3 k A) (v : (X.V ⊗[k] Y.V) ⊗[k] Z.V) :
    (TensorProduct.assoc k X.V Z.V Y.V).symm (TensorProduct.map LinearMap.id
        (TensorProduct.comm k Y.V Z.V).toLinearMap
        (TensorProduct.assoc k X.V Y.V Z.V (action3 X Y Z x v))) =
      action3 X Z Y (CasimirData.tau23 x)
        ((TensorProduct.assoc k X.V Z.V Y.V).symm (TensorProduct.map LinearMap.id
          (TensorProduct.comm k Y.V Z.V).toLinearMap (TensorProduct.assoc k X.V Y.V Z.V v))) := by
  suffices h : ((TensorProduct.assoc k X.V Z.V Y.V).symm.toLinearMap ∘ₗ
      TensorProduct.map LinearMap.id (TensorProduct.comm k Y.V Z.V).toLinearMap ∘ₗ
      (TensorProduct.assoc k X.V Y.V Z.V).toLinearMap ∘ₗ action3 X Y Z x) =
      (action3 X Z Y (CasimirData.tau23 x) ∘ₗ
      (TensorProduct.assoc k X.V Z.V Y.V).symm.toLinearMap ∘ₗ
      TensorProduct.map LinearMap.id (TensorProduct.comm k Y.V Z.V).toLinearMap ∘ₗ
      (TensorProduct.assoc k X.V Y.V Z.V).toLinearMap) from LinearMap.congr_fun h v
  induction x using TensorProduct.induction_on with
  | zero => simp
  | tmul y c =>
    induction y using TensorProduct.induction_on with
    | zero => simp
    | tmul a b =>
      rw [action3_tmul, CasimirData.tau23_tmul, action3_tmul]
      exact TensorProduct.ext_threefold fun _ _ _ => rfl
    | add y y' hy hy' =>
      rw [TensorProduct.add_tmul, map_add, map_add, map_add, LinearMap.comp_add,
        LinearMap.comp_add, LinearMap.comp_add, LinearMap.add_comp, hy, hy']
  | add x y hx hy =>
    simp only [map_add, LinearMap.comp_add, LinearMap.add_comp, hx, hy]

/-- The linear reverse hexagon for the flips. -/
theorem linear_hexagon_reverse (v : (X.V ⊗[k] Y.V) ⊗[k] Z.V) :
    TensorProduct.map (TensorProduct.comm k X.V Z.V).toLinearMap LinearMap.id
        ((TensorProduct.assoc k X.V Z.V Y.V).symm (TensorProduct.map LinearMap.id
          (TensorProduct.comm k Y.V Z.V).toLinearMap (TensorProduct.assoc k X.V Y.V Z.V v))) =
      (TensorProduct.assoc k Z.V X.V Y.V).symm (TensorProduct.comm k (X.V ⊗[k] Y.V) Z.V v) := by
  suffices h : (TensorProduct.map (TensorProduct.comm k X.V Z.V).toLinearMap LinearMap.id ∘ₗ
      (TensorProduct.assoc k X.V Z.V Y.V).symm.toLinearMap ∘ₗ
      TensorProduct.map LinearMap.id (TensorProduct.comm k Y.V Z.V).toLinearMap ∘ₗ
      (TensorProduct.assoc k X.V Y.V Z.V).toLinearMap) =
      ((TensorProduct.assoc k Z.V X.V Y.V).symm.toLinearMap ∘ₗ
      (TensorProduct.comm k (X.V ⊗[k] Y.V) Z.V).toLinearMap) from LinearMap.congr_fun h v
  exact TensorProduct.ext_threefold fun _ _ _ => rfl

end Linear

section Hexagon

variable (E : FreeAlgebra ℚ (Fin 2)) (c : k) {N : ℕ} (hc : c ^ N = 0) (U : CounitData D)
  {Φ : FreeAlgebra ℚ (Fin 2)}

/-- **The forward hexagon**
`α_{Y,Z,X} ∘ β_{X,Y⊗Z} ∘ α_{X,Y,Z} = (id_Y ⊗ β_{X,Z}) ∘ α_{Y,X,Z} ∘ (β_{X,Y} ⊗ id_Z)`. -/
theorem hexagon_forward (hΦ : Inv512 (Fil N 1) Φ)
    (hhex : Hexagon Φ E (RationalAssociator.t N 0) (RationalAssociator.t N 1)
      (RationalAssociator.t N 3)) (X Y Z : Rep.{u, w, v} D) :
    associatorHom c hc U Φ X Y Z ≫ braidingHom E c X (tensorObj Y Z) ≫
        associatorHom c hc U Φ Y Z X =
      tensorHom (braidingHom E c X Y) (𝟙 Z) ≫ associatorHom c hc U Φ Y X Z ≫
        tensorHom (𝟙 Y) (braidingHom E c X Z) := by
  have key := D.hexagon_forward_alg E c hc hΦ hhex
  have hA : ∀ (x : T3 k A) (u : (X.V ⊗[k] Y.V) ⊗[k] Z.V),
      TensorProduct.assoc k X.V Y.V Z.V (action3 X Y Z x u) =
        action3' X Y Z (Algebra.TensorProduct.assoc k k A A A x)
          (TensorProduct.assoc k X.V Y.V Z.V u) :=
    fun x u => LinearMap.congr_fun (assoc_action3 X Y Z x) u
  have h1 : ∀ u : (X.V ⊗[k] Y.V) ⊗[k] Z.V,
      pairAction X (tensorObj Y Z) (D.rMatrix E c) (TensorProduct.assoc k X.V Y.V Z.V u) =
        TensorProduct.assoc k X.V Y.V Z.V (action3 X Y Z
          ((Algebra.TensorProduct.assoc k k A A A).symm
            (Algebra.TensorProduct.map (AlgHom.id k A) D.Δ (D.rMatrix E c))) u) := by
    intro u
    rw [pairAction_tensor_right, hA, AlgEquiv.apply_symm_apply]; rfl
  have hm : ∀ {P Q R' : Rep.{u, w, v} D} (x y : T3 k A) (u : (P.V ⊗[k] Q.V) ⊗[k] R'.V),
      action3 P Q R' x (action3 P Q R' y u) = action3 P Q R' (x * y) u := by
    intro P Q R' x y u
    rw [map_mul, Module.End.mul_apply]
  have hsplit : ∀ {P Q R' S : Type v} [AddCommGroup P] [Module k P] [AddCommGroup Q]
      [Module k Q] [AddCommGroup R'] [Module k R'] [AddCommGroup S] [Module k S]
      (f : P →ₗ[k] Q) (g : R' →ₗ[k] P) (u : R' ⊗[k] S),
      TensorProduct.map (f ∘ₗ g) LinearMap.id u =
        TensorProduct.map f LinearMap.id (TensorProduct.map g LinearMap.id u) := by
    intro P Q R' S _ _ _ _ _ _ _ _ f g u
    rw [← LinearMap.comp_apply, ← TensorProduct.map_comp, LinearMap.id_comp]
  have hsplit' : ∀ {P Q R' S : Type v} [AddCommGroup P] [Module k P] [AddCommGroup Q]
      [Module k Q] [AddCommGroup R'] [Module k R'] [AddCommGroup S] [Module k S]
      (f : P →ₗ[k] Q) (g : R' →ₗ[k] P) (u : S ⊗[k] R'),
      TensorProduct.map LinearMap.id (f ∘ₗ g) u =
        TensorProduct.map LinearMap.id f (TensorProduct.map LinearMap.id g u) := by
    intro P Q R' S _ _ _ _ _ _ _ _ f g u
    rw [← LinearMap.comp_apply, ← TensorProduct.map_comp, LinearMap.id_comp]
  ext1
  refine LinearMap.ext fun v => ?_
  change TensorProduct.assoc k Y.V Z.V X.V (action3 Y Z X (D.assoc3 c hc Φ)
      (TensorProduct.comm k X.V (Y.V ⊗[k] Z.V) (pairAction X (tensorObj Y Z) (D.rMatrix E c)
        (TensorProduct.assoc k X.V Y.V Z.V (action3 X Y Z (D.assoc3 c hc Φ) v))))) =
    TensorProduct.map LinearMap.id
      ((TensorProduct.comm k X.V Z.V).toLinearMap ∘ₗ pairAction X Z (D.rMatrix E c))
      (TensorProduct.assoc k Y.V X.V Z.V (action3 Y X Z (D.assoc3 c hc Φ)
        (TensorProduct.map ((TensorProduct.comm k X.V Y.V).toLinearMap ∘ₗ
          pairAction X Y (D.rMatrix E c)) LinearMap.id v)))
  rw [h1, hm, cycl_action3, hm, key]
  rw [hsplit, ← action3_leg12 X Y Z, flip_action3, hm, hsplit', assoc_action3_leg23, hm]
  have h2 := flip_action3 X Y Z (tau12 (leg23 (D.rMatrix E c) *
    (D.assoc3 c hc Φ * tau12 (leg12 (D.rMatrix E c))))) v
  rw [CasimirData.tau12_tau12] at h2
  rw [← h2, linear_hexagon, cycl_action3, CasimirData.tau12_leg12, CasimirData.rMatrix_symm,
    mul_assoc]

/-- **The reverse hexagon**
`α⁻¹_{Z,X,Y} ∘ β_{X⊗Y,Z} ∘ α⁻¹_{X,Y,Z} = (β_{X,Z} ⊗ id_Y) ∘ α⁻¹_{X,Z,Y} ∘ (id_X ⊗ β_{Y,Z})`. -/
theorem hexagon_reverse (hΦ : AssocU4 N E Φ) (X Y Z : Rep.{u, w, v} D) :
    (associator c hc U hΦ.inv X Y Z).inv ≫ braidingHom E c (tensorObj X Y) Z ≫
        (associator c hc U hΦ.inv Z X Y).inv =
      tensorHom (𝟙 X) (braidingHom E c Y Z) ≫ (associator c hc U hΦ.inv X Z Y).inv ≫
        tensorHom (braidingHom E c X Z) (𝟙 Y) := by
  have key := D.hexagon_reverse_alg E c hc hΦ
  have hm : ∀ {P Q R' : Rep.{u, w, v} D} (x y : T3 k A) (u : (P.V ⊗[k] Q.V) ⊗[k] R'.V),
      action3 P Q R' x (action3 P Q R' y u) = action3 P Q R' (x * y) u := by
    intro P Q R' x y u
    rw [map_mul, Module.End.mul_apply]
  have hsplit : ∀ {P Q R' S : Type v} [AddCommGroup P] [Module k P] [AddCommGroup Q]
      [Module k Q] [AddCommGroup R'] [Module k R'] [AddCommGroup S] [Module k S]
      (f : P →ₗ[k] Q) (g : R' →ₗ[k] P) (u : R' ⊗[k] S),
      TensorProduct.map (f ∘ₗ g) LinearMap.id u =
        TensorProduct.map f LinearMap.id (TensorProduct.map g LinearMap.id u) := by
    intro P Q R' S _ _ _ _ _ _ _ _ f g u
    rw [← LinearMap.comp_apply, ← TensorProduct.map_comp, LinearMap.id_comp]
  have hsplit' : ∀ {P Q R' S : Type v} [AddCommGroup P] [Module k P] [AddCommGroup Q]
      [Module k Q] [AddCommGroup R'] [Module k R'] [AddCommGroup S] [Module k S]
      (f : P →ₗ[k] Q) (g : R' →ₗ[k] P) (u : S ⊗[k] R'),
      TensorProduct.map LinearMap.id (f ∘ₗ g) u =
        TensorProduct.map LinearMap.id f (TensorProduct.map LinearMap.id g u) := by
    intro P Q R' S _ _ _ _ _ _ _ _ f g u
    rw [← LinearMap.comp_apply, ← TensorProduct.map_comp, LinearMap.id_comp]
  have hL : ∀ (y : A ⊗[k] A) (u : (X.V ⊗[k] Y.V) ⊗[k] Z.V),
      pairAction (tensorObj X Y) Z y u =
        action3 X Y Z (Algebra.TensorProduct.map D.Δ (AlgHom.id k A) y) u :=
    fun y u => LinearMap.congr_fun (pairAction_tensor_left X Y Z y) u
  ext1
  refine LinearMap.ext fun w => ?_
  obtain ⟨v, rfl⟩ := (TensorProduct.assoc k X.V Y.V Z.V).surjective w
  change action3 Z X Y (D.assoc3Inv c hc Φ) ((TensorProduct.assoc k Z.V X.V Y.V).symm
      (TensorProduct.comm k (X.V ⊗[k] Y.V) Z.V (pairAction (tensorObj X Y) Z (D.rMatrix E c)
        (action3 X Y Z (D.assoc3Inv c hc Φ) ((TensorProduct.assoc k X.V Y.V Z.V).symm
          (TensorProduct.assoc k X.V Y.V Z.V v)))))) =
    TensorProduct.map ((TensorProduct.comm k X.V Z.V).toLinearMap ∘ₗ
        pairAction X Z (D.rMatrix E c)) LinearMap.id
      (action3 X Z Y (D.assoc3Inv c hc Φ) ((TensorProduct.assoc k X.V Z.V Y.V).symm
        (TensorProduct.map LinearMap.id ((TensorProduct.comm k Y.V Z.V).toLinearMap ∘ₗ
          pairAction Y Z (D.rMatrix E c)) (TensorProduct.assoc k X.V Y.V Z.V v))))
  rw [LinearEquiv.symm_apply_apply, hL, hm, cycl2_action3, hm, key]
  rw [hsplit', assoc_action3_leg23, swap23_action3, hm, hsplit, ← action3_leg12 X Z Y, hm,
    flip_action3, linear_hexagon_reverse, mul_assoc]

end Hexagon

section Braided

/-- The data of a braided structure modulo `h^N`: an associator in `U4 N` for the exponential
`E` (constant term, inverse, hexagon, pentagon), the scale `c` with `c ^ N = 0`, the counit, and
`E` with constant term 1 so that `R = E(c t)` is a unit. -/
structure BraidData (D : CasimirData k A) where
  /-- The truncation order. -/
  N : ℕ
  /-- The scale, e.g. `h` in `ℚ[h]/(h^N)`. -/
  c : k
  hc : c ^ N = 0
  /-- The counit. -/
  U : CounitData D
  /-- The exponential, e.g. `exp(X/2)` truncated. -/
  E : FreeAlgebra ℚ (Fin 2)
  hE : FreeAlgebra.algebraMapInv E = 1
  /-- The associator. -/
  Φ : FreeAlgebra ℚ (Fin 2)
  assoc : AssocU4 N E Φ

/-- The associator data underlying braid data. -/
def BraidData.toAssocData {D : CasimirData k A} (P : BraidData D) : AssocData D where
  N := P.N
  c := P.c
  hc := P.hc
  U := P.U
  Φ := P.Φ
  inv := P.assoc.inv
  const := P.assoc.const
  pentagon := P.assoc.pent

variable (P : BraidData D)

/-- **The braided monoidal category of representations modulo `h^N`**, with braiding
`σ ∘ ρ(R)` for `R = E(c t)`, over the monoidal structure `Rep.monoidal P.toAssocData`. -/
noncomputable def braided :
    letI := monoidal P.toAssocData
    BraidedCategory (Rep.{u, w, u} D) :=
  letI := monoidal P.toAssocData
  { braiding := fun X Y => braiding P.hc P.hE X Y
    braiding_naturality_right := fun X _ _ f => braidingHom_naturality P.E P.c (𝟙 X) f
    braiding_naturality_left := fun f Z => braidingHom_naturality P.E P.c f (𝟙 Z)
    hexagon_forward := fun X Y Z =>
      hexagon_forward P.E P.c P.hc P.U P.assoc.inv P.assoc.hex X Y Z
    hexagon_reverse := fun X Y Z => hexagon_reverse P.E P.c P.hc P.U P.assoc X Y Z }

end Braided

end Rep

end QOU.BraidsAndKnots.HAdicDrinfeld
