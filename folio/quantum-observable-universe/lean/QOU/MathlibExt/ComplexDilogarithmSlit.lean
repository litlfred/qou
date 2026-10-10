import QOU.MathlibExt.ComplexDilogarithm

/-!
# `cLiTwoExt` on all of `ℂ ∖ [1,∞)`, and its derivative along rays

Bean `qou-clx8`. That bean records two things this file acts on.

**First**, the side condition in the existing bricks is *sufficient but not
necessary*:

> `intervalIntegrable_log_one_sub_div` requires `Re(1 − yz) > 0` on `[0,1]`,
> i.e. `Re(1 − y) > 0`. That **fails** at e.g. `y = 1.5 + 0.3i` and
> `y = 3 + 0.001i` **while the identity still holds**. Do not formalize
> `Re(1−y) > 0` as if it were the real hypothesis — it needlessly excludes most
> of `ℂ ∖ [1,∞)`.

and it names the hypothesis that *is* right:

> For `Im y ≠ 0`, the segment `{1 − yz : z ∈ [0,1]}` meets the real axis **only**
> at `z = 0`, because `Im(1 − yz) = −z·Im y` vanishes on `[0,1]` only at `z = 0`.

`mem_slitPlane_one_sub_mul` below is that, and it covers **all** of `ℂ ∖ [1,∞)`
in one statement: `y.im ≠ 0 ∨ y.re < 1` is exactly the complement of the cut,
since `[1,∞) ⊆ ℂ` is `{y : y.im = 0 ∧ 1 ≤ y.re}`. The two cases are disjointly
easy — off the real axis the imaginary part does it, on the real axis below `1`
the real part does. `ComplexDilogarithm.intervalIntegrable_log_one_sub_div` has
been generalised to take `slitPlane` membership directly, with the old
right-half-plane form kept as a corollary.

Consequence: `cLiTwoExt y` is given by a genuinely convergent integral for every
`y` off the cut — including `‖y₁‖ = 1.52`, the 5₂ root the *series* cannot reach,
which is the identification `qou-0yqu` lists as missing.

**Second**, the bean's remaining obstruction is analyticity in `y`, and both
routes it lists go through *differentiation under the integral sign*, which it
calls "not a Mathlib one-liner". This file takes a third route for the radial
direction, where the parameter can be moved into the **limit of integration**
instead of the integrand:

    cLiTwoExt (t·y) = −∫₀ᵗ log(1 − y·u)/u du        (`cLiTwoExt_ofReal_mul`)

by the substitution `u = t·z` — Mathlib's `integral_comp_mul_left`. Once the
parameter is a limit, the derivative is the **fundamental theorem of calculus**,
not differentiation under an integral:

    d/dt cLiTwoExt (t·y) = −log(1 − y·t)/t          (`hasDerivAt_cLiTwoExt_radial`)

which is `d/dw Li₂(w) = −log(1−w)/w` restricted to the ray through `y`, since the
chain rule reads `cLiTwoExt'(ty)·y = −log(1−ty)/t`.

## What this does and does not settle

It gives the derivative **along rays from the origin**. Full analyticity on
`ℂ ∖ [1,∞)` needs the derivative in every direction, and that is still open — a
primitive-of-a-holomorphic-function argument on the simply-connected slit plane
is the natural next route, and it is not written here. So "the analytic
continuation" remains a name plus agreement-on-the-disc plus this radial
derivative, not yet a theorem.

`qou-clx8` is also explicit that closing it does **not** move the sum rule: Route
5 is a restatement, and even the whole chain leaves an unevaluated real integral.
This file is taken for the Mathlib gap, as that bean instructs.

**The 5₂ sum rule is PROVED**: `QOU.QBeta.FiveTwoComplexPentagon.fiveTwo_saddle_sum_rule`
and `fiveTwoSaddleSumRule_holds`, sorry-free, standard axioms.
-/

namespace QOU.MathlibExt

open Complex MeasureTheory intervalIntegral

/-! ### The sharp domain -/

/-- **`1 − y·z` stays in the slit plane for every `y` off the cut `[1,∞)`.**

`y.im ≠ 0 ∨ y.re < 1` *is* `ℂ ∖ [1,∞)`, since the cut is `{y : y.im = 0 ∧ 1 ≤ y.re}`.

