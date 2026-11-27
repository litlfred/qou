import QOU.Nuclear.AfreeThetaConstraint
import Mathlib.Analysis.SpecialFunctions.Sqrt

/-!
# The anchor-count statement at `ℝ` (Transcendental companion)

Split from `QOU.Nuclear.AfreeThetaConstraint` (bean `qou-dk7p`). That file proves
`exists_angle_assignment_of_sqrt` with existence of square roots as a hypothesis.
This file discharges it with `Real.sqrt` and keeps the original name.
-/

namespace QOU.QBeta.AfreeThetaConstraint

open QOU.QBeta.ThetaRealityBound

variable {n : ℕ}

/-- **Adding anchors never helps**, at `ℝ`: see
`exists_angle_assignment_of_sqrt`. -/
theorem exists_angle_assignment (S : Fin n → ℝ) (κ lnq A : ℝ)
    (hadm : ∀ i, S i / (A * κ) ≤ lnq ^ 2) :
    ∃ θ : Fin n → ℝ, ∀ i, (θ i) ^ 2 = thetaSq A κ lnq (S i) :=
  exists_angle_assignment_of_sqrt (fun x hx => ⟨Real.sqrt x, Real.sq_sqrt hx⟩) S κ lnq A hadm

end QOU.QBeta.AfreeThetaConstraint
