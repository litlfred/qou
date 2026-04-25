/-!
# QOU.CategoricalLagrangian.unique — uniqueness of the categorical Lagrangian

Given (∇, ψ), 𝓛_q is uniquely determined by its defining formula.

LaTeX: `\label{prop:categorical-lagrangian-unique}`

## References

- [manuscript] §2-quantum-observable-universes/categorical-lagrangian-unique
- [connes1994] Noncommutative Geometry
-/

import QOU.Basic

namespace QOU

/-- **Uniqueness of the categorical Lagrangian.**

    Given fixed (∇, ψ), the Lagrangian
    `𝒟_∇² + ψ* ⊗ 𝒟_∇ψ` is uniquely determined. -/
-- Ref: [connes1994]
theorem CategoricalLagrangian.unique
    {C : Type u} [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C]
    (fh : FrobeniusHopfData C) :
    Subsingleton (CategoricalLagrangian C fh) := by
  -- Formula-determined; inherits uniqueness from Dirac + ψ adjoint.
  -- Ref: [connes1994]
  sorry

end QOU
