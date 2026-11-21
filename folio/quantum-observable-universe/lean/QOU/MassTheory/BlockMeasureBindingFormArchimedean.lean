/-
# The logarithmic binding form vanishes on an empty entangled support — archimedean companion

§7c split: `BlockMeasureFromFrobeniusPairing.lean` is generic over a commutative
ring / field; this file is the `ℝ` specialisation, because the corpus's
log-assembly binding form `B = −α · log(tr_M(atom) / tr_M(free))` needs `Real.log`.
Bean `qou-jfx8`, session `qou-0nrt`.

-- Ref: [leitner2026] prop:frobenius-pairing; def:markov-axioms-primitive
-/
import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Tactic.FieldSimp
import QOU.MassTheory.BlockMeasureFromFrobeniusPairing
import QOU.MassTheory.BranchingPushforwardMultiplicativity

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

namespace BranchingData

variable {A₁ A₂ A : Type*} [Ring A₁] [Ring A₂] [Ring A]
variable {Λ₁ Λ₂ Λ : Type*} [Fintype Λ₁] [Fintype Λ₂] [Fintype Λ]
variable (B : BranchingData ℝ A₁ A₂ A Λ₁ Λ₂ Λ)

/-- **The binding form is a function of the `y`-weighted entangled deviation alone.**
Against the free product of two marginals with non-vanishing traces,
`B = −α · log(1 + Σ_λ y_λ δ_λ / (tr_M(a) tr_M(b)))`. Nothing else about the composite
enters: two composites with the same weighted deviation bind identically. -/
theorem bindingForm_tensor_eq (α : ℝ) (atom : A) (a : A₁) (b : A₂)
    (ha : B.D₁.trM a ≠ 0) (hb : B.D₂.trM b ≠ 0) :
    B.D.bindingForm α atom (B.tensor a b)
      = -α * Real.log (1 + (∑ l, B.D.y l * B.deviation atom a b l) / (B.D₁.trM a * B.D₂.trM b)) := by
  unfold FrobeniusPairingData.bindingForm
  rw [B.trM_tensor, B.trM_eq_tensor_add_weighted_deviation atom a b]
  congr 2
  field_simp

end BranchingData

end QOU.MassTheory.BlockMeasure
