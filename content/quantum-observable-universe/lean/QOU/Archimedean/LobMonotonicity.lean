/-
  Monotonicity of the Lobachevsky function `Λ`, from the sign of `Λ′`.

  WHY THIS EXISTS.  `qou-52ch` reduces `Vol(4₁) < Vol(5₂)` to a chord bound under
  Rivin concavity, and the chord's far point needs `Λ(a₁) + Λ(a₂) + Λ(a₃) ≥ 0` at
  one specific interior triple.  Using `Lob_pi_sub` to fold the obtuse angle,

      Λ(a₁) + Λ(a₂) + Λ(a₃) = (Λ(a₁) − Λ(a₁ + a₃)) + Λ(a₃),

  so the whole thing follows from `Λ` DECREASING past `π/6` together with the
  corpus's existing `Lob_nonneg_of_lt_pi_div_two`.  No value of `Λ` is needed —
  which is the point of the `qou-52ch` reduction, and would be lost if this were
  done by bounding `Λ` numerically instead.

  THE MATHLIB GAP.  Mathlib has no `Λ`; the corpus supplies it and already proves
  `Λ′(t) = −log(2 sin t)` (`QOU.Knot.Rivin.hasDerivAt_Lob`, sorry-free).  What was
  missing is the one-line consequence: `Λ′ < 0` exactly where `2 sin t > 1`, i.e.
  on `(π/6, 5π/6)`, so `Λ` is strictly decreasing there.

  Archimedean (ℝ): ordering, `sin`, `log` — §7c.

  -- Ref: [milnor1982] Hyperbolic geometry: the first 150 years
  -- Ref: [manuscript] bean qou-52ch
-/

import QOU.Knot.RivinConcavity
import QOU.Knot.LobNearZero

namespace QOU.Archimedean.LobMonotonicity

open Real Set QOU.Archimedean

/-- `2 sin t > 1` on `(π/6, 5π/6)` — the exact locus where `Λ′ < 0`. -/
theorem one_lt_two_mul_sin {t : ℝ} (h0 : π / 6 < t) (h1 : t < 5 * π / 6) :
    1 < 2 * Real.sin t := by
  have hpi := Real.pi_pos
  have key : (1 : ℝ) / 2 < Real.sin t := by
    rcases le_or_gt t (π / 2) with h | h
    · -- on the rising branch: `sin` is strictly mono on `[-π/2, π/2]`
      have := Real.strictMonoOn_sin (a := π / 6) (b := t)
        ⟨by linarith, by linarith⟩ ⟨by linarith, by linarith⟩ h0
      rwa [Real.sin_pi_div_six] at this
    · -- past `π/2`, reflect: `sin t = sin (π - t)` and `π - t < 5π/6`
      have hrefl : Real.sin t = Real.sin (π - t) := (Real.sin_pi_sub t).symm
      have := Real.strictMonoOn_sin (a := π / 6) (b := π - t)
        ⟨by linarith, by linarith⟩ ⟨by linarith, by linarith⟩ (by linarith)
      rw [Real.sin_pi_div_six] at this
      linarith [hrefl ▸ this]
  linarith

/-- `Λ′(t) < 0` on `(π/6, 5π/6)`. -/
theorem deriv_Lob_neg {t : ℝ} (h0 : π / 6 < t) (h1 : t < 5 * π / 6) :
    deriv Lob t < 0 := by
  have hpi := Real.pi_pos
  have hd := QOU.Knot.Rivin.hasDerivAt_Lob (t := t) (by linarith) (by linarith)
  rw [hd.deriv]
  have := one_lt_two_mul_sin h0 h1
  have : 0 < Real.log (2 * Real.sin t) := Real.log_pos this
  linarith

/-- **`Λ` is strictly decreasing on `[π/6, 5π/6]`.**

This is the fact `qou-52ch`'s chord argument needs, and it is a statement about
the SIGN of `Λ′`, never about a value of `Λ`. -/
theorem strictAntiOn_Lob :
    StrictAntiOn Lob (Icc (π / 6) (5 * π / 6)) := by
  refine strictAntiOn_of_deriv_neg (convex_Icc _ _)
    (QOU.Knot.FigureEightVolume.continuous_Lob.continuousOn) ?_
  intro x hx
  rw [interior_Icc] at hx
  exact deriv_Lob_neg hx.1 hx.2

/-- The form the chord argument consumes: folding an obtuse angle with
`Lob_pi_sub` turns the sum into a difference, and this makes it positive. -/
theorem Lob_sub_Lob_add_pos {a c : ℝ}
    (ha : π / 6 < a) (hc : 0 < c) (hac : a + c < 5 * π / 6) :
    0 < Lob a - Lob (a + c) := by
  have hlt : Lob (a + c) < Lob a :=
    strictAntiOn_Lob ⟨le_of_lt ha, by linarith⟩
      ⟨by linarith, le_of_lt hac⟩ (by linarith)
  linarith

end QOU.Archimedean.LobMonotonicity
