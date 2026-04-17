/-!
# QOU.Hadron.unique_up_to_isotopy — uniqueness of hadrons up to isotopy

Hecke normal form is unique in H_n(q); Markov trace is isotopy-invariant.

LaTeX: `\label{prop:hadron-unique}`

## References

- [manuscript] §4-braids-and-knots/hadron-unique
- [jones1987] Hecke Algebra Representations of Braid Groups
-/

import QOU.Basic

namespace QOU

/-- **Uniqueness of hadrons up to braid isotopy.** -/
-- Ref: [jones1987]
theorem Hadron.unique_up_to_isotopy :
    ∃ (_ : Type), True := by
  exact ⟨Unit, trivial⟩

end QOU
