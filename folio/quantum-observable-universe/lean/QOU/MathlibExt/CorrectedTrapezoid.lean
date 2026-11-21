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

  -- Ref: [leitner2026] QOU/MathlibExt/TrapezoidRule.lean        (the order-1 case)
  -- Ref: [leitner2026] QOU/Knot/KashaevEndpointSplit.lean       (what consumes this)
  -- Ref: [leitner2026] computations/probes/kashaev_endpoint_split_probe.py
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

/-! ### Reducing the remainder from `g⁗` to `g″`

The kernel `w = (x−a)²(b−x)²` has DOUBLE roots at both ends, so `w(a) = w(b) =
w′(a) = w′(b) = 0` and two integrations by parts leave no boundary terms at all:

    ∫_a^b w·g⁗ = ∫_a^b w″·g″,        w″ = 12(x−a)² − 12(b−a)(x−a) + 2(b−a)²

(again one FTC application, against `F := w·g‴ − w′·g″`).  Moreover `w″` has ZERO
MEAN, `∫_a^b w″ = 0`, because `w′` vanishes at both ends.

WHY THIS MATTERS FOR `qou-mlgp` (A).  The `g⁗` form needs `sup|logSinc⁗|`, whose
finiteness rests on an eighth-order cancellation (`6/x⁴ − (4cos²+2)/sin⁴`, two
terms that individually blow up — at `N = 100` the crude bound overshoots by
`5·10⁷`).  The `g″` form needs only `logSinc″`, which is already bounded here
(`QOU/Knot/LogSincNearZero.lean`: `|logSinc″| ≤ 1` on `(0,1]`).

The zero mean is what makes it sharp enough.  Writing the remainder as
`∫ w″·(g″ − c)` for any constant `c` and taking `c = g″(a)`,

    |remainder| ≤ (∫|w″|)·osc_cell(g″) ≤ 2h³·osc_cell(g″),

and if `g″` is MONOTONE the per-cell oscillations telescope over the `k` cells to
`|g″(b) − g″(a)| ≤ 2·sup|g″|` instead of accumulating as `k·h·sup|g‴|`.  That
turns the composite error on the sum into `O(h²·sup|g″|) = O(1/N²)` — below the
`O(1/N)` term (A) is after.

So the remaining analytic requirement drops from "bound `logSinc⁗`" (an
eighth-order cancellation) to "`logSinc″` is monotone", i.e. the SIGN condition
`logSinc‴ < 0`, i.e. `x³·cos x < sin³x` on `(0, π)`.  That is a single clean
inequality — an Adamović–Mitrinović-type statement — rather than a cancellation
estimate.  It is not proved here, and Mathlib's `sin_gt_sub_cube` (`x − x³/4`)
is too weak for it; the sharper `sin x > x − x³/6` would suffice.
-/

/-- **The order-2 kernel's derivative has zero mean:** `∫_a^b w″ = 0`.

Immediate from the FTC: its antiderivative `w′ = 4(x−a)³ − 6(b−a)(x−a)² +
2(b−a)²(x−a)` vanishes at both endpoints. -/
theorem integral_weight_sq_deriv2 (a b : ℝ) :
    ∫ x in a..b, (12 * (x - a) ^ 2 - 12 * (b - a) * (x - a) + 2 * (b - a) ^ 2)
      = 0 := by
  have hW : ∀ x : ℝ, HasDerivAt
      (fun y : ℝ => 4 * (y - a) ^ 3 - 6 * (b - a) * (y - a) ^ 2
        + 2 * (b - a) ^ 2 * (y - a))
      (12 * (x - a) ^ 2 - 12 * (b - a) * (x - a) + 2 * (b - a) ^ 2) x := by
    intro x
    have hu : HasDerivAt (fun y : ℝ => y - a) 1 x := by
      simpa using (hasDerivAt_id x).sub_const a
    have hu2 : HasDerivAt (fun y : ℝ => (y - a) ^ 2) (2 * (x - a)) x := by
      have h := hu.pow 2; norm_num at h; convert h using 1
    have hu3 : HasDerivAt (fun y : ℝ => (y - a) ^ 3) (3 * (x - a) ^ 2) x := by
      have h := hu.pow 3; norm_num at h; convert h using 1
    have h := ((hu3.const_mul (4 : ℝ)).sub (hu2.const_mul (6 * (b - a)))).add
      (hu.const_mul (2 * (b - a) ^ 2))
    convert h using 1
    ring
  have hcont : Continuous fun x : ℝ =>
      12 * (x - a) ^ 2 - 12 * (b - a) * (x - a) + 2 * (b - a) ^ 2 := by fun_prop
  rw [integral_eq_sub_of_hasDerivAt (fun x _ => hW x) (hcont.intervalIntegrable a b)]
  ring

