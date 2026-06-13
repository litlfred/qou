import Mathlib.LinearAlgebra.Matrix.PosDef

open Matrix

theorem quadratic_form_two_index_proof
    {n : ℕ} {C : Matrix (Fin n) (Fin n) ℝ} (hH : C.IsHermitian)
    (α β : ℝ) {i j : Fin n} (hij : i ≠ j) :
    dotProduct (star (Pi.single i α + Pi.single j β))
      (C.mulVec (Pi.single i α + Pi.single j β)) =
    α ^ 2 * C i i + 2 * α * β * C i j + β ^ 2 * C j j := by
  have hsymm : C j i = C i j := by
    have h1 := hH j i
    exact h1.symm
  simp [dotProduct, mulVec, Pi.single, star]
  sorry -- Ref: [pos_semidef_diag_zero]
