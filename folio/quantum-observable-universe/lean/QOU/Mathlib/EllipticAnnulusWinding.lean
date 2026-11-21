import Mathlib.MeasureTheory.Integral.CircleIntegral
import QOU.Mathlib.ArgumentPrincipleAnnulus
import Mathlib.MeasureTheory.Integral.IntervalIntegral.Periodic
import Mathlib.Analysis.Calculus.LogDeriv
import Mathlib.Analysis.Calculus.Deriv.CompMul
import Mathlib.Analysis.SpecialFunctions.Complex.Arg

/-!
# QOU.Mathlib.EllipticAnnulusWinding — step 3 of Liouville's third theorem

Bean `qou-z4jb`. For a function invariant under the dilation `w ↦ p w` on `ℂ*`
(which `QOU.Mathlib.EllipticAnnulusDescent.annulusPullback_mul` gives for the
pull-back of an elliptic function), the circle integrals of `g'/g` over
`|z| = ρ` and `|z| = ‖p‖ ρ` agree. Fed into the annulus argument principle this
makes zeros minus poles in a fundamental annulus vanish.

* `circleIntegral_scale_complex` — `∮_{|z|=‖a‖R} f = ∮_{|z|=R} a f(a z)` for complex
  `a ≠ 0`. Mathlib v4.24.0 has no change of variables for `circleIntegral`; the
  corpus had the real-scaling case only (`QOU.QBeta.C1Poles.circleIntegral_scale`).
* `logDeriv_dilation`, `circleIntegral_logDeriv_dilation`.

Sorry-free.
-/

open Complex Real

namespace QOU.Mathlib.EllipticAnnulusWinding

