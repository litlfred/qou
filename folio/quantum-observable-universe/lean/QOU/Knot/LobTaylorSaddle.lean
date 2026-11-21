/-
  Λ AT THE SADDLE, TO SECOND ORDER — the Hessian, with an explicit remainder.
  Bean `qou-fybg`, step 2.

  WHAT THIS PROVES.  With `θ* = 5π/6` (the solution of `2 sin θ = 1` in
  `(π/2, π)`, which `KashaevArgmax` shows is where the Kashaev terms peak),

      | Λ(θ) − ( Λ(θ*) + (√3/2)·(θ − θ*)² ) |  ≤  M·|θ − θ*|³/6

  whenever `1/sin²` is bounded by `M` between the two points.  The linear term
  is ABSENT — not dropped, but zero: `Λ′(θ*) = −log(2 sin θ*) = −log 1 = 0` is
  exactly the saddle condition.  The quadratic coefficient is
  `Λ″(θ*)/2 = −cot(θ*)/2 = √3/2`, so the Hessian of the Kashaev exponent
  `−(2N/π)Λ` at the saddle is `−(2N/π)·√3` — the `|cot θ*|` that
  `c_σ = 2 sin θ* · |cot θ*|^{−1/2}` and `|τ_DG| = |cot θ*|/2` are built from.

  WHY IT IS SEPARATE FROM THE `s_k` EXPANSION.  `kashaev_log_sum_asymptotic`
  approximates a SUM by an integral; this expands the resulting SMOOTH function
  about its maximum.  They are independent steps with independent error terms,
  and combining them is what step 3 (the Gaussian sum) needs.

  THE DERIVATIVE CHAIN, all already in this corpus:

      Λ′  = −log(2 sin)        hasDerivAt_Lob            (Archimedean/…)
      Λ″  = −cot               hasDerivAt_log_two_sin    (MathlibExt/Trapezoid…)
      Λ‴  = 1/sin²             hasDerivAt_cos_div_sin    (same)

  and the Taylor step itself is `QOU.MathlibExt.abs_taylor_two_le`.

  -- Ref: [leitner2026] QOU/MathlibExt/TaylorRemainder.lean
  -- Ref: [leitner2026] QOU/Knot/KashaevArgmax.lean
  -- Ref: [leitner2026] QOU/OneLoopPrefactorInvariance.lean
-/
import QOU.Archimedean.LobachevskyDerivative
import QOU.MathlibExt.TaylorRemainder
import QOU.MathlibExt.TrapezoidRule

namespace QOU.Knot.FigureEightVolume

open Real QOU.Archimedean

/-! ## Part 1 — the derivative chain for `Λ` -/

/-- `Λ″(t) = −cot t` on `(0, π)`. -/
theorem hasDerivAt_Lob_deriv {t : ℝ} (h0 : 0 < t) (hπ : t < π) :
    HasDerivAt (fun s => -Real.log (2 * Real.sin s))
      (-(Real.cos t / Real.sin t)) t :=
  (QOU.MathlibExt.hasDerivAt_log_two_sin
    (ne_of_gt (Real.sin_pos_of_pos_of_lt_pi h0 hπ))).neg

/-- `Λ‴(t) = 1/sin²t` on `(0, π)`. -/
theorem hasDerivAt_Lob_deriv2 {t : ℝ} (h0 : 0 < t) (hπ : t < π) :
    HasDerivAt (fun s => -(Real.cos s / Real.sin s)) (1 / Real.sin t ^ 2) t := by
  have h := (QOU.MathlibExt.hasDerivAt_cos_div_sin
    (ne_of_gt (Real.sin_pos_of_pos_of_lt_pi h0 hπ))).neg
  convert h using 1
  ring

/-! ## Part 2 — Taylor to second order about any interior point -/

