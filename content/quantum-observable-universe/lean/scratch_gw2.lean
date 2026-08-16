import QOU.Mathlib.GenWronskian
open Polynomial
-- 1 and X are independent; their Wronskian is det [[1, X], [0, 1]] = 1, non-zero.
example : genWronskian (R := ℚ) ![1, X] = 1 := by
  simp [genWronskian, wronskianMatrix, Matrix.det_fin_two]
