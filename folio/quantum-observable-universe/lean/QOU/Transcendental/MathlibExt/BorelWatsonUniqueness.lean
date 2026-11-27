/-
  Watson-uniqueness brick 3 — Phragmén–Lindelöf ⇒ uniqueness (bean el8w tranche 5).

  KEY FINDING: Mathlib ALREADY contains the Phragmén–Lindelöf engine Watson
  uniqueness needs —
  `PhragmenLindelof.eqOn_right_half_plane_of_superexponential_decay`: two
  functions analytic + `O(exp(B‖z‖^c))` (c<2) on the right half-plane, bounded
  on the imaginary axis, whose difference decays SUPEREXPONENTIALLY along the
  positive real axis, are equal on the closed half-plane. So brick 3 is NOT a
  missing Mathlib lemma; it is the WIRING plus one genuine analytic step.

  The genuine step — and the subtle heart of Watson — is the decay STRENGTH.
  Mathlib's `SuperpolynomialDecay atTop expR ‖f·‖` means `exp(n x)·‖f x‖ → 0`
  for every `n`: strictly stronger than a single-sector `exp(−c/|z|)` bound
  (which maps to `exp(−c x)` — only exponential, and NOT enough: `exp(−z)` is a
  P–L counterexample on the exact half-plane). The extra strength is exactly
  what a sector of opening `> π` supplies: it amplifies the Gevrey-1 bound to a
  STRETCHED exponential `exp(−b x^s)`, `s > 1`, which IS superexponential.

  This file proves that amplification bridge (`stretchedExp_superpolynomialDecay`)
  and wires it into the P–L engine (`watson_uniqueness_rhp`), both sorry-free.
  The remaining honest gap for the FULL sector-at-0 Watson statement is the
  change of variables `z ↦ 1/z` that maps a `> π` sector at `0` to this
  half-plane at `∞` (transporting analyticity + the stretched-exp bound); that
  transport is the final assembly, scoped in the el8w tranche 5 bean.

  Archimedean (ℝ, ℂ): genuinely archimedean — `Real.exp`, `Real.rpow`, complex
  analyticity, Phragmén–Lindelöf.

  -- Ref: [sokal1980] https://doi.org/10.1063/1.524408
  -- Ref: [leitner2026] bean el8w tranche 5 — Watson uniqueness brick 3
-/

import Mathlib.Analysis.Complex.PhragmenLindelof
import Mathlib.Analysis.SpecialFunctions.Pow.Asymptotics

namespace QOU.Mathlib.Borel

open Real Filter Asymptotics Complex Bornology
open scoped Topology Real

/-- **Stretched-exponential ⇒ superexponential decay (the `>π`-sector
    amplification).** If `‖f x‖ ≤ C·exp(−b·x^s)` eventually with `b > 0` and
    `s > 1`, then `‖f‖` decays superexponentially: `exp(n x)·‖f x‖ → 0` for
    every `n`. The stretched exponent `s > 1` is precisely what a Watson sector
    of opening `> π` produces, and precisely what upgrades the single-sector
    exponential bound to the strength Phragmén–Lindelöf requires. -/
