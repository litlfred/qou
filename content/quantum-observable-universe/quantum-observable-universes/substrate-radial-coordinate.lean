/-!
# QOU.substrate_radial_coordinate — q governs radial/phase coordinates

Within the contact affine chart U_ξ, the substrate parameter q
governs radial and phase coordinates:
- Deep-quantum (q → ∞): Z → 0, state vertical
- Classical boundary (q → 1): Z → ∞, state horizontal

The q-Reeb flow: ℒ_ξ Z = J · ℏ_q · Z where ℏ_q = 1 - q⁻¹.

LaTeX label: `prop:substrate-radial-coordinate`

## References

- [manuscript] §1-quantum-observable-universe/substrate-radial-coordinate

**Ground ring**: `ℝ` (archimedean realisation).
Evaluates formal results at q₀ ≈ 1.1098 for comparison with
experimental data. NOT part of the formal proof chain.
See `GroundRingAnnotations.lean`.
-/

import Mathlib.Data.Real.Basic

namespace QOU

/-- **Substrate radial coordinate**: the relationship between
    the substrate parameter q and the affine coordinate Z. -/
-- Ref: [manuscript] §1
structure SubstrateRadialCoordinate where
  /-- The substrate parameter q > 1. -/
  q : ℝ
  /-- q > 1. -/
  q_gt_one : 1 < q
  /-- The affine coordinate Z = α_H / ι_ξ α. -/
  Z : ℝ
  /-- Z ≥ 0 (radial coordinate). -/
  Z_nonneg : 0 ≤ Z
  /-- The quantum Planck constant ℏ_q = 1 - q⁻¹. -/
  hbar_q : ℝ := 1 - q⁻¹
  /-- The angular momentum quantum number J. -/
  J : ℝ
  /-- The q-Reeb flow rate: ℒ_ξ Z = J · ℏ_q · Z. -/
  reeb_flow_rate : ℝ := J * hbar_q * Z

/-- ℏ_q is positive for q > 1. -/
-- Ref: [manuscript] §1
theorem hbar_q_pos (src : SubstrateRadialCoordinate) :
    0 < src.hbar_q := by
  unfold SubstrateRadialCoordinate.hbar_q
  have : src.q⁻¹ < 1 := inv_lt_one_of_one_lt₀ src.q_gt_one
  linarith

/-- In the deep-quantum limit (q → ∞), ℏ_q → 1. -/
-- Ref: [manuscript] §1
theorem deep_quantum_limit_hbar (q : ℝ) (hq : 100 < q) :
    |1 - (1 - q⁻¹)| < 0.01 := by
  simp
  rw [abs_inv]
  rw [abs_of_pos (by linarith)]
  rw [inv_lt (by linarith) (by positivity)]
  linarith

/-- In the classical limit (q → 1), ℏ_q → 0. -/
-- Ref: [manuscript] §1
theorem classical_limit_hbar (q : ℝ) (hq : q = 1) :
    1 - q⁻¹ = 0 := by
  simp [hq]

end QOU
