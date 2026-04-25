/-!
# QOU.CategoricalDirac.unique — uniqueness of the categorical Dirac operator

𝒟_∇ is uniquely determined by its defining formula once ∇, q, ξ are
fixed.

LaTeX: `\label{prop:categorical-dirac-operator-unique}`

## References

- [manuscript] §2-quantum-observable-universes/categorical-dirac-operator-unique
- [connes1994] Noncommutative Geometry
-/

import QOU.Basic

namespace QOU

/-- **Uniqueness of the categorical Dirac operator.**

    Given fixed ∇, q, ξ, the operator
    `𝒟_∇ = q⁻¹ ∇ + (1 - q⁻¹) ι_ξ ∇` is uniquely determined. -/
-- Ref: [connes1994]
theorem CategoricalDirac.unique
    {C : Type u} [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C]
    (fh : FrobeniusHopfData C) :
    Subsingleton (CategoricalDiracOperator C fh) := by
  -- Formula is an R-linear combination of fixed morphisms.
  -- Ref: [connes1994]
  sorry

end QOU
