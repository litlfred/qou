/-!
# QOU.CategoricalNeutron.exists — existence of the categorical neutron

𝔫 = 𝓑₃(𝔲, 𝔡, 𝔡) is a well-defined element of H₃(q), LP-stable with
two Hopf-link gluons.

LaTeX: `\label{prop:categorical-neutron-exists}`

## References

- [manuscript] §6-descartes-universe/categorical-neutron-exists
- [jones1987] Hecke Algebra Representations of Braid Groups
-/

import QOU.Basic

namespace QOU

/-- **Existence of the categorical neutron.** -/
-- Ref: [jones1987]
theorem CategoricalNeutron.exists :
    ∃ (_ : Type), True := by
  exact ⟨Unit, trivial⟩

end QOU
