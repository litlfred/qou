import QOU.Archimedean.DilogPartAConvergence

/-!
# Part B of `conj:dilogarithm-archimedean-limit` — the positive-factor branch-point sum (V3)

The `W-P1` half of the Part-B cusp cancellation: for the substrate side `q > 1`,
the positive factors `k ≤ k*` (`k* = log_q(1/x)`, `x qᵏ < 1`) give a geometric
Riemann sum running **up to the branch point** `x u = 1`, converging to
`Li₂(x) − π²/6`.

This file builds the target-integral bricks. The genuine analytic core — the
improper limit at the branch point and the variable-term (`k* = ⌊log_q(1/x)⌋`)
Riemann sum — is scoped in bean `qou-jplv` and not yet discharged here.

* `integral_Icc_eq_LiTwo_sub` — **V3 brick 1**, the *interior* target integral
  `∫_x^c −log(1−t)/t = Li₂(c) − Li₂(x)` for `0 < x ≤ c < 1`, straight from the
  dilog derivative `hasDerivAt_LiTwo` + FTC (both endpoints in `(0,1)`, so the
  integrand is continuous — no branch-point/`t=0` singularity).

-- Ref: [manuscript] conj:dilogarithm-archimedean-limit
-- Ref: [faddeev1994] https://doi.org/10.1142/S0217732394002793
-/

namespace QOU.Archimedean

open QOU.QPochhammer intervalIntegral MeasureTheory Filter Topology

/-- **V3 brick 1 — the interior target integral.**  For `0 < x ≤ c < 1`,
    `∫_x^c −log(1−t)/t = Li₂(c) − Li₂(x)`.  Since `−log(1−t)/t` is the derivative
    of `Li₂` (`hasDerivAt_LiTwo`) and both endpoints lie in `(0,1)`, this is a
    proper FTC — the integrand is continuous on `[x,c]` (no `t=0` or branch-point
    singularity).  Taking `c → 1⁻` (with `LiTwo_one`) will give the branch-point
    value `π²/6 − Li₂(x)` (V3 brick 2, the improper step). -/
theorem integral_Icc_eq_LiTwo_sub {x c : ℝ} (hx0 : 0 < x) (hxc : x ≤ c)
    (hc1 : c < 1) : (∫ t in (x : ℝ)..c, -Real.log (1 - t) / t) = LiTwo c - LiTwo x := by
  have hderiv : ∀ t ∈ Set.uIcc x c, HasDerivAt LiTwo (-Real.log (1 - t) / t) t := by
    intro t ht
    rw [Set.uIcc_of_le hxc] at ht
    exact hasDerivAt_LiTwo (lt_of_lt_of_le hx0 ht.1) (lt_of_le_of_lt ht.2 hc1)
  have hint : IntervalIntegrable (fun t => -Real.log (1 - t) / t) volume x c := by
    apply ContinuousOn.intervalIntegrable
    rw [Set.uIcc_of_le hxc]
    refine ContinuousOn.div ?_ continuousOn_id
      (fun t ht => ne_of_gt (lt_of_lt_of_le hx0 ht.1))
    refine ContinuousOn.neg (ContinuousOn.log (continuousOn_const.sub continuousOn_id)
      (fun t ht => ne_of_gt ?_))
    have := ht.2; linarith
  exact intervalIntegral.integral_eq_sub_of_hasDerivAt hderiv hint

/-- **V3 brick 2 — the improper target integral (branch-point limit).**  For
    `0 < x < 1`, as the upper endpoint `c → 1⁻` the interior integral converges to
    the branch-point value:

    `∫_x^c −log(1−t)/t  ⟶  π²/6 − Li₂(x)`.

    Combines brick 1 (`= Li₂(c) − Li₂(x)` on `[x,1)`) with the corpus Abel limit
    `tendsto_LiTwo_nhdsWithin_lt_one` (`Li₂(c) → π²/6`).  Since
    `∫_x^1 −log(1−t)/t = Li₂(1) − Li₂(x) = π²/6 − Li₂(x)`, this is the target the
    positive-factor Riemann sum (`W-P1`) converges to — the last, singular, cell
    of the `q > 1` geometric partition contributing the cusp regulator `ζ(2)`. -/
