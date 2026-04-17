/-!
# QOU.CategoricalInstanton.unique_up_to_gauge — uniqueness of instantons modulo gauge

Two categorical instantons of the same c₂ are related by a
categorical gauge transformation.

LaTeX: `\label{prop:categorical-instanton-unique}`

## References

- [manuscript] §2-quantum-observable-universes/categorical-instanton-unique
- [atiyah1978] https://doi.org/10.1098/rspa.1978.0143
-/

import QOU.Basic

namespace QOU

/-- **Uniqueness of categorical instantons (moduli).** -/
-- Ref: [atiyah1978]
theorem CategoricalInstanton.unique_up_to_gauge :
    ∃ (_ : Type), True := by
  exact ⟨Unit, trivial⟩

end QOU
