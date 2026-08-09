import QOU.Machinery.MarkovTraceH4Gram6

/-!
# QOU.Machinery.H4 Gram closure — part 7 of 8

Auto-generated Gram entries `G_(i,j) = tr_M(b_i * b_j)`, emitted by
`computations/markov/gen_gram_closure.py`.

Split across 8 modules, each importing the previous, so the chain is
built serially and peak elaboration memory stays bounded. Held as ONE module the
closure needs ~15 GB and over an hour (bean qou-8hjy); the split is a pure
refactor — same theorems, same proofs, same namespace.
-/

namespace QOU.Machinery.H4

variable {R : Type*} [CommRing R]

theorem gramval_21_0 (z h : R) : trM z h (mulNF h (e (21:Fin 24)) (e (0:Fin 24))) = h^2*z^3 + 2*h*z^2 + z := by
  have hmul : mulNF h (e (21:Fin 24)) (e (0:Fin 24)) = e (21 : Fin 24) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (21 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  rw [hh0]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_21_1 (z h : R) : trM z h (mulNF h (e (21:Fin 24)) (e (1:Fin 24))) = h^3*z^3 + 2*h^2*z^2 + h*z^3 + h*z + z^2 := by
  have hmul : mulNF h (e (21:Fin 24)) (e (1:Fin 24)) = mulσ2 h (e (21 : Fin 24)) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (21 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ2 h (e (21 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, h, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  rw [hh1]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_21_2 (z h : R) : trM z h (mulNF h (e (21:Fin 24)) (e (2:Fin 24))) = h^3*z^3 + h^2*z^2 + 2*h*z^3 + z^2 := by
  have hmul : mulNF h (e (21:Fin 24)) (e (2:Fin 24)) = mulσ1 h (e (21 : Fin 24)) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (21 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ1 h (e (21 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  rw [hh1]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_21_3 (z h : R) : trM z h (mulNF h (e (21:Fin 24)) (e (3:Fin 24))) = h^3*z^3 + 2*h^2*z^2 + h*z^3 + h*z + z^2 := by
  have hmul : mulNF h (e (21:Fin 24)) (e (3:Fin 24)) = mulσ0 h (e (21 : Fin 24)) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (21 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ0 h (e (21 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, h, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  rw [hh1]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_21_4 (z h : R) : trM z h (mulNF h (e (21:Fin 24)) (e (4:Fin 24))) = h^4*z^3 + h^3*z^2 + 3*h^2*z^3 + 2*h*z^2 + z^3 := by
  have hmul : mulNF h (e (21:Fin 24)) (e (4:Fin 24)) = mulσ2 h (mulσ1 h (e (21 : Fin 24))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (21 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ1 h (e (21 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh2 : mulσ2 h (mulσ1 h (e (21 : Fin 24))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, h] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  rw [hh2]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_21_5 (z h : R) : trM z h (mulNF h (e (21:Fin 24)) (e (5:Fin 24))) = h^4*z^3 + h^3*z^2 + 3*h^2*z^3 + 2*h*z^2 + z^3 := by
  have hmul : mulNF h (e (21:Fin 24)) (e (5:Fin 24)) = mulσ1 h (mulσ2 h (e (21 : Fin 24))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (21 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ2 h (e (21 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, h, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  have hh2 : mulσ1 h (mulσ2 h (e (21 : Fin 24))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, h, 0, 0, 0, h] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  rw [hh2]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_21_6 (z h : R) : trM z h (mulNF h (e (21:Fin 24)) (e (6:Fin 24))) = h^4*z^3 + 2*h^3*z^2 + 2*h^2*z^3 + h^2*z + 2*h*z^2 + z^3 := by
  have hmul : mulNF h (e (21:Fin 24)) (e (6:Fin 24)) = mulσ0 h (mulσ2 h (e (21 : Fin 24))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (21 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ2 h (e (21 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, h, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  have hh2 : mulσ0 h (mulσ2 h (e (21 : Fin 24))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, h, 0, 0, 0, h, 0, h^2, 0, 0] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  rw [hh2]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_21_7 (z h : R) : trM z h (mulNF h (e (21:Fin 24)) (e (7:Fin 24))) = h^4*z^3 + h^3*z^2 + 3*h^2*z^3 + 2*h*z^2 + z^3 := by
  have hmul : mulNF h (e (21:Fin 24)) (e (7:Fin 24)) = mulσ1 h (mulσ0 h (e (21 : Fin 24))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (21 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ0 h (e (21 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, h, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  have hh2 : mulσ1 h (mulσ0 h (e (21 : Fin 24))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, h] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  rw [hh2]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_21_8 (z h : R) : trM z h (mulNF h (e (21:Fin 24)) (e (8:Fin 24))) = h^4*z^3 + h^3*z^2 + 3*h^2*z^3 + 2*h*z^2 + z^3 := by
  have hmul : mulNF h (e (21:Fin 24)) (e (8:Fin 24)) = mulσ0 h (mulσ1 h (e (21 : Fin 24))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (21 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ1 h (e (21 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh2 : mulσ0 h (mulσ1 h (e (21 : Fin 24))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, h] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  rw [hh2]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_21_9 (z h : R) : trM z h (mulNF h (e (21:Fin 24)) (e (9:Fin 24))) = h^5*z^3 + h^4*z^2 + 4*h^3*z^3 + 4*h^2*z^2 + 2*h*z^3 + h*z + z^2 := by
  have hmul : mulNF h (e (21:Fin 24)) (e (9:Fin 24)) = mulσ1 h (mulσ2 h (mulσ1 h (e (21 : Fin 24)))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (21 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ1 h (e (21 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh2 : mulσ2 h (mulσ1 h (e (21 : Fin 24))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, h] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  have hh3 : mulσ1 h (mulσ2 h (mulσ1 h (e (21 : Fin 24)))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, h, h, h^2] := by rw [hh2]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  rw [hh3]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_21_10 (z h : R) : trM z h (mulNF h (e (21:Fin 24)) (e (10:Fin 24))) = h^5*z^3 + h^4*z^2 + 4*h^3*z^3 + 3*h^2*z^2 + 3*h*z^3 + z^2 := by
  have hmul : mulNF h (e (21:Fin 24)) (e (10:Fin 24)) = mulσ2 h (mulσ1 h (mulσ0 h (e (21 : Fin 24)))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (21 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ0 h (e (21 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, h, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  have hh2 : mulσ1 h (mulσ0 h (e (21 : Fin 24))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, h] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh3 : mulσ2 h (mulσ1 h (mulσ0 h (e (21 : Fin 24)))) = ![0, 0, 0, 0, 0, 0, 0, 1, 0, 0, h, h, 0, 0, 0, h^2, 0, 0, 0, 0, 0, 0, h, h^2] := by rw [hh2]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  rw [hh3]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_21_11 (z h : R) : trM z h (mulNF h (e (21:Fin 24)) (e (11:Fin 24))) = h^5*z^3 + h^4*z^2 + 4*h^3*z^3 + 3*h^2*z^2 + 3*h*z^3 + z^2 := by
  have hmul : mulNF h (e (21:Fin 24)) (e (11:Fin 24)) = mulσ1 h (mulσ0 h (mulσ2 h (e (21 : Fin 24)))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (21 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ2 h (e (21 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, h, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  have hh2 : mulσ0 h (mulσ2 h (e (21 : Fin 24))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, h, 0, 0, 0, h, 0, h^2, 0, 0] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  have hh3 : mulσ1 h (mulσ0 h (mulσ2 h (e (21 : Fin 24)))) = ![0, 0, 0, 0, 0, 0, 1, 0, 0, 0, h, h, 0, 0, h, h^2, 0, 0, 0, h^2, 0, 0, 0, h^2] := by rw [hh2]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  rw [hh3]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_21_12 (z h : R) : trM z h (mulNF h (e (21:Fin 24)) (e (12:Fin 24))) = h^5*z^3 + h^4*z^2 + 4*h^3*z^3 + 3*h^2*z^2 + 3*h*z^3 + z^2 := by
  have hmul : mulNF h (e (21:Fin 24)) (e (12:Fin 24)) = mulσ0 h (mulσ2 h (mulσ1 h (e (21 : Fin 24)))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (21 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ1 h (e (21 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh2 : mulσ2 h (mulσ1 h (e (21 : Fin 24))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, h] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  have hh3 : mulσ0 h (mulσ2 h (mulσ1 h (e (21 : Fin 24)))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, h, 0, h, h^2] := by rw [hh2]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  rw [hh3]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_21_13 (z h : R) : trM z h (mulNF h (e (21:Fin 24)) (e (13:Fin 24))) = h^5*z^3 + h^4*z^2 + 4*h^3*z^3 + 4*h^2*z^2 + 2*h*z^3 + h*z + z^2 := by
  have hmul : mulNF h (e (21:Fin 24)) (e (13:Fin 24)) = mulσ0 h (mulσ1 h (mulσ0 h (e (21 : Fin 24)))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (21 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ0 h (e (21 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, h, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  have hh2 : mulσ1 h (mulσ0 h (e (21 : Fin 24))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, h] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh3 : mulσ0 h (mulσ1 h (mulσ0 h (e (21 : Fin 24)))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, h, h, 0, h^2] := by rw [hh2]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  rw [hh3]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_21_14 (z h : R) : trM z h (mulNF h (e (21:Fin 24)) (e (14:Fin 24))) = h^5*z^3 + h^4*z^2 + 4*h^3*z^3 + 3*h^2*z^2 + 3*h*z^3 + z^2 := by
  have hmul : mulNF h (e (21:Fin 24)) (e (14:Fin 24)) = mulσ0 h (mulσ1 h (mulσ2 h (e (21 : Fin 24)))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (21 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ2 h (e (21 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, h, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  have hh2 : mulσ1 h (mulσ2 h (e (21 : Fin 24))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, h, 0, 0, 0, h] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh3 : mulσ0 h (mulσ1 h (mulσ2 h (e (21 : Fin 24)))) = ![0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, h, 0, 0, h, 0, 0, 0, 0, h^2, h, 0, 0, h^2] := by rw [hh2]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  rw [hh3]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_21_15 (z h : R) : trM z h (mulNF h (e (21:Fin 24)) (e (15:Fin 24))) = h^6*z^3 + h^5*z^2 + 5*h^4*z^3 + 5*h^3*z^2 + 5*h^2*z^3 + h^2*z + 4*h*z^2 + z := by
  have hmul : mulNF h (e (21:Fin 24)) (e (15:Fin 24)) = mulσ1 h (mulσ2 h (mulσ1 h (mulσ0 h (e (21 : Fin 24))))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (21 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ0 h (e (21 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, h, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  have hh2 : mulσ1 h (mulσ0 h (e (21 : Fin 24))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, h] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh3 : mulσ2 h (mulσ1 h (mulσ0 h (e (21 : Fin 24)))) = ![0, 0, 0, 0, 0, 0, 0, 1, 0, 0, h, h, 0, 0, 0, h^2, 0, 0, 0, 0, 0, 0, h, h^2] := by rw [hh2]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  have hh4 : mulσ1 h (mulσ2 h (mulσ1 h (mulσ0 h (e (21 : Fin 24))))) = ![0, 0, 0, 1, 0, 0, h, h, 0, 0, h^2, h^2, 0, 0, 0, h^3 + h, 0, 0, h, 0, 0, h^2, h^2, h^3] := by rw [hh3]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  rw [hh4]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_21_16 (z h : R) : trM z h (mulNF h (e (21:Fin 24)) (e (16:Fin 24))) = h^6*z^3 + h^5*z^2 + 5*h^4*z^3 + 5*h^3*z^2 + 5*h^2*z^3 + h^2*z + 4*h*z^2 + z := by
  have hmul : mulNF h (e (21:Fin 24)) (e (16:Fin 24)) = mulσ0 h (mulσ2 h (mulσ1 h (mulσ0 h (e (21 : Fin 24))))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (21 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ0 h (e (21 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, h, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  have hh2 : mulσ1 h (mulσ0 h (e (21 : Fin 24))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, h] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh3 : mulσ2 h (mulσ1 h (mulσ0 h (e (21 : Fin 24)))) = ![0, 0, 0, 0, 0, 0, 0, 1, 0, 0, h, h, 0, 0, 0, h^2, 0, 0, 0, 0, 0, 0, h, h^2] := by rw [hh2]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  have hh4 : mulσ0 h (mulσ2 h (mulσ1 h (mulσ0 h (e (21 : Fin 24))))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, h, h, 0, h, h^2, h^2, h^2, h^3] := by rw [hh3]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  rw [hh4]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_21_17 (z h : R) : trM z h (mulNF h (e (21:Fin 24)) (e (17:Fin 24))) = h^6*z^3 + h^5*z^2 + 5*h^4*z^3 + 5*h^3*z^2 + 5*h^2*z^3 + h^2*z + 3*h*z^2 + z^3 := by
  have hmul : mulNF h (e (21:Fin 24)) (e (17:Fin 24)) = mulσ1 h (mulσ0 h (mulσ2 h (mulσ1 h (e (21 : Fin 24))))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (21 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ1 h (e (21 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh2 : mulσ2 h (mulσ1 h (e (21 : Fin 24))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, h] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  have hh3 : mulσ0 h (mulσ2 h (mulσ1 h (e (21 : Fin 24)))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, h, 0, h, h^2] := by rw [hh2]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  have hh4 : mulσ1 h (mulσ0 h (mulσ2 h (mulσ1 h (e (21 : Fin 24))))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, h, h, h, 0, h^2, h^2, h^2, h^3] := by rw [hh3]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  rw [hh4]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_21_18 (z h : R) : trM z h (mulNF h (e (21:Fin 24)) (e (18:Fin 24))) = h^6*z^3 + h^5*z^2 + 5*h^4*z^3 + 5*h^3*z^2 + 5*h^2*z^3 + h^2*z + 4*h*z^2 + z := by
  have hmul : mulNF h (e (21:Fin 24)) (e (18:Fin 24)) = mulσ0 h (mulσ1 h (mulσ2 h (mulσ1 h (e (21 : Fin 24))))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (21 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ1 h (e (21 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh2 : mulσ2 h (mulσ1 h (e (21 : Fin 24))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, h] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  have hh3 : mulσ1 h (mulσ2 h (mulσ1 h (e (21 : Fin 24)))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, h, h, h^2] := by rw [hh2]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh4 : mulσ0 h (mulσ1 h (mulσ2 h (mulσ1 h (e (21 : Fin 24))))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, h, 0, h, h, 0, h^2, h^2, h^2, h^3] := by rw [hh3]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  rw [hh4]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_21_19 (z h : R) : trM z h (mulNF h (e (21:Fin 24)) (e (19:Fin 24))) = h^6*z^3 + h^5*z^2 + 5*h^4*z^3 + 5*h^3*z^2 + 5*h^2*z^3 + h^2*z + 4*h*z^2 + z := by
  have hmul : mulNF h (e (21:Fin 24)) (e (19:Fin 24)) = mulσ0 h (mulσ1 h (mulσ0 h (mulσ2 h (e (21 : Fin 24))))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (21 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ2 h (e (21 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, h, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  have hh2 : mulσ0 h (mulσ2 h (e (21 : Fin 24))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, h, 0, 0, 0, h, 0, h^2, 0, 0] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  have hh3 : mulσ1 h (mulσ0 h (mulσ2 h (e (21 : Fin 24)))) = ![0, 0, 0, 0, 0, 0, 1, 0, 0, 0, h, h, 0, 0, h, h^2, 0, 0, 0, h^2, 0, 0, 0, h^2] := by rw [hh2]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh4 : mulσ0 h (mulσ1 h (mulσ0 h (mulσ2 h (e (21 : Fin 24))))) = ![0, 1, 0, 0, 0, h, h, 0, 0, 0, 0, h^2, 0, 0, h^2, 0, h, 0, 0, h^3 + h, h^2, h^2, 0, h^3] := by rw [hh3]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  rw [hh4]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_21_20 (z h : R) : trM z h (mulNF h (e (21:Fin 24)) (e (20:Fin 24))) = h^7*z^3 + h^6*z^2 + 6*h^5*z^3 + 6*h^4*z^2 + 9*h^3*z^3 + h^3*z + 7*h^2*z^2 + 3*h*z^3 + h*z + z^2 := by
  have hmul : mulNF h (e (21:Fin 24)) (e (20:Fin 24)) = mulσ1 h (mulσ0 h (mulσ2 h (mulσ1 h (mulσ0 h (e (21 : Fin 24)))))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (21 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ0 h (e (21 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, h, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  have hh2 : mulσ1 h (mulσ0 h (e (21 : Fin 24))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, h] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh3 : mulσ2 h (mulσ1 h (mulσ0 h (e (21 : Fin 24)))) = ![0, 0, 0, 0, 0, 0, 0, 1, 0, 0, h, h, 0, 0, 0, h^2, 0, 0, 0, 0, 0, 0, h, h^2] := by rw [hh2]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  have hh4 : mulσ0 h (mulσ2 h (mulσ1 h (mulσ0 h (e (21 : Fin 24))))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, h, h, 0, h, h^2, h^2, h^2, h^3] := by rw [hh3]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  have hh5 : mulσ1 h (mulσ0 h (mulσ2 h (mulσ1 h (mulσ0 h (e (21 : Fin 24)))))) = ![0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, h, h, h, 0, h^2, h^2, h^2, h^2, h^3 + h, h^3, h^3, h^4 + h^2] := by rw [hh4]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  rw [hh5]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_21_21 (z h : R) : trM z h (mulNF h (e (21:Fin 24)) (e (21:Fin 24))) = h^7*z^3 + h^6*z^2 + 6*h^5*z^3 + 7*h^4*z^2 + 8*h^3*z^3 + 2*h^3*z + 10*h^2*z^2 + 5*h*z + 1 := by
  have hmul : mulNF h (e (21:Fin 24)) (e (21:Fin 24)) = mulσ0 h (mulσ1 h (mulσ2 h (mulσ1 h (mulσ0 h (e (21 : Fin 24)))))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (21 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ0 h (e (21 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, h, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  have hh2 : mulσ1 h (mulσ0 h (e (21 : Fin 24))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, h] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh3 : mulσ2 h (mulσ1 h (mulσ0 h (e (21 : Fin 24)))) = ![0, 0, 0, 0, 0, 0, 0, 1, 0, 0, h, h, 0, 0, 0, h^2, 0, 0, 0, 0, 0, 0, h, h^2] := by rw [hh2]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  have hh4 : mulσ1 h (mulσ2 h (mulσ1 h (mulσ0 h (e (21 : Fin 24))))) = ![0, 0, 0, 1, 0, 0, h, h, 0, 0, h^2, h^2, 0, 0, 0, h^3 + h, 0, 0, h, 0, 0, h^2, h^2, h^3] := by rw [hh3]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh5 : mulσ0 h (mulσ1 h (mulσ2 h (mulσ1 h (mulσ0 h (e (21 : Fin 24)))))) = ![1, h, 0, h, 0, 0, h^2, 0, 0, h, 0, 0, 0, h, 0, h^2, h^2, h^2, h^2, h^2, h^3, 2*h^3 + h, h^3, h^4] := by rw [hh4]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  rw [hh5]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_21_22 (z h : R) : trM z h (mulNF h (e (21:Fin 24)) (e (22:Fin 24))) = h^7*z^3 + h^6*z^2 + 6*h^5*z^3 + 6*h^4*z^2 + 9*h^3*z^3 + h^3*z + 7*h^2*z^2 + 3*h*z^3 + h*z + z^2 := by
  have hmul : mulNF h (e (21:Fin 24)) (e (22:Fin 24)) = mulσ0 h (mulσ1 h (mulσ0 h (mulσ2 h (mulσ1 h (e (21 : Fin 24)))))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (21 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ1 h (e (21 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh2 : mulσ2 h (mulσ1 h (e (21 : Fin 24))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, h] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  have hh3 : mulσ0 h (mulσ2 h (mulσ1 h (e (21 : Fin 24)))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, h, 0, h, h^2] := by rw [hh2]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  have hh4 : mulσ1 h (mulσ0 h (mulσ2 h (mulσ1 h (e (21 : Fin 24))))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, h, h, h, 0, h^2, h^2, h^2, h^3] := by rw [hh3]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh5 : mulσ0 h (mulσ1 h (mulσ0 h (mulσ2 h (mulσ1 h (e (21 : Fin 24)))))) = ![0, 0, 0, 0, 1, 0, 0, 0, 0, h, h, 0, h, 0, 0, h^2, h^2, h^2, h^2, 0, h^3, h^3, h^3 + h, h^4 + h^2] := by rw [hh4]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  rw [hh5]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_21_23 (z h : R) : trM z h (mulNF h (e (21:Fin 24)) (e (23:Fin 24))) = h^8*z^3 + h^7*z^2 + 7*h^6*z^3 + 7*h^5*z^2 + 14*h^4*z^3 + h^4*z + 12*h^3*z^2 + 8*h^2*z^3 + 2*h^2*z + 5*h*z^2 + z := by
  have hmul : mulNF h (e (21:Fin 24)) (e (23:Fin 24)) = mulσ0 h (mulσ1 h (mulσ0 h (mulσ2 h (mulσ1 h (mulσ0 h (e (21 : Fin 24))))))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (21 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ0 h (e (21 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, h, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  have hh2 : mulσ1 h (mulσ0 h (e (21 : Fin 24))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, h] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh3 : mulσ2 h (mulσ1 h (mulσ0 h (e (21 : Fin 24)))) = ![0, 0, 0, 0, 0, 0, 0, 1, 0, 0, h, h, 0, 0, 0, h^2, 0, 0, 0, 0, 0, 0, h, h^2] := by rw [hh2]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  have hh4 : mulσ0 h (mulσ2 h (mulσ1 h (mulσ0 h (e (21 : Fin 24))))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, h, h, 0, h, h^2, h^2, h^2, h^3] := by rw [hh3]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  have hh5 : mulσ1 h (mulσ0 h (mulσ2 h (mulσ1 h (mulσ0 h (e (21 : Fin 24)))))) = ![0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, h, h, h, 0, h^2, h^2, h^2, h^2, h^3 + h, h^3, h^3, h^4 + h^2] := by rw [hh4]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh6 : mulσ0 h (mulσ1 h (mulσ0 h (mulσ2 h (mulσ1 h (mulσ0 h (e (21 : Fin 24))))))) = ![0, 0, 1, 0, h, h, 0, h, h, h^2, h^2, h^2, h^2, h^2, h^2, h^3, h^3, h^3, h^3, h^3, h^4 + h^2, h^4, h^4 + h^2, h^5 + 2*h^3 + h] := by rw [hh5]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  rw [hh6]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_22_0 (z h : R) : trM z h (mulNF h (e (22:Fin 24)) (e (0:Fin 24))) = h^2*z^3 + h*z^2 + z^3 := by
  have hmul : mulNF h (e (22:Fin 24)) (e (0:Fin 24)) = e (22 : Fin 24) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (22 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  rw [hh0]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_22_1 (z h : R) : trM z h (mulNF h (e (22:Fin 24)) (e (1:Fin 24))) = h^3*z^3 + h^2*z^2 + 2*h*z^3 + z^2 := by
  have hmul : mulNF h (e (22:Fin 24)) (e (1:Fin 24)) = mulσ2 h (e (22 : Fin 24)) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (22 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ2 h (e (22 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  rw [hh1]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_22_2 (z h : R) : trM z h (mulNF h (e (22:Fin 24)) (e (2:Fin 24))) = h^3*z^3 + h^2*z^2 + 2*h*z^3 + z^2 := by
  have hmul : mulNF h (e (22:Fin 24)) (e (2:Fin 24)) = mulσ1 h (e (22 : Fin 24)) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (22 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ1 h (e (22 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, h, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  rw [hh1]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_22_3 (z h : R) : trM z h (mulNF h (e (22:Fin 24)) (e (3:Fin 24))) = h^3*z^3 + h^2*z^2 + 2*h*z^3 + z^2 := by
  have hmul : mulNF h (e (22:Fin 24)) (e (3:Fin 24)) = mulσ0 h (e (22 : Fin 24)) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (22 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ0 h (e (22 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, h, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  rw [hh1]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_22_4 (z h : R) : trM z h (mulNF h (e (22:Fin 24)) (e (4:Fin 24))) = h^4*z^3 + h^3*z^2 + 3*h^2*z^3 + 2*h*z^2 + z^3 := by
  have hmul : mulNF h (e (22:Fin 24)) (e (4:Fin 24)) = mulσ2 h (mulσ1 h (e (22 : Fin 24))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (22 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ1 h (e (22 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, h, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh2 : mulσ2 h (mulσ1 h (e (22 : Fin 24))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, h, 0, 0, 0, 0, h] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  rw [hh2]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_22_5 (z h : R) : trM z h (mulNF h (e (22:Fin 24)) (e (5:Fin 24))) = h^4*z^3 + h^3*z^2 + 3*h^2*z^3 + 3*h*z^2 + z := by
  have hmul : mulNF h (e (22:Fin 24)) (e (5:Fin 24)) = mulσ1 h (mulσ2 h (e (22 : Fin 24))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (22 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ2 h (e (22 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  have hh2 : mulσ1 h (mulσ2 h (e (22 : Fin 24))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, h] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  rw [hh2]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_22_6 (z h : R) : trM z h (mulNF h (e (22:Fin 24)) (e (6:Fin 24))) = h^4*z^3 + h^3*z^2 + 3*h^2*z^3 + 2*h*z^2 + z^3 := by
  have hmul : mulNF h (e (22:Fin 24)) (e (6:Fin 24)) = mulσ0 h (mulσ2 h (e (22 : Fin 24))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (22 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ2 h (e (22 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  have hh2 : mulσ0 h (mulσ2 h (e (22 : Fin 24))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, h] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  rw [hh2]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_22_7 (z h : R) : trM z h (mulNF h (e (22:Fin 24)) (e (7:Fin 24))) = h^4*z^3 + h^3*z^2 + 3*h^2*z^3 + 2*h*z^2 + z^3 := by
  have hmul : mulNF h (e (22:Fin 24)) (e (7:Fin 24)) = mulσ1 h (mulσ0 h (e (22 : Fin 24))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (22 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ0 h (e (22 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, h, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  have hh2 : mulσ1 h (mulσ0 h (e (22 : Fin 24))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, h, h, 0, 0, 0, h^2, 0] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  rw [hh2]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_22_8 (z h : R) : trM z h (mulNF h (e (22:Fin 24)) (e (8:Fin 24))) = h^4*z^3 + h^3*z^2 + 3*h^2*z^3 + 3*h*z^2 + z := by
  have hmul : mulNF h (e (22:Fin 24)) (e (8:Fin 24)) = mulσ0 h (mulσ1 h (e (22 : Fin 24))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (22 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ1 h (e (22 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, h, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh2 : mulσ0 h (mulσ1 h (e (22 : Fin 24))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, h, h, 0, 0, 0, h^2, 0] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  rw [hh2]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_22_9 (z h : R) : trM z h (mulNF h (e (22:Fin 24)) (e (9:Fin 24))) = h^5*z^3 + h^4*z^2 + 4*h^3*z^3 + 4*h^2*z^2 + 2*h*z^3 + h*z + z^2 := by
  have hmul : mulNF h (e (22:Fin 24)) (e (9:Fin 24)) = mulσ1 h (mulσ2 h (mulσ1 h (e (22 : Fin 24)))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (22 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ1 h (e (22 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, h, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh2 : mulσ2 h (mulσ1 h (e (22 : Fin 24))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, h, 0, 0, 0, 0, h] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  have hh3 : mulσ1 h (mulσ2 h (mulσ1 h (e (22 : Fin 24)))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, h, h, h^2] := by rw [hh2]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  rw [hh3]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_22_10 (z h : R) : trM z h (mulNF h (e (22:Fin 24)) (e (10:Fin 24))) = h^5*z^3 + h^4*z^2 + 4*h^3*z^3 + 3*h^2*z^2 + 3*h*z^3 + z^2 := by
  have hmul : mulNF h (e (22:Fin 24)) (e (10:Fin 24)) = mulσ2 h (mulσ1 h (mulσ0 h (e (22 : Fin 24)))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (22 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ0 h (e (22 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, h, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  have hh2 : mulσ1 h (mulσ0 h (e (22 : Fin 24))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, h, h, 0, 0, 0, h^2, 0] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh3 : mulσ2 h (mulσ1 h (mulσ0 h (e (22 : Fin 24)))) = ![0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, h, 0, h, 0, 0, 0, h^2, 0, h, 0, 0, h^2] := by rw [hh2]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  rw [hh3]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_22_11 (z h : R) : trM z h (mulNF h (e (22:Fin 24)) (e (11:Fin 24))) = h^5*z^3 + h^4*z^2 + 4*h^3*z^3 + 4*h^2*z^2 + 2*h*z^3 + h*z + z^2 := by
  have hmul : mulNF h (e (22:Fin 24)) (e (11:Fin 24)) = mulσ1 h (mulσ0 h (mulσ2 h (e (22 : Fin 24)))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (22 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ2 h (e (22 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  have hh2 : mulσ0 h (mulσ2 h (e (22 : Fin 24))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, h] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  have hh3 : mulσ1 h (mulσ0 h (mulσ2 h (e (22 : Fin 24)))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, h, h, 0, h^2] := by rw [hh2]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  rw [hh3]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_22_12 (z h : R) : trM z h (mulNF h (e (22:Fin 24)) (e (12:Fin 24))) = h^5*z^3 + h^4*z^2 + 4*h^3*z^3 + 4*h^2*z^2 + 2*h*z^3 + h*z + z^2 := by
  have hmul : mulNF h (e (22:Fin 24)) (e (12:Fin 24)) = mulσ0 h (mulσ2 h (mulσ1 h (e (22 : Fin 24)))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (22 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ1 h (e (22 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, h, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh2 : mulσ2 h (mulσ1 h (e (22 : Fin 24))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, h, 0, 0, 0, 0, h] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  have hh3 : mulσ0 h (mulσ2 h (mulσ1 h (e (22 : Fin 24)))) = ![0, 0, 0, 0, 0, 1, 0, 0, 0, h, 0, 0, 0, 0, h, 0, 0, 0, h^2, 0, h, 0, 0, h^2] := by rw [hh2]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  rw [hh3]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_22_13 (z h : R) : trM z h (mulNF h (e (22:Fin 24)) (e (13:Fin 24))) = h^5*z^3 + h^4*z^2 + 4*h^3*z^3 + 4*h^2*z^2 + 2*h*z^3 + h*z + z^2 := by
  have hmul : mulNF h (e (22:Fin 24)) (e (13:Fin 24)) = mulσ0 h (mulσ1 h (mulσ0 h (e (22 : Fin 24)))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (22 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ0 h (e (22 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, h, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  have hh2 : mulσ1 h (mulσ0 h (e (22 : Fin 24))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, h, h, 0, 0, 0, h^2, 0] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh3 : mulσ0 h (mulσ1 h (mulσ0 h (e (22 : Fin 24)))) = ![0, 0, 0, 0, 1, 0, 0, 0, 0, h, 0, 0, h, 0, 0, 0, 0, h^2, h^2, 0, 0, 0, h^3 + h, 0] := by rw [hh2]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  rw [hh3]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_22_14 (z h : R) : trM z h (mulNF h (e (22:Fin 24)) (e (14:Fin 24))) = h^5*z^3 + h^4*z^2 + 4*h^3*z^3 + 4*h^2*z^2 + 2*h*z^3 + h*z + z^2 := by
  have hmul : mulNF h (e (22:Fin 24)) (e (14:Fin 24)) = mulσ0 h (mulσ1 h (mulσ2 h (e (22 : Fin 24)))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (22 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ2 h (e (22 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  have hh2 : mulσ1 h (mulσ2 h (e (22 : Fin 24))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, h] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh3 : mulσ0 h (mulσ1 h (mulσ2 h (e (22 : Fin 24)))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, h, h, 0, h^2] := by rw [hh2]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  rw [hh3]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_22_15 (z h : R) : trM z h (mulNF h (e (22:Fin 24)) (e (15:Fin 24))) = h^6*z^3 + h^5*z^2 + 5*h^4*z^3 + 5*h^3*z^2 + 5*h^2*z^3 + h^2*z + 4*h*z^2 + z := by
  have hmul : mulNF h (e (22:Fin 24)) (e (15:Fin 24)) = mulσ1 h (mulσ2 h (mulσ1 h (mulσ0 h (e (22 : Fin 24))))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (22 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ0 h (e (22 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, h, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  have hh2 : mulσ1 h (mulσ0 h (e (22 : Fin 24))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, h, h, 0, 0, 0, h^2, 0] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh3 : mulσ2 h (mulσ1 h (mulσ0 h (e (22 : Fin 24)))) = ![0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, h, 0, h, 0, 0, 0, h^2, 0, h, 0, 0, h^2] := by rw [hh2]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  have hh4 : mulσ1 h (mulσ2 h (mulσ1 h (mulσ0 h (e (22 : Fin 24))))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, h, h, 0, h, h^2, h^2, h^2, h^3] := by rw [hh3]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  rw [hh4]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_22_16 (z h : R) : trM z h (mulNF h (e (22:Fin 24)) (e (16:Fin 24))) = h^6*z^3 + h^5*z^2 + 5*h^4*z^3 + 5*h^3*z^2 + 5*h^2*z^3 + h^2*z + 4*h*z^2 + z := by
  have hmul : mulNF h (e (22:Fin 24)) (e (16:Fin 24)) = mulσ0 h (mulσ2 h (mulσ1 h (mulσ0 h (e (22 : Fin 24))))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (22 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ0 h (e (22 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, h, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  have hh2 : mulσ1 h (mulσ0 h (e (22 : Fin 24))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, h, h, 0, 0, 0, h^2, 0] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh3 : mulσ2 h (mulσ1 h (mulσ0 h (e (22 : Fin 24)))) = ![0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, h, 0, h, 0, 0, 0, h^2, 0, h, 0, 0, h^2] := by rw [hh2]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  have hh4 : mulσ0 h (mulσ2 h (mulσ1 h (mulσ0 h (e (22 : Fin 24))))) = ![0, 0, 1, 0, h, h, 0, 0, h, h^2, 0, 0, h^2, 0, h^2, 0, 0, 0, h^3, 0, h^2, 0, 0, h^3 + h] := by rw [hh3]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  rw [hh4]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_22_17 (z h : R) : trM z h (mulNF h (e (22:Fin 24)) (e (17:Fin 24))) = h^6*z^3 + h^5*z^2 + 5*h^4*z^3 + 6*h^3*z^2 + 4*h^2*z^3 + 2*h^2*z + 4*h*z^2 + z := by
  have hmul : mulNF h (e (22:Fin 24)) (e (17:Fin 24)) = mulσ1 h (mulσ0 h (mulσ2 h (mulσ1 h (e (22 : Fin 24))))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (22 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ1 h (e (22 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, h, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh2 : mulσ2 h (mulσ1 h (e (22 : Fin 24))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, h, 0, 0, 0, 0, h] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  have hh3 : mulσ0 h (mulσ2 h (mulσ1 h (e (22 : Fin 24)))) = ![0, 0, 0, 0, 0, 1, 0, 0, 0, h, 0, 0, 0, 0, h, 0, 0, 0, h^2, 0, h, 0, 0, h^2] := by rw [hh2]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  have hh4 : mulσ1 h (mulσ0 h (mulσ2 h (mulσ1 h (e (22 : Fin 24))))) = ![0, 1, 0, 0, h, h, 0, 0, 0, h^2, 0, 0, 0, 0, 0, 0, h, 0, 0, h, h^2, h^2, h^2, h^3] := by rw [hh3]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  rw [hh4]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_22_18 (z h : R) : trM z h (mulNF h (e (22:Fin 24)) (e (18:Fin 24))) = h^6*z^3 + h^5*z^2 + 5*h^4*z^3 + 5*h^3*z^2 + 5*h^2*z^3 + h^2*z + 3*h*z^2 + z^3 := by
  have hmul : mulNF h (e (22:Fin 24)) (e (18:Fin 24)) = mulσ0 h (mulσ1 h (mulσ2 h (mulσ1 h (e (22 : Fin 24))))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (22 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ1 h (e (22 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, h, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh2 : mulσ2 h (mulσ1 h (e (22 : Fin 24))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, h, 0, 0, 0, 0, h] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  have hh3 : mulσ1 h (mulσ2 h (mulσ1 h (e (22 : Fin 24)))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, h, h, h^2] := by rw [hh2]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh4 : mulσ0 h (mulσ1 h (mulσ2 h (mulσ1 h (e (22 : Fin 24))))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, h, 0, h, 0, h, h^2, h^2, h^2, h^3] := by rw [hh3]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  rw [hh4]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_22_19 (z h : R) : trM z h (mulNF h (e (22:Fin 24)) (e (19:Fin 24))) = h^6*z^3 + h^5*z^2 + 5*h^4*z^3 + 5*h^3*z^2 + 5*h^2*z^3 + h^2*z + 3*h*z^2 + z^3 := by
  have hmul : mulNF h (e (22:Fin 24)) (e (19:Fin 24)) = mulσ0 h (mulσ1 h (mulσ0 h (mulσ2 h (e (22 : Fin 24))))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (22 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ2 h (e (22 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  have hh2 : mulσ0 h (mulσ2 h (e (22 : Fin 24))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, h] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  have hh3 : mulσ1 h (mulσ0 h (mulσ2 h (e (22 : Fin 24)))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, h, h, 0, h^2] := by rw [hh2]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh4 : mulσ0 h (mulσ1 h (mulσ0 h (mulσ2 h (e (22 : Fin 24))))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, h, h, 0, 0, 0, h^2, h^2, 0, h^3 + h] := by rw [hh3]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  rw [hh4]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_22_20 (z h : R) : trM z h (mulNF h (e (22:Fin 24)) (e (20:Fin 24))) = h^7*z^3 + h^6*z^2 + 6*h^5*z^3 + 7*h^4*z^2 + 8*h^3*z^3 + 2*h^3*z + 10*h^2*z^2 + 5*h*z + 1 := by
  have hmul : mulNF h (e (22:Fin 24)) (e (20:Fin 24)) = mulσ1 h (mulσ0 h (mulσ2 h (mulσ1 h (mulσ0 h (e (22 : Fin 24)))))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (22 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ0 h (e (22 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, h, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  have hh2 : mulσ1 h (mulσ0 h (e (22 : Fin 24))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, h, h, 0, 0, 0, h^2, 0] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh3 : mulσ2 h (mulσ1 h (mulσ0 h (e (22 : Fin 24)))) = ![0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, h, 0, h, 0, 0, 0, h^2, 0, h, 0, 0, h^2] := by rw [hh2]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  have hh4 : mulσ0 h (mulσ2 h (mulσ1 h (mulσ0 h (e (22 : Fin 24))))) = ![0, 0, 1, 0, h, h, 0, 0, h, h^2, 0, 0, h^2, 0, h^2, 0, 0, 0, h^3, 0, h^2, 0, 0, h^3 + h] := by rw [hh3]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  have hh5 : mulσ1 h (mulσ0 h (mulσ2 h (mulσ1 h (mulσ0 h (e (22 : Fin 24)))))) = ![1, h, h, 0, h^2, h^2, 0, 0, 0, h^3 + h, 0, 0, 0, h, 0, 0, h^2, h^2, 0, h^2, h^3, h^3 + h, h^3, h^4 + h^2] := by rw [hh4]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  rw [hh5]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_22_21 (z h : R) : trM z h (mulNF h (e (22:Fin 24)) (e (21:Fin 24))) = h^7*z^3 + h^6*z^2 + 6*h^5*z^3 + 6*h^4*z^2 + 9*h^3*z^3 + h^3*z + 7*h^2*z^2 + 3*h*z^3 + h*z + z^2 := by
  have hmul : mulNF h (e (22:Fin 24)) (e (21:Fin 24)) = mulσ0 h (mulσ1 h (mulσ2 h (mulσ1 h (mulσ0 h (e (22 : Fin 24)))))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (22 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ0 h (e (22 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, h, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  have hh2 : mulσ1 h (mulσ0 h (e (22 : Fin 24))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, h, h, 0, 0, 0, h^2, 0] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh3 : mulσ2 h (mulσ1 h (mulσ0 h (e (22 : Fin 24)))) = ![0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, h, 0, h, 0, 0, 0, h^2, 0, h, 0, 0, h^2] := by rw [hh2]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  have hh4 : mulσ1 h (mulσ2 h (mulσ1 h (mulσ0 h (e (22 : Fin 24))))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, h, h, 0, h, h^2, h^2, h^2, h^3] := by rw [hh3]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh5 : mulσ0 h (mulσ1 h (mulσ2 h (mulσ1 h (mulσ0 h (e (22 : Fin 24)))))) = ![0, 0, 0, 0, 0, 0, 0, 1, 0, 0, h, h, 0, h, 0, h^2, h^2, h^2, 0, h^2, h^3, h^3, h^3 + h, h^4 + h^2] := by rw [hh4]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  rw [hh5]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_22_22 (z h : R) : trM z h (mulNF h (e (22:Fin 24)) (e (22:Fin 24))) = h^7*z^3 + h^6*z^2 + 6*h^5*z^3 + 6*h^4*z^2 + 9*h^3*z^3 + h^3*z + 6*h^2*z^2 + 4*h*z^3 + z^2 := by
  have hmul : mulNF h (e (22:Fin 24)) (e (22:Fin 24)) = mulσ0 h (mulσ1 h (mulσ0 h (mulσ2 h (mulσ1 h (e (22 : Fin 24)))))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (22 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ1 h (e (22 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, h, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh2 : mulσ2 h (mulσ1 h (e (22 : Fin 24))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, h, 0, 0, 0, 0, h] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  have hh3 : mulσ0 h (mulσ2 h (mulσ1 h (e (22 : Fin 24)))) = ![0, 0, 0, 0, 0, 1, 0, 0, 0, h, 0, 0, 0, 0, h, 0, 0, 0, h^2, 0, h, 0, 0, h^2] := by rw [hh2]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  have hh4 : mulσ1 h (mulσ0 h (mulσ2 h (mulσ1 h (e (22 : Fin 24))))) = ![0, 1, 0, 0, h, h, 0, 0, 0, h^2, 0, 0, 0, 0, 0, 0, h, 0, 0, h, h^2, h^2, h^2, h^3] := by rw [hh3]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh5 : mulσ0 h (mulσ1 h (mulσ0 h (mulσ2 h (mulσ1 h (e (22 : Fin 24)))))) = ![0, 0, 0, 0, 0, 0, 1, 0, 0, 0, h, h, h, 0, h, h^2, h^2, h^2, h^2, h^2, h^3, h^3, h^3, h^4 + h^2] := by rw [hh4]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  rw [hh5]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_22_23 (z h : R) : trM z h (mulNF h (e (22:Fin 24)) (e (23:Fin 24))) = h^8*z^3 + h^7*z^2 + 7*h^6*z^3 + 7*h^5*z^2 + 14*h^4*z^3 + h^4*z + 12*h^3*z^2 + 8*h^2*z^3 + 2*h^2*z + 5*h*z^2 + z := by
  have hmul : mulNF h (e (22:Fin 24)) (e (23:Fin 24)) = mulσ0 h (mulσ1 h (mulσ0 h (mulσ2 h (mulσ1 h (mulσ0 h (e (22 : Fin 24))))))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (22 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ0 h (e (22 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, h, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  have hh2 : mulσ1 h (mulσ0 h (e (22 : Fin 24))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, h, h, 0, 0, 0, h^2, 0] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh3 : mulσ2 h (mulσ1 h (mulσ0 h (e (22 : Fin 24)))) = ![0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, h, 0, h, 0, 0, 0, h^2, 0, h, 0, 0, h^2] := by rw [hh2]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  have hh4 : mulσ0 h (mulσ2 h (mulσ1 h (mulσ0 h (e (22 : Fin 24))))) = ![0, 0, 1, 0, h, h, 0, 0, h, h^2, 0, 0, h^2, 0, h^2, 0, 0, 0, h^3, 0, h^2, 0, 0, h^3 + h] := by rw [hh3]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  have hh5 : mulσ1 h (mulσ0 h (mulσ2 h (mulσ1 h (mulσ0 h (e (22 : Fin 24)))))) = ![1, h, h, 0, h^2, h^2, 0, 0, 0, h^3 + h, 0, 0, 0, h, 0, 0, h^2, h^2, 0, h^2, h^3, h^3 + h, h^3, h^4 + h^2] := by rw [hh4]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh6 : mulσ0 h (mulσ1 h (mulσ0 h (mulσ2 h (mulσ1 h (mulσ0 h (e (22 : Fin 24))))))) = ![0, 0, 0, 1, 0, 0, h, h, h, 0, h^2, h^2, h^2, h^2, h^2, h^3 + h, h^3, h^3, h^3 + h, h^3, h^4 + h^2, h^4 + h^2, h^4 + h^2, h^5 + 2*h^3] := by rw [hh5]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  rw [hh6]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_23_0 (z h : R) : trM z h (mulNF h (e (23:Fin 24)) (e (0:Fin 24))) = h^3*z^3 + h^2*z^2 + 2*h*z^3 + z^2 := by
  have hmul : mulNF h (e (23:Fin 24)) (e (0:Fin 24)) = e (23 : Fin 24) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (23 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  rw [hh0]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_23_1 (z h : R) : trM z h (mulNF h (e (23:Fin 24)) (e (1:Fin 24))) = h^4*z^3 + h^3*z^2 + 3*h^2*z^3 + 2*h*z^2 + z^3 := by
  have hmul : mulNF h (e (23:Fin 24)) (e (1:Fin 24)) = mulσ2 h (e (23 : Fin 24)) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (23 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ2 h (e (23 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, h] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  rw [hh1]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_23_2 (z h : R) : trM z h (mulNF h (e (23:Fin 24)) (e (2:Fin 24))) = h^4*z^3 + h^3*z^2 + 3*h^2*z^3 + 3*h*z^2 + z := by
  have hmul : mulNF h (e (23:Fin 24)) (e (2:Fin 24)) = mulσ1 h (e (23 : Fin 24)) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (23 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ1 h (e (23 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, h] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  rw [hh1]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_23_3 (z h : R) : trM z h (mulNF h (e (23:Fin 24)) (e (3:Fin 24))) = h^4*z^3 + h^3*z^2 + 3*h^2*z^3 + 2*h*z^2 + z^3 := by
  have hmul : mulNF h (e (23:Fin 24)) (e (3:Fin 24)) = mulσ0 h (e (23 : Fin 24)) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (23 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ0 h (e (23 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, h] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  rw [hh1]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_23_4 (z h : R) : trM z h (mulNF h (e (23:Fin 24)) (e (4:Fin 24))) = h^5*z^3 + h^4*z^2 + 4*h^3*z^3 + 4*h^2*z^2 + 2*h*z^3 + h*z + z^2 := by
  have hmul : mulNF h (e (23:Fin 24)) (e (4:Fin 24)) = mulσ2 h (mulσ1 h (e (23 : Fin 24))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (23 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ1 h (e (23 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, h] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh2 : mulσ2 h (mulσ1 h (e (23 : Fin 24))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, h, h, h^2] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  rw [hh2]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_23_5 (z h : R) : trM z h (mulNF h (e (23:Fin 24)) (e (5:Fin 24))) = h^5*z^3 + h^4*z^2 + 4*h^3*z^3 + 4*h^2*z^2 + 2*h*z^3 + h*z + z^2 := by
  have hmul : mulNF h (e (23:Fin 24)) (e (5:Fin 24)) = mulσ1 h (mulσ2 h (e (23 : Fin 24))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (23 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ2 h (e (23 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, h] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  have hh2 : mulσ1 h (mulσ2 h (e (23 : Fin 24))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, h, h, h^2] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  rw [hh2]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_23_6 (z h : R) : trM z h (mulNF h (e (23:Fin 24)) (e (6:Fin 24))) = h^5*z^3 + h^4*z^2 + 4*h^3*z^3 + 3*h^2*z^2 + 3*h*z^3 + z^2 := by
  have hmul : mulNF h (e (23:Fin 24)) (e (6:Fin 24)) = mulσ0 h (mulσ2 h (e (23 : Fin 24))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (23 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ2 h (e (23 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, h] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  have hh2 : mulσ0 h (mulσ2 h (e (23 : Fin 24))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, h, 0, h, h^2] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  rw [hh2]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_23_7 (z h : R) : trM z h (mulNF h (e (23:Fin 24)) (e (7:Fin 24))) = h^5*z^3 + h^4*z^2 + 4*h^3*z^3 + 4*h^2*z^2 + 2*h*z^3 + h*z + z^2 := by
  have hmul : mulNF h (e (23:Fin 24)) (e (7:Fin 24)) = mulσ1 h (mulσ0 h (e (23 : Fin 24))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (23 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ0 h (e (23 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, h] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  have hh2 : mulσ1 h (mulσ0 h (e (23 : Fin 24))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, h, h, 0, h^2] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  rw [hh2]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_23_8 (z h : R) : trM z h (mulNF h (e (23:Fin 24)) (e (8:Fin 24))) = h^5*z^3 + h^4*z^2 + 4*h^3*z^3 + 4*h^2*z^2 + 2*h*z^3 + h*z + z^2 := by
  have hmul : mulNF h (e (23:Fin 24)) (e (8:Fin 24)) = mulσ0 h (mulσ1 h (e (23 : Fin 24))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (23 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ1 h (e (23 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, h] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh2 : mulσ0 h (mulσ1 h (e (23 : Fin 24))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, h, h, 0, h^2] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  rw [hh2]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_23_9 (z h : R) : trM z h (mulNF h (e (23:Fin 24)) (e (9:Fin 24))) = h^6*z^3 + h^5*z^2 + 5*h^4*z^3 + 5*h^3*z^2 + 5*h^2*z^3 + h^2*z + 3*h*z^2 + z^3 := by
  have hmul : mulNF h (e (23:Fin 24)) (e (9:Fin 24)) = mulσ1 h (mulσ2 h (mulσ1 h (e (23 : Fin 24)))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (23 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ1 h (e (23 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, h] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh2 : mulσ2 h (mulσ1 h (e (23 : Fin 24))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, h, h, h^2] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  have hh3 : mulσ1 h (mulσ2 h (mulσ1 h (e (23 : Fin 24)))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, h, h, 0, h^2, h^2, h^3 + h] := by rw [hh2]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  rw [hh3]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_23_10 (z h : R) : trM z h (mulNF h (e (23:Fin 24)) (e (10:Fin 24))) = h^6*z^3 + h^5*z^2 + 5*h^4*z^3 + 5*h^3*z^2 + 5*h^2*z^3 + h^2*z + 4*h*z^2 + z := by
  have hmul : mulNF h (e (23:Fin 24)) (e (10:Fin 24)) = mulσ2 h (mulσ1 h (mulσ0 h (e (23 : Fin 24)))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (23 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ0 h (e (23 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, h] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  have hh2 : mulσ1 h (mulσ0 h (e (23 : Fin 24))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, h, h, 0, h^2] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh3 : mulσ2 h (mulσ1 h (mulσ0 h (e (23 : Fin 24)))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, h, h, 0, h, h^2, h^2, h^2, h^3] := by rw [hh2]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  rw [hh3]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_23_11 (z h : R) : trM z h (mulNF h (e (23:Fin 24)) (e (11:Fin 24))) = h^6*z^3 + h^5*z^2 + 5*h^4*z^3 + 5*h^3*z^2 + 5*h^2*z^3 + h^2*z + 3*h*z^2 + z^3 := by
  have hmul : mulNF h (e (23:Fin 24)) (e (11:Fin 24)) = mulσ1 h (mulσ0 h (mulσ2 h (e (23 : Fin 24)))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (23 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ2 h (e (23 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, h] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  have hh2 : mulσ0 h (mulσ2 h (e (23 : Fin 24))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, h, 0, h, h^2] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  have hh3 : mulσ1 h (mulσ0 h (mulσ2 h (e (23 : Fin 24)))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, h, h, h, 0, h^2, h^2, h^2, h^3] := by rw [hh2]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  rw [hh3]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_23_12 (z h : R) : trM z h (mulNF h (e (23:Fin 24)) (e (12:Fin 24))) = h^6*z^3 + h^5*z^2 + 5*h^4*z^3 + 5*h^3*z^2 + 5*h^2*z^3 + h^2*z + 3*h*z^2 + z^3 := by
  have hmul : mulNF h (e (23:Fin 24)) (e (12:Fin 24)) = mulσ0 h (mulσ2 h (mulσ1 h (e (23 : Fin 24)))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (23 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ1 h (e (23 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, h] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh2 : mulσ2 h (mulσ1 h (e (23 : Fin 24))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, h, h, h^2] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  have hh3 : mulσ0 h (mulσ2 h (mulσ1 h (e (23 : Fin 24)))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, h, 0, h, 0, h, h^2, h^2, h^2, h^3] := by rw [hh2]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  rw [hh3]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_23_13 (z h : R) : trM z h (mulNF h (e (23:Fin 24)) (e (13:Fin 24))) = h^6*z^3 + h^5*z^2 + 5*h^4*z^3 + 5*h^3*z^2 + 5*h^2*z^3 + h^2*z + 3*h*z^2 + z^3 := by
  have hmul : mulNF h (e (23:Fin 24)) (e (13:Fin 24)) = mulσ0 h (mulσ1 h (mulσ0 h (e (23 : Fin 24)))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (23 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ0 h (e (23 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, h] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  have hh2 : mulσ1 h (mulσ0 h (e (23 : Fin 24))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, h, h, 0, h^2] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh3 : mulσ0 h (mulσ1 h (mulσ0 h (e (23 : Fin 24)))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, h, h, 0, 0, 0, h^2, h^2, 0, h^3 + h] := by rw [hh2]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  rw [hh3]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_23_14 (z h : R) : trM z h (mulNF h (e (23:Fin 24)) (e (14:Fin 24))) = h^6*z^3 + h^5*z^2 + 5*h^4*z^3 + 5*h^3*z^2 + 5*h^2*z^3 + h^2*z + 4*h*z^2 + z := by
  have hmul : mulNF h (e (23:Fin 24)) (e (14:Fin 24)) = mulσ0 h (mulσ1 h (mulσ2 h (e (23 : Fin 24)))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (23 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ2 h (e (23 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, h] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  have hh2 : mulσ1 h (mulσ2 h (e (23 : Fin 24))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, h, h, h^2] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh3 : mulσ0 h (mulσ1 h (mulσ2 h (e (23 : Fin 24)))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, h, 0, h, h, 0, h^2, h^2, h^2, h^3] := by rw [hh2]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  rw [hh3]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_23_15 (z h : R) : trM z h (mulNF h (e (23:Fin 24)) (e (15:Fin 24))) = h^7*z^3 + h^6*z^2 + 6*h^5*z^3 + 6*h^4*z^2 + 9*h^3*z^3 + h^3*z + 7*h^2*z^2 + 3*h*z^3 + h*z + z^2 := by
  have hmul : mulNF h (e (23:Fin 24)) (e (15:Fin 24)) = mulσ1 h (mulσ2 h (mulσ1 h (mulσ0 h (e (23 : Fin 24))))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (23 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ0 h (e (23 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, h] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  have hh2 : mulσ1 h (mulσ0 h (e (23 : Fin 24))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, h, h, 0, h^2] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh3 : mulσ2 h (mulσ1 h (mulσ0 h (e (23 : Fin 24)))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, h, h, 0, h, h^2, h^2, h^2, h^3] := by rw [hh2]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  have hh4 : mulσ1 h (mulσ2 h (mulσ1 h (mulσ0 h (e (23 : Fin 24))))) = ![0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, h, h, h, 0, h^2, h^2, h^2, h^2, h^3 + h, h^3, h^3, h^4 + h^2] := by rw [hh3]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  rw [hh4]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_23_16 (z h : R) : trM z h (mulNF h (e (23:Fin 24)) (e (16:Fin 24))) = h^7*z^3 + h^6*z^2 + 6*h^5*z^3 + 6*h^4*z^2 + 9*h^3*z^3 + h^3*z + 7*h^2*z^2 + 3*h*z^3 + h*z + z^2 := by
  have hmul : mulNF h (e (23:Fin 24)) (e (16:Fin 24)) = mulσ0 h (mulσ2 h (mulσ1 h (mulσ0 h (e (23 : Fin 24))))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (23 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ0 h (e (23 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, h] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  have hh2 : mulσ1 h (mulσ0 h (e (23 : Fin 24))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, h, h, 0, h^2] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh3 : mulσ2 h (mulσ1 h (mulσ0 h (e (23 : Fin 24)))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, h, h, 0, h, h^2, h^2, h^2, h^3] := by rw [hh2]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  have hh4 : mulσ0 h (mulσ2 h (mulσ1 h (mulσ0 h (e (23 : Fin 24))))) = ![0, 0, 0, 0, 0, 0, 0, 1, 0, 0, h, h, 0, h, 0, h^2, h^2, h^2, 0, h^2, h^3, h^3, h^3 + h, h^4 + h^2] := by rw [hh3]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  rw [hh4]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_23_17 (z h : R) : trM z h (mulNF h (e (23:Fin 24)) (e (17:Fin 24))) = h^7*z^3 + h^6*z^2 + 6*h^5*z^3 + 6*h^4*z^2 + 9*h^3*z^3 + h^3*z + 6*h^2*z^2 + 4*h*z^3 + z^2 := by
  have hmul : mulNF h (e (23:Fin 24)) (e (17:Fin 24)) = mulσ1 h (mulσ0 h (mulσ2 h (mulσ1 h (e (23 : Fin 24))))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (23 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ1 h (e (23 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, h] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh2 : mulσ2 h (mulσ1 h (e (23 : Fin 24))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, h, h, h^2] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  have hh3 : mulσ0 h (mulσ2 h (mulσ1 h (e (23 : Fin 24)))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, h, 0, h, 0, h, h^2, h^2, h^2, h^3] := by rw [hh2]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  have hh4 : mulσ1 h (mulσ0 h (mulσ2 h (mulσ1 h (e (23 : Fin 24))))) = ![0, 0, 0, 0, 0, 0, 1, 0, 0, 0, h, h, h, 0, h, h^2, h^2, h^2, h^2, h^2, h^3, h^3, h^3, h^4 + h^2] := by rw [hh3]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  rw [hh4]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_23_18 (z h : R) : trM z h (mulNF h (e (23:Fin 24)) (e (18:Fin 24))) = h^7*z^3 + h^6*z^2 + 6*h^5*z^3 + 6*h^4*z^2 + 9*h^3*z^3 + h^3*z + 7*h^2*z^2 + 3*h*z^3 + h*z + z^2 := by
  have hmul : mulNF h (e (23:Fin 24)) (e (18:Fin 24)) = mulσ0 h (mulσ1 h (mulσ2 h (mulσ1 h (e (23 : Fin 24))))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (23 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ1 h (e (23 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, h] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh2 : mulσ2 h (mulσ1 h (e (23 : Fin 24))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, h, h, h^2] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  have hh3 : mulσ1 h (mulσ2 h (mulσ1 h (e (23 : Fin 24)))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, h, h, 0, h^2, h^2, h^3 + h] := by rw [hh2]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh4 : mulσ0 h (mulσ1 h (mulσ2 h (mulσ1 h (e (23 : Fin 24))))) = ![0, 0, 0, 0, 0, 1, 0, 0, 0, h, 0, h, 0, 0, h, h^2, 0, h^2, h^2, h^2, h^3 + h, h^3, h^3, h^4 + h^2] := by rw [hh3]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  rw [hh4]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_23_19 (z h : R) : trM z h (mulNF h (e (23:Fin 24)) (e (19:Fin 24))) = h^7*z^3 + h^6*z^2 + 6*h^5*z^3 + 6*h^4*z^2 + 9*h^3*z^3 + h^3*z + 7*h^2*z^2 + 3*h*z^3 + h*z + z^2 := by
  have hmul : mulNF h (e (23:Fin 24)) (e (19:Fin 24)) = mulσ0 h (mulσ1 h (mulσ0 h (mulσ2 h (e (23 : Fin 24))))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (23 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ2 h (e (23 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, h] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  have hh2 : mulσ0 h (mulσ2 h (e (23 : Fin 24))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, h, 0, h, h^2] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  have hh3 : mulσ1 h (mulσ0 h (mulσ2 h (e (23 : Fin 24)))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, h, h, h, 0, h^2, h^2, h^2, h^3] := by rw [hh2]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh4 : mulσ0 h (mulσ1 h (mulσ0 h (mulσ2 h (e (23 : Fin 24))))) = ![0, 0, 0, 0, 1, 0, 0, 0, 0, h, h, 0, h, 0, 0, h^2, h^2, h^2, h^2, 0, h^3, h^3, h^3 + h, h^4 + h^2] := by rw [hh3]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  rw [hh4]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_23_20 (z h : R) : trM z h (mulNF h (e (23:Fin 24)) (e (20:Fin 24))) = h^8*z^3 + h^7*z^2 + 7*h^6*z^3 + 7*h^5*z^2 + 14*h^4*z^3 + h^4*z + 12*h^3*z^2 + 8*h^2*z^3 + 2*h^2*z + 5*h*z^2 + z := by
  have hmul : mulNF h (e (23:Fin 24)) (e (20:Fin 24)) = mulσ1 h (mulσ0 h (mulσ2 h (mulσ1 h (mulσ0 h (e (23 : Fin 24)))))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (23 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ0 h (e (23 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, h] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  have hh2 : mulσ1 h (mulσ0 h (e (23 : Fin 24))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, h, h, 0, h^2] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh3 : mulσ2 h (mulσ1 h (mulσ0 h (e (23 : Fin 24)))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, h, h, 0, h, h^2, h^2, h^2, h^3] := by rw [hh2]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  have hh4 : mulσ0 h (mulσ2 h (mulσ1 h (mulσ0 h (e (23 : Fin 24))))) = ![0, 0, 0, 0, 0, 0, 0, 1, 0, 0, h, h, 0, h, 0, h^2, h^2, h^2, 0, h^2, h^3, h^3, h^3 + h, h^4 + h^2] := by rw [hh3]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  have hh5 : mulσ1 h (mulσ0 h (mulσ2 h (mulσ1 h (mulσ0 h (e (23 : Fin 24)))))) = ![0, 0, 0, 1, 0, 0, h, h, h, 0, h^2, h^2, h^2, h^2, h^2, h^3 + h, h^3, h^3, h^3 + h, h^3, h^4 + h^2, h^4 + h^2, h^4 + h^2, h^5 + 2*h^3] := by rw [hh4]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  rw [hh5]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_23_21 (z h : R) : trM z h (mulNF h (e (23:Fin 24)) (e (21:Fin 24))) = h^8*z^3 + h^7*z^2 + 7*h^6*z^3 + 7*h^5*z^2 + 14*h^4*z^3 + h^4*z + 12*h^3*z^2 + 8*h^2*z^3 + 2*h^2*z + 5*h*z^2 + z := by
  have hmul : mulNF h (e (23:Fin 24)) (e (21:Fin 24)) = mulσ0 h (mulσ1 h (mulσ2 h (mulσ1 h (mulσ0 h (e (23 : Fin 24)))))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (23 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ0 h (e (23 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, h] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  have hh2 : mulσ1 h (mulσ0 h (e (23 : Fin 24))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, h, h, 0, h^2] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh3 : mulσ2 h (mulσ1 h (mulσ0 h (e (23 : Fin 24)))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, h, h, 0, h, h^2, h^2, h^2, h^3] := by rw [hh2]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  have hh4 : mulσ1 h (mulσ2 h (mulσ1 h (mulσ0 h (e (23 : Fin 24))))) = ![0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, h, h, h, 0, h^2, h^2, h^2, h^2, h^3 + h, h^3, h^3, h^4 + h^2] := by rw [hh3]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh5 : mulσ0 h (mulσ1 h (mulσ2 h (mulσ1 h (mulσ0 h (e (23 : Fin 24)))))) = ![0, 0, 1, 0, h, h, 0, h, h, h^2, h^2, h^2, h^2, h^2, h^2, h^3, h^3, h^3, h^3, h^3, h^4 + h^2, h^4, h^4 + h^2, h^5 + 2*h^3 + h] := by rw [hh4]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  rw [hh5]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_23_22 (z h : R) : trM z h (mulNF h (e (23:Fin 24)) (e (22:Fin 24))) = h^8*z^3 + h^7*z^2 + 7*h^6*z^3 + 7*h^5*z^2 + 14*h^4*z^3 + h^4*z + 12*h^3*z^2 + 8*h^2*z^3 + 2*h^2*z + 5*h*z^2 + z := by
  have hmul : mulNF h (e (23:Fin 24)) (e (22:Fin 24)) = mulσ0 h (mulσ1 h (mulσ0 h (mulσ2 h (mulσ1 h (e (23 : Fin 24)))))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (23 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ1 h (e (23 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, h] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh2 : mulσ2 h (mulσ1 h (e (23 : Fin 24))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, h, h, h^2] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  have hh3 : mulσ0 h (mulσ2 h (mulσ1 h (e (23 : Fin 24)))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, h, 0, h, 0, h, h^2, h^2, h^2, h^3] := by rw [hh2]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  have hh4 : mulσ1 h (mulσ0 h (mulσ2 h (mulσ1 h (e (23 : Fin 24))))) = ![0, 0, 0, 0, 0, 0, 1, 0, 0, 0, h, h, h, 0, h, h^2, h^2, h^2, h^2, h^2, h^3, h^3, h^3, h^4 + h^2] := by rw [hh3]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh5 : mulσ0 h (mulσ1 h (mulσ0 h (mulσ2 h (mulσ1 h (e (23 : Fin 24)))))) = ![0, 1, 0, 0, h, h, h, 0, 0, h^2, h^2, h^2, h^2, 0, h^2, h^3, h^3 + h, h^3, h^3, h^3 + h, h^4 + h^2, h^4 + h^2, h^4 + h^2, h^5 + 2*h^3] := by rw [hh4]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  rw [hh5]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_23_23 (z h : R) : trM z h (mulNF h (e (23:Fin 24)) (e (23:Fin 24))) = h^9*z^3 + h^8*z^2 + 8*h^7*z^3 + 8*h^6*z^2 + 20*h^5*z^3 + h^5*z + 19*h^4*z^2 + 16*h^3*z^3 + 4*h^3*z + 15*h^2*z^2 + 6*h*z + 1 := by
  have hmul : mulNF h (e (23:Fin 24)) (e (23:Fin 24)) = mulσ0 h (mulσ1 h (mulσ0 h (mulσ2 h (mulσ1 h (mulσ0 h (e (23 : Fin 24))))))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (23 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ0 h (e (23 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, h] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  have hh2 : mulσ1 h (mulσ0 h (e (23 : Fin 24))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, h, h, 0, h^2] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh3 : mulσ2 h (mulσ1 h (mulσ0 h (e (23 : Fin 24)))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, h, h, 0, h, h^2, h^2, h^2, h^3] := by rw [hh2]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  have hh4 : mulσ0 h (mulσ2 h (mulσ1 h (mulσ0 h (e (23 : Fin 24))))) = ![0, 0, 0, 0, 0, 0, 0, 1, 0, 0, h, h, 0, h, 0, h^2, h^2, h^2, 0, h^2, h^3, h^3, h^3 + h, h^4 + h^2] := by rw [hh3]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  have hh5 : mulσ1 h (mulσ0 h (mulσ2 h (mulσ1 h (mulσ0 h (e (23 : Fin 24)))))) = ![0, 0, 0, 1, 0, 0, h, h, h, 0, h^2, h^2, h^2, h^2, h^2, h^3 + h, h^3, h^3, h^3 + h, h^3, h^4 + h^2, h^4 + h^2, h^4 + h^2, h^5 + 2*h^3] := by rw [hh4]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh6 : mulσ0 h (mulσ1 h (mulσ0 h (mulσ2 h (mulσ1 h (mulσ0 h (e (23 : Fin 24))))))) = ![1, h, h, h, h^2, h^2, h^2, h^2, h^2, h^3 + h, h^3, h^3, h^3, h^3 + h, h^3, h^4 + h^2, h^4 + h^2, h^4 + h^2, h^4 + h^2, h^4 + h^2, h^5 + 2*h^3, h^5 + 2*h^3 + h, h^5 + 2*h^3, h^6 + 3*h^4 + h^2] := by rw [hh5]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  rw [hh6]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

end QOU.Machinery.H4
