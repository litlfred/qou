import QOU.MassEndomorphism.MassEndomorphismConjecture

/-!
# Trivial witness for `MassEndomorphism`

A zero-mass model over `ℤ` for an arbitrary braid type `β`.  All fields
are zero; `vol_eq` reduces to `0 = 0 - 0`.  It witnesses
**inhabitability** of the class, and nothing more.

**A `def`, not an `instance`, since 2026-08-24**, alongside
`MassEndomorphismConjecture.canonical`, for the same reason: as an
`instance` it made every `[MassEndomorphism ℤ β]` binder resolvable, so
`fullMass_eq_volume` at `R = ℤ` proved `0 = 0` rather than anything
conditional.  The file docstring used to state the opposite — that the
instance *"shows the conditional theorems … are discharged
non-vacuously"*.  It shows the reverse: a global trivial witness is
exactly what makes them vacuous.  The partial mitigation that was in
place (`QOU/MassEndomorphism.lean` deliberately does not import this
module, so the pollution was scoped to direct importers) is retained but
is no longer what is doing the work.

Callers wanting the zero model name it: `letI := trivial_int_zero β`.

This is **not** a closed-form mass endomorphism for any non-trivial
braid.  The principal open item (GAP 18a in the
[2026-05-02 forward-derivation audit](../../../../../docs/audits/2026-05-02-forward-derivation-pre-archimedean.md))
is to produce a deterministic recipe `Braid n → MassEndomorphism R β`.
See
[2026-05-04 GAP 6a + 18a scoping](../../../../../docs/audits/2026-05-04-gap-6a-18a-scoping.md)
for the outstanding work.

Ref: [leitner2026] conj:mass-endomorphism
LaTeX label: scoping for `conj:mass-endomorphism`
-/

namespace QOU.MassEndomorphism

/-- Zero-mass model of `MassEndomorphism ℤ β`.  Not an `instance` — see
    the module docstring. -/
-- Ref: [leitner2026] conj:mass-endomorphism §"What is known", Step 1
--      (the flat case `tr_transient = 0`)
def trivial_int_zero (β : Type*) :
    MassEndomorphism ℤ β where
  q := 0
  N := 0
  z := Fin.elim0
  tr_transient := 0
  tr_descended := 0
  vol_identity := 0
  vol_eq := by ring

end QOU.MassEndomorphism
