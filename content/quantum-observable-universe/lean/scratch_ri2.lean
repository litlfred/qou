import QOU.Mathlib.RothIndex
open MvPolynomial
-- X^2 at the origin with weight 1: index should be exactly 2.
example : index (fun _ : Fin 1 => 1) (fun _ : Fin 1 => (0:ℚ)) (X 0 ^ 2) = (2 : ℚ) := by
  have ht : translate (fun _ : Fin 1 => (0:ℚ)) (X 0 ^ 2) = (X 0 ^ 2 : MvPolynomial (Fin 1) ℚ) := by
    simp [translate]
  rw [index, ht]
  rw [show ((X 0 : MvPolynomial (Fin 1) ℚ) ^ 2) = monomial (Finsupp.single 0 2) 1 by
        simp [X_pow_eq_monomial]]
  rw [support_monomial]
  simp [idxWeight, Finsupp.single_apply]