/-- **The order-2 remainder in second-derivative form.**

    ∫_a^b (x−a)²(b−x)²·g⁗ = ∫_a^b (12(x−a)² − 12(b−a)(x−a) + 2(b−a)²)·g″

Two integrations by parts with no boundary terms, because `w` has double roots at
both endpoints — done as one FTC application against `F := w·g‴ − w′·g″`. -/
theorem integral_weight_sq_mul_deriv4_eq {g₂ g₃ g₄ : ℝ → ℝ} {a b : ℝ}
    (hg2 : ∀ x ∈ Set.uIcc a b, HasDerivAt g₂ (g₃ x) x)
    (hg3 : ∀ x ∈ Set.uIcc a b, HasDerivAt g₃ (g₄ x) x)
    (hc2 : ContinuousOn g₂ (Set.uIcc a b))
    (hc4 : ContinuousOn g₄ (Set.uIcc a b)) :
    (∫ x in a..b, (x - a) ^ 2 * (b - x) ^ 2 * g₄ x)
      = ∫ x in a..b,
          (12 * (x - a) ^ 2 - 12 * (b - a) * (x - a) + 2 * (b - a) ^ 2) * g₂ x := by
  have hwc : ContinuousOn (fun x : ℝ => (x - a) ^ 2 * (b - x) ^ 2)
      (Set.uIcc a b) := by fun_prop
  have hw2c : ContinuousOn (fun x : ℝ =>
      12 * (x - a) ^ 2 - 12 * (b - a) * (x - a) + 2 * (b - a) ^ 2)
      (Set.uIcc a b) := by fun_prop
  have hF : ∀ x ∈ Set.uIcc a b, HasDerivAt
      (fun y : ℝ => (y - a) ^ 2 * (b - y) ^ 2 * g₃ y
        - (4 * (y - a) ^ 3 - 6 * (b - a) * (y - a) ^ 2 + 2 * (b - a) ^ 2 * (y - a))
            * g₂ y)
      ((x - a) ^ 2 * (b - x) ^ 2 * g₄ x
        - (12 * (x - a) ^ 2 - 12 * (b - a) * (x - a) + 2 * (b - a) ^ 2) * g₂ x) x := by
    intro x hx
    have hu : HasDerivAt (fun y : ℝ => y - a) 1 x := by
      simpa using (hasDerivAt_id x).sub_const a
    have hbx : HasDerivAt (fun y : ℝ => b - y) (-1) x := by
      simpa using (hasDerivAt_id x).const_sub b
    have hu2 : HasDerivAt (fun y : ℝ => (y - a) ^ 2) (2 * (x - a)) x := by
      have h := hu.pow 2; norm_num at h; convert h using 1
    have hu3 : HasDerivAt (fun y : ℝ => (y - a) ^ 3) (3 * (x - a) ^ 2) x := by
      have h := hu.pow 3; norm_num at h; convert h using 1
    have hb2 : HasDerivAt (fun y : ℝ => (b - y) ^ 2) (-(2 * (b - x))) x := by
      have h := hbx.pow 2; norm_num at h; convert h using 1
    have hw : HasDerivAt (fun y : ℝ => (y - a) ^ 2 * (b - y) ^ 2)
        (4 * (x - a) ^ 3 - 6 * (b - a) * (x - a) ^ 2
          + 2 * (b - a) ^ 2 * (x - a)) x := by
      have h := hu2.mul hb2
      convert h using 1
      ring
    have hw1 : HasDerivAt
        (fun y : ℝ => 4 * (y - a) ^ 3 - 6 * (b - a) * (y - a) ^ 2
          + 2 * (b - a) ^ 2 * (y - a))
        (12 * (x - a) ^ 2 - 12 * (b - a) * (x - a) + 2 * (b - a) ^ 2) x := by
      have h := ((hu3.const_mul (4 : ℝ)).sub (hu2.const_mul (6 * (b - a)))).add
        (hu.const_mul (2 * (b - a) ^ 2))
      convert h using 1
      ring
    have h := (hw.mul (hg3 x hx)).sub (hw1.mul (hg2 x hx))
    convert h using 1
    ring
  have hint : IntervalIntegrable
      (fun x => (x - a) ^ 2 * (b - x) ^ 2 * g₄ x
        - (12 * (x - a) ^ 2 - 12 * (b - a) * (x - a) + 2 * (b - a) ^ 2) * g₂ x)
      volume a b :=
    ((hwc.mul hc4).sub (hw2c.mul hc2)).intervalIntegrable
  have hftc := integral_eq_sub_of_hasDerivAt hF hint
  rw [integral_sub (hwc.mul hc4).intervalIntegrable
    (hw2c.mul hc2).intervalIntegrable] at hftc
  -- both boundary terms vanish: `w` and `w′` have double/simple roots at `a`, `b`
  have hb : (b - a) ^ 2 * (b - b) ^ 2 * g₃ b
      - (4 * (b - a) ^ 3 - 6 * (b - a) * (b - a) ^ 2 + 2 * (b - a) ^ 2 * (b - a))
        * g₂ b = 0 := by ring
  have ha : (a - a) ^ 2 * (b - a) ^ 2 * g₃ a
      - (4 * (a - a) ^ 3 - 6 * (b - a) * (a - a) ^ 2 + 2 * (b - a) ^ 2 * (a - a))
        * g₂ a = 0 := by ring
  rw [hb, ha] at hftc
  linarith

