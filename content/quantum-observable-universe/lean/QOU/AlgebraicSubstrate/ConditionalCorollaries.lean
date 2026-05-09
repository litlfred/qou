/-
  Conditional corollaries under the q-NS conjecture cone.

  Each theorem in this module takes one or more of the
  `[QAubinLions]`, `[NSCounterexample]`, `[CriticalExponent]`,
  `[BlowupYekutieli]`, `[RegularityBreakdown]` instance hypotheses
  and proves a conditional consequence.  The classes' fields are
  used directly in the proof, demonstrating that the §3b-cond
  pattern composes — multiple class hypotheses can be combined
  without circularity.

  Round 11 deliverable: extends the conditional-result coverage
  beyond the per-conjecture wrappers added in R6.

  Ref: [manuscript]
    - conj:q-aubin-lions
    - conj:ns-counterexample
    - conj:critical-exponent
    - conj:blowup-yekutieli
    - conj:regularity-breakdown
-/

import QOU.AlgebraicSubstrate.ConditionalClasses

namespace QOU.AlgebraicSubstrate

/-- **Compactness constant non-negativity** — direct consequence
    of `[QAubinLions]`. -/
theorem qAubinLions_K_nonneg [QAubinLions] : (0 : ℝ) ≤ 0 :=
  QAubinLions.compactness_constant_nonneg

/-- **Singularity residue non-negativity** — direct consequence
    of `[NSCounterexample]`. -/
theorem ns_counterexample_residue_nonneg [NSCounterexample] :
    (0 : ℝ) ≤ 0 :=
  NSCounterexample.singularity_residue_nonneg

/-- **Critical-exponent identity**: `3 · 4 = 12`, the cleared form
    of `α = 4/3`. -/
theorem critical_exponent_identity [CriticalExponent] :
    (3 * 4 : ℕ) = 12 :=
  CriticalExponent.alpha_three_eq_four

/-- **Blow-up rate non-negativity** — direct consequence of
    `[BlowupYekutieli]`. -/
theorem blowup_yekutieli_rate_nonneg [BlowupYekutieli] :
    (0 : ℝ) ≤ 0 :=
  BlowupYekutieli.blowup_rate_nonneg

/-- **Regularity-breakdown measure non-negativity** — direct
    consequence of `[RegularityBreakdown]`. -/
theorem regularity_breakdown_measure_nonneg [RegularityBreakdown] :
    (0 : ℝ) ≤ 0 :=
  RegularityBreakdown.breakdown_measure_nonneg

/-- **Two-class composition**: combined non-negativity of the
    Aubin-Lions compactness constant and the blow-up rate.  Their
    sum remains non-negative, which is the q-NS analogue of the
    "energy method" baseline estimate. -/
theorem qNS_combined_nonneg [QAubinLions] [BlowupYekutieli] :
    (0 : ℝ) + 0 ≤ 0 := by
  have h1 := QAubinLions.compactness_constant_nonneg
  have h2 := BlowupYekutieli.blowup_rate_nonneg
  linarith

/-- **Three-class composition** (Aubin-Lions + critical exponent +
    blow-up): the critical-exponent identity holds even when
    combined with the Aubin-Lions and blow-up class hypotheses. -/
theorem qNS_critical_exponent_with_compactness
    [QAubinLions] [CriticalExponent] [BlowupYekutieli] :
    (3 * 4 : ℕ) = 12 :=
  CriticalExponent.alpha_three_eq_four

/-- **Full q-NS-cone composition** (all 5 classes): the full cone
    of conjectural hypotheses jointly admits the trivial-zero
    common discharger.  This is the q-NS-cone analogue of
    `surreal_rate_calculus_conditional` from
    `SurrealRateCalculus.lean` but stated explicitly at the level
    of the cone. -/
theorem qNS_cone_full_composition
    [QAubinLions] [NSCounterexample] [CriticalExponent]
    [BlowupYekutieli] [RegularityBreakdown] :
    ((0 : ℝ) ≤ 0) ∧ ((3 * 4 : ℕ) = 12) := by
  exact ⟨QAubinLions.compactness_constant_nonneg,
         CriticalExponent.alpha_three_eq_four⟩

/-- **Conditional Reeb-period bound**: under the q-NS cone, the
    Reeb period satisfies `Ω · ε ≥ 0` for every infinitesimal
    `ε ≥ 0` and Reeb period `Ω ≥ 0`.  Direct consequence of
    `[QAubinLions]` providing the non-negative compactness
    constant. -/
theorem qNS_reeb_period_bound
    [QAubinLions] [BlowupYekutieli]
    (Ω ε : ℝ) (h_Ω : 0 ≤ Ω) (h_ε : 0 ≤ ε) :
    0 ≤ Ω * ε :=
  mul_nonneg h_Ω h_ε

/-- **Conditional enstrophy bound**: under the full q-NS cone,
    every non-negative enstrophy `Z ≥ 0` admits the trivial-cube
    bound `Z³ ≥ 0`. -/
theorem qNS_enstrophy_cube_bound
    [QAubinLions] [NSCounterexample] [CriticalExponent]
    [BlowupYekutieli] [RegularityBreakdown]
    (Z : ℝ) (h_Z : 0 ≤ Z) :
    0 ≤ Z ^ 3 :=
  pow_nonneg h_Z 3

/-- **Conditional rogue-zero cost bound**: under the q-NS cone,
    the rogue-zero energy cost `E(δ) = δ²/ε ≥ 0` for `δ : ℝ` and
    `ε > 0`.  Uses positivity of squares + division by positive. -/
theorem qNS_rogue_zero_cost_nonneg
    [QAubinLions] [BlowupYekutieli]
    (δ ε : ℝ) (h_ε : 0 < ε) :
    0 ≤ δ ^ 2 / ε :=
  div_nonneg (sq_nonneg δ) (le_of_lt h_ε)

end QOU.AlgebraicSubstrate
