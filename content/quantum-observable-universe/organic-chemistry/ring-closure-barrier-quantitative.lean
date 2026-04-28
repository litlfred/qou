/-!
# QOU.Organic.RingClosureBarrierQuantitative — ΔE_closure(N) formula

The quantitative ring-closure barrier as a function of the
threading Alexander weight and the molecular crossing-energy
quantum.

## References

- [manuscript] Ch. 10, Proposition `prop:ring-closure-barrier-quantitative`
- [manuscript] Ch. 10, Proposition `prop:molecular-crossing-quantum`
- [manuscript] Ch. 10, Lemma `lem:alexander-T2N-closed-form`
-/

namespace QOU.Organic

/-- The closure barrier for an even-N ring as a real-valued function
    of the chain length N, the threading Alexander weight at q₀, and
    the molecular crossing-energy quantum e_mol. -/
-- Ref: [manuscript] Ch. 10, Proposition prop:ring-closure-barrier-quantitative
def ringClosureBarrierQuantitative
    (N : ℕ) (delta_q0 e_mol : ℝ) : ℝ :=
  ((N : ℝ) - 1 - delta_q0) * e_mol

/-- The barrier vanishes precisely when the threading weight equals
    the chain weight (N − 1). -/
-- Ref: [manuscript] Ch. 10, Proposition prop:ring-closure-barrier-quantitative
theorem ringClosureBarrier_zero_iff
    (N : ℕ) (delta_q0 e_mol : ℝ) (h_e : e_mol ≠ 0) :
    ringClosureBarrierQuantitative N delta_q0 e_mol = 0
      ↔ delta_q0 = (N : ℝ) - 1 := by
  unfold ringClosureBarrierQuantitative
  constructor
  · intro h
    have : (N : ℝ) - 1 - delta_q0 = 0 := by
      rcases mul_eq_zero.mp h with h | h
      · exact h
      · exact absurd h h_e
    linarith
  · intro h
    rw [h]; ring

/-- Linearity in the crossing quantum. -/
-- Ref: [manuscript] Ch. 10, Proposition prop:ring-closure-barrier-quantitative
theorem ringClosureBarrier_scale
    (N : ℕ) (delta_q0 e_mol c : ℝ) :
    ringClosureBarrierQuantitative N delta_q0 (c * e_mol)
      = c * ringClosureBarrierQuantitative N delta_q0 e_mol := by
  unfold ringClosureBarrierQuantitative; ring

end QOU.Organic
