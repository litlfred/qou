/-
  Quantum volume: V_q = |U| · Vol(S³_q) where Vol(S³_q) = π² · [2]_q.

  The q-integer [2]_q = q + q⁻¹ controls the S³ fibre volume.

**Ground ring**: archimedean specialisation over `ℝ` (AGENTS.md §7c).
The substrate field `q = sp.field p : ℝ`; the combinatorial `q`-integer
content is generic to any field with the same `q`-data, but the
positivity statements below are archimedean and so live over `ℝ`.
-/
import QOU.QuantumObservableUniverse
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Positivity

namespace QOU.Information

/-- The q-integer [n]_q = (q^n - q^{-n}) / (q - q^{-1}). -/
noncomputable def qInteger (q : ℝ) (n : ℕ) : ℝ :=
  (q ^ n - q⁻¹ ^ n) / (q - q⁻¹)

/-- [2]_q = q + q⁻¹. -/
theorem qInteger_two (q : ℝ) (hq : q ≠ 0) (hq1 : q ≠ 1) (hqn1 : q ≠ -1) :
    qInteger q 2 = q + q⁻¹ := by
  unfold qInteger
  have hden : q - q⁻¹ ≠ 0 := by
    intro h
    have hqq : q = q⁻¹ := by linarith
    have hsq : q * q = 1 := by
      have hmul := congr_arg (· * q) hqq
      simp only at hmul
      rw [inv_mul_cancel₀ hq] at hmul
      linarith
    have hfac : (q - 1) * (q + 1) = 0 := by ring_nf; linarith
    rcases mul_eq_zero.mp hfac with h | h
    · exact hq1 (by linarith)
    · exact hqn1 (by linarith)
  rw [div_eq_iff hden]
  field_simp
  ring

/-- **S³ fibre volume** in the q-deformed metric.
    Vol(S³_q) = π² · [2]_q = π²(q + q⁻¹).
    Label: def:quantum-volume -/
noncomputable def s3FibreVolume {M : Type*} (sp : SubstrateParameter M)
    (p : M) : ℝ :=
  Real.pi ^ 2 * (sp.field p + (sp.field p)⁻¹)

/-- The S³ fibre volume is positive when q > 1. -/
theorem s3FibreVolume_pos {M : Type*} (sp : SubstrateParameter M)
    (p : M) (hq : sp.field p > 1) :
    0 < s3FibreVolume sp p := by
  unfold s3FibreVolume
  have hq_pos : (0 : ℝ) < sp.field p := by linarith
  have hinv_pos : (0 : ℝ) < (sp.field p)⁻¹ := inv_pos.mpr hq_pos
  have hpi : (0 : ℝ) < Real.pi ^ 2 := by positivity
  positivity

/-- At classicality (q = 1), Vol(S³_q) = 2π² = Vol(S³). -/
theorem s3FibreVolume_classical {M : Type*} (sp : SubstrateParameter M)
    (p : M) (hq : sp.field p = 1) :
    s3FibreVolume sp p = 2 * Real.pi ^ 2 := by
  unfold s3FibreVolume
  rw [hq]; simp; ring

/-- **Quantum volume** of a region with |U| brane points (homogeneous gas).
    V_q(U) = |U| · Vol(S³_q).
    Label: def:quantum-volume -/
noncomputable def quantumVolume {M : Type*} (sp : SubstrateParameter M)
    (p : M) (branePoints : ℕ) : ℝ :=
  branePoints * s3FibreVolume sp p

end QOU.Information
