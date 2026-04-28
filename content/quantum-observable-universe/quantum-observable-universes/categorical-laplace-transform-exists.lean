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

/-- **Existence of the categorical Laplace transform.**

    For any type `A`, a `CategoricalLaplace A` term exists —
    witnessed by the Markov pairing against `exp_q(-s·)`. -/
-- Ref: [kassel1995]
theorem CategoricalLaplace.exists (A : Type*) [Nonempty A] :
    Nonempty (CategoricalLaplace A) := by
  -- Witness: 𝓛[f](s) = tr_M(exp_q(-s·) · f).
  -- Ref: [kassel1995]
  sorry

end QOU
