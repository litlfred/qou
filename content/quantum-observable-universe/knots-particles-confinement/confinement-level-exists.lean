import QOU.BraidKnot.ConfinementLevel


/-!
# QOU.BraidKnot.ConfinementLevel.exists — existence of confinement level

The set { ℓ : T_w ∈ J^ℓ(q) } is finite, upward-closed, and nonempty,
so its minimum exists.

LaTeX: `\label{prop:confinement-level-exists}`

**Canonical declaration.** The theorem `QOU.BraidKnot.ConfinementLevel.exists`
is proved in the compiled library module `QOU.BraidKnot.ConfinementLevel`
(imported above), which the `.ts` manifest's `lean.ref` resolves to. This
content-extract file confirms the canonical statement is in scope rather than
shadowing it with a re-declaration (AGENTS.md §0a no-shadowing-stubs).
-/

namespace QOU.BraidKnot

-- Witness that the canonical existence theorem is in scope (no re-declaration).
-- canonical decl: QOU.BraidKnot.ConfinementLevel.exists
-- Ref: [manuscript] braids-and-knots/confinement-level
example (R : Type) [CommRing R] : Nonempty (ConfinementLevel R) :=
  ConfinementLevel.exists R

end QOU.BraidKnot
