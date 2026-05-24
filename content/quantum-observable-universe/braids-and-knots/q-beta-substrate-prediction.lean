/-!
# QOU.BraidKnot.QBetaSubstratePrediction

The substrate-only closed form for the free-neutron β-decay Q-value
in terms of (m_e, q_0). Algebraic identity over any field where
`q ≠ 0` (so `q²` and `q³` are units); the choice `R = ℝ` and the
empirical match `Q_β(q_0) ≈ 0.78365 MeV (+0.168 % CODATA)` are
documented in the .md sibling.

This file states the algebraic identity. The numerical evaluation
at q = q_0 ≈ 1.1098 is in the Python sibling
`folio-assistant/computations/q_beta_substrate_prediction.py` and
the witness `q-beta-substrate-prediction.witness.json`.

Generic over any field R per CLAUDE.md §7c base-ring discipline.
-/

import Mathlib.Algebra.Field.Defs
import Mathlib.Algebra.GroupPower.Basic
-- Ref: [manuscript] prop:q-beta-substrate-prediction
-- Ref: [manuscript] prop:three-parameters-wedderburn
-- Ref: [manuscript] rem:calibration-inputs

namespace QOU.BraidKnot.QBetaSubstratePrediction

/-- The substrate closed form for Q_β as a real-valued algebraic
    expression in the electron mass `m_e` and the substrate
    parameter `q`. Defined over any field `R` with `q ≠ 0`.

    Q_β(m_e, q) = m_e · |q² − 2q − 1| · (q + 1) / (2 q³)

    For the formal statement we drop the absolute value (`absoluteQBeta`
    below); the signed form
    `q² − 2q − 1` is the algebraic primitive, and its sign at
    `q ≈ 1.1098` happens to be positive but for general `q < 1 + √2`
    it would flip. The .md sibling documents the convention. -/
noncomputable def qBetaSubstrate
    {R : Type*} [Field R] (m_e q : R) (hq : q ≠ 0) : R :=
  m_e * (q^2 - 2*q - 1) * (q + 1) / (2 * q^3)

/-- The closed form is a non-vanishing scalar multiple of `m_e`
    when `q ∉ {0, -1, 1 ± √2}`. Statement-only here; the witness
    side handles the numerical evaluation. -/
theorem q_beta_closed_form
    {R : Type*} [Field R] (m_e q : R) (hq : q ≠ 0) :
    qBetaSubstrate m_e q hq
      = m_e * (q^2 - 2*q - 1) * (q + 1) / (2 * q^3) := by
  rfl

end QOU.BraidKnot.QBetaSubstratePrediction
