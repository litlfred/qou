/-
  The trapezoid rule with its exact error term — bean `qou-mlgp` (A), gap 1.

  THE MATHLIB GAP.  Mathlib has no quadrature at all: grepping the whole library
  for `trapezoid`, `trapezium`, `quadrature` and Simpson's rule returns nothing.
  It has the fundamental theorem of calculus, integration by parts, and
  `Polynomial.bernoulli`, but no rule for approximating an integral by samples
  and no error estimate for one.  This file adds the first such rule.

  WHAT IS HERE.

    integral_weight                  ∫_a^b (x−a)(b−x) dx = (b−a)³/6
    integral_eq_trapezoid_sub        the EXACT error identity
    abs_trapezoid_sub_integral_le    |trapezoid − ∫| ≤ (b−a)³·M/12  for |f″| ≤ M
    hasDerivAt_log_two_sin           (log(2 sin))′ = cos/sin
    hasDerivAt_cos_div_sin           (cos/sin)′ = −1/sin²
    abs_trapezoid_sub_integral_log_two_sin_le    the instance (A) needs

  The identity is

      ∫_a^b f = ((b−a)/2)·(f(a) + f(b)) − ½·∫_a^b (x−a)(b−x)·f″(x) dx

  exact for every `f ∈ C²`, no asymptotics.  It is the Peano-kernel form of the
  trapezoid rule, with kernel `(x−a)(b−x) ≥ 0`, and the `O(h³)` bound follows by
  pulling `sup|f″|` out against `∫ (x−a)(b−x) = (b−a)³/6`.

  THE PROOF IS ONE APPLICATION OF THE FTC, not two integrations by parts.  With
  `w(x) = (x−a)(b−x)` (so `w(a) = w(b) = 0`, `w′ = a+b−2x`, `w″ = −2`), the
  function

      F := w·f′ − w′·f          satisfies      F′ = w·f″ + 2f

  because the two `w′f′` terms cancel.  So `∫ (w f″ + 2f) = F(b) − F(a)`, and
  `F(b) − F(a) = (b−a)·(f(a) + f(b))` since `w` vanishes at both ends.  Rearrange.

  WHY THIS CORPUS WANTS IT.  `QOU/Knot/KashaevReflectionTrapezoid.lean` proves
  that the reflection collapses `ε_k + ε_{N−1−k}` to exactly the trapezoid
  remainder of `log(2 sin)` on one cell `[θ, θ+h]`.  That identity is proved;
  the resulting `O(h²)` BOUND was asserted in its docstring and not proved,
  because nothing in Mathlib bounds a trapezoid remainder.  This file supplies
  the missing half, and `abs_trapezoid_sub_integral_log_two_sin_le` at the end
  applies it: with `f = log(2 sin)`, `f′ = cos/sin`, `f″ = −1/sin²`, the
  symmetric half of `qou-mlgp` (A)'s error is bounded by `(b−a)³·M/12` with
  `M = sup 1/sin²` on the cell — `O(h³)` per cell, hence `O(h²)` against the
  `1/h` of the expansion, one order better than the `O(1/N)` claimed.  That is
  what leaves all of (A)'s remaining difficulty in the antisymmetric half.

  Neither `(log(2 sin))′` nor `(cos/sin)′` is in Mathlib in this form either;
  both are proved here from the chain and quotient rules.

  -- Ref: [leitner2026] QOU/Knot/KashaevReflectionTrapezoid.lean  (what consumes this)
  -- Ref: [leitner2026] computations/probes/kashaev_reflection_probe.py
-/
import Mathlib.MeasureTheory.Integral.IntervalIntegral.IntegrationByParts
import Mathlib.Analysis.Calculus.Deriv.Pow
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Deriv
import Mathlib.Analysis.SpecialFunctions.Log.Deriv

namespace QOU.MathlibExt

open Real MeasureTheory intervalIntegral

