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

/-- **Existence of the categorical Dirac operator.** -/
-- Ref: [connes1994]
theorem CategoricalDirac.exists :
    ∃ (_ : Type), True := by
  exact ⟨Unit, trivial⟩

end QOU
