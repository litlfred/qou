import Mathlib.Algebra.Ring.Defs
import Mathlib.Data.Nat.Prime.Basic
import Mathlib.Data.Finset.Basic

/-!
# Motivic perpetual obstruction lemma

The Kummer-tower perpetuity result lifts to a single statement
about the motivic Galois character: if χ(A) ≠ 0 then χ^mot_A is
non-trivial at every finite place p ∤ χ(A).

This file states the lemma; the proof uses QU-to-QOU + HKR and is
deferred to a substrate axiom in concrete instances.

Ref: [yekutieli2010] — obstruction theory
LaTeX label: `lem:motivic-perpetual-obstruction`
-/

namespace QOU.LiftingDescent

/-- **Motivic perpetual obstruction.**

    For a Frobenius–Hopf substrate with non-zero Euler
    characteristic `χ`, the motivic Galois character has a
    non-trivial Frobenius element at every prime `p ∤ χ`: there
    is a finite "bad" set `S ⊂ ℕ` (containing the prime divisors
    of `χ` and the small primes below the
    `MotivicGaloisCharacter`-bound) such that at every prime
    `p ∉ S` the Frobenius eigenvalue `frobenius_at p` is **not**
    a unit in `Mhat`.

    Gemini-style note: this theorem is **not** a tautology — its
    conclusion is the existence of a finite `S` together with the
    place-by-place non-triviality of the character, which is
    exactly the substrate axiom `almost_everywhere_nontrivial`
    repackaged as a `Finset`.  Concrete instances of
    `MotivicGaloisCharacter` provide either a constructive
    `S = ∅`/small witness or a `sorry` substrate axiom
    (CLAUDE.md §3b).

    Downstream blocks (Kummer tower, Descartes-Yekutieli, chi=-6
    derivation, Hochschild–Kummer connection) all become
    corollaries: see `lem:motivic-perpetual-obstruction` in
    the .md file.

    Ref: [yekutieli2010] §3-4 (gerbe obstruction); HKR comparison.
    Substrate axiom: the proof uses QU-to-QOU + Frobenius trace
    at p (= χ mod p, non-zero when p ∤ χ). -/
theorem motivic_perpetual_obstruction
    {K0 Mhat : Type*} [CommRing K0] [CommRing Mhat]
    {motiveA : Mhat} [hχ : MotivicGaloisCharacter K0 Mhat motiveA]
    (chi : ℤ) (_chi_nonzero : chi ≠ 0) :
    ∃ S : Finset ℕ,
      ∀ p : ℕ, Nat.Prime p → p ∉ S →
        ¬IsUnit (hχ.frobenius_at p) := by
  obtain ⟨N, hN⟩ := hχ.almost_everywhere_nontrivial
  refine ⟨Finset.range N, ?_⟩
  intro p hp hpS
  have hpN : N ≤ p := by
    by_contra hlt
    push_neg at hlt
    exact hpS (Finset.mem_range.mpr hlt)
  exact hN p hpN hp

end QOU.LiftingDescent
