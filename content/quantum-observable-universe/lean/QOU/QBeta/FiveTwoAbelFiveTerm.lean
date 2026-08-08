import QOU.QBeta.FiveTwoRogersReflection
import QOU.QBeta.FiveTwoFiveTermArguments

/-!
# Abel's five-term relation for the Rogers dilogarithm on `(0,1)`

Bean `qou-abel` — the twelfth and last hypothesis of
`FiveTwoLevelSevenLadder.numerators_original_form`, and the one input
`FiveTwoFiveTermArguments.numerators_of_abel` still takes on faith.

    L x + L y - L (x·y) - L (x(1-y)/(1-x·y)) - L (y(1-x)/(1-x·y)) = 0

for `x, y ∈ (0,1)`.

## Shape of the proof

The same shape `QOU/Archimedean/DilogReflection.lean` uses for
`LiTwo_reflection'`: fix `y`, show the left-hand side has vanishing derivative in
`x` on `(0,1)`, hence is constant there, then evaluate the constant by letting
`x → 0⁺`, where three of the five terms go to `0` and the other two cancel.

## Why the derivative vanishes — the cancellation is linear

Write `A = log x`, `B = log (1-x)`, `C = log y`, `D = log (1-y)`, `E = log (1-xy)`.
The two inner arguments satisfy

    1 - x(1-y)/(1-xy) = (1-x)/(1-xy)        1 - y(1-x)/(1-xy) = (1-y)/(1-xy)

so every log appearing after the chain rule splits into `A,…,E` — this is
`log_inner_left`, `log_inner_right` and friends below. Once it does, `-2·F'(x)`
is a *linear* form in `A,…,E` with rational-function coefficients, and each of
the five coefficients vanishes identically. For instance the `A` coefficient is

    1/(1-x) - y/(1-xy) - (1-y)/((1-x)(1-xy))
      = [(1-xy) - y(1-x) - (1-y)] / ((1-x)(1-xy)) = 0,

and the other four go the same way. That is why the final step is `field_simp`
and `ring` rather than an argument: **all the content is in the log splittings**,
which is where the positivity side conditions live and where a wrong branch would
hide.

## Status

**This closes `qou-abel`.** With it, `numerators_of_abel` becomes unconditional
for the corpus's `rogersL` given only reflection, which
`FiveTwoRogersReflection.rogersL_reflection` already proves.

It does **not** close the 5₂ sum rule. The transport `x = 1 → x = -1` is still
unformalized (`qou-trns`), and `extend` is still not identified with the analytic
continuation in Lean (`qou-rstq` item 4 — closed on paper by Route 15, not in
Lean). **The 5₂ sum rule remains verified to 80 dps, unproved.**
-/

namespace QOU.QBeta.FiveTwoAbelFiveTerm

open QOU.QPochhammer QOU.Archimedean QOU.QBeta.FiveTwoRogersReflection
open Filter Topology

variable {x y : ℝ}

/-! ### The two inner arguments, and that they stay in `(0,1)` -/

/-- `1 - x·y > 0` on the square — the denominator every inner argument shares. -/
theorem one_sub_mul_pos (hx0 : 0 < x) (hx1 : x < 1) (_hy0 : 0 < y) (hy1 : y < 1) :
    0 < 1 - x * y := by nlinarith

/-- The left inner argument's complement: `1 - x(1-y)/(1-xy) = (1-x)/(1-xy)`. -/
theorem one_sub_inner_left (hd : 1 - x * y ≠ 0) :
    1 - x * (1 - y) / (1 - x * y) = (1 - x) / (1 - x * y) := by
  field_simp
  ring

/-- The right inner argument's complement: `1 - y(1-x)/(1-xy) = (1-y)/(1-xy)`. -/
theorem one_sub_inner_right (hd : 1 - x * y ≠ 0) :
    1 - y * (1 - x) / (1 - x * y) = (1 - y) / (1 - x * y) := by
  have hd' : 1 - y * x ≠ 0 := by rwa [mul_comm]
  field_simp
  ring

theorem inner_left_pos (hx0 : 0 < x) (hx1 : x < 1) (hy0 : 0 < y) (hy1 : y < 1) :
    0 < x * (1 - y) / (1 - x * y) :=
  div_pos (by nlinarith) (one_sub_mul_pos hx0 hx1 hy0 hy1)

