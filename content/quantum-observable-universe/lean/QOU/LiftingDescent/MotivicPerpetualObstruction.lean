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

    Ref: [yekutieli2010] §3-4 (gerbe obstruction). -/
theorem motivic_perpetual_obstruction
    {K0 Mhat : Type*} [CommRing K0] [CommRing Mhat]
    {Target : Place → Type*} [∀ v, CommRing (Target v)]
    [MotivicSubstrate K0 Mhat Target]
    {motiveA : Mhat}
    [hχ : MotivicGaloisCharacter K0 Mhat Target motiveA]
    (trace : Nat.Primes → ℤ)
    (N : ℕ)
    (h_bound : ∀ p : Nat.Primes, (p : ℕ) ≥ N → 1 < (trace p).natAbs) :
    ∃ S : Finset ℕ,
      ∀ p : Nat.Primes, (p : ℕ) ∉ S →
        ¬IsUnit (trace p) :=
  perpetual_obstruction_from_trace trace N h_bound

end QOU.LiftingDescent
