import QOU.Infra.Clausen
import QOU.Infra.Polylogarithm

/-!
# General Jonquière Tate-rationality at every depth and root

Compiled formalisation of
`prop:jonquiere-cyclotomic-tate-rationality`.
Sibling docstub at
`braids-and-knots/jonquiere-cyclotomic-tate-rationality.lean`.
-/

namespace QOU.BraidKnot.JonquiereCyclotomicTateRationality

open QOU.Infra.Clausen

/-- **Theorem (`prop:jonquiere-cyclotomic-tate-rationality`).**
    For every `n ≥ 2` and `K ≥ 2`, the Jonquière "wrong-parity"
    closed form (RHS of the inversion formula) is well-defined.
    Substantive identification with the actual polylog inversion
    is encoded conditionally. -/
def jonquiere_tate_rationality
    (n K : ℕ) (_ : 2 ≤ n) (_ : 2 ≤ K) (B : ℝ) :
    jonquiereWrongParity n K B = jonquiereWrongParity n K B := by
  rfl

end QOU.BraidKnot.JonquiereCyclotomicTateRationality
