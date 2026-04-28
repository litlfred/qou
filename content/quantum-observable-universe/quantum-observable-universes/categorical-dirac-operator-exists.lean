/-!
# QOU.CategoricalDirac.exists — existence of the categorical Dirac operator

𝒟_∇ = q⁻¹ ∇ + (1 - q⁻¹) ι_ξ ∇ is a morphism, compositional from
∇, ι_ξ, and scalar operations.

LaTeX: `\label{prop:categorical-dirac-operator-exists}`

## References

- [manuscript] §2-quantum-observable-universes/categorical-dirac-operator-exists
- [connes1994] Noncommutative Geometry (Academic Press)
-/

import QOU.Basic

namespace QOU

/-- **Existence of the categorical Dirac operator.**

    For any `FrobeniusHopfData C`, a `CategoricalDiracOperator C fh`
    term exists via the formula
    `𝒟_∇ = q⁻¹ ∇ + (1 - q⁻¹) ι_ξ ∇`. -/
-- Ref: [connes1994]
theorem CategoricalDirac.exists
    {C : Type u} [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C]
    (fh : FrobeniusHopfData C) :
    Nonempty (CategoricalDiracOperator C fh) := by
  -- Compositional witness from ∇, ι_ξ, and scalars.
  -- Ref: [connes1994]
  sorry

end QOU