/-! ### The `g″`-form error bound, driven by OSCILLATION rather than a sup

Combining the three previous results — the exact order-2 identity, the reduction
`∫ w·g⁗ = ∫ w″·g″`, and `∫ w″ = 0` — the per-cell error is controlled by the
OSCILLATION of `g″` on the cell, not by `sup|g⁗|`.  That is what lets the cells
telescope when `g″` is monotone.
-/

/-- `|w″| ≤ 2(b−a)²` on `[a,b]`.  Writing `u = x−a` and `h = b−a`,
`w″ = 12u² − 12hu + 2h² = 12(u − h/2)² − h²`, which on `u ∈ [0,h]` ranges over
`[−h², 2h²]`. -/
theorem abs_weight_sq_deriv2_le {a b x : ℝ} (_hab : a ≤ b) (hx : x ∈ Set.Icc a b) :
    |12 * (x - a) ^ 2 - 12 * (b - a) * (x - a) + 2 * (b - a) ^ 2|
      ≤ 2 * (b - a) ^ 2 := by
  rw [Set.mem_Icc] at hx
  rw [abs_le]
  constructor <;>
    nlinarith [mul_nonneg (sub_nonneg.mpr hx.1) (sub_nonneg.mpr hx.2),
      sq_nonneg (b - a), sq_nonneg (2 * x - a - b)]

/-- **The order-2 identity from the order-1 one — only `C²` needed.**

    ∫_a^b g = (h/2)(g a + g b) − (h²/12)(g₁ b − g₁ a)
                + (1/24)·∫_a^b w″·g₂,      h = b−a

with NO `g‴` or `g⁗` hypotheses anywhere.  The order-2 rule was originally
derived from the quartic kernel, which forced four derivatives; but the kernel
identity

    w″ = 12(x−a)² − 12(b−a)(x−a) + 2(b−a)² = −12·(x−a)(b−x) + 2(b−a)²

expresses `w″` in terms of the ORDER-1 kernel `(x−a)(b−x)`, so

    (1/24)∫ w″ g₂ = −½∫ (x−a)(b−x) g₂ + ((b−a)²/12)·∫ g₂
                  = −½∫ (x−a)(b−x) g₂ + ((b−a)²/12)(g₁ b − g₁ a)

