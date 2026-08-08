import QOU.QBeta.FiveTwoTransport

/-!
# The level-7 bridge: the correction is `−π²`, and it is one `arg`

Bean `qou-trns`. The transport gives `S(π) − S(0) = π²`, and `S(0)` **is** the 5₂
sum rule (`−3π²/2`, Route 32). So the sum rule reduces to evaluating `S(π)`,
which sits at `x = −1` where the curve's cubic is

    unitCubic (−1) y = y³ + 2y² − y − 1 ,

the **level-7** cubic. There `V(−1, y) = Li₂(y) + 2·Li₂(−y) + log(−y)²`, and the
already-proved cyclotomic identity `extended_sum` reads
`Σⱼ Re[2L(−yⱼ) + L(yⱼ)] = +π²/2` once `wₖ = −yⱼ` — which it does, exactly.

What separates the two is a log-bilinear correction with **no dilogarithms in
it**:

    corr y = Re[ log(−y)² − log(−y)·log(1+y) − ½·log(y)·log(1−y) ] .

Route 32 measures `Σⱼ corr yⱼ = −π²` to `2e-50`. This file proves it.

## Why it collapses

Per root, the log-times-log part factors as

    log|y| · ( log|y| − log|1+y| − ½·log(1−y) )

and the second factor vanishes because

    2·log|y| = 2·log|1+y| + log(1−y)   ⟺   y² = (1+y)²(1−y)
                                        ⟺   y³ + 2y² − y − 1 = 0 ,

**which is the cubic itself** (`sq_eq_of_root`). So every root contributes
nothing from the logarithms.

What is left is arguments. At a **negative** root every factor's argument
cancels out of the real part, giving `0`. At the unique **positive** root
`t ∈ (0,1)`, `−t` is a negative real, `log(−t) = log t + iπ`, and
`Re[log(−t)²] = (log t)² − π²` contributes a bare `−π²`.

So the entire correction is **one argument at one root** — the same `−t`-on-the-
cut that produced corrections 5 and 6 in this branch. Third appearance, and this
time it is not a defect but the answer.

## What this does and does not close

It closes the arithmetic between `S(π)` and `extended_sum`. It does **not**
close the sum rule: `extended_sum` is stated for the corpus's piecewise
`extend`, and identifying that with `Re` of the analytic Rogers `L` is
`qou-rstq` item 4 — open, on paper only, and sitting directly on this bridge.

**The 5₂ sum rule remains verified to 80 dps, unproved.**
-/

namespace QOU.QBeta.FiveTwoDeformedSaddle

open Real Complex

/-! ### 1. The cubic *is* the log relation -/

/-- **`y² = (1+y)²(1−y)` is the level-7 cubic**, on the nose. -/
theorem sq_eq_of_root {y : ℝ} (hy : y ^ 3 + 2 * y ^ 2 - y - 1 = 0) :
    y ^ 2 = (1 + y) ^ 2 * (1 - y) := by linear_combination hy

/-- The level-7 cubic is `unitCubic (−1)` — the curve at `x = −1`, the endpoint
of the transport arc. -/
theorem levelSeven_eq_unitCubic (y : ℝ) : unitCubic (-1) y = y ^ 3 + 2 * y ^ 2 - y - 1 := by
  unfold unitCubic; ring

/-- **The log relation at a root.** `Real.log` is even in Mathlib, so this is the
statement for `|y|` and `|1+y|` without writing the bars. -/
theorem log_rel_of_root {y : ℝ} (hy : y ^ 3 + 2 * y ^ 2 - y - 1 = 0)
    (hy0 : y ≠ 0) (hy1 : 1 + y ≠ 0) (h1y : (1 : ℝ) - y ≠ 0) :
    2 * Real.log y = 2 * Real.log (1 + y) + Real.log (1 - y) := by
  have h := congrArg Real.log (sq_eq_of_root hy)
  rw [Real.log_pow, Real.log_mul (pow_ne_zero 2 hy1) h1y, Real.log_pow] at h
  push_cast at h
  linarith

/-! ### 2. The correction, per root -/

/-- The log-bilinear correction at a real root:
`Re[log(−y)² − log(−y)·log(1+y) − ½·log(y)·log(1−y)]`. No dilogarithms. -/
noncomputable def corr (y : ℝ) : ℝ :=
  (Complex.log (-(y : ℂ)) ^ 2 - Complex.log (-(y : ℂ)) * Complex.log (1 + (y : ℂ))
    - Complex.log (y : ℂ) * Complex.log (1 - (y : ℂ)) / 2).re

