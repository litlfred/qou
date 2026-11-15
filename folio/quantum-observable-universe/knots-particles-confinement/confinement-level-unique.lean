import QOU.Basic
import QOU.BraidKnot.ConfinementLevel

/-!
# QOU.BraidKnot.ConfinementLevel.unique — uniqueness of the confinement level

The canonical statement lives in `QOU.BraidKnot.ConfinementLevel` (imported
above), which the `.ts` manifest's `lean.ref` resolves to. This content-extract
file confirms the canonical statement is in scope rather than shadowing it with
a re-declaration (AGENTS.md §0a no-shadowing-stubs).

**This file previously carried `axiom ConfinementLevel.level_canonical` and
derived `unique` from it.** That axiom was FALSE — the old plain structure had
`level` as a free field, so `⟨0,0,0,0⟩` and `⟨0,0,0,1⟩` agreed on
`braidIndex`, `nStrands` and `q` while differing in `level`. Both are gone;
`unique` is now a one-line theorem over the refactored structure, depending on
no axioms at all. Bean `qou-i6u4`.

LaTeX: `\label{prop:confinement-level-unique}`
-/

namespace QOU.BraidKnot

-- Witness that the canonical uniqueness theorem is in scope (no re-declaration).
-- canonical decl: QOU.BraidKnot.ConfinementLevel.unique
-- Ref: [leitner2026] braids-and-knots/confinement-level
example (R : Type) [CommRing R] (valid : BraidDatum R → ℕ → Prop)
    (d : BraidDatum R) (L₁ L₂ : ConfinementLevel valid d) :
    L₁.level = L₂.level :=
  ConfinementLevel.unique L₁ L₂

end QOU.BraidKnot
