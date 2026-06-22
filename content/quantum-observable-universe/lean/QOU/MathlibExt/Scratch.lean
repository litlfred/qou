import Mathlib.LinearAlgebra.Matrix.PosDef

open Matrix

theorem quadratic_form_two_index_proof
    {n : ℕ} {C : Matrix (Fin n) (Fin n) ℝ} (hH : C.IsHermitian)
    (α β : ℝ) {i j : Fin n} :
    dotProduct (star (Pi.single i α + Pi.single j β))
      (C.mulVec (Pi.single i α + Pi.single j β)) =
    α ^ 2 * C i i + 2 * α * β * C i j + β ^ 2 * C j j := by
  have hsymm : C j i = C i j := by
    have h := congrFun (congrFun hH i) j
    simpa [Matrix.conjTranspose_apply, star_trivial] using h
  rw [show (star (Pi.single i α + Pi.single j β) : Fin n → ℝ)
        = Pi.single i α + Pi.single j β by
      funext k; simp [star_trivial]]
  simp only [dotProduct, Matrix.mulVec, Pi.add_apply, Pi.single_apply,
    Finset.sum_add_distrib, add_mul, mul_add, ite_mul, mul_ite, zero_mul, mul_zero,
    Finset.sum_ite_eq', Finset.mem_univ, if_true]
  rw [hsymm]; ring
