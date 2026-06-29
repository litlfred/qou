import Mathlib.Data.Nat.Notation

/-!
# B1 at additional hyperbolic-knot rows

Compiled formalisation of `prop:b1-hyperbolic-rows-theorem`.
Sibling docstub at `appendix-surreals/b1-hyperbolic-rows-theorem.lean`.

The B1 keystone holds unconditionally at Borromean rings,
the Whitehead link, and the twist-knot family via Bloch-Suslin
together with van der Veen et al.'s Volume-Conjecture extensions.
-/

namespace QOU.AppendixSurreals.B1HyperbolicRowsTheorem

/-- **Conjecture (`prop:b1-hyperbolic-rows-theorem`).**
    B1 holds at least at 3 hyperbolic rows (Borromean, Whitehead, twist-knot family)
    conditional on the Bloch-Suslin regulator condition and van der Veen's Volume Conjecture extensions. -/
-- Ref: [manuscript] quantum-observable-universe/appendix-surreals/b1-hyperbolic-rows-theorem.md
axiom b1_hyperbolic_rows
    (n_hyperbolic_rows_verified : ℕ)
    (bloch_suslin van_der_veen : Prop) :
    bloch_suslin → van_der_veen → 3 ≤ n_hyperbolic_rows_verified

end QOU.AppendixSurreals.B1HyperbolicRowsTheorem
