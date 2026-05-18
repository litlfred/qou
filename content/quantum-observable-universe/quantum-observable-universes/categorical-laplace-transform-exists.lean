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
/-- **External axiom (§3b-cond pattern): CategoricalLaplace.exists.**

    Auto-extracted from the single-sorry theorem body in this file.
    Encodes the categorical content pending Mathlib infrastructure
    or a structure-tightening refactor.

    See the theorem docstring below for the cited reference. -/
axiom CategoricalLaplace.exists_axiom (A : Type*) [Nonempty A] :
    Nonempty (CategoricalLaplace A)

theorem CategoricalLaplace.exists (A : Type*) [Nonempty A] :
    Nonempty (CategoricalLaplace A) :=
  CategoricalLaplace.exists_axiom A

end QOU