theorem log_ofReal_pos {r : ℝ} (hr : 0 < r) : Complex.log (r : ℂ) = ((Real.log r : ℝ) : ℂ) :=
  (Complex.ofReal_log hr.le).symm

/-- **At the positive root the correction is `−π²`** — and all of it comes from
`arg(−t) = π`, since the logarithms cancel by `log_rel_of_root`. -/
theorem corr_of_pos_root {y : ℝ} (hy : y ^ 3 + 2 * y ^ 2 - y - 1 = 0)
    (h0 : 0 < y) (h1 : y < 1) : corr y = -π ^ 2 := by
  have e₁ : Complex.log (-(y : ℂ)) = ((Real.log y : ℝ) : ℂ) + (Real.pi : ℂ) * Complex.I :=
    log_neg_ofReal h0
  have e₂ : Complex.log (1 + (y : ℂ)) = ((Real.log (1 + y) : ℝ) : ℂ) := by
    have : (1 : ℂ) + (y : ℂ) = ((1 + y : ℝ) : ℂ) := by push_cast; ring
    rw [this, log_ofReal_pos (by linarith)]
  have e₃ : Complex.log (y : ℂ) = ((Real.log y : ℝ) : ℂ) := log_ofReal_pos h0
  have e₄ : Complex.log (1 - (y : ℂ)) = ((Real.log (1 - y) : ℝ) : ℂ) := by
    have : (1 : ℂ) - (y : ℂ) = ((1 - y : ℝ) : ℂ) := by push_cast; ring
    rw [this, log_ofReal_pos (by linarith)]
  have hrel := log_rel_of_root hy (by linarith) (by linarith) (by linarith)
  unfold corr
  rw [e₁, e₂, e₃, e₄]
  simp only [Complex.sub_re, Complex.div_re, Complex.mul_re, Complex.mul_im, Complex.add_re,
    Complex.add_im, Complex.ofReal_re, Complex.ofReal_im, Complex.I_re, Complex.I_im,
    Complex.normSq_apply, pow_two]
  norm_num
  linear_combination (Real.log y / 2) * hrel

/-- **At a negative root the correction is `0`.** Every argument drops out of the
real part, and the logarithms cancel by the same relation. -/
theorem corr_of_neg_root {y : ℝ} (hy : y ^ 3 + 2 * y ^ 2 - y - 1 = 0)
    (h0 : y < 0) (h1 : 1 + y ≠ 0) : corr y = 0 := by
  have hny : 0 < -y := by linarith
  have e₁ : Complex.log (-(y : ℂ)) = ((Real.log (-y) : ℝ) : ℂ) := by
    have : -(y : ℂ) = ((-y : ℝ) : ℂ) := by push_cast; ring
    rw [this, log_ofReal_pos hny]
  have e₃ : Complex.log (y : ℂ) = ((Real.log (-y) : ℝ) : ℂ) + (Real.pi : ℂ) * Complex.I := by
    have : (y : ℂ) = -((-y : ℝ) : ℂ) := by push_cast; ring
    rw [this, log_neg_ofReal hny]
  have e₄ : Complex.log (1 - (y : ℂ)) = ((Real.log (1 - y) : ℝ) : ℂ) := by
    have : (1 : ℂ) - (y : ℂ) = ((1 - y : ℝ) : ℂ) := by push_cast; ring
    rw [this, log_ofReal_pos (by linarith)]
  have hrel := log_rel_of_root hy (by linarith) h1 (by linarith)
  have hlogeq : Real.log (-y) = Real.log y := Real.log_neg_eq_log y
  rcases lt_trichotomy (1 + y) 0 with hs | hs | hs
  · -- `1 + y < 0`: its argument is `π`, but `log(−y)` is real so it drops out
    have e₂ : Complex.log (1 + (y : ℂ))
        = ((Real.log (-(1 + y)) : ℝ) : ℂ) + (Real.pi : ℂ) * Complex.I := by
      have : (1 : ℂ) + (y : ℂ) = -((-(1 + y) : ℝ) : ℂ) := by push_cast; ring
      rw [this, log_neg_ofReal (by linarith)]
    have h2 : Real.log (-y + -1) = Real.log (1 + y) := by
      rw [show (-y + -1 : ℝ) = -(1 + y) by ring]
      exact Real.log_neg_eq_log (1 + y)
    unfold corr
    rw [e₁, e₂, e₃, e₄]
    simp only [Complex.sub_re, Complex.div_re, Complex.mul_re, Complex.mul_im, Complex.add_re,
      Complex.add_im, Complex.ofReal_re, Complex.ofReal_im, Complex.I_re, Complex.I_im,
      Complex.normSq_apply, pow_two]
    norm_num
    linear_combination (Real.log y / 2) * hrel - Real.log y * h2
  · exact absurd hs h1
  · have e₂ : Complex.log (1 + (y : ℂ)) = ((Real.log (1 + y) : ℝ) : ℂ) := by
      have : (1 : ℂ) + (y : ℂ) = ((1 + y : ℝ) : ℂ) := by push_cast; ring
      rw [this, log_ofReal_pos hs]
    unfold corr
    rw [e₁, e₂, e₃, e₄]
    simp only [Complex.sub_re, Complex.div_re, Complex.mul_re, Complex.mul_im, Complex.add_re,
      Complex.add_im, Complex.ofReal_re, Complex.ofReal_im, Complex.I_re, Complex.I_im,
      Complex.normSq_apply, pow_two]
    norm_num
    linear_combination (Real.log y / 2) * hrel

