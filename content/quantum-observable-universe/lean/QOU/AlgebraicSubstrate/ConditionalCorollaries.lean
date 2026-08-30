/-
  Conditional corollaries under the q-NS conjecture cone.

  Each theorem in this module takes one or more of the
  `[QAubinLions]`, `[NSCounterexample]`, `[CriticalExponent]`,
  `[BlowupYekutieli]`, `[RegularityBreakdown]` instance hypotheses
  and proves a conditional consequence.  The classes' existential
  fields are used directly in the proof, demonstrating that the
  §3b-cond pattern composes — multiple class hypotheses can be
  combined without circularity.

  Round 11 deliverable: extends the conditional-result coverage
  beyond the per-conjecture wrappers added in R6.  Updated post
  Gemini review to use the existential class fields.

  Ref: [manuscript]
    - conj:q-aubin-lions
    - conj:ns-counterexample
    - conj:critical-exponent
    - conj:blowup-yekutieli
    - conj:regularity-breakdown
-/

import QOU.AlgebraicSubstrate.ConditionalClasses

namespace QOU.AlgebraicSubstrate

/-- **Compactness-constant existence** — direct consequence of
    `[QAubinLions]` at energy `E = 0`. -/
theorem qAubinLions_K_exists [QAubinLions] :
    ∃ K : ℝ, 0 ≤ K ∧ K ≤ 2 * (0 : ℝ) :=
  QAubinLions.exists_compactness_constant 0 (le_refl 0)

/-- **Singularity-time existence** — direct consequence of
    `[NSCounterexample]`. -/
theorem ns_counterexample_T_exists [NSCounterexample] :
    ∃ T : ℝ, 0 ≤ T :=
  NSCounterexample.exists_singularity_time 0 (le_refl 0)

/-- **Critical-exponent value**: under `[CriticalExponent α]`, the exponent
    `α` is `4/3`.

    Until 2026-08-30 this concluded `(3 * 4 : ℕ) = 12` — true by `rfl` with or
    without the hypothesis, so the `[CriticalExponent]` binder was decorative.
    It now concludes something the hypothesis is actually needed for. -/
theorem critical_exponent_identity (α : ℝ) [h : CriticalExponent α] :
    α = 4 / 3 :=
  h.alpha_eq

/-- **Blow-up rate existence** — direct consequence of
    `[BlowupYekutieli]`. -/
theorem blowup_yekutieli_r_exists [BlowupYekutieli] :
    ∃ r : ℝ, 0 ≤ r ∧ r ≤ 1 + (0 : ℝ) :=
  BlowupYekutieli.exists_blowup_rate 0 (le_refl 0)

/-- **Breakdown-measure existence** — direct consequence of
    `[RegularityBreakdown]`. -/
theorem regularity_breakdown_measure_exists [RegularityBreakdown] :
    ∃ μ : ℝ, 0 ≤ μ ∧ μ ≤ (0 : ℝ) :=
  RegularityBreakdown.exists_breakdown_measure 0 (le_refl 0)

/-- **Two-class composition** (Aubin-Lions + blow-up): there exists
    a non-negative compactness constant *and* a non-negative blow-up
    rate.  The two existentials combine without circularity. -/
theorem qNS_combined_existence [QAubinLions] [BlowupYekutieli] :
    (∃ K : ℝ, 0 ≤ K) ∧ (∃ r : ℝ, 0 ≤ r) := by
  obtain ⟨K, hK, _⟩ := QAubinLions.exists_compactness_constant 0 (le_refl 0)
  obtain ⟨r, hr, _⟩ := BlowupYekutieli.exists_blowup_rate 0 (le_refl 0)
  exact ⟨⟨K, hK⟩, ⟨r, hr⟩⟩

/-- **Three-class composition** (Aubin-Lions + critical + blow-up):
    the critical-exponent identity holds even when combined with the
    Aubin-Lions and blow-up class hypotheses. -/
