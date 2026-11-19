import Mathlib.Data.Nat.Basic
import Mathlib.Algebra.Group.Even
import Mathlib.Tactic.Common


/-!
# QOU.Organic.ChainRingComparison — Predicted vs. observed barrier

The threading link T(2,6) has linking number 3 (the reduced Alexander
polynomial at t = 1), versus total linking number 5 for the chain of five
Hopf links. This file checks only that integer arithmetic. The energy reading
(conj:chain-ring-comparison) multiplies the difference by a chosen molecular
energy quantum of 1–2 eV; that quantum is not derived, so the kJ/mol figure
is a calibrated comparison, not a parameter-free prediction.

## References

- [leitner2026] Ch. 10, §3 Carbon chains and benzene
-/

namespace QOU.Organic

/-- The threading efficiency ratio for even-N rings is always 1/2:
    lk(T(2,N)) / N = (N/2) / N = 1/2, with lk the linking number. -/
-- Ref: [leitner2026] Ch. 10, Proposition: Predicted vs. observed barrier
theorem threading_efficiency_half (N : ℕ) (heven : Even N) (hpos : 0 < N) :
    2 * (N / 2) = N := by
  obtain ⟨k, hk⟩ := heven
  rw [hk]
  omega

/-- For benzene (N=6): chain linking number is 5, ring linking number is 3,
    difference is 2. -/
-- Ref: [leitner2026] Ch. 10, Proposition: Predicted vs. observed barrier
theorem benzene_weights :
    (6 - 1 = 5) ∧ (6 / 2 = 3) ∧ (5 - 3 = 2) := by
  omega

/-- The linking-number difference between chain and threaded ring.
    For even N: (N-1) - N/2 = (N-2)/2.  Mirrors the definition in
    `QOU.Organic.alexanderWeightDifference` (ring-closure-barrier);
    repeated here so this content-block sibling compiles standalone. -/
-- Ref: [leitner2026] Ch. 10, Proposition: Ring-closure energy barrier
def alexanderWeightDifference (N : ℕ) : ℕ :=
  (N - 1) - N / 2

/-- The barrier prediction for even-N rings:
    ΔE ∝ (N-1) - N/2 = (N-2)/2.
    For N=6: ΔE ∝ 2. For N=8: ΔE ∝ 3. Etc. -/
-- Ref: [leitner2026] Ch. 10, Proposition: Predicted vs. observed barrier
theorem barrier_grows_with_ring_size :
    alexanderWeightDifference 6 < alexanderWeightDifference 8 := by
  decide

/-- **Class-axiomatised molecular chain-to-ring barrier calibration (`conj:chain-ring-comparison`, §3b-cond).**
    Models a positive integer crossing-energy quantum `quantum_meV : ℕ`
    assigning barrier `quantum_meV * alexanderWeightDifference N` to even-`N`
    rings. -/
class ChainRingBarrierConjecture where
  quantum_meV : ℕ
  quantum_pos : 0 < quantum_meV
  calibratedBarrier : ℕ → ℕ
  barrier_formula :
    ∀ N : ℕ, calibratedBarrier N = quantum_meV * alexanderWeightDifference N

/-- **Conditional theorem.** Under `[ChainRingBarrierConjecture]`, the calibrated
    cyclooctatetraene (`N = 8`) barrier strictly exceeds the benzene (`N = 6`)
    barrier (`2 * quantum < 3 * quantum`). -/
theorem calibrated_barrier_six_lt_eight [c : ChainRingBarrierConjecture] :
    c.calibratedBarrier 6 < c.calibratedBarrier 8 := by
  rw [c.barrier_formula 6, c.barrier_formula 8]
  have hpos := c.quantum_pos
  have hlt : alexanderWeightDifference 6 < alexanderWeightDifference 8 :=
    barrier_grows_with_ring_size
  exact Nat.mul_lt_mul_of_pos_left hlt hpos

end QOU.Organic
