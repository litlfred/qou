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
  -- Need to show (q - q⁻¹) / (q - q⁻¹) = 1, i.e. q - q⁻¹ ≠ 0
  have hden : q - q⁻¹ ≠ 0 := by
    intro h
    -- If q = q⁻¹ then q² = 1, contradiction
    have heq : q = q⁻¹ := by linarith
    have hmul : q * q⁻¹ = 1 := mul_inv_cancel₀ hq
    rw [← heq] at hmul
    -- hmul : q * q = 1
    have : q ^ 2 = 1 := by nlinarith [hmul]
    exact hqn this
  unfold qDegeneracy
  simp only [Nat.mul_zero, Nat.zero_add, pow_one]
  exact div_self hden

/-- When q > 1, we have q² ≠ 1 (needed for qDegeneracy lemmas). -/
theorem sq_ne_one_of_gt_one (q : ℝ) (hq : q > 1) : q ^ 2 ≠ 1 := by
  intro h
  nlinarith

/-- **Boltzmann factor at j = 0**: exp(-β · J²(0) · ℏ_q) = exp(0) = 1.
    Since J²(0) = 0, the exponent vanishes. -/
theorem boltzmann_ground_state (q β hbar : ℝ) :
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
    (sp : ArchimedeanSubstrateField M) (p : M) (jMax : ℕ) : ℝ :=
  let q := sp.field p
  let beta := q / (q - 1)
  let hbar := quantumPlanckConstant sp p
  Finset.sum (Finset.range (jMax + 1)) fun j =>
    qDegeneracy q j * Real.exp (-beta * qAngularMomentum q j * hbar)

/-- **Hydrogen heat capacity** at low temperature (high β):
    the partition function with only j = 0 equals 1, which is positive.
    This shows the ground state is non-degenerate and Z > 0. -/
theorem hydrogen_partition_ground_pos {M : Type*}
    (sp : ArchimedeanSubstrateField M) (p : M) (hq : sp.field p > 1) :
    rotationalPartitionFunction sp p 0 > 0 := by
  unfold rotationalPartitionFunction
  simp only [zero_add, Finset.sum_range_one]
  have hdeg : qDegeneracy (sp.field p) 0 = 1 :=
    qDegeneracy_zero (sp.field p) (by linarith) (sq_ne_one_of_gt_one (sp.field p) hq)
  rw [hdeg, one_mul]
  exact Real.exp_pos _

/-- The partition function is monotone in j_max: adding more angular
    momentum modes can only increase Z (all Boltzmann factors are positive). -/
theorem partition_monotone {M : Type*}
    (sp : ArchimedeanSubstrateField M) (p : M) (hq : sp.field p > 1)
    (j : ℕ) :
    rotationalPartitionFunction sp p j ≤
    rotationalPartitionFunction sp p (j + 1) := by
  unfold rotationalPartitionFunction
  simp only [Finset.sum_range_succ]
  have hq_pos : (0 : ℝ) < sp.field p := by linarith
  have hinv_pos : (0 : ℝ) < (sp.field p)⁻¹ := inv_pos.mpr hq_pos
  have hmul : sp.field p * (sp.field p)⁻¹ = 1 := mul_inv_cancel₀ (ne_of_gt hq_pos)
  have hinv_lt : (sp.field p)⁻¹ < sp.field p := by nlinarith [hmul, hq, hinv_pos]
  -- [2j+3]_q ≥ 0 when q > 1: numerator and denominator have same sign
  have hdeg : (0 : ℝ) ≤ qDegeneracy (sp.field p) (j + 1) := by
    unfold qDegeneracy
    apply div_nonneg
    · have hpow : (sp.field p)⁻¹ ^ (2 * (j + 1) + 1) ≤
               sp.field p ^ (2 * (j + 1) + 1) := by
        gcongr
      linarith
    · linarith
  have hexp : (0 : ℝ) ≤ Real.exp
      (-(sp.field p / (sp.field p - 1)) * qAngularMomentum (sp.field p) (j + 1)
        * quantumPlanckConstant sp p) := Real.exp_nonneg _
  have hterm : (0 : ℝ) ≤ qDegeneracy (sp.field p) (j + 1) *
      Real.exp (-(sp.field p / (sp.field p - 1)) * qAngularMomentum (sp.field p) (j + 1)
        * quantumPlanckConstant sp p) := mul_nonneg hdeg hexp
  linarith [hterm]

end QOU.Information
