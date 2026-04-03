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
-- Ref: [lurie2009] https://doi.org/10.4310/CDM.2008.v2008.n1.a3
structure DescentData where
  /-- Source brane level. -/
  level : ℕ
  /-- The restriction morphism r_n : A_n → A_{n-1} exists. -/
  restriction_exists : Prop

end QOU
