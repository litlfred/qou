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

-- Ref: [leitner2026] conj:dilogarithm-archimedean-limit
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

/-! ### B3.3b — the telescoping Riemann-sum error bound -/

/-- **B3.3b — the Riemann-sum error bound.**  The left-Riemann sum
    `S_n = Σ_{k<n} h(qᵏ)·(qᵏ − qᵏ⁺¹)` over-estimates `∫_{qⁿ}^1 h` by at most
    `(1-q)·(h(1) − h(qⁿ))`:  `0 ≤ S_n − ∫_{qⁿ}^1 h ≤ (1-q)·(h(1) − h(qⁿ))`.
    Proof by induction: each step adds a cell whose error is squeezed by the
    per-cell bounds (B3.3a) and telescopes. -/
theorem riemann_error_bound {x q : ℝ} (hx0 : 0 < x) (hx1 : x < 1)
    (hq0 : 0 < q) (hq1 : q < 1) (n : ℕ) :
    0 ≤ (∑ k ∈ Finset.range n,
            (-Real.log (1 - x * q ^ k) / q ^ k) * (q ^ k - q ^ (k + 1)))
          - ∫ u in q ^ n..(1 : ℝ), -Real.log (1 - x * u) / u
      ∧ (∑ k ∈ Finset.range n,
            (-Real.log (1 - x * q ^ k) / q ^ k) * (q ^ k - q ^ (k + 1)))
          - ∫ u in q ^ n..(1 : ℝ), -Real.log (1 - x * u) / u
        ≤ (1 - q) * ((-Real.log (1 - x * 1) / 1)
            - (-Real.log (1 - x * q ^ n) / q ^ n)) := by
  induction n with
  | zero => refine ⟨?_, ?_⟩ <;> simp [intervalIntegral.integral_same]
  | succ m ih =>
    obtain ⟨ih_lo, ih_hi⟩ := ih
    have hqm1_pos : (0 : ℝ) < q ^ (m + 1) := pow_pos hq0 _
    have hqm_pos : (0 : ℝ) < q ^ m := pow_pos hq0 _
    have hqm_le1 : q ^ m ≤ 1 := pow_le_one₀ hq0.le hq1.le
    have hq_le : q ^ (m + 1) ≤ q ^ m := by
      rw [pow_succ]; exact mul_le_of_le_one_right (pow_nonneg hq0.le m) hq1.le
    -- per-cell squeeze on the new cell [qᵐ⁺¹, qᵐ]
    have hJ_le := h_integral_le_right hx0 hx1 hqm1_pos hqm_le1 hq_le
    have hJ_ge := h_integral_ge_left hx0 hx1 hqm1_pos hqm_le1 hq_le
    -- integral split ∫_{qᵐ⁺¹}^1 = ∫_{qᵐ⁺¹}^{qᵐ} + ∫_{qᵐ}^1
    have hsplit :
        (∫ u in q ^ (m + 1)..(1 : ℝ), -Real.log (1 - x * u) / u)
          = (∫ u in q ^ (m + 1)..q ^ m, -Real.log (1 - x * u) / u)
            + ∫ u in q ^ m..(1 : ℝ), -Real.log (1 - x * u) / u :=
      (intervalIntegral.integral_add_adjacent_intervals
        (h_intervalIntegrable hx0 hx1 hqm_le1 hqm1_pos hq_le)
        (h_intervalIntegrable hx0 hx1 le_rfl hqm_pos hqm_le1)).symm
    -- monotone gap h(qᵐ) − h(qᵐ⁺¹) ≥ 0 and width qᵐ − qᵐ⁺¹ ≤ 1 − q
    have hmono := h_monotoneOn hx0 hx1
      ⟨hqm1_pos, le_trans hq_le hqm_le1⟩ ⟨hqm_pos, hqm_le1⟩ hq_le
    have hwidth : q ^ m - q ^ (m + 1) ≤ 1 - q := by
      have : q ^ m - q ^ (m + 1) = q ^ m * (1 - q) := by rw [pow_succ]; ring
      rw [this]
      calc q ^ m * (1 - q) ≤ 1 * (1 - q) :=
            mul_le_mul_of_nonneg_right hqm_le1 (by linarith)
        _ = 1 - q := one_mul _
    have hprod :
        ((-Real.log (1 - x * q ^ m) / q ^ m) - (-Real.log (1 - x * q ^ (m + 1)) / q ^ (m + 1)))
            * (q ^ m - q ^ (m + 1))
          ≤ ((-Real.log (1 - x * q ^ m) / q ^ m) - (-Real.log (1 - x * q ^ (m + 1)) / q ^ (m + 1)))
            * (1 - q) :=
      mul_le_mul_of_nonneg_left hwidth (by simp only [Function.const] at hmono ⊢; linarith)
    rw [Finset.sum_range_succ, hsplit]
    constructor
    · nlinarith [ih_lo, hJ_le]
    · nlinarith [ih_hi, hJ_ge, hprod]

