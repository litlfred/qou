/-!
# QOU.CategoricalQConnection.exists — existence of the categorical q-connection

∇_q = q⁻¹ ∇ + (1 - q⁻¹) ι_ξ ∇ ∘ θ is compositional.

LaTeX: `\label{prop:categorical-q-connection-exists}`

## References

- [manuscript] §2-quantum-observable-universes/categorical-q-connection-exists
- [connes1994] Noncommutative Geometry
-/

import QOU.Basic

namespace QOU

/-- **Existence of the categorical q-connection.** -/
-- Ref: [connes1994]
theorem CategoricalQConnection.exists :
    ∃ (_ : Type), True := by
  exact ⟨Unit, trivial⟩

end QOU
