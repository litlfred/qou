import QOU.Infra.BorelRank

/-!
# Dimension synthesis at all depths: parity-dependent

Compiled formalisation of
`prop:cyclotomic-dimension-synthesis-all-depths`.
Sibling docstub at
`braids-and-knots/cyclotomic-dimension-synthesis-all-depths.lean`.
-/

namespace QOU.BraidKnot.CyclotomicDimensionSynthesisAllDepths

open QOU.Infra.BorelRank

/-- Predicted dimension at depth `n` over `ℚ(ζ_K)` for prime `K`:

      n odd:  `(K - 3) / 2`
      n even: `(K - 1) / 2`
-/
def predictedDim (n K : ℕ) : ℕ :=
  if n % 2 = 1 then (K - 3) / 2 else (K - 1) / 2

/-- The all-depths dimension-synthesis claim
    (`prop:cyclotomic-dimension-synthesis-all-depths`), as a **predicate** on the
    actual dimension at depth `n` over `ℚ(ζ_K)` (prime `K`): it equals the
    parity-cased prediction.

    Named (§3b), not asserted: the previous
    `dimension_synthesis_all_depths … : predictedDim n K = (if …) := rfl`
    unfolded the definition under three unused hypotheses (its own docstring
    read "consistent with itself"). Substantive content — Bloch–Suslin at
    `n = 2`, Beilinson-conditional at `n ≥ 3` — is upstream/open, so this names
    the claim rather than proving it. -/
def dimensionSynthesisHolds (n K actualDim : ℕ) : Prop :=
  actualDim = predictedDim n K

end QOU.BraidKnot.CyclotomicDimensionSynthesisAllDepths
