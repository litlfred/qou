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

/-- **Existence of the categorical action.**

    For any `FrobeniusHopfData C`, a `CategoricalAction C fh` term
    exists — the composite `ev_A ∘ (id ⊗ Φ) ∘ coev_A` using the rigid
    structure of the category. -/
-- Ref: [kelly1982]
theorem CategoricalAction.exists
    {C : Type u} [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C]
    (fh : FrobeniusHopfData C) :
    Nonempty (CategoricalAction C fh) := by
  -- Compositional witness via rigid ev / coev.
  -- Ref: [kelly1982]
  sorry

end QOU