by the FTC on `g₂`.  Substituting into `integral_eq_trapezoid_sub` the `B₂`
terms cancel exactly and the order-1 identity is recovered.  So the order-2
rule is a REWRITING of the order-1 rule, not a deeper theorem — and it inherits
the order-1 rule's `C²` hypotheses. -/
theorem integral_eq_corrected_trapezoid_sub_deriv2 {g g₁ g₂ : ℝ → ℝ} {a b : ℝ}
    (hg : ∀ x ∈ Set.uIcc a b, HasDerivAt g (g₁ x) x)
    (hg1 : ∀ x ∈ Set.uIcc a b, HasDerivAt g₁ (g₂ x) x)
    (hc2 : ContinuousOn g₂ (Set.uIcc a b)) :
    ∫ x in a..b, g x
      = (b - a) / 2 * (g a + g b)
        - (b - a) ^ 2 / 12 * (g₁ b - g₁ a)
        + 1 / 24 * ∫ x in a..b,
            (12 * (x - a) ^ 2 - 12 * (b - a) * (x - a) + 2 * (b - a) ^ 2) * g₂ x := by
  have hord1 := integral_eq_trapezoid_sub hg hg1 hc2
  have hg2int := hc2.intervalIntegrable (μ := volume)
  have hftc : (∫ x in a..b, g₂ x) = g₁ b - g₁ a :=
    integral_eq_sub_of_hasDerivAt hg1 hg2int
  have hw1c : ContinuousOn (fun x : ℝ => (x - a) * (b - x)) (Set.uIcc a b) := by fun_prop
  have hw1g := (hw1c.mul hc2).intervalIntegrable (μ := volume)
  -- `w″·g₂ = −12·(x−a)(b−x)·g₂ + 2(b−a)²·g₂`
  have hpt : ∀ x : ℝ,
      (12 * (x - a) ^ 2 - 12 * (b - a) * (x - a) + 2 * (b - a) ^ 2) * g₂ x
        = -12 * ((x - a) * (b - x) * g₂ x) + 2 * (b - a) ^ 2 * g₂ x := by
    intro x; ring
  have hsplit : (∫ x in a..b,
      (12 * (x - a) ^ 2 - 12 * (b - a) * (x - a) + 2 * (b - a) ^ 2) * g₂ x)
      = -12 * (∫ x in a..b, (x - a) * (b - x) * g₂ x)
        + 2 * (b - a) ^ 2 * (g₁ b - g₁ a) := by
    simp_rw [hpt]
    rw [integral_add (hw1g.const_mul _) (hg2int.const_mul _),
      intervalIntegral.integral_const_mul, intervalIntegral.integral_const_mul, hftc]
  rw [hsplit]
  linarith [hord1]

/-- **`|∫_a^b w″·g″| ≤ 2(b−a)³·D`** when `|g″ − g″(a)| ≤ D` on the cell.

