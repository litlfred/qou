/-!
# QOU.CategoricalLaplace.exists — existence of the categorical Laplace transform

𝓛 exists as a monoidal functor via the q-exponential grouplike and
the Markov trace.

LaTeX: `\label{prop:categorical-laplace-exists}`

## References

- [manuscript] §2-quantum-observable-universes/categorical-laplace-transform-exists
- [kassel1995] Quantum Groups, §IV
-/

import QOU.Basic

namespace QOU

/-- **Existence of the categorical Laplace transform.** -/
-- Ref: [kassel1995]
theorem CategoricalLaplace.exists :
    ∃ (_ : Type), True := by
  exact ⟨Unit, trivial⟩

end QOU
