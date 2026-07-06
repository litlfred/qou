-- Sibling docstub for `conj:b1-hyperbolic-rows-theorem`.
--
-- This file is documentation only.  The compiled formalisation
-- lives in the Lake-built tree at:
--
--   lean/QOU/AppendixSurreals/B1HyperbolicRowsTheorem.lean
--
-- See `QOU.AppendixSurreals.B1HyperbolicRowsTheorem.b1_hyperbolic_rows`.
--
-- See the chapter umbrella `lean/QOU/AppendixSurreals.lean`
-- for the import wiring.

namespace QOU.AppendixSurreals.B1HyperbolicRowsTheorem

/-- **CONJECTURE.** B1 at additional hyperbolic-knot rows (Borromean, Whitehead, twist knots) conditionally reduces to Volume Conjecture. -/
-- Ref: [manuscript] conj:b1-hyperbolic-rows-theorem
axiom b1_hyperbolic_rows
    (n_hyperbolic_rows_verified : Nat)
    (bloch_suslin van_der_veen : Prop) :
    bloch_suslin → van_der_veen → 3 ≤ n_hyperbolic_rows_verified

end QOU.AppendixSurreals.B1HyperbolicRowsTheorem
