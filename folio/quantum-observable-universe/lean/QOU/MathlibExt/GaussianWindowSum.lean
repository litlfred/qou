/-
  THE TILTED GAUSSIAN OVER A FINITE WINDOW.

      | ∑_{|n|≤W} e^{−an² + 2Ln}  −  e^{L²/a}√(π/a) |
          ≤  e^{L²/a}·( √(π/a)·(theta error)  +  (tail beyond W) ).

  Steps 12 and 13 combined.  This is what the Kashaev assembly actually
  consumes: the sum it can control is over a WINDOW (outside it the ratio
  expansion's cubic remainder is out of hand), while the closed form
  `e^{L²/a}√(π/a)` is for the whole of `ℤ`.  Two errors separate them and they
  are of completely different kinds:

    * `√(π/a)·2q/(1−q)`, `q = e^{−π²/a}` — the sum-versus-integral discrepancy,
      exponentially small in `1/a`.  Nothing to do with the window.
    * the tail beyond `±W` — exponentially small in `aW²`.  Nothing to do with
      the sum-versus-integral question.

  Keeping them separate is deliberate: they are optimised by opposite choices
  of `W`, and a single lumped constant would hide that.

  -- Ref: [leitner2026] QOU/MathlibExt/GaussianTiltedSum.lean
  -- Ref: [leitner2026] QOU/MathlibExt/GaussianTailBound.lean
-/
import QOU.MathlibExt.GaussianTiltedSum
import QOU.MathlibExt.GaussianTailBound

namespace QOU.MathlibExt

open Real

/-- The window sum of the tilted family, refactored through the shift. -/
theorem sum_Icc_tilted_eq {a L : ℝ} (ha : a ≠ 0) (W : ℕ) :
    (∑ n ∈ Finset.Icc (-(W : ℤ)) (W : ℤ),
        Real.exp (-a * (n : ℝ) ^ 2 + 2 * L * (n : ℝ)))
      = Real.exp (L ^ 2 / a)
        * ∑ n ∈ Finset.Icc (-(W : ℤ)) (W : ℤ),
            Real.exp (-a * ((n : ℝ) - L / a) ^ 2) := by
  rw [Finset.mul_sum]
  exact Finset.sum_congr rfl fun n _ => exp_quadratic_eq ha

/-- **The window sum against the closed form.**  Both errors explicit and
kept apart. -/
theorem abs_sum_Icc_tilted_sub_le {a L : ℝ} (ha : 0 < a) (W : ℕ) :
    |(∑ n ∈ Finset.Icc (-(W : ℤ)) (W : ℤ),
        Real.exp (-a * (n : ℝ) ^ 2 + 2 * L * (n : ℝ)))
        - Real.exp (L ^ 2 / a) * Real.sqrt (π / a)|
      ≤ Real.exp (L ^ 2 / a)
        * (Real.sqrt (π / a)
             * (2 * Real.exp (-(π ^ 2 / a)) / (1 - Real.exp (-(π ^ 2 / a))))
           + Real.exp (a * (L / a) ^ 2)
             * Real.exp (-a * ((W : ℝ) + 1) ^ 2 / 4)
             * (1 + 2 * Real.exp (-a / 4) / (1 - Real.exp (-a / 4)))) := by
  have hE : (0 : ℝ) < Real.exp (L ^ 2 / a) := Real.exp_pos _
  rw [sum_Icc_tilted_eq (ne_of_gt ha) W]
  have hfac : Real.exp (L ^ 2 / a)
        * (∑ n ∈ Finset.Icc (-(W : ℤ)) (W : ℤ),
            Real.exp (-a * ((n : ℝ) - L / a) ^ 2))
        - Real.exp (L ^ 2 / a) * Real.sqrt (π / a)
      = Real.exp (L ^ 2 / a)
        * ((∑ n ∈ Finset.Icc (-(W : ℤ)) (W : ℤ),
              Real.exp (-a * ((n : ℝ) - L / a) ^ 2)) - Real.sqrt (π / a)) := by
    ring
  rw [hfac, abs_mul, abs_of_pos hE]
  refine mul_le_mul_of_nonneg_left ?_ hE.le
  -- the window sum is under the `ℤ` sum, and over it by at most the tail
  have hsumm := (hasSum_gaussian_theta_real a (L / a) ha).summable
  have hle : (∑ n ∈ Finset.Icc (-(W : ℤ)) (W : ℤ),
        Real.exp (-a * ((n : ℝ) - L / a) ^ 2))
      ≤ ∑' n : ℤ, Real.exp (-a * ((n : ℝ) - L / a) ^ 2) :=
    hsumm.sum_le_tsum _ (fun _ _ => (Real.exp_pos _).le)
  have htail := tsum_gaussian_sub_sum_Icc_le (a := a) (c := L / a) ha W
  have hbase := abs_tsum_gaussian_sub_sqrt_le a (L / a) ha
  have hb := abs_le.mp hbase
  rw [abs_le]
  constructor
  · -- from below: window ≥ ℤ-sum − tail ≥ √(π/a) − (theta error) − tail
    linarith [hb.1, htail]
  · -- from above: window ≤ ℤ-sum ≤ √(π/a) + (theta error)
    have hnn : (0 : ℝ) ≤ Real.exp (a * (L / a) ^ 2)
        * Real.exp (-a * ((W : ℝ) + 1) ^ 2 / 4)
        * (1 + 2 * Real.exp (-a / 4) / (1 - Real.exp (-a / 4))) := by
      have hσ1 : Real.exp (-a / 4) < 1 := by
        rw [Real.exp_lt_one_iff]; linarith
      have hσ0 : 0 < Real.exp (-a / 4) := Real.exp_pos _
      have : (0 : ℝ) < 1 - Real.exp (-a / 4) := by linarith
      positivity
    linarith [hb.2, hle]

end QOU.MathlibExt
