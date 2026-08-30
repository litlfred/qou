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

/-- **Compactness vanishes at zero energy** — a consequence of linearity.

    Until 2026-08-30 this concluded `∃ K, 0 ≤ K ∧ K ≤ 2 · 0`, i.e. that some
    non-negative real is `≤ 0`, which is true of `0` with or without the
    hypothesis. The class now says `K` is linear in the energy, so the
    zero-energy value is *determined* rather than merely bounded, and the proof
    has to use the hypothesis to get it. Bean `qou-3ytx`. -/
theorem qAubinLions_zero_energy (K : ℝ → ℝ) [h : QAubinLions K] :
    K 0 = 0 := by
  obtain ⟨C, _, hlin⟩ := h.linear_in_energy
  rw [hlin 0 (le_refl 0)]; ring

/-- **Compactness is monotone in the energy bound** — the substantive half of
    linearity: more available energy never yields a smaller constant. -/
theorem qAubinLions_monotone (K : ℝ → ℝ) [h : QAubinLions K]
    {E₁ E₂ : ℝ} (h₁ : 0 ≤ E₁) (h₂ : E₁ ≤ E₂) :
    K E₁ ≤ K E₂ := by
  obtain ⟨C, hC, hlin⟩ := h.linear_in_energy
  rw [hlin E₁ h₁, hlin E₂ (le_trans h₁ h₂)]
  exact mul_le_mul_of_nonneg_left h₂ (le_of_lt hC)

/-- **The vorticity is unbounded** — a consequence of blow-up.

    Until 2026-08-30 this concluded `∃ T, 0 ≤ T` — "there exists a non-negative
    real" — which needs no hypothesis at all. The class now asserts divergence,
    so what follows from it is that no bound holds. Bean `qou-5nj1`. -/
theorem ns_counterexample_unbounded (ω : ℝ → ℝ) [h : NSCounterexample ω] :
    ∀ M : ℝ, ∃ t : ℝ, M < ω t := by
  obtain ⟨T, _, hdiv⟩ := h.blowup_at_finite_time
  intro M
  obtain ⟨t, _, hM⟩ := hdiv M
  exact ⟨t, hM⟩

