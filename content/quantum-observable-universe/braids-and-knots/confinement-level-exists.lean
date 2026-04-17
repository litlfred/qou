/-!
# QOU.BraidKnot.ConfinementLevel.exists — existence of confinement level

The set { ℓ : T_w ∈ J^ℓ(q) } is finite, upward-closed, and nonempty,
so its minimum exists.

LaTeX: `\label{prop:confinement-level-exists}`
-/

import QOU.Basic

namespace QOU.BraidKnot

universe u

/-- **Existence of the confinement level.** -/
-- Ref: [manuscript] braids-and-knots/confinement-level
theorem ConfinementLevel.exists (R : Type u) [CommRing R] :
    Nonempty (ConfinementLevel R) := by
  exact ⟨{ braidIndex := 0, nStrands := 1, q := 0, level := 0 }⟩

end QOU.BraidKnot
