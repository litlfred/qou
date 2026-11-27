import QOU.Nuclear.NucleonDownQuarkStrand
import Mathlib.Analysis.SpecialFunctions.Log.Basic

/-!
# The curl and through-strand Gibbs splits (archimedean)

Split off `QOU.Nuclear.NucleonDownQuarkStrand` at the transcendental boundary (bean `qou-gfsr`);
name and namespace unchanged. The γγ, strand-orientation and curl-factor results stay in that
module over a generic field; only the `Real.log` statements live here.
-/

namespace QOU.Nuclear.NucleonDownQuarkStrand

/-- Curl reading of the Gibbs split: `E·log(z_D/z̄_D) = 4E·log q`. -/
theorem curl_split (q E : ℝ) (hq : 0 < q) :
    E * Real.log (zD q / zbarD q) = 4 * E * Real.log q := by
  have hq0 : q ≠ 0 := hq.ne'
  have hq2 : q ^ 2 + 1 ≠ 0 := by positivity
  have hz : zbarD q ≠ 0 := by
    rw [zbarD_eq q hq0 hq2]; positivity
  rw [curl_ratio q hq0 hq2, mul_div_assoc, div_self hz, mul_one, Real.log_pow]
  push_cast; ring

/-- Through reading: `E·log(q/q⁻¹) = 2E·log q` (the existing `K`-weight cell). -/
theorem through_split (q E : ℝ) (hq : 0 < q) :
    E * Real.log (q / q⁻¹) = 2 * E * Real.log q := by
  have : q / q⁻¹ = q ^ 2 := by field_simp
  rw [this, Real.log_pow]; push_cast; ring

theorem curl_split_eq_twice_through (q E : ℝ) (hq : 0 < q) :
    E * Real.log (zD q / zbarD q) = 2 * (E * Real.log (q / q⁻¹)) := by
  rw [curl_split q E hq, through_split q E hq]; ring

end QOU.Nuclear.NucleonDownQuarkStrand
