import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

/-!
# Two q-NS conjecture statements are weaker than their prose

Run:  `LEAN_PATH=<mathlib oleans> lean <this file>`  ->  exit 0, no `sorryAx`.

Each instance below inhabits a chapter conjecture carrier with a witness
that **fails the property the block's `.md` claims**, which is what shows
the Lean statement does not encode that property.

Classes copied VERBATIM (fields only) from
    content/quantum-observable-universe/fluid-dynamics/p2-critical-exponent.lean
    content/quantum-observable-universe/fluid-dynamics/p5-counterexample.lean
    Convention follows docs/audits/2026-08-24-vacuous-prop-carrier-probe.lean. -/

class CriticalExponentCopy where
  enstrophy : ℝ → ℝ
  criticalExponent : ℝ
  criticalExponent_pos : 0 < criticalExponent
  enstrophy_nonneg : ∀ q, 0 ≤ enstrophy q
  enstrophy_diverges : ∀ M : ℝ, ∃ q : ℝ, q ≠ 1 ∧ M < enstrophy q

class NSCounterexampleCopy where
  singularityTime : ℝ
  velocityProfile : ℝ → ℝ → ℝ
  singularityTime_pos : 0 < singularityTime
  ns_counterexample_holds :
    ∀ M : ℝ, ∃ t x : ℝ, t < singularityTime ∧ M < velocityProfile t x

/-- WITNESS 1: enstrophy = `max q 0`, which near `q = 1` is just the
    identity — bounded, no divergence of any kind at `q → 1`.
    Yet it satisfies `enstrophy_diverges`. -/
instance regularAtOne : CriticalExponentCopy where
  enstrophy := fun q => max q 0
  criticalExponent := 1
  criticalExponent_pos := by norm_num
  enstrophy_nonneg := fun q => le_max_right q 0
  enstrophy_diverges := by
    intro M
    refine ⟨max M 0 + 2, by have := le_max_right M 0; intro h; linarith, ?_⟩
    have h0 : (0:ℝ) ≤ max M 0 := le_max_right M 0
    have hM : M ≤ max M 0 := le_max_left M 0
    have : max (max M 0 + 2) 0 = max M 0 + 2 := max_eq_left (by linarith)
    rw [this]; linarith

/-- WITNESS 2: velocity = `max (-t) 0`, which tends to 0 as `t → T*⁻ = 1⁻`.
    Perfectly regular AT the alleged singularity time.
    Yet it satisfies `ns_counterexample_holds`. -/
instance noSingularityAtT : NSCounterexampleCopy where
  singularityTime := 1
  velocityProfile := fun t _ => max (-t) 0
  singularityTime_pos := by norm_num
  ns_counterexample_holds := by
    intro M
    have h0 : (0:ℝ) ≤ max M 0 := le_max_right M 0
    have hM : M ≤ max M 0 := le_max_left M 0
    refine ⟨-(max M 0 + 2), 0, by linarith, ?_⟩
    have hneg : -(-(max M 0 + 2)) = max M 0 + 2 := by ring
    have hmax : max (-(-(max M 0 + 2))) 0 = max M 0 + 2 := by
      rw [hneg]; exact max_eq_left (by linarith)
    rw [hmax]; linarith

#print axioms regularAtOne
#print axioms noSingularityAtT
