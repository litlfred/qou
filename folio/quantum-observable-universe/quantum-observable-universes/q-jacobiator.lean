import Mathlib.Algebra.Ring.Basic
import Mathlib.Algebra.GroupWithZero.Units.Basic

/-!
# QOU.q_jacobiator — q-Jacobiator formula

For horizontal vector fields U, V, W, the q-Jacobiator is:

  Jac_q(U,V,W) = -q⁻¹(1-q⁻¹) Σ_cyc dθ(V,W) ℒ_ξ U

Since the Levi form L_θ = dθ|_{H×H} is non-degenerate, [·,·]_q
violates the Jacobi identity for all q ≠ 1. Thus (𝔛(M), [·,·]_q)
is a Leibniz algebra, not a Lie algebra.

LaTeX label: `prop:q-jacobiator`

## References

- [leitner2026] §1-quantum-observable-universe/q-jacobiator

**Ground ring (AGENTS.md §7c)**: the formal data is stated over a bare
commutative ring `R`, with the substrate parameter carried as a **unit**
`q : Rˣ` rather than a nonzero element of a field.  The Jacobiator
coefficient's inverse is then the units inverse `↑q⁻¹`, so no field, no
`Inv` on `R`, and no division appear — the pre-Archimedean home is
`ℤ[q, q⁻¹]`, where `q` is exactly a unit.  The non-vanishing statement
additionally asks for `IsDomain R` (needed only to conclude that a
product of nonzero factors is nonzero); every field is such a ring, so
this is strictly more general than the previous `[Field R]` form.  The
canonical specialisation is `R = ℝ` with `q ↦ q₀`, post-τ.
-/

namespace QOU

/-- **q-Jacobiator data**: the geometric inputs to the failure of the
    Jacobi identity for the q-deformed bracket — the substrate
    parameter `q` (a unit of the ground ring), the three cyclic
    Levi-form values `dθ(·,·)`, and the three Lie derivatives
    `ℒ_ξ(·)`. -/
structure QJacobiator (R : Type*) [CommRing R] where
  /-- The substrate parameter q, carried as a unit of `R`. -/
  q : Rˣ
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

/-- The cyclic Levi-form sum `Σ_cyc dθ(V,W) · ℒ_ξ U` carried by the data. -/
def QJacobiator.cyclicSum {R : Type*} [CommRing R] (j : QJacobiator R) : R :=
  j.levi_form_VW * j.lie_U + j.levi_form_WU * j.lie_V + j.levi_form_UV * j.lie_W

/-- The Jacobiator value:
    `Jac_q(U,V,W) = -q⁻¹(1-q⁻¹) · Σ_cyc dθ(V,W) · ℒ_ξ U`. -/
def QJacobiator.value {R : Type*} [CommRing R] (j : QJacobiator R) : R :=
  -(↑j.q⁻¹ : R) * (1 - (↑j.q⁻¹ : R)) * j.cyclicSum

/-- The Jacobiator vanishes at q = 1 (classical Lie algebra). -/
theorem jacobiator_classical {R : Type*} [CommRing R] (j : QJacobiator R)
    (hq : j.q = 1) : j.value = 0 := by
  unfold QJacobiator.value
  rw [hq]
  simp

/-- The Jacobiator is non-zero for q ≠ 1 when the cyclic Levi-form sum is
    non-degenerate (the fields are not all Reeb-invariant).  The `q ≠ 0`
    hypothesis of the field-based statement is no longer needed: `q` is a
    unit by construction. -/
theorem jacobiator_nonzero {R : Type*} [CommRing R] [IsDomain R]
    (j : QJacobiator R) (hq : j.q ≠ 1) (h_cyclic : j.cyclicSum ≠ 0) :
    j.value ≠ 0 := by
  unfold QJacobiator.value
  refine mul_ne_zero (mul_ne_zero ?_ ?_) h_cyclic
  · exact neg_ne_zero.mpr (Units.ne_zero _)
  · rw [sub_ne_zero]
    intro h
    exact hq (inv_eq_one.mp (Units.val_eq_one.mp h.symm))

/-- The Leibniz coefficient `q⁻¹(1 - q⁻¹)` of the q-bracket vanishes
    **exactly** at the classical limit `q = 1`.

    This is the coefficient-level counterpart of `jacobiator_classical`
    and `jacobiator_nonzero` above: those locate the vanishing of the
    Jacobiator itself, this one locates the vanishing of the prefactor
    that carries it, and shows `q = 1` is the only place it can vanish. -/
theorem leibniz_coeff_eq_zero_iff {R : Type*} [CommRing R] [IsDomain R]
    (j : QJacobiator R) :
    (↑j.q⁻¹ : R) * (1 - (↑j.q⁻¹ : R)) = 0 ↔ j.q = 1 := by
  rw [mul_eq_zero]
  constructor
  · rintro (h | h)
    · exact absurd h (Units.ne_zero _)
    · rw [sub_eq_zero] at h
      exact inv_eq_one.mp (Units.val_eq_one.mp h.symm)
  · intro h
    right
    rw [h]
    simp

end QOU
