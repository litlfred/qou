/-!
# QOU.BraidKnot.LocalShadowOrdering — local ≤_q ordering of shadow prices

A ≤_q B iff |y_A(q')| ≤ |y_B(q')| on a neighborhood of q.

LaTeX: `\label{def:local-shadow-ordering}`
-/

import QOU.Basic

namespace QOU.BraidKnot

universe u

/-- **Local shadow-price ordering** at point `q : R`.

    `LocalShadowOrdering R` records two partitions and the proposition
    that the second has at-least-equal shadow-price magnitude on a
    neighborhood of `q`.  The "neighborhood" is a topological
    formalisation requiring `R` to carry a topology — for `ℝ`, this is
    the Euclidean topology; for `ℚ_p`, the `p`-adic topology. -/
structure LocalShadowOrdering (R : Type u) [CommRing R] where
  /-- Partition λ₁ ⊢ k₁. -/
  partition_low  : List ℕ
  /-- Partition λ₂ ⊢ k₂. -/
  partition_high : List ℕ
  /-- Substrate parameter at which the ordering is asserted. -/
  q : R
  /-- The ordering holds on a neighborhood of `q`.
      Stub: requires `R` to carry a topology to formalise. -/
  holds_on_neighborhood : Prop := True

end QOU.BraidKnot
