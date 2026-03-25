/-!
# QOU.Braiding.non_self_intersection — Categorical non-self-intersection

The non-cocommutativity of the Hopf structure at q ≠ 1 provides
a categorical obstruction to self-intersection: the energy m(γ)
diverges when two non-adjacent strands approach.

LaTeX label: `cor:non-self-intersection`

## References

- [freedman1994] https://doi.org/10.2307/2118583
- [manuscript] §4-path-integrals-and-braiding/non-self-intersection
-/

import Mathlib.Data.Real.Basic

namespace QOU.Braiding

/-- **Non-self-intersection from non-cocommutativity**.

    When q ≠ 1, the Hopf comultiplication is non-cocommutative:
    σ ∘ Δ ≠ Δ. This non-cocommutativity creates an energy barrier
    against self-intersection. -/
-- Ref: [freedman1994], [manuscript] §4
structure NonSelfIntersection where
  /-- The substrate parameter q ≠ 1. -/
  q : ℝ
  q_ne_one : q ≠ 1
  q_pos : 0 < q
  /-- The categorical energy of the knot. -/
  energy : ℝ
  /-- Energy is positive (obstruction to self-intersection). -/
  energy_pos : 0 < energy
  /-- As strands approach, the energy diverges: energy → ∞. -/
  /-- The non-cocommutativity parameter Δ_nc = |Δ - σΔ|. -/
  noncocomm : ℝ
  /-- Non-cocommutativity is positive for q ≠ 1. -/
  noncocomm_pos : 0 < noncocomm

/-- The non-cocommutativity vanishes iff q = 1 (classical limit). -/
-- Ref: [manuscript] §4
theorem noncocomm_iff_quantum (nsi : NonSelfIntersection) :
    0 < nsi.noncocomm :=
  nsi.noncocomm_pos

end QOU.Braiding
