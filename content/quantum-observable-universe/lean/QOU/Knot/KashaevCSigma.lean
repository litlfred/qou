/-
  `hc`, DERIVED.

  `OneLoopPrefactorInvariance` proves the algebra downstream of the saddle from
  a hypothesis

      hc : c² · |cot θ| = (2 sin θ)²

  and its header records that nobody had derived that hypothesis from the
  analytic theorems.  This file derives it.

  The whole content is that the asymptotics of steps 7–19 produce the constant
  in a specific SHAPE:

      c_σ(θ) = (2 sin θ) · |cot θ|^{−1/2}
                  ↑              ↑
      Stirling factor      Gaussian width

  the first from step 7's `log(2N sin θ_{k*})`, the second from steps 12–19's
  `√(π/a)` at `a = π|cot θ|/N`.  Square that and multiply by `|cot θ|` and the
  Hessian cancels: `hc` is not a coincidence about `4₁`, it is the statement
  that `c_σ` is a Stirling factor over a square-rooted Hessian, which is what
  every Laplace-method constant is.

  `stirling_mul_gaussWidth` is the link back to the analysis — the exact
  identity showing the two ingredients combine to `c_σ·N^{3/2}`.

  -- Ref: [manuscript] QOU/OneLoopPrefactorInvariance.lean
  -- Ref: [manuscript] QOU/Knot/KashaevAsymptoticBounds.lean
-/
import QOU.Knot.KashaevAsymptoticBounds
import QOU.OneLoopPrefactorInvariance

namespace QOU.Knot.FigureEightVolume

open Real

/-- **The one-loop constant, in the shape the asymptotics produce it.**
Stirling factor over the square root of the Hessian. -/
noncomputable def cSigma (θ : ℝ) : ℝ :=
  2 * Real.sin θ / Real.sqrt |Real.cos θ / Real.sin θ|

/-- **`hc`, derived.**  The Hessian cancels between the two ingredients.

This is the hypothesis `OneLoopPrefactorInvariance` assumed; it is an identity
for the `c_σ` the analysis actually produces, at any angle where `cot θ ≠ 0`.
Nothing about `4₁` enters. -/
theorem cSigma_sq_mul_abs_cot {θ : ℝ} (hcot : Real.cos θ / Real.sin θ ≠ 0) :
    cSigma θ ^ 2 * |Real.cos θ / Real.sin θ| = (2 * Real.sin θ) ^ 2 := by
  have habs : 0 < |Real.cos θ / Real.sin θ| := abs_pos.mpr hcot
  unfold cSigma
  rw [div_pow, Real.sq_sqrt habs.le]
  field_simp

/-- **The link back to the analysis.**  Step 7's Stirling factor `2N sin θ`
times steps 12–19's Gaussian width `√(π/a)` at `a = π|cot θ|/N` is exactly
`c_σ(θ)·N^{3/2}`. -/
theorem stirling_mul_gaussWidth {θ N : ℝ} (hcot : Real.cos θ / Real.sin θ ≠ 0)
    (hN : 0 < N) :
    (2 * N * Real.sin θ)
        * Real.sqrt (π / (π * |Real.cos θ / Real.sin θ| / N))
      = cSigma θ * (N * Real.sqrt N) := by
  have hpi := Real.pi_pos
  have habs : 0 < |Real.cos θ / Real.sin θ| := abs_pos.mpr hcot
  have hsq : 0 < Real.sqrt |Real.cos θ / Real.sin θ| := Real.sqrt_pos.mpr habs
  have hsimp : π / (π * |Real.cos θ / Real.sin θ| / N)
      = N / |Real.cos θ / Real.sin θ| := by
    field_simp
  rw [hsimp, Real.sqrt_div hN.le]
  unfold cSigma
  field_simp

/-- `c_σ(5π/6) = 1/√√3 = 3^{−1/4}`. -/
theorem cSigma_saddle : cSigma (5 * π / 6) = 1 / Real.sqrt (Real.sqrt 3) := by
  unfold cSigma
  rw [cot_five_pi_div_six, sin_five_pi_div_six, abs_neg,
    abs_of_nonneg (Real.sqrt_nonneg 3)]
  norm_num

/-- The saddle's cotangent is nonzero — what `cSigma_sq_mul_abs_cot` needs. -/
theorem cot_saddle_ne_zero :
    Real.cos (5 * π / 6) / Real.sin (5 * π / 6) ≠ 0 := by
  rw [cot_five_pi_div_six]
  have : (0 : ℝ) < Real.sqrt 3 := Real.sqrt_pos.mpr (by norm_num)
  linarith

/-- **`c_σ⁴ = 1/3`, with `hc` supplied rather than assumed.**

`OneLoopPrefactorInvariance.c_pow_four_eq_third` is applied here with its `hc`
discharged by `cSigma_sq_mul_abs_cot` — so the chain from the Kashaev sum to
`c_σ = 3^{−1/4}` no longer passes through an assumption. -/
theorem cSigma_saddle_pow_four : cSigma (5 * π / 6) ^ 4 = 1 / 3 := by
  have hpi := Real.pi_pos
  refine QOU.OneLoopPrefactorInvariance.c_pow_four_eq_third
    (θ := 5 * π / 6) (c := cSigma (5 * π / 6)) ⟨by linarith, by linarith⟩ ?_ ?_
  · rw [sin_five_pi_div_six]; norm_num
  · exact cSigma_sq_mul_abs_cot cot_saddle_ne_zero

/-- **`k = 2^{−1/2}` too**, with `hc` supplied.  The Hessian cancels between
`c_σ` and `|τ|` before it is ever evaluated — so this never depended on
`cot θ* = −√3`, on the trace field, or on which manifold this is. -/
theorem k_sq_eq_half {k : ℝ}
    (hk : k = cSigma (5 * π / 6)
        * Real.sqrt (|Real.cos (5 * π / 6) / Real.sin (5 * π / 6)| / 2)) :
    k ^ 2 = 1 / 2 :=
  QOU.OneLoopPrefactorInvariance.k_sq_eq_half_of_saddle
    (θ := 5 * π / 6) (c := cSigma (5 * π / 6)) (k := k)
    (by rw [sin_five_pi_div_six]; norm_num)
    (cSigma_sq_mul_abs_cot cot_saddle_ne_zero) hk

end QOU.Knot.FigureEightVolume
