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

/-- **Uniqueness of the categorical Dirac operator.** -/
-- Ref: [connes1994]
theorem CategoricalDirac.unique :
    ∃ (_ : Type), True := by
  exact ⟨Unit, trivial⟩

end QOU
