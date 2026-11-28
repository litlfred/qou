import QOU.BraidsAndKnots.HAdicDrinfeld.Pentagon
import QOU.BraidsAndKnots.RationalAssociator.BaseChangeAction

/-!
# Quasi-bialgebra axioms for the h-adic Drinfeld data

Epic `qou-dk7p`, step C of `docs/audits/2026-11-27-kz-trio-strangler-plan.md`.

`Hexagon.lean` and `Pentagon.lean` give the hexagon and pentagon for `R = E(c t)` and
`Φ = φ(c t₁₂, c t₂₃)`. A quasi-bialgebra also needs a counit, quasi-coassociativity of `Δ` and an
invertible `Φ`. This file supplies them.

* `CounitData D`: a counit `ε` for `D : CasimirData k A`, with `Δ` coassociative, the two counit
  laws, and `(ε ⊗ id)(t) = (id ⊗ ε)(t) = 0` (true for the split Casimir of `U(𝔤)`);
* `assoc3_commute_coproduct3`: `Φ` commutes with `(Δ ⊗ id)Δ(a)`, so
  `quasiCoassoc`: `(id ⊗ Δ)Δ(a) · Φ = Φ · (Δ ⊗ id)Δ(a)`;
* `middleCounit_assoc3`: `(id ⊗ ε ⊗ id)(Φ) = 1`, the triangle axiom, from `ε(φ) = 1`;
* `assoc3_mul_inv`, `inv_mul_assoc3`: `Φ` is a unit with inverse `φ(c t₂₃, c t₁₂)`, from
  Drinfeld's (5.12) (`Inv512`).

No analysis and no numerical value is used.
-/

namespace QOU.BraidsAndKnots.HAdicDrinfeld

open scoped TensorProduct
open QOU.HeckeTemperleyLieb.QuasiYangBaxterFromHexagon
open QOU.BraidsAndKnots.RationalAssociator
open Algebra.TensorProduct

set_option linter.unusedSectionVars false

variable {k A : Type*} [CommRing k] [Algebra ℚ k] [Ring A] [Algebra k A] [Algebra ℚ A]
  [IsScalarTower ℚ k A]

namespace CasimirData

variable (D : CasimirData k A)

/-- `(Δ ⊗ id) Δ (a)`. -/
noncomputable def coprod3 (a : A) : T3 k A :=
  Algebra.TensorProduct.map D.Δ (AlgHom.id k A) (D.Δ a)

/-- `(id ⊗ Δ) Δ (a)`, re-associated to the left. -/
noncomputable def coprod3' (a : A) : T3 k A :=
  (Algebra.TensorProduct.assoc k k A A A).symm (Algebra.TensorProduct.map (AlgHom.id k A) D.Δ (D.Δ a))

end CasimirData

/-- **Counit data** for a `CasimirData`: a counit `ε`, coassociativity of `Δ`, the two counit
laws, and `t` killed by `ε` on either side. -/
structure CounitData (D : CasimirData k A) where
  ε : A →ₐ[k] k
  coassoc : ∀ a, D.coprod3' a = D.coprod3 a
  counit_left : ∀ a, Algebra.TensorProduct.lid k A (Algebra.TensorProduct.map ε (AlgHom.id k A) (D.Δ a)) = a
  counit_right : ∀ a, Algebra.TensorProduct.rid k k A (Algebra.TensorProduct.map (AlgHom.id k A) ε (D.Δ a)) = a
  ε_t_left : Algebra.TensorProduct.lid k A (Algebra.TensorProduct.map ε (AlgHom.id k A) D.t) = 0
  ε_t_right : Algebra.TensorProduct.rid k k A (Algebra.TensorProduct.map (AlgHom.id k A) ε D.t) = 0

namespace CasimirData

variable (D : CasimirData k A) {N : ℕ} (c : k) (hc : c ^ N = 0)

/-! ### Quasi-coassociativity -/

/-- **`Φ` commutes with the iterated coproduct.** -/
theorem assoc3_commute_coproduct3 (U : CounitData D) (Φ : FreeAlgebra ℚ (Fin 2)) (a : A) :
    Commute (D.assoc3 c hc Φ) (D.coprod3 a) := by
  rw [assoc3_eq]
  refine commute_eval ?_ ?_ Φ
  · exact (D.commute_leg12_mapLeft (D.Δ a)).smul_left c
  · rw [← U.coassoc a]
    exact (D.commute_leg23_mapRight (D.Δ a)).smul_left c

/-- **Quasi-coassociativity.** `(id ⊗ Δ)Δ(a) · Φ = Φ · (Δ ⊗ id)Δ(a)`. -/
theorem quasiCoassoc (U : CounitData D) (Φ : FreeAlgebra ℚ (Fin 2)) (a : A) :
    D.coprod3' a * D.assoc3 c hc Φ = D.assoc3 c hc Φ * D.coprod3 a := by
  rw [U.coassoc a]
  exact (D.assoc3_commute_coproduct3 c hc U Φ a).eq.symm

