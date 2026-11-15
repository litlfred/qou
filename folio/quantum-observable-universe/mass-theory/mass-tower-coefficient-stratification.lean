import QOU.BraidKnot.PlancherelWeightBoundedness


/-!
# QOU.BraidKnot.mass_tower_coefficient_stratification

QOU mass-tower coefficients
`(λ_V, λ_S, λ_pair, λ_Wigner, λ_shell)` are each the Plancherel-
weighted projection onto a specific curvature-rank stratum `Λ_k`.

Each coefficient is forced by spectral structure, not fit.

LaTeX label: `prop:mass-tower-coefficient-stratification`

## References

- [leitner2026] Ch. Braids and Knots, §Mass tower coefficients
-/

namespace QOU.BraidKnot

/-- Mapping from QOU mass-tower term to curvature-rank stratum. -/
inductive MassTowerTerm
  | volume       -- λ_V at depth 0
  | surface      -- λ_S at depth 1
  | pair         -- λ_pair at depth 2
  | wigner       -- λ_Wigner restricted self-conj
  | shell        -- universal tail (depth ≥ 4)
  | knotFactor   -- a_K chirality projection at depth 2
  | pauli        -- F_Pauli sym/alt extremal blocks

/-- The forced depth (or stratum identifier) for each QOU mass-tower term. -/
def stratumDepth : MassTowerTerm → ℕ
  | .volume => 0
  | .surface => 1
  | .pair => 2
  | .wigner => 3
  | .shell => 4         -- representative; "≥ 4" tail
  | .knotFactor => 2
  | .pauli => 0         -- representative; uses both sym (Λ_0) and alt (Λ_{n-1})

/-- **Proposition (mass-tower strata are exhausted by depths 0–4).**

    Every `MassTowerTerm` is assigned a stratum depth in the range
    `0 … 4`; no term escapes the finite stratification the mass tower
    is built on.

    **Scope.** This is the well-definedness half of
    `prop:mass-tower-coefficient-stratification`. The full narrative
    claim — that each prefactor *equals* the Plancherel-weighted
    Frobenius integral over the partitions of its stratum — is not
    formalised here; it needs the Frobenius-integral machinery, which
    is not yet available in Lean. What is proved is falsifiable (it
    would fail if any constructor were assigned a depth above 4) and
    is checked by exhaustion over the constructors.

    Note the depth map is deliberately **not** injective: `.pair` and
    `.knotFactor` both sit at depth 2, and `.volume` and `.pauli` both
    at depth 0, so no uniqueness claim is available or intended. -/
-- Ref: [leitner2026] Ch. Braids and Knots, §Mass tower coefficients
theorem mass_tower_coefficient_stratification
    (term : MassTowerTerm) :
    stratumDepth term ≤ 4 := by
  cases term <;> decide

end QOU.BraidKnot
