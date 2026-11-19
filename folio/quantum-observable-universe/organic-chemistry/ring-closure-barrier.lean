import Mathlib.Data.Nat.Basic
import Mathlib.Algebra.Group.Even
import Mathlib.Tactic.Common


/-!
# QOU.Organic.RingClosureBarrier — Ring-closure energy barrier

The transition from a pairwise Hopf chain to a threaded ring is a
topological phase transition.  The ring has lower Alexander weight
(more efficient binding) but the transition passes through a state
of maximum crossing energy.

## References

- [leitner2026] Ch. 10, §2 Molecular Hopf chains and rings
-/

namespace QOU.Organic

/-- The Alexander weight difference between chain and threaded ring.
    For even N: (N-1) - N/2 = (N-2)/2.
    This quantity is proportional to the energy barrier. -/
-- Ref: [leitner2026] Ch. 10, Proposition: Ring-closure energy barrier
def alexanderWeightDifference (N : ℕ) : ℕ :=
  (N - 1) - N / 2

/-- For N = 6, the Alexander weight difference is 2. -/
-- Ref: [leitner2026] Ch. 10, Proposition: Predicted vs. observed barrier
theorem alexander_weight_diff_six : alexanderWeightDifference 6 = 2 := by
  rfl

/-- The weight difference increases with N (for even N ≥ 4). -/
-- Ref: [leitner2026] Ch. 10, Proposition: Ring-closure energy barrier
theorem weight_diff_monotone (N M : ℕ) (hN : Even N) (hM : Even M)
    (hNge : 4 ≤ N) (hMge : 4 ≤ M) (hle : N ≤ M) :
    alexanderWeightDifference N ≤ alexanderWeightDifference M := by
  simp [alexanderWeightDifference]
  obtain ⟨k, hk⟩ := hN
  obtain ⟨j, hj⟩ := hM
  rw [hk, hj]
  omega

/-- The ring-opening barrier exceeds the ring-closure barrier.
    Formally: the threading link provides additional stabilisation
    equal to the Alexander weight saved. -/
-- Ref: [leitner2026] Ch. 10, Proposition: Ring-closure energy barrier
theorem ring_opening_exceeds_closure (N : ℕ) (heven : Even N) (hge : 4 ≤ N) :
    N / 2 < N - 1 := by
  obtain ⟨k, hk⟩ := heven
  rw [hk]
  omega

/-- **Class-axiomatised ring-closure barrier scaling (`conj:ring-closure-barrier`, §3b-cond).** -/
class RingClosureBarrierConjecture where
  unitEnergy : ℕ
  unitEnergy_pos : 0 < unitEnergy
  barrierEnergy : ℕ → ℕ
  barrier_proportional :
    ∀ N : ℕ, Even N → 4 ≤ N → barrierEnergy N = unitEnergy * alexanderWeightDifference N

/-- **Conditional theorem (monotonicity of ring-closure barrier).** Under
    `[RingClosureBarrierConjecture]`, the energy barrier increases weakly with
    even ring size `4 ≤ N ≤ M`. -/
theorem ring_closure_barrier_monotone [c : RingClosureBarrierConjecture]
    (N M : ℕ) (hN : Even N) (hM : Even M) (hNge : 4 ≤ N) (hMge : 4 ≤ M) (hle : N ≤ M) :
    c.barrierEnergy N ≤ c.barrierEnergy M := by
  rw [c.barrier_proportional N hN hNge, c.barrier_proportional M hM hMge]
  exact Nat.mul_le_mul_left c.unitEnergy (weight_diff_monotone N M hN hM hNge hMge hle)

end QOU.Organic
