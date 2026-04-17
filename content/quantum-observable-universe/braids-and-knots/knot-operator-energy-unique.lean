/-!
# QOU.BraidKnot.KnotOperatorEnergy.unique — uniqueness of knot operator energy

The shadow price y_λ(q) ∈ R is unique by LP duality (complementary
slackness). The absolute value is unique up to base-ring equivalence.

LaTeX: `\label{prop:knot-operator-energy-unique}`
-/

import QOU.Basic

namespace QOU.BraidKnot

universe u

/-- **Uniqueness of the shadow price.**

    Two `KnotOperatorEnergy R` terms with the same partition and `q`
    have equal shadow prices.  Proof: by LP duality, the dual variable
    for each binding constraint is unique. -/
-- Ref: [manuscript] braids-and-knots/knot-operator-energy
theorem KnotOperatorEnergy.shadowPrice_unique
    {R : Type u} [CommRing R]
    (E₁ E₂ : KnotOperatorEnergy R)
    (h_part : E₁.partition = E₂.partition)
    (h_q    : E₁.q         = E₂.q) :
    E₁.shadowPrice = E₂.shadowPrice := by
  -- LP duality: dual variable per binding constraint is unique.
  -- Ref: [manuscript] prop:bw-coefficient-shadow-price
  sorry

end QOU.BraidKnot
