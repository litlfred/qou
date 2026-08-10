import QOU.QBeta.FiveTwoRootStructure

/-!
# The branch pinning, end to end: `Σⱼ log(1 − x·yⱼ) = log x`

Bean `qou-trns`. `FiveTwoEnvelopeSum` proved `exp(Σⱼ log(1 − x·yⱼ) − log x) = 1`
from Vieta alone, and `FiveTwoArgSector` proved that the branch integer vanishes
*given* a bound on `Σⱼ arg(1 − x·yⱼ)`. Between them sat a step nobody had
written: **taking imaginary parts.** This file writes it, and closes the pinning.

## The step

`Complex.exp_eq_one_iff` turns `exp(A − log x) = 1` into `A − log x = n·(2πi)`
for an integer `n`. Its imaginary part is

    Im A = arg x + 2π·n,

and `Im(log w) = arg w` makes the left side `Σⱼ arg(1 − x·yⱼ)` — exactly the
shape `branchInt_eq_zero_of_sector` consumes. Once `n = 0`, the *original*
equation gives `A = log x` outright: no need to recover the real part
separately, which is the small trick that makes this clean.

## What it costs

Nothing beyond Mathlib. The content was already there on both sides; the gap
was that neither end had been connected to the other, and a chain of proved
lemmas with an unwritten join is not a proof. Recorded here rather than folded
silently into a larger file, because "assembly of proved parts" is exactly the
phrase under which a missing step hides.

**The 5₂ sum rule is PROVED**: `QOU.QBeta.FiveTwoComplexPentagon.fiveTwo_saddle_sum_rule`
and `fiveTwoSaddleSumRule_holds`, sorry-free, standard axioms.
-/

namespace QOU.QBeta.FiveTwoDeformedSaddle

open Real Complex

/-! ### 1. Imaginary parts -/

/-- **`exp(A − log x) = 1` pins `Im A` to `arg x` modulo `2π`.** -/
theorem exists_int_im_eq {A x : ℂ} (h : Complex.exp (A - Complex.log x) = 1) :
    ∃ k : ℤ, A - Complex.log x = k * (2 * π * Complex.I) ∧ A.im = x.arg + 2 * π * k := by
  obtain ⟨n, hn⟩ := Complex.exp_eq_one_iff.mp h
  refine ⟨n, hn, ?_⟩
  -- rewrite the numeral away before taking components
  have hrw : (n : ℂ) * (2 * (π : ℂ) * Complex.I) = ((2 * π * n : ℝ) : ℂ) * Complex.I := by
    push_cast; ring
  rw [hrw] at hn
  have him := congrArg Complex.im hn
  simp only [Complex.sub_im, Complex.log_im, Complex.mul_im,
    Complex.ofReal_re, Complex.ofReal_im, Complex.I_re, Complex.I_im] at him
  linarith

/-- **And once the integer is `0`, `A = log x`.**

Taken from the *original* equation rather than by recovering the real part —
that is what keeps this short. -/
theorem eq_log_of_branchInt_eq_zero {A x : ℂ} (h : Complex.exp (A - Complex.log x) = 1)
    (hk : ∀ k : ℤ, A.im = x.arg + 2 * π * k → k = 0) : A = Complex.log x := by
  obtain ⟨n, hn, him⟩ := exists_int_im_eq h
  rw [hk n him] at hn
  simpa using sub_eq_zero.mp (by simpa using hn)

/-- The imaginary part of a three-term log-sum is the sum of the arguments. -/
theorem im_logSum (w₁ w₂ w₃ : ℂ) :
    (Complex.log w₁ + Complex.log w₂ + Complex.log w₃).im = w₁.arg + w₂.arg + w₃.arg := by
  simp [Complex.add_im, Complex.log_im]

/-! ### 2. The pinning, end to end -/

/-- **`Σⱼ log(1 − x·yⱼ) = log x`, from Vieta and the sector bound.**

Every hypothesis here is discharged elsewhere in this branch: the Vieta
relations hold on the curve, `t ∈ (0,1)` and the two `Im` conditions come from
`exists_pinning_data`, and `x.arg = φ` holds on the arc. This is the statement
`sum_dVdx_of_pinned` has been waiting on. -/
theorem logSumA_eq_log {x : ℂ} {t : ℝ} {y₂ y₃ : ℂ} {φ : ℝ}
    (hx : x ≠ 0)
    (hb₁ : (1 : ℂ) - x * (t : ℂ) ≠ 0) (hb₂ : (1 : ℂ) - x * y₂ ≠ 0)
    (hb₃ : (1 : ℂ) - x * y₃ ≠ 0)
    (hv₁ : x * ((t : ℂ) + y₂ + y₃) = x ^ 2 + 1)
    (hv₂ : x * ((t : ℂ) * y₂ + (t : ℂ) * y₃ + y₂ * y₃) = x ^ 2 + x + 1)
    (hv₃ : (t : ℂ) * y₂ * y₃ = 1)
    (hxim : 0 < x.im) (hxnorm : x.re ^ 2 + x.im ^ 2 = 1)
    (ht0 : 0 < t) (ht1 : t < 1)
    (h3 : (x * y₃).im ≤ 0) (hbig : π / 2 < φ → (x * y₂).im ≤ 0)
    (hφ0 : 0 ≤ φ) (hφπ : φ < π) (hxarg : x.arg = φ) :
    Complex.log (1 - x * (t : ℂ)) + Complex.log (1 - x * y₂) + Complex.log (1 - x * y₃)
      = Complex.log x := by
  refine eq_log_of_branchInt_eq_zero
    (exp_logSumA_sub_log_eq_one hx hb₁ hb₂ hb₃ hv₁ hv₂ hv₃) ?_
  intro k hk
  rw [im_logSum, hxarg, mul_comm x (t : ℂ)] at hk
  exact branchInt_eq_zero_of_roots (t := t) (y₂ := y₂) (y₃ := y₃)
    hxim hxnorm ht0 ht1 h3 hbig hφ0 hφπ hk

end QOU.QBeta.FiveTwoDeformedSaddle
