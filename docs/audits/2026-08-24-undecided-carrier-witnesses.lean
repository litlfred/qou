import Mathlib.Data.Real.Basic
import Mathlib.Tactic

/-! # Hand witnesses for the seven `undecided` self-contained Prop carriers

`scripts/vacuous-prop-carrier-probe.py --emit` left these seven undecided: its
generic tactic list only ever tries the witness `0`, and six of the seven need
`1` or a constant function. That is why a failed probe settles nothing.

Six are inhabited outright. The seventh asserts `False` and is the honest
opposite of a vacuous carrier -- deliberately uninhabitable. -/

set_option linter.unusedVariables false

namespace UndecidedCarrierWitnesses

-- QOU.FluidDynamics.QAubinLions  (fluid-dynamics/q-aubin-lions.lean:43)
class QAubinLions : Prop where
  compactness_threshold : ∃ q_thresh : ℝ, q_thresh > 0
theorem w_qAubinLions : QAubinLions := ⟨⟨1, by norm_num⟩⟩

-- QOU.FluidDynamics.RegularityBreakdown  (fluid-dynamics/regularity-breakdown.lean:43)
class RegularityBreakdown : Prop where
  critical_reynolds : ∃ Re_c : ℝ, Re_c > 0
theorem w_regularityBreakdown : RegularityBreakdown := ⟨⟨1, by norm_num⟩⟩

-- QOU.AlgebraicSubstrate.PvsNPQou  (lean/QOU/AlgebraicSubstrate/PvsNPQou.lean:52)
class PvsNPQou : Prop where
  strict_separation : ∀ (eps : ℝ), 0 < eps → ∃ s : ℝ, 0 < s ∧ s ≤ eps
  noncompressible : ∃ s0 : ℝ, 0 < s0
theorem w_pvsNPQou : PvsNPQou :=
  ⟨fun eps h => ⟨eps, h, le_refl eps⟩, ⟨1, by norm_num⟩⟩

-- QOU.FeynmanClassicalLimit.…​.ClassicalLimitStpart  (mass-theory/feynman-classical-limit.lean:50)
class ClassicalLimitStpart : Prop where
  jones_trivial_at_one : ∃ jonesAtOne : ℕ → ℝ, ∀ K : ℕ, jonesAtOne K = 1
theorem w_classicalLimitStpart : ClassicalLimitStpart := ⟨⟨fun _ => 1, fun _ => rfl⟩⟩

-- QOU.BraidKnot.…​.CrystalGraphRealization  (mass-theory/transfer-matrix-level-independence.lean:120)
class CrystalGraphRealization : Prop where
  highest_weight : ∃ raise : ℕ → ℤ, ∀ i : ℕ, raise i = 0
theorem w_crystalGraphRealization : CrystalGraphRealization := ⟨⟨fun _ => 0, fun _ => rfl⟩⟩

-- QOU.BraidKnot.…​.QIntegerMassFormula  (mass-theory/wigner-coefficient-derivation.lean:70)
class QIntegerMassFormula : Prop where
  coeffs_are_q_rational :
    ∀ (m_e : ℝ), 0 ≤ m_e → ∀ _c : ℕ, ∃ r : ℝ, 0 ≤ r ∧ ∃ value : ℝ, value = r * m_e
theorem w_qIntegerMassFormula : QIntegerMassFormula :=
  ⟨fun m_e h _c => ⟨0, le_refl 0, 0 * m_e, rfl⟩⟩

#print axioms w_qAubinLions
#print axioms w_pvsNPQou
#print axioms w_qIntegerMassFormula

/-! ## The seventh is the honest opposite

`QOU.Machinery.SeparateLambdaScale_Antipattern` has the single field
`is_antipattern : False`. It is not vacuous -- it is deliberately
UNINHABITABLE, marking a construction the corpus forbids (the purged
`λ_scale`). A carrier that cannot be inhabited says the most a carrier can. -/

class SeparateLambdaScale_Antipattern : Prop where
  is_antipattern : False

-- Uninhabitable, so it can only be USED, never proved:
example (h : SeparateLambdaScale_Antipattern) : (0 : ℕ) = 1 := absurd h.is_antipattern not_false

end UndecidedCarrierWitnesses
