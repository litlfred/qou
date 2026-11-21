import QOU.BraidKnot.ConfinementLevel


/-!
# QOU.BraidKnot.ConfinementLevel.nonempty — existence of confinement level (the library theorem was renamed from `exists` to `nonempty`; re-pointed 2026-09-04)

The set { ℓ : T_w ∈ J^ℓ(q) } is finite, upward-closed, and nonempty,
so its minimum exists.

LaTeX: `\label{prop:confinement-level-exists}`

**Canonical declaration.** The theorem `QOU.BraidKnot.ConfinementLevel.nonempty`
is proved in the compiled library module `QOU.BraidKnot.ConfinementLevel`
(imported above), which the `.ts` manifest's `lean.ref` resolves to. This
content-extract file confirms the canonical statement is in scope rather than
shadowing it with a re-declaration (AGENTS.md §0a no-shadowing-stubs).
-/

namespace QOU.BraidKnot

-- Witness that the canonical existence theorem is in scope (no re-declaration).
-- canonical decl: QOU.BraidKnot.ConfinementLevel.nonempty
-- Ref: [leitner2026] braids-and-knots/confinement-level
example (R : Type) [CommRing R] (valid : BraidDatum R → ℕ → Prop)
    (d : BraidDatum R) [DecidablePred (valid d)] (h : ∃ ℓ, valid d ℓ) :
    Nonempty (ConfinementLevel valid d) :=
  ConfinementLevel.nonempty h

end QOU.BraidKnot
