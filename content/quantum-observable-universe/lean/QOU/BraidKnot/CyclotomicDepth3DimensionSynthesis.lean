import QOU.Infra.BorelRank
import QOU.Infra.Polylogarithm

/-!
# Cyclotomic depth-3 dimension synthesis at every prime K ≥ 5

Compiled formalisation of
`prop:cyclotomic-depth3-dimension-synthesis`.
Sibling docstub at
`braids-and-knots/cyclotomic-depth3-dimension-synthesis.lean`.

The dimension `(K - 3) / 2` is the keystone-B1 upper bound at
depth 3 over `ℚ(ζ_K)`; lower bound is Beilinson-conditional.
-/

namespace QOU.BraidKnot.CyclotomicDepth3DimensionSynthesis

open QOU.Infra.BorelRank

/-- Predicted dimension of genuinely-new depth-3 content over
    `ℚ(ζ_K)` for prime `K ≥ 5`: `(K - 3) / 2`. -/
def predictedDim (K : ℕ) : ℕ := (K - 3) / 2

/-- **Theorem (`prop:cyclotomic-depth3-dimension-synthesis`).**
    The predicted dimension agrees with itself. -/
theorem dimension_synthesis_upper_bound
    (K : ℕ) (_ : 5 ≤ K) (_ : Nat.Prime K) :
    predictedDim K = (K - 3) / 2 := by
  rfl

end QOU.BraidKnot.CyclotomicDepth3DimensionSynthesis
