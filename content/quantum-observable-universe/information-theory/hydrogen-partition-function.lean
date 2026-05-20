/-
  Hydrogen partition function: monatomic H as the simplest knot gas.

  Each hydrogen atom A(1,0) has:
  - Borromean proton (amphichiral, writhe = 0)
  - Trefoil electron (Vol = 0, mass from vacuum drag)
  - Rotational modes from SU_q(2): J² = [j]_q · [j+1]_q

**Ground ring**: `ℝ` (geometric/analytic realisation).
Uses ℝ-specific analysis (trig, norms, real powers).
NOT part of the formal proof chain.
See `GroundRingAnnotations.lean`.
-/
import QOU.QuantumObservableUniverse
import QOU.MathConstants
import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Positivity
import Mathlib.Analysis.SpecialFunctions.ExpDeriv

namespace QOU.Information

/-- **q-angular momentum eigenvalue** J²_q(j) = [j]_q · [j+1]_q.
    This is the Casimir of SU_q(2) at spin j. -/
noncomputable def qAngularMomentum (q : ℝ) (j : ℕ) : ℝ :=
  let qj := (q ^ j - q⁻¹ ^ j) / (q - q⁻¹)
  let qj1 := (q ^ (j + 1) - q⁻¹ ^ (j + 1)) / (q - q⁻¹)
  qj * qj1

/-- At j = 0, the angular momentum vanishes: [0]_q · [1]_q = 0.
    This is because [0]_q = (q⁰ - q⁻⁰)/(q - q⁻¹) = 0. -/
theorem qAngularMomentum_zero (q : ℝ) : qAngularMomentum q 0 = 0 := by
  unfold qAngularMomentum
  simp

/-- **q-degeneracy**: the number of states at spin j is [2j+1]_q. -/
noncomputable def qDegeneracy (q : ℝ) (j : ℕ) : ℝ :=
  (q ^ (2 * j + 1) - q⁻¹ ^ (2 * j + 1)) / (q - q⁻¹)

/-- [1]_q = 1 for all nonzero q ≠ ±1.
    Proof: [1]_q = (q - q⁻¹)/(q - q⁻¹) = 1. -/
theorem qDegeneracy_zero (q : ℝ) (hq : q ≠ 0) (hqn : q ^ 2 ≠ 1) :
    qDegeneracy q 0 = 1 := by
  unfold qDegeneracy
  simp
  -- Need to show (q - q⁻¹) / (q - q⁻¹) = 1, i.e. q - q⁻¹ ≠ 0
  have hden : q - q⁻¹ ≠ 0 := by
    intro h
    -- If q = q⁻¹ then q² = 1, contradiction
    have heq : q = q⁻¹ := by linarith
    have : q * q = q * q⁻¹ := by rw [heq]
    rw [mul_inv_cancel₀ hq] at this
    -- q² = 1
    have : q ^ 2 = 1 := by nlinarith
    exact hqn this
  exact div_self hden

/-- When q > 1, we have q² ≠ 1 (needed for qDegeneracy lemmas). -/
theorem sq_ne_one_of_gt_one (q : ℝ) (hq : q > 1) : q ^ 2 ≠ 1 := by
  intro h
  nlinarith

/-- **Boltzmann factor at j = 0**: exp(-β · J²(0) · ℏ_q) = exp(0) = 1.
    Since J²(0) = 0, the exponent vanishes. -/
theorem boltzmann_ground_state (β hbar : ℝ) :
    Real.exp (-β * qAngularMomentum q 0 * hbar) = 1 := by
  rw [qAngularMomentum_zero]
  simp

/-- **The j = 0 contribution** to the partition function is 1
    (degeneracy [1]_q = 1 times Boltzmann factor exp(0) = 1). -/
theorem ground_state_contribution (q : ℝ) (hq : q > 1) (β hbar : ℝ) :
    qDegeneracy q 0 * Real.exp (-β * qAngularMomentum q 0 * hbar) = 1 := by
  rw [qAngularMomentum_zero]
  simp
  exact qDegeneracy_zero q (by linarith) (sq_ne_one_of_gt_one q hq)

/-- **Rotational partition function** for a single hydrogen atom.
    z_rot = Σ_{j=0}^{j_max} [2j+1]_q · exp(-β · [j]_q[j+1]_q · ℏ_q).
    Parameterised by the maximum angular momentum j_max. -/
noncomputable def rotationalPartitionFunction {M : Type*}
    (sp : SubstrateParameter M) (p : M) (jMax : ℕ) : ℝ :=
  let q := sp.field p
  let beta := q / (q - 1)
  let hbar := quantumPlanckConstant sp p
  Finset.sum (Finset.range (jMax + 1)) fun j =>
    qDegeneracy q j * Real.exp (-beta * qAngularMomentum q j * hbar)

/-- **Hydrogen heat capacity** at low temperature (high β):
    the partition function with only j = 0 equals 1, which is positive.
    This shows the ground state is non-degenerate and Z > 0. -/
theorem hydrogen_partition_ground_pos {M : Type*}
    (sp : SubstrateParameter M) (p : M) (hq : sp.field p > 1) :
    rotationalPartitionFunction sp p 0 > 0 := by
  unfold rotationalPartitionFunction
  simp [Finset.sum_range_succ, Finset.sum_range_zero]
  rw [ground_state_contribution (sp.field p) hq]
  norm_num

/-- The partition function is monotone in j_max: adding more angular
    momentum modes can only increase Z (all Boltzmann factors are positive). -/
theorem partition_monotone {M : Type*}
    (sp : SubstrateParameter M) (p : M) (hq : sp.field p > 1)
    (j : ℕ) :
    rotationalPartitionFunction sp p j ≤
    rotationalPartitionFunction sp p (j + 1) := by
  unfold rotationalPartitionFunction
  simp only [Finset.sum_range_succ]
  linarith [mul_nonneg
    (by -- [2j+3]_q ≥ 0 when q > 1: numerator and denominator have same sign
      unfold qDegeneracy
      apply div_nonneg
      · have hq_pos : (0 : ℝ) < sp.field p := by linarith
        have hinv_pos : (0 : ℝ) < (sp.field p)⁻¹ := inv_pos.mpr hq_pos
        have hinv_lt : (sp.field p)⁻¹ < sp.field p := by
          rw [inv_lt_comm₀ hq_pos hq_pos]; exact hq
        have : (sp.field p)⁻¹ ^ (2 * (j + 1) + 1) ≤
               sp.field p ^ (2 * (j + 1) + 1) := by
          apply pow_le_pow_left (le_of_lt hinv_pos) (le_of_lt hinv_lt)
        linarith
      · have hq_pos : (0 : ℝ) < sp.field p := by linarith
        have hinv_lt : (sp.field p)⁻¹ < sp.field p := by
          rw [inv_lt_comm₀ hq_pos hq_pos]; exact hq
        linarith :
      ℝ)
    (Real.exp_nonneg _)]

end QOU.Information