/-! ### 3. The bridge -/

/-- **`Σⱼ corr yⱼ = −π²`.**

One positive root contributes `−π²`, two negative roots contribute nothing. That
is the entire gap between `Σⱼ Re V(−1, yⱼ)` and the proved
`Σⱼ Re[2L(−yⱼ) + L(yⱼ)] = π²/2`, and it makes `S(π) = π²/2 − π² = −π²/2`. -/
theorem corr_sum_eq_neg_pi_sq {y₁ y₂ y₃ : ℝ}
    (h₁ : y₁ ^ 3 + 2 * y₁ ^ 2 - y₁ - 1 = 0)
    (h₂ : y₂ ^ 3 + 2 * y₂ ^ 2 - y₂ - 1 = 0)
    (h₃ : y₃ ^ 3 + 2 * y₃ ^ 2 - y₃ - 1 = 0)
    (hp : 0 < y₁) (hp' : y₁ < 1) (hn₂ : y₂ < 0) (hn₃ : y₃ < 0)
    (hne₂ : 1 + y₂ ≠ 0) (hne₃ : 1 + y₃ ≠ 0) :
    corr y₁ + corr y₂ + corr y₃ = -π ^ 2 := by
  rw [corr_of_pos_root h₁ hp hp', corr_of_neg_root h₂ hn₂ hne₂,
    corr_of_neg_root h₃ hn₃ hne₃]
  ring

/-! ### 4. Non-vacuity -/

/-- **Non-vacuity.** The level-7 cubic really does have one root in `(0,1)` and
two negative ones — reusing `FiveTwoRootStructure` at `c = −1`, where
`unitCubic (−1)` *is* this cubic. So `corr_sum_eq_neg_pi_sq` is not about an
empty configuration. -/
theorem levelSeven_has_pos_root : ∃ t ∈ Set.Ioo (0 : ℝ) 1, t ^ 3 + 2 * t ^ 2 - t - 1 = 0 := by
  obtain ⟨t, ht, h⟩ := exists_root_mem_Ioo (-1)
  exact ⟨t, ht, by rwa [levelSeven_eq_unitCubic] at h⟩

/-- And every other real root is negative — `real_root_neg_of_ne` at `c = −1`. -/
theorem levelSeven_other_roots_neg {t r : ℝ} (ht0 : 0 < t) (ht1 : t < 1)
    (hpt : t ^ 3 + 2 * t ^ 2 - t - 1 = 0) (hpr : r ^ 3 + 2 * r ^ 2 - r - 1 = 0)
    (hne : r ≠ t) : r < 0 :=
  real_root_neg_of_ne (c := -1) (by norm_num) ht0 ht1
    (by rwa [levelSeven_eq_unitCubic]) (by rwa [levelSeven_eq_unitCubic]) hne

end QOU.QBeta.FiveTwoDeformedSaddle
