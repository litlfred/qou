/-
  TAYLOR'S THEOREM TO SECOND ORDER, WITH THE INTEGRAL REMAINDER.

  Mathlib has `taylor_mean_remainder_lagrange`, stated through `ContDiffOn` and
  `iteratedDerivWithin`.  That is the right general form, and it is the wrong
  shape for a function whose derivatives one has as an explicit chain of
  `HasDerivAt`s — which is how every function in this corpus arrives
  (`hasDerivAt_Lob`, `hasDerivAt_log_two_sin`, `hasDerivAt_cos_div_sin`).
  Restating those as a `ContDiffOn` is more work than the theorem.

  So: the order-2 case, in the `HasDerivAt`-chain shape,

      f b = f a + f₁ a (b−a) + f₂ a (b−a)²/2 + ∫_a^b f₃ t (b−t)²/2 dt

  proved by ONE application of the fundamental theorem of calculus against

      F t = f t + f₁ t (b−t) + f₂ t (b−t)²/2,      F′ t = f₃ t (b−t)²/2

  where the two `f₁` terms and the two `f₂` terms cancel in pairs.  Same trick
  as `TrapezoidRule.lean`'s `F := w·f′ − w′·f`, and it works for the same
  reason: choosing the primitive so that the telescoping is visible turns a
  three-step induction into a single FTC.

  `b` is not required to be on either side of `a` — the bound carries `|b−a|³`
  and both orders are proved.

  -- Ref: [leitner2026] QOU/MathlibExt/TrapezoidRule.lean
-/
import Mathlib.Analysis.Calculus.MeanValue
import Mathlib.MeasureTheory.Integral.IntervalIntegral.FundThmCalculus
import Mathlib.Tactic

namespace QOU.MathlibExt

open Real MeasureTheory intervalIntegral

/-- `∫_a^b (b−t)²/2 dt = (b−a)³/6`, both orders. -/
theorem integral_sq_weight (a b : ℝ) :
    ∫ t in a..b, (b - t) ^ 2 / 2 = (b - a) ^ 3 / 6 := by
  have hG : ∀ t ∈ Set.uIcc a b,
      HasDerivAt (fun s : ℝ => -((b - s) ^ 3) / 6) ((b - t) ^ 2 / 2) t := by
    intro t _
    have hbt : HasDerivAt (fun s : ℝ => b - s) (-1) t := by
      simpa using (hasDerivAt_id t).const_sub b
    have h3 : HasDerivAt (fun s : ℝ => (b - s) ^ 3) (3 * (b - t) ^ 2 * (-1)) t := by
      simpa using hbt.pow 3
    have := (h3.neg).div_const 6
    convert this using 1
    ring
  have hc : ContinuousOn (fun t : ℝ => (b - t) ^ 2 / 2) (Set.uIcc a b) := by fun_prop
  rw [integral_eq_sub_of_hasDerivAt hG (hc.intervalIntegrable ..)]
  ring

