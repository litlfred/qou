import QOU.BraidsAndKnots.HAdicDrinfeld.ModuleAssociator
import QOU.BraidsAndKnots.HAdicDrinfeld.Pentagon

/-!
# The pentagon on modules over a Casimir datum

Epic `qou-dk7p`, step B of `docs/audits/2026-11-27-kz-trio-strangler-plan.md`.

The associator `α = a ∘ ρ(Φ)` of `ModuleAssociator.lean` satisfies the pentagon of a monoidal
category,

  `(id ⊗ α_{X,Y,Z}) ∘ α_{W,X⊗Y,Z} ∘ (α_{W,X,Y} ⊗ id) = α_{W,X,Y⊗Z} ∘ α_{W⊗X,Y,Z}`,

because `Φ` satisfies the quasi-Hopf pentagon in `A^{⊗4}` (`CasimirData.pentagon`). Here:

* `action4`: the action of `A^{⊗4}` on `((W ⊗ X) ⊗ Y) ⊗ Z`;
* `action4_face0 … action4_face4`: each coface map `A^{⊗3} → A^{⊗4}` of `Pentagon.lean`
  corresponds, through the linear associators, to the action of `A^{⊗3}` on one of the five
  triple tensor products that occur in the pentagon;
* `linear_pentagon`: the pentagon for the linear associators;
* `pentagon`: the displayed identity.

Over an arbitrary commutative `ℚ`-algebra `k`; no analysis.
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

variable {D : CasimirData k A} (W X Y Z : Rep.{u, w, v} D)

/-- The action of `A^{⊗4}` on `((W ⊗ X) ⊗ Y) ⊗ Z`. -/
noncomputable def action4 : T4 k A →ₐ[k] Module.End k (((W.V ⊗[k] X.V) ⊗[k] Y.V) ⊗[k] Z.V) :=
  (Module.endTensorEndAlgHom (R := k) (S := k) (A := k)).comp
    (Algebra.TensorProduct.map (action3 W X Y) Z.ρ)

/-- The action of `(A ⊗ A) ⊗ (A ⊗ A)` on `(W ⊗ X) ⊗ (Y ⊗ Z)`. -/
noncomputable def action22 :
    (A ⊗[k] A) ⊗[k] (A ⊗[k] A) →ₐ[k] Module.End k ((W.V ⊗[k] X.V) ⊗[k] (Y.V ⊗[k] Z.V)) :=
  (Module.endTensorEndAlgHom (R := k) (S := k) (A := k)).comp
    (Algebra.TensorProduct.map (pairAction W X) (pairAction Y Z))

theorem action4_face4 (y : T3 k A) :
    action4 W X Y Z (D.face4 y) = TensorProduct.map (action3 W X Y y) LinearMap.id := by
  change TensorProduct.map (action3 W X Y y) (Z.ρ 1) = _
  rw [map_one, Module.End.one_eq_id]

