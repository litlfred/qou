import QOU.LiftingDescent.MotivicGaloisCharacter
import QOU.AlgebraicSubstrate.MotivicSubstrateTrivial
import Mathlib.Tactic

/-!
# Trivial witness for `MotivicGaloisCharacter`

A minimal `MotivicGaloisCharacter ℤ ℤ trivialTarget (motiveA := 1)`
instance with `frobenius_at p := (p : ℤ)`.  The instance witnesses
**inhabitability** and shows `motivic_perpetual_obstruction` is
discharged non-vacuously — for any prime `p ≥ 2`, `(p : ℤ)` is not
a unit in `ℤ` (the only units are `±1`), so the
`almost_everywhere_nontrivial` hypothesis holds with `N := 2`.

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
  almost_everywhere_nontrivial := by
    refine ⟨2, fun p hp hu => ?_⟩
    -- `(p.val : ℤ)` is a unit in `ℤ` only when `p.val = 1` or
    -- `p.val = -1` (impossible since `p.val ≥ 2`).
    have hp_int : (p.val : ℤ) ≥ 2 := by exact_mod_cast hp
    rcases Int.isUnit_iff.mp hu with h | h <;> omega

end QOU.LiftingDescent
