import QOU.BraidsAndKnots.HAdicDrinfeld.ModuleCategory
import QOU.BraidsAndKnots.HAdicDrinfeld.Hexagon
import QOU.BraidsAndKnots.RationalAssociator.NilpotentUnits
import Mathlib.CategoryTheory.Iso

/-!
# The braiding on representations modulo `h^N`

Epic `qou-dk7p`, step B of `docs/audits/2026-11-27-kz-trio-strangler-plan.md`.

For `R = E(c t)` (`CasimirData.rMatrix`) the braiding of two representations is
`β_{X,Y} = σ ∘ ρ(R) : X ⊗ Y → Y ⊗ X`, with `σ` the flip.

* `cIdeal c`: the multiples `c • x` in `A ⊗ A`. For `c ^ N = 0` it is a two-sided ideal of
  nilpotent elements (`nilIdeal_cIdeal`);
* `rMatrix_isUnit`: so `R = E(c t)` is a unit whenever `E` has constant term `1`;
* `comm_pairAction`: the flip turns the action of `z` into the action of the flipped `z`;
* `braidingHom`: `β` is a morphism of representations, by `rMatrix_quasiCocomm`
  (`Δᵒᵖ(a) R = R Δ(a)`) and cocommutativity of `Δ`;
* `braiding`: `β` as an isomorphism, with inverse `ρ(R⁻¹) ∘ σ`;
* `braidingHom_naturality`.

Over an arbitrary commutative `ℚ`-algebra `k`; no analysis and no numerical value.
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

namespace CasimirData

/-- The `ℚ`-submodule `c • (A ⊗ A)`. -/
noncomputable def cIdeal (c : k) : Submodule ℚ (A ⊗[k] A) :=
  LinearMap.range ((c • LinearMap.id : (A ⊗[k] A) →ₗ[k] A ⊗[k] A).restrictScalars ℚ)

theorem mem_cIdeal {c : k} {x : A ⊗[k] A} : x ∈ cIdeal c ↔ ∃ y, c • y = x := by
  simp [cIdeal]

theorem nilIdeal_cIdeal {N : ℕ} {c : k} (hc : c ^ N = 0) :
    NilIdeal (R := A ⊗[k] A) (cIdeal c) where
  mul_left x y hy := by
    obtain ⟨z, rfl⟩ := mem_cIdeal.mp hy
    exact mem_cIdeal.mpr ⟨x * z, (mul_smul_comm c x z).symm⟩
  mul_right {x} y hx := by
    obtain ⟨z, rfl⟩ := mem_cIdeal.mp hx
    exact mem_cIdeal.mpr ⟨z * y, (smul_mul_assoc c z y).symm⟩
  nil x hx := by
    obtain ⟨z, rfl⟩ := mem_cIdeal.mp hx
    exact ⟨N, by rw [smul_pow, hc, zero_smul]⟩

variable (D : CasimirData k A) {N : ℕ} (E : FreeAlgebra ℚ (Fin 2)) {c : k}

/-- `R = E(c t)` is a unit when `E` has constant term `1`. -/
theorem rMatrix_isUnit (hc : c ^ N = 0) (hE : FreeAlgebra.algebraMapInv E = 1) :
    IsUnit (D.rMatrix E c) :=
  isUnit_eval (nilIdeal_cIdeal hc) (mem_cIdeal.mpr ⟨D.t, rfl⟩) (zero_mem _) hE

/-- `R` as a unit of `A ⊗ A`. -/
noncomputable def rMatrixUnit (hc : c ^ N = 0) (hE : FreeAlgebra.algebraMapInv E = 1) :
    (A ⊗[k] A)ˣ :=
  (D.rMatrix_isUnit E hc hE).unit

@[simp] theorem val_rMatrixUnit (hc : c ^ N = 0) (hE : FreeAlgebra.algebraMapInv E = 1) :
    (D.rMatrixUnit E hc hE : A ⊗[k] A) = D.rMatrix E c :=
  IsUnit.unit_spec _

/-- `R` commutes with every `Δ(a)`. -/
theorem commute_rMatrix (c : k) (a : A) : Commute (D.rMatrix E c) (D.Δ a) := by
  have h := D.rMatrix_quasiCocomm E c a
  rw [D.cocomm a] at h
  exact h.symm

end CasimirData

namespace Rep

variable {D : CasimirData k A}

/-- The flip intertwines the action of `z` on `X ⊗ Y` and of the flipped `z` on `Y ⊗ X`. -/
theorem comm_pairAction (X Y : Rep.{u, w, v} D) (z : A ⊗[k] A) :
    (TensorProduct.comm k X.V Y.V).toLinearMap ∘ₗ pairAction X Y z =
      pairAction Y X (Algebra.TensorProduct.comm k A A z) ∘ₗ
        (TensorProduct.comm k X.V Y.V).toLinearMap := by
  induction z using TensorProduct.induction_on with
  | zero => simp
  | tmul a b =>
    rw [Algebra.TensorProduct.comm_tmul, pairAction_tmul, pairAction_tmul]
    exact TensorProduct.ext' fun x y => rfl
  | add x y hx hy => rw [map_add, map_add, map_add, LinearMap.comp_add, LinearMap.add_comp, hx, hy]

variable (E : FreeAlgebra ℚ (Fin 2)) (c : k)

