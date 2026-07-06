import Mathlib.Tactic

/-!
# QOU.BraidKnot.knot_factor_spectral_derivation — `a_𝒦` as Plancherel-weighted character pairing

**Proposition** ([`prop:knot-factor-spectral-derivation`](../../../quantum-observable-universe/braids-and-knots/knot-factor-spectral-derivation.md)).

*Let `𝒦` be a knot with braid representative `β_𝒦 ∈ B_n` and mirror
`β_𝒦*`, working over `A = H_n(R, q)`.  The knot factor `a_𝒦` in the
unified mass formula is the normalised chirality Gram pairing*

```
  a_𝒦 = G_{β_𝒦, β_𝒦*} / G_{𝟙, 𝟙}
      = Σ_{λ ⊢ n} w_λ · χ_λ(β_𝒦) · χ_λ(β_𝒦*) / χ_λ(𝟙)²
```

*with Plancherel weights `w_λ = dim_q²(V_λ) / [n]_q!` summing to 1.
The identity is exact in `R`.*

The Lean encoding records the closed-form sum against an abstract
`KnotFactorContext` carrying the Plancherel weights, characters,
and Gram-pairing data.

-- Ref: [manuscript] quantum-observable-universe/braids-and-knots/knot-factor-spectral-derivation.md
-/

namespace QOU.BraidKnot

/-- Abstract context for the knot-factor spectral formula. -/
class KnotFactorSpectralContext (n : ℕ) where
  /-- The Hecke parameter `q`. -/
  q : ℝ
  /-- Indexing type for partitions of `n`. -/
  Partition : Type
  /-- The finite set of partitions of `n`. -/
  partitions : Finset Partition
  /-- Plancherel weight `w_λ` for each partition. -/
  plancherelWeight : Partition → ℝ
  /-- Character of `β_𝒦` on irrep `λ`. -/
  chi_beta : Partition → ℝ
  /-- Character of the mirror `β_𝒦*` on irrep `λ`. -/
  chi_beta_mirror : Partition → ℝ
  /-- Character of `𝟙` on irrep `λ` (the categorical dimension
      of irrep `λ`). -/
  chi_one : Partition → ℝ
  /-- Non-vanishing: `χ_λ(𝟙) ≠ 0` for every `λ` (the categorical
      dimension is non-zero in generic position). -/
  chi_one_ne_zero : ∀ lam, chi_one lam ≠ 0
  /-- The knot factor `a_𝒦` from the unified mass formula. -/
  knotFactor : ℝ
  /-- Plancherel weights sum to 1 (Wedderburn trace identity). -/
  claim_plancherel_sum_one :
    (partitions.sum fun lam => plancherelWeight lam) = 1
  /-- Knot-factor spectral formula. -/
  claim_knot_factor_spectral :
    knotFactor = partitions.sum
      fun lam => plancherelWeight lam * chi_beta lam * chi_beta_mirror lam
               / (chi_one lam) ^ 2

/-- **Plancherel weights sum to 1** ([`prop:knot-factor-spectral-derivation`]
    sub-claim from the manuscript). -/
-- Ref: [manuscript] quantum-observable-universe/braids-and-knots/knot-factor-spectral-derivation.md
def plancherelWeight_sum_eq_one
    {n : ℕ} [ctx : KnotFactorSpectralContext n] :
    (ctx.partitions.sum fun lam => ctx.plancherelWeight lam) = 1 :=
  ctx.claim_plancherel_sum_one

/-- **Knot-factor spectral formula** ([`prop:knot-factor-spectral-derivation`]).

    `a_𝒦 = Σ_λ w_λ · χ_λ(β_𝒦) · χ_λ(β_𝒦*) / χ_λ(𝟙)²`. -/
-- Ref: [manuscript] quantum-observable-universe/braids-and-knots/knot-factor-spectral-derivation.md
def knot_factor_spectral_derivation
    {n : ℕ} [ctx : KnotFactorSpectralContext n] :
    ctx.knotFactor
      = ctx.partitions.sum
          fun lam => ctx.plancherelWeight lam
                   * ctx.chi_beta lam * ctx.chi_beta_mirror lam
                   / (ctx.chi_one lam) ^ 2 :=
  ctx.claim_knot_factor_spectral

end QOU.BraidKnot
