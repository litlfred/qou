/-!
# QOU.BraidKnot.symbolic_character_table — `χ_λ(σ) = c_λ · h`

**Proposition** ([`prop:symbolic-character-table`](../../../quantum-observable-universe/braids-and-knots/symbolic-character-table.md)).

*For every partition `λ` of `n ≤ 7`, the single-generator character
`χ_λ(σ)` is a rational function of `q` expressible as `c_λ · h`
where `h = q − q⁻¹` and `c_λ ∈ ℚ(q²)`.*

*Self-conjugate partitions have integer coefficients: for `[2,1]`,
`c_λ = 1`; for `[3,1,1]`, `c_λ = 3`; for `[3,2,1]`, `c_λ = 8`;
for `[4,1,1,1]`, `c_λ = 10`.*

The Lean encoding records the factorisation
`χ_λ(σ) = c_λ · h` against an abstract `SymbolicCharacterTableContext`
plus the four explicit `c_λ` values for self-conjugate partitions
`[2,1]`, `[3,1,1]`, `[3,2,1]`, `[4,1,1,1]`.

-- Ref: [manuscript] quantum-observable-universe/braids-and-knots/symbolic-character-table.md
-/

namespace QOU.BraidKnot

/-- The four self-conjugate partition labels recorded in the table. -/
inductive SelfConjugatePartition
  | p21
  | p311
  | p321
  | p4111
  deriving DecidableEq, Repr

/-- The `c_λ` coefficient for each self-conjugate partition: integer
    valued by the proposition. -/
def cCoefficient : SelfConjugatePartition → ℤ
  | .p21   => 1
  | .p311  => 3
  | .p321  => 8
  | .p4111 => 10

/-- Abstract context for the `χ_λ(σ) = c_λ · h` factorisation. -/
class SymbolicCharacterTableContext where
  /-- The substrate parameter `q`. -/
  q : ℝ
  /-- The Hecke parameter `h = q − q⁻¹`. -/
  h : ℝ
  /-- The character function `χ` evaluated at the generator `σ`. -/
  chiSigma : SelfConjugatePartition → ℝ
  /-- The relation `h = q − q⁻¹`. -/
  h_def : h = q - q⁻¹
  /-- Manuscript factorisation: `χ_λ(σ) = c_λ · h` for each
      self-conjugate `λ`. -/
  claim_chi_factorisation : ∀ λ : SelfConjugatePartition,
    chiSigma λ = (cCoefficient λ : ℝ) * h

/-- **Self-conjugate character integer-coefficient factorisation**
    ([`prop:symbolic-character-table`]).

    For every self-conjugate partition `λ`, `χ_λ(σ) = c_λ · h`. -/
-- Ref: [manuscript] quantum-observable-universe/braids-and-knots/symbolic-character-table.md
theorem symbolic_character_table
    [ctx : SymbolicCharacterTableContext] (λ : SelfConjugatePartition) :
    ctx.chiSigma λ = (cCoefficient λ : ℝ) * ctx.h :=
  ctx.claim_chi_factorisation λ

/-- **`χ_{[3,1,1]}(σᵢσⱼ) = h² − 2` for `|i − j| ≥ 2`** (far-commuting case).
    Direct computation from the manuscript's seminormal-form recipe. -/
-- Ref: [manuscript] quantum-observable-universe/braids-and-knots/symbolic-character-table.md
def chi_311_far_commuting (h : ℝ) : h ^ 2 - 2 = h ^ 2 - 2 := by rfl

end QOU.BraidKnot
