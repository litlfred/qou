/-!
# QOU.BraidKnot.mass_formula_wedderburn_enumeration

Every partition `μ ⊢ n` enters the unified mass formula exactly once,
via its curvature-rank stratum `Λ_k = {μ : depth(μ) = k}`.  The
strata partition the set of partitions; Plancherel completeness
`∑_μ w_μ = 1` certifies exhaustivity.

LaTeX label: `rem:mass-formula-wedderburn-enumeration`

## References

- [manuscript] Ch. Braids and Knots, §Mass formula
-/

import QOU.Descartes.SkewSYT

namespace QOU.BraidKnot

open QOU.Descartes.SkewSYT

/-- Curvature-rank depth of a partition: number of parts minus one. -/
def depth (μ : Partition) : ℕ := μ.length - 1

/-- The depth-`k` stratum: partitions of size `n` with curvature-rank `k`. -/
def Stratum (n k : ℕ) : Set Partition :=
  {μ | μ.size = n ∧ depth μ = k}

/-- Strata are pairwise disjoint and cover every partition of `n`. -/
-- Ref: [manuscript] Ch. Braids and Knots, §Mass formula
theorem strata_partition (n : ℕ) :
    (∀ (k k' : ℕ) (μ : Partition),
      μ ∈ Stratum n k → μ ∈ Stratum n k' → k = k') ∧
    (∀ μ : Partition, μ.size = n → μ ∈ Stratum n (depth μ)) := by
  refine ⟨?_, ?_⟩
  · intro k k' μ hk hk'
    simp [Stratum] at hk hk'
    exact hk.2.symm.trans hk'.2
  · intro μ hμ
    simp [Stratum, hμ]

end QOU.BraidKnot
