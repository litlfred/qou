import QOU.BraidsAndKnots.HAdicDrinfeld.ModuleAssociator

/-!
# The unit object and the unitors

Epic `qou-dk7p`, step B of `docs/audits/2026-11-27-kz-trio-strangler-plan.md`.

The unit of the h-adic Drinfeld category is `k`, on which `a` acts by the scalar `ε(a)`. The
unitors are the linear ones, `k ⊗ X ≅ X` and `X ⊗ k ≅ X`; they are `A`-linear by the two counit
laws of `CounitData`.

* `Rep.unit U`: the representation `k` with `ρ(a) = ε(a)`;
* `Rep.leftUnitor`, `Rep.rightUnitor`: the unitors, as isomorphisms of representations;
* `Rep.leftUnitor_naturality`, `Rep.rightUnitor_naturality`.

Over an arbitrary commutative ring `k`; no analysis.
-/

namespace QOU.BraidsAndKnots.HAdicDrinfeld

open scoped TensorProduct
open CategoryTheory

set_option linter.unusedSectionVars false
set_option linter.unusedSimpArgs false

universe u w v

variable {k : Type u} {A : Type w} [CommRing k] [Algebra ℚ k] [Ring A] [Algebra k A]
  [Algebra ℚ A] [IsScalarTower ℚ k A]

namespace Rep

variable {D : CasimirData k A} (U : CounitData D)

/-- The unit representation: `k`, with `a` acting by `ε(a)`. -/
noncomputable def unit : Rep.{u, w, u} D where
  V := k
  ρ := (Algebra.ofId k (Module.End k k)).comp U.ε

theorem unit_ρ_apply (a : A) (r : k) : (unit U).ρ a r = U.ε a * r := by
  change (algebraMap k (Module.End k k) (U.ε a)) r = _
  rw [Module.algebraMap_end_apply, smul_eq_mul]

/-- On `k ⊗ X`, the linear left unitor turns the action of `A ⊗ A` into the action of
`(ε ⊗ id)` of it. -/
theorem lid_pairAction (X : Rep.{u, w, u} D) (z : A ⊗[k] A) :
    (TensorProduct.lid k X.V).toLinearMap ∘ₗ pairAction (unit U) X z =
      X.ρ (Algebra.TensorProduct.lid k A (Algebra.TensorProduct.map U.ε (AlgHom.id k A) z)) ∘ₗ
        (TensorProduct.lid k X.V).toLinearMap := by
  induction z using TensorProduct.induction_on with
  | zero => simp
  | tmul x y =>
    refine TensorProduct.ext' fun (r : k) w => ?_
    show TensorProduct.lid k X.V ((U.ε x * r) ⊗ₜ[k] X.ρ y w) =
      X.ρ (Algebra.TensorProduct.lid k A (U.ε x ⊗ₜ[k] y)) (TensorProduct.lid k X.V (r ⊗ₜ[k] w))
    rw [TensorProduct.lid_tmul, TensorProduct.lid_tmul, Algebra.TensorProduct.lid_tmul, map_smul X.ρ,
      LinearMap.smul_apply, mul_comm, mul_smul, map_smul, smul_comm]
  | add x y hx hy => rw [map_add, map_add, map_add, map_add, LinearMap.comp_add,
      LinearMap.add_comp, hx, hy]

/-- On `X ⊗ k`, the linear right unitor turns the action of `A ⊗ A` into the action of
`(id ⊗ ε)` of it. -/
theorem rid_pairAction (X : Rep.{u, w, u} D) (z : A ⊗[k] A) :
    (TensorProduct.rid k X.V).toLinearMap ∘ₗ pairAction X (unit U) z =
      X.ρ (Algebra.TensorProduct.rid k k A (Algebra.TensorProduct.map (AlgHom.id k A) U.ε z)) ∘ₗ
        (TensorProduct.rid k X.V).toLinearMap := by
  induction z using TensorProduct.induction_on with
  | zero => simp
  | tmul x y =>
    refine TensorProduct.ext' fun w (r : k) => ?_
    show TensorProduct.rid k X.V (X.ρ x w ⊗ₜ[k] (U.ε y * r)) =
      X.ρ (Algebra.TensorProduct.rid k k A (x ⊗ₜ[k] U.ε y)) (TensorProduct.rid k X.V (w ⊗ₜ[k] r))
    rw [TensorProduct.rid_tmul, TensorProduct.rid_tmul, Algebra.TensorProduct.rid_tmul, map_smul X.ρ,
      LinearMap.smul_apply, mul_comm, mul_smul, map_smul, smul_comm]
  | add x y hx hy => rw [map_add, map_add, map_add, map_add, LinearMap.comp_add,
      LinearMap.add_comp, hx, hy]

