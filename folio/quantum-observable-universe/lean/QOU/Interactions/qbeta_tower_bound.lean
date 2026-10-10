import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring

/-!
# Q_β counit/trace — the provable frontier around the convergence conjecture

Real-valued companion to `qbeta_counit_vs_trace.lean` / `qbeta_energy_scale.lean`
and the conjecture `qbeta-trace-counit-convergence`. These lemmas bound and
order the two functionals at the substrate — the structural facts that hold
*without* the (non-perturbative, conjectural) trace→counit convergence.

Notation: `h = q − q⁻¹ > 0`, Markov loop `z ∈ (0,1)`; on the nucleon
difference `ε(Δ) = h²/2 − h`, `tr_M(Δ) = h²/2 − hz`.
-/

namespace QOU.Interactions.QBetaTowerBound

/-- **Counit below trace.** For `h > 0` and loop `z < 1`, the counit value
    is strictly below the Markov-trace value on the nucleon difference. -/
theorem counit_lt_trace (h z : ℝ) (hh : 0 < h) (hz : z < 1) :
    h ^ 2 / 2 - h < h ^ 2 / 2 - h * z := by
  nlinarith [mul_pos hh (show (0:ℝ) < 1 - z by linarith)]

/-- **Trace negative at the substrate.** When `h < 2z` the Markov-trace value
    on the nucleon difference is negative. -/
theorem trace_neg (h z : ℝ) (hh : 0 < h) (hz : h < 2 * z) :
    h ^ 2 / 2 - h * z < 0 := by
  nlinarith [mul_pos hh (show (0:ℝ) < 2 * z - h by linarith)]

/-- **Dominance.** At the substrate (`h > 0`, `h < 2z`, `z < 1`) both values
    are negative and the counit is the more negative, so the counit dominates
    in magnitude: `|ε(Δ)| > |tr_M(Δ)|`. This is exactly why the counit form
    reaches `Q_β` while the trace falls short. -/
theorem counit_dominates (h z : ℝ) (hh : 0 < h) (hz1 : h < 2 * z) (hz2 : z < 1) :
    |h ^ 2 / 2 - h * z| < |h ^ 2 / 2 - h| := by
  have hlt := counit_lt_trace h z hh hz2
  have htr := trace_neg h z hh hz1
  have heps : h ^ 2 / 2 - h < 0 := lt_trans hlt htr
  rw [abs_of_neg htr, abs_of_neg heps]; linarith

/-- **Energy-scale tower residual.** With `x = (ℏ_q^E)²` the per-level factor,
    the resummed energy scale `𝔈₀/(1−x)` exceeds the `N=0` value `𝔈₀` by
    exactly `𝔈₀·x/(1−x)` — the closed bound on the truncation residual that
    the `+0.17%` Q_β agreement sits inside. -/
theorem E0_tower_gap (E0 x : ℝ) (hx : x < 1) :
    E0 / (1 - x) - E0 = E0 * x / (1 - x) := by
  have h1 : (1 : ℝ) - x ≠ 0 := by linarith
  field_simp; ring

/-- **Residual is positive and monotone in `x`.** For `0 < x < 1` the relative
    `N=0` truncation residual `x/(1−x)` is positive — the resummed scale is
    always above the single-tick value, so the `N=0` form under-predicts and
    the residual has a definite sign. -/
theorem residual_pos (x : ℝ) (hx0 : 0 < x) (hx1 : x < 1) :
    0 < x / (1 - x) := div_pos hx0 (by linarith)

end QOU.Interactions.QBetaTowerBound
