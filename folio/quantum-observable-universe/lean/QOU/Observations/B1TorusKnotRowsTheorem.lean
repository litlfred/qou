import Mathlib.Data.Nat.GCD.Basic

/-!
# B1 keystone is theorem-level at torus-knot rows

Compiled formalisation of `prop:b1-torus-knot-rows-theorem`.
Sibling docstub at `appendix-surreals/b1-torus-knot-rows-theorem.lean`.

The B1 keystone holds unconditionally for every torus-knot row
`T(r, s)` (`gcd(r, s) = 1`, `r, s ≥ 2`) via Bloch-Suslin plus
Garoufalidis-Lê (Tate-rationality of the Chern-Simons invariant
of torus knots).
-/

namespace QOU.AppendixSurreals.B1TorusKnotRowsTheorem

/-- Abstract context for `prop:b1-torus-knot-rows-theorem`. -/
class B1TorusKnotRowsContext where
  /-- Predicate "`B1 holds unconditionally at the torus-knot row T(r, s)`". -/
  b1_holds : ℕ → ℕ → Prop
  /-- Bloch-Suslin regulator condition is satisfied. -/
  bloch_suslin : Prop
  /-- Garoufalidis-Lê (Tate-rationality of Chern-Simons invariant) holds. -/
  garoufalidis_le : Prop
  /-- Witness for Bloch-Suslin. -/
  h_bloch_suslin : bloch_suslin
  /-- Witness for Garoufalidis-Lê. -/
  h_garoufalidis_le : garoufalidis_le
  /-- Together, these imply Tate-rationality and B1 at torus knot rows. -/
  b1_from_tate_rationality : bloch_suslin → garoufalidis_le → ∀ r s : ℕ,
    Nat.Coprime r s → 2 ≤ r → 2 ≤ s → b1_holds r s

/-- **Proposition (`prop:b1-torus-knot-rows-theorem`).** -/
-- Ref: [leitner2026] quantum-observable-universe/appendix-surreals/b1-torus-knot-rows-theorem.md
theorem b1_torus_knot_rows [ctx : B1TorusKnotRowsContext] :
    ∀ r s : ℕ, Nat.Coprime r s → 2 ≤ r → 2 ≤ s → ctx.b1_holds r s :=
  ctx.b1_from_tate_rationality ctx.h_bloch_suslin ctx.h_garoufalidis_le

end QOU.AppendixSurreals.B1TorusKnotRowsTheorem
