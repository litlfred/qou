import QOU.Archimedean.BlochWignerFiveTermInstance
import QOU.Archimedean.ThreeSubstantiveMathlibFillers
import QOU.Archimedean.ClausenDoubleAngleSeries
import QOU.MathlibExt.ComplexDilogarithmBoundary

/-!
# The Cl₂ pentagon, from the Bloch–Wigner five-term relation

Two facts:

* `cLiTwo_exp_im`: `Im Li₂(e^{iθ}) = Cl₂(θ)` for every real `θ`, using the
  library series `QOU.MathlibExt.cLiTwo`;
* `blochD_exp`: the Bloch–Wigner function on the unit circle is the Clausen
  function, `D(e^{iθ}) = Cl₂(θ)`.

Together with the proved five-term relation (`FiveTermProof.fiveSum_eq_zero`),
these give a genuine instance of `SubstantiveFillers.Cl_2_PentagonHolds`
(bean `qou-eao2`). That class had a free `closure` predicate as a field until
2026-11-20, so it could be inhabited vacuously.

-- Ref: [zagier1986] DOI 10.1007/BFb0084581
-- Ref: [bloch2000]
-/

namespace QOU.Archimedean.Cl2PentagonFromBlochWigner

open Complex QOU.MathlibExt QOU.Archimedean QOU.Archimedean.FiveTermProof

/-- **`Im Li₂(e^{iθ}) = Cl₂(θ)`** for every real `θ` (series argument). -/
theorem cLiTwo_exp_im (θ : ℝ) : (cLiTwo (exp (θ * I))).im = Cl_2 θ := by
  have hcast : ∀ k : ℕ, ((k : ℂ) + 1) ^ 2 = (((((k : ℝ) + 1) ^ 2 : ℝ)) : ℂ) := by
    intro k; push_cast; ring
  have hs : Summable (fun k : ℕ => exp (θ * I) ^ (k + 1) / ((k : ℂ) + 1) ^ 2) := by
    refine Summable.of_norm_bounded
      (ClausenDoubleAngleSeries.summable_bounded_div_sq (fun _ => 1) (fun _ => by simp))
      (fun k => ?_)
    rw [hcast, norm_div, norm_pow, norm_exp_ofReal_mul_I, one_pow,
      Complex.norm_real, Real.norm_eq_abs, abs_of_pos (by positivity)]
  unfold cLiTwo
  rw [Complex.im_tsum hs]
  unfold Cl_2
  refine tsum_congr (fun k => ?_)
  rw [hcast, Complex.div_ofReal_im, ← Complex.exp_nat_mul,
    show ((k + 1 : ℕ) : ℂ) * (θ * I) = (((((k : ℝ) + 1) * θ : ℝ)) : ℂ) * I by
      push_cast; ring,
    exp_ofReal_mul_I_im]

/-- `Cl₂` vanishes at every multiple of `2π`. -/
theorem Cl_2_two_pi_mul (n : ℤ) : Cl_2 (2 * Real.pi * n) = 0 := by
  unfold Cl_2
  have h : ∀ k : ℕ, Real.sin (((k : ℝ) + 1) * (2 * Real.pi * n)) / ((k : ℝ) + 1) ^ 2 = 0 := by
    intro k
    have hc : ((k : ℝ) + 1) * (2 * Real.pi * n) = (((2 * (k + 1) * n : ℤ)) : ℝ) * Real.pi := by
      push_cast; ring
    rw [hc, Real.sin_int_mul_pi, zero_div]
  simp only [h, tsum_zero]

/-- **The Bloch–Wigner function on the unit circle is the Clausen function**:
    `D(e^{iθ}) = Cl₂(θ)` for every real `θ`. -/
theorem blochD_exp (θ : ℝ) : blochD (exp (θ * I)) = Cl_2 θ := by
  by_cases h1 : exp (θ * I) = 1
  · obtain ⟨n, hn⟩ := Complex.exp_eq_one_iff.mp h1
    have hθ : θ = 2 * Real.pi * n := by
      have := congrArg Complex.im hn
      simp at this
      linarith
    rw [h1, show (1 : ℂ) = ((1 : ℝ) : ℂ) by simp, blochD_ofReal, hθ, Cl_2_two_pi_mul]
  · have hnorm : ‖exp (θ * I)‖ = 1 := norm_exp_ofReal_mul_I θ
    have hnotcut : exp (θ * I) ∈ notCut := by
      by_contra hc
      simp only [notCut, Set.mem_setOf_eq, not_or, not_not, not_lt] at hc
      apply h1
      apply Complex.ext
      · have hre : (exp (θ * I)).re ≤ 1 := by
          have := Complex.re_le_norm (exp (θ * I)); linarith
        rw [Complex.one_re]; linarith [hc.2]
      · rw [Complex.one_im]; exact hc.1
    have hcut : ¬ ((exp (θ * I)).im = 0 ∧ 1 < (exp (θ * I)).re) := by
      rintro ⟨-, hre⟩
      have := Complex.re_le_norm (exp (θ * I)); linarith
    unfold blochD
    rw [if_neg hcut]
    unfold DNZ
    rw [hnorm, Real.log_one, zero_mul, add_zero,
      cLiTwoExt_eq_cLiTwo_of_norm_le_one hnorm.le hnotcut, cLiTwo_exp_im]

/-- **The genuine instance** of `Cl_2_PentagonHolds`: the five-term relation of
    the Bloch–Wigner function, read on the unit circle. -/
instance instCl_2_PentagonHolds : SubstantiveFillers.Cl_2_PentagonHolds where
  pentagon_holds_general c hc _ := by
    obtain ⟨x, y, hx0, hx1, hy0, hy1, hxy, e0, e1, e2, e3, e4⟩ := hc
    have h := fiveSum_eq_zero hx0 hx1 hy0 hy1 hxy
    unfold fiveSum at h
    rw [← blochD_exp, ← blochD_exp, ← blochD_exp, ← blochD_exp, ← blochD_exp,
      e0, e1, e2, e3, e4]
    exact h

end QOU.Archimedean.Cl2PentagonFromBlochWigner
