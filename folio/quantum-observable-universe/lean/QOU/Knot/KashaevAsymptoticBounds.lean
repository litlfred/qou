/-
  `⟨4₁⟩_N` BOUNDED ABOVE AND BELOW, WITH NO `g_{k*}` LEFT IN IT.

  Step 18 gives `⟨4₁⟩_N` as `g_{k*}·(model ± err)`.  Step 7 gives `log g_{k*}`
  to `O(1/N)`.  Putting them together removes the peak term entirely:

      e^{P−E}·(model − err)  ≤  ⟨4₁⟩_N  ≤  e^{P+E}·(model + err)

  with `P = −(2N/π)Λ(5π/6) + log(2N sin θ_{k*}) + (π/6N)cot θ_{k*}` and `E` step
  7's error.

  **`P` is where the volume enters.**  `−(2/π)Λ(5π/6)` is `Vol(4₁)/2π`, so the
  first term of `P` is `N·Vol(4₁)/2π` — the exponential growth rate of the
  volume conjecture.  The second is `log N + log(2 sin θ_{k*}) ≈ log N`, and
  `model ≈ 3^{−1/4}√N`.  Multiply: `⟨4₁⟩_N ≈ 3^{−1/4}·N^{3/2}·e^{N·Vol/2π}`.

  `model` and `err` stay abstract.  A caller supplies them from step 18, and
  the only thing this file needs to know about them is `err ≤ model`, which is
  what makes the lower bound non-vacuous.

  -- Ref: [leitner2026] QOU/Knot/KashaevFullSum.lean
  -- Ref: [leitner2026] QOU/Knot/KashaevLogAsymptotic.lean
-/
import QOU.Knot.KashaevFullSum
import QOU.Knot.KashaevLogAsymptotic

namespace QOU.Knot.FigureEightVolume

open Real QOU.Archimedean

/-- The main term of `log g_{k*}` — step 7's, named. -/
noncomputable def peakLogMain (N : ℕ) : ℝ :=
  -(2 * (N : ℝ) / π) * Lob (5 * π / 6)
  + Real.log (2 * N * Real.sin (((5 * N / 6 : ℕ) : ℝ) * π / N))
  + (π / (6 * N)) * (Real.cos (((5 * N / 6 : ℕ) : ℝ) * π / N)
                     / Real.sin (((5 * N / 6 : ℕ) : ℝ) * π / N))

/-- The error of `log g_{k*}` — step 7's, named. -/
noncomputable def peakLogErr (N : ℕ) : ℝ :=
  2 * (1 / (144 * ((5 * N / 6 : ℕ) : ℝ) ^ 2) + 7 / 12 * (π / N) ^ 2
       + (π / N) ^ 2
         / (12 * Real.sin (((5 * N / 6 : ℕ) : ℝ) * π / N) ^ 2))
  + (2 * (N : ℝ) / π) * (Real.sqrt 3 * (π / N) ^ 2 / 2 + 4 * (π / N) ^ 3 / 6)

/-- Step 7 in the named form. -/
theorem abs_log_kashaevProd_argmax_le {N : ℕ} (hN : 6 ≤ N) :
    |Real.log (kashaevProd N (5 * N / 6)) - peakLogMain N| ≤ peakLogErr N :=
  log_kashaevProd_argmax hN

/-- **The peak term, bracketed.**  `g_{k*} = e^{log g_{k*}}`, and step 7
brackets the exponent. -/
theorem kashaevProd_argmax_bounds {N : ℕ} (hN : 6 ≤ N) :
    Real.exp (peakLogMain N - peakLogErr N) ≤ kashaevProd N (5 * N / 6)
      ∧ kashaevProd N (5 * N / 6) ≤ Real.exp (peakLogMain N + peakLogErr N) := by
  have hpos := kashaevProd_pos (N := N) (k := 5 * N / 6) (by omega)
  have hd := abs_le.mp (abs_log_kashaevProd_argmax_le hN)
  constructor
  · calc Real.exp (peakLogMain N - peakLogErr N)
        ≤ Real.exp (Real.log (kashaevProd N (5 * N / 6))) :=
          Real.exp_le_exp.mpr (by linarith [hd.1])
      _ = kashaevProd N (5 * N / 6) := Real.exp_log hpos
  · calc kashaevProd N (5 * N / 6)
        = Real.exp (Real.log (kashaevProd N (5 * N / 6))) := (Real.exp_log hpos).symm
      _ ≤ Real.exp (peakLogMain N + peakLogErr N) :=
          Real.exp_le_exp.mpr (by linarith [hd.2])

/-- **`⟨4₁⟩_N`, above and below, with no `g_{k*}`.**

`err ≤ model` is what keeps the lower bound from being vacuous — without it the
left-hand side is negative and says nothing.  It is exactly the condition step
18's error has to satisfy before the constant is readable, and it holds for `N`
past a threshold. -/
theorem kashaev_bounds_of_model {N : ℕ} (hN : 6 ≤ N) {model err : ℝ}
    (herr : err ≤ model) (herr0 : 0 ≤ err)
    (h18 : |kashaev N - kashaevProd N (5 * N / 6) * model|
        ≤ kashaevProd N (5 * N / 6) * err) :
    Real.exp (peakLogMain N - peakLogErr N) * (model - err) ≤ kashaev N
      ∧ kashaev N ≤ Real.exp (peakLogMain N + peakLogErr N) * (model + err) := by
  have hpos := kashaevProd_pos (N := N) (k := 5 * N / 6) (by omega)
  have hpeak := kashaevProd_argmax_bounds hN
  have hd := abs_le.mp h18
  have hme : (0 : ℝ) ≤ model - err := by linarith
  have hpe : (0 : ℝ) ≤ model + err := by linarith
  constructor
  · -- `⟨4₁⟩_N ≥ g_{k*}(model − err) ≥ e^{P−E}(model − err)`
    have h1 : kashaevProd N (5 * N / 6) * (model - err) ≤ kashaev N := by
      have := hd.1; nlinarith
    have h2 : Real.exp (peakLogMain N - peakLogErr N) * (model - err)
        ≤ kashaevProd N (5 * N / 6) * (model - err) :=
      mul_le_mul_of_nonneg_right hpeak.1 hme
    linarith
  · -- `⟨4₁⟩_N ≤ g_{k*}(model + err) ≤ e^{P+E}(model + err)`
    have h1 : kashaev N ≤ kashaevProd N (5 * N / 6) * (model + err) := by
      have := hd.2; nlinarith
    have h2 : kashaevProd N (5 * N / 6) * (model + err)
        ≤ Real.exp (peakLogMain N + peakLogErr N) * (model + err) :=
      mul_le_mul_of_nonneg_right hpeak.2 hpe
    linarith

end QOU.Knot.FigureEightVolume
