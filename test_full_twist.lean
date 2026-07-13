import QOU.Interactions.CentralElement

open QOU.Interactions QOU.Archimedean Matrix

theorem fullTwist_sq_eq_one_test :
    (stdRep3_gen0 * stdRep3_gen1 * stdRep3_gen0) *
    (stdRep3_gen0 * stdRep3_gen1 * stdRep3_gen0) = (1 : TMatrix) := by
  ext i j : 1
  fin_cases i <;> fin_cases j <;>
    simp [stdRep3_gen0, stdRep3_gen1, Matrix.mul_apply, Fin.sum_univ_two, Matrix.of_apply] <;>
    simp only [q_from_t, q_inv_from_t, t, t_inv, mul_add, add_mul, neg_mul,
               mul_neg, mul_one, one_mul, sub_mul, mul_sub,
               ← LaurentPolynomial.T_add,
               Int.reduceAdd, Int.reduceNeg, LaurentPolynomial.T_zero] <;>
    ring1
