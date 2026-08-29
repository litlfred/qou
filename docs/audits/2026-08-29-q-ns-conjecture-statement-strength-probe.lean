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

/-! ## Part 2 — the fix bites (added 2026-08-29, same session)

The strengthened fields landed in `p2-critical-exponent.lean` and
`p5-counterexample.lean`.  These two theorems show the strengthening is
not cosmetic: the very witnesses above are now **provably excluded**.
Same functions, same `T*`; only the quantifier changed. -/

/-- `enstrophy q = max q 0` no longer inhabits the strengthened
    `enstrophy_diverges`: on the punctured neighbourhood `|q - 1| < 1`
    the enstrophy is below `2`, so `M = 10` has no witness. -/
theorem regularAtOne_refuted_by_strengthened :
    ¬ (∀ M : ℝ, ∀ ε : ℝ, 0 < ε →
        ∃ q : ℝ, 1 < q ∧ q - 1 < ε ∧ M < max q 0) := by
  intro h
  obtain ⟨q, -, hq, hM⟩ := h 10 1 one_pos
  have hq2 : q < 2 := by linarith
  rcases max_cases q 0 with ⟨he, _⟩ | ⟨he, _⟩ <;> rw [he] at hM <;> linarith

/-- `velocityProfile t x = max (-t) 0` with `T* = 1` no longer inhabits
    the strengthened `ns_counterexample_holds`: on the left
    neighbourhood `1 - 1 < t < 1` the velocity is `0`, so `M = 1` has
    no witness. -/
theorem noSingularityAtT_refuted_by_strengthened :
    ¬ (∀ M : ℝ, ∀ ε : ℝ, 0 < ε →
        ∃ t _x : ℝ, (1 : ℝ) - ε < t ∧ t < 1 ∧ M < max (-t) 0) := by
  intro h
  obtain ⟨t, -, ht0, -, hM⟩ := h 1 1 one_pos
  have htpos : (0 : ℝ) < t := by linarith
  have : max (-t) 0 = 0 := max_eq_right (by linarith)
  rw [this] at hM; linarith
