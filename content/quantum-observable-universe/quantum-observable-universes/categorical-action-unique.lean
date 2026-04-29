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

/-- **Uniqueness of the categorical action — open statement.**

    For fixed `Φ`, the rigid trace `𝒮_Φ = tr(Φ)` is canonical. The
    `Subsingleton (CategoricalAction C fh)` claim originally written
    here is **strictly false** because the `CategoricalAction`
    structure exposes free fields:

      `state : 𝟙 → A`     (no constraint)
      `gravity : 𝟙 → 𝟙`   (no constraint)
      `gauge   : 𝟙 → 𝟙`   (no constraint)
      `matter  : 𝟙 → 𝟙`   (no constraint)
      `connection : CategoricalConnection C fh`  (also has free fields)

    Different choices give different actions, all equally valid as
    `CategoricalAction` terms. Subsingleton therefore cannot hold.

    To recover a meaningful uniqueness theorem, the
    `CategoricalAction` scaffold must be tightened so that
    gravity/gauge/matter are *defined* in terms of `connection +
    state` via the rigid trace formula, not held as free fields. The
    `variational_*` theorems in `categorical-action.lean` are the
    Euler-Lagrange equations these definitions would satisfy.

    Until the scaffold is tightened, the honest disposition is to
    leave this `sorry` with a clear note rather than close-as-written
    (which would be a false claim). -/
-- Ref: [kelly1982]
theorem CategoricalAction.unique
    {C : Type u} [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C]
    (fh : FrobeniusHopfData C) :
    Subsingleton (CategoricalAction C fh) := by
  -- The original Subsingleton claim is too strong (see docstring).
  -- Sharpening requires tightening the CategoricalAction scaffold.
  sorry  -- Ref: [kelly1982] — but theorem needs scaffold revision; see docstring

end QOU
