import QOU.LiftingDescent.MotivicGaloisCharacter
import QOU.AlgebraicSubstrate.MotivicSubstrateTrivial
import Mathlib.Tactic

/-!
# Trivial witness for `MotivicGaloisCharacter`

A minimal `MotivicGaloisCharacter ℤ ℤ trivialTarget (motiveA := 1)`
instance with `frobenius_at p := (p : ℤ)`.  The instance witnesses
**inhabitability** — for any prime `p ≥ 2`, `(p : ℤ)` is not
a unit in `ℤ` (the only units are `±1`).

The perpetual obstruction (non-unitality at almost every prime) is
now a standalone theorem in `MotivicPerpetualObstructionFromTrace.lean`,
not a class field obligation.

This is **not** the QOU motivic Galois character at `q₀`.  The
principal open item is GAP 6a in the
[2026-05-02 forward-derivation audit](../../../../../docs/audits/2026-05-02-forward-derivation-pre-archimedean.md);
see
[2026-05-04 GAP 6a + 18a scoping](../../../../../docs/audits/2026-05-04-gap-6a-18a-scoping.md)
for the outstanding work.

Ref: [yekutieli2010]
LaTeX label: scoping for `def:motivic-galois-character`
-/

namespace QOU.LiftingDescent

open QOU.AlgebraicSubstrate

/-- Trivial witness: `frobenius_at p := (p.val : ℤ)`. -/
-- Ref: [yekutieli2010] §3 (the perpetual-obstruction phenomenon)
instance trivial_motivic_galois_character :
    MotivicGaloisCharacter ℤ ℤ trivialTarget (motiveA := 1) where
  frobenius_at := fun p => (p.val : ℤ)
  frobenius_realize_ne_zero := by
    -- `trivialTarget v = ℤ` and `realize v = RingHom.id ℤ`, so the goal is
    -- definitionally `((p : ℕ) : ℤ) ≠ 0`, and a prime is positive.
    intro p _
    show ((p : ℕ) : ℤ) ≠ 0
    exact_mod_cast p.property.pos.ne'

end QOU.LiftingDescent