/-- **`Λ` to second order**, with the `O(|θ − θ₀|³)` remainder explicit. -/
theorem abs_Lob_taylor_two {θ θ₀ M : ℝ}
    (hmem : ∀ x ∈ Set.uIcc θ₀ θ, 0 < x ∧ x < π)
    (hM : ∀ x ∈ Set.uIcc θ₀ θ, 1 / Real.sin x ^ 2 ≤ M) :
    |Lob θ - (Lob θ₀ - Real.log (2 * Real.sin θ₀) * (θ - θ₀)
              - (Real.cos θ₀ / Real.sin θ₀) * ((θ - θ₀) ^ 2 / 2))|
      ≤ M * |θ - θ₀| ^ 3 / 6 := by
  have hc : ContinuousOn (fun s => 1 / Real.sin s ^ 2) (Set.uIcc θ₀ θ) := by
    intro x hx
    obtain ⟨h0, hpi⟩ := hmem x hx
    have hs : Real.sin x ≠ 0 := ne_of_gt (Real.sin_pos_of_pos_of_lt_pi h0 hpi)
    exact (continuousAt_const.div (Real.continuous_sin.continuousAt.pow 2)
      (pow_ne_zero 2 hs)).continuousWithinAt
  have habs : ∀ x ∈ Set.uIcc θ₀ θ, |1 / Real.sin x ^ 2| ≤ M := by
    intro x hx
    obtain ⟨h0, hpi⟩ := hmem x hx
    have hs : 0 < Real.sin x := Real.sin_pos_of_pos_of_lt_pi h0 hpi
    rw [abs_of_pos (by positivity)]
    exact hM x hx
  have h := QOU.MathlibExt.abs_taylor_two_le
    (f := Lob) (f₁ := fun s => -Real.log (2 * Real.sin s))
    (f₂ := fun s => -(Real.cos s / Real.sin s))
    (f₃ := fun s => 1 / Real.sin s ^ 2) (a := θ₀) (b := θ)
    (fun x hx => by obtain ⟨h0, hpi⟩ := hmem x hx; exact hasDerivAt_Lob h0 hpi)
    (fun x hx => by obtain ⟨h0, hpi⟩ := hmem x hx; exact hasDerivAt_Lob_deriv h0 hpi)
    (fun x hx => by obtain ⟨h0, hpi⟩ := hmem x hx; exact hasDerivAt_Lob_deriv2 h0 hpi)
    hc habs
  have heq : Lob θ₀ + (-Real.log (2 * Real.sin θ₀)) * (θ - θ₀)
        + (-(Real.cos θ₀ / Real.sin θ₀)) * ((θ - θ₀) ^ 2 / 2)
      = Lob θ₀ - Real.log (2 * Real.sin θ₀) * (θ - θ₀)
        - (Real.cos θ₀ / Real.sin θ₀) * ((θ - θ₀) ^ 2 / 2) := by ring
  rwa [heq] at h

/-! ## Part 3 — at the saddle `θ* = 5π/6` -/

/-- `sin(5π/6) = 1/2` — the saddle condition `2 sin θ* = 1`, at the point
`saddle_forces_cot` singles out in `(π/2, π)`. -/
@[simp] theorem sin_five_pi_div_six : Real.sin (5 * π / 6) = 1 / 2 := by
  rw [show (5 : ℝ) * π / 6 = π - π / 6 by ring, Real.sin_pi_sub,
    Real.sin_pi_div_six]

/-- `cos(5π/6) = −√3/2`. -/
@[simp] theorem cos_five_pi_div_six : Real.cos (5 * π / 6) = -(Real.sqrt 3 / 2) := by
  rw [show (5 : ℝ) * π / 6 = π - π / 6 by ring, Real.cos_pi_sub,
    Real.cos_pi_div_six]

/-- `cot(5π/6) = −√3` — the Hessian of the Kashaev exponent, up to `2N/π`. -/
theorem cot_five_pi_div_six :
    Real.cos (5 * π / 6) / Real.sin (5 * π / 6) = -Real.sqrt 3 := by
  rw [sin_five_pi_div_six, cos_five_pi_div_six]
  ring

/-- **`Λ` at the saddle.**  The linear term is absent because `Λ′(θ*) = 0`;
the quadratic coefficient is `√3/2 = |cot θ*|/2`. -/
theorem abs_Lob_taylor_saddle {θ M : ℝ}
    (hmem : ∀ x ∈ Set.uIcc (5 * π / 6) θ, 0 < x ∧ x < π)
    (hM : ∀ x ∈ Set.uIcc (5 * π / 6) θ, 1 / Real.sin x ^ 2 ≤ M) :
    |Lob θ - (Lob (5 * π / 6) + Real.sqrt 3 * ((θ - 5 * π / 6) ^ 2 / 2))|
      ≤ M * |θ - 5 * π / 6| ^ 3 / 6 := by
  have h := abs_Lob_taylor_two hmem hM
  -- cot FIRST: rewriting `sin(5π/6)` first would break `cos/sin` into `cos/(1/2)`
  rw [cot_five_pi_div_six, sin_five_pi_div_six] at h
  have hlog : Real.log (2 * (1 / 2 : ℝ)) = 0 := by norm_num
  rw [hlog] at h
  have heq : Lob (5 * π / 6) - 0 * (θ - 5 * π / 6)
        - -Real.sqrt 3 * ((θ - 5 * π / 6) ^ 2 / 2)
      = Lob (5 * π / 6) + Real.sqrt 3 * ((θ - 5 * π / 6) ^ 2 / 2) := by ring
  rwa [heq] at h

end QOU.Knot.FigureEightVolume