Off the real axis the imaginary part does the work — `Im(1 − yz) = −z·(Im y)`,
which is non-zero for `z > 0`, and at `z = 0` the point is `1`. On the real axis
below `1` the real part does it: `Re(1 − yz) = 1 − z·(Re y) ≥ 1 − max(Re y, 0) > 0`
for `z ∈ [0,1]`. -/
theorem mem_slitPlane_one_sub_mul {y : ℂ} (hy : y.im ≠ 0 ∨ y.re < 1)
    {z : ℝ} (hz0 : 0 ≤ z) (hz1 : z ≤ 1) : 1 - y * (z : ℂ) ∈ slitPlane := by
  have hre : (1 - y * (z : ℂ)).re = 1 - z * y.re := by simp; ring
  have him : (1 - y * (z : ℂ)).im = -(z * y.im) := by simp; ring
  rcases hy with him0 | hre1
  · -- off the real axis: only `z = 0` can put us on the axis, and that point is `1`
    rcases eq_or_lt_of_le hz0 with rfl | hzpos
    · exact mem_slitPlane_iff.2 (Or.inl (by simp))
    · refine mem_slitPlane_iff.2 (Or.inr ?_)
      rw [him]
      exact neg_ne_zero.mpr (mul_ne_zero (ne_of_gt hzpos) him0)
  · -- on or off the axis, `Re y < 1` keeps the real part positive on `[0,1]`
    refine mem_slitPlane_iff.2 (Or.inl ?_)
    rw [hre]
    rcases le_or_gt y.re 0 with h | h
    · nlinarith
    · nlinarith

/-- **The integrand is interval-integrable for every `y` off the cut.**

This is the statement `qou-clx8` asks for: the integral defining `cLiTwoExt`
converges on all of `ℂ ∖ [1,∞)`, *regardless of `‖y‖`* — unlike the series. -/
theorem intervalIntegrable_log_one_sub_div_of_notCut {y : ℂ}
    (hy : y.im ≠ 0 ∨ y.re < 1) :
    IntervalIntegrable (fun z : ℝ => Complex.log (1 - y * (z : ℂ)) / (z : ℂ))
      MeasureTheory.volume 0 1 :=
  intervalIntegrable_log_one_sub_div_of_slitPlane
    (fun _ h0 h1 => mem_slitPlane_one_sub_mul hy h0 h1)

/-! ### Moving the parameter from the integrand to the limit -/

/-- The `cLiTwoExt` integrand as a function of the integration variable alone. -/
noncomputable def liTwoKernel (y : ℂ) (u : ℝ) : ℂ :=
  Complex.log (1 - y * (u : ℂ)) / (u : ℂ)

/-- **The substitution `u = t·z`.**

`cLiTwoExt (t·y) = −∫₀ᵗ log(1 − y·u)/u du` for real `t ≠ 0`. This is the whole
point of the file: on the left the parameter sits *inside* the integrand, on the
right it is a **limit of integration**, where the fundamental theorem of calculus
reaches it. -/
theorem cLiTwoExt_ofReal_mul {y : ℂ} {t : ℝ} (ht : t ≠ 0) :
    cLiTwoExt ((t : ℂ) * y) = -∫ u in (0 : ℝ)..t, liTwoKernel y u := by
  have hpt : ∀ z : ℝ, Complex.log (1 - (t : ℂ) * y * (z : ℂ)) / (z : ℂ)
      = (t : ℝ) • liTwoKernel y (t * z) := by
    intro z
    rcases eq_or_ne z 0 with rfl | hz
    · simp [liTwoKernel]
    · have hz' : ((z : ℝ) : ℂ) ≠ 0 := Complex.ofReal_ne_zero.mpr hz
      have ht' : ((t : ℝ) : ℂ) ≠ 0 := Complex.ofReal_ne_zero.mpr ht
      simp only [liTwoKernel, Complex.ofReal_mul, Complex.real_smul]
      rw [show (1 : ℂ) - y * ((t : ℂ) * (z : ℂ)) = 1 - (t : ℂ) * y * (z : ℂ) by ring]
      field_simp
  unfold cLiTwoExt
  rw [intervalIntegral.integral_congr (g := fun z : ℝ => (t : ℝ) • liTwoKernel y (t * z))
      (fun z _ => hpt z)]
  rw [intervalIntegral.integral_smul, intervalIntegral.integral_comp_mul_left _ ht]
  rw [smul_smul, mul_inv_cancel₀ ht, one_smul, mul_zero, mul_one]

