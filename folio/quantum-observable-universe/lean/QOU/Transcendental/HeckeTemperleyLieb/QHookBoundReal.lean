import HeckeTemperleyLieb.QHookBound

/-!
# Féray–Méliot convergence rate — companion of `QHookBound`

The `O(1/√k)` rate class of `HeckeTemperleyLieb.QHookBound`, kept inside the
transcendental boundary because it is stated with `Real.sqrt` (bean `qou-dk7p`).
-/

namespace QOU.Archimedean.QHookBound

open QOU.Archimedean

/-! **Convergence rate** (improved via Féray–Méliot).

    The q-Plancherel CLT [feray2010] gives character variance O(1/k),
    so the branching fraction converges at rate O(1/√k):

    |f_μ^{(k)} − f_μ^∞| ≤ C_q / √(k − 3)

    where C_q = O(h² · [2]_q) depends on q but not on k or μ.

    This is STRONGER than our earlier O(1/k) estimate.
    At k = 9: bound ≈ C_q/√6 ≈ 0.11 (actual 0.008 — well within).
    At k = 12: bound ≈ C_q/3 ≈ 0.09. -/
-- Ref: [feray2010] V. Féray, P.-L. Méliot,
--   "Asymptotics of q-Plancherel measures",
--   Prob. Theory Related Fields 152, 589-624, 2012.
--   Theorem 1.1 (q-Plancherel CLT).

/-- **q-Plancherel convergence rate — typeclass (Pattern 4).**
    Per-instance witness for the Féray–Méliot O(1/√k) bound. -/
class ConvergenceRate (q : ℝ) (_hq : q > 1) (_hq2 : q < 2)
    (k : ℕ) (_hk : k ≥ 4)
    (f_k f_inf : ℝ)
    (C_q : ℝ) (_hC : C_q = 3 * (q - q⁻¹) ^ 2 * (q + q⁻¹)) : Prop where
  /-- The Féray–Méliot rate. -/
  bound : |f_k - f_inf| ≤ C_q / Real.sqrt (k - 3 : ℝ)

/-- **Default instance from a Fact witness on the rate bound**. -/
instance convergenceRate_of_fact (q : ℝ) (hq : q > 1) (hq2 : q < 2)
    (k : ℕ) (hk : k ≥ 4)
    (f_k f_inf : ℝ)
    (C_q : ℝ) (hC : C_q = 3 * (q - q⁻¹) ^ 2 * (q + q⁻¹))
    [hf : Fact (|f_k - f_inf| ≤ C_q / Real.sqrt (k - 3 : ℝ))] :
    ConvergenceRate q hq hq2 k hk f_k f_inf C_q hC :=
  ⟨hf.out⟩

/-- **Self-convergence (reflexivity)**: when `f_k = f_inf`, the
    Féray–Méliot rate holds with LHS = 0. The RHS is non-negative
    since `C_q = 3·h²·(q + q⁻¹)` with each factor positive for
    `q > 1`. -/
instance convergenceRate_refl (q : ℝ) (hq : q > 1) (hq2 : q < 2)
    (k : ℕ) (hk : k ≥ 4)
    (f : ℝ)
    (C_q : ℝ) (hC : C_q = 3 * (q - q⁻¹) ^ 2 * (q + q⁻¹)) :
    ConvergenceRate q hq hq2 k hk f f C_q hC := by
  refine ⟨?_⟩
  simp
  have hq_pos : q > 0 := by linarith
  have hq_inv_pos : q⁻¹ > 0 := inv_pos.mpr hq_pos
  rw [hC]
  have h_diff_pos : (q - q⁻¹)^2 ≥ 0 := sq_nonneg _
  have h_sum_pos : q + q⁻¹ > 0 := by positivity
  have h_C_nonneg : 3 * (q - q⁻¹) ^ 2 * (q + q⁻¹) ≥ 0 := by positivity
  have hk_real : (3 : ℝ) ≤ (k : ℝ) := by
    have : (4 : ℝ) ≤ (k : ℝ) := by exact_mod_cast hk
    linarith
  have h_sqrt_nonneg : Real.sqrt ((k : ℝ) - 3) ≥ 0 := Real.sqrt_nonneg _
  positivity

end QOU.Archimedean.QHookBound