/-- **The braiding** `β_{X,Y} = σ ∘ ρ(R)`, a morphism of representations. -/
noncomputable def braidingHom (X Y : Rep.{u, w, v} D) : tensorObj X Y ⟶ tensorObj Y X :=
  ⟨(TensorProduct.comm k X.V Y.V).toLinearMap ∘ₗ pairAction X Y (D.rMatrix E c), fun a => by
    rw [tensorObj_ρ, tensorObj_ρ, LinearMap.comp_assoc, ← Module.End.mul_eq_comp,
      ← map_mul (pairAction X Y), ← D.rMatrix_quasiCocomm E c a, map_mul, Module.End.mul_eq_comp,
      ← LinearMap.comp_assoc, comm_pairAction, LinearMap.comp_assoc, D.cocomm a, D.cocomm a]⟩

theorem braidingHom_f (X Y : Rep.{u, w, v} D) :
    (braidingHom E c X Y).f =
      (TensorProduct.comm k X.V Y.V).toLinearMap ∘ₗ pairAction X Y (D.rMatrix E c) := rfl

/-- **Naturality** of the braiding. -/
theorem braidingHom_naturality {X X' Y Y' : Rep.{u, w, v} D} (φ : X ⟶ X') (ψ : Y ⟶ Y') :
    tensorHom φ ψ ≫ braidingHom E c X' Y' = braidingHom E c X Y ≫ tensorHom ψ φ := by
  ext1
  change ((TensorProduct.comm k X'.V Y'.V).toLinearMap ∘ₗ pairAction X' Y' (D.rMatrix E c)) ∘ₗ
      TensorProduct.map φ.f ψ.f =
    TensorProduct.map ψ.f φ.f ∘ₗ
      ((TensorProduct.comm k X.V Y.V).toLinearMap ∘ₗ pairAction X Y (D.rMatrix E c))
  rw [LinearMap.comp_assoc, ← map_comm_pairAction, ← LinearMap.comp_assoc,
    ← LinearMap.comp_assoc]
  congr 1
  exact TensorProduct.ext' fun x y => rfl

variable {N : ℕ} {E} {c} (hc : c ^ N = 0) (hE : FreeAlgebra.algebraMapInv E = 1)

/-- **The braiding as an isomorphism**, with inverse `ρ(R⁻¹) ∘ σ⁻¹`. -/
noncomputable def braiding (X Y : Rep.{u, w, v} D) : tensorObj X Y ≅ tensorObj Y X where
  hom := braidingHom E c X Y
  inv := ⟨pairAction X Y (((D.rMatrixUnit E hc hE)⁻¹ : (A ⊗[k] A)ˣ) : A ⊗[k] A) ∘ₗ
      (TensorProduct.comm k X.V Y.V).symm.toLinearMap, fun a => by
    have hq : Commute (((D.rMatrixUnit E hc hE)⁻¹ : (A ⊗[k] A)ˣ) : A ⊗[k] A) (D.Δ a) := by
      apply Commute.units_inv_left
      rw [CasimirData.val_rMatrixUnit]
      exact D.commute_rMatrix E c a
    have hσ : (TensorProduct.comm k X.V Y.V).symm.toLinearMap ∘ₗ pairAction Y X (D.Δ a) =
        pairAction X Y (D.Δ a) ∘ₗ (TensorProduct.comm k X.V Y.V).symm.toLinearMap := by
      refine LinearMap.ext fun v => ?_
      have h := LinearMap.congr_fun (comm_pairAction X Y (D.Δ a))
        ((TensorProduct.comm k X.V Y.V).symm v)
      simp only [LinearMap.comp_apply, LinearEquiv.coe_coe, LinearEquiv.apply_symm_apply,
        D.cocomm a] at h
      simp only [LinearMap.comp_apply, LinearEquiv.coe_coe]
      rw [← h, LinearEquiv.symm_apply_apply]
    rw [tensorObj_ρ, tensorObj_ρ, LinearMap.comp_assoc, hσ, ← LinearMap.comp_assoc,
      ← Module.End.mul_eq_comp, ← map_mul (pairAction X Y), hq.eq, map_mul,
      Module.End.mul_eq_comp, LinearMap.comp_assoc]⟩
  hom_inv_id := by
    ext1
    refine LinearMap.ext fun v => ?_
    change pairAction X Y (((D.rMatrixUnit E hc hE)⁻¹ : (A ⊗[k] A)ˣ) : A ⊗[k] A)
        ((TensorProduct.comm k X.V Y.V).symm ((TensorProduct.comm k X.V Y.V)
          (pairAction X Y (D.rMatrix E c) v))) = v
    rw [LinearEquiv.symm_apply_apply, ← Module.End.mul_apply, ← map_mul (pairAction X Y),
      ← D.val_rMatrixUnit E hc hE, Units.inv_mul, map_one, Module.End.one_apply]
  inv_hom_id := by
    ext1
    refine LinearMap.ext fun v => ?_
    change (TensorProduct.comm k X.V Y.V) (pairAction X Y (D.rMatrix E c)
        (pairAction X Y (((D.rMatrixUnit E hc hE)⁻¹ : (A ⊗[k] A)ˣ) : A ⊗[k] A)
          ((TensorProduct.comm k X.V Y.V).symm v))) = v
    rw [← Module.End.mul_apply, ← map_mul (pairAction X Y), ← D.val_rMatrixUnit E hc hE,
      Units.mul_inv, map_one, Module.End.one_apply, LinearEquiv.apply_symm_apply]

end Rep

end QOU.BraidsAndKnots.HAdicDrinfeld
