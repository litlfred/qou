/-
Copyright (c) 2026 litlfred. All rights reserved.
Released under Apache 2.0 license.
-/
import MathlibExt.TannakaCoendOneObject
import QOU.LiftingDescent.MatrixCoefficientCoproducts
import Mathlib.Logic.Equiv.Fin.Basic
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.Module

/-!
# `O_q(SU(2))` is the Tannaka coend of the fundamental representation

Take `V = R²` with basis `e₀, e₁` and the two duality morphisms of the fundamental
representation of `U_q(sl₂)`:

* the **cup** `𝟙 → V ⊗ V`, `1 ↦ e₀ ⊗ e₁ − q e₁ ⊗ e₀`;
* the **cap** `V ⊗ V → 𝟙`, `e₀ ⊗ e₁ ↦ 1`, `e₁ ⊗ e₀ ↦ −q`, `eᵢ ⊗ eᵢ ↦ 0`.

Both have the matrix of the `q`-antisymmetric form `ω = ((0, 1), (−q, 0))`. `fundData q` is
this intertwiner data. Once `q^{1/2}` is adjoined, the Kauffman bracket writes the braiding
`Ř` of the fundamental representation as a combination of `id` and `cup ∘ cap`. So the
duality morphisms carry the FRT data of `Ř`. This file uses the cup and cap directly and does
not formalise the Kauffman identity.

**Main result.** `coendEquiv : Coend (fundData q) ≃ₐ[R] OqSU2 R q`. Under it, the coend's
coproduct, which is a theorem about the coend rather than a definition, is the corpus's
`OqSU2.coprod` (`coendEquiv_comul`). So `OqSU2.coprod` is derived from the fibre functor
of the fundamental representation.

The proof is the observation that the eight intertwining equations of the cup and the cap
are exactly the seven defining relations of `O_q(SU(2))` (`intertwines_fund_iff`).

Generic commutative ring with `q : Rˣ`; no analysis; no axiom.
-/

set_option linter.unusedSectionVars false
set_option linter.unusedSimpArgs false

namespace QOU.Coproduct

open TensorProduct QOU.AlgebraicSubstrate QOU.AlgebraicSubstrate.OqSU2

noncomputable section

variable {R : Type*} [CommRing R] (q : Rˣ)

/-- The `q`-antisymmetric form `ω = ((0, 1), (−q, 0))`. -/
def qForm : Fin 2 → Fin 2 → R := ![![0, 1], ![-(q : R), 0]]

/-- The two duality morphisms of the fundamental representation. -/
inductive Duality
  | cup
  | cap

