/-
Copyright (c) 2026 Frederick Carl Leitner. All rights reserved.
-/
import Mathlib.Data.Real.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring

/-!
# QOU.BraidsAndKnots.FBorBorromeanObservable

The Borromean categorical observable

  `F_Bor(q) := |tr_M(β_Bor, q)| · [3]_q! / q³`

built from the Lean-proved closed forms

  `|tr_M(β_Bor, q)| = (4 + h² − 3h⁴ − h⁶) / (h² + 4)`
    (proved upstream in `BorromeanMarkovTrace.lean` — restated as
     `trM_borromean_abs` for self-contained use)

  `[3]_q! = (q² + 1 + q⁻²)(q + q⁻¹)`
    (proved upstream in `YLambdaQSchur.lean` `qFactorial_three` —
     restated as `qFact_three` for self-contained use)

The structural-integer identifications

  `bar_pair_factor_two_categorical = 2 = dim V_{(2,1)}`
  `ocneanu_factor_twelve_categorical = 12 = |S_3| · dim V_{(2,1)} = 6 · 2`

attach to this observable. They are categorical (group dimensions and
orders) and carry no archimedean information.

The archimedean substrate evaluation
  `m_p = 2 · m_μ · F_Bor(q_0) − 12 · m_e`
lives in `appendix-qvalues/proton-mass-substrate-identity.lean`, which
imports this module.

Refs:
  - docs/audits/2026-05-25-proton-mass-identity-12-me-ocneanu.md
  - PR #1272 (origin), PR #546 (Hoefsmit symbolic for −1/12)
-/

namespace QOU.BraidsAndKnots

/-- The Borromean Markov-trace closed form
    `|tr_M(β_Bor, q)| = (4 + h² − 3h⁴ − h⁶) / (h² + 4)`.

    Mirror of the proved `trM_borromean` in
    `BorromeanMarkovTrace.lean` (restated here for self-contained
    use in the F_Bor observable). -/
noncomputable def trM_borromean_abs (h : ℝ) : ℝ :=
  |(4 + h^2 - 3 * h^4 - h^6) / (h^2 + 4)|

/-- The q-factorial `[3]_q! = (q² + 1 + q⁻²)(q + q⁻¹)`.

    Mirror of the proved `qFactorial_three` from `YLambdaQSchur.lean`
    (restated here for self-contained use). -/
noncomputable def qFact_three (q : ℝ) : ℝ :=
  (q^2 + 1 + q^(-2 : ℤ)) * (q + q⁻¹)

/-- The natural categorical observable
    `F_Bor(q) := |tr_M(β_Bor, q)| · [3]_q! / q^3`.

    Combines the Lean-proved Borromean Markov trace with the
    q-factorial normalisation, shifted by content q^3 (the content
    sum of the partition (3) ⊢ 3). -/
noncomputable def F_Bor (q : ℝ) : ℝ :=
  trM_borromean_abs (q - q⁻¹) * qFact_three q / q^3

/-- **Bar-pair partition count (categorical).**

    The integer 2 in the F_Bor-based substrate identity counts the
    bar-pair partitions in the proton's H_3(q) Wedderburn
    decomposition: (3) and (1,1,1) form a transpose pair under bar
    involution.

    Proved upstream in `YLambdaQSchur.lean
    yLambdaQSchur_transpose_pair`:
      y_(3)(q) · y_{(3)^T}(q) = 1/[3]_q!²

    where (3)^T = (1,1,1).  The bar-pair has exactly 2 elements;
    self-conjugate (2,1) is the third partition of 3 not in this
    pair.

    The bridge from this combinatorial fact to the "factor 2 in
    the mass formula" is the open structural step. -/
def bar_pair_factor_two_categorical : ℕ := 2

/-- **Ocneanu cancellation reciprocal (categorical).**

    The integer 12 in the F_Bor-based substrate identity is the
    inverse of the leading-pole coefficient −1/12 of
    `tr_M(β_Bor, q) ~ −1/(12 · q^10)` as q → 0.

    Verified to 200 dps in PR #546's Hoefsmit symbolic work;
    the symbolic identity itself awaits PR #546's 2×2 bug fix
    for full categorical proof.

    Ref: docs/audits/2026-05-04-ocneanu-cancellation-numerical-verification.md
    -/
def ocneanu_factor_twelve_categorical : ℕ := 12

end QOU.BraidsAndKnots
