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

/-- **Uniqueness of the categorical action.**

    The rigid structure `(ev_A, coev_A)` is canonical; for fixed Φ,
    the action `𝒮_Φ = tr(Φ)` is therefore unique. -/
-- Ref: [kelly1982]
theorem CategoricalAction.unique
    {C : Type u} [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C]
    (fh : FrobeniusHopfData C) :
    Subsingleton (CategoricalAction C fh) := by
  -- Rigid structure canonical; trace unique up to canonical iso.
  -- Ref: [kelly1982]
  sorry

end QOU
