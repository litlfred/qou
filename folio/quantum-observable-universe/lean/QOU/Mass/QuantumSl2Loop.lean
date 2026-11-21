import QOU.Mass.QuantumSl2ClaspFlip

/-!
# Bending an operator into a trace, and the loop around a hook

`natOp W` bends the first output of `W` down to the left and its second input up to the right
(`trace_mul_rotOp`). Here we show it is an ordinary rotation after a weight twist:

    nat W = rot((K ⊗ 1) · W · (1 ⊗ K⁻¹))        (`natOp_eq_rotOp`),

because swapping the legs of the cup or cap costs `(−1)^m` and a power of `q`
(`capVec_swap`, `cupVec_swap`).

This is a step of the Whitehead flype (issue #7912).

-- Ref: [kassel1995] Kassel, "Quantum Groups", Ch. XIV
-- Ref: [kauffman1987] Kauffman, "State models and the Jones polynomial", Topology 26 (1987)
-/

namespace QOU.Mass.QuantumSl2

open Matrix

variable {𝕜 : Type*} [Field 𝕜]

section Swap

variable (q : 𝕜) (hq : q ≠ 0) (m : ℕ) (hint : ∀ i, 0 < i → i ≤ m → qint q i ≠ 0)

include hq hint in
/-- **Swapping the cap:** `cap(a, b) = (−1)^m q^{wt a} cap(b, a)`. -/
theorem capVec_swap (a b : Fin (m + 1)) :
    capVec q m (a, b) = (-1) ^ m * q ^ wt m a * capVec q m (b, a) := by
  by_cases h : (a : ℕ) + b = m
  · simp only [capVec]
    rw [if_pos h, if_pos (by omega)]
    have hs := snake_coef' q hq m hint a (by omega)
    rw [show (b : ℕ) = m - a by omega]
    have hA := hwCoef_ne_zero q hq m hint a (by omega)
    rw [eq_inv_of_mul_eq_one_right hs]
    unfold capCoefQ
    rw [show ((m : ℤ) - 2 * ((a : ℕ) : ℤ)) = wt m a from rfl]
    field_simp
  · simp only [capVec]
    rw [if_neg h, if_neg (by omega), mul_zero]

include hq hint in
/-- **Swapping the cup:** `cup(a, b) = (−1)^m q^{−wt b} cup(b, a)`. -/
theorem cupVec_swap (a b : Fin (m + 1)) :
    cupVec q m (a, b) = (-1) ^ m * (q ^ wt m b)⁻¹ * cupVec q m (b, a) := by
  by_cases h : (a : ℕ) + b = m
  · simp only [cupVec, hwVec]
    rw [if_pos h, if_pos (by omega)]
    have hs := snake_coef' q hq m hint b (by omega)
    rw [show m - (b : ℕ) = a by omega] at hs
    have hA := hwCoef_ne_zero q hq m hint a (by omega)
    have hB := hwCoef_ne_zero q hq m hint b (by omega)
    rw [eq_inv_of_mul_eq_one_left hs]
    unfold capCoefQ
    rw [show ((m : ℤ) - 2 * ((a : ℕ) : ℤ)) = -wt m b by unfold wt; omega]
    have hq' : q ^ wt m b ≠ 0 := zpow_ne_zero _ hq
    rw [zpow_neg]
    field_simp
  · simp only [cupVec, hwVec]
    rw [if_neg h, if_neg (by omega), mul_zero]

include hq hint in
/-- **Bending is rotation after a twist:** `nat W = rot((K ⊗ 1) W (1 ⊗ K⁻¹))`. -/
theorem natOp_eq_rotOp (W : Matrix (Fin (m + 1) × Fin (m + 1)) (Fin (m + 1) × Fin (m + 1)) 𝕜) :
    natOp q m W = rotOp q m (diagonal (fun x : Fin (m + 1) × Fin (m + 1) => q ^ wt m x.1) * W
      * diagonal (fun x : Fin (m + 1) × Fin (m + 1) => (q ^ wt m x.2)⁻¹)) := by
  ext y x
  rw [rotOp_apply]
  simp only [natOp, diagonal_mul, mul_diagonal]
  refine Finset.sum_congr rfl fun a _ => Finset.sum_congr rfl fun d _ => ?_
  rw [capVec_swap q hq m hint a x.1, cupVec_swap q hq m hint y.2 d]
  have h1 : ((-1 : 𝕜)) ^ m * (-1) ^ m = 1 := by rw [← mul_pow]; simp
  linear_combination (capVec q m (x.1, a) * (q ^ wt m a * W (a, y.1) (x.2, d) * (q ^ wt m d)⁻¹)
    * cupVec q m (d, y.2)) * h1

end Swap

end QOU.Mass.QuantumSl2
