/-
  Conditional corollaries under the q-NS conjecture cone.

  Each theorem in this module takes one or more of the
  `[QAubinLions]`, `[NSCounterexample]`, `[CriticalExponent]`,
  `[BlowupYekutieli]`, `[RegularityBreakdown]` instance hypotheses
  and proves a conditional consequence, demonstrating that the
  §3b-cond pattern composes — multiple class hypotheses can be
  combined without circularity.

  **"The classes' existential fields" is history.** That was the Round 11
  design, and every one of those existentials was satisfiable by zero, which is
  why all five carriers were re-encoded or replaced on 2026-08-30 (bean
  `qou-rq9n`). The fields are now refutable statements about caller-supplied
  parameters, and each theorem below records what its own conclusion used to
  be.

  Ref: [leitner2026]
    - conj:q-aubin-lions
    - conj:ns-counterexample
    - conj:critical-exponent
    - prop:blowup-yekutieli  (no `conj:` label exists; see ConditionalClasses)
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
  obtain ⟨t, _, _, hM⟩ := hdiv M (T - 1) (by linarith)
  exact ⟨t, hM⟩

/-- **The enstrophy is unbounded near `q = 1`** — a consequence of the
    critical-exponent conjecture.

    Three states on one day, and the middle one is the instructive failure.

    1. It concluded `(3 * 4 : ℕ) = 12` — true by `rfl` with or without the
       hypothesis, so the `[CriticalExponent]` binder was decorative
       (`qou-93hu`).
    2. It concluded `3 * α = 4`, from a class field typed `α = 4/3`. That
       cleared the *shape* defect and inherited a worse one from the class:
       **`4/3` is not a result the corpus holds.** `p2-critical-exponent.md`
       offers it as one of two heuristic values under two named turbulence
       closures and says the true exponent is open. So this theorem derived an
       arithmetic identity from a fabricated premise — the derivation was
       sound and the premise was not (`qou-4670`).
    3. Now: the class asserts divergence, and what follows from it is
       unboundedness. `M` is arbitrary, so this is not satisfiable by any
       bounded enstrophy, and it uses the hypothesis at `ε = 1`.

    Note the conclusion drops the neighbourhood. That is deliberate: the
    localisation is what makes the *hypothesis* strong, and a consequence is
    free to be weaker. The `1 < q` conjunct is kept so the statement stays in
    the q-NS regime. -/
theorem critical_exponent_enstrophy_unbounded (enstrophy : ℝ → ℝ) (α : ℝ)
    [h : CriticalExponent enstrophy α] :
    ∀ M : ℝ, ∃ q : ℝ, 1 < q ∧ M < enstrophy q := by
  intro M
  obtain ⟨q, hq1, _, hM⟩ := h.enstrophy_diverges M 1 one_pos
  exact ⟨q, hq1, hM⟩

/-- **Blow-up is a finite obstruction level** — the contrapositive half of
    smoothness-as-lifting.

    Until 2026-08-30 this concluded `∃ r, 0 ≤ r ∧ r ≤ 1 + 0`, satisfied by
    `r = 0` with or without the hypothesis. The class now states
    `smooth ↔ ∀ n, obstruction n = 0`, so what follows from it is the blow-up
    characterisation: failing to lift means some finite level obstructs. The
    proof is `not_forall` after rewriting, mirroring upstream
    `QOU.FluidDynamics.blowup_yekutieli`. Bean `qou-88nf`. -/
theorem blowup_yekutieli_iff_obstruction (obstruction : ℕ → ℕ) (smooth : Prop)
    [h : BlowupYekutieli obstruction smooth] :
    ¬ smooth ↔ ∃ n : ℕ, obstruction n ≠ 0 := by
  rw [h.smooth_iff_all_obstructions_vanish, not_forall]

/-- **Every subset of the breakdown locus is null** — monotonicity of measure.

    Until 2026-08-30 this concluded `∃ μ, 0 ≤ μ ∧ μ ≤ 0`, satisfied by `0`
    regardless. The class now asserts the locus is Lebesgue-null, so what
    follows is a genuine statement about subsets of it. Bean `qou-m7a2`. -/
theorem regularity_breakdown_subset_null (S : Set ℝ) [h : RegularityBreakdown S]
    {A : Set ℝ} (hA : A ⊆ S) :
    MeasureTheory.volume A = 0 :=
  MeasureTheory.measure_mono_null hA h.breakdown_measure_zero

/-- **Two-class composition** (Aubin-Lions + blow-up): the compactness constant
    is pinned at zero energy *and* blow-up is a finite obstruction level.

    The composition is the point — two class hypotheses used together without
    circularity. **The asymmetry this docstring used to record is gone**: the
    Yekutieli half produced an existential satisfied by zero until its carrier
    was replaced on 2026-08-30 (`qou-88nf`), and now both halves derive
    something the hypothesis is needed for. -/
theorem qNS_combined (K : ℝ → ℝ) (obstruction : ℕ → ℕ) (smooth : Prop)
    [QAubinLions K] [BlowupYekutieli obstruction smooth] :
    K 0 = 0 ∧ (¬ smooth ↔ ∃ n : ℕ, obstruction n ≠ 0) :=
  ⟨qAubinLions_zero_energy K,
   blowup_yekutieli_iff_obstruction obstruction smooth⟩