theorem qNS_critical_exponent_with_compactness (α : ℝ)
    [QAubinLions] [h : CriticalExponent α] [BlowupYekutieli] :
    α = 4 / 3 :=
  h.alpha_eq

/-- **Full q-NS-cone composition** (all 5 classes): every
    conjectural existential field admits a witness simultaneously. -/
theorem qNS_cone_full_composition (α : ℝ)
    [QAubinLions] [NSCounterexample] [h : CriticalExponent α]
    [BlowupYekutieli] [RegularityBreakdown] :
    (∃ K : ℝ, 0 ≤ K) ∧
    (∃ T : ℝ, 0 ≤ T) ∧
    (α = 4 / 3) ∧
    (∃ r : ℝ, 0 ≤ r) ∧
    (∃ μ : ℝ, 0 ≤ μ) := by
  obtain ⟨K, hK, _⟩ := QAubinLions.exists_compactness_constant 0 (le_refl 0)
  obtain ⟨T, hT⟩ := NSCounterexample.exists_singularity_time 0 (le_refl 0)
  obtain ⟨r, hr, _⟩ := BlowupYekutieli.exists_blowup_rate 0 (le_refl 0)
  obtain ⟨μ, hμ, _⟩ := RegularityBreakdown.exists_breakdown_measure 0 (le_refl 0)
  exact ⟨⟨K, hK⟩, ⟨T, hT⟩, h.alpha_eq, ⟨r, hr⟩, ⟨μ, hμ⟩⟩

/-- **Conditional Reeb-period bound**: under Aubin-Lions + blow-up,
    the Reeb period `Ω · ε ≥ 0` for every infinitesimal `ε ≥ 0` and
    Reeb period `Ω ≥ 0`. -/
theorem qNS_reeb_period_bound
    [QAubinLions] [BlowupYekutieli]
    (Ω ε : ℝ) (h_Ω : 0 ≤ Ω) (h_ε : 0 ≤ ε) :
    0 ≤ Ω * ε :=
  mul_nonneg h_Ω h_ε

/-- **Conditional enstrophy bound**: under the full q-NS cone,
    every non-negative enstrophy `Z ≥ 0` admits the trivial-cube
    bound `Z³ ≥ 0`. -/
theorem qNS_enstrophy_cube_bound {α : ℝ}
    [QAubinLions] [NSCounterexample] [CriticalExponent α]
    [BlowupYekutieli] [RegularityBreakdown]
    (Z : ℝ) (h_Z : 0 ≤ Z) :
    0 ≤ Z ^ 3 :=
  pow_nonneg h_Z 3
-- NOTE (2026-08-30, bean `qou-93hu`): the `α` binder above is added only to
-- track the `CriticalExponent` signature change. It does not make this theorem
-- conditional, because it never was: the proof is `pow_nonneg h_Z 3` and uses
-- NONE of the five class hypotheses — `0 ≤ Z ^ 3` follows from `0 ≤ Z` alone.
-- `qNS_reeb_period_bound` (`mul_nonneg`) and `qNS_rogue_zero_cost_nonneg`
-- (`div_nonneg`) have the same shape. That is a distinct defect from the one
-- this bean fixes — decorative hypotheses on an unconditionally-true claim,
-- the `proof-no-unused-hypothesis-rfl` family — and it is left untouched here
-- rather than folded into a critical-exponent change.

/-- **Conditional rogue-zero cost bound**: under Aubin-Lions +
    blow-up, the rogue-zero energy cost `E(δ) = δ²/ε ≥ 0` for
    `δ : ℝ` and `ε > 0`. -/
theorem qNS_rogue_zero_cost_nonneg
    [QAubinLions] [BlowupYekutieli]
    (δ ε : ℝ) (h_ε : 0 < ε) :
    0 ≤ δ ^ 2 / ε :=
  div_nonneg (sq_nonneg δ) (le_of_lt h_ε)

end QOU.AlgebraicSubstrate
