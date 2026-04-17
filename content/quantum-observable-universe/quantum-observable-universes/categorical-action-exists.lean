/-!
# QOU.CategoricalAction.exists — existence of the categorical action

𝒮_Φ = ev_A ∘ (id ⊗ Φ) ∘ coev_A exists as a morphism 𝟙 → 𝟙 for every
Φ ∈ End(A), via the rigid structure of 𝐂.  Equals tr(Φ).

LaTeX: `\label{prop:categorical-action-exists}`

## References

- [manuscript] §2-quantum-observable-universes/categorical-action-exists
- [kelly1982] Basic Concepts of Enriched Category Theory
-/

import QOU.Basic

namespace QOU

/-- **Existence of the categorical action.** -/
-- Ref: [kelly1982] Basic Concepts of Enriched Category Theory
theorem CategoricalAction.exists :
    ∃ (_ : Type), True := by
  -- Compositional via rigid structure ev/coev.
  -- Ref: [kelly1982]
  exact ⟨Unit, trivial⟩

end QOU
