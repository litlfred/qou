import QOU.Archimedean.DilogReflection
import QOU.Archimedean.DilogPartARiemannSum
import Mathlib.Analysis.Convex.Slope
import Mathlib.Analysis.Convex.SpecificFunctions.Basic

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

open QOU.QPochhammer intervalIntegral MeasureTheory

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

/-- Convexity of `g(u) = −log(1 - x u)` on `[0,1]` — `log` is concave on `(0,∞)`,
    `u ↦ 1 - x u` is affine mapping `[0,1]` into `(0,∞)` (since `x u ≤ x < 1`),
    and negation flips concave to convex. -/
theorem convexOn_neg_log_one_sub_mul {x : ℝ} (hx0 : 0 < x) (hx1 : x < 1) :
    ConvexOn ℝ (Set.Icc (0 : ℝ) 1) (fun u => -Real.log (1 - x * u)) := by
  set g : ℝ →ᵃ[ℝ] ℝ := AffineMap.const ℝ ℝ 1 - x • AffineMap.id ℝ ℝ with hg_def
  have hg_eval : ∀ u : ℝ, g u = 1 - x * u := by
    intro u; simp [hg_def]
  have hsub : Set.Icc (0 : ℝ) 1 ⊆ g ⁻¹' Set.Ioi 0 := by
    intro u hu
    rw [Set.mem_preimage, hg_eval, Set.mem_Ioi]
    obtain ⟨hu0, hu1⟩ := hu
    nlinarith [mul_le_mul_of_nonneg_left hu1 hx0.le]
  have hconc : ConcaveOn ℝ (Set.Icc (0 : ℝ) 1) (fun u => Real.log (1 - x * u)) := by
    have h1 := (strictConcaveOn_log_Ioi.concaveOn).comp_affineMap g
    have h2 := h1.subset hsub (convex_Icc 0 1)
    convert h2 using 1
  exact hconc.neg

/-- **B3.2 — monotonicity.**  `h(u) = −log(1 - x u)/u` is monotone increasing on
    `(0,1]` for `0 < x < 1`.  Convex-slope: with `g(u) = −log(1 - x u)` convex and
    `g(0) = 0`, `h(u) = (g u − g 0)/(u − 0)` is a secant slope from `0`, which is
    monotone for a convex function (`ConvexOn.secant_mono`). -/
theorem h_monotoneOn {x : ℝ} (hx0 : 0 < x) (hx1 : x < 1) :
    MonotoneOn (fun u : ℝ => -Real.log (1 - x * u) / u) (Set.Ioc (0 : ℝ) 1) := by
  have hconv := convexOn_neg_log_one_sub_mul hx0 hx1
  intro u hu v hv huv
  have h0mem : (0 : ℝ) ∈ Set.Icc (0 : ℝ) 1 := ⟨le_refl 0, zero_le_one⟩
  have humem : u ∈ Set.Icc (0 : ℝ) 1 := ⟨hu.1.le, hu.2⟩
  have hvmem : v ∈ Set.Icc (0 : ℝ) 1 := ⟨hv.1.le, hv.2⟩
  have hsec := hconv.secant_mono h0mem humem hvmem (ne_of_gt hu.1) (ne_of_gt hv.1) huv
  simpa [Real.log_one] using hsec

/-! ### B3.3 — per-cell monotone integral bounds -/

