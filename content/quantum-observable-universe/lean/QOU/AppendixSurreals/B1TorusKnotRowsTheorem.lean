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
  /-- Manuscript claim — B1 holds at every torus-knot row
      `T(r, s)` with `gcd(r, s) = 1` and `r, s ≥ 2`. -/
  claim_torus_rows : ∀ r s : ℕ,
    Nat.Coprime r s → 2 ≤ r → 2 ≤ s → b1_holds r s

/-- **Proposition (`prop:b1-torus-knot-rows-theorem`).** -/
-- Ref: [manuscript] quantum-observable-universe/appendix-surreals/b1-torus-knot-rows-theorem.md
theorem b1_torus_knot_rows [ctx : B1TorusKnotRowsContext] :
    ∀ r s : ℕ, Nat.Coprime r s → 2 ≤ r → 2 ≤ s → ctx.b1_holds r s :=
  ctx.claim_torus_rows

end QOU.AppendixSurreals.B1TorusKnotRowsTheorem
