/-!
# QOU.Organic.OddNRingBarrier — Odd-N ring closure barrier

For odd N, the closed ring is a torus knot T(2, N) and the barrier
specialises to (N − 2)·|q+q⁻¹|_mol in the classical limit q → 1.

## References

- [manuscript] Ch. 10, Proposition `prop:odd-N-ring-barrier`
- [manuscript] Ch. 10, Proposition `prop:ring-closure-barrier-quantitative`
- [manuscript] Ch. 10, Definition `def:torus-knot-T2-odd-alexander`
-/

namespace QOU.Organic

/-- Odd-N ring closure barrier in the classical limit q → 1:
    `(N − 2) · |q+q⁻¹|_mol`. -/
-- Ref: [manuscript] Ch. 10, Proposition prop:odd-N-ring-barrier
def oddNRingBarrierClassical (N : ℕ) (e_mol : ℝ) : ℝ :=
  ((N : ℝ) - 2) * e_mol

/-- For odd N ≥ 3, the classical-limit barrier is positive when
    e_mol is positive. -/
-- Ref: [manuscript] Ch. 10, Proposition prop:odd-N-ring-barrier
theorem oddNRingBarrierClassical_pos
    (N : ℕ) (e_mol : ℝ) (h_N : 3 ≤ N) (h_e : 0 < e_mol) :
    0 < oddNRingBarrierClassical N e_mol := by
  unfold oddNRingBarrierClassical
  have hN_real : (3 : ℝ) ≤ (N : ℝ) := by exact_mod_cast h_N
  have : (1 : ℝ) ≤ (N : ℝ) - 2 := by linarith
  have h_pos : 0 < (N : ℝ) - 2 := by linarith
  exact mul_pos h_pos h_e

end QOU.Organic
