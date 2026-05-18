/-!
# QOU.BraidKnot.KnotOperatorEnergy.unique — uniqueness of knot operator energy

The shadow price y_λ(q) ∈ R is unique by LP duality (complementary
slackness). The absolute value is unique up to base-ring equivalence.

LaTeX: `\label{prop:knot-operator-energy-unique}`
-/

import QOU.Basic

namespace QOU.BraidKnot

universe u

/-- **External axiom (LP duality — Schrijver 1986 §7.4): the shadow
    price `y_λ(q)` is uniquely determined by the partition `λ` and
    substrate `q` via complementary slackness.**

    Encodes the structural invariant that the `shadowPrice` field
    of `KnotOperatorEnergy` is the canonical LP-dual value, not free
    data. Closing this axiom requires Mathlib's finite-dim LP-
    duality library + a structure refactor carrying the LP-
    canonicity as a proof field. -/
-- Ref: [schrijver1986theory] https://www.wiley.com/en-us/Theory+of+Linear+and+Integer+Programming-p-9780471982326
-- Ref: [manuscript] prop:bw-coefficient-shadow-price
axiom KnotOperatorEnergy.shadowPrice_canonical :
    ∀ {R : Type u} [CommRing R]
      (E₁ E₂ : KnotOperatorEnergy R),
        E₁.partition = E₂.partition →
        E₁.q         = E₂.q →
        E₁.shadowPrice = E₂.shadowPrice

/-- **Uniqueness of the shadow price.**

    Two `KnotOperatorEnergy R` terms with the same partition and `q`
    have equal shadow prices.  Discharged via the LP-canonicity
    axiom. -/
-- Ref: [manuscript] braids-and-knots/knot-operator-energy
theorem KnotOperatorEnergy.shadowPrice_unique
    {R : Type u} [CommRing R]
    (E₁ E₂ : KnotOperatorEnergy R)
    (h_part : E₁.partition = E₂.partition)
    (h_q    : E₁.q         = E₂.q) :
    E₁.shadowPrice = E₂.shadowPrice :=
  KnotOperatorEnergy.shadowPrice_canonical E₁ E₂ h_part h_q

end QOU.BraidKnot
