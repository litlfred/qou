import QOU.KZ.Drinfeld.Braiding
import QOU.KZ.Drinfeld.Natural
import Mathlib.Analysis.SpecialFunctions.Complex.Log

/-!
# The braiding of `D_ℏ` on `V ⊗ V`

Split out of `RibbonDH` so that `Duals` can use it. With `s = e^{iπℏ/2}`, `t = e^{−3iπℏ/2}` and
`q = e^{iπℏ}`, the braiding matrix is `β_{V,V} = s·P₊ − t·P₋` (`βmat_VV`), with `P₊`, `P₋` the
projections onto `Sym²V` and `Λ²V`. Also here: the scaled Hecke relation `hecke_mat`, the
inequalities `q² ≠ 1` (`qV_sub_inv_ne_zero`) and `s ≠ −t` (`sV_add_tV_ne_zero`) for
transcendental `ℏ`, and the failure of the unscaled Hecke relation (`not_hecke_unscaled`).
Nothing here depends on the associator. Sorry-free.

-- Ref: [leitner2026] beans/defs/qou-zoyv (stages S5, S6)
-/

noncomputable section

namespace QOU.KZ.Drinfeld

open CategoryTheory MonoidalCategory Finset QOU.KZ.FuchsianFormal QOU.KZ.BlockResidues Obj

attribute [local instance] Matrix.linftyOpNormedRing Matrix.linftyOpNormedAlgebra

section Annihilate

variable {m L : Type*} [Fintype L] [DecidableEq L]

