import QOU.Infra.BorelRank
import QOU.Infra.Polylogarithm

/-!
# Cyclotomic depth-3 dimension synthesis at every prime K ≥ 5

Compiled formalisation of
`conj:cyclotomic-depth3-dimension-synthesis`.
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

/-- The depth-3 dimension-synthesis claim
    (`conj:cyclotomic-depth3-dimension-synthesis`), as a **predicate** on the
    actual dimension: the dimension of genuinely-new depth-3 content over
    `ℚ(ζ_K)` (prime `K ≥ 5`) equals the predicted `(K-3)/2`.

    Named (§3b), not asserted: the previous
    `dimension_synthesis_upper_bound (K) (_ : 5 ≤ K) (_ : Prime K) :
    predictedDim K = (K-3)/2 := rfl` unfolded the definition under two unused
    hypotheses and asserted nothing (its own docstring read "agrees with
    itself"). The keystone-B1 upper bound is real and the lower bound is
    Beilinson-conditional — both upstream/open — so this names the claim
    (mirroring the `rank_witness` predicate fix in `QOU.Infra.BorelRank`). -/
def dimensionSynthesisHolds (K actualDim : ℕ) : Prop :=
  actualDim = predictedDim K

end QOU.BraidKnot.CyclotomicDepth3DimensionSynthesis
