import QOU.Mass.QuantumSl2LoopLemma

/-!
# The flype

The Whitehead link's braid `γ = σ₂σ₁⁻²σ₂σ₁⁻¹` closes to the same link as the belt word with the
mirror monodromy swapped for the monodromy and one extra crossing. Bent into the plane, this is

    nat((K ⊗ K) X(Ř⁻²)) = (−1)^m s^{m(m+2)} · Ř · nat((K ⊗ K) X(Ř²))     (`natOp_flype`),

where `X(Y)` closes the third strand of `Ř₂ (Y ⊗ 1) Ř₂` (`hookOp`). The proof combines the loop
lemma (`natOp_hookOp`), the bending of a graded operator (`natOp_kk_graded`), the clasp flip
(`claspBar_eq_rCheck_mul_clasp`) and the commuting of the two clasps (`clasp_comm_claspBar`).

This is a step of the Whitehead link trace (issue #7912).

-- Ref: [kassel1995] Kassel, "Quantum Groups", Ch. XIV
-- Ref: [kauffman1987] Kauffman, "State models and the Jones polynomial", Topology 26 (1987)
-/

namespace QOU.Mass.QuantumSl2

open Matrix

variable {𝕜 : Type*} [Field 𝕜]

theorem wt_rev (m : ℕ) (a : Fin (m + 1)) : wt m (a.rev : ℕ) = -wt m a := by
  have h : (a.rev : ℕ) = m - a := by rw [Fin.val_rev]; omega
  have ha : (a : ℕ) ≤ m := by omega
  unfold wt; rw [h, Nat.cast_sub ha]; ring

section Bend

variable (q : 𝕜) (hq : q ≠ 0) (m : ℕ) (hint : ∀ i, 0 < i → i ≤ m → qint q i ≠ 0)

include hq hint in
/-- **Bending a graded operator.** If `Y` preserves `p + r`, then
`nat((K ⊗ K) Y) = rot Y · (K⁻¹ ⊗ K)`. -/
theorem natOp_kk_graded (Y : Matrix (Fin (m + 1) × Fin (m + 1)) (Fin (m + 1) × Fin (m + 1)) 𝕜)
    (hY : ∀ x y : Fin (m + 1) × Fin (m + 1), (x.1 : ℕ) + x.2 ≠ y.1 + y.2 → Y x y = 0) :
    natOp q m (kk q m * Y) = rotOp q m Y
      * diagonal (fun x : Fin (m + 1) × Fin (m + 1) => (q ^ wt m x.1)⁻¹ * q ^ wt m x.2) := by
  ext ⟨y1, y2⟩ ⟨x1, x2⟩
  rw [natOp_eq_rotOp q hq m hint, mul_diagonal, rotOp_apply, rotOp_apply, Finset.sum_mul]
  refine Finset.sum_congr rfl fun β _ => ?_
  rw [Finset.sum_mul]
  refine Finset.sum_congr rfl fun γ _ => ?_
  simp only [kk, diagonal_mul, mul_diagonal]
  by_cases hβ : β = x1.rev
  swap
  · rw [capVec_eq_zero q m hβ]; ring
  by_cases hγ : γ = y2.rev
  swap
  · rw [cupVec_eq_zero q m hγ]; ring
  subst hβ hγ
  by_cases hg : ((x1.rev : Fin (m + 1)) : ℕ) + y1 = x2 + (y2.rev : Fin (m + 1))
  swap
  · rw [hY _ _ hg]; ring
  have hw : wt m y1 + wt m y2 = wt m x1 + wt m x2 := by
    rw [Fin.val_rev, Fin.val_rev] at hg
    unfold wt
    have h1 : (x1 : ℕ) ≤ m := by omega
    have h2 : (y2 : ℕ) ≤ m := by omega
    omega
  have hz : q ^ wt m y1 * q ^ wt m y2 = q ^ wt m x1 * q ^ wt m x2 := by
    rw [← zpow_add₀ hq, ← zpow_add₀ hq, hw]
  have hA : q ^ wt m x1 ≠ 0 := zpow_ne_zero _ hq
  have hC : q ^ wt m y2 ≠ 0 := zpow_ne_zero _ hq
  rw [wt_rev, wt_rev, zpow_neg, zpow_neg, inv_inv]
  field_simp
  linear_combination capVec q m (x1, x1.rev) * Y (x1.rev, y1) (x2, y2.rev)
    * cupVec q m (y2.rev, y2) * hz

end Bend

section Flype

variable (s : 𝕜) (hs : s ≠ 0) (m : ℕ) (hq2 : s ^ 2 - (s ^ 2)⁻¹ ≠ 0)
  (hint : ∀ i, 0 < i → i ≤ 2 * m → qint (s ^ 2) i ≠ 0)

include hq2 hint in
/-- **The two clasps commute**: both are scalar on every string. -/
theorem clasp_comm_claspBar : clasp s hs m * claspBar s hs m = claspBar s hs m * clasp s hs m := by
  have hq : s ^ 2 ≠ 0 := pow_ne_zero 2 hs
  apply Matrix.toLin'.injective
  refine (strBasis (s ^ 2) hq m hq2 hint).ext fun x => ?_
  rw [strBasis_apply, Matrix.toLin'_apply, Matrix.toLin'_apply, ← mulVec_mulVec, ← mulVec_mulVec]
  simp only [clasp_strVec s hs hq2 m hint x, claspBar_strVec s hs m hq2 hint x, mulVec_smul,
    smul_smul]
  rw [mul_comm]

include hq2 in
/-- The quarter-turned crossing squared is the inverse monodromy. -/
theorem rotOp_rCheck_sq (hint' : ∀ i, 0 < i → i ≤ m → qint (s ^ 2) i ≠ 0) :
    rotOp (s ^ 2) m (rCheckMat s hs m m) * rotOp (s ^ 2) m (rCheckMat s hs m m)
      = (mono s hs m m)⁻¹ := by
  have h := rotOp_rCheck_mul_rCheck s hs m hq2 hint'
  refine (Matrix.inv_eq_left_inv ?_).symm
  unfold mono
  rw [mul_assoc, ← mul_assoc (rotOp (s ^ 2) m (rCheckMat s hs m m)) (rCheckMat s hs m m), h,
    one_mul, h]

include hq2 hint in
/-- **The flype.** `nat((K⊗K) X(Ř⁻²)) = (−1)^m s^{m(m+2)} Ř · nat((K⊗K) X(Ř²))`. -/
theorem natOp_flype :
    natOp (s ^ 2) m (kk (s ^ 2) m * hookOp (s ^ 2) m (rCheckMat s hs m m)
        (rotOp (s ^ 2) m (rCheckMat s hs m m) * rotOp (s ^ 2) m (rCheckMat s hs m m)))
      = ((-1) ^ m * s ^ (m * (m + 2))) • (rCheckMat s hs m m
          * natOp (s ^ 2) m (kk (s ^ 2) m * hookOp (s ^ 2) m (rCheckMat s hs m m)
            (mono s hs m m))) := by
  have hq : s ^ 2 ≠ 0 := pow_ne_zero 2 hs
  have hm : ∀ i, 0 < i → i ≤ m → qint (s ^ 2) i ≠ 0 := fun i h1 h2 => hint i h1 (by omega)
  have hsq := rotOp_rCheck_sq s hs m hq2 hm
  have hbar : claspBar s hs m = rotOp (s ^ 2) m (mono s hs m m)⁻¹ :=
    claspBar_eq s hs m hq2 hint
  have hcl : clasp s hs m = rotOp (s ^ 2) m (mono s hs m m) := rfl
  set T := diagonal (fun x : Fin (m + 1) × Fin (m + 1) => ((s ^ 2) ^ wt m x.1)⁻¹ * (s ^ 2) ^ wt m x.2)
  have hNbar : natOp (s ^ 2) m (kk (s ^ 2) m * (mono s hs m m)⁻¹) = claspBar s hs m * T := by
    rw [natOp_kk_graded (s ^ 2) hq m hm, hbar]
    intro x y h
    rw [monoBar_eq_inv s hs m hq2 hint]
    exact monoBar_grade s hs m x y h
  have hN : natOp (s ^ 2) m (kk (s ^ 2) m * mono s hs m m) = clasp s hs m * T := by
    rw [natOp_kk_graded (s ^ 2) hq m hm, hcl]
    exact fun x y h => mono_grade s hs m m x y h
  have hL := natOp_hookOp s hs m hq2 hm
    (rotOp (s ^ 2) m (rCheckMat s hs m m) * rotOp (s ^ 2) m (rCheckMat s hs m m))
  have hR := natOp_hookOp s hs m hq2 hm (mono s hs m m)
  rw [hsq] at hL hR ⊢
  rw [hL, hR, hNbar, hN, ← hbar]
  nth_rewrite 1 [claspBar_eq_rCheck_mul_clasp s hs hq2 m hint]
  simp only [smul_mul_assoc, mul_smul_comm, smul_smul, mul_assoc]
  rw [← mul_assoc (clasp s hs m), clasp_comm_claspBar s hs m hq2 hint, mul_assoc]
  congr 1
  ring

end Flype

end QOU.Mass.QuantumSl2