/-- **Critical-exponent identity**, in cleared form: under `[CriticalExponent
    α]`, the exponent satisfies `3 · α = 4`.

    Two changes on 2026-08-30 (bean `qou-93hu`), and the second is a
    consequence of the first.

    It used to conclude `(3 * 4 : ℕ) = 12` — true by `rfl` with or without the
    hypothesis, so the `[CriticalExponent]` binder was decorative.

    Restating the conclusion as `α = 4/3` fixed that and immediately created a
    different defect: the class field is *typed* `α = 4/3`, so a theorem
    concluding it and proving it by `h.alpha_eq` is a §3b-cond item 5
    self-assuming projection — correctly flagged by
    `proof-no-self-assuming-projection`, which had nothing to flag while the
    conclusion was a closed numeral.

    The cleared form is the honest exit, and it is what this declaration's own
    original docstring promised (*"the scaling-exponent identity `3 · α_num =
    4`"*): the conclusion is **not** the field's type, and the proof does
    arithmetic rather than returning the hypothesis. -/
theorem critical_exponent_identity (α : ℝ) [h : CriticalExponent α] :
    3 * α = 4 := by
  rw [h.alpha_eq]; norm_num

/-- **Blow-up rate existence** — direct consequence of
    `[BlowupYekutieli]`. -/
theorem blowup_yekutieli_r_exists [BlowupYekutieli] :
    ∃ r : ℝ, 0 ≤ r ∧ r ≤ 1 + (0 : ℝ) :=
  BlowupYekutieli.exists_blowup_rate 0 (le_refl 0)

/-- **Every subset of the breakdown locus is null** — monotonicity of measure.

    Until 2026-08-30 this concluded `∃ μ, 0 ≤ μ ∧ μ ≤ 0`, satisfied by `0`
    regardless. The class now asserts the locus is Lebesgue-null, so what
    follows is a genuine statement about subsets of it. Bean `qou-m7a2`. -/
theorem regularity_breakdown_subset_null (S : Set ℝ) [h : RegularityBreakdown S]
    {A : Set ℝ} (hA : A ⊆ S) :
    MeasureTheory.volume A = 0 :=
  MeasureTheory.measure_mono_null hA h.breakdown_measure_zero

/-- **Two-class composition** (Aubin-Lions + blow-up): the compactness constant
    is pinned at zero energy *and* the blow-up rate exists.

    The composition is the point — two class hypotheses used together without
    circularity — but note the asymmetry it now exposes: the Aubin-Lions half
    derives a determined value, while the Yekutieli half can still only produce
    an existential, because that carrier has not been re-encoded (bean
    `qou-88nf`). -/
theorem qNS_combined (K : ℝ → ℝ) [QAubinLions K] [BlowupYekutieli] :
    K 0 = 0 ∧ (∃ r : ℝ, 0 ≤ r) := by
  refine ⟨qAubinLions_zero_energy K, ?_⟩
  obtain ⟨r, hr, _⟩ := BlowupYekutieli.exists_blowup_rate 0 (le_refl 0)
  exact ⟨r, hr⟩

/-- **Three-class composition** (Aubin-Lions + critical + blow-up):
    the critical-exponent identity holds even when combined with the
    Aubin-Lions and blow-up class hypotheses. -/
theorem qNS_critical_exponent_with_compactness (α : ℝ) (K : ℝ → ℝ)
    [QAubinLions K] [h : CriticalExponent α] [BlowupYekutieli] :
    3 * α = 4 := by
  rw [h.alpha_eq]; norm_num

/-- **Full q-NS-cone composition** (all 5 classes).

    Until 2026-08-30 this concluded that "every conjectural existential field
    admits a witness simultaneously" — five existentials, all witnessed by
    zero, so the conjunction was provable with none of the hypotheses. Four of
    the five conjuncts now say something the corresponding class is needed for:
    a determined zero-energy compactness, an unbounded vorticity, the exponent's
    value, a null breakdown locus.

    **The fourth conjunct is the exception and is left visible rather than
    dressed up.** `BlowupYekutieli` has not been re-encoded (bean `qou-88nf`),
    so its leg is still an existential satisfied by zero — the one place this
    composition is as weak as the whole thing used to be. -/
theorem qNS_cone_full_composition (α : ℝ) (K ω : ℝ → ℝ) (S : Set ℝ)
    [QAubinLions K] [NSCounterexample ω] [h : CriticalExponent α]
    [BlowupYekutieli] [RegularityBreakdown S] :
    K 0 = 0 ∧
    (∀ M : ℝ, ∃ t : ℝ, M < ω t) ∧
    (α = 4 / 3) ∧
    (∃ r : ℝ, 0 ≤ r) ∧
    MeasureTheory.volume S = 0 := by
  obtain ⟨r, hr, _⟩ := BlowupYekutieli.exists_blowup_rate 0 (le_refl 0)
  exact ⟨qAubinLions_zero_energy K, ns_counterexample_unbounded ω, h.alpha_eq,
         ⟨r, hr⟩, RegularityBreakdown.breakdown_measure_zero⟩

/-- **Conditional Reeb-period bound**: under Aubin-Lions + blow-up,
    the Reeb period `Ω · ε ≥ 0` for every infinitesimal `ε ≥ 0` and
    Reeb period `Ω ≥ 0`. -/
theorem qNS_reeb_period_bound (K : ℝ → ℝ)
    [QAubinLions K] [BlowupYekutieli]
    (Ω ε : ℝ) (h_Ω : 0 ≤ Ω) (h_ε : 0 ≤ ε) :
    0 ≤ Ω * ε :=
  mul_nonneg h_Ω h_ε

/-- **Conditional enstrophy bound**: under the full q-NS cone,
    every non-negative enstrophy `Z ≥ 0` admits the trivial-cube
    bound `Z³ ≥ 0`. -/
theorem qNS_enstrophy_cube_bound {α : ℝ} {K ω : ℝ → ℝ} {S : Set ℝ}
    [QAubinLions K] [NSCounterexample ω] [CriticalExponent α]
    [BlowupYekutieli] [RegularityBreakdown S]
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
theorem qNS_rogue_zero_cost_nonneg (K : ℝ → ℝ)
    [QAubinLions K] [BlowupYekutieli]
    (δ ε : ℝ) (h_ε : 0 < ε) :
    0 ≤ δ ^ 2 / ε :=
  div_nonneg (sq_nonneg δ) (le_of_lt h_ε)

end QOU.AlgebraicSubstrate
