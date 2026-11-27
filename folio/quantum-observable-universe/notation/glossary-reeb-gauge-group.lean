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
    to `TopologicalGroup.maximalTorus`.

    **`is_commutative : Prop` and `preserves_contact : Prop` removed 2026-09-07.
    Both were typed with the *universe* `Prop`, so an instance chose the
    proposition; neither was read or constructed anywhere. `Commutative` is
    statable once the group operation is a field; `preserves_contact` needs the
    contact form.** -/
-- Ref: [leitner2026] Ch. 8 Glossary
structure ReebGaugeGroup where
  /-- The R-group scheme carrier. -/
  carrier : Type*

end QOU
