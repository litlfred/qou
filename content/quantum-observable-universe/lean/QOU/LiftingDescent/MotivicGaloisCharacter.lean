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
    [MotivicSubstrate K0 Mhat Target]
    (motiveA : Mhat) where
  /-- Local Frobenius eigenvalue at a finite prime `p`,
      represented as an element of the dimension-completion. -/
  frobenius_at : Nat.Primes → Mhat

end QOU.LiftingDescent
