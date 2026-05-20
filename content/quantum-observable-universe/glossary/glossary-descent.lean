/-!
# QOU.DescentData — Glossary: descent

Descent is the reverse traversal of the brane tower: from level n
to level n-1 via the restriction morphism.

LaTeX label: `rem:glossary-descent`
-/

namespace QOU

/-- Descent data: restriction from brane level n to level n-1.

    Maps to Mathlib: analogous to `CategoryTheory.EffectiveEpiFamily`
    or descent data in a fibered category. -/
-- Ref: [manuscript] Ch. 8 Glossary
-- Ref: [lurie2009] Lurie, "On the Classification of Topological Field Theories," arXiv:0905.0465
structure DescentData where
  /-- Source brane level. -/
  level : ℕ
  /-- The restriction morphism r_n : A_n → A_{n-1} exists. -/
  restriction_exists : Prop

end QOU
