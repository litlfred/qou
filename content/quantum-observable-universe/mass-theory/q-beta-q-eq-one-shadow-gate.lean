/-
  # q = 1 classical-limit shadow gate for the Q_β c_k precision ladder

  Sibling .lean for the `prop:q-beta-q-eq-one-shadow-gate` block.
  The §4(c) formalize-first invariant: any candidate Habiro element
  F(q) must reproduce the canonical integer shadows at q = 1:

    lim_{q → 1} c_2(q) = -1       (PR #1786 Taylor-exact anchor)
    lim_{q → 1} c_3(q) = -2       (J_Hopf(q=1), registry §3 anchor)

  Three ingredients:

  1. `QOneShadowGateClass (c2 c3 : ℝ → ℝ)` (§3b-cond conditional class
     PARAMETRIC over the candidate coefficient functions per Gemini
     review) — axiomatises the property "c_2(1) = -1 AND c_3(1) = -2"
     as two field hypotheses encoding the canonical anchors. Parametric
     so any future kernel candidate can be checked by instantiating
     with its own (c_2, c_3) pair.

  2. `q_eq_one_shadow_gate_reject_c2` / `_c3` — the gate rejection
     lemmas: if a candidate's (c_2 1, c_3 1) disagrees with the
     canonical anchors, the class cannot be instantiated.

  3. `hopf_jones_at_q_one_unfolds` — trivial unfolding helper.

  Sorry-free. Composes with PR #1839's `CFinite.recurrence_step` via
  the Track C unified typeclass.

  Ref: [pr1786] https://github.com/litlfred/qou/pull/1786
       [pr1875] https://github.com/litlfred/qou/pull/1875
       [pr1889] https://github.com/litlfred/qou/pull/1889
       [jones1985] https://doi.org/10.2307/1971403  (Hopf Jones)
       [habiro2004] https://doi.org/10.4310/MRL.2004.v11.n4.a4
       docs/audits/2026-06-04-qbeta-ck-refuted-class-map-and-open-axis.md
       docs/audits/2026-06-05-qbeta-formalize-first-gates-consolidation.md
-/

import Mathlib.Data.Real.Basic

namespace QOU.QBeta.QOneShadowGate

universe u

/-- **The canonical Hopf-Jones classical value.**

    `J_Hopf(q = 1) = -2` is the categorical anchor for the inter-block
    N=3 correction; recorded as a definitional constant. -/
-- Ref: [jones1985] doi:10.2307/1971403
noncomputable def hopfJonesAtQOne : ℝ := -2

/-- **q = 1 classical-limit shadow gate class (§3b-cond, PARAMETRIC).**

    Parametric over the candidate coefficient functions `c2 c3 : ℝ → ℝ`
    (per Gemini high-priority review on PR #1890): this allows any
    future kernel candidate to be checked by instantiating the class
    with its own coefficient pair, rather than locking the class to a
    single global axiom. This is essential for the Track C unified
    typeclass composition.

    Axiomatises both canonical integer shadows in a single class:
    `c2 1 = -1` (PR #1786 Taylor-exact) and `c3 1 = -2 = J_Hopf(1)`
    (registry §3 anchor). A candidate must satisfy BOTH to instantiate
    the class. -/
-- Ref: [manuscript] prop:q-beta-q-eq-one-shadow-gate
-- Ref: [pr1786] https://github.com/litlfred/qou/pull/1786
class QOneShadowGateClass (c2 c3 : ℝ → ℝ) : Prop where
  /-- The c_2 classical-limit shadow equals the PR #1786 anchor `-1`. -/
  c2_at_one_eq_neg_one : c2 1 = -1
  /-- The c_3 classical-limit shadow equals the Hopf-Jones value `-2`. -/
  c3_at_one_eq_jones_hopf : c3 1 = hopfJonesAtQOne

/-- **The gate theorem (forward direction): under the class, the
    candidate's q=1 shadows match the canonical anchors.**

    Routine restatement of the class fields; the value of formalising
    is composition with downstream checks (cross-anchor swing, radius
    of convergence, bar-evenness). -/
-- Ref: [manuscript] prop:q-beta-q-eq-one-shadow-gate
def qbeta_q_eq_one_shadow_anchors
    (c2 c3 : ℝ → ℝ) [hC : QOneShadowGateClass c2 c3] :
    c2 1 = -1 ∧ c3 1 = hopfJonesAtQOne :=
  ⟨hC.c2_at_one_eq_neg_one, hC.c3_at_one_eq_jones_hopf⟩

/-- **The gate theorem (refute direction, c_2 failure): rejection
    lemma when the c_2 shadow is wrong.**

    If a candidate predicts `c2 1 = a` with `a ≠ -1`, then the class
    cannot be instantiated for `(c2, c3)`. -/
-- Ref: [manuscript] prop:q-beta-q-eq-one-shadow-gate
theorem q_eq_one_shadow_gate_reject_c2
    (c2 c3 : ℝ → ℝ) (a : ℝ)
    (h_candidate_c2 : c2 1 = a) (h_mismatch : a ≠ -1) :
    ¬ QOneShadowGateClass c2 c3 := by
  intro hC
  have h_eq : a = -1 := by
    rw [← h_candidate_c2]
    exact hC.c2_at_one_eq_neg_one
  exact h_mismatch h_eq

/-- **The gate theorem (refute direction, c_3 failure): rejection
    lemma when the c_3 shadow is wrong.** -/
-- Ref: [manuscript] prop:q-beta-q-eq-one-shadow-gate
theorem q_eq_one_shadow_gate_reject_c3
    (c2 c3 : ℝ → ℝ) (a : ℝ)
    (h_candidate_c3 : c3 1 = a) (h_mismatch : a ≠ hopfJonesAtQOne) :
    ¬ QOneShadowGateClass c2 c3 := by
  intro hC
  have h_eq : a = hopfJonesAtQOne := by
    rw [← h_candidate_c3]
    exact hC.c3_at_one_eq_jones_hopf
  exact h_mismatch h_eq

/-- **Composition with the exact `J_Hopf(1) = -2` value**: the gate's
    c_3 anchor unfolds to the literal `-2` value. -/
-- Ref: [manuscript] prop:q-beta-q-eq-one-shadow-gate
theorem hopf_jones_at_q_one_unfolds :
    hopfJonesAtQOne = -2 := rfl

end QOU.QBeta.QOneShadowGate
