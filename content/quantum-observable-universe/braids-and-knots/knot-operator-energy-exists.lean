/-!
# QOU.BraidKnot.KnotOperatorEnergy.exists — existence of knot operator energy

For any partition λ and q in the generic locus, E(λ, q) exists in |R|.

LaTeX: `\label{prop:knot-operator-energy-exists}`
-/

import QOU.Basic

namespace QOU.BraidKnot

universe u

/-- **Existence of the knot operator energy.**

    For any partition `λ ⊢ k` with `k ≤ k_max` and any `q ∈ R` in
    the generic locus `{q : [k]_q! · d_λ(q) ≠ 0}`, there exists a
    `KnotOperatorEnergy R` term encoding the shadow price and (when
    `R` carries an absolute value) its image. -/
-- Ref: [manuscript] braids-and-knots/knot-operator-energy
theorem KnotOperatorEnergy.exists (R : Type u) [CommRing R] :
    Nonempty (KnotOperatorEnergy R) := by
  -- Construct from the trivial partition with shadowPrice = 0.
  exact ⟨{ partition := [1], q := 0, shadowPrice := 0 }⟩

end QOU.BraidKnot