theorem inner_left_lt_one (hx0 : 0 < x) (hx1 : x < 1) (hy0 : 0 < y) (hy1 : y < 1) :
    x * (1 - y) / (1 - x * y) < 1 := by
  have hd := one_sub_mul_pos hx0 hx1 hy0 hy1
  have h := one_sub_inner_left (x := x) (y := y) (ne_of_gt hd)
  have : 0 < (1 - x) / (1 - x * y) := div_pos (by linarith) hd
  linarith

theorem inner_right_pos (hx0 : 0 < x) (hx1 : x < 1) (hy0 : 0 < y) (hy1 : y < 1) :
    0 < y * (1 - x) / (1 - x * y) :=
  div_pos (by nlinarith) (one_sub_mul_pos hx0 hx1 hy0 hy1)

theorem inner_right_lt_one (hx0 : 0 < x) (hx1 : x < 1) (hy0 : 0 < y) (hy1 : y < 1) :
    y * (1 - x) / (1 - x * y) < 1 := by
  have hd := one_sub_mul_pos hx0 hx1 hy0 hy1
  have h := one_sub_inner_right (x := x) (y := y) (ne_of_gt hd)
  have : 0 < (1 - y) / (1 - x * y) := div_pos (by linarith) hd
  linarith

/-! ### The log splittings

Everything the chain rule produces is a `log` of a product or quotient of
`x, 1-x, y, 1-y, 1-xy`. These are the splittings, and they are where the
positivity hypotheses are actually used. -/

theorem log_inner_left (hx0 : 0 < x) (hx1 : x < 1) (hy0 : 0 < y) (hy1 : y < 1) :
    Real.log (x * (1 - y) / (1 - x * y))
      = Real.log x + Real.log (1 - y) - Real.log (1 - x * y) := by
  have hd := one_sub_mul_pos hx0 hx1 hy0 hy1
  rw [Real.log_div (ne_of_gt (mul_pos hx0 (by linarith))) (ne_of_gt hd),
    Real.log_mul (ne_of_gt hx0) (by linarith)]

theorem log_one_sub_inner_left (hx0 : 0 < x) (hx1 : x < 1) (hy0 : 0 < y) (hy1 : y < 1) :
    Real.log (1 - x * (1 - y) / (1 - x * y))
      = Real.log (1 - x) - Real.log (1 - x * y) := by
  have hd := one_sub_mul_pos hx0 hx1 hy0 hy1
  rw [one_sub_inner_left (ne_of_gt hd), Real.log_div (by linarith) (ne_of_gt hd)]

theorem log_inner_right (hx0 : 0 < x) (hx1 : x < 1) (hy0 : 0 < y) (hy1 : y < 1) :
    Real.log (y * (1 - x) / (1 - x * y))
      = Real.log y + Real.log (1 - x) - Real.log (1 - x * y) := by
  have hd := one_sub_mul_pos hx0 hx1 hy0 hy1
  rw [Real.log_div (ne_of_gt (mul_pos hy0 (by linarith))) (ne_of_gt hd),
    Real.log_mul (ne_of_gt hy0) (by linarith)]

theorem log_one_sub_inner_right (hx0 : 0 < x) (hx1 : x < 1) (hy0 : 0 < y) (hy1 : y < 1) :
    Real.log (1 - y * (1 - x) / (1 - x * y))
      = Real.log (1 - y) - Real.log (1 - x * y) := by
  have hd := one_sub_mul_pos hx0 hx1 hy0 hy1
  rw [one_sub_inner_right (ne_of_gt hd), Real.log_div (by linarith) (ne_of_gt hd)]

/-! ### Derivatives of the two inner arguments -/

theorem hasDerivAt_inner_left (hd : 1 - x * y ≠ 0) :
    HasDerivAt (fun t : ℝ => t * (1 - y) / (1 - t * y)) ((1 - y) / (1 - x * y) ^ 2) x := by
  have hn : HasDerivAt (fun t : ℝ => t * (1 - y)) (1 - y) x := by
    simpa using (hasDerivAt_id x).mul_const (1 - y)
  have hdd : HasDerivAt (fun t : ℝ => 1 - t * y) (-y) x := by
    simpa using ((hasDerivAt_id x).mul_const y).const_sub 1
  have h := hn.div hdd hd
  convert h using 1
  field_simp
  ring