The point is that `D` is an OSCILLATION, not a supremum: `∫ w″ = 0` lets `g″` be
replaced by `g″ − g″(a)` for free. -/
theorem abs_integral_weight_sq_deriv2_mul_le {g₂ : ℝ → ℝ} {a b D : ℝ} (hab : a ≤ b)
    (hc2 : ContinuousOn g₂ (Set.uIcc a b))
    (hD : ∀ x ∈ Set.uIcc a b, |g₂ x - g₂ a| ≤ D) :
    |∫ x in a..b,
        (12 * (x - a) ^ 2 - 12 * (b - a) * (x - a) + 2 * (b - a) ^ 2) * g₂ x|
      ≤ 2 * (b - a) ^ 3 * D := by
  have hWc : ContinuousOn (fun x : ℝ =>
      12 * (x - a) ^ 2 - 12 * (b - a) * (x - a) + 2 * (b - a) ^ 2)
      (Set.uIcc a b) := by fun_prop
  have hWint := hWc.intervalIntegrable (μ := volume)
  have hWg2 := (hWc.mul hc2).intervalIntegrable (μ := volume)
  -- replace `g₂` by `g₂ − g₂ a`, free because `∫ w″ = 0`
  have hshift : (∫ x in a..b,
        (12 * (x - a) ^ 2 - 12 * (b - a) * (x - a) + 2 * (b - a) ^ 2) * g₂ x)
      = ∫ x in a..b,
          (12 * (x - a) ^ 2 - 12 * (b - a) * (x - a) + 2 * (b - a) ^ 2)
            * (g₂ x - g₂ a) := by
    have hpt : ∀ x : ℝ,
        (12 * (x - a) ^ 2 - 12 * (b - a) * (x - a) + 2 * (b - a) ^ 2) * (g₂ x - g₂ a)
          = (12 * (x - a) ^ 2 - 12 * (b - a) * (x - a) + 2 * (b - a) ^ 2) * g₂ x
            - g₂ a * (12 * (x - a) ^ 2 - 12 * (b - a) * (x - a) + 2 * (b - a) ^ 2) := by
      intro x; ring
    simp_rw [hpt]
    rw [integral_sub hWg2 (hWint.const_mul _),
      intervalIntegral.integral_const_mul, integral_weight_sq_deriv2]
    ring
  rw [hshift]
  have hDnn : 0 ≤ D := le_trans (abs_nonneg _)
    (hD a (by rw [Set.uIcc_of_le hab]; exact ⟨le_rfl, hab⟩))
  have hpt : ∀ x ∈ Set.uIcc a b,
      |(12 * (x - a) ^ 2 - 12 * (b - a) * (x - a) + 2 * (b - a) ^ 2) * (g₂ x - g₂ a)|
        ≤ 2 * (b - a) ^ 2 * D := by
    intro x hx
    rw [abs_mul]
    have h1 := abs_weight_sq_deriv2_le hab (by rwa [Set.uIcc_of_le hab] at hx)
    have h2 := hD x hx
    have hw0 : (0 : ℝ) ≤ 2 * (b - a) ^ 2 := by positivity
    exact mul_le_mul h1 h2 (abs_nonneg _) hw0
  calc |∫ x in a..b, _ * (g₂ x - g₂ a)|
      ≤ ∫ x in a..b,
          |(12 * (x - a) ^ 2 - 12 * (b - a) * (x - a) + 2 * (b - a) ^ 2)
            * (g₂ x - g₂ a)| := abs_integral_le_integral_abs hab
    _ ≤ ∫ _x in a..b, 2 * (b - a) ^ 2 * D := by
        refine integral_mono_on hab
          (((hWc.mul (hc2.sub continuousOn_const)).abs).intervalIntegrable
            (μ := volume))
          ((continuousOn_const :
            ContinuousOn (fun _ : ℝ => 2 * (b - a) ^ 2 * D)
              (Set.uIcc a b)).intervalIntegrable (μ := volume)) ?_
        intro x hx
        exact hpt x (by rw [Set.uIcc_of_le hab]; exact hx)
    _ = 2 * (b - a) ^ 3 * D := by
        rw [intervalIntegral.integral_const, smul_eq_mul]
        ring

/-- **The order-2 error bound driven by the oscillation of `g″`.**

    |trapezoid − B₂-correction − ∫| ≤ (b−a)³·D/12   when |g″ − g″(a)| ≤ D.

Compare `abs_corrected_trapezoid_sub_integral_le`, which needs `sup|g⁗|`.  This
version needs only how much `g″` MOVES across the cell, which is what telescopes
when `g″` is monotone. -/
theorem abs_corrected_trapezoid_sub_integral_le_osc
    {g g₁ g₂ : ℝ → ℝ} {a b D : ℝ} (hab : a ≤ b)
    (hg : ∀ x ∈ Set.uIcc a b, HasDerivAt g (g₁ x) x)
    (hg1 : ∀ x ∈ Set.uIcc a b, HasDerivAt g₁ (g₂ x) x)
    (hc2 : ContinuousOn g₂ (Set.uIcc a b))
    (hD : ∀ x ∈ Set.uIcc a b, |g₂ x - g₂ a| ≤ D) :
    |(b - a) / 2 * (g a + g b) - (b - a) ^ 2 / 12 * (g₁ b - g₁ a)
        - ∫ x in a..b, g x|
      ≤ (b - a) ^ 3 * D / 12 := by
  have hid := integral_eq_corrected_trapezoid_sub_deriv2 hg hg1 hc2
  have hbd := abs_integral_weight_sq_deriv2_mul_le hab hc2 hD
  have hrw : (b - a) / 2 * (g a + g b) - (b - a) ^ 2 / 12 * (g₁ b - g₁ a)
      - ∫ x in a..b, g x
      = -(1 / 24) * ∫ x in a..b,
          (12 * (x - a) ^ 2 - 12 * (b - a) * (x - a) + 2 * (b - a) ^ 2) * g₂ x := by
    rw [hid]; ring
  rw [hrw, abs_mul]
  have h24 : |-(1 : ℝ) / 24| = 1 / 24 := by norm_num
  rw [show -(1 / 24 : ℝ) = -(1 : ℝ) / 24 by norm_num, h24]
  linarith

end QOU.MathlibExt