/-- If `A * D = 0` then `A * exp D = A`. -/
theorem mul_exp_of_mul_eq_zero (A : Matrix m (L → Fin 2) ℂ) (D : EndL L) (h : A * D = 0) :
    A * NormedSpace.exp ℂ D = A := by
  have hpow : ∀ n : ℕ, A * D ^ (n + 1) = 0 := fun n => by
    rw [pow_succ', ← Matrix.mul_assoc, h, Matrix.zero_mul]
  let g : EndL L →+ Matrix m (L → Fin 2) ℂ :=
    { toFun := fun M => A * M, map_zero' := Matrix.mul_zero A, map_add' := Matrix.mul_add A }
  have hg : Continuous g := continuous_const.matrix_mul continuous_id
  have hs := ((NormedSpace.expSeries_summable' (𝕂 := ℂ) D).hasSum.map g hg).tsum_eq
  rw [NormedSpace.exp_eq_tsum (𝕂 := ℂ)]
  show g _ = A
  rw [← hs, tsum_eq_single 0]
  · simp [g]
  · intro n hn
    obtain ⟨k, rfl⟩ := Nat.exists_eq_succ_of_ne_zero hn
    simp [g, Matrix.mul_smul, hpow k]

/-- If `A * X = A * Y` with `X`, `Y` commuting, then `A * expi X = A * expi Y`. -/
theorem mul_expi_congr (A : Matrix m (L → Fin 2) ℂ) {X Y : EndL L} (hXY : Commute X Y)
    (h : A * X = A * Y) : A * expi X = A * expi Y := by
  have hX : X = (X - Y) + Y := by abel
  have hc : Commute (X - Y) Y := (hXY.sub_left (Commute.refl Y))
  rw [hX, expi_add hc, ← Matrix.mul_assoc]
  congr 1
  apply mul_exp_of_mul_eq_zero
  rw [Matrix.mul_smul, Matrix.mul_sub, h, sub_self, smul_zero]

end Annihilate

/-! ### The braiding on `V ⊗ V` -/

section Hecke

/-- The flip of the two legs of `V ⊗ V`. -/
abbrev PV : EndL (Leaves (tensor V V)) := flipL ℂ 2 (Sum.inl ()) (Sum.inr ())

theorem PV_mul_PV : PV * PV = 1 := by
  rw [PV, flipL, permL_mul, Equiv.swap_mul_self]
  ext y x
  simp [permL, permMat, Matrix.one_apply, eq_comm]

theorem reidx_swapLegs_VV : reidx (swapLegs V V) = PV := by
  have key : ∀ x y : Idx (tensor V V),
      (x = y ∘ swapLegs V V) ↔ (x ∘ Equiv.swap (Sum.inl ()) (Sum.inr ()) = y) := by
    intro x y
    constructor
    · rintro rfl; funext k; rcases k with ⟨⟩ | ⟨⟩ <;> simp [swapLegs]
    · rintro rfl; funext k; rcases k with ⟨⟩ | ⟨⟩ <;> simp [swapLegs]
  ext y x
  simp only [reidx, PV, flipL, permL, permMat, Matrix.of_apply, key]

theorem bL_VV : bL V V = {Sum.inl ()} := by
  ext k; rcases k with ⟨⟩ | ⟨⟩ <;> simp [bL]

theorem bR_VV : bR V V = {Sum.inr ()} := by
  ext k; rcases k with ⟨⟩ | ⟨⟩ <;> simp [bR]

/-- On `V ⊗ V` the `sl₂` block Casimir is `t = P − ½`. -/
theorem tsl_VV : tsl (bL V V) (bR V V) = PV - (1 / 2 : ℂ) • 1 := by
  have h := tB_eq_tsl (disj_bLR V V)
  rw [bL_VV, bR_VV] at h ⊢
  rw [tB, sum_singleton, sum_singleton, card_singleton] at h
  rw [eq_sub_of_add_eq h.symm, card_singleton]; norm_num

/-- `exp(iπ r·1) = e^{iπr}·1`. -/
theorem expi_smul_one {L : Type*} [Fintype L] [DecidableEq L] (r : ℂ) :
    expi (r • (1 : EndL L)) = Complex.exp (Real.pi * Complex.I * r) • 1 := by
  unfold expi
  rw [smul_smul, ← Algebra.algebraMap_eq_smul_one, ← NormedSpace.algebraMap_exp_comm,
    ← Complex.exp_eq_exp_ℂ, Algebra.algebraMap_eq_smul_one]

/-- The two spectral projections of the flip. -/
def Pp : EndL (Leaves (tensor V V)) := (1 / 2 : ℂ) • (1 + PV)
def Pm : EndL (Leaves (tensor V V)) := (1 / 2 : ℂ) • (1 - PV)

theorem Pp_mul_PV : Pp * PV = Pp := by
  rw [Pp, Matrix.smul_mul, Matrix.add_mul, PV_mul_PV, Matrix.one_mul, add_comm]

theorem Pm_mul_PV : Pm * PV = -Pm := by
  rw [Pm, Matrix.smul_mul, Matrix.sub_mul, PV_mul_PV, Matrix.one_mul, ← smul_neg, neg_sub]

theorem Pp_add_Pm : Pp + Pm = 1 := by
  rw [Pp, Pm, ← smul_add]; module

theorem PV_eq : PV = Pp - Pm := by
  rw [Pp, Pm]; module

theorem Pp_mul_Pp : Pp * Pp = Pp := by
  show Pp * ((1 / 2 : ℂ) • (1 + PV)) = Pp
  rw [Matrix.mul_smul, Matrix.mul_add, Matrix.mul_one, Pp_mul_PV, ← two_smul ℂ Pp, smul_smul]
  norm_num

theorem Pm_mul_Pm : Pm * Pm = Pm := by
  show Pm * ((1 / 2 : ℂ) • (1 - PV)) = Pm
  rw [Matrix.mul_smul, Matrix.mul_sub, Matrix.mul_one, Pm_mul_PV, sub_neg_eq_add, ← two_smul ℂ Pm,
    smul_smul]
  norm_num

theorem Pp_mul_Pm : Pp * Pm = 0 := by
  conv_lhs => rw [show (Pm : EndL _) = (1 / 2 : ℂ) • (1 - PV) from rfl]
  rw [Matrix.mul_smul, Matrix.mul_sub, Matrix.mul_one, Pp_mul_PV, sub_self, smul_zero]

theorem Pm_mul_Pp : Pm * Pp = 0 := by
  conv_lhs => rw [show (Pp : EndL _) = (1 / 2 : ℂ) • (1 + PV) from rfl]
  rw [Matrix.mul_smul, Matrix.mul_add, Matrix.mul_one, Pm_mul_PV, add_neg_cancel, smul_zero]

variable (c : ℂ)

/-- `e^{iπℏ/2}`, the eigenvalue of `β_{V,V}` on `Sym² V`. -/
def sV : ℂ := Complex.exp (Real.pi * Complex.I * (c / 2))
/-- `e^{−3iπℏ/2}`, minus the eigenvalue of `β_{V,V}` on `Λ² V`. -/
def tV : ℂ := Complex.exp (Real.pi * Complex.I * (-(3 * c / 2)))
/-- `q = e^{iπℏ}`. -/
def qV : ℂ := Complex.exp (Real.pi * Complex.I * c)

theorem Pp_mul_expi : Pp * expi (c • tsl (bL V V) (bR V V)) = sV c • Pp := by
  have h : Pp * (c • tsl (bL V V) (bR V V)) = Pp * ((c / 2) • (1 : EndL _)) := by
    rw [tsl_VV, Matrix.mul_smul, Matrix.mul_sub, Pp_mul_PV, Matrix.mul_smul, Matrix.mul_one,
      Matrix.mul_smul, Matrix.mul_one]
    module
  rw [mul_expi_congr Pp (commute_scalar (c / 2) _).symm h, expi_smul_one, Matrix.mul_smul,
    Matrix.mul_one]
  rfl

theorem Pm_mul_expi : Pm * expi (c • tsl (bL V V) (bR V V)) = tV c • Pm := by
  have h : Pm * (c • tsl (bL V V) (bR V V)) = Pm * ((-(3 * c / 2)) • (1 : EndL _)) := by
    rw [tsl_VV, Matrix.mul_smul, Matrix.mul_sub, Pm_mul_PV, Matrix.mul_smul, Matrix.mul_one,
      Matrix.mul_smul, Matrix.mul_one]
    module
  rw [mul_expi_congr Pm (commute_scalar (-(3 * c / 2)) _).symm h, expi_smul_one, Matrix.mul_smul,
    Matrix.mul_one]
  rfl

theorem βmat_VV : βmat c V V = sV c • Pp - tV c • Pm := by
  rw [βmat, reidx_swapLegs_VV, PV_eq, Matrix.sub_mul, Pp_mul_expi, Pm_mul_expi]

theorem sV_ne_zero : sV c ≠ 0 := Complex.exp_ne_zero _
theorem tV_ne_zero : tV c ≠ 0 := Complex.exp_ne_zero _

theorem βinv_VV : βinv c V V = (sV c)⁻¹ • Pp - (tV c)⁻¹ • Pm := by
  have hs := sV_ne_zero c
  have ht := tV_ne_zero c
  have h1 : βmat c V V * ((sV c)⁻¹ • Pp - (tV c)⁻¹ • Pm) = 1 := by
    rw [βmat_VV]
    simp only [Matrix.sub_mul, Matrix.mul_sub, Matrix.smul_mul, Matrix.mul_smul]
    rw [Pp_mul_Pp, Pm_mul_Pm, Pp_mul_Pm, Pm_mul_Pp]
    conv_rhs => rw [← Pp_add_Pm]
    match_scalars <;> field_simp
  calc βinv c V V = βinv c V V * (βmat c V V * ((sV c)⁻¹ • Pp - (tV c)⁻¹ • Pm)) := by
        rw [h1, Matrix.mul_one]
    _ = _ := by rw [← Matrix.mul_assoc, βinv_mul_βmat, Matrix.one_mul]

theorem sV_mul_sV : sV c * sV c = qV c := by
  unfold sV qV; rw [← Complex.exp_add]; ring_nf

theorem sV_mul_tV : sV c * tV c = (qV c)⁻¹ := by
  unfold sV tV qV; rw [← Complex.exp_add, ← Complex.exp_neg]; ring_nf

/-- **The Hecke skein relation in `D_ℏ`** (matrix form): with `s = e^{iπℏ/2}`, `q = e^{iπℏ}`,
`s·β − s⁻¹·β⁻¹ = (q − q⁻¹)·1` on `V ⊗ V`. -/
theorem tV_eq : tV c = ((sV c) ^ 3)⁻¹ := by
  unfold tV sV; rw [← Complex.exp_nat_mul, ← Complex.exp_neg]; ring_nf

theorem qV_eq : qV c = sV c ^ 2 := by rw [sq, sV_mul_sV]

/-- **The Hecke skein relation in `D_ℏ`** (matrix form): with `s = e^{iπℏ/2}`, `q = e^{iπℏ}`,
`s·β − s⁻¹·β⁻¹ = (q − q⁻¹)·1` on `V ⊗ V`. -/
theorem hecke_mat :
    sV c • βmat c V V - (sV c)⁻¹ • βinv c V V = (qV c - (qV c)⁻¹) • 1 := by
  have hs := sV_ne_zero c
  rw [βmat_VV, βinv_VV, tV_eq, qV_eq]
  conv_rhs => rw [← Pp_add_Pm]
  match_scalars <;> field_simp <;> ring

end Hecke

section Spectral

variable (c : ℂ)

theorem qV_sub_inv_ne_zero (hc : Transcendental ℚ c) : qV c - (qV c)⁻¹ ≠ 0 := by
  intro h
  have hq0 : qV c ≠ 0 := Complex.exp_ne_zero _
  have h2 : qV c * qV c = 1 := by
    have := congrArg (qV c * ·) h
    simp only [mul_sub, mul_inv_cancel₀ hq0, mul_zero] at this
    exact sub_eq_zero.1 this
  have he : Complex.exp (c * (2 * Real.pi * Complex.I)) = 1 := by
    rw [← h2]; unfold qV; rw [← Complex.exp_add]; ring_nf
  obtain ⟨n, hn⟩ := Complex.exp_eq_one_iff.1 he
  have h2pi : (2 * Real.pi * Complex.I : ℂ) ≠ 0 := by
    simp [Real.pi_ne_zero, Complex.I_ne_zero]
  have hcn : c = n := mul_right_cancel₀ h2pi hn
  exact hc (hcn ▸ isAlgebraic_int (R := ℚ) (A := ℂ) n)

/-- **`s ≠ −t`** for transcendental `ℏ`: the two eigenvalues `s` and `−t` of `β_{V,V}` differ.
Otherwise `s⁴ = −1`, so `e^{4iπℏ} = 1` and `ℏ` would be rational. -/
theorem sV_add_tV_ne_zero (hc : Transcendental ℚ c) : sV c + tV c ≠ 0 := by
  intro e
  have hs := sV_ne_zero c
  rw [tV_eq] at e
  have h8 : sV c ^ 8 = 1 := by
    field_simp at e
    linear_combination (sV c ^ 4 - 1) * e
  have he : Complex.exp ((2 * c) * (2 * Real.pi * Complex.I)) = 1 := by
    rw [← h8]; unfold sV; rw [← Complex.exp_nat_mul]; ring_nf
  obtain ⟨n, hn⟩ := Complex.exp_eq_one_iff.1 he
  have h2pi : (2 * Real.pi * Complex.I : ℂ) ≠ 0 := by
    simp [Real.pi_ne_zero, Complex.I_ne_zero]
  have hcn : c = ((n / 2 : ℚ) : ℂ) := by
    have := mul_right_cancel₀ h2pi hn
    push_cast
    linear_combination this / 2
  exact hc (hcn ▸ isAlgebraic_algebraMap (R := ℚ) (A := ℂ) ((n : ℚ) / 2))

end Spectral

/-! ### The unscaled Hecke relation fails in the `sl₂` normalisation

`ribbon_hecke_qDim_eq_qint_two` assumes `β − β⁻¹ = (q − q⁻¹)·𝟙`. In `D_ℏ` the braiding is built
from the `sl₂` Casimir `t = P − ½` (forced by naturality, see `Braiding`), so its eigenvalues are
`s = e^{iπℏ/2}` on `Sym²V` and `−s⁻³` on `Λ²V`; `β − β⁻¹` is then **not** a scalar for any
transcendental `ℏ`. Only the rescaled braiding `s·β` satisfies the Hecke relation (`hecke_DH`),
which is why `ribbon_hecke_dimension_scaled` is used. -/

section Unscaled

theorem Pp_ne_zero : Pp ≠ 0 := by
  intro h
  have := congrFun (congrFun h (fun _ => 0)) (fun _ => 0)
  have hc : (fun _ : Leaves (tensor V V) => (0 : Fin 2)) ∘ ⇑(Equiv.swap (Sum.inl ()) (Sum.inr ()))
      = fun _ => 0 := rfl
  simp [Pp, PV, permL, permMat] at this
  rw [if_pos hc] at this
  norm_num at this

theorem Pm_ne_zero : Pm ≠ 0 := by
  intro h
  set y : Idx (tensor V V) := Sum.elim (fun _ => 0) (fun _ => 1)
  have hy : ¬ (y ∘ Equiv.swap (Sum.inl ()) (Sum.inr ()) = y) := by
    intro e
    have := congrFun e (Sum.inl ())
    simp [y] at this
  have := congrFun (congrFun h y) y
  simp [Pm, PV, permL, permMat, hy] at this

theorem not_hecke_unscaled (c : ℂ) (hc : Transcendental ℚ c) :
    ¬ ∃ r : ℂ, βmat c V V - βinv c V V = r • 1 := by
  rintro ⟨r, hr⟩
  have hs := sV_ne_zero c
  rw [βmat_VV, βinv_VV, ← Pp_add_Pm] at hr
  have hp := congrArg (Pp * ·) hr
  have hm := congrArg (Pm * ·) hr
  simp only [Matrix.mul_sub, Matrix.mul_add, Matrix.mul_smul] at hp hm
  rw [Pp_mul_Pp, Pp_mul_Pm] at hp
  rw [Pm_mul_Pp, Pm_mul_Pm] at hm
  have e1 : (sV c - (sV c)⁻¹) • Pp = r • Pp := by
    rw [show r • Pp = r • (Pp + 0) by rw [add_zero], ← hp]; module
  have e2 : ((tV c)⁻¹ - tV c) • Pm = r • Pm := by
    rw [show r • Pm = r • (0 + Pm) by rw [zero_add], ← hm]; module
  have f1 := smul_left_injective ℂ Pp_ne_zero e1
  have f2 := smul_left_injective ℂ Pm_ne_zero e2
  have e : sV c - (sV c)⁻¹ = (tV c)⁻¹ - tV c := f1.trans f2.symm
  rw [tV_eq, inv_inv] at e
  have h8 : sV c ^ 8 = 1 := by
    field_simp at e
    linear_combination (exp := 1) (-(sV c ^ 2 + 1)) * e
  have he : Complex.exp ((2 * c) * (2 * Real.pi * Complex.I)) = 1 := by
    rw [← h8]; unfold sV; rw [← Complex.exp_nat_mul]; ring_nf
  obtain ⟨n, hn⟩ := Complex.exp_eq_one_iff.1 he
  have h2pi : (2 * Real.pi * Complex.I : ℂ) ≠ 0 := by
    simp [Real.pi_ne_zero, Complex.I_ne_zero]
  have hcn : c = ((n / 2 : ℚ) : ℂ) := by
    have := mul_right_cancel₀ h2pi hn
    push_cast
    linear_combination this / 2
  exact hc (hcn ▸ isAlgebraic_algebraMap (R := ℚ) (A := ℂ) ((n : ℚ) / 2))

end Unscaled

end QOU.KZ.Drinfeld
