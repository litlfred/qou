/-!
# QOU.CategoricalFourier.unique — uniqueness of the categorical Fourier transform

𝓕 is unique by Wick rotation of 𝓛 + Peter-Weyl uniqueness.

LaTeX: `\label{prop:categorical-fourier-unique}`

## References

- [manuscript] §2-quantum-observable-universes/categorical-fourier-transform-unique
- [kassel1995] Quantum Groups, §IV
-/

import QOU.Basic

namespace QOU

/-- **Uniqueness of the categorical Fourier transform.**

    Inherits uniqueness from the Laplace transform via Wick rotation;
    Peter-Weyl pins down the irrep labelling up to permutation. -/
-- Ref: [kassel1995]
theorem CategoricalFourier.unique (A : Type*) (Irreps : Type*) :
    Subsingleton (CategoricalFourier A Irreps) := by
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
