import QOU.Nuclear.DecayLadderConventionDPositivity
import Mathlib.Analysis.SpecialFunctions.Sqrt

/-!
# Convention C with `Real.sqrt` (Transcendental companion)

Split from `QOU.Nuclear.DecayLadderConventionDPositivity` (bean `qou-dk7p`). That
file states convention C in the square-root variable `t`, `q = t²`. This file
keeps `z_C(q) = √q/(1+q)` and the original theorem names, reducing each to the
`t` form at `t = √q`.
-/

namespace QOU.QBeta.DecayLadderConventionDPositivity

/-- The convention-C Markov parameter, `z_C(q) = √q/(1+q)`. -/
noncomputable def zC (q : ℝ) : ℝ := Real.sqrt q / (1 + q)

theorem zC_eq_zCt (q : ℝ) (hq : 0 ≤ q) : zC q = zCt (Real.sqrt q) := by
  unfold zC zCt
  rw [Real.sq_sqrt hq]

theorem one_lt_sqrt_of_one_lt {q : ℝ} (hq : 1 < q) : 1 < Real.sqrt q := by
  have : Real.sqrt 1 < Real.sqrt q := Real.sqrt_lt_sqrt zero_le_one hq
  simpa using this

/-- **`z_C(q) < 1/2` on the whole substrate regime `q > 1`.** -/
theorem zC_lt_half (q : ℝ) (hq : 1 < q) : zC q < 1 / 2 := by
  rw [zC_eq_zCt q (by linarith)]
  exact zCt_lt_half _ (one_lt_sqrt_of_one_lt hq)

theorem ladderPhaseCoeff_pos_at_zC (q : ℝ) (hq : 1 < q) :
    0 < ladderPhaseCoeff (zC q) := by
  rw [zC_eq_zCt q (by linarith)]
  exact ladderPhaseCoeff_pos_at_zCt _ (one_lt_sqrt_of_one_lt hq)

theorem ladderPhaseCoeff_sign_separates_zC_zD (q : ℝ) (hq : 1 < q) :
    0 < ladderPhaseCoeff (zC q) ∧ ladderPhaseCoeff (zD q) < 0 :=
  ⟨ladderPhaseCoeff_pos_at_zC q hq, ladderPhaseCoeff_neg_at_zD q hq⟩

end QOU.QBeta.DecayLadderConventionDPositivity