/-- The left unitor `k ⊗ X ≅ X`. -/
noncomputable def leftUnitor (X : Rep.{u, w, u} D) : tensorObj (unit U) X ≅ X where
  hom := ⟨(TensorProduct.lid k X.V).toLinearMap, fun a => by
    rw [tensorObj_ρ, lid_pairAction, U.counit_left]⟩
  inv := ⟨(TensorProduct.lid k X.V).symm.toLinearMap, fun a => by
    refine LinearMap.ext fun w => (TensorProduct.lid k X.V).injective ?_
    have h := congrArg (fun f => f ((TensorProduct.lid k X.V).symm w))
      (show (TensorProduct.lid k X.V).toLinearMap ∘ₗ (tensorObj (unit U) X).ρ a =
        X.ρ a ∘ₗ (TensorProduct.lid k X.V).toLinearMap by
          rw [tensorObj_ρ, lid_pairAction, U.counit_left])
    change TensorProduct.lid k X.V ((TensorProduct.lid k X.V).symm (X.ρ a w)) =
      TensorProduct.lid k X.V ((tensorObj (unit U) X).ρ a ((TensorProduct.lid k X.V).symm w))
    rw [LinearEquiv.apply_symm_apply]
    simp only [LinearMap.comp_apply, LinearEquiv.coe_coe, LinearEquiv.apply_symm_apply] at h
    exact (h.trans (congrArg (X.ρ a) ((TensorProduct.lid k X.V).apply_symm_apply w))).symm⟩
  hom_inv_id := hom_ext (LinearMap.ext fun x => (TensorProduct.lid k X.V).symm_apply_apply x)
  inv_hom_id := hom_ext (LinearMap.ext fun x => (TensorProduct.lid k X.V).apply_symm_apply x)

/-- The right unitor `X ⊗ k ≅ X`. -/
noncomputable def rightUnitor (X : Rep.{u, w, u} D) : tensorObj X (unit U) ≅ X where
  hom := ⟨(TensorProduct.rid k X.V).toLinearMap, fun a => by
    rw [tensorObj_ρ, rid_pairAction, U.counit_right]⟩
  inv := ⟨(TensorProduct.rid k X.V).symm.toLinearMap, fun a => by
    refine LinearMap.ext fun w => (TensorProduct.rid k X.V).injective ?_
    have h := congrArg (fun f => f ((TensorProduct.rid k X.V).symm w))
      (show (TensorProduct.rid k X.V).toLinearMap ∘ₗ (tensorObj X (unit U)).ρ a =
        X.ρ a ∘ₗ (TensorProduct.rid k X.V).toLinearMap by
          rw [tensorObj_ρ, rid_pairAction, U.counit_right])
    change TensorProduct.rid k X.V ((TensorProduct.rid k X.V).symm (X.ρ a w)) =
      TensorProduct.rid k X.V ((tensorObj X (unit U)).ρ a ((TensorProduct.rid k X.V).symm w))
    rw [LinearEquiv.apply_symm_apply]
    simp only [LinearMap.comp_apply, LinearEquiv.coe_coe, LinearEquiv.apply_symm_apply] at h
    exact (h.trans (congrArg (X.ρ a) ((TensorProduct.rid k X.V).apply_symm_apply w))).symm⟩
  hom_inv_id := hom_ext (LinearMap.ext fun x => (TensorProduct.rid k X.V).symm_apply_apply x)
  inv_hom_id := hom_ext (LinearMap.ext fun x => (TensorProduct.rid k X.V).apply_symm_apply x)

theorem leftUnitor_naturality {X Y : Rep.{u, w, u} D} (φ : X ⟶ Y) :
    tensorHom (𝟙 (unit U)) φ ≫ (leftUnitor U Y).hom = (leftUnitor U X).hom ≫ φ := by
  ext1
  refine TensorProduct.ext' fun (r : k) w => ?_
  change TensorProduct.lid k Y.V (r ⊗ₜ[k] φ.f w) = φ.f (TensorProduct.lid k X.V (r ⊗ₜ[k] w))
  rw [TensorProduct.lid_tmul, TensorProduct.lid_tmul, map_smul]

