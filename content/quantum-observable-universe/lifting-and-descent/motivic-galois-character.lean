import Mathlib.Algebra.Ring.Defs
import Mathlib.Data.Nat.Prime.Basic
import QOU.AlgebraicSubstrate.MotivicSubstrate

/-!
# Motivic Galois character of the Frobenius–Hopf substrate

The motivic-Galois layer on the Yekutieli obstruction κ_n is
carried by a single character of the cyclotomic Galois group:

  χ^mot_A : Gal(ℚ(μ_∞)/ℚ) → Aut_𝓜̂([A])

axiomatised here as a Lean class.  Concrete instances supply the
substrate-internal structure.

**This file is a documentation MIRROR** of the compiled declaration in
`lean/QOU/LiftingDescent/MotivicGaloisCharacter.lean`, which is what
`import QOU.LiftingDescent.MotivicGaloisCharacter` resolves to — the Lake
library globs are `["QOU", "QOU.+"]` rooted at `lean/`, so this path is
outside the build and nothing compiles it.  It exists because
`def:motivic-galois-character` is a `definition` block and AGENTS.md §3
requires a sibling `.lean`; per §0a the sibling is what a reader following
the block's `lean.ref` actually lands on.  **Keep it byte-faithful to the
library class.**

**Re-synced 2026-08-25 after drift, and the drift had a direction.**  This
mirror had gone stale in the one way that matters: it still declared

    almost_everywhere_nontrivial :
      ∃ N : ℕ, ∀ p : Nat.Primes, (p : ℕ) ≥ N → ¬IsUnit (frobenius_at p)

as a **class field** — the field the library *removed* on 2026-08-12,
in its own words, because "encoding it as a class field forced every
instance to either prove it or launder an axiom … the Route A proof shows
it is a *consequence* of the Habiro structure, not an input".  So the ref
resolved to a class that **assumes the perpetual obstruction**, which is
exactly what "Axiomatization is NOT a Proof" forbids, while the compiled
class does not.  The mirror also predated `frobenius_realize_ne_zero`, the
Prop field that stops `⟨fun _ => 0⟩` inhabiting the class, and carried a
superseded three-parameter signature with no `Target` / `MotivicSubstrate`.

Same defect family as beans `qou-a5dr` / `qou-ngac` — a stale sibling
manufacturing a false reading that survives the corpus-grep checklist —
one file over.  Those were `theorem` blocks, so deletion was the fix there;
a `definition` block requires its sibling, so the fix here is re-synchronisation.

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

      Without it the class carries a single data field and no Prop field
      at all, so `⟨fun _ => 0⟩` inhabits it and every downstream
      `[MotivicGaloisCharacter …]` hypothesis is discharged by a character
      that is identically zero.

      **Scope.**  The full compatibility of `χ^mot_{A,p}` with the
      realization tower would relate `frobenius_at p` to a Frobenius
      *operator* on `Target (Place.finite p)`.  `MotivicSubstrate` supplies
      no such operator, so that statement is not expressible here.  What is
      encoded is the non-degeneracy half. -/
  frobenius_realize_ne_zero :
    ∀ p : Nat.Primes, Nontrivial (Target (Place.finite p)) →
      sub.realize (Place.finite p) (frobenius_at p) ≠ 0

end QOU.LiftingDescent
