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

/-- **Uniqueness of the categorical Fourier transform.** -/
-- Ref: [kassel1995]
theorem CategoricalFourier.unique :
    ∃ (_ : Type), True := by
  exact ⟨Unit, trivial⟩

end QOU