theorem rightUnitor_naturality {X Y : Rep.{u, w, u} D} (φ : X ⟶ Y) :
    tensorHom φ (𝟙 (unit U)) ≫ (rightUnitor U Y).hom = (rightUnitor U X).hom ≫ φ := by
  ext1
  refine TensorProduct.ext' fun w (r : k) => ?_
  change TensorProduct.rid k Y.V (φ.f w ⊗ₜ[k] r) = φ.f (TensorProduct.rid k X.V (w ⊗ₜ[k] r))
  rw [TensorProduct.rid_tmul, TensorProduct.rid_tmul, map_smul]

/-! ### The triangle -/

/-- On `(X ⊗ k) ⊗ Y`, removing the middle `k` turns the action of `A^{⊗3}` into the action of
`middleCounit` of it. -/
theorem rid_action3 (X Y : Rep.{u, w, u} D) (x : T3 k A) :
    TensorProduct.map (TensorProduct.rid k X.V).toLinearMap LinearMap.id ∘ₗ
        action3 X (unit U) Y x =
      pairAction X Y (D.middleCounit U x) ∘ₗ
        TensorProduct.map (TensorProduct.rid k X.V).toLinearMap LinearMap.id := by
  induction x using TensorProduct.induction_on with
  | zero => simp
  | tmul z c =>
    induction z using TensorProduct.induction_on with
    | zero => simp
    | tmul a b =>
      refine TensorProduct.ext_threefold fun xv (r : k) yv => ?_
      show TensorProduct.map (TensorProduct.rid k X.V).toLinearMap LinearMap.id
          ((X.ρ a xv ⊗ₜ[k] (U.ε b * r)) ⊗ₜ[k] Y.ρ c yv) =
        TensorProduct.map (X.ρ (U.ε b • a)) (Y.ρ c) (TensorProduct.map
          (TensorProduct.rid k X.V).toLinearMap LinearMap.id ((xv ⊗ₜ[k] r) ⊗ₜ[k] yv))
      simp only [TensorProduct.map_tmul, LinearEquiv.coe_coe, TensorProduct.rid_tmul,
        LinearMap.id_apply, map_smul, LinearMap.smul_apply, mul_smul, map_smul X.ρ,
        TensorProduct.smul_tmul']
      rw [smul_comm]
    | add z z' hz hz' =>
      rw [TensorProduct.add_tmul, map_add, map_add, map_add, LinearMap.comp_add,
        LinearMap.add_comp, hz, hz']
  | add x y hx hy => rw [map_add, map_add, map_add, LinearMap.comp_add, LinearMap.add_comp,
      hx, hy]

/-- The linear triangle `(id ⊗ λ) ∘ a = ρ ⊗ id` on `(X ⊗ k) ⊗ Y`. -/
theorem linear_triangle (X Y : Rep.{u, w, u} D) :
    TensorProduct.map LinearMap.id (TensorProduct.lid k Y.V).toLinearMap ∘ₗ
        (TensorProduct.assoc k X.V k Y.V).toLinearMap =
      TensorProduct.map (TensorProduct.rid k X.V).toLinearMap LinearMap.id := by
  refine TensorProduct.ext_threefold fun xv (r : k) yv => ?_
  simp [TensorProduct.smul_tmul]

variable (c : k) {N : ℕ} (hc : c ^ N = 0) {Φ : FreeAlgebra ℚ (Fin 2)}

/-- **The triangle**: `(id ⊗ λ_Y) ∘ α_{X,k,Y} = ρ_X ⊗ id`. Needs `Φ` to have constant term `1`. -/
theorem triangle (hΦ : FreeAlgebra.algebraMapInv Φ = 1) (X Y : Rep.{u, w, u} D) :
    associatorHom c hc U Φ X (unit U) Y ≫ tensorHom (𝟙 X) (leftUnitor U Y).hom =
      tensorHom (rightUnitor U X).hom (𝟙 Y) := by
  ext1
  change TensorProduct.map LinearMap.id (TensorProduct.lid k Y.V).toLinearMap ∘ₗ
      ((TensorProduct.assoc k X.V k Y.V).toLinearMap ∘ₗ
        action3 X (unit U) Y (D.assoc3 c hc Φ)) =
    TensorProduct.map (TensorProduct.rid k X.V).toLinearMap LinearMap.id
  rw [← LinearMap.comp_assoc, linear_triangle, rid_action3, D.middleCounit_assoc3 c hc U hΦ,
    map_one, Module.End.one_eq_id, LinearMap.id_comp]

end Rep

end QOU.BraidsAndKnots.HAdicDrinfeld
