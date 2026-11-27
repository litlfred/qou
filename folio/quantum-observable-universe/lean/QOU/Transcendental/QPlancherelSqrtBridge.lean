import Mathlib.Analysis.SpecialFunctions.Sqrt
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import QOU.Observations.QPlancherelAsymptoticSkeleton

/-!
# QOU.Transcendental.QPlancherelSqrtBridge — the `Real.sqrt` / `Tendsto` form

Transcendental subgraph (bean `qou-e1uf`, epic `qou-dk7p`). The q-Plancherel
asymptotic skeleton is stated algebraically in
`QOU.Observations.QPlancherelAsymptoticSkeleton`: a squared majorant
`v_n² (n − 3) ≤ 1` over an Archimedean ordered field, with located-cut
convergence. This module keeps the earlier `ℝ` form, with the majorant
`v_n ≤ 1/√(n − 3)` and the conclusion `Tendsto … (𝓝 0)`, and shows it follows
from the algebraic one. No empirical value enters this file.
-/

namespace QOU.Transcendental.QPlancherelSqrtBridge

open Filter Topology QOU.Core.CutLimit QOU.Observations

/-- For `v ≥ 0` and `n ≥ 4`, the root majorant implies the squared one. -/
theorem sq_majorant_of_sqrt {v : ℝ} {n : ℕ} (hv : 0 ≤ v) (hn : 4 ≤ n)
    (h : v ≤ 1 / Real.sqrt ((n : ℝ) - 3)) : v ^ 2 * ((n : ℝ) - 3) ≤ 1 := by
  have hpos : 0 < (n : ℝ) - 3 := by
    have : (4 : ℝ) ≤ n := by exact_mod_cast hn
    linarith
  have hs : 0 < Real.sqrt ((n : ℝ) - 3) := Real.sqrt_pos.mpr hpos
  have h' : v * Real.sqrt ((n : ℝ) - 3) ≤ 1 := by
    rw [le_div_iff₀ hs] at h; exact h
  have hsq : (v * Real.sqrt ((n : ℝ) - 3)) ^ 2 ≤ 1 := by
    have h0 : 0 ≤ v * Real.sqrt ((n : ℝ) - 3) := mul_nonneg hv hs.le
    nlinarith
  rw [mul_pow, Real.sq_sqrt hpos.le] at hsq
  exact hsq

/-- The earlier `ℝ` context, with the root majorant. -/
def ofSqrtMajorant (v : ℕ → ℝ) (hv : ∀ n, 0 ≤ v n)
    (hmaj : ∀ n : ℕ, 4 ≤ n → v n ≤ 1 / Real.sqrt ((n : ℝ) - 3)) :
    QPlancherelAsymptoticSkeletonContext ℝ where
  char_variance := v
  variance_nonneg := hv
  variance_majorant_sq n hn := sq_majorant_of_sqrt (hv n) hn (hmaj n hn)

/-- The earlier statement: under the root majorant, `v n → 0` in `ℝ`. -/
theorem tendsto_zero_of_sqrtMajorant (v : ℕ → ℝ) (hv : ∀ n, 0 ≤ v n)
    (hmaj : ∀ n : ℕ, 4 ≤ n → v n ≤ 1 / Real.sqrt ((n : ℝ) - 3)) :
    Tendsto v atTop (𝓝 0) := by
  letI := ofSqrtMajorant v hv hmaj
  have hc : ConvergesTo v 0 := QPlancherelAsymptoticSkeleton (K := ℝ)
  have he := tendstoEps_of_convergesTo hc
  rw [Metric.tendsto_atTop]
  intro ε hε
  obtain ⟨N, hN⟩ := he ε hε
  exact ⟨N, fun n hn => by simpa [Real.dist_eq] using hN n hn⟩

end QOU.Transcendental.QPlancherelSqrtBridge
