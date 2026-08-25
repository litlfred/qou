import Mathlib.Algebra.Ring.Defs
import Mathlib.Data.Nat.Prime.Basic
import QOU.AlgebraicSubstrate.MotivicSubstrate

/-!
# Motivic Galois character of the Frobenius–Hopf substrate

The motivic-Galois layer on the Yekutieli obstruction κ_n is
carried by a single character of the cyclotomic Galois group:

  χ^mot_A : Gal(ℚ(μ_∞)/ℚ) → Aut_𝓜̂([A])

axiomatised here as a Lean class.  Concrete instances supply the
substrate-internal structure; `sorry` in any field is a substrate
axiom (AGENTS.md §3b), not a missing proof.

**Formal-chain version.**  This file lives under `lean/QOU/` and is
compiled by `lake build`.  The co-located documentation stub at
`content/quantum-observable-universe/lifting-and-descent/motivic-galois-character.lean`
mirrors this content (per `QOU.GroundRingAnnotations`).

Ref: [yekutieli2010] — Yekutieli's obstruction theory
Ref: [tate1967] — Tate's thesis (adelic decomposition)
LaTeX label: `def:motivic-galois-character`
-/

namespace QOU.LiftingDescent

open QOU.AlgebraicSubstrate

/-- **Motivic Galois character of a Frobenius–Hopf substrate.**

    Axiomatic class encoding the cyclotomic-Galois action on the
    motivic class `[A]` of the substrate.  Parameters:
    * `K0 Mhat` — Grothendieck ring + dimension-completion
      ([`MotivicSubstrate`](MotivicSubstrate)).
    * `Target` — realisation target functor (passed through to
      `MotivicSubstrate`).
    * `motiveA : Mhat` — the motivic class of the substrate $A$.

    The class **takes a `MotivicSubstrate` instance as a
    hypothesis** (per `def:motivic-galois-character` narrative),
    making the Galois character genuinely local to a substrate
    rather than free-floating type parameters.

    Fields encode the family of local Frobenius characters
    $\chi^{\mathrm{mot}}_{A, p}$ at each finite place, satisfying
    a compatibility with the realization tower of the substrate.

    **Architectural note (2026-08-12):** the `almost_everywhere_nontrivial`
    field was removed from this class.  The perpetual obstruction is now
    a standalone theorem (`perpetual_obstruction_from_collapse_invariant`
    in `MotivicPerpetualObstructionFromTrace.lean`) proved via the
    prime-ideal-collapse argument: C = a₀(-1) + 2·a₁(-1), with |C| > 1
    for all QOU atoms.  Encoding it as a class field forced every
    instance to either prove it or launder an axiom — the Route A proof
    shows it is a *consequence* of the Habiro structure, not an input.

    Ref: [yekutieli2010], [tate1967]. -/
class MotivicGaloisCharacter
    (K0 Mhat : Type*) [CommRing K0] [CommRing Mhat]
    (Target : Place → Type*) [∀ v, CommRing (Target v)]
    [sub : MotivicSubstrate K0 Mhat Target]
    (motiveA : Mhat) where
  /-- Local Frobenius eigenvalue at a finite prime `p`,
      represented as an element of the dimension-completion. -/
  frobenius_at : Nat.Primes → Mhat
  /-- **Realization-tower compatibility.**

      At every finite place whose realization target is nontrivial, the
      local Frobenius character is *visible in the tower*: its image
      under the substrate's realization map at that place is nonzero.

      This is the law the class docstring has always promised and never
      encoded.  Without it the class carries a single data field and no
      Prop field at all, so `⟨fun _ => 0⟩` inhabits it and every
      downstream `[MotivicGaloisCharacter …]` hypothesis is discharged by
      a character that is identically zero — see
      `not_forall_frobenius_eq_zero` below, which is exactly the
      statement this field buys.

      **Scope — what this does NOT encode.**  The full compatibility of
      `χ^mot_{A,p}` with the realization tower would relate
      `frobenius_at p` to a Frobenius *operator* on `Target
      (Place.finite p)` and to `motiveA` through it.  `MotivicSubstrate`
      supplies no such operator, so that statement is not expressible
      here.  What is encoded is the non-degeneracy half: the character
      does not vanish where the tower is non-degenerate. -/
  frobenius_realize_ne_zero :
    ∀ p : Nat.Primes, Nontrivial (Target (Place.finite p)) →
      sub.realize (Place.finite p) (frobenius_at p) ≠ 0

/-- **The class is not vacuous.**  No `MotivicGaloisCharacter` has an
    identically-zero Frobenius family.

    This is the point of `frobenius_realize_ne_zero`.  The substrate axiom
    `nonarchimedean_nontrivial` supplies a finite place with a nontrivial
    target; realization is a ring hom, so it sends `0` to `0`; and the
    compatibility law forbids that.  Before the law was added, the
    all-zero family was a legitimate instance. -/
theorem not_forall_frobenius_eq_zero
    {K0 Mhat : Type*} [CommRing K0] [CommRing Mhat]
    {Target : Place → Type*} [∀ v, CommRing (Target v)]
    [inst : MotivicSubstrate K0 Mhat Target]
    {motiveA : Mhat}
    (hχ : MotivicGaloisCharacter K0 Mhat Target motiveA) :
    ¬ (∀ p : Nat.Primes, hχ.frobenius_at p = 0) := by
  intro hzero
  obtain ⟨p, hp⟩ := inst.nonarchimedean_nontrivial
  refine hχ.frobenius_realize_ne_zero p hp ?_
  rw [hzero p, map_zero]

end QOU.LiftingDescent