/-- `∫_a^b (x−a)(b−x) dx = (b−a)³/6` — the Peano kernel of the trapezoid rule
has total mass `(b−a)³/6`.  This is what turns `sup|f″|` into the `1/12`. -/
theorem integral_weight (a b : ℝ) :
    ∫ x in a..b, (x - a) * (b - x) = (b - a) ^ 3 / 6 := by
  have hG : ∀ x : ℝ, HasDerivAt
      (fun y : ℝ => -(y ^ 3) / 3 + (a + b) * y ^ 2 / 2 - a * b * y)
      ((x - a) * (b - x)) x := by
    intro x
    have h3 : HasDerivAt (fun y : ℝ => y ^ 3) (3 * x ^ 2) x := by
      simpa using (hasDerivAt_id x).pow 3
    have h2 : HasDerivAt (fun y : ℝ => y ^ 2) (2 * x) x := by
      simpa using (hasDerivAt_id x).pow 2
    have h := ((h3.neg.div_const 3).add ((h2.const_mul (a + b)).div_const 2)).sub
      ((hasDerivAt_id x).const_mul (a * b))
    convert h using 1
    ring
  have hcont : Continuous fun x : ℝ => (x - a) * (b - x) := by fun_prop
  rw [integral_eq_sub_of_hasDerivAt (fun x _ => hG x) (hcont.intervalIntegrable a b)]
  ring

/-- **The trapezoid rule with its exact error term.**

    ∫_a^b f = ((b−a)/2)·(f a + f b) − ½·∫_a^b (x−a)(b−x)·f″(x) dx