/-- **The FRT data of the fundamental representation**: the cup `𝟙 → V ⊗ V` and the cap
`V ⊗ V → 𝟙`, both with matrix `ω`. -/
def fundData : IntertwinerData.{0} R (Fin 2) where
  ι := Duality
  src f := match f with
    | .cup => 0
    | .cap => 2
  tgt f := match f with
    | .cup => 2
    | .cap => 0
  mat f := match f with
    | .cup => fun w _ => qForm q (w 0) (w 1)
    | .cap => fun _ w' => qForm q (w' 0) (w' 1)

section Sums

variable {M : Type*} [AddCommMonoid M]

theorem sum_fin_two_arrow {n : Type*} [Fintype n] [DecidableEq n] (f : (Fin 2 → n) → M) :
    ∑ v, f v = ∑ i, ∑ j, f ![i, j] := by
  rw [← (finTwoArrowEquiv n).symm.sum_comp, Fintype.sum_prod_type]
  rfl

theorem sum_fin_zero_arrow {n : Type*} [Fintype n] (f : (Fin 0 → n) → M) :
    ∑ v, f v = f Fin.elim0 := by
  rw [Fintype.sum_unique]
  exact congrArg f (Subsingleton.elim _ _)

end Sums

theorem tpow_two {A : Type*} [Semiring A] {n : Type*} (M : Matrix n n A) (v w : Fin 2 → n) :
    tpow M 2 v w = M (v 0) (w 0) * M (v 1) (w 1) := by
  simp [tpow, List.ofFn_succ]

/-- **The intertwining equations of the cup and the cap.** A matrix `M` intertwines the
fundamental data exactly when, for all `a b`,
`M a 0 M b 1 − q M a 1 M b 0 = ω a b` (cup) and `M 0 a M 1 b − q M 1 a M 0 b = ω a b` (cap). -/
theorem intertwines_fund_iff {A : Type*} [Ring A] [Algebra R A] (M : Matrix (Fin 2) (Fin 2) A) :
    Intertwines (fundData q) M ↔
      (∀ a b, M a 0 * M b 1 - (q : R) • (M a 1 * M b 0) = algebraMap R A (qForm q a b)) ∧
      (∀ a b, M 0 a * M 1 b - (q : R) • (M 1 a * M 0 b) = algebraMap R A (qForm q a b)) := by
  constructor
  · intro h
    refine ⟨fun a b => ?_, fun a b => ?_⟩
    · have := h .cup ![a, b] Fin.elim0
      simp only [fundData, sum_fin_two_arrow, sum_fin_zero_arrow, tpow_zero, tpow_two,
        Fin.sum_univ_two, Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.head_cons] at this
      rw [Algebra.algebraMap_eq_smul_one]
      simp only [qForm, Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.head_cons] at this ⊢
      linear_combination (norm := module) -this
    · have := h .cap Fin.elim0 ![a, b]
      simp only [fundData, sum_fin_two_arrow, sum_fin_zero_arrow, tpow_zero, tpow_two,
        Fin.sum_univ_two, Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.head_cons] at this
      rw [Algebra.algebraMap_eq_smul_one]
      simp only [qForm, Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.head_cons] at this ⊢
      linear_combination (norm := module) this
  · rintro ⟨hcup, hcap⟩ f w w'
    cases f
    · have := hcup ((show Fin 2 → Fin 2 from w) 0) ((show Fin 2 → Fin 2 from w) 1)
      simp only [fundData, sum_fin_two_arrow, sum_fin_zero_arrow, tpow_zero, tpow_two,
        Fin.sum_univ_two, Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.head_cons]
      rw [Algebra.algebraMap_eq_smul_one] at this
      simp only [qForm, Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.head_cons] at this ⊢
      linear_combination (norm := module) -this
    · have := hcap ((show Fin 2 → Fin 2 from w') 0) ((show Fin 2 → Fin 2 from w') 1)
      simp only [fundData, sum_fin_two_arrow, sum_fin_zero_arrow, tpow_zero, tpow_two,
        Fin.sum_univ_two, Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.head_cons]
      rw [Algebra.algebraMap_eq_smul_one] at this
      simp only [qForm, Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.head_cons] at this ⊢
      linear_combination (norm := module) this

/-- The eight intertwining equations are the seven relations of `O_q(SU(2))`. -/
theorem intertwines_fund_iff_quadruple {A : Type*} [Ring A] [Algebra R A]
    (M : Matrix (Fin 2) (Fin 2) A) :
    Intertwines (fundData q) M ↔ IsOqSU2Quadruple q (M 0 0) (M 0 1) (M 1 0) (M 1 1) := by
  rw [intertwines_fund_iff]
  constructor
  · rintro ⟨hcup, hcap⟩
    have c00 := hcup 0 0; have c01 := hcup 0 1; have c10 := hcup 1 0; have c11 := hcup 1 1
    have p00 := hcap 0 0; have p01 := hcap 0 1; have p10 := hcap 1 0; have p11 := hcap 1 1
    simp only [qForm, Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.head_cons, map_zero,
      map_one, map_neg, Algebra.algebraMap_eq_smul_one] at c00 c01 c10 c11 p00 p01 p10 p11
    have bg : M 0 1 * M 1 0 = M 1 0 * M 0 1 := by
      have h : (q : R) • (M 1 0 * M 0 1 - M 0 1 * M 1 0) = 0 := by
        rw [smul_sub]; linear_combination (norm := module) c01 - p01
      have h' := congrArg (fun x => (((q⁻¹ : Rˣ) : R)) • x) h
      simp only [smul_smul, Units.inv_mul, one_smul, smul_zero] at h'
      exact (sub_eq_zero.mp h').symm
    refine ⟨?_, ?_, ?_, ?_, bg, ?_, ?_⟩
    · linear_combination (norm := module) c00
    · linear_combination (norm := module) p00
    · linear_combination (norm := module) p11
    · linear_combination (norm := module) c11
    · linear_combination (norm := module) c01
    · -- δα = 1 + q⁻¹ βγ, from the cap equation `βγ − q δα = −q`
      have h := congrArg (fun x => (((q⁻¹ : Rˣ) : R)) • x) p10
      simp only [smul_sub, smul_smul, Units.inv_mul, one_smul, smul_neg] at h
      linear_combination (norm := module) -h
  · rintro ⟨hab, hag, hbd, hgd, hbg, hdl, hdr⟩
    have hdr' : M 0 1 * M 1 0 - (q : R) • (M 1 1 * M 0 0) = -((q : R) • (1 : A)) := by
      have h := congrArg (fun x => (q : R) • x) hdr
      simp only [smul_sub, smul_smul, Units.mul_inv, one_smul] at h
      linear_combination (norm := module) -h
    refine ⟨fun a b => ?_, fun a b => ?_⟩ <;> fin_cases a <;> fin_cases b <;>
      simp only [qForm, Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.head_cons, map_zero,
        map_one, map_neg, Algebra.algebraMap_eq_smul_one, Fin.zero_eta, Fin.mk_one, Fin.isValue]
    · linear_combination (norm := module) hab
    · linear_combination (norm := module) hdl
    · rw [← hbg]; linear_combination (norm := module) hdr'
    · linear_combination (norm := module) hgd
    · linear_combination (norm := module) hag
    · rw [← hbg]; linear_combination (norm := module) hdl
    · linear_combination (norm := module) hdr'
    · linear_combination (norm := module) hbd

/-! ## The isomorphism -/

theorem oqSU2_quadruple : IsOqSU2Quadruple (R := R) q (α q) (β q) (γ q) (δ q) :=
  ⟨rel_ab q, rel_ag q, rel_bd q, rel_gd q, rel_bg q, rel_det_left q, rel_det_right q⟩

theorem oqMatrix_intertwines : Intertwines (fundData q) (oqMatrix (R := R) q) := by
  rw [intertwines_fund_iff_quadruple]
  simpa [oqMatrix] using oqSU2_quadruple q

theorem coendMat_quadruple :
    IsOqSU2Quadruple q (coendMat (fundData q) 0 0) (coendMat (fundData q) 0 1)
      (coendMat (fundData q) 1 0) (coendMat (fundData q) 1 1) :=
  (intertwines_fund_iff_quadruple q _).1 (coendMat_intertwines _)

/-- `Coend → O_q(SU(2))`: the point given by `((α, β), (γ, δ))`. -/
def coendToOq : Coend (fundData q) →ₐ[R] OqSU2 R q :=
  liftPoint (oqMatrix q) (oqMatrix_intertwines q)

/-- `O_q(SU(2)) → Coend`: `α, β, γ, δ ↦ u₀₀, u₀₁, u₁₀, u₁₁`. -/
def oqToCoend : OqSU2 R q →ₐ[R] Coend (fundData q) :=
  liftQuadruple q _ _ _ _ (coendMat_quadruple q)

/-- **`O_q(SU(2))` is the Tannaka coend of the fundamental representation.** -/
def coendEquiv : Coend (fundData q) ≃ₐ[R] OqSU2 R q :=
  AlgEquiv.ofAlgHom (coendToOq q) (oqToCoend q)
    (algHom_ext (by simp [coendToOq, oqToCoend, oqMatrix])
      (by simp [coendToOq, oqToCoend, oqMatrix]) (by simp [coendToOq, oqToCoend, oqMatrix])
      (by simp [coendToOq, oqToCoend, oqMatrix]))
    (point_ext fun i j => by
      fin_cases i <;> fin_cases j <;> simp [coendToOq, oqToCoend, oqMatrix])

/-- **The coend's coproduct is `OqSU2.coprod`.** The coproduct of the coend is a theorem,
descended from the intertwining relations. Under `coendEquiv` it is the corpus's hand-built
`OqSU2.coprod`. -/
theorem coendEquiv_comul :
    (Algebra.TensorProduct.map (coendEquiv q).toAlgHom (coendEquiv q).toAlgHom).comp
        (coendComul (fundData q)) =
      (coprod q).comp (coendEquiv q).toAlgHom := by
  apply point_ext
  intro i j
  have h := (isMatrixCoproduct_iff (oqMatrix q) (coprod q)).1 (oqSU2_isMatrixCoproduct q) i j
  simp only [AlgHom.coe_comp, Function.comp_apply, coendComul_coendMat, map_sum,
    Algebra.TensorProduct.map_tmul]
  simp [coendEquiv, coendToOq, h]

end

end QOU.Coproduct
