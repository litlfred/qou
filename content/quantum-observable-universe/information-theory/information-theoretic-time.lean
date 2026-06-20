/-
  Information-theoretic time: T = N (cumulative Reeb operation count)
  with rescaling t = ℏ_q · T to obtain the continuous Reeb flow parameter.

  **Archimedean specialisation** (AGENTS.md §7c): the monotonicity
  theorem uses `linarith` on `q : ℝ`, so the whole file specialises
  to ℝ. The structural data (q, stepCount) is `ℝ`-valued throughout.
-/
import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Linarith

namespace QOU

/-- Information-theoretic time: the cumulative count of Reeb operations
    (iterations of f_q on the exceptional divisor).

    Specialised to `ℝ` per §7c (the monotonicity theorem below uses
    archimedean ordering). -/
structure InformationTheoreticTime where
  /-- Substrate parameter q ≠ 0, 1 -/
  q : ℝ
  hq_ne_zero : q ≠ 0
  hq_ne_one : q ≠ 1
  /-- Cumulative operation count -/
  stepCount : ℕ

/-- The continuous Reeb time coordinate, obtained by rescaling the
    discrete step count by ℏ_q = 1 - q⁻¹. -/
noncomputable def informationTheoreticTime
    (τ : InformationTheoreticTime) : ℝ :=
  (1 - τ.q⁻¹) * (τ.stepCount : ℝ)

/-- Reeb time preserves ordering: more steps means later time. -/
-- Ref: [manuscript] Ch 8, Definition: Information-Theoretic Time
theorem reeb_time_monotone
    (q : ℝ) (hq0 : q ≠ 0) (hq1 : q ≠ 1) (hq_pos : 1 < q)
    (n m : ℕ) (hnm : n < m) :
    informationTheoreticTime ⟨q, hq0, hq1, n⟩ <
    informationTheoreticTime ⟨q, hq0, hq1, m⟩ := by
  -- Ref: [manuscript] Ch 8, Definition: Information-Theoretic Time
  -- Since q > 1, the coefficient (1 - q⁻¹) is positive,
  -- so (1 - q⁻¹)·n < (1 - q⁻¹)·m when n < m.
  simp only [informationTheoreticTime]
  apply mul_lt_mul_of_pos_left (Nat.cast_lt.mpr hnm)
  -- Show 0 < 1 - q⁻¹: since q > 1, we have q⁻¹ < 1
  have hq_pos' : (0 : ℝ) < q := by linarith
  have hq_inv_lt : q⁻¹ < 1 := by
    rw [inv_lt_one_iff_of_pos hq_pos']
    exact hq_pos
  linarith

end QOU