theorem hasDerivAt_inner_right (hd : 1 - x * y ≠ 0) :
    HasDerivAt (fun t : ℝ => y * (1 - t) / (1 - t * y))
      (y * (y - 1) / (1 - x * y) ^ 2) x := by
  have hn : HasDerivAt (fun t : ℝ => y * (1 - t)) (-y) x := by
    simpa using ((hasDerivAt_id x).const_sub 1).const_mul y
  have hdd : HasDerivAt (fun t : ℝ => 1 - t * y) (-y) x := by
    simpa using ((hasDerivAt_id x).mul_const y).const_sub 1
  have h := hn.div hdd hd
  convert h using 1
  field_simp
  ring

/-! ### The auxiliary function and its vanishing derivative -/

/-- The five-term expression, as a function of `x` with `y` held fixed. -/
noncomputable def abelAux (y : ℝ) : ℝ → ℝ := fun t =>
  rogersL t + rogersL y - rogersL (t * y)
    - rogersL (t * (1 - y) / (1 - t * y)) - rogersL (y * (1 - t) / (1 - t * y))

/-- **The derivative vanishes.** Every `log` the chain rule produces splits into
`log x, log (1-x), log y, log (1-y), log (1-xy)`; after that the whole expression
is a linear form in those five with rational coefficients, and each coefficient
is identically zero. -/
theorem hasDerivAt_abelAux (hx0 : 0 < x) (hx1 : x < 1) (hy0 : 0 < y) (hy1 : y < 1) :
    HasDerivAt (abelAux y) 0 x := by
  have hd : 0 < 1 - x * y := one_sub_mul_pos hx0 hx1 hy0 hy1
  have hdne : 1 - x * y ≠ 0 := ne_of_gt hd
  have hxy0 : 0 < x * y := mul_pos hx0 hy0
  have hxy1 : x * y < 1 := by nlinarith
  have hl0 := inner_left_pos hx0 hx1 hy0 hy1
  have hl1 := inner_left_lt_one hx0 hx1 hy0 hy1
  have hr0 := inner_right_pos hx0 hx1 hy0 hy1
  have hr1 := inner_right_lt_one hx0 hx1 hy0 hy1
  -- the five pieces
  have t1 := hasDerivAt_rogersL hx0 hx1
  have t2 : HasDerivAt (fun _ : ℝ => rogersL y) 0 x := hasDerivAt_const x _
  have t3 := (hasDerivAt_rogersL hxy0 hxy1).comp x ((hasDerivAt_id x).mul_const y)
  have t4 := (hasDerivAt_rogersL hl0 hl1).comp x (hasDerivAt_inner_left hdne)
  have t5 := (hasDerivAt_rogersL hr0 hr1).comp x (hasDerivAt_inner_right hdne)
  simp only [Function.comp_def, one_mul] at t3 t4 t5
  have h := (((t1.add t2).sub t3).sub t4).sub t5
  refine h.congr_deriv ?_
  -- split every log, and rewrite the two complements
  rw [log_inner_left hx0 hx1 hy0 hy1, log_one_sub_inner_left hx0 hx1 hy0 hy1,
    log_inner_right hx0 hx1 hy0 hy1, log_one_sub_inner_right hx0 hx1 hy0 hy1,
    one_sub_inner_left hdne, one_sub_inner_right hdne,
    Real.log_mul (ne_of_gt hx0) (ne_of_gt hy0)]
  have hx1' : (1 : ℝ) - x ≠ 0 := by linarith
  have hy1' : (1 : ℝ) - y ≠ 0 := by linarith
  field_simp
  ring

/-! ### Constancy on `(0,1)` -/

theorem abelAux_eq (hy0 : 0 < y) (hy1 : y < 1) {a b : ℝ}
    (ha : a ∈ Set.Ioo (0 : ℝ) 1) (hb : b ∈ Set.Ioo (0 : ℝ) 1) :
    abelAux y a = abelAux y b := by
  refine IsOpen.is_const_of_deriv_eq_zero isOpen_Ioo isPreconnected_Ioo ?_ ?_ ha hb
  · intro z hz
    exact (hasDerivAt_abelAux hz.1 hz.2 hy0 hy1).differentiableAt.differentiableWithinAt
  · intro z hz
    exact (hasDerivAt_abelAux hz.1 hz.2 hy0 hy1).deriv