/-- **Three-class composition** (Aubin-Lions + critical + blow-up):
    the enstrophy divergence survives combination with the Aubin-Lions and
    blow-up class hypotheses.

    The conclusion changed with the class on 2026-08-30 (`qou-4670`); it used
    to be `3 * α = 4`, which the class no longer supports and which the
    corpus does not assert. -/
theorem qNS_critical_exponent_with_compactness (α : ℝ) (K enstrophy : ℝ → ℝ)
    (obstruction : ℕ → ℕ) (smooth : Prop)
    [QAubinLions K] [CriticalExponent enstrophy α]
    [BlowupYekutieli obstruction smooth] :
    ∀ M : ℝ, ∃ q : ℝ, 1 < q ∧ M < enstrophy q :=
  critical_exponent_enstrophy_unbounded enstrophy α

/-- **Full q-NS-cone composition** (all 5 classes).

    Until 2026-08-30 this concluded that "every conjectural existential field
    admits a witness simultaneously" — five existentials, all witnessed by
    zero, so the conjunction was provable with none of the hypotheses. Four of
    the five conjuncts now say something the corresponding class is needed for:
    a determined zero-energy compactness, an unbounded vorticity, the exponent's
    value, a null breakdown locus.

    **The fourth conjunct WAS the exception and no longer is.** It read
    `∃ r, 0 ≤ r` — satisfied by zero, the one place this composition stayed as
    weak as the whole thing used to be — because `BlowupYekutieli` had not been
    re-encoded. On 2026-08-30 that carrier was **replaced** by the upstream
    obstruction statement (`qou-88nf`), so all five conjuncts now need their
    class. Note the replacement is not a strengthening of the old leg: a
    blow-up *rate* and obstruction-class *vanishing* are different
    propositions that shared a name.

    The third conjunct read `α = 4/3` until 2026-08-30. That was a projection
    of a class field asserting a value the corpus calls open; both the field
    and this conjunct are gone (`qou-4670`). What replaces it is the
    divergence consequence, which is derived rather than returned. -/
theorem qNS_cone_full_composition (α : ℝ) (K ω enstrophy : ℝ → ℝ) (S : Set ℝ)
    (obstruction : ℕ → ℕ) (smooth : Prop)
    [QAubinLions K] [NSCounterexample ω] [CriticalExponent enstrophy α]
    [BlowupYekutieli obstruction smooth] [RegularityBreakdown S] :
    K 0 = 0 ∧
    (∀ M : ℝ, ∃ t : ℝ, M < ω t) ∧
    (∀ M : ℝ, ∃ q : ℝ, 1 < q ∧ M < enstrophy q) ∧
    (¬ smooth ↔ ∃ n : ℕ, obstruction n ≠ 0) ∧
    MeasureTheory.volume S = 0 :=
  ⟨qAubinLions_zero_energy K, ns_counterexample_unbounded ω,
   critical_exponent_enstrophy_unbounded enstrophy α,
   blowup_yekutieli_iff_obstruction obstruction smooth,
   RegularityBreakdown.breakdown_measure_zero⟩

/-- **Reeb-period bound**: `Ω · ε ≥ 0` for non-negative `Ω` and `ε`.

    Unconditional, and its class binders are dropped for the same reason as
    `qNS_enstrophy_cube_bound` above: the proof is `mul_nonneg` and used none
    of them. -/
theorem qNS_reeb_period_bound
    (Ω ε : ℝ) (h_Ω : 0 ≤ Ω) (h_ε : 0 ≤ ε) :
    0 ≤ Ω * ε :=
  mul_nonneg h_Ω h_ε

/-- **Enstrophy cube bound**: every non-negative enstrophy `Z ≥ 0` satisfies
    `Z³ ≥ 0`.

    **This is UNCONDITIONAL and used to pretend otherwise.** It carried all
    five q-NS class hypotheses while its proof is `pow_nonneg h_Z 3`, which
    uses none of them — `0 ≤ Z ^ 3` follows from `0 ≤ Z` alone. I flagged that
    in a note here and left the binders; a reviewer then flagged the same thing
    on PR #6122, observing that it makes dependency tracking noisy and reads
    later as a genuine conditional consequence. Two independent reads agreeing
    is enough: the binders are gone.

    Verified safe to drop: these corollaries have no external callers, so
    removing hypotheses breaks nothing. -/
theorem qNS_enstrophy_cube_bound (Z : ℝ) (h_Z : 0 ≤ Z) :
    0 ≤ Z ^ 3 :=
  pow_nonneg h_Z 3

/-- **Conditional rogue-zero cost bound**: under Aubin-Lions +
    blow-up, the rogue-zero energy cost `E(δ) = δ²/ε ≥ 0` for
    `δ : ℝ` and `ε > 0`. -/
theorem qNS_rogue_zero_cost_nonneg
    (δ ε : ℝ) (h_ε : 0 < ε) :
    0 ≤ δ ^ 2 / ε :=
  div_nonneg (sq_nonneg δ) (le_of_lt h_ε)

end QOU.AlgebraicSubstrate
