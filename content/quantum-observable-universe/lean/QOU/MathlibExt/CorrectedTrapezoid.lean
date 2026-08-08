/-
  The CORRECTED trapezoid rule — order-2 Euler–Maclaurin, `qou-mlgp` (A) gap 1.

  WHAT THIS IS.  `QOU/MathlibExt/TrapezoidRule.lean` gives the order-1 rule,

      ∫_a^b f = (h/2)(f a + f b) − ½∫ (x−a)(b−x)·f″,      h := b−a

  with an `O(h³)` per-cell error.  This file gives the next order, the rule that
  Euler–Maclaurin actually needs:

      ∫_a^b f = (h/2)(f a + f b) − (h²/12)·(f′ b − f′ a)
                  + (1/24)·∫_a^b (x−a)²(b−x)²·f⁗(x) dx

  exact for every `f ∈ C⁴`, with per-cell error `≤ h⁵·sup|f⁗|/720`.  The
  `−(h²/12)(f′(b) − f′(a))` term is exactly the Euler–Maclaurin `B₂` correction,
  and it TELESCOPES when the cells are summed — which is the entire reason the
  `qou-mlgp` (A) expansion has a `−(π/12N)·cot θ` term and no others below
  `O(1/N³)`.

  THE SAME ONE-FTC TRICK, ONE DEGREE UP.  Write `u := x−a` and take the kernel
  `w = u²(u−h)² = u⁴ − 2h·u³ + h²·u²`, whose double roots at both ends kill the
  first two boundary terms.  Its derivatives are

      w′  = 4u³ − 6h·u² + 2h²·u          w′(a) = w′(b) = 0
      w″  = 12u² − 12h·u + 2h²           w″(a) = w″(b) = 2h²
      w‴  = 24u − 12h                    w‴(a) = −12h,  w‴(b) = 12h
      w⁗  = 24

  and then

      F := w·f‴ − w′·f″ + w″·f′ − w‴·f       satisfies      F′ = w·f⁗ − 24·f

  since every cross term cancels against its neighbour.  One application of the
  FTC gives `∫(w f⁗ − 24 f) = F(b) − F(a) = 2h²(f′b − f′a) − 12h(f a + f b)`,
  and dividing by `24` is the identity.  No integration by parts is performed at
  all, let alone four times.

  WHAT THIS COMPLETES.  With this, every analytic ingredient `qou-mlgp` (A)
  named is in place: the reflection, the trapezoid identity AND bound, the exact
  removal of the `j = 0` singularity, Robbins' Stirling bounds on both sides,
  and now the order-2 correction whose `B₂` term is the `−(π/12N)cot θ` being
  chased.  What remains is assembly — summing this over the `k` cells of
  `logSinc` and combining with the split — not a missing piece of analysis.

  MATHLIB HAS NEITHER RULE, nor any quadrature at all.  See the header of
  `TrapezoidRule.lean`.

  -- Ref: [manuscript] QOU/MathlibExt/TrapezoidRule.lean        (the order-1 case)
  -- Ref: [manuscript] QOU/Knot/KashaevEndpointSplit.lean       (what consumes this)
  -- Ref: [manuscript] computations/probes/kashaev_endpoint_split_probe.py
-/
import QOU.MathlibExt.TrapezoidRule

namespace QOU.MathlibExt

open Real MeasureTheory intervalIntegral

/-- `∫_a^b (x−a)²(b−x)² dx = (b−a)⁵/30` — the total mass of the order-2 Peano
kernel.  This is what turns `sup|f⁗|` into the `1/720`. -/
theorem integral_weight_sq (a b : ℝ) :
    ∫ x in a..b, (x - a) ^ 2 * (b - x) ^ 2 = (b - a) ^ 5 / 30 := by
  have hG : ∀ x : ℝ, HasDerivAt
      (fun y : ℝ => (y - a) ^ 5 / 5 - (b - a) * (y - a) ^ 4 / 2
        + (b - a) ^ 2 * (y - a) ^ 3 / 3)
      ((x - a) ^ 2 * (b - x) ^ 2) x := by
    intro x
    have hu : HasDerivAt (fun y : ℝ => y - a) 1 x := by
      simpa using (hasDerivAt_id x).sub_const a
    have h5 := (hu.pow 5).div_const 5
    have h4 := ((hu.pow 4).const_mul (b - a)).div_const 2
    have h3 := ((hu.pow 3).const_mul ((b - a) ^ 2)).div_const 3
    have h := (h5.sub h4).add h3
    convert h using 1
    push_cast
    ring
  have hcont : Continuous fun x : ℝ => (x - a) ^ 2 * (b - x) ^ 2 := by fun_prop
  rw [integral_eq_sub_of_hasDerivAt (fun x _ => hG x) (hcont.intervalIntegrable a b)]
  ring

/-- **The corrected trapezoid rule with its exact error term.**

    ∫_a^b f = (h/2)(f a + f b) − (h²/12)(f′ b − f′ a)
                + (1/24)·∫_a^b (x−a)²(b−x)²·f⁗(x) dx,     h = b−a

