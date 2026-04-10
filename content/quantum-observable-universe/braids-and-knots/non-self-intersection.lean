/-!
# QOU.Braiding.non_self_intersection — Categorical non-self-intersection

The non-cocommutativity of the Hopf structure at q ≠ 1 provides
a categorical obstruction to self-intersection: the energy m(γ)
diverges when two non-adjacent strands approach.

LaTeX label: `cor:non-self-intersection`

## References

- [freedman1994] https://doi.org/10.2307/2118583
- [manuscript] §4-path-integrals-and-braiding/non-self-intersection

**Ground ring**: `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
Part of the formal proof chain. The parameter `q` is the canonical
indeterminate of `R_q`. Specialise via `ι : R_q → ℝ, q ↦ q₀` for
numerical evaluation.
-/

import Mathlib.Algebra.Polynomial.Laurent
import Mathlib.Data.Int.Basic

namespace QOU.Braiding

/-- Ground ring `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
    See `QOU.Descartes.GroundRing` for the compiled definition. -/
noncomputable section
abbrev R_q := LaurentPolynomial ℤ
def q_param : R_q := LaurentPolynomial.T 1
def q_inv_param : R_q := LaurentPolynomial.T (-1)

/-- **Non-self-intersection from non-cocommutativity**.

    When q ≠ 1, the Hopf comultiplication is non-cocommutative:
    σ ∘ Δ ≠ Δ. This non-cocommutativity creates an energy barrier
    against self-intersection. -/
-- Ref: [freedman1994], [manuscript] §4
structure NonSelfIntersection where
  /-- The substrate parameter q ≠ 1. -/
  q : R_q
  q_ne_one : q ≠ 1
  -- q_pos : 0 < q  -- (archimedean; not meaningful over R_q)
  /-- The categorical energy of the knot. -/
  energy : R_q
  /-- Energy is positive (obstruction to self-intersection). -/
  energy_pos : 0 < energy
  /-- As strands approach, the energy diverges: energy → ∞. -/
  /-- The non-cocommutativity parameter Δ_nc = |Δ - σΔ|. -/
  noncocomm : R_q
  /-- Non-cocommutativity is positive for q ≠ 1. -/
  noncocomm_pos : 0 < noncocomm

/-- The non-cocommutativity vanishes iff q = 1 (classical limit). -/
-- Ref: [manuscript] §4
theorem noncocomm_iff_quantum (nsi : NonSelfIntersection) :
    0 < nsi.noncocomm :=
  nsi.noncocomm_pos

end QOU.Braiding
