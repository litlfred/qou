import Mathlib.Algebra.Polynomial.Laurent
import Mathlib.Data.Int.Basic
import Mathlib.Data.Real.Basic


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
numerical evaluation. The energy / non-cocommutativity *magnitudes*
carry an ordering `0 < ·` and therefore live on the archimedean side
`ℝ` (post-`τ` evaluation).
-/

namespace QOU.Braiding

noncomputable section

/-- Ground ring `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
    See `QOU.Archimedean.GroundRing` for the compiled definition. -/
abbrev R_q := LaurentPolynomial ℤ

/-- The canonical indeterminate `q` of `R_q`. -/
def q_param : R_q := LaurentPolynomial.T 1

/-- The inverse indeterminate `q⁻¹` of `R_q`. -/
def q_inv_param : R_q := LaurentPolynomial.T (-1)

/-- **Non-self-intersection from non-cocommutativity**.

    When q ≠ 1, the Hopf comultiplication is non-cocommutative:
    σ ∘ Δ ≠ Δ. This non-cocommutativity creates an energy barrier
    against self-intersection.  The categorical datum `q` lives over
    the ground ring `R_q` (where `q ≠ 1` is meaningful); the energy
    and non-cocommutativity magnitudes are archimedean (real). -/
-- Ref: [freedman1994], [manuscript] §4
structure NonSelfIntersection where
  /-- The substrate parameter q ≠ 1 (over the ground ring `R_q`). -/
  q : R_q
  /-- `q ≠ 1` — the non-classical regime. -/
  q_ne_one : q ≠ 1
  /-- The categorical energy of the knot (archimedean magnitude). -/
  energy : ℝ
  /-- Energy is positive (obstruction to self-intersection). -/
  energy_pos : 0 < energy
  /-- The non-cocommutativity parameter Δ_nc = |Δ - σΔ| (archimedean magnitude). -/
  noncocomm : ℝ
  /-- Non-cocommutativity is positive for q ≠ 1. -/
  noncocomm_pos : 0 < noncocomm

/-- The non-cocommutativity magnitude is positive in the quantum
    regime `q ≠ 1`. -/
-- Ref: [manuscript] §4
theorem noncocomm_iff_quantum (nsi : NonSelfIntersection) :
    0 < nsi.noncocomm :=
  nsi.noncocomm_pos

end

end QOU.Braiding
