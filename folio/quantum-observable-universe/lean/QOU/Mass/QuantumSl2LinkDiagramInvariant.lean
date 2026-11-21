import QOU.Mass.QuantumSl2LinkDiagram
import QOU.Mass.QuantumSl2CrossingSymmetry

/-!
# Reidemeister invariance of the coloured `U_q(sl₂)` diagram model

WIP
-/

namespace QOU.Mass.QuantumSl2.LinkDiagram

open Matrix
open QOU.MathlibExt.PL.Diagram
open QOU.Mass.QuantumSl2.MarkovTrace
open QOU.Mass.QuantumSl2.Markov (rCheckInv rCheck_mul_inv rCheckInv_mul rCheckMat_apply)

variable {𝕜 : Type*} [Field 𝕜]

/-! ### Reflection of the weights -/

section Reflection

variable (q : 𝕜) (d : ℕ)

theorem irrepE_rev (i j : Fin (d + 1)) : irrepE q d i.rev j.rev = irrepF q d i j := by
  simp only [irrepE, irrepF, Fin.val_rev]
  have := i.isLt; have := j.isLt
  by_cases h : (i : ℕ) = j + 1
  · rw [if_pos (by omega), if_pos h]; congr 1; omega
  · rw [if_neg (by omega), if_neg h]

theorem irrepE_pow_submatrix_rev (n : ℕ) :
    (irrepE q d ^ n).submatrix Fin.revPerm Fin.revPerm = irrepF q d ^ n := by
  induction n with
  | zero => simp [Matrix.submatrix_one_equiv]
  | succ n ih =>
    rw [pow_succ, pow_succ, ← ih, ← Matrix.submatrix_mul_equiv (e₂ := Fin.revPerm)]
    congr 1
    ext i j
    exact irrepE_rev q d i j

theorem irrepE_pow_rev (n : ℕ) (i j : Fin (d + 1)) :
    (irrepE q d ^ n) i.rev j.rev = (irrepF q d ^ n) i j := by
  rw [← irrepE_pow_submatrix_rev q d n]; rfl

theorem irrepF_pow_rev (n : ℕ) (i j : Fin (d + 1)) :
    (irrepF q d ^ n) i.rev j.rev = (irrepE q d ^ n) i j := by
  rw [← irrepE_pow_rev, Fin.rev_rev, Fin.rev_rev]

theorem wt_rev (r : Fin (d + 1)) : wt d r.rev = -wt d r := by
  unfold wt; rw [Fin.val_rev]; have := r.isLt; push_cast [show (r : ℕ) ≤ d by omega]; omega

end Reflection

/-- The reflection `(a, b) ↦ (d − b, d − a)` of a pair of weights. -/
def flipE (d : ℕ) : (Fin (d + 1) × Fin (d + 1)) ≃ (Fin (d + 1) × Fin (d + 1)) where
  toFun x := (x.2.rev, x.1.rev)
  invFun x := (x.2.rev, x.1.rev)
  left_inv x := by simp
  right_inv x := by simp

theorem flipE_apply (d : ℕ) (x : Fin (d + 1) × Fin (d + 1)) : flipE d x = (x.2.rev, x.1.rev) := rfl

variable (s : 𝕜) (hs : s ≠ 0) (d : ℕ)

/-- **The braiding is invariant under the reflection** `v_a ⊗ v_b ↦ v_{d−b} ⊗ v_{d−a}`. -/
theorem rCheckMat_flip (y x : Fin (d + 1) × Fin (d + 1)) :
    rCheckMat s hs d d (flipE d y) (flipE d x) = rCheckMat s hs d d y x := by
  rw [rCheckMat_apply, rCheckMat_apply]
  obtain ⟨y1, y2⟩ := y
  obtain ⟨x1, x2⟩ := x
  simp only [flipE_apply, wt_rev, Prod.swap]
  congr 1
  · ring_nf
  · simp only [Rep.rSum, Matrix.sum_apply, Matrix.smul_apply, kroneckerMap_apply, smul_eq_mul]
    refine Finset.sum_congr rfl fun n _ => ?_
    change rcoef s n * ((irrepE (s ^ 2) d ^ n) y1.rev x2.rev * (irrepF (s ^ 2) d ^ n) y2.rev x1.rev)
      = rcoef s n * ((irrepE (s ^ 2) d ^ n) y2 x1 * (irrepF (s ^ 2) d ^ n) y1 x2)
    rw [irrepE_pow_rev, irrepF_pow_rev, mul_comm ((irrepF _ _ ^ n) _ _)]

