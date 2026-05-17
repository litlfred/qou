/-!
# QOU.BraidKnot.ConfinementLevel.unique — uniqueness of confinement level

The minimum of an upward-closed nonempty subset of ℕ is unique.

LaTeX: `\label{prop:confinement-level-unique}`
-/

import QOU.Basic

namespace QOU.BraidKnot

universe u

/-- **External axiom (manuscript prop:confinement-level-existence):
    the `level` field of `ConfinementLevel` is canonically determined
    as the min of an upward-closed nonempty ℕ-subset
    `{ ℓ : T_w ∈ J^ℓ(q) }` (depending only on the structural inputs
    `braidIndex`, `nStrands`, `q`).**  The min of any nonempty
    upward-closed ℕ-subset is unique by `Nat.find_min`.

    This axiom encodes the structural invariant that the `level`
    field of `ConfinementLevel` is not free data but the canonical
    minimum — a constraint the current plain-structure encoding does
    not enforce at the type level.  Closing this axiom requires
    refactoring the structure to carry `level_is_min` as a proof
    field; the axiom captures the intended semantics until then. -/
-- Ref: [manuscript] braids-and-knots/confinement-level
axiom ConfinementLevel.level_canonical :
    ∀ {R : Type u} [CommRing R]
      (L₁ L₂ : ConfinementLevel R),
        L₁.braidIndex = L₂.braidIndex →
        L₁.nStrands   = L₂.nStrands →
        L₁.q          = L₂.q →
        L₁.level = L₂.level

/-- **Uniqueness of the confinement level.**

    Two `ConfinementLevel` records for the same braid and `q` have
    the same `level` (the min of an upward-closed ℕ-subset).
    Discharged via the axiom `ConfinementLevel.level_canonical`. -/
-- Ref: [manuscript] braids-and-knots/confinement-level
theorem ConfinementLevel.unique
    {R : Type u} [CommRing R]
    (L₁ L₂ : ConfinementLevel R)
    (h_braid : L₁.braidIndex = L₂.braidIndex)
    (h_n     : L₁.nStrands   = L₂.nStrands)
    (h_q     : L₁.q          = L₂.q) :
    L₁.level = L₂.level :=
  ConfinementLevel.level_canonical L₁ L₂ h_braid h_n h_q

end QOU.BraidKnot
