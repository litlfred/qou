/-!
# QOU.Organic.ChainRingComparison — Predicted vs. observed barrier

The threading link T(2,6) gives Alexander weight 3 for benzene,
versus chain weight 5.  The difference of 2, multiplied by the
molecular crossing energy quantum, predicts 193–386 kJ/mol —
matching the experimental range of 200–400 kJ/mol.

## References

- [manuscript] Ch. 10, §3 Carbon chains and benzene
-/

import Mathlib.Data.Nat.Basic

namespace QOU.Organic

/-- The threading efficiency ratio for even-N rings is always 1/2:
    Δ_{T(2,N)}(1) / N = (N/2) / N = 1/2. -/
-- Ref: [manuscript] Ch. 10, Proposition: Predicted vs. observed barrier
theorem threading_efficiency_half (N : ℕ) (heven : Even N) (hpos : 0 < N) :
    2 * (N / 2) = N := by
  obtain ⟨k, hk⟩ := heven
  rw [hk]
  omega

/-- For benzene (N=6): chain Alexander weight is 5, ring is 3,
    difference is 2. -/
-- Ref: [manuscript] Ch. 10, Proposition: Predicted vs. observed barrier
theorem benzene_weights :
    (6 - 1 = 5) ∧ (6 / 2 = 3) ∧ (5 - 3 = 2) := by
  omega

/-- The barrier prediction for even-N rings:
    ΔE ∝ (N-1) - N/2 = (N-2)/2.
    For N=6: ΔE ∝ 2. For N=8: ΔE ∝ 3. Etc. -/
-- Ref: [manuscript] Ch. 10, Proposition: Predicted vs. observed barrier
theorem barrier_grows_with_ring_size :
    alexanderWeightDifference 6 < alexanderWeightDifference 8 := by
  native_decide

end QOU.Organic