exact for every `f` with four derivatives on `[[a,b]]` and `f⁗` continuous
there.  The `−(h²/12)(f′ b − f′ a)` term is the Euler–Maclaurin `B₂`
correction. -/
theorem integral_eq_corrected_trapezoid_sub
    {f f' f'' f''' f'''' : ℝ → ℝ} {a b : ℝ}
    (hf : ∀ x ∈ Set.uIcc a b, HasDerivAt f (f' x) x)
    (hf' : ∀ x ∈ Set.uIcc a b, HasDerivAt f' (f'' x) x)
    (hf'' : ∀ x ∈ Set.uIcc a b, HasDerivAt f'' (f''' x) x)
    (hf''' : ∀ x ∈ Set.uIcc a b, HasDerivAt f''' (f'''' x) x)
    (hcont : ContinuousOn f'''' (Set.uIcc a b)) :
    ∫ x in a..b, f x
      = (b - a) / 2 * (f a + f b)
        - (b - a) ^ 2 / 12 * (f' b - f' a)
        + 1 / 24 * ∫ x in a..b, (x - a) ^ 2 * (b - x) ^ 2 * f'''' x := by
  have hfcont : ContinuousOn f (Set.uIcc a b) := fun x hx =>
    (hf x hx).continuousAt.continuousWithinAt
  have hwcont : ContinuousOn (fun x : ℝ => (x - a) ^ 2 * (b - x) ^ 2)
      (Set.uIcc a b) := by fun_prop
  -- `F := w f‴ − w′ f″ + w″ f′ − w‴ f` has derivative `w f⁗ − 24 f`.
  have hF : ∀ x ∈ Set.uIcc a b, HasDerivAt
      (fun y : ℝ => (y - a) ^ 2 * (b - y) ^ 2 * f''' y
        - (4 * (y - a) ^ 3 - 6 * (b - a) * (y - a) ^ 2 + 2 * (b - a) ^ 2 * (y - a))
            * f'' y
        + (12 * (y - a) ^ 2 - 12 * (b - a) * (y - a) + 2 * (b - a) ^ 2) * f' y
        - (24 * (y - a) - 12 * (b - a)) * f y)
      ((x - a) ^ 2 * (b - x) ^ 2 * f'''' x - 24 * f x) x := by
    intro x hx
    have hu : HasDerivAt (fun y : ℝ => y - a) 1 x := by
      simpa using (hasDerivAt_id x).sub_const a
    have hbx : HasDerivAt (fun y : ℝ => b - y) (-1) x := by
      simpa using (hasDerivAt_id x).const_sub b
    -- ascribe each power to its lambda form, so `.mul` below builds a genuine
    -- pointwise product rather than a `Pi` power that `ring` cannot beta-reduce
    have hu2 : HasDerivAt (fun y : ℝ => (y - a) ^ 2) (2 * (x - a)) x := by
      have h := hu.pow 2; norm_num at h; convert h using 1
    have hu3 : HasDerivAt (fun y : ℝ => (y - a) ^ 3) (3 * (x - a) ^ 2) x := by
      have h := hu.pow 3; norm_num at h; convert h using 1
    have hb2 : HasDerivAt (fun y : ℝ => (b - y) ^ 2) (-(2 * (b - x))) x := by
      have h := hbx.pow 2; norm_num at h; convert h using 1
    -- `w′ = 4u³ − 6h u² + 2h² u`
    have hw : HasDerivAt (fun y : ℝ => (y - a) ^ 2 * (b - y) ^ 2)
        (4 * (x - a) ^ 3 - 6 * (b - a) * (x - a) ^ 2
          + 2 * (b - a) ^ 2 * (x - a)) x := by
      have h := hu2.mul hb2
      convert h using 1
      ring
    -- `w″ = 12u² − 12h u + 2h²`
    have hw1 : HasDerivAt
        (fun y : ℝ => 4 * (y - a) ^ 3 - 6 * (b - a) * (y - a) ^ 2
          + 2 * (b - a) ^ 2 * (y - a))
        (12 * (x - a) ^ 2 - 12 * (b - a) * (x - a) + 2 * (b - a) ^ 2) x := by
      have h := ((hu3.const_mul (4 : ℝ)).sub (hu2.const_mul (6 * (b - a)))).add
        (hu.const_mul (2 * (b - a) ^ 2))
      convert h using 1
      ring
    -- `w‴ = 24u − 12h`
    have hw2 : HasDerivAt
        (fun y : ℝ => 12 * (y - a) ^ 2 - 12 * (b - a) * (y - a) + 2 * (b - a) ^ 2)
        (24 * (x - a) - 12 * (b - a)) x := by
      have h := ((hu2.const_mul (12 : ℝ)).sub (hu.const_mul (12 * (b - a)))).add_const
        (2 * (b - a) ^ 2)
      convert h using 1
      ring
    -- `w⁗ = 24`
    have hw3 : HasDerivAt (fun y : ℝ => 24 * (y - a) - 12 * (b - a)) 24 x := by
      have h := (hu.const_mul (24 : ℝ)).sub_const (12 * (b - a))
      convert h using 1
      ring
    -- assemble the `f`-tower; every cross term cancels against its neighbour
    have hgoal := (((hw.mul (hf''' x hx)).sub (hw1.mul (hf'' x hx))).add
      (hw2.mul (hf' x hx))).sub (hw3.mul (hf x hx))
    convert hgoal using 1
    ring
  have hint : IntervalIntegrable
      (fun x => (x - a) ^ 2 * (b - x) ^ 2 * f'''' x - 24 * f x) volume a b := by
    refine IntervalIntegrable.sub ?_ ?_
    · exact (hwcont.mul hcont).intervalIntegrable
    · exact (continuousOn_const.mul hfcont).intervalIntegrable
  have hftc := integral_eq_sub_of_hasDerivAt hF hint
  rw [integral_sub ((hwcont.mul hcont).intervalIntegrable)
    ((continuousOn_const.mul hfcont).intervalIntegrable)] at hftc
  rw [intervalIntegral.integral_const_mul] at hftc
  linear_combination -hftc / 24

/-- **The corrected trapezoid error bound.**  `h⁵·M/720` for `|f⁗| ≤ M`.

Two orders better per cell than the plain trapezoid rule — `O(h⁴)` rather than
`O(h²)` once summed over `1/h` cells. -/
theorem abs_corrected_trapezoid_sub_integral_le
    {f f' f'' f''' f'''' : ℝ → ℝ} {a b M : ℝ} (hab : a ≤ b)
    (hf : ∀ x ∈ Set.uIcc a b, HasDerivAt f (f' x) x)
    (hf' : ∀ x ∈ Set.uIcc a b, HasDerivAt f' (f'' x) x)
    (hf'' : ∀ x ∈ Set.uIcc a b, HasDerivAt f'' (f''' x) x)
    (hf''' : ∀ x ∈ Set.uIcc a b, HasDerivAt f''' (f'''' x) x)
    (hcont : ContinuousOn f'''' (Set.uIcc a b))
    (hM : ∀ x ∈ Set.uIcc a b, |f'''' x| ≤ M) :
    |(b - a) / 2 * (f a + f b) - (b - a) ^ 2 / 12 * (f' b - f' a)
        - ∫ x in a..b, f x|
      ≤ (b - a) ^ 5 * M / 720 := by
  have hwcont : ContinuousOn (fun x : ℝ => (x - a) ^ 2 * (b - x) ^ 2)
      (Set.uIcc a b) := by fun_prop
  have hkey := integral_eq_corrected_trapezoid_sub hf hf' hf'' hf''' hcont
  have hrw : (b - a) / 2 * (f a + f b) - (b - a) ^ 2 / 12 * (f' b - f' a)
        - ∫ x in a..b, f x
      = -(1 / 24) * ∫ x in a..b, (x - a) ^ 2 * (b - x) ^ 2 * f'''' x := by
    rw [hkey]; ring
  rw [hrw, abs_mul]
  have habs : |∫ x in a..b, (x - a) ^ 2 * (b - x) ^ 2 * f'''' x|
      ≤ ∫ x in a..b, |(x - a) ^ 2 * (b - x) ^ 2 * f'''' x| :=
    abs_integral_le_integral_abs hab
  have hpt : ∀ x ∈ Set.uIcc a b,
      |(x - a) ^ 2 * (b - x) ^ 2 * f'''' x| ≤ M * ((x - a) ^ 2 * (b - x) ^ 2) := by
    intro x hx
    have hw0 : (0 : ℝ) ≤ (x - a) ^ 2 * (b - x) ^ 2 := by positivity
    rw [abs_mul, abs_of_nonneg hw0]
    have hMx : |f'''' x| ≤ M := hM x hx
    nlinarith [abs_nonneg (f'''' x), hw0, hMx]
  have hmono : (∫ x in a..b, |(x - a) ^ 2 * (b - x) ^ 2 * f'''' x|)
      ≤ ∫ x in a..b, M * ((x - a) ^ 2 * (b - x) ^ 2) := by
    refine integral_mono_on hab ?_ ?_ ?_
    · exact ((hwcont.mul hcont).abs).intervalIntegrable
    · exact (continuousOn_const.mul hwcont).intervalIntegrable
    · intro x hx
      exact hpt x (by rw [Set.uIcc_of_le hab]; exact hx)
  rw [intervalIntegral.integral_const_mul, integral_weight_sq] at hmono
  have h24 : |-(1 : ℝ) / 24| = 1 / 24 := by norm_num
  rw [show -(1 / 24 : ℝ) = -(1 : ℝ) / 24 by norm_num, h24]
  linarith

end QOU.MathlibExt