/-! ### The boundary value at `x → 0⁺`

Three of the five terms go to `0` and the remaining two, `rogersL y` and
`rogersL (y(1-x)/(1-xy)) → rogersL y`, cancel. -/

theorem mem_Ioo_nhdsWithin : Set.Ioo (0 : ℝ) 1 ∈ 𝓝[>] (0 : ℝ) := by
  have := inter_mem_nhdsWithin (Set.Ioi (0 : ℝ))
    (Iio_mem_nhds (show (0 : ℝ) < 1 by norm_num))
  rwa [Set.Ioi_inter_Iio] at this

/-- `log x · log (1-x) → 0` as `x → 0⁺`. The corpus proves this at `x → 1⁻`; the
expression is invariant under `x ↦ 1 - x`, so it transports. -/
theorem tendsto_log_mul_log_one_sub_zero :
    Tendsto (fun x : ℝ => Real.log x * Real.log (1 - x)) (𝓝[>] (0 : ℝ)) (𝓝 0) := by
  have htend : Tendsto (fun x : ℝ => 1 - x) (𝓝[>] (0 : ℝ)) (𝓝[<] (1 : ℝ)) := by
    apply tendsto_nhdsWithin_of_tendsto_nhds_of_eventually_within
    · have hcont : Continuous (fun x : ℝ => 1 - x) := continuous_const.sub continuous_id
      simpa using (hcont.tendsto (0 : ℝ)).mono_left nhdsWithin_le_nhds
    · filter_upwards [self_mem_nhdsWithin] with x hx
      simp only [Set.mem_Iio]
      have : (0 : ℝ) < x := hx
      linarith
  have h := tendsto_log_mul_log_one_sub_nhdsWithin_lt_one.comp htend
  refine h.congr (fun x => ?_)
  simp only [Function.comp_apply, sub_sub_cancel]
  ring

theorem tendsto_rogersL_zero : Tendsto rogersL (𝓝[>] (0 : ℝ)) (𝓝 0) := by
  have h1 : Tendsto LiTwo (𝓝[>] (0 : ℝ)) (𝓝 0) :=
    tendsto_LiTwo_nhds_zero.mono_left nhdsWithin_le_nhds
  have h2 := tendsto_log_mul_log_one_sub_zero.div_const 2
  simpa [rogersL] using h1.add (by simpa using h2)

/-- An inner argument that vanishes at `0⁺` and stays positive there. -/
theorem tendsto_rogersL_comp_zero {g : ℝ → ℝ}
    (hg : Tendsto g (𝓝[>] (0 : ℝ)) (𝓝[>] (0 : ℝ))) :
    Tendsto (fun t => rogersL (g t)) (𝓝[>] (0 : ℝ)) (𝓝 0) :=
  tendsto_rogersL_zero.comp hg

theorem tendsto_mul_const_zero (hy0 : 0 < y) :
    Tendsto (fun t : ℝ => t * y) (𝓝[>] (0 : ℝ)) (𝓝[>] (0 : ℝ)) := by
  apply tendsto_nhdsWithin_of_tendsto_nhds_of_eventually_within
  · have : Continuous (fun t : ℝ => t * y) := continuous_id.mul continuous_const
    simpa using (this.tendsto (0 : ℝ)).mono_left nhdsWithin_le_nhds
  · filter_upwards [self_mem_nhdsWithin] with t ht
    exact mul_pos ht hy0

theorem tendsto_inner_left_zero (hy0 : 0 < y) (hy1 : y < 1) :
    Tendsto (fun t : ℝ => t * (1 - y) / (1 - t * y)) (𝓝[>] (0 : ℝ)) (𝓝[>] (0 : ℝ)) := by
  apply tendsto_nhdsWithin_of_tendsto_nhds_of_eventually_within
  · have hc : ContinuousAt (fun t : ℝ => t * (1 - y) / (1 - t * y)) 0 := by
      apply ContinuousAt.div
      · exact (continuous_id.mul continuous_const).continuousAt
      · exact (continuous_const.sub (continuous_id.mul continuous_const)).continuousAt
      · norm_num
    simpa using hc.tendsto.mono_left nhdsWithin_le_nhds
  · filter_upwards [mem_Ioo_nhdsWithin] with t ht
    exact inner_left_pos ht.1 ht.2 hy0 hy1

