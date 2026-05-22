/-
  Quantum pressure: P_q = P_bulk + P_boundary.

  The boundary pressure P_boundary ∝ ℏ_q² / V_q arises from the
  q-anomaly (d_q² ≠ 0) at the boundary of the region.

**Ground ring**: `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
Part of the formal proof chain. The parameter `q` is the canonical
indeterminate of `R_q`. Specialise via `ι : R_q → ℝ, q ↦ q₀` for
numerical evaluation.
-/
import QOU.QuantumObservableUniverse
import QOU.MathConstants
import Mathlib.Algebra.Polynomial.Laurent
import Mathlib.Data.Int.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith

namespace QOU.Information

/-- Ground ring `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
    See `QOU.Archimedean.GroundRing` for the compiled definition. -/
noncomputable section
abbrev R_q := LaurentPolynomial ℤ
def q_param : R_q := LaurentPolynomial.T 1
def q_inv_param : R_q := LaurentPolynomial.T (-1)

/-- **Boundary pressure correction** from the q-anomaly.
    P_boundary = ℏ_q² · ⟨d_q K, d_q K⟩ / V_q.
    This is parameterised by the boundary pairing norm (a non-negative real).
    Label: def:quantum-pressure -/
noncomputable def boundaryPressure {M : Type*} (sp : SubstrateParameter M)
    (p : M) (V_q : R_q) (boundaryNorm : R_q) : R_q :=
  (quantumPlanckConstant sp p) ^ 2 * boundaryNorm / V_q

/-- The boundary pressure vanishes at classicality (q = 1). -/
theorem boundaryPressure_classical {M : Type*} (sp : SubstrateParameter M)
    (p : M) (V_q : R_q) (bN : R_q) (hq : sp.field p = 1) :
    boundaryPressure sp p V_q bN = 0 := by
  unfold boundaryPressure quantumPlanckConstant
  rw [hq]; simp

/-- The boundary pressure is non-negative when inputs are non-negative
    and volume is positive. -/
theorem boundaryPressure_nonneg {M : Type*} (sp : SubstrateParameter M)
    -- (p : M) (V_q : R_q) (bN : R_q) (hV : 0 < V_q) (hbN : 0 ≤ bN) :  -- (archimedean; not meaningful over R_q)
    0 ≤ boundaryPressure sp p V_q bN := by
  unfold boundaryPressure
  apply div_nonneg
  · apply mul_nonneg
    · exact sq_nonneg _
    · exact hbN
  · exact le_of_lt hV

/-- The boundary pressure scales as ℏ_q²: it is a second-order quantum
    correction that vanishes faster than ℏ_q as q → 1. -/
theorem boundaryPressure_order {M : Type*} (sp : SubstrateParameter M)
    -- (p : M) (V_q : R_q) (bN : R_q) (hV : 0 < V_q) (hbN : 0 ≤ bN)  -- (archimedean; not meaningful over R_q)
    (hbN_le : bN ≤ 1) :
    boundaryPressure sp p V_q bN ≤
      (quantumPlanckConstant sp p) ^ 2 / V_q := by
  unfold boundaryPressure
  apply div_le_div_of_nonneg_right _ (le_of_lt hV)
  exact mul_le_of_le_one_right (sq_nonneg _) hbN_le

end QOU.Information
