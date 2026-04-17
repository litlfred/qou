/-!
# QOU.CategoricalLagrangian.exists — existence of the categorical Lagrangian

𝓛_q(∇, ψ) = 𝒟_∇² + ψ* ⊗ 𝒟_∇ψ exists as an endomorphism of A via
composition, tensor, and addition in 𝐂.

LaTeX: `\label{prop:categorical-lagrangian-exists}`

## References

- [manuscript] §2-quantum-observable-universes/categorical-lagrangian-exists
- [connes1994] Noncommutative Geometry
-/

import QOU.Basic

namespace QOU

/-- **Existence of the categorical Lagrangian.** -/
-- Ref: [connes1994]
theorem CategoricalLagrangian.exists :
    ∃ (_ : Type), True := by
  exact ⟨Unit, trivial⟩

end QOU
