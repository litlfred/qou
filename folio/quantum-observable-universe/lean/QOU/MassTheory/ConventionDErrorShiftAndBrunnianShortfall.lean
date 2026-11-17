import Mathlib.Tactic

/-!
# Convention-D Error Shift and Cluster Shortfall Ratio Divergence (`qou-04cj`, `qou-2vut`)

This module formalizes two structural results in the nuclear binding sector:

1. **Convention-D Parameter Doubling and Underbinding Error Shift (`qou-04cj`)**:
   Under the square map $q_D = q_C^2$, the skein difference parameter satisfies
   $q_C^2 - q_C^{-2} = (q_C - q_C^{-1})(q_C + q_C^{-1})$ and the deformation factor
   satisfies $1 - q_C^{-2} = (1 - q_C^{-1})(1 + q_C^{-1})$. Whenever two binding
   predictions satisfy $0 < B_D < B_C < B_{\mathrm{target}}$, migrating from $B_C$ to
   $B_D$ strictly increases the absolute shortfall $|B - B_{\mathrm{target}}|$ by
   $B_C - B_D > 0$ and the relative shortfall by $(B_C - B_D) / B_{\mathrm{target}} > 0$.

2. **Cluster Shortfall Ratio Divergence and Multi-Term Closure (`qou-2vut`)**:
   When the $A = 3$ and $A = 4$ cluster shortfall ratios $r_3 = t_3 / b_3 = 1.585$
   and $r_4 = t_4 / b_4 = 78.8$ differ ($r_4 / r_3 = 15760 / 317 > 49$), no single
   constant multiplier $c$ can simultaneously satisfy $c \cdot b_3 = t_3$ and
   $c \cdot b_4 = t_4$. In a two-term additive closure $c \cdot b_A + d_A = t_A$
   anchored at $d_3 = 0$, the required $A = 4$ residual term is uniquely
   $d_4 = t_4 - (t_3 / b_3) b_4 > 0$.
-/

namespace QOU.MassTheory.ConventionDErrorShiftAndBrunnianShortfall

/-- Skein difference parameter $q - q^{-1}$ at scale parameter $q$. -/
noncomputable def skeinDiffParam (q : ℝ) : ℝ :=
  q - 1 / q

/-- Deformation factor $1 - q^{-1}$ at scale parameter $q$. -/
noncomputable def deformFactor (q : ℝ) : ℝ :=
  1 - 1 / q

/-- Under the square map $q \mapsto q^2$, the skein difference parameter factors as
$(q - q^{-1})(q + q^{-1})$. -/
theorem skeinDiffParam_square_factorization (q : ℝ) (hq : q ≠ 0) :
    skeinDiffParam (q ^ 2) = skeinDiffParam q * (q + 1 / q) := by
  unfold skeinDiffParam
  have hq2 : q ^ 2 ≠ 0 := pow_ne_zero 2 hq
  have h_expand : (q - 1 / q) * (q + 1 / q) = q ^ 2 - 1 / q ^ 2 := by
    field_simp [hq, hq2]
    ring
  exact h_expand.symm

/-- Under the square map $q \mapsto q^2$, the deformation factor factors as
$(1 - q^{-1})(1 + q^{-1})$. -/
theorem deformFactor_square_factorization (q : ℝ) (hq : q ≠ 0) :
    deformFactor (q ^ 2) = deformFactor q * (1 + 1 / q) := by
  unfold deformFactor
  have hq2 : q ^ 2 ≠ 0 := pow_ne_zero 2 hq
  have h_expand : (1 - 1 / q) * (1 + 1 / q) = 1 - 1 / q ^ 2 := by
    field_simp [hq, hq2]
    ring
  exact h_expand.symm

/-- Absolute shortfall $|B - B_{\mathrm{target}}|$ relative to a positive target. -/
noncomputable def absShortfall (B B_target : ℝ) : ℝ :=
  |B - B_target|

