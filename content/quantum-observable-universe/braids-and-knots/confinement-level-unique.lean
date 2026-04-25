/-!
# QOU.BraidKnot.ConfinementLevel.unique — uniqueness of confinement level

The minimum of an upward-closed nonempty subset of ℕ is unique.

LaTeX: `\label{prop:confinement-level-unique}`
-/

import QOU.Basic

namespace QOU.BraidKnot

universe u

/-- **Uniqueness of the confinement level.**

    Two `ConfinementLevel` records for the same braid and `q` have
    the same `level` (the min of an upward-closed ℕ-subset). -/
-- Ref: [manuscript] braids-and-knots/confinement-level
theorem ConfinementLevel.unique
    {R : Type u} [CommRing R]
    (L₁ L₂ : ConfinementLevel R)
    (h_braid : L₁.braidIndex = L₂.braidIndex)
    (h_n     : L₁.nStrands   = L₂.nStrands)
    (h_q     : L₁.q          = L₂.q) :
    L₁.level = L₂.level := by
  -- Min of upward-closed nonempty ℕ-subset is unique.
  -- Ref: [manuscript] confinement-level-unique
  sorry

end QOU.BraidKnot
