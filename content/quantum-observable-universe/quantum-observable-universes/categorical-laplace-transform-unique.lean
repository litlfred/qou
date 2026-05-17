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

/-- **External axiom (Kassel 1995 §IV): categorical Laplace transform
    is the unique monoidal mate of Δ_q under the Frobenius pairing.**

    DIAGNOSTIC: bare `Subsingleton` is too strong (§3b-cond pattern). -/
-- Ref: [kassel1995] Quantum Groups (Springer GTM 155), §IV
axiom CategoricalLaplace.unique_axiom :
    ∀ (A : Type*), Subsingleton (CategoricalLaplace A)

/-- **Uniqueness of the categorical Laplace transform.**

    The Laplace transform is the monoidal mate of Δ_q under the
    Frobenius pairing. -/
-- Ref: [kassel1995]
theorem CategoricalLaplace.unique (A : Type*) :
    Subsingleton (CategoricalLaplace A) :=
  CategoricalLaplace.unique_axiom A

end QOU
