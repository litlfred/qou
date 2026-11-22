import Mathlib.Analysis.Complex.Basic
import Mathlib.Analysis.SpecialFunctions.Sqrt
import Mathlib.Analysis.SpecificLimits.Basic

namespace QOU.Archimedean.BlochRigidity

set_option maxHeartbeats 2000000 in
/-- **Growth lemma (pure inequalities).** A dilation relation
`Ω(y) = Ω(10y) - Ω(9y/(1-y))/(1-y) + y R(y)` near `0`, with `R` bounded and `Ω` bounded on one
annulus, forces `|Ω(y)| ≤ C/√|y|`. Both other arguments sit at a larger radius, and the weights
`1/√10 + 1/(√8·0.99) < 1` make the induction over shells close. -/
theorem growth_sqrt {Ω R : ℂ → ℂ} {r B K : ℝ} (hr : 0 < r) (hr1 : r ≤ 1 / 100)
    (hK : 0 ≤ K)
    (hrel : ∀ y : ℂ, y ≠ 0 → ‖y‖ ≤ r →
      Ω y = Ω (10 * y) - Ω (9 * y / (1 - y)) / (1 - y) + y * R y)
    (hR : ∀ y : ℂ, y ≠ 0 → ‖y‖ ≤ r → ‖R y‖ ≤ K)
    (hB : ∀ w : ℂ, r ≤ ‖w‖ → ‖w‖ ≤ 11 * r → ‖Ω w‖ ≤ B) :
    ∃ C : ℝ, ∀ y : ℂ, y ≠ 0 → ‖y‖ ≤ r → ‖Ω y‖ * Real.sqrt ‖y‖ ≤ C := by
  set C : ℝ := max (B * Real.sqrt (11 * r)) K with hC
  have hCK : K ≤ C := le_max_right _ _
  have hCB : B * Real.sqrt (11 * r) ≤ C := le_max_left _ _
  have hC0 : 0 ≤ C := le_trans hK hCK
  -- shells
  have P : ∀ n : ℕ, ∀ w : ℂ, r * (1 / 8) ^ n ≤ ‖w‖ → ‖w‖ ≤ 11 * r →
      ‖Ω w‖ * Real.sqrt ‖w‖ ≤ C := by
    intro n
    induction n with
    | zero =>
      intro w h1 h2
      simp only [pow_zero, mul_one] at h1
      calc ‖Ω w‖ * Real.sqrt ‖w‖ ≤ B * Real.sqrt (11 * r) :=
            mul_le_mul (hB w h1 h2) (Real.sqrt_le_sqrt h2) (Real.sqrt_nonneg _)
              (le_trans (norm_nonneg _) (hB w h1 h2))
        _ ≤ C := hCB
    | succ n ih =>
      intro w h1 h2
      by_cases hw : r * (1 / 8) ^ n ≤ ‖w‖
      · exact ih w hw h2
      push_neg at hw
      have hpow : (1 / 8 : ℝ) ^ n ≤ 1 := pow_le_one₀ (by norm_num) (by norm_num)
      have hwr : ‖w‖ ≤ r := le_trans hw.le (by nlinarith)
      have hwpos : 0 < ‖w‖ := lt_of_lt_of_le (by positivity) h1
      have hw0 : w ≠ 0 := norm_pos_iff.1 hwpos
      have hsucc : r * (1 / 8) ^ (n + 1) = r * (1 / 8) ^ n / 8 := by ring
      rw [hsucc] at h1
      -- the factor `1 - w`
      have hn1 : ‖1 - w‖ ≤ 1 + ‖w‖ := by
        calc ‖1 - w‖ ≤ ‖(1 : ℂ)‖ + ‖w‖ := norm_sub_le _ _
          _ = 1 + ‖w‖ := by simp
      have hn2 : 1 - ‖w‖ ≤ ‖1 - w‖ := by
        have := norm_sub_norm_le (1 : ℂ) w
        simpa using this
      have hlow : (99 / 100 : ℝ) ≤ ‖1 - w‖ := by linarith
      have h1w : 1 - w ≠ 0 := by
        intro h; rw [h, norm_zero] at hlow; norm_num at hlow
      -- first argument `10 w`
      set a := 10 * w with ha
      have hna : ‖a‖ = 10 * ‖w‖ := by rw [ha, norm_mul]; norm_num
      have IA := ih a (by rw [hna]; linarith) (by rw [hna]; linarith)
      -- second argument `9 w / (1 - w)`
      set b := 9 * w / (1 - w) with hb
      have hnb : ‖b‖ = 9 * ‖w‖ / ‖1 - w‖ := by rw [hb, norm_div, norm_mul]; norm_num
      have hb1 : 8 * ‖w‖ ≤ ‖b‖ := by
        rw [hnb, le_div_iff₀ (by linarith)]; nlinarith
      have hb2 : ‖b‖ ≤ 11 * r := by
        rw [hnb, div_le_iff₀ (by linarith)]; nlinarith
      have IB := ih b (by linarith) hb2
      -- square-root comparisons
      have sw := Real.sqrt_nonneg ‖w‖
      have sa : 3 * Real.sqrt ‖w‖ ≤ Real.sqrt ‖a‖ := by
        rw [hna, Real.sqrt_mul (by norm_num)]
        have : (3 : ℝ) ≤ Real.sqrt 10 := by
          rw [Real.le_sqrt (by norm_num) (by norm_num)]; norm_num
        nlinarith
      have sb : (14 / 5) * Real.sqrt ‖w‖ ≤ Real.sqrt ‖b‖ := by
        have : Real.sqrt (8 * ‖w‖) ≤ Real.sqrt ‖b‖ := Real.sqrt_le_sqrt hb1
        rw [Real.sqrt_mul (by norm_num)] at this
        have h8 : (14 / 5 : ℝ) ≤ Real.sqrt 8 := by
          rw [Real.le_sqrt (by norm_num) (by norm_num)]; norm_num
        nlinarith
      have hA : ‖Ω a‖ * Real.sqrt ‖w‖ ≤ C / 3 := by
        rw [le_div_iff₀ (by norm_num)]
        nlinarith [norm_nonneg (Ω a)]
      have hBb : ‖Ω b‖ * Real.sqrt ‖w‖ ≤ C * (5 / 14) := by
        nlinarith [norm_nonneg (Ω b)]
      -- the relation
      have hrel' := hrel w hw0 hwr
      have hRw := hR w hw0 hwr
      have tri : ‖Ω w‖ ≤ ‖Ω a‖ + ‖Ω b‖ / ‖1 - w‖ + ‖w‖ * K := by
        rw [hrel']
        calc ‖Ω a - Ω b / (1 - w) + w * R w‖
            ≤ ‖Ω a‖ + ‖Ω b / (1 - w)‖ + ‖w * R w‖ := by
              refine le_trans (norm_add_le _ _) ?_
              gcongr
              exact norm_sub_le _ _
          _ ≤ ‖Ω a‖ + ‖Ω b‖ / ‖1 - w‖ + ‖w‖ * K := by
              rw [norm_div, norm_mul]
              gcongr
      have hdiv : ‖Ω b‖ / ‖1 - w‖ ≤ ‖Ω b‖ * (100 / 99) := by
        rw [div_le_iff₀ (by linarith)]
        have h1 : 1 ≤ (100 / 99) * ‖1 - w‖ := by linarith
        calc ‖Ω b‖ = ‖Ω b‖ * 1 := by ring
          _ ≤ ‖Ω b‖ * ((100 / 99) * ‖1 - w‖) := mul_le_mul_of_nonneg_left h1 (norm_nonneg _)
          _ = ‖Ω b‖ * (100 / 99) * ‖1 - w‖ := by ring
      -- `‖w‖ · K · √‖w‖ ≤ K / 100`
      have hsq : Real.sqrt ‖w‖ ≤ 1 := by
        rw [Real.sqrt_le_one]; linarith
      have hKt : ‖w‖ * K * Real.sqrt ‖w‖ ≤ C / 100 := by
        have : ‖w‖ * K * Real.sqrt ‖w‖ ≤ (1 / 100) * K * 1 := by
          apply mul_le_mul (mul_le_mul_of_nonneg_right (by linarith) hK) hsq sw (by positivity)
        linarith
      calc ‖Ω w‖ * Real.sqrt ‖w‖
          ≤ (‖Ω a‖ + ‖Ω b‖ * (100 / 99) + ‖w‖ * K) * Real.sqrt ‖w‖ :=
            mul_le_mul_of_nonneg_right (by linarith) sw
        _ = ‖Ω a‖ * Real.sqrt ‖w‖ + (‖Ω b‖ * Real.sqrt ‖w‖) * (100 / 99)
              + ‖w‖ * K * Real.sqrt ‖w‖ := by ring
        _ ≤ C / 3 + C * (5 / 14) * (100 / 99) + C / 100 := by gcongr
        _ ≤ C := by linarith
  refine ⟨C, fun y hy0 hyr => ?_⟩
  have hypos : 0 < ‖y‖ / r := div_pos (norm_pos_iff.2 hy0) hr
  obtain ⟨n, hn⟩ := exists_pow_lt_of_lt_one hypos (by norm_num : (1 / 8 : ℝ) < 1)
  refine P n y ?_ (by linarith)
  rw [lt_div_iff₀ hr] at hn
  linarith

end QOU.Archimedean.BlochRigidity
