import Mathlib.Algebra.Ring.Defs
import Mathlib.Data.Nat.Prime.Basic
import Mathlib.Data.Finset.Basic
import QOU.LiftingDescent.MotivicGaloisCharacter
import QOU.LiftingDescent.MotivicPerpetualObstructionFromTrace

/-!
# Motivic perpetual obstruction theorem

The Kummer-tower perpetuity result lifts to a single statement
about the motivic Galois character: if the Frobenius trace satisfies
a growth bound (|trace| > 1 past some N), then the character is
non-trivial at every prime outside a finite exception set.

**Architectural note (2026-08-12):** this theorem was formerly a
conditional extraction of the `MotivicGaloisCharacter.almost_everywhere_nontrivial`
class field. That field has been removed — the perpetual obstruction
is now a *theorem* proved via the prime-ideal-collapse argument
(`perpetual_obstruction_from_collapse_invariant`), not an axiom
that instances must fill. This file preserves the theorem's
interface for downstream consumers, taking the trace bound as an
explicit hypothesis rather than a class field.

For the concrete QOU instances (proton: C=4, deuteron: C=-32),
the exception set is EMPTY — see `qou_proton_perpetual_obstruction`
and `qou_deuteron_perpetual_obstruction` in
`MotivicPerpetualObstructionFromTrace.lean`.

Ref: [yekutieli2010] — obstruction theory
LaTeX label: `thm:motivic-perpetual-obstruction`
-/

namespace QOU.LiftingDescent

open QOU.AlgebraicSubstrate

/-- **Motivic perpetual obstruction (almost-everywhere form).**

    For a substrate carrying a `MotivicGaloisCharacter` whose
    Frobenius eigenvalues satisfy a trace-growth bound in ℤ, there
    is a finite "bad" set `S ⊂ ℕ` such that at every prime `p ∉ S`
    the Frobenius eigenvalue is **not** a unit.

    This version takes the trace bound as an explicit hypothesis.
    For the stronger result with S = ∅, see
    `perpetual_obstruction_from_collapse_invariant`.

    **The `MotivicGaloisCharacter` binder is deliberately inert** and
    is written `_hχ` to say so.  The conclusion quantifies over an
    arbitrary `trace : Nat.Primes → ℤ`, so nothing here connects the
    bound to the character's own `frobenius_at` family; the binder is
    retained only because this declaration's name is the interface
    cited by the 2026-05-03 and 2026-05-04 audits.  For the statement
    that *is* about the character, see
    `motivic_perpetual_obstruction_frobenius` below, whose conclusion
    is about `hχ.frobenius_at` itself.

    Ref: [yekutieli2010] §3-4 (gerbe obstruction). -/
theorem motivic_perpetual_obstruction
    {K0 Mhat : Type*} [CommRing K0] [CommRing Mhat]
    {Target : Place → Type*} [∀ v, CommRing (Target v)]
    [MotivicSubstrate K0 Mhat Target]
    {motiveA : Mhat}
    [_hχ : MotivicGaloisCharacter K0 Mhat Target motiveA]
    (trace : Nat.Primes → ℤ)
    (N : ℕ)
    (h_bound : ∀ p : Nat.Primes, (p : ℕ) ≥ N → 1 < (trace p).natAbs) :
    ∃ S : Finset ℕ,
      ∀ p : Nat.Primes, (p : ℕ) ∉ S →
        ¬IsUnit (trace p) :=
  perpetual_obstruction_from_trace trace N h_bound

/-- **Motivic perpetual obstruction, stated about the Frobenius family
    itself.**

    `motivic_perpetual_obstruction` above carries a
    `[MotivicGaloisCharacter …]` binder that it never uses: its `trace` is a
    free function and its conclusion is about `trace`, with nothing relating
    the two.  What it proves therefore holds of *any* integer-valued function
    that is eventually large in absolute value, and mentions no motivic
    structure at all.  It is kept as stated — it is true, and it is the form
    a caller who already has a trace function wants.

    This version supplies the missing link.  The trace is not free: it is the
    image of the Frobenius family under a given realization `φ : Mhat →+* ℤ`,
    and the conclusion is about `hχ.frobenius_at p` rather than about its
    image.  The transfer is the contrapositive of `IsUnit.map`: a ring hom
    carries units to units, so a non-unit image forces a non-unit source.

    `φ` is an explicit argument rather than derived from the substrate's
    `realize`, because `MotivicSubstrate.realize` lands in `Target v`, which
    is a bare `CommRing` with no ordering — `1 < |·|` is not expressible
    there.  A caller with `Target (Place.finite p) = ℤ` supplies `realize`
    itself; the generality costs nothing and avoids inventing structure on
    `Target`.

    Ref: [yekutieli2010] §3-4 (gerbe obstruction). -/
theorem motivic_perpetual_obstruction_frobenius
    {K0 Mhat : Type*} [CommRing K0] [CommRing Mhat]
    {Target : Place → Type*} [∀ v, CommRing (Target v)]
    [MotivicSubstrate K0 Mhat Target]
    {motiveA : Mhat}
    (hχ : MotivicGaloisCharacter K0 Mhat Target motiveA)
    (φ : Mhat →+* ℤ)
    (N : ℕ)
    (h_bound : ∀ p : Nat.Primes, (p : ℕ) ≥ N →
      1 < (φ (hχ.frobenius_at p)).natAbs) :
    ∃ S : Finset ℕ,
      ∀ p : Nat.Primes, (p : ℕ) ∉ S →
        ¬IsUnit (hχ.frobenius_at p) := by
  obtain ⟨S, hS⟩ :=
    perpetual_obstruction_from_trace (fun p => φ (hχ.frobenius_at p)) N h_bound
  exact ⟨S, fun p hp hu => hS p hp (hu.map φ)⟩

end QOU.LiftingDescent