theorem action4_face1 (y : T3 k A) :
    action4 W X Y Z (D.face1 y) = action3 (tensorObj W X) Y Z y := by
  induction y using TensorProduct.induction_on with
  | zero => simp
  | tmul u c =>
    induction u using TensorProduct.induction_on with
    | zero => simp
    | tmul a b => rfl
    | add u u' hu hu' => rw [TensorProduct.add_tmul, map_add, map_add, map_add, hu, hu']
  | add x y hx hy => rw [map_add, map_add, map_add, hx, hy]

theorem action4_face2 (y : T3 k A) :
    TensorProduct.map (TensorProduct.assoc k W.V X.V Y.V).toLinearMap LinearMap.id ∘ₗ
        action4 W X Y Z (D.face2 y) =
      action3 W (tensorObj X Y) Z y ∘ₗ
        TensorProduct.map (TensorProduct.assoc k W.V X.V Y.V).toLinearMap LinearMap.id := by
  induction y using TensorProduct.induction_on with
  | zero => simp
  | tmul u c =>
    induction u using TensorProduct.induction_on with
    | zero => simp
    | tmul a b =>
      change TensorProduct.map (TensorProduct.assoc k W.V X.V Y.V).toLinearMap LinearMap.id ∘ₗ
          TensorProduct.map (action3 W X Y ((Algebra.TensorProduct.assoc k k A A A).symm
            (a ⊗ₜ[k] D.Δ b))) (Z.ρ c) =
        TensorProduct.map (action3' W X Y (a ⊗ₜ[k] D.Δ b)) (Z.ρ c) ∘ₗ
          TensorProduct.map (TensorProduct.assoc k W.V X.V Y.V).toLinearMap LinearMap.id
      rw [← TensorProduct.map_comp, ← TensorProduct.map_comp, assoc_action3,
        AlgEquiv.apply_symm_apply, LinearMap.id_comp, LinearMap.comp_id]
    | add u u' hu hu' =>
      rw [TensorProduct.add_tmul, map_add, map_add, map_add, LinearMap.comp_add,
        LinearMap.add_comp, hu, hu']
  | add x y hx hy => rw [map_add, map_add, map_add, LinearMap.comp_add, LinearMap.add_comp,
      hx, hy]

theorem assoc_action4 (x : T4 k A) :
    (TensorProduct.assoc k (W.V ⊗[k] X.V) Y.V Z.V).toLinearMap ∘ₗ action4 W X Y Z x =
      action22 W X Y Z (Algebra.TensorProduct.assoc k k (A ⊗[k] A) A A x) ∘ₗ
        (TensorProduct.assoc k (W.V ⊗[k] X.V) Y.V Z.V).toLinearMap := by
  induction x using TensorProduct.induction_on with
  | zero => simp
  | tmul v c =>
    induction v using TensorProduct.induction_on with
    | zero => simp
    | tmul u b =>
      change _ ∘ₗ TensorProduct.map (TensorProduct.map (pairAction W X u) (Y.ρ b)) (Z.ρ c) =
        TensorProduct.map (pairAction W X u) (TensorProduct.map (Y.ρ b) (Z.ρ c)) ∘ₗ _
      rw [TensorProduct.map_map_comp_assoc_eq]
    | add v v' hv hv' =>
      rw [TensorProduct.add_tmul, map_add, map_add, map_add, LinearMap.comp_add,
        LinearMap.add_comp, hv, hv']
  | add x y hx hy => rw [map_add, map_add, map_add, LinearMap.comp_add, LinearMap.add_comp,
      hx, hy]

theorem action3_tensor_right (y : T3 k A) :
    action3 W X (tensorObj Y Z) y =
      action22 W X Y Z (Algebra.TensorProduct.map (AlgHom.id k (A ⊗[k] A)) D.Δ y) := by
  induction y using TensorProduct.induction_on with
  | zero => simp
  | tmul u c => rfl
  | add x y hx hy => rw [map_add, map_add, map_add, hx, hy]

theorem action4_face3 (y : T3 k A) :
    (TensorProduct.assoc k (W.V ⊗[k] X.V) Y.V Z.V).toLinearMap ∘ₗ action4 W X Y Z (D.face3 y) =
      action3 W X (tensorObj Y Z) y ∘ₗ
        (TensorProduct.assoc k (W.V ⊗[k] X.V) Y.V Z.V).toLinearMap := by
  rw [assoc_action4, action3_tensor_right]
  change action22 W X Y Z (Algebra.TensorProduct.assoc k k (A ⊗[k] A) A A
    ((Algebra.TensorProduct.assoc k k (A ⊗[k] A) A A).symm _)) ∘ₗ _ = _
  rw [AlgEquiv.apply_symm_apply]
  rfl

/-- The linear isomorphism `((W ⊗ X) ⊗ Y) ⊗ Z → W ⊗ ((X ⊗ Y) ⊗ Z)`. -/
noncomputable def assoc31 :
    ((W.V ⊗[k] X.V) ⊗[k] Y.V) ⊗[k] Z.V →ₗ[k] W.V ⊗[k] ((X.V ⊗[k] Y.V) ⊗[k] Z.V) :=
  (TensorProduct.assoc k W.V (X.V ⊗[k] Y.V) Z.V).toLinearMap ∘ₗ
    TensorProduct.map (TensorProduct.assoc k W.V X.V Y.V).toLinearMap LinearMap.id

theorem action4_face0 (y : T3 k A) :
    assoc31 W X Y Z ∘ₗ action4 W X Y Z (D.face0 y) =
      TensorProduct.map LinearMap.id (action3 X Y Z y) ∘ₗ assoc31 W X Y Z := by
  induction y using TensorProduct.induction_on with
  | zero => simp
  | tmul u c =>
    induction u using TensorProduct.induction_on with
    | zero => simp
    | tmul a b =>
      change _ ∘ₗ TensorProduct.map (TensorProduct.map (TensorProduct.map (W.ρ 1) (X.ρ a))
          (Y.ρ b)) (Z.ρ c) = _
      rw [map_one, Module.End.one_eq_id]
      refine TensorProduct.ext_fourfold fun w x y z => ?_
      rfl
    | add u u' hu hu' =>
      rw [TensorProduct.add_tmul, map_add, map_add, map_add, TensorProduct.map_add_right,
        LinearMap.comp_add, LinearMap.add_comp, hu, hu']
  | add x y hx hy => rw [map_add, map_add, map_add, TensorProduct.map_add_right,
      LinearMap.comp_add, LinearMap.add_comp, hx, hy]

/-- The pentagon for the linear associators. -/
theorem linear_pentagon :
    TensorProduct.map LinearMap.id (TensorProduct.assoc k X.V Y.V Z.V).toLinearMap ∘ₗ
        assoc31 W X Y Z =
      (TensorProduct.assoc k W.V X.V (Y.V ⊗[k] Z.V)).toLinearMap ∘ₗ
        (TensorProduct.assoc k (W.V ⊗[k] X.V) Y.V Z.V).toLinearMap :=
  TensorProduct.ext_fourfold fun _ _ _ _ => rfl

variable (c : k) {N : ℕ} (hc : c ^ N = 0) (U : CounitData D) {Φ : FreeAlgebra ℚ (Fin 2)}

/-- **The pentagon** for the associator `α = a ∘ ρ(Φ)` on representations. -/
theorem pentagon
    (hp : Pentagon Φ (RationalAssociator.t N 0) (RationalAssociator.t N 1)
      (RationalAssociator.t N 3) (RationalAssociator.t N 4) (RationalAssociator.t N 5)) :
    tensorHom (associatorHom c hc U Φ W X Y) (𝟙 Z) ≫ associatorHom c hc U Φ W (tensorObj X Y) Z ≫
        tensorHom (𝟙 W) (associatorHom c hc U Φ X Y Z) =
      associatorHom c hc U Φ (tensorObj W X) Y Z ≫ associatorHom c hc U Φ W X (tensorObj Y Z) := by
  have key := D.pentagon c hc hp
  set F := D.assoc3 c hc Φ
  have h0 : ∀ u, assoc31 W X Y Z (action4 W X Y Z (D.face0 F) u) =
      TensorProduct.map LinearMap.id (action3 X Y Z F) (assoc31 W X Y Z u) :=
    fun u => LinearMap.congr_fun (action4_face0 W X Y Z F) u
  have h2 : ∀ u, TensorProduct.map (TensorProduct.assoc k W.V X.V Y.V).toLinearMap LinearMap.id
      (action4 W X Y Z (D.face2 F) u) = action3 W (tensorObj X Y) Z F
        (TensorProduct.map (TensorProduct.assoc k W.V X.V Y.V).toLinearMap LinearMap.id u) :=
    fun u => LinearMap.congr_fun (action4_face2 W X Y Z F) u
  have h3 : ∀ u, TensorProduct.assoc k (W.V ⊗[k] X.V) Y.V Z.V (action4 W X Y Z (D.face3 F) u) =
      action3 W X (tensorObj Y Z) F (TensorProduct.assoc k (W.V ⊗[k] X.V) Y.V Z.V u) :=
    fun u => LinearMap.congr_fun (action4_face3 W X Y Z F) u
  have h1 := action4_face1 W X Y Z F
  have hl : ∀ u, TensorProduct.map LinearMap.id (TensorProduct.assoc k X.V Y.V Z.V).toLinearMap
      (assoc31 W X Y Z u) = TensorProduct.assoc k W.V X.V (Y.V ⊗[k] Z.V)
        (TensorProduct.assoc k (W.V ⊗[k] X.V) Y.V Z.V u) :=
    fun u => LinearMap.congr_fun (linear_pentagon W X Y Z) u
  ext1
  refine LinearMap.ext fun v => ?_
  change TensorProduct.map LinearMap.id
      ((TensorProduct.assoc k X.V Y.V Z.V).toLinearMap ∘ₗ action3 X Y Z F)
      ((TensorProduct.assoc k W.V (X.V ⊗[k] Y.V) Z.V)
        (action3 W (tensorObj X Y) Z F (TensorProduct.map
          ((TensorProduct.assoc k W.V X.V Y.V).toLinearMap ∘ₗ action3 W X Y F) LinearMap.id v))) =
    (TensorProduct.assoc k W.V X.V (Y.V ⊗[k] Z.V))
      (action3 W X (tensorObj Y Z) F ((TensorProduct.assoc k (W.V ⊗[k] X.V) Y.V Z.V)
        (action3 (tensorObj W X) Y Z F v)))
  rw [← h1, ← h3]
  have e4 : TensorProduct.map ((TensorProduct.assoc k W.V X.V Y.V).toLinearMap ∘ₗ
      action3 W X Y F) LinearMap.id v =
      TensorProduct.map (TensorProduct.assoc k W.V X.V Y.V).toLinearMap LinearMap.id
        (action4 W X Y Z (D.face4 F) v) := by
    rw [action4_face4, ← LinearMap.comp_apply, ← TensorProduct.map_comp, LinearMap.id_comp]
  have e0 : ∀ w : W.V ⊗[k] ((X.V ⊗[k] Y.V) ⊗[k] Z.V), TensorProduct.map LinearMap.id
      ((TensorProduct.assoc k X.V Y.V Z.V).toLinearMap ∘ₗ action3 X Y Z F) w =
      TensorProduct.map LinearMap.id (TensorProduct.assoc k X.V Y.V Z.V).toLinearMap
        (TensorProduct.map LinearMap.id (action3 X Y Z F) w) := by
    intro w
    rw [← LinearMap.comp_apply, ← TensorProduct.map_comp, LinearMap.id_comp]
  rw [e4, ← h2, e0]
  have e31 : ∀ u, (TensorProduct.assoc k W.V (X.V ⊗[k] Y.V) Z.V)
      (TensorProduct.map (TensorProduct.assoc k W.V X.V Y.V).toLinearMap LinearMap.id u) =
      assoc31 W X Y Z u := fun _ => rfl
  rw [e31, ← h0, hl]
  congr 2
  rw [← Module.End.mul_apply, ← map_mul (action4 W X Y Z), ← Module.End.mul_apply,
    ← map_mul (action4 W X Y Z), ← key, map_mul, Module.End.mul_apply]
  rfl

end Rep

end QOU.BraidsAndKnots.HAdicDrinfeld
