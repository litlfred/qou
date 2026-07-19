import QOU.Archimedean.DilogReflection
import QOU.Archimedean.DilogPartARiemannSum

/-!
# Part A of `conj:dilogarithm-archimedean-limit` — the convergence core (Brick 3)

The remaining analytic core of Part A: the geometric-partition Riemann sum
`(1-q)·Σ_{k<n} −log(1 - x qᵏ)` (= `log Φ_n`, Brick 1; = a left-Riemann sum,
Brick 2) converges to `∫₀¹ −log(1 - x u)/u du = Li₂(x)` as `q → 1⁻`,
`n(1-q) → ∞`.

Sub-bricks:

* **B3.1 `integral_zero_one_eq_LiTwo`** — `∫₀¹ −log(1 - x u)/u du = Li₂(x)`, the
  change of variables `t = x u` from `LiTwo_eq_integral` (Brick A / PR #4088).
  This is the integral the Riemann sum targets.

Further sub-bricks (B3.2 Lipschitz bound on the integrand, B3.3 Riemann-sum
error, B3.4 tail control, B3.5 the `ArchimedeanLimit` instance) build on B3.1.
No `ArchimedeanLimit` instance is fabricated — the convergence is proved, not
axiomatised.

-- Ref: [manuscript] conj:dilogarithm-archimedean-limit
-/

namespace QOU.Archimedean

open QOU.QPochhammer intervalIntegral

/-- **B3.1 — the target integral.**  `∫₀¹ −log(1 - x u)/u du = Li₂(x)` for
    `0 < x < 1`, via the change of variables `t = x u` in `LiTwo_eq_integral`. -/
theorem integral_zero_one_eq_LiTwo {x : ℝ} (hx0 : 0 < x) (hx1 : x < 1) :
    (∫ u in (0 : ℝ)..1, -Real.log (1 - x * u) / u) = LiTwo x := by
  have key : x • ∫ u in (0 : ℝ)..1, -Real.log (1 - x * u) / (x * u)
      = ∫ t in (0 : ℝ)..x, -Real.log (1 - t) / t := by
    have h := smul_integral_comp_mul_left
      (f := fun t => -Real.log (1 - t) / t) (a := (0 : ℝ)) (b := 1) x
    simpa using h
  rw [LiTwo_eq_integral hx0 hx1, ← key, ← intervalIntegral.integral_smul]
  refine intervalIntegral.integral_congr (fun u _ => ?_)
  simp only [smul_eq_mul]
  rw [← mul_div_assoc, mul_div_mul_left _ _ (ne_of_gt hx0)]

end QOU.Archimedean