/-- In the underbinding regime $B_D < B_C < B_{\mathrm{target}}$, migrating from $B_C$
to $B_D$ increases the absolute shortfall by exactly $B_C - B_D > 0$. -/
theorem underbinding_shortfall_increase (B_D B_C B_target : ℝ)
    (hDC : B_D < B_C) (hCT : B_C < B_target) :
    absShortfall B_D B_target - absShortfall B_C B_target = B_C - B_D ∧
      0 < absShortfall B_D B_target - absShortfall B_C B_target := by
  unfold absShortfall
  have hDT : B_D - B_target < 0 := by linarith
  have hCT' : B_C - B_target < 0 := by linarith
  have h_absD : |B_D - B_target| = B_target - B_D := by
    rw [abs_of_neg hDT]
    ring
  have h_absC : |B_C - B_target| = B_target - B_C := by
    rw [abs_of_neg hCT']
    ring
  have h_diff : |B_D - B_target| - |B_C - B_target| = B_C - B_D := by
    rw [h_absD, h_absC]
    ring
  refine ⟨h_diff, ?_⟩
  rw [h_diff]
  linarith

/-- Exact rational ratio between the $A = 4$ cabled shortfall factor $78.8 = 788/10$
and the $A = 3$ cabled shortfall factor $1.585 = 1585/1000$. -/
def cabledShortfallRatioQuotient : ℚ :=
  (788 / 10) / (1585 / 1000)

/-- The cabled shortfall ratio quotient equals $15760 / 317$ and strictly exceeds $49$. -/
theorem cabledShortfallRatioQuotient_exact_and_gt_49 :
    cabledShortfallRatioQuotient = 15760 / 317 ∧
      (49 : ℚ) < cabledShortfallRatioQuotient := by
  unfold cabledShortfallRatioQuotient
  have h_eq : ((788 : ℚ) / 10) / (1585 / 1000) = 15760 / 317 := by
    norm_num
  have h_gt : (49 : ℚ) < 15760 / 317 := by
    norm_num
  refine ⟨h_eq, ?_⟩
  rw [h_eq]
  exact h_gt

/-- When two baseline cluster contributions $b_3, b_4$ and targets $t_3, t_4$ satisfy
$t_3 \cdot b_4 \neq t_4 \cdot b_3$, no single constant scalar $c$ closes both simultaneously. -/
theorem no_constant_reweight_closes_both (b3 b4 t3 t4 : ℝ)
    (h_cross : t3 * b4 ≠ t4 * b3) :
    ¬ ∃ c : ℝ, c * b3 = t3 ∧ c * b4 = t4 := by
  rintro ⟨c, hc3, hc4⟩
  have h_lhs : t3 * b4 = c * b3 * b4 := by
    rw [← hc3]
  have h_rhs : t4 * b3 = c * b4 * b3 := by
    rw [← hc4]
  have h_comm : c * b3 * b4 = c * b4 * b3 := by
    ring
  have h_eq : t3 * b4 = t4 * b3 := by
    rw [h_lhs, h_rhs, h_comm]
  exact h_cross h_eq

/-- In a two-term additive closure $c \cdot b_A + d_A = t_A$ anchored at $d_3 = 0$,
the $A = 4$ residual term $d_4$ equals $b_4 (t_4 / b_4 - t_3 / b_3)$ and is strictly
positive whenever $b_3 > 0$, $b_4 > 0$, and $t_3 / b_3 < t_4 / b_4$. -/
theorem two_term_closure_positive_residual (b3 b4 t3 t4 c d4 : ℝ)
    (hb3 : 0 < b3) (hb4 : 0 < b4)
    (hc3 : c * b3 = t3) (hc4 : c * b4 + d4 = t4)
    (h_ratio : t3 / b3 < t4 / b4) :
    d4 = b4 * (t4 / b4 - t3 / b3) ∧ 0 < d4 := by
  have hb3_ne : b3 ≠ 0 := ne_of_gt hb3
  have hb4_ne : b4 ≠ 0 := ne_of_gt hb4
  have hc_val : c = t3 / b3 := by
    have h1 : c * b3 / b3 = t3 / b3 := congrArg (· / b3) hc3
    have h2 : c * b3 / b3 = c := mul_div_cancel_right₀ c hb3_ne
    rw [← h2, h1]
  have hd4_val : d4 = b4 * (t4 / b4 - t3 / b3) := by
    have h_sub : d4 = t4 - c * b4 := by linarith
    rw [h_sub, hc_val]
    field_simp [hb3_ne, hb4_ne]
    ring
  have h_diff_pos : 0 < t4 / b4 - t3 / b3 := sub_pos.mpr h_ratio
  have hd4_pos : 0 < d4 := by
    rw [hd4_val]
    exact mul_pos hb4 h_diff_pos
  exact ⟨hd4_val, hd4_pos⟩

end QOU.MassTheory.ConventionDErrorShiftAndBrunnianShortfall
