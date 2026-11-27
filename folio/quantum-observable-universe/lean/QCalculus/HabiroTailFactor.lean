import Mathlib.Algebra.Field.Basic
import Mathlib.Tactic.Ring

/-!
# QCalculus.HabiroTailFactor — the 4₁ Habiro tail factor, algebraically

The `j`-th factor of the 4₁ Habiro cyclotomic tail, `(1 - q^j)(1 - q^{-j})`,
over any field `K`, and its bar-evenness (`q ↔ q⁻¹`). This is the algebraic
half of `QOU.Transcendental.QCalculus.HabiroTailAction`; the resurgent action
`π²/5` (dilogarithms, logarithms) stays behind the transcendental boundary.

Strangler step of bean `qou-gfsr` (item 5 of epic `qou-dk7p`). The
declaration names are kept so existing references resolve.
-/

namespace QOU.QBeta.HabiroTailAction

variable {K : Type*} [Field K]

/-- The `j`-th factor of the 4₁ Habiro cyclotomic tail:
    `(1 - q^j)(1 - q^{-j})`. -/
def habiroFactor (q : K) (j : ℕ) : K :=
  (1 - q ^ j) * (1 - (q⁻¹) ^ j)

/-- **The 4₁ Habiro tail factor is bar-even** (`q ↔ q⁻¹`-invariant), so
    `S(q) = S(q⁻¹)`: no bar-odd datum (4₁ amphichirality).
    ⇒ the odd-channel b3ix needs the chiral 5₂ tail. -/
theorem habiroFactor_bar_even (q : K) (j : ℕ) :
    habiroFactor q j = habiroFactor q⁻¹ j := by
  unfold habiroFactor
  rw [inv_inv]
  ring

end QOU.QBeta.HabiroTailAction
