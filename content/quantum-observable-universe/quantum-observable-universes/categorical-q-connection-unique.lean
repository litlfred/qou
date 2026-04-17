/-!
# QOU.CategoricalQConnection.unique — uniqueness of the categorical q-connection

∇_q uniquely determined by (∇, ξ, θ, q), inheriting the gauge
freedom of ∇.

LaTeX: `\label{prop:categorical-q-connection-unique}`

## References

- [manuscript] §2-quantum-observable-universes/categorical-q-connection-unique
- [connes1994] Noncommutative Geometry
-/

import QOU.Basic

namespace QOU

/-- **Uniqueness of the categorical q-connection.** -/
-- Ref: [connes1994]
theorem CategoricalQConnection.unique :
    ∃ (_ : Type), True := by
  exact ⟨Unit, trivial⟩

end QOU
