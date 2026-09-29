/-
  The law of sines for an ideal tetrahedron: `‖z‖ = sin θ₂ / sin θ₃`.

  Bean `qou-kmmr`, third increment — the crux of the **radial reduction** that
  takes Kummer's identity from `|z| = 1` to general `z`.

  ═══ WHY THIS IS THE KEY LEMMA ═══

  Kummer for general `z` looks like it needs a genuine two-variable argument
  (`dD = log|z| d arg(1−z) − log|1−z| d arg z` against
  `dΛ(θ) = −log|2 sin θ| dθ`).  It does not — it reduces to **one** variable, by
  fixing `arg z` and varying `|z|` along a ray.  Along such a ray:

  * `θ₁ = arg z` is **constant**, so `Λ(θ₁)` contributes nothing;
  * `θ₁ + θ₂ + θ₃ = π` (`tetAngles_sum_eq_pi`) then forces `dθ₃ = −dθ₂`;
  * so `d/dr (Λ(θ₂) + Λ(θ₃)) = log(sin θ₃ / sin θ₂) · dθ₂/dr`;
  * and on the dilogarithm side `d/dr D = −log r · dθ₂/dr`.

  Those two agree **iff** `r = sin θ₂ / sin θ₃`, which is exactly this file.  The
  basepoint `r = 1` is then supplied by `KummerDilogHalf.kummer_unit_circle`,
  already proved.  So this lemma is what converts a two-variable problem into the
  same "same derivative, pin the constant" shape the rest of this lane uses.

  **That programme is now carried out**: `QOU/Knot/KummerRadial.lean` proves
  Kummer for general `z` (`kummer`), and this lemma is the step that makes the
  two sides' derivatives agree.

  ═══ THE PROOF ═══

  Entirely elementary, via `Complex.sin_arg : sin (arg x) = x.im / ‖x‖` — which
  is *unconditional* in Mathlib, so no `x ≠ 0` bookkeeping is needed for the sine
  computations themselves:

      sin θ₂ = z.im / ‖1 − z‖,        sin θ₃ = z.im / (‖z‖ · ‖1 − z‖)

  and the ratio is `‖z‖` on the nose.  Note both sines are **positive** on the
  upper half plane, which is what makes the division safe.

  Numerically checked at five shapes including the 5₂ shape `y₁` before being
  stated: `‖y₁‖ = 1.524702579929852 = sin θ₂ / sin θ₃` exactly.

  -- Ref: [thurston1978], [neumann-zagier1985]
-/
import QOU.Archimedean.BlochWignerLobachevsky

namespace QOU.Knot.IdealTet

open Real Complex QOU.Archimedean

variable {z : ℂ}

/-- On the upper half plane, `1 − z ≠ 0`. -/
theorem one_sub_ne_zero (hz : 0 < z.im) : (1 : ℂ) - z ≠ 0 := by
  intro h
  have : z = 1 := by linear_combination -h
  rw [this] at hz; simp at hz

/-- On the upper half plane, `z ≠ 0`. -/
theorem ne_zero_of_im_pos (hz : 0 < z.im) : z ≠ 0 := by
  intro h; rw [h] at hz; simp at hz

/-! ### The two sines -/

/-- `sin θ₂ = Im z / ‖1 − z‖`. -/
theorem sin_tetAngle₂ (hz : 0 < z.im) :
    Real.sin (tetAngle₂ z) = z.im / ‖1 - z‖ := by
  have h1z : (1 : ℂ) - z ≠ 0 := one_sub_ne_zero hz
  have hn : ‖(1 : ℂ) - z‖ ≠ 0 := norm_ne_zero_iff.mpr h1z
  unfold tetAngle₂
  rw [Complex.sin_arg, one_div, Complex.inv_im, norm_inv]
  rw [Complex.normSq_eq_norm_sq]
  field_simp
  simp

