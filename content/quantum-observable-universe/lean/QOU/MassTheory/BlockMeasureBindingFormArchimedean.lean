/-
# The logarithmic binding form vanishes on an empty entangled support — archimedean companion

§7c split: `BlockMeasureFromFrobeniusPairing.lean` is generic over a commutative
ring / field; this file is the `ℝ` specialisation, because the corpus's
log-assembly binding form `B = −α · log(tr_M(atom) / tr_M(free))` needs `Real.log`.
Bean `qou-jfx8`, session `qou-0nrt`.

-- Ref: [manuscript] prop:frobenius-pairing; def:markov-axioms-primitive
-/
import Mathlib.Analysis.SpecialFunctions.Log.Basic
import QOU.MassTheory.BlockMeasureFromFrobeniusPairing

namespace QOU.MassTheory.BlockMeasure

namespace FrobeniusPairingData

variable {A : Type*} [Ring A] {Λ : Type*} [Fintype Λ]
variable (D : FrobeniusPairingData ℝ A Λ)

/-- The logarithmic binding form `B = −α · log(tr_M(atom) / tr_M(free))` used by the
corpus's log-assembly binding routes. -/
noncomputable def bindingForm (α : ℝ) (atom free : A) : ℝ :=
  -α * Real.log (D.trM atom / D.trM free)

/-- **No shared block, no binding.** If the bound word and its free constituent
product agree on every block character, the logarithmic binding vanishes. The
contrapositive: a nonzero binding forces a block on which the two characters
differ — the "entangled" block set is non-empty. -/
theorem bindingForm_eq_zero_of_entangledSupp_empty (α : ℝ) {atom free : A}
    (h : D.entangledSupp atom free = ∅) (hfree : D.trM free ≠ 0) :
    D.bindingForm α atom free = 0 := by
  unfold bindingForm
  rw [D.trM_eq_of_entangledSupp_empty h, div_self hfree, Real.log_one, mul_zero]


end FrobeniusPairingData

end QOU.MassTheory.BlockMeasure