/-! ### B3.4 — the tail `∫₀^b h` -/

/-- `0 ≤ h(u) ≤ x/(1-x)` on `(0,1]` (the integrand is bounded near `0`). -/
theorem h_bounds_Ioc {x u : ℝ} (hx0 : 0 < x) (hx1 : x < 1) (hu0 : 0 < u) (hu1 : u ≤ 1) :
    0 ≤ -Real.log (1 - x * u) / u ∧ -Real.log (1 - x * u) / u ≤ x / (1 - x) := by
  have hxu1 : x * u < 1 := by nlinarith [mul_le_mul_of_nonneg_left hu1 hx0.le]
  have h1xu : (0 : ℝ) < 1 - x * u := by linarith
  have h1x : (0 : ℝ) < 1 - x := by linarith
  have hnn : (0 : ℝ) ≤ -Real.log (1 - x * u) := by
    have hlp : Real.log (1 - x * u) ≤ 0 :=
      Real.log_nonpos h1xu.le (by nlinarith [mul_nonneg hx0.le hu0.le])
    linarith
  refine ⟨div_nonneg hnn hu0.le, ?_⟩
  have hlog2 : -Real.log (1 - x * u) * (1 - x * u) ≤ x * u := by
    have h := Real.one_sub_inv_le_log_of_pos h1xu
    have hmul : (1 - (1 - x * u)⁻¹) * (1 - x * u) ≤ Real.log (1 - x * u) * (1 - x * u) :=
      mul_le_mul_of_nonneg_right h h1xu.le
    have hlhs : (1 - (1 - x * u)⁻¹) * (1 - x * u) = -(x * u) := by field_simp; ring
    rw [hlhs] at hmul; nlinarith [hmul]
  rw [div_le_iff₀ hu0, div_mul_eq_mul_div, le_div_iff₀ h1x]
  have hle : -Real.log (1 - x * u) * (1 - x) ≤ -Real.log (1 - x * u) * (1 - x * u) :=
    mul_le_mul_of_nonneg_left (by nlinarith [mul_le_mul_of_nonneg_left hu1 hx0.le]) hnn
  linarith [hle, hlog2]

/-- Tail integrability: `h` is interval-integrable on `[0,b]` for `0 < b ≤ 1`
    (continuous on `(0,b]`, bounded by `x/(1-x)`). -/