/-! ### The derivative along a ray, by the fundamental theorem of calculus -/

/-- The kernel is continuous at every `t ≠ 0` off the cut. -/
theorem continuousAt_liTwoKernel {y : ℂ} {t : ℝ} (ht : t ≠ 0)
    (hslit : 1 - y * (t : ℂ) ∈ slitPlane) : ContinuousAt (liTwoKernel y) t := by
  have hbase : ContinuousAt (fun u : ℝ => 1 - y * (u : ℂ)) t :=
    (continuous_const.sub (continuous_const.mul Complex.continuous_ofReal)).continuousAt
  exact (hbase.clog hslit).div
    Complex.continuous_ofReal.continuousAt (Complex.ofReal_ne_zero.mpr ht)

/-- **`d/dt cLiTwoExt (t·y) = −log(1 − y·t)/t`.**

The radial derivative of the dilogarithm, by the fundamental theorem of calculus
rather than by differentiating under an integral sign. Reading it through the
chain rule, `cLiTwoExt'(ty)·y = −log(1−ty)/t`, i.e. `d/dw Li₂(w) = −log(1−w)/w`
along the ray through `y`.

Hypotheses: `t ∈ (0,1]` and `y` off the cut. The interval `[0,t]` is inside
`[0,1]`, where `mem_slitPlane_one_sub_mul` keeps the path off the branch cut. -/
theorem hasDerivAt_cLiTwoExt_radial {y : ℂ} {t : ℝ}
    (hy : y.im ≠ 0 ∨ y.re < 1) (ht0 : 0 < t) (ht1 : t ≤ 1) :
    HasDerivAt (fun s : ℝ => cLiTwoExt ((s : ℂ) * y))
      (-(Complex.log (1 - y * (t : ℂ)) / (t : ℂ))) t := by
  have htne : t ≠ 0 := ne_of_gt ht0
  -- the kernel is integrable on `[0,t]` …
  have hint : IntervalIntegrable (liTwoKernel y) MeasureTheory.volume 0 t := by
    have h1 : IntervalIntegrable (liTwoKernel y) MeasureTheory.volume 0 1 :=
      intervalIntegrable_log_one_sub_div_of_notCut hy
    exact h1.mono_set (by
      rw [Set.uIcc_of_le ht0.le, Set.uIcc_of_le (by norm_num : (0:ℝ) ≤ 1)]
      exact Set.Icc_subset_Icc le_rfl ht1)
  -- … and continuous at `t`
  have hcont : ContinuousAt (liTwoKernel y) t :=
    continuousAt_liTwoKernel htne (mem_slitPlane_one_sub_mul hy ht0.le ht1)
  -- measurability near `t`: the kernel is continuous on the open set where it is
  -- defined at all — off `0` and off the branch cut
  have hUopen : IsOpen ({u : ℝ | u ≠ 0} ∩ (fun u : ℝ => 1 - y * (u : ℂ)) ⁻¹' slitPlane) :=
    isOpen_ne.inter (Complex.isOpen_slitPlane.preimage
      (continuous_const.sub (continuous_const.mul Complex.continuous_ofReal)))
  have htU : t ∈ ({u : ℝ | u ≠ 0} ∩ (fun u : ℝ => 1 - y * (u : ℂ)) ⁻¹' slitPlane) :=
    ⟨htne, mem_slitPlane_one_sub_mul hy ht0.le ht1⟩
  have hUcont : ContinuousOn (liTwoKernel y)
      ({u : ℝ | u ≠ 0} ∩ (fun u : ℝ => 1 - y * (u : ℂ)) ⁻¹' slitPlane) :=
    fun u hu => (continuousAt_liTwoKernel hu.1 hu.2).continuousWithinAt
  have hmeas : StronglyMeasurableAtFilter (liTwoKernel y) (nhds t) :=
    hUcont.stronglyMeasurableAtFilter hUopen t htU
  -- FTC-1 on the primitive, then transport across the substitution
  have hftc : HasDerivAt (fun u : ℝ => ∫ x in (0 : ℝ)..u, liTwoKernel y x)
      (liTwoKernel y t) t := intervalIntegral.integral_hasDerivAt_right hint hmeas hcont
  have := hftc.neg
  refine this.congr_of_eventuallyEq ?_
  filter_upwards [eventually_ne_nhds htne] with s hs
  exact (cLiTwoExt_ofReal_mul (y := y) hs)

end QOU.MathlibExt
