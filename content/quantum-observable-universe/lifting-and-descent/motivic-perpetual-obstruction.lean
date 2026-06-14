import Mathlib.Algebra.Ring.Defs
import Mathlib.Data.Finset.Basic
import Mathlib.Data.Nat.Prime.Basic

/-!
# QOU.LiftingDescent.motivic_perpetual_obstruction
-/

namespace QOU.LiftingDescent

class MotivicGaloisCharacter (K0 Mhat : Type*) [CommRing K0] [CommRing Mhat] (motive : Mhat) where
  frobenius_at : Nat.Primes → Mhat

/-- **CONJECTURE.** Motivic perpetual obstruction (almost-everywhere form).
    If χ(A) ≠ 0 then χ^mot_A is non-trivial at every finite place p ∤ χ(A). -/
theorem motivic_perpetual_obstruction
    {K0 Mhat : Type*} [CommRing K0] [CommRing Mhat]
    {motiveA : Mhat} [hχ : MotivicGaloisCharacter K0 Mhat motiveA] :
    ∃ S : Finset ℕ,
      ∀ p : Nat.Primes, (p : ℕ) ∉ S →
        ¬IsUnit (hχ.frobenius_at p) := by
  -- Ref: [manuscript] conj:motivic-perpetual-obstruction
  sorry

end QOU.LiftingDescent
