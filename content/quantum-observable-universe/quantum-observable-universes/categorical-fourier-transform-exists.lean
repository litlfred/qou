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

/-- **Existence of the categorical Fourier transform.**

    For any types `A` and `Irreps`, a `CategoricalFourier A Irreps`
    term exists — via Wick rotation of the Laplace transform. -/
-- Ref: [kassel1995]
theorem CategoricalFourier.exists
    (A : Type*) (Irreps : Type*) [Nonempty A] [Nonempty Irreps] :
    Nonempty (CategoricalFourier A Irreps) := by
  -- Witness: Wick rotation 𝓕[f](ξ) = 𝓛[f](-iξ) + Peter-Weyl.
  -- Ref: [kassel1995]
  sorry

end QOU
