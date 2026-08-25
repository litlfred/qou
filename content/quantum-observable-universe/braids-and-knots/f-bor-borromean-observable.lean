/-
Copyright (c) 2026 Frederick Carl Leitner. All rights reserved.
-/
import Mathlib.Algebra.Field.Basic
import Mathlib.Algebra.Order.Field.Basic

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
    use in the F_Bor observable).

    The `|·|` is the only post-archimedean construct (it requires an
    order), so the base ring is the generic linearly ordered field
    `[Field R] [LinearOrder R] [IsStrictOrderedRing R]` rather than
    `ℝ` — the archimedean evaluation at `q_0 : ℝ` happens downstream
    (§7c). -/
noncomputable def trM_borromean_abs {R : Type*} [Field R] [LinearOrder R]
    [IsStrictOrderedRing R] (h : R) : R :=
  |(4 + h^2 - 3 * h^4 - h^6) / (h^2 + 4)|

/-- The q-factorial `[3]_q! = (q² + 1 + q⁻²)(q + q⁻¹)`.

    Mirror of the proved `qFactorial_three` from `YLambdaQSchur.lean`
    (restated here for self-contained use). Purely categorical
    (field inverse + integer powers, no order), so the base ring is
    the weakest that admits the construction, `[Field R]` (§7c). -/
noncomputable def qFact_three {R : Type*} [Field R] (q : R) : R :=
  (q^2 + 1 + q^(-2 : ℤ)) * (q + q⁻¹)

/-- The natural categorical observable
    `F_Bor(q) := |tr_M(β_Bor, q)| · [3]_q! / q^3`.

    Combines the Lean-proved Borromean Markov trace with the
    q-factorial normalisation, shifted by content q^3 (the content
    sum of the partition (3) ⊢ 3).

    Inherits the linearly ordered field structure from
    `trM_borromean_abs`'s `|·|`; `qFact_three` (only `[Field R]`)
    composes on the shared `Field R`. The archimedean evaluation
    `F_Bor (q_0 : ℝ)` resolves with `R := ℝ` downstream. -/
noncomputable def F_Bor {R : Type*} [Field R] [LinearOrder R]
    [IsStrictOrderedRing R] (q : R) : R :=
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

/-- **The categorical integer 12 of the F_Bor substrate identity.**

    `12 = mult · bind = 2 · 6 = dim V_{(2,1)} · |S_3|` — a categorical count
    (trace-dominant irrep dimension times the symmetric-group order).

    HISTORICAL / REFUTED PROVENANCE: an earlier reading identified 12 as the
    inverse of an Ocneanu leading-pole coefficient −1/12, claiming
    `tr_M(β_Bor, q) ~ −1/(12 · q^10)` as q → 0. This is **refuted for β_Bor**:
    its Markov trace has a q^(-4) pole of coefficient 1, not q^(-10)·(−1/12)
    (the −1/12·q^(-10) pole belongs to the measured no-interface braid, a
    different word). Retracted 2026-05-25; re-confirmed in the 2026-08-22 F_Bor
    red-team (docs/audits/2026-08-22-mp-fbor-massformula-redteam.md). The −1/12
    provenance is NOT part of the derivation; only the categorical count `2 · 6`
    is. (Name retained for reference stability; the "ocneanu" in it is historical.)
    -/
def ocneanu_factor_twelve_categorical : ℕ := 12

end QOU.BraidsAndKnots
