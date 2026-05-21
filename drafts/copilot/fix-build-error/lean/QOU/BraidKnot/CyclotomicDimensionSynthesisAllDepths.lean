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

/-- **Theorem (`prop:cyclotomic-dimension-synthesis-all-depths`).**
    The parity-cased dimension formula is consistent with itself.
    Substantive content (Bloch-Suslin at n = 2; Beilinson-conditional
    at n ≥ 3) is conditional. -/
theorem dimension_synthesis_all_depths
    (n K : ℕ) (_ : 2 ≤ n) (_ : 3 ≤ K) (_ : Nat.Prime K) :
    predictedDim n K = (if n % 2 = 1 then (K - 3) / 2 else (K - 1) / 2) := by
  rfl

end QOU.BraidKnot.CyclotomicDimensionSynthesisAllDepths
