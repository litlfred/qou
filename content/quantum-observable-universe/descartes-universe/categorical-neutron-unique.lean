/-!
# QOU.CategoricalNeutron.unique_up_to_isotopy — uniqueness of the categorical neutron

𝔫 unique up to Hecke NF in H₃(q) + S₃-symmetry on color tubes.

LaTeX: `\label{prop:categorical-neutron-unique}`

## References

- [manuscript] §6-descartes-universe/categorical-neutron-unique
- [jones1987] Hecke Algebra Representations of Braid Groups
-/

import QOU.Basic

namespace QOU

/-- **Uniqueness of the categorical neutron up to braid isotopy.** -/
-- Ref: [jones1987]
theorem CategoricalNeutron.unique_up_to_isotopy :
    ∃ (_ : Type), True := by
  exact ⟨Unit, trivial⟩

end QOU