/-- The remainder integral is `O(|b−a|³)` with the sharp constant `1/6`. -/
theorem abs_integral_sq_weight_mul_le {g : ℝ → ℝ} {a b M : ℝ}
    (hg : ∀ x ∈ Set.uIcc a b, |g x| ≤ M)
    (hgc : ContinuousOn g (Set.uIcc a b)) :
    |∫ t in a..b, g t * ((b - t) ^ 2 / 2)| ≤ M * |b - a| ^ 3 / 6 := by
  have hM0 : 0 ≤ M := by
    have ha : a ∈ Set.uIcc a b := Set.left_mem_uIcc
    exact le_trans (abs_nonneg _) (hg a ha)
  have hwc : ContinuousOn (fun t : ℝ => (b - t) ^ 2 / 2) (Set.uIcc a b) := by fun_prop
  have hprod : IntervalIntegrable (fun t => g t * ((b - t) ^ 2 / 2)) volume a b :=
    (hgc.mul hwc).intervalIntegrable ..
  have hMint : IntervalIntegrable (fun t => M * ((b - t) ^ 2 / 2)) volume a b :=
    (continuousOn_const.mul hwc).intervalIntegrable ..
  have hmMint : IntervalIntegrable (fun t => -M * ((b - t) ^ 2 / 2)) volume a b :=
    (continuousOn_const.mul hwc).intervalIntegrable ..
  have hMval : (∫ t in a..b, M * ((b - t) ^ 2 / 2)) = M * ((b - a) ^ 3 / 6) := by
    rw [intervalIntegral.integral_const_mul, integral_sq_weight]
  have hmMval : (∫ t in a..b, -M * ((b - t) ^ 2 / 2)) = -M * ((b - a) ^ 3 / 6) := by
    rw [intervalIntegral.integral_const_mul, integral_sq_weight]
  rcases le_total a b with hab | hab
  · have hsub : Set.Icc a b ⊆ Set.uIcc a b := by rw [Set.uIcc_of_le hab]
    have hup : (∫ t in a..b, g t * ((b - t) ^ 2 / 2))
        ≤ ∫ t in a..b, M * ((b - t) ^ 2 / 2) := by
      refine intervalIntegral.integral_mono_on hab hprod hMint (fun x hx => ?_)
      have hb := (abs_le.mp (hg x (hsub hx))).2
      have hw : (0 : ℝ) ≤ (b - x) ^ 2 / 2 := by positivity
      nlinarith
    have hlo : (∫ t in a..b, -M * ((b - t) ^ 2 / 2))
        ≤ ∫ t in a..b, g t * ((b - t) ^ 2 / 2) := by
      refine intervalIntegral.integral_mono_on hab hmMint hprod (fun x hx => ?_)
      have hb := (abs_le.mp (hg x (hsub hx))).1
      have hw : (0 : ℝ) ≤ (b - x) ^ 2 / 2 := by positivity
      nlinarith
    rw [hMval] at hup
    rw [hmMval] at hlo
    have habs : |b - a| = b - a := abs_of_nonneg (by linarith)
    rw [abs_le, habs]
    constructor <;> nlinarith
  · -- `b ≤ a`: flip the interval; the weight integral changes sign with it
    have hflip : (∫ t in a..b, g t * ((b - t) ^ 2 / 2))
        = -∫ t in b..a, g t * ((b - t) ^ 2 / 2) :=
      intervalIntegral.integral_symm (μ := volume)
        (f := fun t => g t * ((b - t) ^ 2 / 2)) b a
    have huIcc : Set.uIcc b a = Set.uIcc a b := Set.uIcc_comm b a
    have hsub : Set.Icc b a ⊆ Set.uIcc a b := by
      rw [← huIcc, Set.uIcc_of_le hab]
    have hprod' : IntervalIntegrable (fun t => g t * ((b - t) ^ 2 / 2)) volume b a :=
      hprod.symm
    have hMint' : IntervalIntegrable (fun t => M * ((b - t) ^ 2 / 2)) volume b a :=
      hMint.symm
    have hmMint' : IntervalIntegrable (fun t => -M * ((b - t) ^ 2 / 2)) volume b a :=
      hmMint.symm
    have hMval' : (∫ t in b..a, M * ((b - t) ^ 2 / 2)) = -(M * ((b - a) ^ 3 / 6)) := by
      rw [intervalIntegral.integral_symm, hMval]
    have hmMval' : (∫ t in b..a, -M * ((b - t) ^ 2 / 2)) = -(-M * ((b - a) ^ 3 / 6)) := by
      rw [intervalIntegral.integral_symm, hmMval]
    have hup : (∫ t in b..a, g t * ((b - t) ^ 2 / 2))
        ≤ ∫ t in b..a, M * ((b - t) ^ 2 / 2) := by
      refine intervalIntegral.integral_mono_on hab hprod' hMint' (fun x hx => ?_)
      have hb := (abs_le.mp (hg x (hsub hx))).2
      have hw : (0 : ℝ) ≤ (b - x) ^ 2 / 2 := by positivity
      nlinarith
    have hlo : (∫ t in b..a, -M * ((b - t) ^ 2 / 2))
        ≤ ∫ t in b..a, g t * ((b - t) ^ 2 / 2) := by
      refine intervalIntegral.integral_mono_on hab hmMint' hprod' (fun x hx => ?_)
      have hb := (abs_le.mp (hg x (hsub hx))).1
      have hw : (0 : ℝ) ≤ (b - x) ^ 2 / 2 := by positivity
      nlinarith
    rw [hMval'] at hup
    rw [hmMval'] at hlo
    -- `abs_of_nonpos` gives `-(b−a)`, which is not defeq to `a−b`; ascribing the
    -- `a−b` form directly leaves the `?x ≤ 0` side goal a metavariable.
    have habs : |b - a| = a - b := by
      rw [abs_of_nonpos (by linarith : b - a ≤ 0)]; ring
    have hcube : (b - a) ^ 3 = -((a - b) ^ 3) := by ring
    rw [hflip, abs_neg, abs_le, habs]
    constructor <;> linarith

/-- **Taylor to second order, integral remainder.**  One FTC against
`F t = f t + f₁ t (b−t) + f₂ t (b−t)²/2`. -/
theorem taylor_two_integral_remainder {f f₁ f₂ f₃ : ℝ → ℝ} {a b : ℝ}
    (hf : ∀ x ∈ Set.uIcc a b, HasDerivAt f (f₁ x) x)
    (hf1 : ∀ x ∈ Set.uIcc a b, HasDerivAt f₁ (f₂ x) x)
    (hf2 : ∀ x ∈ Set.uIcc a b, HasDerivAt f₂ (f₃ x) x)
    (hc : ContinuousOn f₃ (Set.uIcc a b)) :
    f b = f a + f₁ a * (b - a) + f₂ a * ((b - a) ^ 2 / 2)
      + ∫ t in a..b, f₃ t * ((b - t) ^ 2 / 2) := by
  have hF : ∀ x ∈ Set.uIcc a b,
      HasDerivAt (fun s : ℝ => f s + f₁ s * (b - s) + f₂ s * ((b - s) ^ 2 / 2))
        (f₃ x * ((b - x) ^ 2 / 2)) x := by
    intro x hx
    have hbx : HasDerivAt (fun s : ℝ => b - s) (-1) x := by
      simpa using (hasDerivAt_id x).const_sub b
    have hbx2 : HasDerivAt (fun s : ℝ => (b - s) ^ 2 / 2) (-(b - x)) x := by
      have h2 : HasDerivAt (fun s : ℝ => (b - s) ^ 2) (2 * (b - x) * (-1)) x := by
        simpa using hbx.pow 2
      have := h2.div_const 2
      convert this using 1
      ring
    have hterm := ((hf x hx).add ((hf1 x hx).mul hbx)).add ((hf2 x hx).mul hbx2)
    convert hterm using 1
    ring
  have hwc : ContinuousOn (fun t : ℝ => (b - t) ^ 2 / 2) (Set.uIcc a b) := by fun_prop
  have hint : IntervalIntegrable (fun x => f₃ x * ((b - x) ^ 2 / 2)) volume a b :=
    (hc.mul hwc).intervalIntegrable ..
  have hftc := integral_eq_sub_of_hasDerivAt hF hint
  -- `F b = f b`: the `(b−b)` factors vanish, so only the `a` end survives
  simp only [sub_self, mul_zero, ne_eq, OfNat.ofNat_ne_zero, not_false_eq_true,
    zero_pow, zero_div, add_zero] at hftc
  linarith [hftc]

/-- **Taylor to second order, with an explicit `O(|b−a|³)` bound.** -/
theorem abs_taylor_two_le {f f₁ f₂ f₃ : ℝ → ℝ} {a b M : ℝ}
    (hf : ∀ x ∈ Set.uIcc a b, HasDerivAt f (f₁ x) x)
    (hf1 : ∀ x ∈ Set.uIcc a b, HasDerivAt f₁ (f₂ x) x)
    (hf2 : ∀ x ∈ Set.uIcc a b, HasDerivAt f₂ (f₃ x) x)
    (hc : ContinuousOn f₃ (Set.uIcc a b))
    (hM : ∀ x ∈ Set.uIcc a b, |f₃ x| ≤ M) :
    |f b - (f a + f₁ a * (b - a) + f₂ a * ((b - a) ^ 2 / 2))|
      ≤ M * |b - a| ^ 3 / 6 := by
  have hid := taylor_two_integral_remainder hf hf1 hf2 hc
  have hsub : f b - (f a + f₁ a * (b - a) + f₂ a * ((b - a) ^ 2 / 2))
      = ∫ t in a..b, f₃ t * ((b - t) ^ 2 / 2) := by linarith [hid]
  rw [hsub]
  exact abs_integral_sq_weight_mul_le hM hc

end QOU.MathlibExt
