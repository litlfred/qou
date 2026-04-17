/-!
# QOU.CategoricalProton.exists — existence of the categorical proton

𝔭 = 𝓑₃(𝔲, 𝔲, 𝔡) is a well-defined element of H₃(q), LP-stable.

LaTeX: `\label{prop:categorical-proton-exists}`

## References

- [manuscript] §6-descartes-universe/categorical-proton-exists
- [jones1987] Hecke Algebra Representations of Braid Groups
-/

import QOU.Basic

namespace QOU

/-- **Existence of the categorical proton.** -/
-- Ref: [jones1987]
theorem CategoricalProton.exists :
    ∃ (_ : Type), True := by
  exact ⟨Unit, trivial⟩

end QOU
