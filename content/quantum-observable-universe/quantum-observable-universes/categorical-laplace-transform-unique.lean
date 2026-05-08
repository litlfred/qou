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

/-- **Uniqueness of the categorical Laplace transform.**

    The Laplace transform is the monoidal mate of Δ_q under the
    Frobenius pairing, hence unique up to canonical iso at the
    `CategoricalLaplace A` type level. -/
-- Ref: [kassel1995]
theorem CategoricalLaplace.unique (A : Type*) :
    Subsingleton (CategoricalLaplace A) := by
  -- DIAGNOSTIC: The `Subsingleton` claim is too strong. The underlying
  -- structure carries free fields (parameters / morphisms / opaque
  -- functions) that admit distinct valid values, so two instances
  -- need not coincide. To recover a meaningful uniqueness claim,
  -- sharpen with a constraining hypothesis (fixing the carrier
  -- object, fixing the substrate parameter, or quantifying over a
  -- quotient by structural equivalence) — see
  -- `frobenius-pairing-unique.lean` for the pattern. Sorry retained
  -- with this diagnosis rather than closed-as-stated.
  sorry

end QOU