/-! ### The triangle axiom -/

/-- `id ⊗ ε ⊗ id : A^{⊗3} → A^{⊗2}`. -/
noncomputable def middleCounit (U : CounitData D) : T3 k A →ₐ[k] A ⊗[k] A :=
  Algebra.TensorProduct.map
    ((Algebra.TensorProduct.rid k k A).toAlgHom.comp
      (Algebra.TensorProduct.map (AlgHom.id k A) U.ε)) (AlgHom.id k A)

theorem middleCounit_leg12 (U : CounitData D) (x : A ⊗[k] A) :
    D.middleCounit U (leg12 x) =
      (Algebra.TensorProduct.includeLeft : A →ₐ[k] A ⊗[k] A)
        (Algebra.TensorProduct.rid k k A (Algebra.TensorProduct.map (AlgHom.id k A) U.ε x)) := by
  simp [middleCounit, leg12, map_tmul, includeLeft_apply]

theorem middleCounit_leg23 (U : CounitData D) (x : A ⊗[k] A) :
    D.middleCounit U (leg23 x) =
      (Algebra.TensorProduct.includeRight : A →ₐ[k] A ⊗[k] A)
        (Algebra.TensorProduct.lid k A (Algebra.TensorProduct.map U.ε (AlgHom.id k A) x)) := by
  induction x using TensorProduct.induction_on with
  | zero => simp
  | tmul a b =>
    simp only [middleCounit, leg23, map_tmul, includeRight_apply, AlgHom.coe_comp,
      Function.comp_apply, AlgHom.id_apply, AlgEquiv.toAlgHom_eq_coe, AlgHom.coe_coe,
      Algebra.TensorProduct.rid_tmul, Algebra.TensorProduct.lid_tmul, map_one]
    rw [Algebra.smul_def, Algebra.smul_def, mul_one, Algebra.algebraMap_eq_smul_one,
      smul_mul_assoc, one_mul, TensorProduct.smul_tmul]
  | add x y hx hy => simp only [map_add, hx, hy]

/-- **The triangle axiom**, `(id ⊗ ε ⊗ id)(Φ) = 1`, when `ε(φ) = 1`. -/
theorem middleCounit_assoc3 (U : CounitData D) {Φ : FreeAlgebra ℚ (Fin 2)}
    (hΦ : FreeAlgebra.algebraMapInv Φ = 1) : D.middleCounit U (D.assoc3 c hc Φ) = 1 := by
  rw [assoc3_eq]
  have h := map_eval (A := T3 k A) (B := A ⊗[k] A) ((D.middleCounit U).restrictScalars ℚ)
    (c • leg12 D.t) (c • leg23 D.t) Φ
  rw [AlgHom.restrictScalars_apply] at h
  rw [h, AlgHom.restrictScalars_apply, AlgHom.restrictScalars_apply, map_smul, map_smul,
    middleCounit_leg12, middleCounit_leg23, U.ε_t_left, U.ε_t_right, map_zero, map_zero,
    smul_zero, eval_zero_zero, hΦ, map_one]

/-! ### Invertibility of `Φ` -/

/-- `φ(c t₂₃, c t₁₂)`, the inverse of `Φ`. -/
noncomputable def assoc3Inv (Φ : FreeAlgebra ℚ (Fin 2)) : T3 k A :=
  D.realize3 N c hc (eval (RationalAssociator.t N 3) (RationalAssociator.t N 0) Φ)

theorem assoc3_mul_inv {Φ : FreeAlgebra ℚ (Fin 2)} (hΦ : Inv512 (Fil N 1) Φ) :
    D.assoc3 c hc Φ * D.assoc3Inv c hc Φ = 1 := by
  rw [assoc3, assoc3Inv, ← map_mul, hΦ _ _ (t_mem_Fil_one 0) (t_mem_Fil_one 3), map_one]

theorem inv_mul_assoc3 {Φ : FreeAlgebra ℚ (Fin 2)} (hΦ : Inv512 (Fil N 1) Φ) :
    D.assoc3Inv c hc Φ * D.assoc3 c hc Φ = 1 := by
  rw [assoc3, assoc3Inv, ← map_mul, hΦ _ _ (t_mem_Fil_one 3) (t_mem_Fil_one 0), map_one]

/-- `Φ` as a unit of `A^{⊗3}`. -/
noncomputable def assoc3Unit {Φ : FreeAlgebra ℚ (Fin 2)} (hΦ : Inv512 (Fil N 1) Φ) :
    (T3 k A)ˣ :=
  ⟨D.assoc3 c hc Φ, D.assoc3Inv c hc Φ, D.assoc3_mul_inv c hc hΦ, D.inv_mul_assoc3 c hc hΦ⟩

end CasimirData

end QOU.BraidsAndKnots.HAdicDrinfeld