theorem rCheckMat_submatrix_flip :
    (rCheckMat s hs d d).submatrix (flipE d) (flipE d) = rCheckMat s hs d d := by
  ext y x; exact rCheckMat_flip s hs d y x

theorem rCheckInv_submatrix_flip :
    (rCheckInv s hs d).submatrix (flipE d) (flipE d) = rCheckInv s hs d := by
  have h : (rCheckInv s hs d).submatrix (flipE d) (flipE d) * rCheckMat s hs d d = 1 := by
    conv_lhs => rw [← rCheckMat_submatrix_flip s hs d]
    rw [Matrix.submatrix_mul_equiv, rCheckInv_mul, Matrix.submatrix_one_equiv]
  calc (rCheckInv s hs d).submatrix (flipE d) (flipE d)
      = (rCheckInv s hs d).submatrix (flipE d) (flipE d) * (rCheckMat s hs d d * rCheckInv s hs d) := by
        rw [rCheck_mul_inv, Matrix.mul_one]
    _ = rCheckInv s hs d := by rw [← Matrix.mul_assoc, h, Matrix.one_mul]

theorem rCheckInv_flip (y x : Fin (d + 1) × Fin (d + 1)) :
    rCheckInv s hs d (flipE d y) (flipE d x) = rCheckInv s hs d y x := by
  conv_rhs => rw [← rCheckInv_submatrix_flip s hs d]
  rfl

theorem qWt_rev (r : Fin (d + 1)) : qWt s d r.rev = (qWt s d r)⁻¹ := by
  simp only [qWt, wt_rev, mul_neg, zpow_neg]

variable (hq2 : s ^ 2 - (s ^ 2)⁻¹ ≠ 0) (hint : ∀ k, 0 < k → k ≤ 2 * d → qint (s ^ 2) k ≠ 0)

include hq2 hint in
/-- **R1 with the loop traced on the left**, from the right-traced R1 and the reflection. -/
theorem rModel_r1_left (b : Bool) (x y : Fin (d + 1)) :
    ∑ i, kinkW (rModel s hs d) b b x y i * ((((rModel s hs d).K i ^ kinkTurn b b : 𝕜ˣ)) : 𝕜) =
      ((thetaU s hs d ^ signZ b : 𝕜ˣ) : 𝕜) * if x = y then 1 else 0 := by
  have h := rModel_r1_right s hs d hq2 hint b x.rev y.rev
  simp only [Fin.rev_inj] at h
  rw [← h, ← Equiv.sum_comp Fin.revPerm]
  refine Finset.sum_congr rfl fun i _ => ?_
  cases b
  · have hf := rCheckInv_flip s hs d (i.rev, x) (i.rev, y)
    simp only [flipE_apply, Fin.rev_rev] at hf
    simp only [Fin.revPerm_apply, kinkW_true, kinkW_false, Bool.not_false, kinkTurn, if_true,
      Bool.true_eq_false, if_false, zpow_one, zpow_neg_one, Units.val_inv_eq_inv_val, rModel_K,
      rModel_X_false, qWt_rev, inv_inv]
    rw [← hf]
  · have hf := rCheckMat_flip s hs d (i.rev, x) (i.rev, y)
    simp only [flipE_apply, Fin.rev_rev] at hf
    simp only [Fin.revPerm_apply, kinkW_true, kinkW_false, Bool.not_true, kinkTurn, if_true,
      Bool.false_eq_true, if_false, zpow_one, zpow_neg_one, Units.val_inv_eq_inv_val, rModel_K,
      rModel_X_true, qWt_rev, inv_inv]
    rw [← hf]

end QOU.Mass.QuantumSl2.LinkDiagram