theorem stretchedExp_superpolynomialDecay {f : ℝ → ℝ} {C b s : ℝ}
    (hb : 0 < b) (hs : 1 < s)
    (hbound : ∀ᶠ x in atTop, |f x| ≤ C * Real.exp (-b * x ^ s)) :
    SuperpolynomialDecay atTop Real.exp (fun x => |f x|) := by
  intro n
  -- exp(n x) · |f x| ≤ C · exp(n x − b x^s), and n x − b x^s → −∞.
  have hdiff : Tendsto (fun x : ℝ => (n : ℝ) * x - b * x ^ s) atTop atBot := by
    -- n x − b x^s ≤ −(b/2) x^s eventually, and −(b/2) x^s → −∞.
    have hs0 : (0 : ℝ) < s := lt_trans one_pos hs
    have hs1 : (0 : ℝ) < s - 1 := by linarith
    have hxs1 : Tendsto (fun x : ℝ => (b / 2) * x ^ (s - 1)) atTop atTop :=
      (tendsto_rpow_atTop hs1).const_mul_atTop (by positivity)
    -- eventually n ≤ (b/2) x^{s-1}, i.e. n x ≤ (b/2) x^s ⇒ n x − b x^s ≤ −(b/2) x^s
    have hev : ∀ᶠ x : ℝ in atTop,
        (n : ℝ) * x - b * x ^ s ≤ -(b / 2) * x ^ s := by
      filter_upwards [hxs1.eventually_ge_atTop (n : ℝ),
        eventually_gt_atTop (0 : ℝ)] with x hx hx0
      have hxs : x ^ (s - 1) * x = x ^ s := by
        rw [Real.rpow_sub_one hx0.ne', div_mul_cancel₀ _ hx0.ne']
      have hnx : (n : ℝ) * x ≤ (b / 2) * x ^ (s - 1) * x :=
        mul_le_mul_of_nonneg_right hx hx0.le
      rw [mul_assoc, hxs] at hnx
      linarith
    have hbig : Tendsto (fun x : ℝ => -(b / 2) * x ^ s) atTop atBot :=
      (tendsto_rpow_atTop hs0).const_mul_atTop_of_neg (show -(b / 2) < 0 by linarith)
    exact tendsto_atBot_mono' _ hev hbig
  have hexp0 : Tendsto (fun x : ℝ => C * Real.exp ((n : ℝ) * x - b * x ^ s))
      atTop (𝓝 0) := by
    have := (Real.tendsto_exp_atBot.comp hdiff)
    simpa using this.const_mul C
  refine squeeze_zero' ?_ ?_ hexp0
  · filter_upwards with x; positivity
  · filter_upwards [hbound] with x hx
    calc Real.exp x ^ n * |f x|
        = Real.exp ((n : ℝ) * x) * |f x| := by
          rw [← Real.exp_nat_mul]
      _ ≤ Real.exp ((n : ℝ) * x) * (C * Real.exp (-b * x ^ s)) := by
          gcongr
      _ = C * Real.exp ((n : ℝ) * x - b * x ^ s) := by
          rw [mul_left_comm, ← Real.exp_add]; congr 1; ring

/-- **Watson uniqueness on the right half-plane.** Two functions analytic on the
    open right half-plane, continuous on its closure, `O(exp(B‖z‖^c))` with
    `c < 2`, and bounded on the imaginary axis, that agree up to a stretched-
    exponential `≤ C·exp(−b·x^s)` (`b>0`, `s>1`) along the positive real axis,
    are equal on the closed right half-plane. A Borel/Watson wrapper of
    `PhragmenLindelof.eqOn_right_half_plane_of_superexponential_decay`, with the
    superexponential hypothesis supplied by `stretchedExp_superpolynomialDecay`.
    This is the uniqueness half of Watson / Nevanlinna–Sokal, realized. -/
theorem watson_uniqueness_rhp {E : Type*} [NormedAddCommGroup E] [NormedSpace ℂ E]
    {f g : ℂ → E} {C b s : ℝ} (hb : 0 < b) (hs : 1 < s)
    (hfd : DiffContOnCl ℂ f {z : ℂ | 0 < z.re})
    (hgd : DiffContOnCl ℂ g {z : ℂ | 0 < z.re})
    (hfexp : ∃ c < (2 : ℝ), ∃ B,
      f =O[cobounded ℂ ⊓ 𝓟 {z : ℂ | 0 < z.re}] fun z => Real.exp (B * ‖z‖ ^ c))
    (hgexp : ∃ c < (2 : ℝ), ∃ B,
      g =O[cobounded ℂ ⊓ 𝓟 {z : ℂ | 0 < z.re}] fun z => Real.exp (B * ‖z‖ ^ c))
    (hfim : ∃ C, ∀ x : ℝ, ‖f (x * Complex.I)‖ ≤ C)
    (hgim : ∃ C, ∀ x : ℝ, ‖g (x * Complex.I)‖ ≤ C)
    (hre : ∀ᶠ x : ℝ in atTop, ‖f (x : ℂ) - g (x : ℂ)‖ ≤ C * Real.exp (-b * x ^ s)) :
    Set.EqOn f g {z : ℂ | 0 ≤ z.re} := by
  refine PhragmenLindelof.eqOn_right_half_plane_of_superexponential_decay
    hfd hgd hfexp hgexp ?_ hfim hgim
  have := stretchedExp_superpolynomialDecay
    (f := fun x : ℝ => ‖f (x : ℂ) - g (x : ℂ)‖) hb hs
    (by filter_upwards [hre] with x hx; rwa [abs_of_nonneg (norm_nonneg _)])
  simpa using this

end QOU.Mathlib.Borel
