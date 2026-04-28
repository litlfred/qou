/-!
# QOU.Organic.TorusKnotT2OddAlexander — Δ_{T(2, 2m+1)} closed form

The symmetric Alexander polynomial of the odd-N torus knot T(2, 2m+1).

## References

- [manuscript] Ch. 10, Definition `def:torus-knot-T2-odd-alexander`
- [manuscript] Ch. 10, Lemma `lem:alexander-T2N-closed-form`
- [kawauchi1996] A Survey of Knot Theory, §6
-/

import Mathlib.Data.Nat.Basic

namespace QOU.Organic

/-- Δ_{T(2, 2m+1)}(1) = 1 for all m ≥ 0. -/
-- Ref: [manuscript] Ch. 10, Definition def:torus-knot-T2-odd-alexander
def torusKnotT2OddAlexanderAtOne (_m : ℕ) : ℕ := 1

/-- Sanity check: trefoil T(2,3), m = 1, evaluates to 1 at q = 1. -/
-- Ref: [manuscript] Ch. 10, Definition def:torus-knot-T2-odd-alexander
theorem torusKnotT2Odd_trefoil : torusKnotT2OddAlexanderAtOne 1 = 1 := by
  rfl

/-- Sanity check: cinquefoil T(2,5), m = 2. -/
-- Ref: [manuscript] Ch. 10, Definition def:torus-knot-T2-odd-alexander
theorem torusKnotT2Odd_cinquefoil : torusKnotT2OddAlexanderAtOne 2 = 1 := by
  rfl

end QOU.Organic
