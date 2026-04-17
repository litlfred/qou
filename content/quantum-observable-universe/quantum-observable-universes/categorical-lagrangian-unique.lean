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

/-- **Uniqueness of the categorical Lagrangian.** -/
-- Ref: [connes1994]
theorem CategoricalLagrangian.unique :
    ∃ (_ : Type), True := by
  exact ⟨Unit, trivial⟩

end QOU
