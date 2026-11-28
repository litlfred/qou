import BraidKnotOctonion.YoungDiagramTailThirdInstanceAssembly

/-!
# The depth-2 tail `ν_{n−2}(n)` at `n = 4, 5`, and the closed form for every `n ≥ 4`

`YoungDiagramTailThirdInstanceAssembly` proves `nuV n (n − 2) = nuDepthTwoClosedForm n` for
`n ≥ 6`; its shape classification degenerates below that. This file evaluates the two remaining
cases directly from the definitions: `ν_2(4) = −2/3` and `ν_3(5) = 0`. Both rest on an exact
integer sum over the partitions of `4` and `5`, checked by `decide` in the kernel.

Together they give the closed form for every `n ≥ 4`, and the full sign pattern of the depth-2
tail: for `n ≥ 4`, `ν_{n−2}(n) > 0` iff `n = 6` or `n ≥ 10`, and `ν_{n−2}(n) = 0` iff `n = 5`.

Audit: `docs/audits/2026-11-27-covariance-kernel-depth-two-tail.md`; bean `qou-swk4`.
-/

set_option autoImplicit false

namespace QOU.BraidsAndKnots.YoungDiagramTailThirdInstanceSmallN

open QOU.BraidsAndKnots.YoungDiagramKernel
open QOU.BraidsAndKnots.YoungDiagramKernelPincer
open QOU.BraidsAndKnots.SecondMomentKernelVanishes
open QOU.BraidsAndKnots.YoungDiagramTailThirdInstance
open QOU.BraidsAndKnots.YoungDiagramTailThirdInstanceAssembly

/-- The exact integer numerator of `ν_v(k)`: `Σ_{λ ⊢ k} (f^λ)²·N_v(λ)·ω₃(λ)`. -/
noncomputable def nuNumerator (k v : ℕ) : ℤ :=
  ((partsOf k).map (fun l => (sytDim l : ℤ) ^ 2 * (hookCount l v : ℤ) * omega3 k l)).sum

/-- `ν_v(k) = (Σ_λ (f^λ)²·N_v(λ)·ω₃(λ)) / k!`, the mean of `ω₃` being zero. -/
theorem nuV_eq_numerator_div (k v : ℕ) :
    nuV k v = (nuNumerator k v : ℝ) / (Nat.factorial k : ℝ) := by
  unfold nuV
  rw [tiltedMean_zero k, mul_zero, sub_zero]
  unfold nuMixedMoment
  rw [QOU.BraidsAndKnots.PlancherelNormalisation.tiltNorm_zero_eq_factorial k]
  congr 1
  unfold nuNumerator
  rw [Int.cast_list_sum, List.map_map]
  refine congrArg List.sum (List.map_congr_left fun l _ => ?_)
  simp only [Function.comp_apply]
  rw [tilt_zero]
  push_cast
  ring

/-- The integer numerator at `n = 4`, `v = 2`. -/
theorem nuNumerator_four_two : nuNumerator 4 2 = -16 := by
  unfold nuNumerator; decide

/-- The integer numerator at `n = 5`, `v = 3`. -/
theorem nuNumerator_five_three : nuNumerator 5 3 = 0 := by
  unfold nuNumerator; decide

/-- `ν_2(4) = −2/3`, the closed-form value at `n = 4`. -/
theorem nuV_four_two : nuV 4 2 = nuDepthTwoClosedForm (R := ℝ) 4 := by
  rw [nuV_eq_numerator_div, nuNumerator_four_two, (nuDepthTwo_small_values (R := ℝ)).1]
  norm_num [Nat.factorial]

/-- `ν_3(5) = 0`, the closed-form value at `n = 5`. -/
theorem nuV_five_three : nuV 5 3 = nuDepthTwoClosedForm (R := ℝ) 5 := by
  rw [nuV_eq_numerator_div, nuNumerator_five_three, (nuDepthTwo_small_values (R := ℝ)).2.1]
  simp

/-- **The depth-2 tail in closed form, for every `n ≥ 4`.** -/
theorem nuV_depthTwo_closed_form_of_four_le (n : ℕ) (hn : 4 ≤ n) :
    nuV n (n - 2) = nuDepthTwoClosedForm (R := ℝ) n := by
  rcases Nat.lt_or_ge n 6 with h | h
  · obtain rfl | rfl : n = 4 ∨ n = 5 := by omega
    · rw [show (4 : ℕ) - 2 = 2 from rfl]; exact nuV_four_two
    · rw [show (5 : ℕ) - 2 = 3 from rfl]; exact nuV_five_three
  · exact nuV_depthTwo_closed_form n h

/-- **Sign of the depth-2 tail.** For `n ≥ 4`, `ν_{n−2}(n) > 0` iff `n = 6` or `n ≥ 10`. -/
theorem nuV_depthTwo_pos_iff_of_four_le (n : ℕ) (hn : 4 ≤ n) :
    0 < nuV n (n - 2) ↔ n = 6 ∨ 10 ≤ n := by
  rw [nuV_depthTwo_closed_form_of_four_le n hn]
  exact nuDepthTwo_pos_iff n hn

/-- For `n ≥ 4`, the depth-2 tail vanishes exactly at `n = 5`. -/
theorem nuV_depthTwo_eq_zero_iff_of_four_le (n : ℕ) (hn : 4 ≤ n) :
    nuV n (n - 2) = 0 ↔ n = 5 := by
  rw [nuV_depthTwo_closed_form_of_four_le n hn]
  exact nuDepthTwo_eq_zero_iff n hn

end QOU.BraidsAndKnots.YoungDiagramTailThirdInstanceSmallN
