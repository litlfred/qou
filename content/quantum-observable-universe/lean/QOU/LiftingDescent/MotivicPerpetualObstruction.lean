import Mathlib.Algebra.Ring.Defs
import Mathlib.Data.Nat.Prime.Basic
import Mathlib.Data.Finset.Basic
import QOU.LiftingDescent.MotivicGaloisCharacter

/-!
# Motivic perpetual obstruction conjecture

The Kummer-tower perpetuity result lifts to a single statement
about the motivic Galois character: if χ(A) ≠ 0 then χ^mot_A is
non-trivial at every finite place p ∤ χ(A).

**Block kind: `conjecture` (AGENTS.md §3b conditional-class
pattern).**  The conjectural content is concentrated in the field
`MotivicGaloisCharacter.almost_everywhere_nontrivial` (which any
instance is required to populate).  The Lean theorem below is
**conditional on a `[MotivicGaloisCharacter ...]` instance** and
contains no `sorry` — it is a direct extraction of the class
field, repackaged in the conjecture's preferred form (existence of
a "bad" finite set `S`).

**Formal-chain version.**  This file lives under `lean/QOU/` and is
compiled by `lake build`.  The co-located documentation stub at
`content/quantum-observable-universe/lifting-and-descent/motivic-perpetual-obstruction.lean`
mirrors this content (per `QOU.GroundRingAnnotations`).

Ref: [yekutieli2010] — obstruction theory
LaTeX label: `conj:motivic-perpetual-obstruction`
-/

namespace QOU.LiftingDescent

open QOU.AlgebraicSubstrate

/-- **Motivic perpetual obstruction (almost-everywhere form).**

    For a substrate carrying a `MotivicGaloisCharacter`, there is a
    finite "bad" set `S ⊂ ℕ` (here `Finset.range N` for the
    substrate-bound `N`) such that at every prime `p ∉ S` the
    Frobenius eigenvalue `frobenius_at p` is **not** a unit in
    `Mhat`.

    This is the universal almost-everywhere statement extracted
    from the `MotivicGaloisCharacter.almost_everywhere_nontrivial`
    field.  In concrete substrates the bad set `S` can typically
    be sharpened to `{primes p : p ∣ χ(A)} ∪ {primes < N}` — that
    sharper, χ-aware statement is recorded in the narrative .md
    block; here the Lean theorem records only the universal
    conclusion that holds for every motivic substrate.

    Concrete instances of `MotivicGaloisCharacter` provide either
    a constructive `S = ∅`/small witness or a `sorry` substrate
    axiom (AGENTS.md §3b).

    Downstream blocks (Kummer tower, Descartes-Yekutieli, chi=-6
    derivation, Hochschild–Kummer connection) all become
    corollaries: see `conj:motivic-perpetual-obstruction` in
    the .md file.

    Ref: [yekutieli2010] §3-4 (gerbe obstruction); HKR comparison.
    Substrate axiom: the proof uses QU-to-QOU + Frobenius trace
    at p (= χ mod p, non-zero when p ∤ χ). -/
theorem motivic_perpetual_obstruction
    {K0 Mhat : Type*} [CommRing K0] [CommRing Mhat]
    {Target : Place → Type*} [∀ v, CommRing (Target v)]
    [MotivicSubstrate K0 Mhat Target]
    {motiveA : Mhat}
    [hχ : MotivicGaloisCharacter K0 Mhat Target motiveA] :
    ∃ S : Finset ℕ,
      ∀ p : Nat.Primes, (p : ℕ) ∉ S →
        ¬IsUnit (hχ.frobenius_at p) := by
  obtain ⟨N, hN⟩ := hχ.almost_everywhere_nontrivial
  refine ⟨Finset.range N, ?_⟩
  intro p hpS
  have hpN : N ≤ (p : ℕ) := by
    by_contra hlt
    push_neg at hlt
    exact hpS (Finset.mem_range.mpr hlt)
  exact hN p hpN

end QOU.LiftingDescent
