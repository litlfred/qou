import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity
import QOU.AlgebraicSubstrate.PlanckStepAtomicity

/-!
# Unified Layer-I Grain, Thomae–Jackson UV Ceiling, and Atomic Clock Scaling

Generic-field (§7c) bridge backing `rem:spacetime-length-distance-layers`:
1. **Tier 1 (`[Field K]`, `q ∈ Kˣ \ {1}`):** the single dimensionless grain
   `hbarQ q = 1 - q⁻¹` generates the full-circuit tick `planckTick q = (hbarQ q)⁻¹`
   with `hbarQ q * planckTick q = 1`, internal `G_Planck = 1`, and the exact
   Thomae–Jackson geometric partial sum `∑_{j < N} (q⁻¹)^j = (1 - (q⁻¹)^N) / (1 - q⁻¹)`.
2. **Tier 2 (`[Field K] [LinearOrder K] [IsStrictOrderedRing K]`, `1 < q`):**
   every finite Thomae–Jackson proper-time partial sum is strictly bounded above
   by `planckTick q = (1 - q⁻¹)⁻¹`.
3. **Atomic-step clock scaling (`PlanckStepAtomicity` → `SubstrateClockUniqueness`):**
   on an atomic step monoid, any additive clock is an exact scalar multiple of a
   Reeb circuit clock calibrated to `planckTick q` per generator step.
-/

-- Ref: [leitner2026] information-theory, rem:spacetime-length-distance-layers
namespace QOU.InformationTheory.UnifiedClockScaleLayers

open scoped BigOperators
open QOU.AlgebraicSubstrate.SubstrateClock

section GenericField

variable {K : Type*} [Field K]

/-- Dimensionless Layer-I substrate grain `ℏ_q = 1 - q⁻¹`. -/
def hbarQ (q : K) : K := 1 - q⁻¹

/-- Full-circuit Reeb/Planck tick `t_P(q) = ℏ_q⁻¹`. -/
def planckTick (q : K) : K := (hbarQ q)⁻¹

theorem hbarQ_ne_zero {q : K} (hq1 : q ≠ 1) : hbarQ q ≠ 0 := by
  unfold hbarQ
  intro h
  have hinv : q⁻¹ = 1 := (sub_eq_zero.mp h).symm
  exact hq1 (inv_eq_one.mp hinv)

/-- Exact Layer-I circuit identity `ℏ_q · t_P(q) = 1` over any field `K` (`q ≠ 1`). -/
theorem hbarQ_mul_planckTick {q : K} (hq1 : q ≠ 1) :
    hbarQ q * planckTick q = 1 :=
  mul_inv_cancel₀ (hbarQ_ne_zero hq1)

/-- Rational form `t_P(q) = q / (q - 1)` over any field `K`. -/
theorem planckTick_eq_div {q : K} (hq0 : q ≠ 0) (hq1 : q ≠ 1) :
    planckTick q = q / (q - 1) := by
  have hqsub : q - 1 ≠ 0 := sub_ne_zero.mpr hq1
  unfold planckTick hbarQ
  field_simp [hq0, hqsub]

/-- Thomae–Jackson UV geometric partial sum `(1 - (q⁻¹)^N) / (1 - q⁻¹)` over any field. -/
theorem jackson_uv_geom_sum {q : K} (hq1 : q ≠ 1) (N : ℕ) :
    (∑ j ∈ Finset.range N, (q⁻¹) ^ j) = (1 - (q⁻¹) ^ N) / (1 - q⁻¹) := by
  have hden : 1 - q⁻¹ ≠ 0 := hbarQ_ne_zero hq1
  induction N with
  | zero => simp
  | succ n ih =>
    rw [Finset.sum_range_succ, ih, eq_div_iff hden, add_mul, div_mul_cancel₀ _ hden, pow_succ]
    ring

end GenericField

section OrderedField

variable {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]

/-- Over any ordered field with `1 < q`, the finite Thomae–Jackson UV partial sum
is strictly bounded above by the full-circuit tick `t_P(q) = (1 - q⁻¹)⁻¹`. -/
theorem jackson_uv_sum_lt_planckTick {q : K} (hq : 1 < q) (N : ℕ) :
    (∑ j ∈ Finset.range N, (q⁻¹) ^ j) < planckTick q := by
  have hq0 : (0 : K) < q := lt_trans zero_lt_one hq
  have hqinv_pos : 0 < q⁻¹ := inv_pos.mpr hq0
  have hqinv_lt : q⁻¹ < 1 := inv_lt_one_of_one_lt₀ hq
  have hden_pos : 0 < 1 - q⁻¹ := sub_pos.mpr hqinv_lt
  have hpow_pos : 0 < (q⁻¹) ^ N := pow_pos hqinv_pos N
  have hlt : 1 - (q⁻¹) ^ N < 1 := sub_lt_self 1 hpow_pos
  rw [jackson_uv_geom_sum (ne_of_gt hq) N, planckTick, hbarQ, ← one_div (1 - q⁻¹)]
  exact (div_lt_div_iff_of_pos_right hden_pos).mpr hlt

end OrderedField

section AtomicClockBridge

variable {M : Type*} [AddCommMonoid M] {K : Type*} [Field K] [CharZero K]

/-- Under `PlanckStepAtomicity`, any additive substrate clock `T` (e.g. Borel or
Thomae–Jackson proper time) scales strictly proportionally to a Reeb clock `T_reeb`
calibrated to `planckTick q` on the atomic generator `g`, with ratio `T g * hbarQ q`. -/
theorem atomic_clock_scales_with_planckTick [PlanckStepAtomicity M]
    {q : K} (hq1 : q ≠ 1)
    (T_reeb T : M → K) (hR : IsClock T_reeb) (hT : IsClock T) :
    ∃ lam : K, lam ≠ 0 ∧ ∀ a : M, T a = (lam * (hbarQ q * planckTick q)) * T_reeb a := by
  obtain ⟨lam, hlam, hprop⟩ := clocks_agree_up_to_scale (M := M) (K := K) T T_reeb hT hR
  refine ⟨lam, hlam, fun a => ?_⟩
  rw [hbarQ_mul_planckTick hq1, mul_one]
  exact hprop a

end AtomicClockBridge

end QOU.InformationTheory.UnifiedClockScaleLayers
