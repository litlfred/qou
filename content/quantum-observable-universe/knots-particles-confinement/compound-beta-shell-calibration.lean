import QOU.Basic


/-!
# QOU.BraidKnot.CompoundBetaShellCalibration
  — Compound β-decay calibration across magic shells

y_target(A_magic) is derived from β-decay Q-values via a chain
through the magic anchor.  For magic-crossing decays, the knot
operator differs between parent and daughter, so Q_β does not
directly give y_target; instead, a chain of Q-values along the
β-stability valley gives the cumulative contribution.

LaTeX: `\label{prop:compound-beta-shell-calibration}`
-/

namespace QOU.BraidKnot

universe u

/-- **Compound β-decay chain data.**

    A β-decay chain through a magic shell consists of:
      - Chain Q-values from AME data
      - Identification of which steps cross the magic boundary
      - Non-magic Q-values predictable from level-3 shadow prices
-/
structure CompoundBetaChain where
  A_magic : ℕ
  chain_Q_MeV : List Float       -- Q-values along the chain
  is_magic_crossing : List Bool  -- whether each step crosses the shell

/-- The reference E_0 is exactly 0.782 MeV. -/
def CompoundBetaChain.reference_E_0_MeV (_ : CompoundBetaChain) : Float := 0.782


/-! Both formulas below were `theorem … : ∃ x : Float, x = <rhs> := ⟨_, rfl⟩`
    until 2026-08-21.  Neither said anything: an existential naming a value
    of a total expression holds for every right-hand side, so the formula
    was never actually asserted — only written down.  They are `def`s now,
    which is what writing a formula down *is*.  `Float` admits no useful
    reasoning anyway (no `ring`, no associativity), so promoting them back
    to theorems would need the quantities to be `ℝ`-valued first; that is a
    larger change than this pass, and the `.ts` block is `not_checked`.  -/

/-- The Q-value of a magic-crossing β-decay:
    `Q_beta = E_0 * (|tr_M(parent)| - |tr_M(daughter)| - |tr_M(e^- + \bar\nu)|)`.
    The Q-value measures the difference of shell-operator contributions. -/
-- Ref: [manuscript] prop:compound-beta-shell-calibration
def magicCrossingQ
    (E_0 : Float) (tr_M_parent tr_M_daughter tr_M_leptons : Float) : Float :=
  E_0 * (tr_M_parent - tr_M_daughter - tr_M_leptons)

/-- **y_target extraction.**
    `y_target = [Σ (chain) Q - Σ (non-magic) Q^(3)] / (E_0 · A_magic)` -/
-- Ref: [manuscript] prop:compound-beta-shell-calibration
def compoundBetaYTarget
    (chain : CompoundBetaChain) (non_magic_Q_sum : Float) : Float :=
  (chain.chain_Q_MeV.sum - non_magic_Q_sum) /
    (chain.reference_E_0_MeV * chain.A_magic.toFloat)

/-- **Single-calibration framework invariant.**
    The framework uses only E_0 = 0.782 MeV as archimedean input. -/
-- Ref: [manuscript] prop:compound-beta-shell-calibration
theorem single_calibration_framework (chain : CompoundBetaChain) :
    chain.reference_E_0_MeV = 0.782 := by
  rfl

end QOU.BraidKnot
