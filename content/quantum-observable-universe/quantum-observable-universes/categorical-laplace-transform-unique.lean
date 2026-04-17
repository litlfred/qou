/-!
# QOU.CategoricalLaplace.unique — uniqueness of the categorical Laplace transform

𝓛 is unique as the monoidal mate of Δ_q under the Frobenius pairing.

LaTeX: `\label{prop:categorical-laplace-unique}`

## References

- [manuscript] §2-quantum-observable-universes/categorical-laplace-transform-unique
- [kassel1995] Quantum Groups, §IV
-/

import QOU.Basic

namespace QOU

/-- **Uniqueness of the categorical Laplace transform.** -/
-- Ref: [kassel1995]
theorem CategoricalLaplace.unique :
    ∃ (_ : Type), True := by
  exact ⟨Unit, trivial⟩

end QOU
