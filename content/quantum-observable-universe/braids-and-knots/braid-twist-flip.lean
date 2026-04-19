/-!
# QOU.BraidTwistFlip

Two involutions on 4-tuples: twist σ₁(w) = (w₂,w₁,w₄,w₃)
and flip σ₂(w) = (w₄,w₃,w₂,w₁), generating the Klein four-group V₄.

LaTeX label: `def:braid-twist-flip`

## References

- [manuscript] Chapter 4, §Braid involutions
-/

import QOU.Basic
import Mathlib.Data.Fin.Basic

namespace QOU

/-- The twist permutation on {0,1,2,3}: 0↔1, 2↔3. -/
-- Ref: [manuscript] Chapter 4
def twistPerm : Fin 4 → Fin 4
  | ⟨0, _⟩ => ⟨1, by omega⟩
  | ⟨1, _⟩ => ⟨0, by omega⟩
  | ⟨2, _⟩ => ⟨3, by omega⟩
  | ⟨3, _⟩ => ⟨2, by omega⟩

/-- The flip permutation on {0,1,2,3}: 0↔3, 1↔2. -/
-- Ref: [manuscript] Chapter 4
def flipPerm : Fin 4 → Fin 4
  | ⟨0, _⟩ => ⟨3, by omega⟩
  | ⟨1, _⟩ => ⟨2, by omega⟩
  | ⟨2, _⟩ => ⟨1, by omega⟩
  | ⟨3, _⟩ => ⟨0, by omega⟩

/-- Twist is an involution. -/
-- Ref: [manuscript] Chapter 4
theorem twistPerm_involution (i : Fin 4) : twistPerm (twistPerm i) = i := by
  fin_cases i <;> rfl

/-- Flip is an involution. -/
-- Ref: [manuscript] Chapter 4
theorem flipPerm_involution (i : Fin 4) : flipPerm (flipPerm i) = i := by
  fin_cases i <;> rfl

/-- Twist and flip commute (generate V₄ = ℤ/2 × ℤ/2). -/
-- Ref: [manuscript] Chapter 4
theorem twist_flip_comm (i : Fin 4) :
    twistPerm (flipPerm i) = flipPerm (twistPerm i) := by
  fin_cases i <;> rfl


/-- **def:braid-twist-flip** — placeholder stub; full definition TBD. -/
structure BraidTwistFlip where
  witness : ℝ
  witness_pos : 0 < witness
end QOU