theorem tendsto_inner_right_zero (_hy0 : 0 < y) :
    Tendsto (fun t : ℝ => y * (1 - t) / (1 - t * y)) (𝓝[>] (0 : ℝ)) (𝓝 y) := by
  have hc : ContinuousAt (fun t : ℝ => y * (1 - t) / (1 - t * y)) 0 := by
    apply ContinuousAt.div
    · exact (continuous_const.mul (continuous_const.sub continuous_id)).continuousAt
    · exact (continuous_const.sub (continuous_id.mul continuous_const)).continuousAt
    · norm_num
  have := hc.tendsto.mono_left (nhdsWithin_le_nhds (s := Set.Ioi (0 : ℝ)))
  simpa using this

theorem tendsto_abelAux_zero (hy0 : 0 < y) (hy1 : y < 1) :
    Tendsto (abelAux y) (𝓝[>] (0 : ℝ)) (𝓝 0) := by
  have h1 := tendsto_rogersL_zero
  have h2 : Tendsto (fun _ : ℝ => rogersL y) (𝓝[>] (0 : ℝ)) (𝓝 (rogersL y)) :=
    tendsto_const_nhds
  have h3 := tendsto_rogersL_comp_zero (tendsto_mul_const_zero (y := y) hy0)
  have h4 := tendsto_rogersL_comp_zero (tendsto_inner_left_zero hy0 hy1)
  have h5 := ((hasDerivAt_rogersL hy0 hy1).continuousAt.tendsto).comp
    (tendsto_inner_right_zero (y := y) hy0)
  simp only [Function.comp_def] at h5
  have := (((h1.add h2).sub h3).sub h4).sub h5
  simpa [abelAux] using this

/-! ### Abel's five-term relation -/

/-- **Abel's five-term relation** for the Rogers dilogarithm on `(0,1)`.

    L x + L y - L (x·y) - L (x(1-y)/(1-x·y)) - L (y(1-x)/(1-x·y)) = 0

`L` here is `FiveTwoRogersReflection.rogersL`, built from the corpus's own
`LiTwo`. This is the last hypothesis
`FiveTwoFiveTermArguments.numerators_of_abel` takes. -/
theorem rogersL_fiveTerm (hx0 : 0 < x) (hx1 : x < 1) (hy0 : 0 < y) (hy1 : y < 1) :
    rogersL x + rogersL y - rogersL (x * y)
      - rogersL (x * (1 - y) / (1 - x * y))
      - rogersL (y * (1 - x) / (1 - x * y)) = 0 := by
  have hconst : Tendsto (abelAux y) (𝓝[>] (0 : ℝ)) (𝓝 (abelAux y x)) := by
    refine tendsto_const_nhds.congr' ?_
    filter_upwards [mem_Ioo_nhdsWithin] with t ht
      using (abelAux_eq hy0 hy1 ht ⟨hx0, hx1⟩).symm
  have h := tendsto_nhds_unique hconst (tendsto_abelAux_zero hy0 hy1)
  simpa [abelAux] using h

/-! ### The level-7 numerators, unconditionally

`FiveTwoFiveTermArguments.numerators_of_abel` took Abel's relation and reflection
as hypotheses. Both are now theorems for `rogersL`, so the numerators follow from
nothing but the cubic and a bound on its root.

The bound is the sub-gap `qou-abel` flagged in advance: `1/2 < x` is genuinely
needed, because `s = (1-x)/x < 1` is false without it. -/

theorem root_bounds {x : ℝ} (hlo : 1 / 2 < x) (hhi : x < 1) :
    (0 < 1 / (2 - x) ∧ 1 / (2 - x) < 1) ∧ (0 < x / (x + 1) ∧ x / (x + 1) < 1)
      ∧ (0 < (1 - x) / x ∧ (1 - x) / x < 1) := by
  have hx0 : (0 : ℝ) < x := by linarith
  have h2 : (0 : ℝ) < 2 - x := by linarith
  have h1 : (0 : ℝ) < x + 1 := by linarith
  have h1x : (0 : ℝ) < 1 - x := by linarith
  refine ⟨⟨by positivity, ?_⟩, ⟨by positivity, ?_⟩, ⟨by positivity, ?_⟩⟩
  · rw [div_lt_one h2]; linarith
  · rw [div_lt_one h1]; linarith
  · rw [div_lt_one hx0]; linarith

