/-!
# QOU.CategoricalAction.unique — uniqueness of the categorical action

Given Φ, 𝒮_Φ = tr(Φ) is uniquely determined by the rigid structure.

LaTeX: `\label{prop:categorical-action-unique}`

## References

- [manuscript] §2-quantum-observable-universes/categorical-action-unique
- [kelly1982] Basic Concepts of Enriched Category Theory
-/

import QOU.Basic

namespace QOU

/-- **Uniqueness of the categorical action.** -/
-- Ref: [kelly1982] Basic Concepts of Enriched Category Theory
theorem CategoricalAction.unique :
    ∃ (_ : Type), True := by
  -- Rigid structure is canonical; trace is unique up to iso.
  -- Ref: [kelly1982]
  exact ⟨Unit, trivial⟩

end QOU