theorem h_intervalIntegrable_zero {x b : ℝ} (hx0 : 0 < x) (hx1 : x < 1) (hb0 : 0 < b)
    (hb1 : b ≤ 1) :
    IntervalIntegrable (fun u => -Real.log (1 - x * u) / u) volume 0 b := by
  rw [intervalIntegrable_iff_integrableOn_Ioc_of_le hb0.le]
  have hcontOn : ContinuousOn (fun u => -Real.log (1 - x * u) / u) (Set.Ioc 0 b) := by
    have hnum : ContinuousOn (fun u : ℝ => -Real.log (1 - x * u)) (Set.Ioc 0 b) := by
      refine ContinuousOn.neg (ContinuousOn.log
        ((by fun_prop : Continuous (fun u : ℝ => 1 - x * u)).continuousOn) (fun u hu => ?_))
      have : x * u < 1 := by nlinarith [mul_le_mul_of_nonneg_left (le_trans hu.2 hb1) hx0.le]
      exact ne_of_gt (by linarith)
    exact hnum.div continuousOn_id (fun u hu => ne_of_gt hu.1)
  have hmeas : AEStronglyMeasurable (fun u => -Real.log (1 - x * u) / u)
      (volume.restrict (Set.Ioc (0 : ℝ) b)) := hcontOn.aestronglyMeasurable measurableSet_Ioc
  haveI : IsFiniteMeasure (volume.restrict (Set.Ioc (0 : ℝ) b)) :=
    ⟨by rw [Measure.restrict_apply_univ]; exact measure_Ioc_lt_top⟩
  refine Integrable.mono' (g := fun _ => x / (1 - x)) (integrable_const _) hmeas ?_
  refine ae_restrict_of_forall_mem measurableSet_Ioc (fun u hu => ?_)
  obtain ⟨hb, hub⟩ := (h_bounds_Ioc hx0 hx1 hu.1 (le_trans hu.2 hb1))
  rw [Real.norm_eq_abs, abs_of_nonneg hb]; exact hub

/-- **B3.4 — tail bound.**  `0 ≤ ∫₀^b h ≤ b·x/(1-x)` for `0 < b ≤ 1`. -/
theorem tail_bound {x b : ℝ} (hx0 : 0 < x) (hx1 : x < 1) (hb0 : 0 < b) (hb1 : b ≤ 1) :
    0 ≤ (∫ u in (0 : ℝ)..b, -Real.log (1 - x * u) / u)
      ∧ (∫ u in (0 : ℝ)..b, -Real.log (1 - x * u) / u) ≤ b * (x / (1 - x)) := by
  have hint := h_intervalIntegrable_zero hx0 hx1 hb0 hb1
  constructor
  · refine intervalIntegral.integral_nonneg hb0.le (fun u hu => ?_)
    rcases eq_or_lt_of_le hu.1 with h0 | h0
    · rw [← h0]; simp
    · exact (h_bounds_Ioc hx0 hx1 h0 (le_trans hu.2 hb1)).1
  · calc (∫ u in (0 : ℝ)..b, -Real.log (1 - x * u) / u)
        ≤ ∫ _ in (0 : ℝ)..b, x / (1 - x) := by
          refine intervalIntegral.integral_mono_on hb0.le hint intervalIntegrable_const
            (fun u hu => ?_)
          rcases eq_or_lt_of_le hu.1 with h0 | h0
          · rw [← h0]; simp; exact div_nonneg hx0.le (by linarith)
          · exact (h_bounds_Ioc hx0 hx1 h0 (le_trans hu.2 hb1)).2
      _ = b * (x / (1 - x)) := by rw [intervalIntegral.integral_const, smul_eq_mul]; ring

/-! ### B3.5 — assembling the `ArchimedeanLimit x` instance -/

/-- `qⁿ ≤ exp(−n·(1−q))` for `0 < q` (from `log q ≤ q − 1`). -/
theorem pow_le_exp_neg_mul {q : ℝ} (hq0 : 0 < q) (n : ℕ) :
    q ^ n ≤ Real.exp (-((n : ℝ) * (1 - q))) := by
  have hlog : Real.log (q ^ n) ≤ -((n : ℝ) * (1 - q)) := by
    rw [Real.log_pow]
    have hlq : Real.log q ≤ q - 1 := Real.log_le_sub_one_of_pos hq0
    have hn : (0 : ℝ) ≤ (n : ℝ) := Nat.cast_nonneg n
    nlinarith [mul_le_mul_of_nonneg_left hlq hn]
  calc q ^ n = Real.exp (Real.log (q ^ n)) := (Real.exp_log (pow_pos hq0 n)).symm
    _ ≤ Real.exp (-((n : ℝ) * (1 - q))) := Real.exp_le_exp.mpr hlog

/-- **B3.5 — Part-A convergence.**  For `0 < x < 1`, the Faddeev-scaling limit
    `(1-q)·log Φ_n(x;q) → Li₂(x)` holds: `ArchimedeanLimit x`.  Assembled from the
    Riemann-sum identity (Bricks 1–2), the telescoping error bound
    (`riemann_error_bound`), the tail bound (`tail_bound`), and the target integral
    (`integral_zero_one_eq_LiTwo`).  This discharges the last open field of Part A
    of `conj:dilogarithm-archimedean-limit`. -/
