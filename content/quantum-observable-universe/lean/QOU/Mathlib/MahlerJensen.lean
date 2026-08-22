/-
  **The Mahler measure of a linear factor** — the cornerstone of the Jensen form.

  Bean `qou-4lbh`.  ⚠ Mathlib-style, Mathlib imports only, no QOU dependency: liftable
  verbatim.

  ═══ ⚠ THIS REVERSES A RECOMMENDATION ═══

  `qou-4lbh` recorded that the last open step of Roth's lemma — bounding the heights of the
  factors `φₖ, ψₖ` of a separated `P = ∑ₖ φₖ(x)ψₖ(y)` — needs Gelfond's inequality, and that
  the choice was between **filling Mathlib's missing Mahler bridges upstream** and a
  **bare-hands Gelfond inequality on `ℤ[X]`**.  The recommendation given was bare-hands, to
  avoid `ℂ[X]` and circle averages.

  **That was the wrong call, and measuring says so.**  Two things:

  * Gelfond's standard proof *goes through* the Mahler measure.  "Bare-hands" is not a
    shortcut around it; it is a re-derivation of it.
  * Mathlib already has the hard analytic content —
    `circleAverage_log_norm_sub_const_eq_posLog`, i.e. Jensen's formula for a single root.
    What was missing is only its connection to `mahlerMeasure`, which is the one theorem
    below.

  So the upstream route is much cheaper than it looked.  What remains for the Jensen form
  `M(P) = ‖lead P‖ · ∏ max(1, ‖root‖)` is the factorization of a complex polynomial into
  linear factors together with `mahlerMeasure_mul`, both of which Mathlib has.

  ═══ WHAT THIS DOES NOT YET GIVE ═══

  ⚠ The Jensen form is one of *two* bridges.  Landau's `M(P) ≤ √(deg+1) · H(P)` — needed to
  turn a Mahler bound into a *coefficient* bound — is still absent, and is not addressed
  here.  Gelfond needs both directions.
-/
import Mathlib.Analysis.Polynomial.MahlerMeasure
import Mathlib.Analysis.SpecialFunctions.Integrals.PosLogEqCircleAverage

open Real

namespace Polynomial

/-- **The Mahler measure of a linear factor:** `M(X − a) = max(1, ‖a‖)`.

This is Jensen's formula for a single root.  Mathlib supplies the analytic content
(`circleAverage_log_norm_sub_const_eq_posLog`) but does not connect it to `mahlerMeasure`. -/
theorem mahlerMeasure_X_sub_C (a : ℂ) :
    (X - C a : ℂ[X]).mahlerMeasure = max 1 ‖a‖ := by
  have hne : (X - C a : ℂ[X]) ≠ 0 := X_sub_C_ne_zero a
  have hpos : (0 : ℝ) < max 1 ‖a‖ := lt_of_lt_of_le one_pos (le_max_left _ _)
  have hlog : (X - C a : ℂ[X]).logMahlerMeasure = Real.log (max 1 ‖a‖) := by
    rw [logMahlerMeasure_def]
    have heval : (fun x : ℂ => Real.log ‖eval x (X - C a : ℂ[X])‖)
        = fun x : ℂ => Real.log ‖x - a‖ := by
      funext x
      simp
    rw [heval, circleAverage_log_norm_sub_const_eq_posLog,
      posLog_eq_log_max_one (norm_nonneg a)]
  rw [mahlerMeasure, if_pos hne, hlog, Real.exp_log hpos]

/-! ### Next

1. **The Jensen form** `M(P) = ‖lead P‖ · ∏ max(1, ‖root‖)`.  With the theorem above,
   `mahlerMeasure_mul`, and the factorization of a complex polynomial into linear factors,
   this is assembly rather than analysis.
2. **Landau's inequality** `M(P) ≤ √(deg+1) · H(P)` — the *other* bridge, still absent, and
   the one that converts a Mahler bound into a coefficient bound.
3. **Gelfond**, from (1) and (2), and then the height control on the factors that the
   induction step of Roth's lemma needs. -/

end Polynomial
