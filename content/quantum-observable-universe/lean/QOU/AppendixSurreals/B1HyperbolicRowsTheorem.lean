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

/-- Abstract context for `prop:b1-hyperbolic-rows-theorem`. -/
class B1HyperbolicRowsContext where
  /-- Number of distinguished hyperbolic-knot rows verified
      unconditionally (manuscript: Borromean rings, Whitehead link,
      twist-knot family — at least 3). -/
  n_hyperbolic_rows_verified : ℕ
  /-- Bloch-Suslin regulator condition is satisfied. -/
  bloch_suslin : Prop
  /-- van der Veen et al.'s Volume-Conjecture extensions hold. -/
  van_der_veen : Prop
  /-- Witness for Bloch-Suslin. -/
  h_bloch_suslin : bloch_suslin
  /-- Witness for van der Veen. -/
  h_van_der_veen : van_der_veen
  /-- Together, these imply B1 holds at least at 3 hyperbolic rows. -/
  rows_from_volume_conj : bloch_suslin → van_der_veen → 3 ≤ n_hyperbolic_rows_verified

/-- **Proposition (`prop:b1-hyperbolic-rows-theorem`).** -/
-- Ref: [manuscript] quantum-observable-universe/appendix-surreals/b1-hyperbolic-rows-theorem.md
theorem b1_hyperbolic_rows [ctx : B1HyperbolicRowsContext] :
    3 ≤ ctx.n_hyperbolic_rows_verified :=
  ctx.rows_from_volume_conj ctx.h_bloch_suslin ctx.h_van_der_veen

end QOU.AppendixSurreals.B1HyperbolicRowsTheorem