/-- `h(u) = −log(1 - x u)/u` is continuous on any `[a,b] ⊆ (0,1]`. -/
theorem h_continuousOn {x a b : ℝ} (hx0 : 0 < x) (hx1 : x < 1) (hb1 : b ≤ 1) (ha : 0 < a) :
    ContinuousOn (fun u => -Real.log (1 - x * u) / u) (Set.Icc a b) := by
  have hnum : ContinuousOn (fun u : ℝ => -Real.log (1 - x * u)) (Set.Icc a b) := by
    refine ContinuousOn.neg (ContinuousOn.log
      ((by fun_prop : Continuous (fun u : ℝ => 1 - x * u)).continuousOn) (fun u hu => ?_))
    have hxu : x * u ≤ x := by
      calc x * u ≤ x * b := mul_le_mul_of_nonneg_left hu.2 hx0.le
        _ ≤ x * 1 := mul_le_mul_of_nonneg_left hb1 hx0.le
        _ = x := mul_one x
    exact ne_of_gt (by linarith)
  exact hnum.div continuousOn_id (fun u hu => ne_of_gt (lt_of_lt_of_le ha hu.1))

/-- `h` is interval-integrable on any `[a,b] ⊆ (0,1]`. -/
theorem h_intervalIntegrable {x a b : ℝ} (hx0 : 0 < x) (hx1 : x < 1) (hb1 : b ≤ 1) (ha : 0 < a)
    (hab : a ≤ b) :
    IntervalIntegrable (fun u => -Real.log (1 - x * u) / u) volume a b := by
  apply ContinuousOn.intervalIntegrable
  rw [Set.uIcc_of_le hab]
  exact h_continuousOn hx0 hx1 hb1 ha

/-- **B3.3 upper cell bound.**  `∫_a^b h ≤ h(b)·(b−a)` on `[a,b] ⊆ (0,1]`
    (monotone: `h(b)` is the max). -/
theorem h_integral_le_right {x a b : ℝ} (hx0 : 0 < x) (hx1 : x < 1) (ha : 0 < a)
    (hb1 : b ≤ 1) (hab : a ≤ b) :
    (∫ u in a..b, -Real.log (1 - x * u) / u) ≤ (-Real.log (1 - x * b) / b) * (b - a) := by
  have hbmem : b ∈ Set.Ioc (0 : ℝ) 1 := ⟨lt_of_lt_of_le ha hab, hb1⟩
  calc (∫ u in a..b, -Real.log (1 - x * u) / u)
      ≤ ∫ _ in a..b, (-Real.log (1 - x * b) / b) := by
        refine integral_mono_on hab (h_intervalIntegrable hx0 hx1 hb1 ha hab)
          intervalIntegrable_const (fun u hu => ?_)
        exact h_monotoneOn hx0 hx1 ⟨lt_of_lt_of_le ha hu.1, le_trans hu.2 hb1⟩ hbmem hu.2
    _ = (-Real.log (1 - x * b) / b) * (b - a) := by
        rw [intervalIntegral.integral_const, smul_eq_mul]; ring

/-- **B3.3 lower cell bound.**  `h(a)·(b−a) ≤ ∫_a^b h` on `[a,b] ⊆ (0,1]`
    (monotone: `h(a)` is the min). -/
theorem h_integral_ge_left {x a b : ℝ} (hx0 : 0 < x) (hx1 : x < 1) (ha : 0 < a)
    (hb1 : b ≤ 1) (hab : a ≤ b) :
    (-Real.log (1 - x * a) / a) * (b - a) ≤ ∫ u in a..b, -Real.log (1 - x * u) / u := by
  have hamem : a ∈ Set.Ioc (0 : ℝ) 1 := ⟨ha, le_trans hab hb1⟩
  calc (-Real.log (1 - x * a) / a) * (b - a)
      = ∫ _ in a..b, (-Real.log (1 - x * a) / a) := by
        rw [intervalIntegral.integral_const, smul_eq_mul]; ring
    _ ≤ ∫ u in a..b, -Real.log (1 - x * u) / u := by
        refine integral_mono_on hab intervalIntegrable_const
          (h_intervalIntegrable hx0 hx1 hb1 ha hab) (fun u hu => ?_)
        exact h_monotoneOn hx0 hx1 hamem ⟨lt_of_lt_of_le ha hu.1, le_trans hu.2 hb1⟩ hu.1

end QOU.Archimedean