for any `f` with a second derivative on `[[a,b]]` and `f″` continuous there.
Exact — an identity, not an estimate. -/
theorem integral_eq_trapezoid_sub {f f' f'' : ℝ → ℝ} {a b : ℝ}
    (hf : ∀ x ∈ Set.uIcc a b, HasDerivAt f (f' x) x)
    (hf' : ∀ x ∈ Set.uIcc a b, HasDerivAt f' (f'' x) x)
    (hcont : ContinuousOn f'' (Set.uIcc a b)) :
    ∫ x in a..b, f x
      = (b - a) / 2 * (f a + f b)
        - 1 / 2 * ∫ x in a..b, (x - a) * (b - x) * f'' x := by
  have hfcont : ContinuousOn f (Set.uIcc a b) := fun x hx =>
    (hf x hx).continuousAt.continuousWithinAt
  have hwcont : ContinuousOn (fun x : ℝ => (x - a) * (b - x)) (Set.uIcc a b) := by fun_prop
  -- `F := w·f′ − w′·f` has derivative `w·f″ + 2f`: the two `w′f′` terms cancel.
  have hF : ∀ x ∈ Set.uIcc a b,
      HasDerivAt (fun y : ℝ => (y - a) * (b - y) * f' y - (a + b - 2 * y) * f y)
        ((x - a) * (b - x) * f'' x + 2 * f x) x := by
    intro x hx
    have hxa : HasDerivAt (fun y : ℝ => y - a) 1 x := by
      simpa using (hasDerivAt_id x).sub_const a
    have hbx : HasDerivAt (fun y : ℝ => b - y) (-1) x := by
      simpa using (hasDerivAt_id x).const_sub b
    have hw : HasDerivAt (fun y : ℝ => (y - a) * (b - y)) (a + b - 2 * x) x := by
      have := hxa.mul hbx
      convert this using 1
      ring
    have hw' : HasDerivAt (fun y : ℝ => a + b - 2 * y) (-2) x := by
      have := ((hasDerivAt_id x).const_mul (2:ℝ)).const_sub (a + b)
      convert this using 1
      ring
    have := (hw.mul (hf' x hx)).sub (hw'.mul (hf x hx))
    convert this using 1
    ring
  have hint : IntervalIntegrable
      (fun x => (x - a) * (b - x) * f'' x + 2 * f x) volume a b := by
    refine IntervalIntegrable.add ?_ ?_
    · exact (hwcont.mul hcont).intervalIntegrable
    · exact (continuousOn_const.mul hfcont).intervalIntegrable
  have hftc := integral_eq_sub_of_hasDerivAt hF hint
  rw [integral_add ((hwcont.mul hcont).intervalIntegrable)
    ((continuousOn_const.mul hfcont).intervalIntegrable)] at hftc
  rw [intervalIntegral.integral_const_mul] at hftc
  -- `w` vanishes at both ends, so the boundary term is `(b−a)·(f a + f b)`;
  -- `linear_combination` does that simplification and the rearrangement at once.
  linear_combination hftc / 2

/-- **The trapezoid error bound.**  `|trapezoid − ∫| ≤ (b−a)³·M/12` when
`|f″| ≤ M` on `[a,b]`.

The classical `O(h³)` per-cell estimate — `O(h²)` after summing `1/h` cells —
and the reason a trapezoid rule sees one order more than a rectangle rule. -/
theorem abs_trapezoid_sub_integral_le {f f' f'' : ℝ → ℝ} {a b M : ℝ} (hab : a ≤ b)
    (hf : ∀ x ∈ Set.uIcc a b, HasDerivAt f (f' x) x)
    (hf' : ∀ x ∈ Set.uIcc a b, HasDerivAt f' (f'' x) x)
    (hcont : ContinuousOn f'' (Set.uIcc a b))
    (hM : ∀ x ∈ Set.uIcc a b, |f'' x| ≤ M) :
    |(b - a) / 2 * (f a + f b) - ∫ x in a..b, f x| ≤ (b - a) ^ 3 * M / 12 := by
  have hwcont : ContinuousOn (fun x : ℝ => (x - a) * (b - x)) (Set.uIcc a b) := by fun_prop
  have hkey := integral_eq_trapezoid_sub hf hf' hcont
  have hrw : (b - a) / 2 * (f a + f b) - ∫ x in a..b, f x
      = 1 / 2 * ∫ x in a..b, (x - a) * (b - x) * f'' x := by
    rw [hkey]; ring
  rw [hrw, abs_mul]
  have habs : |∫ x in a..b, (x - a) * (b - x) * f'' x|
      ≤ ∫ x in a..b, |(x - a) * (b - x) * f'' x| :=
    abs_integral_le_integral_abs hab
  -- on `[a,b]` the kernel is nonnegative, so `|w·f″| ≤ M·w`
  have hpt : ∀ x ∈ Set.uIcc a b, |(x - a) * (b - x) * f'' x| ≤ M * ((x - a) * (b - x)) := by
    intro x hx
    rw [Set.uIcc_of_le hab, Set.mem_Icc] at hx
    have hw0 : (0 : ℝ) ≤ (x - a) * (b - x) := by nlinarith [hx.1, hx.2]
    rw [abs_mul, abs_of_nonneg hw0]
    have hMx : |f'' x| ≤ M := hM x (by rw [Set.uIcc_of_le hab, Set.mem_Icc]; exact hx)
    nlinarith [abs_nonneg (f'' x), hw0, hMx]
  have hmono : (∫ x in a..b, |(x - a) * (b - x) * f'' x|)
      ≤ ∫ x in a..b, M * ((x - a) * (b - x)) := by
    refine integral_mono_on hab ?_ ?_ ?_
    · exact ((hwcont.mul hcont).abs).intervalIntegrable
    · exact ((continuousOn_const.mul hwcont)).intervalIntegrable
    · intro x hx
      exact hpt x (by rw [Set.uIcc_of_le hab]; exact hx)
  rw [intervalIntegral.integral_const_mul, integral_weight] at hmono
  have h2 : |(1 : ℝ) / 2| = 1 / 2 := by norm_num
  rw [h2]
  linarith

/-! ### The instance `qou-mlgp` (A) needs: `f = log(2 sin)` on `(0, π)`

`f′ = cot`, `f″ = −1/sin²`.  Both are two-line consequences of the chain and
quotient rules; neither is in Mathlib in this form.
-/

/-- `(log(2 sin))′ = cos/sin` on `(0, π)`. -/
theorem hasDerivAt_log_two_sin {x : ℝ} (hx : Real.sin x ≠ 0) :
    HasDerivAt (fun y : ℝ => Real.log (2 * Real.sin y))
      (Real.cos x / Real.sin x) x := by
  have hg : HasDerivAt (fun y : ℝ => 2 * Real.sin y) (2 * Real.cos x) x :=
    (Real.hasDerivAt_sin x).const_mul 2
  have hne : (2 : ℝ) * Real.sin x ≠ 0 := by
    simpa using mul_ne_zero (two_ne_zero) hx
  have := hg.log hne
  convert this using 1
  field_simp

/-- `(cos/sin)′ = −1/sin²` on `(0, π)` — the second derivative of `log(2 sin)`. -/
theorem hasDerivAt_cos_div_sin {x : ℝ} (hx : Real.sin x ≠ 0) :
    HasDerivAt (fun y : ℝ => Real.cos y / Real.sin y)
      (-(1 / Real.sin x ^ 2)) x := by
  have := (Real.hasDerivAt_cos x).div (Real.hasDerivAt_sin x) hx
  convert this using 1
  have hpyth := Real.sin_sq_add_cos_sq x
  field_simp
  nlinarith [hpyth]

/-- **The trapezoid bound for `log(2 sin)`.**

`|trapezoid − ∫| ≤ (b−a)³·M/12` on any `[a,b] ⊆ (0,π)` with `1/sin² ≤ M`.

This is exactly the quantity `QOU.Knot.FigureEightVolume.kashaevErr_add_reflect`
proves `ε_k + ε_{N−1−k}` equals, on the cell `[θ, θ+h]`.  Bounding it completes
the symmetric half of `qou-mlgp` (A): it is `O(h³)` on the cell, hence `O(h²)`
against the `1/h` of the expansion — one order better than the `O(1/N)` claimed,
which is what leaves all the remaining difficulty in the antisymmetric half. -/
theorem abs_trapezoid_sub_integral_log_two_sin_le {a b M : ℝ}
    (ha : 0 < a) (hab : a ≤ b) (hb : b < π)
    (hM : ∀ x ∈ Set.uIcc a b, 1 / Real.sin x ^ 2 ≤ M) :
    |(b - a) / 2 * (Real.log (2 * Real.sin a) + Real.log (2 * Real.sin b))
        - ∫ x in a..b, Real.log (2 * Real.sin x)|
      ≤ (b - a) ^ 3 * M / 12 := by
  have hmem : ∀ x ∈ Set.uIcc a b, 0 < Real.sin x := by
    intro x hx
    rw [Set.uIcc_of_le hab, Set.mem_Icc] at hx
    exact Real.sin_pos_of_pos_of_lt_pi (lt_of_lt_of_le ha hx.1) (lt_of_le_of_lt hx.2 hb)
  refine abs_trapezoid_sub_integral_le (f' := fun x => Real.cos x / Real.sin x)
    (f'' := fun x => -(1 / Real.sin x ^ 2)) hab
    (fun x hx => hasDerivAt_log_two_sin (ne_of_gt (hmem x hx)))
    (fun x hx => hasDerivAt_cos_div_sin (ne_of_gt (hmem x hx))) ?_ ?_
  · intro x hx
    have hs : 0 < Real.sin x := hmem x hx
    exact (continuousWithinAt_const.div
      ((Real.continuous_sin.continuousWithinAt).pow 2) (by positivity)).neg
  · intro x hx
    have hs : 0 < Real.sin x := hmem x hx
    have : (0 : ℝ) < 1 / Real.sin x ^ 2 := by positivity
    rw [abs_neg, abs_of_pos this]
    exact hM x hx

end QOU.MathlibExt
