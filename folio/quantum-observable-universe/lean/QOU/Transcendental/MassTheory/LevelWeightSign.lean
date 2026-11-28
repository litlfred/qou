import Mathlib.Data.Real.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity

/-!
# Sign of the jet-level pole, as `q → 1⁺` (transcendental side)

By `QOU.MassTheory.LevelWeightEnergy.energy_hbar_zpow_mul`, a level factor `ℏ_q^j` adds
`−j/(q − 1)` to the energy reading. This file states, over `ℝ` and for `q > 1`, which signs of `j`
keep that term bounded below near the classical point `q = 1`.

* `levelPole_unbounded_below`: for `j > 0` the term is unbounded below on `(1, 2)`.
* `levelPole_nonneg`: for `j ≤ 0` it is `≥ 0` on `q > 1`.

So **if** one requires the energy reading to be bounded below as `q → 1⁺`, the level exponent must
satisfy `j ≤ 0`: the weight is `ℏ_q^(−|j|)`, i.e. heavier with level. That requirement is a
hypothesis, not an axiom of the framework; no measured value enters.
-/

namespace QOU.Transcendental.MassTheory.LevelWeightSign

/-- The level pole term `−j/(q − 1)`. -/
noncomputable def levelPole (j q : ℝ) : ℝ := -j / (q - 1)

/-- **For `j > 0` the level pole is unbounded below as `q → 1⁺`.** -/
theorem levelPole_unbounded_below {j : ℝ} (hj : 0 < j) (M : ℝ) :
    ∃ q : ℝ, 1 < q ∧ q < 2 ∧ levelPole j q < M := by
  have hden : 0 < |M| + 1 + j := by positivity
  have ht0 : 0 < j / (|M| + 1 + j) := div_pos hj hden
  have ht1 : j / (|M| + 1 + j) < 1 := (div_lt_one hden).mpr (by linarith [abs_nonneg M])
  refine ⟨1 + j / (|M| + 1 + j), by linarith, by linarith, ?_⟩
  have hval : levelPole j (1 + j / (|M| + 1 + j)) = -(|M| + 1 + j) := by
    unfold levelPole
    rw [add_sub_cancel_left]
    field_simp
  rw [hval]
  linarith [neg_abs_le M]

/-- **For `j ≤ 0` the level pole is nonnegative on `q > 1`.** -/
theorem levelPole_nonneg {j q : ℝ} (hj : j ≤ 0) (hq : 1 < q) : 0 ≤ levelPole j q := by
  unfold levelPole
  apply div_nonneg <;> linarith

end QOU.Transcendental.MassTheory.LevelWeightSign
