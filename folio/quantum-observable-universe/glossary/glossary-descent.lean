import Mathlib.Data.Nat.Basic
/-!
# QOU.DescentData — Glossary: descent

Descent is the reverse traversal of the brane tower: from level n
to level n-1 via the restriction morphism.

LaTeX label: `rem:glossary-descent`
-/

namespace QOU

/-- Descent data: restriction from brane level n to level n-1.

    Maps to Mathlib: analogous to `CategoryTheory.EffectiveEpiFamily`
    or descent data in a fibered category.

    **`restriction_exists : Prop` removed 2026-09-07. It promised "the restriction
    morphism `r_n : A_n -> A_{n-1}` exists" and asserted nothing: typed with the
    *universe* `Prop`, so an instance chose the proposition and `True` was legal.
    Nothing read it and nothing constructed it. Stating it needs the morphism as
    a field, which this glossary wrapper does not carry.** -/
-- Ref: [leitner2026] Ch. 8 Glossary
-- Ref: [lurie2009] Lurie, "On the Classification of Topological Field Theories," arXiv:0905.0465
structure DescentData where
  /-- Source brane level. -/
  level : ℕ

end QOU
