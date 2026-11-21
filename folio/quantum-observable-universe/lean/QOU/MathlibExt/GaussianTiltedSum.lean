/-
  THE TILTED GAUSSIAN SUM: `∑_{n∈ℤ} e^{−an² + 2Ln} = e^{L²/a}·√(π/a)·(1 + tiny)`.

  Step 10 produced a summand of the form `e^{−au² + 2Lu}` — a Gaussian with a
  linear tilt, the tilt being `2L = 2·log(2 sin θ_k)`, which does not vanish
  because `⌊5N/6⌋` is not exactly `5N/6`.  This file evaluates that sum.

  Completing the square is the whole idea: `−au² + 2Lu = L²/a − a(u − L/a)²`,
  so a tilt is a SHIFT of the Gaussian's centre by `L/a`, plus an overall
  factor `e^{L²/a}`.  And `GaussianThetaBound` was proved uniformly in the
  shift — which is exactly why it was stated that way.  Nothing new is needed
  analytically; the tilt costs one line of algebra and an already-uniform
  estimate.

  Sizes, for the Kashaev application: `L ≈ 4.52/N` and `a ≈ √3π/N`, so
  `L²/a ≈ 3.75/N → 0` and the tilt factor `e^{L²/a} → 1`.  Meanwhile
  `√(π/a) = √(N/√3) = √N·3^{−1/4}`.  **So the model sum tends to `c_σ·√N`, and
  the tilt contributes nothing in the limit** — but it had to be carried, since
  before taking the limit it is a genuine `1 + O(1/N)` factor.

  -- Ref: [leitner2026] QOU/MathlibExt/GaussianThetaBound.lean
  -- Ref: [leitner2026] QOU/Knot/KashaevRatioExpansion.lean
-/
import QOU.MathlibExt.GaussianThetaBound

namespace QOU.MathlibExt

open Real

/-- **Completing the square.**  A linear tilt is a shift of the centre plus a
constant factor. -/
theorem exp_quadratic_eq {a L u : ℝ} (ha : a ≠ 0) :
    Real.exp (-a * u ^ 2 + 2 * L * u)
      = Real.exp (L ^ 2 / a) * Real.exp (-a * (u - L / a) ^ 2) := by
  rw [← Real.exp_add]
  congr 1
  field_simp
  ring

/-- The tilted family is summable over `ℤ`. -/
theorem summable_tilted_gaussian {a L : ℝ} (ha : 0 < a) :
    Summable (fun n : ℤ => Real.exp (-a * (n : ℝ) ^ 2 + 2 * L * (n : ℝ))) := by
  have hfun : (fun n : ℤ => Real.exp (-a * (n : ℝ) ^ 2 + 2 * L * (n : ℝ)))
      = fun n : ℤ => Real.exp (L ^ 2 / a)
          * Real.exp (-a * ((n : ℝ) - L / a) ^ 2) := by
    funext n
    exact exp_quadratic_eq (ne_of_gt ha)
  rw [hfun]
  exact ((hasSum_gaussian_theta_real a (L / a) ha).mul_left _).summable

/-- **The tilted sum equals the tilted integral**, up to the same
exponentially small relative error as the untilted one.

`e^{L²/a}·√(π/a)` is exactly `∫_ℝ e^{−ax² + 2Lx} dx`, so this says the tilted
Laplace sum is its tilted Laplace integral — which is the statement the
constant `c_σ` is read off from. -/
theorem abs_tsum_tilted_gaussian_sub_le {a L : ℝ} (ha : 0 < a) :
    |(∑' n : ℤ, Real.exp (-a * (n : ℝ) ^ 2 + 2 * L * (n : ℝ)))
        - Real.exp (L ^ 2 / a) * Real.sqrt (π / a)|
      ≤ Real.exp (L ^ 2 / a) * Real.sqrt (π / a)
        * (2 * Real.exp (-(π ^ 2 / a)) / (1 - Real.exp (-(π ^ 2 / a)))) := by
  have hfun : (fun n : ℤ => Real.exp (-a * (n : ℝ) ^ 2 + 2 * L * (n : ℝ)))
      = fun n : ℤ => Real.exp (L ^ 2 / a)
          * Real.exp (-a * ((n : ℝ) - L / a) ^ 2) := by
    funext n
    exact exp_quadratic_eq (ne_of_gt ha)
  rw [hfun, tsum_mul_left]
  have hbase := abs_tsum_gaussian_sub_sqrt_le a (L / a) ha
  have hE : (0 : ℝ) < Real.exp (L ^ 2 / a) := Real.exp_pos _
  have hsplit : Real.exp (L ^ 2 / a)
        * (∑' n : ℤ, Real.exp (-a * ((n : ℝ) - L / a) ^ 2))
      - Real.exp (L ^ 2 / a) * Real.sqrt (π / a)
      = Real.exp (L ^ 2 / a)
        * ((∑' n : ℤ, Real.exp (-a * ((n : ℝ) - L / a) ^ 2))
           - Real.sqrt (π / a)) := by ring
  rw [hsplit, abs_mul, abs_of_pos hE]
  calc Real.exp (L ^ 2 / a)
        * |(∑' n : ℤ, Real.exp (-a * ((n : ℝ) - L / a) ^ 2)) - Real.sqrt (π / a)|
      ≤ Real.exp (L ^ 2 / a)
        * (Real.sqrt (π / a)
           * (2 * Real.exp (-(π ^ 2 / a)) / (1 - Real.exp (-(π ^ 2 / a))))) :=
        mul_le_mul_of_nonneg_left hbase hE.le
    _ = Real.exp (L ^ 2 / a) * Real.sqrt (π / a)
        * (2 * Real.exp (-(π ^ 2 / a)) / (1 - Real.exp (-(π ^ 2 / a)))) := by
        ring

/-- Any finite part of the tilted sum is at most the whole — the free half of
the window-versus-`ℤ` comparison.  (The other half needs a tail bound.) -/
theorem sum_le_tsum_tilted_gaussian {a L : ℝ} (ha : 0 < a) (s : Finset ℤ) :
    ∑ n ∈ s, Real.exp (-a * (n : ℝ) ^ 2 + 2 * L * (n : ℝ))
      ≤ ∑' n : ℤ, Real.exp (-a * (n : ℝ) ^ 2 + 2 * L * (n : ℝ)) :=
  (summable_tilted_gaussian ha).sum_le_tsum s (fun _ _ => (Real.exp_pos _).le)

/-- The tilted sum is positive — needed to divide by it. -/
theorem tsum_tilted_gaussian_pos {a L : ℝ} (ha : 0 < a) :
    0 < ∑' n : ℤ, Real.exp (-a * (n : ℝ) ^ 2 + 2 * L * (n : ℝ)) := by
  have h0 := sum_le_tsum_tilted_gaussian (a := a) (L := L) ha {0}
  simp only [Finset.sum_singleton] at h0
  have : (0 : ℝ) < Real.exp (-a * ((0 : ℤ) : ℝ) ^ 2 + 2 * L * ((0 : ℤ) : ℝ)) :=
    Real.exp_pos _
  linarith

end QOU.MathlibExt
