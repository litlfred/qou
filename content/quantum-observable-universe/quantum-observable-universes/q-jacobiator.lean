import Mathlib.Algebra.Field.Basic

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

**Ground ring**: the formal data is stated over a generic field `R`
so that the inverse `q⁻¹` appearing in the Jacobiator coefficient is
available. The canonical specialisation is `R = ℝ` with `q ↦ q₀`
(the substrate parameter) for numerical evaluation; the formula is
field-generic, so any choice of evaluation ring (e.g. the fraction
field of `ℤ[q, q⁻¹]`) is admissible.
-/

namespace QOU

/-- **q-Jacobiator data**: the geometric inputs to the failure of the
    Jacobi identity for the q-deformed bracket — the substrate
    parameter `q`, the three cyclic Levi-form values `dθ(·,·)`, and
    the three Lie derivatives `ℒ_ξ(·)`. -/
structure QJacobiator (R : Type*) [Field R] where
  /-- The substrate parameter q. -/
  q : R
  /-- The Levi form value dθ(V,W). -/
  levi_form_VW : R
  /-- The Levi form value dθ(W,U). -/
  levi_form_WU : R
  /-- The Levi form value dθ(U,V). -/
  levi_form_UV : R
  /-- The Lie derivative ℒ_ξ U. -/
  lie_U : R
  /-- The Lie derivative ℒ_ξ V. -/
  lie_V : R
  /-- The Lie derivative ℒ_ξ W. -/
  lie_W : R

/-- The Jacobiator value:
    `Jac_q(U,V,W) = -q⁻¹(1-q⁻¹) · Σ_cyc dθ(V,W) · ℒ_ξ U`. -/
def QJacobiator.value {R : Type*} [Field R] (j : QJacobiator R) : R :=
  -j.q⁻¹ * (1 - j.q⁻¹) *
    (j.levi_form_VW * j.lie_U + j.levi_form_WU * j.lie_V + j.levi_form_UV * j.lie_W)

/-- The Jacobiator vanishes at q = 1 (classical Lie algebra). -/
theorem jacobiator_classical {R : Type*} [Field R] (j : QJacobiator R)
    (hq : j.q = 1) : j.value = 0 := by
  unfold QJacobiator.value
  rw [hq]; simp

/-- The Jacobiator is non-zero for q ≠ 1 (and q ≠ 0) when the cyclic
    Levi-form sum is non-degenerate (the fields are not all
    Reeb-invariant). -/
theorem jacobiator_nonzero {R : Type*} [Field R] (j : QJacobiator R)
    (hq : j.q ≠ 1) (hq0 : j.q ≠ 0)
    (h_cyclic :
      j.levi_form_VW * j.lie_U +
      j.levi_form_WU * j.lie_V +
      j.levi_form_UV * j.lie_W ≠ 0) :
    j.value ≠ 0 := by
  unfold QJacobiator.value
  apply mul_ne_zero
  apply mul_ne_zero
  · exact neg_ne_zero.mpr (inv_ne_zero hq0)
  · rw [sub_ne_zero]
    intro h
    exact hq (by rw [← inv_inv j.q, ← h, inv_one])
  · exact h_cyclic

/-- The Leibniz coefficient `q⁻¹(1 - q⁻¹)` of the q-bracket exists in
    the ground field. -/
theorem leibniz_coeff_exists {R : Type*} [Field R] (j : QJacobiator R) :
    ∃ c : R, c = j.q⁻¹ * (1 - j.q⁻¹) :=
  ⟨j.q⁻¹ * (1 - j.q⁻¹), rfl⟩

end QOU
