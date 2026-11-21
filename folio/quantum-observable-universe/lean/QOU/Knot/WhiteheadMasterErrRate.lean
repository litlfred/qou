import QOU.Knot.WhiteheadTailDecay

/-!
# The `masterErr` rate: `N · masterErr N ≤ 30 (1 + log N)`

Small-argument Clausen bound `0 ≤ clausen θ ≤ θ(1 + log π) − θ log θ` on `[0, π]`
(monotonicity, with derivative `log(2π sin(θ/2)/θ) ≥ log 2` by Jordan), and the
logarithmic rate of the master Riemann-sum error used by the Whitehead tail bound.
-/

namespace QOU.Knot.WhiteheadInner

open Real QOU.Knot.FigureEightVolume

/-- `F θ = θ(1 + log π) − θ log θ − clausen θ`. -/
noncomputable def clausenGap (θ : ℝ) : ℝ := θ * (1 + Real.log π) - θ * Real.log θ - clausen θ

theorem continuous_clausenGap : Continuous clausenGap := by
  unfold clausenGap
  exact ((continuous_id.mul continuous_const).sub Real.continuous_mul_log).sub
    QOU.Knot.continuous_clausen

theorem hasDerivAt_clausenGap {θ : ℝ} (h0 : 0 < θ) (h2 : θ < 2 * π) :
    HasDerivAt clausenGap
      ((1 + Real.log π) - (Real.log θ + 1) + Real.log (2 * Real.sin (θ / 2))) θ := by
  have h1 : HasDerivAt (fun x : ℝ => x * (1 + Real.log π)) (1 + Real.log π) θ := by
    simpa using (hasDerivAt_id θ).mul_const (1 + Real.log π)
  have h3 : HasDerivAt (fun x : ℝ => x * Real.log x) (Real.log θ + 1) θ := by
    have := (hasDerivAt_id θ).mul (Real.hasDerivAt_log h0.ne')
    simp only [id, one_mul] at this
    convert this using 1; field_simp
  have h4 := QOU.Knot.hasDerivAt_clausen h0 h2
  have := (h1.sub h3).sub h4
  unfold clausenGap
  convert this using 1; ring

theorem clausenGap_deriv_nonneg {θ : ℝ} (h0 : 0 < θ) (h2 : θ ≤ π) :
    0 ≤ (1 + Real.log π) - (Real.log θ + 1) + Real.log (2 * Real.sin (θ / 2)) := by
  have hpi := Real.pi_pos
  have hj := jordan (t := θ / 2) (by linarith) (by linarith)
  have hs : 0 < Real.sin (θ / 2) := lt_of_lt_of_le (by positivity) hj
  have hle : θ / π ≤ Real.sin (θ / 2) := by
    calc θ / π = 2 / π * (θ / 2) := by ring
      _ ≤ _ := hj
  -- log π − log θ + log(2 sin) = log(2π sin/θ) ≥ log 2 ≥ 0
  have hratio : 1 ≤ π * (2 * Real.sin (θ / 2)) / θ := by
    rw [le_div_iff₀ h0]
    have := mul_le_mul_of_nonneg_left hle hpi.le
    rw [mul_div_cancel₀ _ hpi.ne'] at this
    nlinarith
  have hl := Real.log_nonneg hratio
  rw [Real.log_div (by positivity) h0.ne', Real.log_mul hpi.ne' (by positivity)] at hl
  linarith

theorem clausen_le_small {θ : ℝ} (h0 : 0 ≤ θ) (h2 : θ ≤ π) :
    clausen θ ≤ θ * (1 + Real.log π) - θ * Real.log θ := by
  have hpi := Real.pi_pos
  have hmono : MonotoneOn clausenGap (Set.Icc 0 π) := by
    apply monotoneOn_of_deriv_nonneg (convex_Icc 0 π) continuous_clausenGap.continuousOn
    · intro x hx
      rw [interior_Icc] at hx
      exact (hasDerivAt_clausenGap hx.1 (by linarith [hx.2])).differentiableAt.differentiableWithinAt
    · intro x hx
      rw [interior_Icc] at hx
      rw [(hasDerivAt_clausenGap hx.1 (by linarith [hx.2])).deriv]
      exact clausenGap_deriv_nonneg hx.1 hx.2.le
  have := hmono ⟨le_refl 0, hpi.le⟩ ⟨h0, h2⟩ h0
  unfold clausenGap at this
  simp only [zero_mul, sub_zero, QOU.Knot.clausen_zero] at this
  linarith

theorem abs_log_two_sin_le {N : ℕ} (hN : 4 ≤ N) :
    |Real.log (2 * Real.sin (π / N))| ≤ Real.log N := by
  have hpi := Real.pi_pos
  have hNpos : (0 : ℝ) < N := by exact_mod_cast (by omega : 0 < N)
  have hN4 : (4 : ℝ) ≤ N := by exact_mod_cast hN
  have hle : π / N ≤ π / 2 := div_le_div_of_nonneg_left hpi.le (by norm_num) (by linarith)
  have hj := jordan (t := π / N) (by positivity) hle
  have hj' : 2 / π * (π / N) = 2 / N := by field_simp
  rw [hj'] at hj
  have hs1 := Real.sin_le_one (π / N)
  have hpos : 0 < 2 * Real.sin (π / N) := by
    have : 0 < (2 : ℝ) / N := by positivity
    linarith
  have hlog2 : Real.log 2 ≤ Real.log N := Real.log_le_log (by norm_num) (by linarith)
  have hup : Real.log (2 * Real.sin (π / N)) ≤ Real.log N :=
    le_trans (Real.log_le_log hpos (by linarith)) hlog2
  have hlo : -Real.log N ≤ Real.log (2 * Real.sin (π / N)) := by
    have h4 : (4 : ℝ) / N ≤ 2 * Real.sin (π / N) := by
      have : (4 : ℝ) / N = 2 * (2 / N) := by ring
      linarith
    have := Real.log_le_log (by positivity) h4
    rw [Real.log_div (by norm_num) hNpos.ne'] at this
    have : 0 ≤ Real.log 4 := Real.log_nonneg (by norm_num)
    linarith
  rw [abs_le]; exact ⟨hlo, hup⟩

/-- **Logarithmic rate of the master error.** `N · masterErr N ≤ 60 (1 + log N)` for `N ≥ 4`. -/
theorem nat_mul_masterErr_le {N : ℕ} (hN : 4 ≤ N) :
    (N : ℝ) * masterErr N ≤ 60 * (1 + Real.log N) := by
  have hpi := Real.pi_pos
  have hpi3 := Real.pi_lt_d2
  have hNpos : (0 : ℝ) < N := by exact_mod_cast (by omega : 0 < N)
  have hN4 : (4 : ℝ) ≤ N := by exact_mod_cast hN
  have hL := abs_log_two_sin_le hN
  have hlogN : 0 ≤ Real.log N := Real.log_nonneg (by linarith)
  have hlog2 : Real.log 2 ≤ Real.log N := Real.log_le_log (by norm_num) (by linarith)
  set θ : ℝ := 2 * (π / N) with hθ
  have hθ0 : 0 < θ := by positivity
  have hθπ : θ ≤ π := by
    rw [hθ, mul_div_assoc', div_le_iff₀ hNpos]; nlinarith
  have hcl0 : 0 ≤ clausen θ := QOU.Knot.WhiteheadSaddle.clausen_nonneg hθ0.le hθπ
  have hcl := clausen_le_small hθ0.le hθπ
  have hlogθ : Real.log θ = Real.log 2 + Real.log π - Real.log N := by
    rw [hθ, Real.log_mul (by norm_num) (by positivity), Real.log_div hpi.ne' hNpos.ne']; ring
  rw [hlogθ] at hcl
  have hlog2p : 0 ≤ Real.log 2 := Real.log_nonneg (by norm_num)
  have hcl' : clausen θ ≤ θ * (1 + Real.log N) := by nlinarith
  have hNθ : (N : ℝ) * θ = 2 * π := by rw [hθ]; field_simp
  have hNh : (N : ℝ) * (π / N) = π := by field_simp
  unfold masterErr
  rw [← hθ, neg_div, abs_neg, abs_div, abs_of_nonneg hcl0, abs_two]
  have e1 : (N : ℝ) * (clausen θ / 2) ≤ π * (1 + Real.log N) := by
    have := mul_le_mul_of_nonneg_left hcl' hNpos.le
    rw [← mul_assoc, hNθ] at this
    linarith
  have e2 : (N : ℝ) * ((π / N) * |Real.log (2 * Real.sin (π / N))|) ≤ π * Real.log N := by
    rw [← mul_assoc, hNh]; exact mul_le_mul_of_nonneg_left hL hpi.le
  have e3 : (N : ℝ) * (7 * ((π / N) * (|Real.log (2 * Real.sin (π / N))| + Real.log 2)))
      ≤ 7 * π * (2 * Real.log N) := by
    rw [show (N : ℝ) * (7 * ((π / N) * (|Real.log (2 * Real.sin (π / N))| + Real.log 2)))
        = 7 * ((N : ℝ) * (π / N)) * (|Real.log (2 * Real.sin (π / N))| + Real.log 2) by ring, hNh]
    exact mul_le_mul_of_nonneg_left (by linarith) (by positivity)
  rw [mul_add, mul_add]
  nlinarith

end QOU.Knot.WhiteheadInner
