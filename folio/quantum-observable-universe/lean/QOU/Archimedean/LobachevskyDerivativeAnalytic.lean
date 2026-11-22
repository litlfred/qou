/-
  Real-analyticity of `Λ' = −log(2 sin t)` on `(0, π)` — the Mathlib infra the
  obtuse ideal-tetrahedron volume identity needs (bean `qou-w3eg`, H4-5 step 1a).

  WHY THIS FILE.  The acute Milnor Λ-sum is proved sorry-free
  (`hypVolume_chimney_inscribedTriangle`).  Milnor's Appendix closes the obtuse
  case "by a similar argument, or by analytic continuation"; the analytic route
  (the one that needs no signed-subdivision sign convention) has three steps —

    1. `Λ` is real-analytic on `(0, π)`;
    2. the base integral is real-analytic in the angles `(α, β)`;
    3. the identity theorem glues the acute equality onto the whole open simplex.

  Step 1 factors through `Λ'`, and `Λ'(t) = −log(2 sin t)`
  (`QOU.Archimedean.deriv_Lob`).  This file supplies the analyticity of THAT
  function on `(0, π)` — a genuine Mathlib gap for the real trigonometric
  functions, filled by restricting the (entire) COMPLEX `sin` to the reals.

  WHAT WAS AND WAS NOT IN MATHLIB (measured against v4.24.0).  Mathlib carries
  `Complex.analyticAt_sin` (ℂ, entire) and `AnalyticAt.re_ofReal`
  (`Analysis/SpecialFunctions/Complex/Analytic.lean`), so real-analyticity of
  `Real.sin` follows by one `simpa` — but is not itself a named Mathlib lemma.
  Real `log`-analyticity on the positives IS present there
  (`Real.analyticAt_log`, `hx : 0 < x`), as is `AnalyticAt.log`.  Composing
  them gives `Λ'` analytic on `(0, π)`, where `sin t > 0`.

  WHAT THIS DOES NOT DO.  It does NOT prove `Λ` itself analytic — only its
  derivative.  Per bean `qou-w3eg`'s guard, nothing about the obtuse volume is
  asserted here.

  🛑 SUPERSEDED ROUTE (corrected in the same tranche).  This header first said
  step 1 was blocked here because "Mathlib has no antiderivative-of-analytic
  lemma".  That is true of Mathlib and was the wrong conclusion: `Λ` does not
  have to be reached through its derivative at all.  **Step 1 is CLOSED**, by
  composition rather than antidifferentiation, in
  `QOU.Archimedean.analyticAt_Lob` / `analyticOnNhd_Lob`
  (`QOU/Archimedean/LobAnalytic.lean`), using the corpus's own complex-dilog
  layer: on `(0, π)`, `Λ t = Im cLiTwoExt(e^{2it}) / 2`.  This file remains a
  correct standalone statement about `Λ'` and is still the natural input for a
  derivative-side argument; it is simply no longer on the critical path.
  Steps 2–3 stay open (`qou-w3eg`).

  Archimedean (ℝ): `Real.sin`, `Real.log`, ordering — §7c.

  -- Ref: [milnor1982] https://doi.org/10.1090/S0273-0979-1982-14958-8
  -- Ref: [thurston1978] Ch. 7
  -- Ref: [leitner2026] beans qou-w3eg (H4-5 obtuse, step 1a), qou-idvt
-/
import Mathlib.Analysis.SpecialFunctions.Complex.Analytic
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Deriv

namespace QOU.Archimedean

open Real Set

/-- **`Real.sin` is real-analytic at every point.**  The complex `sin` is
entire (`Complex.analyticAt_sin`); its restriction to the reals along
`ofReal`, read off by the real part, is `Real.sin` (`Complex.sin_ofReal_re`).
Mathlib proves the ℂ side but names no ℝ-side lemma, so this fills the gap. -/
theorem analyticAt_real_sin (x : ℝ) : AnalyticAt ℝ Real.sin x := by
  have h : AnalyticAt ℂ Complex.sin (x : ℂ) := Complex.analyticAt_sin
  simpa [Complex.sin_ofReal_re] using h.re_ofReal

/-- **`Real.cos` is real-analytic at every point.**  Same route through the
entire complex `cos`. -/
theorem analyticAt_real_cos (x : ℝ) : AnalyticAt ℝ Real.cos x := by
  have h : AnalyticAt ℂ Complex.cos (x : ℂ) := Complex.analyticAt_cos
  simpa [Complex.cos_ofReal_re] using h.re_ofReal

/-- **`Λ'(t) = −log(2 sin t)` is real-analytic on `(0, π)`.**  On `(0, π)`,
`sin t > 0`, so `2 sin t > 0` and `Real.log` is analytic there
(`AnalyticAt.log`); precompose with the analytic `Real.sin` and negate.

This is the analytic input the obtuse ideal-tetrahedron volume identity's
analytic-continuation route consumes for its derivative; it does not by itself
make `Λ` analytic (see the file header). -/
theorem analyticAt_neg_log_two_sin {t : ℝ} (h0 : 0 < t) (hπ : t < π) :
    AnalyticAt ℝ (fun s => -Real.log (2 * Real.sin s)) t := by
  have hpos : 0 < 2 * Real.sin t := by
    have : 0 < Real.sin t := Real.sin_pos_of_pos_of_lt_pi h0 hπ
    linarith
  have h2 : AnalyticAt ℝ (fun s => 2 * Real.sin s) t :=
    analyticAt_const.mul (analyticAt_real_sin t)
  exact (h2.log hpos).neg

/-- **`Λ'` is real-analytic on the whole open interval `(0, π)`** (the
`AnalyticOnNhd` form the identity theorem consumes). -/
theorem analyticOnNhd_neg_log_two_sin :
    AnalyticOnNhd ℝ (fun s => -Real.log (2 * Real.sin s)) (Ioo 0 π) :=
  fun _ ht => analyticAt_neg_log_two_sin ht.1 ht.2

end QOU.Archimedean