/-- **The level-7 numerators `(17, 5, -1)`, from the cubic alone.**

No hypothesis about `L` remains: Abel's relation is `rogersL_fiveTerm` and
reflection is `rogersL_one_sub`, both proved. -/
theorem numerators_of_root {x : ℝ} (hx : x ^ 3 - 2 * x ^ 2 - x + 1 = 0)
    (hlo : 1 / 2 < x) (hhi : x < 1) :
    (7 * (2 * (Real.pi ^ 2 / 6) + 2 * rogersL x - rogersL (1 / (2 - x)))
        = 17 * (Real.pi ^ 2 / 6))
      ∧ (7 * (2 * rogersL x - rogersL (x / (x + 1))) = 5 * (Real.pi ^ 2 / 6))
      ∧ (7 * (-(2 * (Real.pi ^ 2 / 6)) + 2 * rogersL x + rogersL ((1 - x) / x))
        = -(Real.pi ^ 2 / 6)) := by
  obtain ⟨⟨hq0, hq1⟩, ⟨hr0, hr1⟩, ⟨hs0, hs1⟩⟩ := root_bounds hlo hhi
  have hx0 : (0 : ℝ) < x := by linarith
  have h2 : (2 : ℝ) - x ≠ 0 := by intro h; linarith [h ▸ (rfl : (2:ℝ) - x = 2 - x)]
  have h2' : (0 : ℝ) < 2 - x := by linarith
  have h1 : (0 : ℝ) < x + 1 := by linarith
  have hxx : (1 : ℝ) - x * x ≠ 0 := by nlinarith
  -- defining relations
  have hq : (1 / (2 - x)) * (2 - x) = 1 := by field_simp
  have hr : (x / (x + 1)) * (x + 1) = x := by field_simp
  have hs : ((1 - x) / x) * x = 1 - x := by field_simp
  -- the four reflection instances
  have hrw := rogersL_one_sub hx0 hhi
  have hrq := rogersL_one_sub hq0 hq1
  have hrr := rogersL_one_sub hr0 hr1
  have hrs := rogersL_one_sub hs0 hs1
  -- the three Abel instances
  have hA := rogersL_fiveTerm hx0 hhi hx0 hhi
  have hB := rogersL_fiveTerm (x := 1 - x) (y := 1 / (2 - x))
    (by linarith) (by linarith) hq0 hq1
  have hC := rogersL_fiveTerm (x := x) (y := (1 - x) / x) hx0 hhi hs0 hs1
  exact FiveTwoFiveTermArguments.numerators_of_abel rogersL (Real.pi ^ 2 / 6)
    hx hq hr hs hxx hrw hrq hrr hrs hA hB hC

/-- The cubic really does have a root in `(1/2, 1)`, so `numerators_of_root` is
not vacuous. `f(1/2) = 1/8 > 0` and `f(1) = -1 < 0`. -/
theorem exists_root_in_Ioo :
    ∃ x : ℝ, x ^ 3 - 2 * x ^ 2 - x + 1 = 0 ∧ 1 / 2 < x ∧ x < 1 := by
  have hcont : ContinuousOn (fun t : ℝ => t ^ 3 - 2 * t ^ 2 - t + 1) (Set.Icc (1 / 2) 1) :=
    (((continuous_pow 3).sub ((continuous_pow 2).const_smul (2 : ℝ))).sub
      continuous_id).add continuous_const |>.continuousOn
  have hmem : (0 : ℝ) ∈ Set.Ioo ((1 : ℝ) ^ 3 - 2 * 1 ^ 2 - 1 + 1)
      ((1 / 2 : ℝ) ^ 3 - 2 * (1 / 2) ^ 2 - 1 / 2 + 1) := by norm_num
  obtain ⟨c, hc, hfc⟩ := intermediate_value_Ioo' (by norm_num : (1 / 2 : ℝ) ≤ 1) hcont hmem
  exact ⟨c, hfc, hc.1, hc.2⟩

end QOU.QBeta.FiveTwoAbelFiveTerm
