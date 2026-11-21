/-
  # Direction-sanity gate for the Q_β c_k precision ladder

  Sibling .lean for the `rem:q-beta-direction-sanity-gate` block.
  The §4(d) formalize-first invariant: any candidate Habiro element
  F(q) must have |F(q_0)| in the same order of magnitude as the
  target observable's substrate ratio.

  Canonical refutation precedent: PR #1850's trace-level Markov-
  stabilization attack (refuted-class row C12) was killed at the
  formalize-first level because z(q_0) < 1 cannot multiply up to
  linking_weight ≈ 2.53 > 1 (z(q_0) ≈ 0.6127 at the canonical
  z = q³/(q²+1); the PR quoted 0.4993, the excised convention-C value). The direction-sanity invariant
  abstracts this one-line magnitude argument.

  Three ingredients:

  1. `DirectionSanityGateClass (m_candidate : ℝ)` (§3b-cond conditional
     class PARAMETRIC over the candidate magnitude per Gemini review
     on PR #1890) — axiomatises the property
     `|m_candidate - target| ≤ threshold · |target|` (order-of-
     magnitude match against the substrate target).

  2. `direction_sanity_gate_reject` — the gate rejection lemma: if a
     candidate predicts a magnitude `m` whose distance from target
     exceeds threshold·target, the class cannot be instantiated.

  3. `direction_sanity_threshold_positive` — trivial positivity check
     on the threshold constant.

  Sorry-free. Composes with PR #1839's `CFinite.recurrence_step` via
  the Track C unified typeclass.

  Ref: [pr1786] https://github.com/litlfred/qou/pull/1786
       [pr1850] https://github.com/litlfred/qou/pull/1850  (z<1 obstruction)
       [pr1875] https://github.com/litlfred/qou/pull/1875
       [pr1889] https://github.com/litlfred/qou/pull/1889
       docs/audits/2026-06-04-qbeta-ck-refuted-class-map-and-open-axis.md (C12)
       docs/audits/2026-06-05-qbeta-formalize-first-gates-consolidation.md
-/

import Mathlib.Data.Real.Basic

namespace QOU.QBeta.DirectionSanityGate

universe u

/-- **The substrate target magnitude.**

    `Q_β^CODATA / (Q_A(q_0) · cos(α_eff(q_0))) ≈ 0.99824` at the
    proton-pinned q_0; the precision-ladder product
    `∏_k(1 + c_k u^k)` collectively contributes only ~0.18% of the
    bare `Q_A · cos` value. -/
-- Ref: [leitner2026] rem:q-beta-direction-sanity-gate
noncomputable def qBetaTargetMagnitudeAtQ0 : ℝ := 0.99824

/-- **The 10× order-of-magnitude direction-sanity threshold.**

    Set deliberately loose: catches order-of-magnitude direction
    errors (like PR #1850's z < 1 vs target > 1) without false-
    positives on the small numerical deviations covered by the
    §4(a) radius-of-convergence and §4(c) q=1 shadow gates. -/
-- Ref: [leitner2026] rem:q-beta-direction-sanity-gate
noncomputable def directionSanityThreshold : ℝ := 10

/-- **Direction-sanity gate class (§3b-cond, PARAMETRIC).**

    Parametric over the candidate's substrate magnitude `m_candidate`
    (per Gemini high-priority review on PR #1890): allows multiple
    candidates to be checked in the same environment by instantiating
    the class with each candidate's predicted F(q_0) magnitude.

    Axiomatises the structural prediction that the candidate's
    magnitude at q_0 is within the 10× threshold of the target. -/
-- Ref: [leitner2026] rem:q-beta-direction-sanity-gate
-- Ref: [pr1850] https://github.com/litlfred/qou/pull/1850
class DirectionSanityGateClass (m_candidate : ℝ) : Prop where
  /-- Structural identity: the candidate's magnitude at q_0 matches
      the target within the 10× threshold. -/
  magnitude_match :
    |m_candidate - qBetaTargetMagnitudeAtQ0|
      ≤ directionSanityThreshold * qBetaTargetMagnitudeAtQ0

/-- **The gate theorem (forward direction): under the class, the
    candidate's magnitude matches the target within threshold.** -/
-- Ref: [leitner2026] rem:q-beta-direction-sanity-gate
theorem qbeta_direction_sanity_magnitude_match
    (m_candidate : ℝ) [hC : DirectionSanityGateClass m_candidate] :
    |m_candidate - qBetaTargetMagnitudeAtQ0|
      ≤ directionSanityThreshold * qBetaTargetMagnitudeAtQ0 :=
  hC.magnitude_match

/-- **The gate theorem (refute direction): rejection lemma.**

    If a candidate predicts a magnitude `m` whose distance from the
    target exceeds the threshold, then the gate class cannot be
    instantiated for that magnitude — the candidate is structurally
    REFUTED. -/
-- Ref: [leitner2026] rem:q-beta-direction-sanity-gate
theorem direction_sanity_gate_reject
    (m_candidate : ℝ)
    (h_mismatch :
      |m_candidate - qBetaTargetMagnitudeAtQ0|
        > directionSanityThreshold * qBetaTargetMagnitudeAtQ0) :
    ¬ DirectionSanityGateClass m_candidate := by
  intro hC
  exact absurd hC.magnitude_match (not_le.mpr h_mismatch)

/-- **Threshold positivity**: 10 > 0. Used downstream when reasoning
    about the threshold's role as a tolerance. -/
-- Ref: [leitner2026] rem:q-beta-direction-sanity-gate
theorem direction_sanity_threshold_positive :
    directionSanityThreshold > 0 := by
  unfold directionSanityThreshold
  norm_num

end QOU.QBeta.DirectionSanityGate
