import Mathlib.Algebra.Ring.Defs
import Mathlib.Data.Nat.Prime.Basic

/-!
# Motivic Galois character of the Frobenius–Hopf substrate

The motivic-Galois layer on the Yekutieli obstruction κ_n is
carried by a single character of the cyclotomic Galois group:

  χ^mot_A : Gal(ℚ(μ_∞)/ℚ) → Aut_𝓜̂([A])

axiomatised here as a Lean class.  Concrete instances supply the
substrate-internal structure; `sorry` in any field is a substrate
axiom (AGENTS.md §3b), not a missing proof.

Ref: [yekutieli2010] — Yekutieli's obstruction theory
Ref: [tate1967] — Tate's thesis (adelic decomposition)
LaTeX label: `def:motivic-galois-character`
-/

namespace QOU.LiftingDescent

/-- **Motivic Galois character of a Frobenius–Hopf substrate.**

    Axiomatic class encoding the cyclotomic-Galois action on the
    motivic class `[A]` of the substrate.  Parameters:
    * `K0 Mhat` — Grothendieck ring + dimension-completion
      ([`MotivicSubstrate`](MotivicSubstrate)).
    * `motiveA : Mhat` — the motivic class of the substrate $A$.

    Fields encode the family of local Frobenius characters
    $\chi^{\mathrm{mot}}_{A, p}$ at each finite place, satisfying
    a compatibility with the realization tower of the substrate.

    Ref: [yekutieli2010], [tate1967]. -/
class MotivicGaloisCharacter
    (K0 Mhat : Type*) [CommRing K0] [CommRing Mhat]
    (motiveA : Mhat) where
  /-- Local Frobenius eigenvalue at a finite prime `p`,
      represented as an element of the dimension-completion. The
      domain is `Nat.Primes` (Mathlib subtype `{p // p.Prime}`)
      rather than `ℕ` so that non-prime indices are ruled out at
      the type level. -/
  frobenius_at : Nat.Primes → Mhat
  /-- The character is non-trivial: at almost every prime, the
      Frobenius eigenvalue is not a unit (which would make the
      character trivial there).  This encapsulates the perpetual
      obstruction phenomenon. -/
  almost_everywhere_nontrivial :
    ∃ N : ℕ, ∀ p : Nat.Primes, (p : ℕ) ≥ N → ¬IsUnit (frobenius_at p)

end QOU.LiftingDescent
