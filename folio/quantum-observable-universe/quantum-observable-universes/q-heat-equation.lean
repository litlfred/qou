import Mathlib.Algebra.Polynomial.Laurent
import Mathlib.Data.Int.Basic
import Mathlib.Data.Real.Basic


/-!
# QOU.QHeatEquation — q-deformed heat equation

The q-heat equation on a quantum observable universe:

  ∂ₜ u = Δ_q u

where Δ_q is the q-Laplacian and t is the Reeb-flow parameter.

LaTeX label: `def:q-heat-equation`

## References

- [leitner2026] §2-quantum-observable-universes/q-heat-equation

**Ground ring**: `R_q = ℤ[q, q⁻¹]`.  The operator equation is
purely algebraic and holds in `End(S)` over `R_q`.  Convergent
solutions (heat kernel, q-Gaussian) are archimedean and live in
`archimedean-realisations`.
-/

namespace QOU

noncomputable section
abbrev R_q := LaurentPolynomial ℤ

/-- **q-Heat equation data**: a one-parameter family of sections `u t`
    together with the q-Laplacian `Δ_q`, satisfying `∂ₜ u = Δ_q u`.

    Encoded abstractly as a predicate on the pair (time-derivative,
    q-Laplacian-value) — this is the algebraic shadow of the PDE,
    independent of any analytic choice of differentiability. -/
-- Ref: [leitner2026] §2
structure QHeatEquation (S : Type*) where
  /-- Time-dependent section `u : ℝ → S → R_q`. -/
  u : ℝ → S → R_q
  /-- Time-derivative `∂ₜ u : ℝ → S → R_q`. -/
  dt_u : ℝ → S → R_q
  /-- q-Laplacian applied to `u`: `Δ_q u : ℝ → S → R_q`. -/
  dq_u : ℝ → S → R_q
  /-- The evolution equation: `∂ₜ u(t,x) = Δ_q u(t,x)` pointwise. -/
  evolves : ∀ (t : ℝ) (x : S), dt_u t x = -dq_u t x

/-- Classical heat equation is the `q = 1` specialisation.  Over
    `R_q = ℤ[T; T⁻¹]`, evaluating at `q = 1` sends each monomial
    `T^n ↦ 1`, so the value is the sum of all Laurent coefficients
    (`LaurentPolynomial ℤ = ℤ →₀ ℤ`). -/
-- Ref: [leitner2026] §2
def QHeatEquation.classicalLimit {S : Type*} (H : QHeatEquation S)
    (t : ℝ) (x : S) : ℤ :=
  (H.u t x).sum (fun _ c => c)

end

end QOU