theorem archimedeanLimit_Ioo {x : ℝ} (hx0 : 0 < x) (hx1 : x < 1) :
    ArchimedeanLimit x := by
  refine ⟨fun ε hε => ?_⟩
  have h1x : (0 : ℝ) < 1 - x := by linarith
  have hL_pos : 0 < -Real.log (1 - x) := neg_pos.mpr (Real.log_neg h1x (by linarith))
  have hC_pos : 0 < x / (1 - x) := div_pos hx0 h1x
  set L := -Real.log (1 - x) with hLdef
  set C := x / (1 - x) with hCdef
  set D := max 1 (Real.log (2 * C / ε)) with hDdef
  have hD1 : (1 : ℝ) ≤ D := le_max_left _ _
  have hDpos : 0 < D := lt_of_lt_of_le one_pos hD1
  set δ := min (ε / (2 * L)) (1 / D) with hδdef
  have hδ_pos : 0 < δ := lt_min (by positivity) (by positivity)
  refine ⟨δ, hδ_pos, fun q n hyp => ?_⟩
  obtain ⟨hq_lo, hq1, hn⟩ := hyp
  have hδ_le1 : δ ≤ 1 := le_trans (min_le_right _ _) ((div_le_one hDpos).mpr hD1)
  have hq0 : 0 < q := by linarith
  have hq1le : q ≤ 1 := hq1.le
  have hqn_pos : 0 < q ^ n := pow_pos hq0 n
  have hqn_le1 : q ^ n ≤ 1 := pow_le_one₀ hq0.le hq1le
  -- two ε/2 bounds
  have hbound1 : (1 - q) * L < ε / 2 := by
    have h1 : 1 - q < δ := by linarith
    calc (1 - q) * L < δ * L := mul_lt_mul_of_pos_right h1 hL_pos
      _ ≤ (ε / (2 * L)) * L := mul_le_mul_of_nonneg_right (min_le_left _ _) hL_pos.le
      _ = ε / 2 := by field_simp
  have hbound2 : q ^ n * C < ε / 2 := by
    have hqn_le : q ^ n ≤ Real.exp (-((n : ℝ) * (1 - q))) := pow_le_exp_neg_mul hq0 n
    have hlt : Real.exp (-((n : ℝ) * (1 - q))) < Real.exp (-δ⁻¹) :=
      Real.exp_lt_exp.mpr (by linarith [hn])
    have hDδinv : D ≤ δ⁻¹ := by
      have hδD : δ ≤ 1 / D := min_le_right _ _
      rw [← one_div, le_div_iff₀ hδ_pos, mul_comm]
      exact (le_div_iff₀ hDpos).mp hδD
    have hexp_le : Real.exp (-δ⁻¹) ≤ ε / (2 * C) := by
      have hy : (0 : ℝ) < 2 * C / ε := by positivity
      have hstep : Real.exp (-δ⁻¹) ≤ Real.exp (-Real.log (2 * C / ε)) :=
        Real.exp_le_exp.mpr (by linarith [le_max_right (1 : ℝ) (Real.log (2 * C / ε))])
      have hval : Real.exp (-Real.log (2 * C / ε)) = ε / (2 * C) := by
        rw [Real.exp_neg, Real.exp_log hy, inv_div]
      rwa [hval] at hstep
    calc q ^ n * C ≤ Real.exp (-((n : ℝ) * (1 - q))) * C :=
          mul_le_mul_of_nonneg_right hqn_le hC_pos.le
      _ < Real.exp (-δ⁻¹) * C := mul_lt_mul_of_pos_right hlt hC_pos
      _ ≤ (ε / (2 * C)) * C := mul_le_mul_of_nonneg_right hexp_le hC_pos.le
      _ = ε / 2 := by field_simp
  -- (1-q)·log Φ_n = S_n (Bricks 1+2)
  rw [Real.norm_eq_abs,
      show (1 - q) * Real.log (partialProductLocal q x n)
        = ∑ k ∈ Finset.range n,
            -Real.log (1 - x * q ^ k) / q ^ k * (q ^ k - q ^ (k + 1)) by
        have hlog : Real.log (partialProductLocal q x n)
            = ∑ k ∈ Finset.range n, -Real.log (1 - x * q ^ k) := by
          rw [log_partialProduct_eq_neg_sum hx0 hx1 hq0 hq1le n]; simp
        rw [hlog, riemann_sum_form hq0 n]]
  obtain ⟨hE_lo, hE_hi⟩ := riemann_error_bound hx0 hx1 hq0 hq1 n
  obtain ⟨hT_lo, hT_hi⟩ := tail_bound hx0 hx1 hqn_pos hqn_le1
  have hI : LiTwo x
      = (∫ u in (0 : ℝ)..q ^ n, -Real.log (1 - x * u) / u)
        + ∫ u in q ^ n..(1 : ℝ), -Real.log (1 - x * u) / u := by
    rw [← integral_zero_one_eq_LiTwo hx0 hx1]
    exact (intervalIntegral.integral_add_adjacent_intervals
      (h_intervalIntegrable_zero hx0 hx1 hqn_pos hqn_le1)
      (h_intervalIntegrable hx0 hx1 le_rfl hqn_pos hqn_le1)).symm
  have hhqn_nonneg : 0 ≤ -Real.log (1 - x * q ^ n) / q ^ n :=
    (h_bounds_Ioc hx0 hx1 hqn_pos hqn_le1).1
  have hE_hi' :
      (∑ k ∈ Finset.range n, -Real.log (1 - x * q ^ k) / q ^ k * (q ^ k - q ^ (k + 1)))
        - ∫ u in q ^ n..(1 : ℝ), -Real.log (1 - x * u) / u ≤ (1 - q) * L := by
    refine le_trans hE_hi ?_
    have hh1 : -Real.log (1 - x * 1) / 1 = L := by rw [mul_one, div_one]
    rw [hh1]
    nlinarith [hhqn_nonneg, hq1, mul_nonneg (by linarith : (0:ℝ) ≤ 1 - q) hhqn_nonneg]
  rw [abs_lt]
  have hsplit :
      (∑ k ∈ Finset.range n, -Real.log (1 - x * q ^ k) / q ^ k * (q ^ k - q ^ (k + 1)))
        - LiTwo x
      = ((∑ k ∈ Finset.range n, -Real.log (1 - x * q ^ k) / q ^ k * (q ^ k - q ^ (k + 1)))
            - ∫ u in q ^ n..(1 : ℝ), -Real.log (1 - x * u) / u)
        - ∫ u in (0 : ℝ)..q ^ n, -Real.log (1 - x * u) / u := by
    rw [hI]; ring
  rw [hsplit]
  refine ⟨by nlinarith [hE_lo, hT_hi, hbound2, hε], by nlinarith [hE_hi', hT_lo, hbound1, hε]⟩

/-- **Unconditional Part-A limit on `(0,1)`.**  With `archimedeanLimit_Ioo` the
    `[ArchimedeanLimit x]` typeclass gate on the conditional consumer
    `partialProduct_to_LiTwo` is discharged for every `x ∈ (0,1)`: the Faddeev-
    scaling convergence `(1-q)·log Φ_n(x;q) → Li₂(x)` holds outright, no instance
    hypothesis required. -/
theorem partialProduct_to_LiTwo_Ioo {x : ℝ} (hx0 : 0 < x) (hx1 : x < 1)
    (ε : ℝ) (hε : 0 < ε) :
    ∃ δ > (0 : ℝ), ∀ (q : ℝ) (n : ℕ),
      (1 - δ < q) ∧ (q < 1) ∧ (n : ℝ) * (1 - q) > δ⁻¹ →
        ‖(1 - q) * Real.log (partialProductLocal q x n) - LiTwo x‖ < ε :=
  haveI := archimedeanLimit_Ioo hx0 hx1
  partialProduct_to_LiTwo x ε hε

end QOU.Archimedean
