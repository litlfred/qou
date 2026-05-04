import QOU.MassEndomorphism.MassEndomorphismConjecture

/-!
# Trivial witness for `MassEndomorphism`

A zero-mass instance over `ℤ` for an arbitrary braid type `β`.  All
fields are zero; `vol_eq` reduces to `0 = 0 - 0`.  The instance
witnesses **inhabitability** of the class and shows the conditional
theorems (`fullMass_eq_volume`, etc.) are discharged non-vacuously.

This is **not** a closed-form mass endomorphism for any non-trivial
braid.  The principal open item (GAP 18a in the
[2026-05-02 forward-derivation audit](../../../../../docs/audits/2026-05-02-forward-derivation-pre-archimedean.md))
is to produce a deterministic recipe `Braid n → MassEndomorphism R β`.
See
[2026-05-04 GAP 6a + 18a scoping](../../../../../docs/audits/2026-05-04-gap-6a-18a-scoping.md)
for the outstanding work.

Ref: [manuscript] conj:mass-endomorphism
LaTeX label: scoping for `conj:mass-endomorphism`
-/

namespace QOU.MassEndomorphism

/-- Trivial witness: zero-mass instance over `ℤ`. -/
-- Ref: [manuscript] conj:mass-endomorphism §"What is known", Step 1
--      (the flat case `tr_transient = 0`)
instance trivialIntZero (β : Type) :
    MassEndomorphism ℤ β where
  q := 0
  N := 0
  z := Fin.elim0
  tr_transient := 0
  tr_descended := 0
  vol_identity := 0
  vol_eq := by ring

end QOU.MassEndomorphism
