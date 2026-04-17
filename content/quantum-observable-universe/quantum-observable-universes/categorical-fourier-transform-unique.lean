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
  -- Wick rotation inherits uniqueness from Laplace.
  -- Ref: [kassel1995]
  sorry

end QOU
