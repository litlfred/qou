/-
# The Milnor-parity sign law for A-component Brunnian binding clusters
# — consolidating #4360 (A=3, proved +) and #4378 (A=4, measured −).

(STUB — full formalization in a following commit.)
-/
import Mathlib.Tactic

namespace QOU.MassTheory.MilnorParitySignLaw

/-- Leading Milnor order of the A-component Brunnian trace deficit: `2(A-1)`. -/
def leadingOrder (A : ℕ) : ℕ := 2 * (A - 1)

end QOU.MassTheory.MilnorParitySignLaw