/-- **Complex change of variables on a circle.** For `a ≠ 0`,
`∮_{|z| = ‖a‖ R} f = ∮_{|z| = R} a · f (a z)`. The real-scaling case is
`QOU.QBeta.C1Poles.circleIntegral_scale`; the rotation by `arg a` is absorbed by
`2π`-periodicity of the integrand in the angle. -/
theorem circleIntegral_scale_complex (f : ℂ → ℂ) {a : ℂ} (ha : a ≠ 0) (R : ℝ) :
    (∮ z in C(0, ‖a‖ * R), f z) = ∮ z in C(0, R), a * f (a * z) := by
  have hb : a * exp (-(arg a * I)) = (‖a‖ : ℂ) := by
    have ha' : (‖a‖ : ℂ) * exp (arg a * I) = a := norm_mul_exp_arg_mul_I a
    nth_rewrite 1 [← ha']
    rw [mul_assoc, ← Complex.exp_add, add_neg_cancel, Complex.exp_zero, mul_one]
  have hrot : ∀ θ : ℝ, circleMap 0 (‖a‖ * R) θ = a * circleMap 0 R (θ - arg a) := by
    intro θ
    simp only [circleMap, zero_add, ofReal_mul, ofReal_sub]
    rw [sub_mul, Complex.exp_sub, ← hb, Complex.exp_neg]
    field_simp
  set G : ℝ → ℂ := fun θ => deriv (circleMap 0 R) θ • (a * f (a * circleMap 0 R θ)) with hG
  have hper : Function.Periodic G (2 * π) := by
    intro θ
    simp only [hG, deriv_circleMap, periodic_circleMap 0 R θ]
  have hlhs : (∮ z in C(0, ‖a‖ * R), f z) = ∫ θ in (0:ℝ)..2 * π, G (θ - arg a) := by
    simp only [circleIntegral]
    refine intervalIntegral.integral_congr fun θ _ => ?_
    simp only [hG, deriv_circleMap, smul_eq_mul, hrot θ]
    ring
  rw [hlhs, intervalIntegral.integral_comp_sub_right, zero_sub,
    show 2 * π - arg a = -arg a + 2 * π by ring, hper.intervalIntegral_add_eq (-arg a) 0,
    zero_add]
  rfl

/-- Dilation invariance passes to the logarithmic derivative:
if `g (p w) = g w` for all `w ≠ 0`, then `p · (g'/g)(p z) = (g'/g)(z)` for `z ≠ 0`. -/
theorem logDeriv_dilation {g : ℂ → ℂ} {p : ℂ} (hinv : ∀ w, w ≠ 0 → g (p * w) = g w)
    {z : ℂ} (hz : z ≠ 0) : p * logDeriv g (p * z) = logDeriv g z := by
  have heq : (fun w => g (p * w)) =ᶠ[nhds z] g := by
    filter_upwards [isOpen_ne.mem_nhds hz] with w hw using hinv w hw
  have hd : deriv g z = p * deriv g (p * z) := by
    rw [← heq.deriv_eq, deriv_comp_mul_left, smul_eq_mul]
  rw [logDeriv_apply, logDeriv_apply, hd, hinv z hz, mul_div_assoc]

/-- **The winding identity.** For `g` invariant under `w ↦ p w` on `ℂ*`,
`∮_{|z| = ‖p‖ ρ} g'/g = ∮_{|z| = ρ} g'/g` for `ρ > 0`. -/
theorem circleIntegral_logDeriv_dilation {g : ℂ → ℂ} {p : ℂ} (hp : p ≠ 0)
    (hinv : ∀ w, w ≠ 0 → g (p * w) = g w) {ρ : ℝ} (hρ : 0 < ρ) :
    (∮ z in C(0, ‖p‖ * ρ), logDeriv g z) = ∮ z in C(0, ρ), logDeriv g z := by
  rw [circleIntegral_scale_complex _ hp]
  refine circleIntegral.integral_congr hρ.le fun z hz => ?_
  have hz0 : z ≠ 0 := by
    intro h; rw [h] at hz; simp at hz; linarith
  exact logDeriv_dilation hinv hz0

open QOU.Mathlib.ArgumentPrincipleAnnulus in
/-- **Degree zero on a fundamental annulus.** If `g` is meromorphic on `ℂ*` and
invariant under `w ↦ p w` with `‖p‖ > 1`, and the two circles `|w| = ρ`,
`|w| = ‖p‖ρ` carry no zero, pole or removable irregularity of `g`, then the
divisor of `g` sums to `0` over the open annulus `ρ < |w| < ‖p‖ρ`:
the annulus argument principle turns the sum into the difference of the two
circle integrals of `g'/g`, which `circleIntegral_logDeriv_dilation` makes `0`. -/
theorem annulus_divisor_sum_eq_zero {g : ℂ → ℂ} {p : ℂ} (hp : 1 < ‖p‖) {ρ : ℝ} (hρ : 0 < ρ)
    (hmero : ∀ w, w ≠ 0 → MeromorphicAt g w)
    (hinv : ∀ w, w ≠ 0 → g (p * w) = g w)
    (S : Finset ℂ)
    (hbd : ∀ z, (‖z‖ = ρ ∨ ‖z‖ = ‖p‖ * ρ) → AnalyticAt ℂ g z ∧ g z ≠ 0)
    (hS : (S : Set ℂ) = {z | (ρ < ‖z‖ ∧ ‖z‖ < ‖p‖ * ρ) ∧
        (MeromorphicOn.divisor g (closedAnnulus ρ (‖p‖ * ρ))) z ≠ 0}) :
    ∑ w ∈ S, (MeromorphicOn.divisor g (closedAnnulus ρ (‖p‖ * ρ))) w = 0 := by
  have hp0 : p ≠ 0 := by
    intro h; rw [h, norm_zero] at hp; linarith
  have hlt : ρ < ‖p‖ * ρ := by nlinarith
  have hK : MeromorphicOn g (closedAnnulus ρ (‖p‖ * ρ)) := by
    intro z hz
    apply hmero z
    intro h0
    have := (mem_closedAnnulus.mp hz).1
    rw [h0, norm_zero] at this; linarith
  have hAP := argument_principle_annulus hρ hlt hK S hbd hS
  rw [circleIntegral_logDeriv_dilation hp0 hinv hρ, sub_self, mul_zero] at hAP
  exact_mod_cast hAP.symm

end QOU.Mathlib.EllipticAnnulusWinding
