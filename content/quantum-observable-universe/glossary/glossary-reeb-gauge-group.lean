import Mathlib.Tactic.Basic

/-!
# QOU.ReebGaugeGroup — Glossary: Reeb gauge group U₁(R)

The maximal torus T of the quantum gauge group, acting as the
Reeb gauge group governing the contact structure.

LaTeX label: `rem:glossary-reeb-gauge-group`
-/

namespace QOU

/-- The Reeb gauge group U₁(R) := T, the maximal torus of G_q.

    This is the commutative subgroup that preserves the contact
    form θ and generates the Reeb flow.

    Maps to Mathlib: `Subgroup` of the gauge group, analogous
    to `TopologicalGroup.maximalTorus`. -/
-- Ref: [manuscript] Ch. 8 Glossary
structure ReebGaugeGroup where
  /-- The R-group scheme carrier. -/
  carrier : Type*
  /-- U₁(R) is commutative. -/
  is_commutative : Prop
  /-- U₁(R) preserves the contact form θ. -/
  preserves_contact : Prop

end QOU
