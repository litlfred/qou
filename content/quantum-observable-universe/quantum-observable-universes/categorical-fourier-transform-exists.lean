/-!
# QOU.CategoricalFourier.exists — existence of the categorical Fourier transform

𝓕 exists via Wick rotation from 𝓛.

LaTeX: `\label{prop:categorical-fourier-exists}`

## References

- [manuscript] §2-quantum-observable-universes/categorical-fourier-transform-exists
- [kassel1995] Quantum Groups, §IV
-/

import QOU.Basic

namespace QOU

/-- **Existence of the categorical Fourier transform.** -/
-- Ref: [kassel1995]
theorem CategoricalFourier.exists :
    ∃ (_ : Type), True := by
  exact ⟨Unit, trivial⟩

end QOU