theorem tendsto_integral_x_to_c_nhdsWithin_one {x : ℝ} (hx0 : 0 < x) (hx1 : x < 1) :
    Tendsto (fun c : ℝ => ∫ t in (x : ℝ)..c, -Real.log (1 - t) / t) (𝓝[<] 1)
      (𝓝 (Real.pi ^ 2 / 6 - LiTwo x)) := by
  have hcong : (fun c : ℝ => ∫ t in (x : ℝ)..c, -Real.log (1 - t) / t)
      =ᶠ[𝓝[<] 1] (fun c => LiTwo c - LiTwo x) := by
    have hmem : Set.Ico x 1 ∈ 𝓝[<] (1 : ℝ) := by
      rw [← Set.Ici_inter_Iio]
      exact inter_mem (mem_nhdsWithin_of_mem_nhds (Ici_mem_nhds hx1)) self_mem_nhdsWithin
    filter_upwards [hmem] with c hc
    exact integral_Icc_eq_LiTwo_sub hx0 hc.1 hc.2
  refine Tendsto.congr' hcong.symm ?_
  exact tendsto_LiTwo_nhdsWithin_lt_one.sub_const (LiTwo x)

/-! ### V3 brick 3 — the going-up (`q > 1`) Riemann-sum ingredients

The `q > 1` positive-factor sum is a geometric Riemann sum on cells
`[qᵏ, qᵏ⁺¹] ⊆ [1, 1/x)` running up to the branch point.  The per-cell squeeze
needs the convexity/monotonicity of the integrand `h(u) = −log(1−xu)/u` on the
*wider* interval `[0, b]` with `x·b < 1` (Part A's versions are the special case
`b = 1`).  These generalise the Part-A bricks with `1 ≤ · ⇒ x·b < 1`. -/

/-- Convexity of `g(u) = −log(1 − x u)` on `[0, b]` whenever `x·b < 1` — the
    going-up generalisation of `convexOn_neg_log_one_sub_mul` (which is `b = 1`).
    `log` is concave on `(0,∞)`, `u ↦ 1 − x u` is affine mapping `[0,b]` into
    `(0,∞)` (since `x u ≤ x b < 1`), negation flips concave to convex. -/
theorem convexOn_neg_log_one_sub_mul_Icc {x b : ℝ} (hx0 : 0 < x) (hb : x * b < 1) :
    ConvexOn ℝ (Set.Icc (0 : ℝ) b) (fun u => -Real.log (1 - x * u)) := by
  set g : ℝ →ᵃ[ℝ] ℝ := AffineMap.const ℝ ℝ 1 - x • AffineMap.id ℝ ℝ with hg_def
  have hg_eval : ∀ u : ℝ, g u = 1 - x * u := by intro u; simp [hg_def]
  have hsub : Set.Icc (0 : ℝ) b ⊆ g ⁻¹' Set.Ioi 0 := by
    intro u hu
    rw [Set.mem_preimage, hg_eval, Set.mem_Ioi]
    obtain ⟨hu0, hub⟩ := hu
    nlinarith [mul_le_mul_of_nonneg_left hub hx0.le]
  have hconc : ConcaveOn ℝ (Set.Icc (0 : ℝ) b) (fun u => Real.log (1 - x * u)) := by
    have h1 := (strictConcaveOn_log_Ioi.concaveOn).comp_affineMap g
    have h2 := h1.subset hsub (convex_Icc 0 b)
    convert h2 using 1
  exact hconc.neg

/-- Monotonicity of `h(u) = −log(1 − x u)/u` on `(0, b]` whenever `x·b < 1` — the
    going-up generalisation of `h_monotoneOn` (which is `b = 1`).  Convex-slope:
    `h(u) = (g u − g 0)/(u − 0)` is a secant slope from `0` of the convex `g`,
    hence monotone (`ConvexOn.secant_mono`). -/
theorem h_monotoneOn_Ioc {x b : ℝ} (hx0 : 0 < x) (hb0 : 0 ≤ b) (hb : x * b < 1) :
    MonotoneOn (fun u : ℝ => -Real.log (1 - x * u) / u) (Set.Ioc (0 : ℝ) b) := by
  have hconv := convexOn_neg_log_one_sub_mul_Icc hx0 hb
  intro u hu v hv huv
  have h0mem : (0 : ℝ) ∈ Set.Icc (0 : ℝ) b := ⟨le_refl 0, hb0⟩
  have humem : u ∈ Set.Icc (0 : ℝ) b := ⟨hu.1.le, hu.2⟩
  have hvmem : v ∈ Set.Icc (0 : ℝ) b := ⟨hv.1.le, hv.2⟩
  have hsec := hconv.secant_mono h0mem humem hvmem (ne_of_gt hu.1) (ne_of_gt hv.1) huv
  simpa [Real.log_one] using hsec

/-! ### V3 brick 3b — going-up per-cell integral bounds

