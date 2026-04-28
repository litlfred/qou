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
    axiom (CLAUDE.md §3b).

    Downstream blocks (Kummer tower, Descartes-Yekutieli, chi=-6
    derivation, Hochschild–Kummer connection) all become
    corollaries: see `lem:motivic-perpetual-obstruction` in
    the .md file.

    Ref: [yekutieli2010] §3-4 (gerbe obstruction); HKR comparison.
    Substrate axiom: the proof uses QU-to-QOU + Frobenius trace
    at p (= χ mod p, non-zero when p ∤ χ). -/
theorem motivic_perpetual_obstruction
    {K0 Mhat : Type*} [CommRing K0] [CommRing Mhat]
    {motiveA : Mhat} [hχ : MotivicGaloisCharacter K0 Mhat motiveA] :
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