/-- `sin θ₃ = Im z / (‖z‖ · ‖1 − z‖)`. -/
theorem sin_tetAngle₃ (hz : 0 < z.im) :
    Real.sin (tetAngle₃ z) = z.im / (‖z‖ * ‖1 - z‖) := by
  have hz0 : z ≠ 0 := ne_zero_of_im_pos hz
  have h1z : (1 : ℂ) - z ≠ 0 := one_sub_ne_zero hz
  have hnz : ‖z‖ ≠ 0 := norm_ne_zero_iff.mpr hz0
  have hn1 : ‖(1 : ℂ) - z‖ ≠ 0 := norm_ne_zero_iff.mpr h1z
  unfold tetAngle₃
  -- `1 - 1/z = (z - 1)/z`, whose imaginary part is `Im z / ‖z‖²`
  have him : ((1 : ℂ) - 1 / z).im = z.im / ‖z‖ ^ 2 := by
    rw [Complex.sub_im, Complex.one_im, one_div, Complex.inv_im,
      Complex.normSq_eq_norm_sq]
    ring
  have hnorm : ‖(1 : ℂ) - 1 / z‖ = ‖(1 : ℂ) - z‖ / ‖z‖ := by
    have hrw : (1 : ℂ) - 1 / z = -((1 - z) / z) := by field_simp; ring
    rw [hrw, norm_neg, norm_div]
  rw [Complex.sin_arg, him, hnorm]
  field_simp

/-! ### Positivity, so the ratio is safe -/

theorem sin_tetAngle₂_pos (hz : 0 < z.im) : 0 < Real.sin (tetAngle₂ z) := by
  rw [sin_tetAngle₂ hz]
  exact div_pos hz (norm_pos_iff.mpr (one_sub_ne_zero hz))

theorem sin_tetAngle₃_pos (hz : 0 < z.im) : 0 < Real.sin (tetAngle₃ z) := by
  rw [sin_tetAngle₃ hz]
  exact div_pos hz (mul_pos (norm_pos_iff.mpr (ne_zero_of_im_pos hz))
    (norm_pos_iff.mpr (one_sub_ne_zero hz)))

/-! ### The law of sines -/

/-- **THE LAW OF SINES FOR AN IDEAL TETRAHEDRON.**

For `Im z > 0`,

    `‖z‖ = sin θ₂ / sin θ₃`

with `θ₂ = arg(1/(1−z))`, `θ₃ = arg(1 − 1/z)`.

This is what makes the radial reduction of Kummer's identity work: along a ray of
constant `arg z`, it is exactly the condition under which the Λ-side and the
dilogarithm side have the same derivative. -/
theorem norm_eq_sin_div_sin (hz : 0 < z.im) :
    ‖z‖ = Real.sin (tetAngle₂ z) / Real.sin (tetAngle₃ z) := by
  have hz0 : z ≠ 0 := ne_zero_of_im_pos hz
  have h1z : (1 : ℂ) - z ≠ 0 := one_sub_ne_zero hz
  have hnz : ‖z‖ ≠ 0 := norm_ne_zero_iff.mpr hz0
  have hn1 : ‖(1 : ℂ) - z‖ ≠ 0 := norm_ne_zero_iff.mpr h1z
  have him : z.im ≠ 0 := ne_of_gt hz
  rw [sin_tetAngle₂ hz, sin_tetAngle₃ hz]
  field_simp

/-- The same, in the product form the derivative computation actually consumes:
`sin θ₂ = ‖z‖ · sin θ₃`. -/
theorem sin_tetAngle₂_eq (hz : 0 < z.im) :
    Real.sin (tetAngle₂ z) = ‖z‖ * Real.sin (tetAngle₃ z) := by
  have h3 := sin_tetAngle₃_pos hz
  rw [norm_eq_sin_div_sin hz]
  field_simp

/-- **The log form**, which is the shape the Λ-derivative produces:
`log(2 sin θ₃) − log(2 sin θ₂) = −log ‖z‖`.

This is precisely the identity that makes the two sides of Kummer agree along a
ray, so it is worth having stated separately. -/
theorem log_sin_sub_log_sin (hz : 0 < z.im) :
    Real.log (2 * Real.sin (tetAngle₃ z)) - Real.log (2 * Real.sin (tetAngle₂ z))
      = -Real.log ‖z‖ := by
  have h2 := sin_tetAngle₂_pos hz
  have h3 := sin_tetAngle₃_pos hz
  have hnz : (0 : ℝ) < ‖z‖ := norm_pos_iff.mpr (ne_zero_of_im_pos hz)
  rw [sin_tetAngle₂_eq hz, show (2 : ℝ) * (‖z‖ * Real.sin (tetAngle₃ z))
      = ‖z‖ * (2 * Real.sin (tetAngle₃ z)) by ring,
    Real.log_mul (ne_of_gt hnz) (by positivity)]
  ring

end QOU.Knot.IdealTet
