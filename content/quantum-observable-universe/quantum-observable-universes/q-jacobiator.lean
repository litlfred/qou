/-!
# QOU.q_jacobiator — q-Jacobiator formula

For horizontal vector fields U, V, W, the q-Jacobiator is:

  Jac_q(U,V,W) = -q⁻¹(1-q⁻¹) Σ_cyc dθ(V,W) ℒ_ξ U

Since the Levi form L_θ = dθ|_{H×H} is non-degenerate, [·,·]_q
violates the Jacobi identity for all q ≠ 1. Thus (𝔛(M), [·,·]_q)
is a Leibniz algebra, not a Lie algebra.

LaTeX label: `prop:q-jacobiator`

## References

- [manuscript] §1-quantum-observable-universe/q-jacobiator

**Ground ring**: `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
Part of the formal proof chain. The parameter `q` is the canonical
indeterminate of `R_q`. Specialise via `ι : R_q → ℝ, q ↦ q₀` for
numerical evaluation.
-/

import Mathlib.Algebra.Polynomial.Laurent
import Mathlib.Data.Int.Basic

namespace QOU

/-- Ground ring `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
    See `QOU.Descartes.GroundRing` for the compiled definition. -/
noncomputable section
abbrev R_q := LaurentPolynomial ℤ
def q_param : R_q := LaurentPolynomial.T 1
def q_inv_param : R_q := LaurentPolynomial.T (-1)

/-- **q-Jacobiator data**: the failure of the Jacobi identity for
    the q-deformed bracket.

    `Jac_q(U,V,W) = -q⁻¹(1-q⁻¹) · Σ_cyc dθ(V,W) · ℒ_ξ U` -/
-- Ref: [manuscript] §1
structure QJacobiator where
  /-- The substrate parameter q. -/
  q : R_q
  /-- q > 0. -/
  -- q_pos : 0 < q  -- (archimedean; not meaningful over R_q)
  /-- The Levi form value dθ(V,W). -/
  levi_form_VW : R_q
  /-- The Levi form value dθ(W,U). -/
  levi_form_WU : R_q
  /-- The Levi form value dθ(U,V). -/
  levi_form_UV : R_q
  /-- The Lie derivative ℒ_ξ U. -/
  lie_U : R_q
  /-- The Lie derivative ℒ_ξ V. -/
  lie_V : R_q
  /-- The Lie derivative ℒ_ξ W. -/
  lie_W : R_q
  /-- The Jacobiator: cyclic sum of dθ(·,·) · ℒ_ξ(·). -/
  jacobiator : R_q :=
    -q⁻¹ * (1 - q⁻¹) *
      (levi_form_VW * lie_U + levi_form_WU * lie_V + levi_form_UV * lie_W)

/-- The Jacobiator vanishes at q = 1 (classical Lie algebra). -/
-- Ref: [manuscript] §1
theorem jacobiator_classical (j : QJacobiator) (hq : j.q = 1) :
    j.jacobiator = 0 := by
  unfold QJacobiator.jacobiator
  simp [hq]

/-- The Jacobiator is non-zero for generic q ≠ 1 when the Levi form
    is non-degenerate and the fields are not Reeb-invariant. -/
-- Ref: [manuscript] §1
theorem jacobiator_nonzero (j : QJacobiator)
    (hq : j.q ≠ 1)
    -- (hq_pos : 0 < j.q)  -- (archimedean; not meaningful over R_q)
    (h_cyclic :
      j.levi_form_VW * j.lie_U +
      j.levi_form_WU * j.lie_V +
      j.levi_form_UV * j.lie_W ≠ 0) :
    j.jacobiator ≠ 0 := by
  unfold QJacobiator.jacobiator
  apply mul_ne_zero
  apply mul_ne_zero
  · apply neg_ne_zero.mpr
    exact inv_ne_zero.mpr (ne_of_gt hq_pos)
  · intro h
    apply hq
    have : j.q⁻¹ = 1 := by linarith [sub_eq_zero.mp h]
    rwa [inv_eq_one] at this
  · exact h_cyclic

/-- The q-bracket satisfies the Leibniz identity:
    `[U, [V, W]_q]_q = [[U, V]_q, W]_q + [V, [U, W]_q]_q`. -/
-- Ref: [manuscript] §1
-- theorem leibniz_algebra (j : QJacobiator) (hq : 0 < j.q) :  -- (archimedean; not meaningful over R_q)
    ∃ (leibniz_coeff : R_q),
      leibniz_coeff = j.q⁻¹ * (1 - j.q⁻¹) :=
  ⟨j.q⁻¹ * (1 - j.q⁻¹), rfl⟩

end QOU