The going-up generalisations of Part A's `h_continuousOn` / `h_intervalIntegrable`
/ `h_integral_le_right` / `h_integral_ge_left`, on cells `[a,b] ⊆ (0, 1/x)`
(hypothesis `x·b < 1` in place of `b ≤ 1`).  With `h` monotone increasing
(`h_monotoneOn_Ioc`), the per-cell integral is squeezed between the left/right
endpoint values. -/

/-- Continuity of `h(u) = −log(1 − x u)/u` on `[a,b] ⊆ (0, 1/x)` (`x·b < 1`). -/
theorem h_continuousOn_Icc {x a b : ℝ} (hx0 : 0 < x) (ha : 0 < a) (hb : x * b < 1) :
    ContinuousOn (fun u => -Real.log (1 - x * u) / u) (Set.Icc a b) := by
  have hnum : ContinuousOn (fun u : ℝ => -Real.log (1 - x * u)) (Set.Icc a b) := by
    refine ContinuousOn.neg (ContinuousOn.log
      ((by fun_prop : Continuous (fun u : ℝ => 1 - x * u)).continuousOn) (fun u hu => ?_))
    have hxu : x * u ≤ x * b := mul_le_mul_of_nonneg_left hu.2 hx0.le
    exact ne_of_gt (by linarith)
  exact hnum.div continuousOn_id (fun u hu => ne_of_gt (lt_of_lt_of_le ha hu.1))

/-- `h` is interval-integrable on any `[a,b] ⊆ (0, 1/x)` (`x·b < 1`). -/
theorem h_intervalIntegrable_Icc {x a b : ℝ} (hx0 : 0 < x) (ha : 0 < a) (hb : x * b < 1)
    (hab : a ≤ b) :
    IntervalIntegrable (fun u => -Real.log (1 - x * u) / u) volume a b := by
  apply ContinuousOn.intervalIntegrable
  rw [Set.uIcc_of_le hab]
  exact h_continuousOn_Icc hx0 ha hb

/-- **Upper cell bound.**  `∫_a^b h ≤ h(b)·(b−a)` on `[a,b] ⊆ (0, 1/x)`
    (`h` increasing ⇒ `h(b)` is the max). -/
theorem h_integral_le_right_Icc {x a b : ℝ} (hx0 : 0 < x) (ha : 0 < a) (hb : x * b < 1)
    (hab : a ≤ b) :
    (∫ u in a..b, -Real.log (1 - x * u) / u) ≤ (-Real.log (1 - x * b) / b) * (b - a) := by
  have hb0 : 0 < b := lt_of_lt_of_le ha hab
  have hbmem : b ∈ Set.Ioc (0 : ℝ) b := ⟨hb0, le_refl b⟩
  calc (∫ u in a..b, -Real.log (1 - x * u) / u)
      ≤ ∫ _ in a..b, (-Real.log (1 - x * b) / b) := by
        refine integral_mono_on hab (h_intervalIntegrable_Icc hx0 ha hb hab)
          intervalIntegrable_const (fun u hu => ?_)
        exact h_monotoneOn_Ioc hx0 hb0.le hb ⟨lt_of_lt_of_le ha hu.1, hu.2⟩ hbmem hu.2
    _ = (-Real.log (1 - x * b) / b) * (b - a) := by
        rw [intervalIntegral.integral_const, smul_eq_mul]; ring

/-- **Lower cell bound.**  `h(a)·(b−a) ≤ ∫_a^b h` on `[a,b] ⊆ (0, 1/x)`
    (`h` increasing ⇒ `h(a)` is the min). -/
theorem h_integral_ge_left_Icc {x a b : ℝ} (hx0 : 0 < x) (ha : 0 < a) (hb : x * b < 1)
    (hab : a ≤ b) :
    (-Real.log (1 - x * a) / a) * (b - a) ≤ ∫ u in a..b, -Real.log (1 - x * u) / u := by
  have hb0 : 0 < b := lt_of_lt_of_le ha hab
  have hamem : a ∈ Set.Ioc (0 : ℝ) b := ⟨ha, hab⟩
  calc (-Real.log (1 - x * a) / a) * (b - a)
      = ∫ _ in a..b, (-Real.log (1 - x * a) / a) := by
        rw [intervalIntegral.integral_const, smul_eq_mul]; ring
    _ ≤ ∫ u in a..b, -Real.log (1 - x * u) / u := by
        refine integral_mono_on hab intervalIntegrable_const
          (h_intervalIntegrable_Icc hx0 ha hb hab) (fun u hu => ?_)
        exact h_monotoneOn_Ioc hx0 hb0.le hb hamem ⟨lt_of_lt_of_le ha hu.1, hu.2⟩ hu.1

end QOU.Archimedean
