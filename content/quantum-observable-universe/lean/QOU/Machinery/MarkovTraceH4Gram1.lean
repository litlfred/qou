import QOU.Machinery.MarkovTraceH4Gram0

/-!
# QOU.Machinery.H4 Gram closure — part 1 of 8

Auto-generated Gram entries `G_(i,j) = tr_M(b_i * b_j)`, emitted by
`computations/markov/gen_gram_closure.py`.

Split across 8 modules, each importing the previous, so the chain is
built serially and peak elaboration memory stays bounded. Held as ONE module the
closure needs ~15 GB and over an hour (bean qou-8hjy); the split is a pure
refactor — same theorems, same proofs, same namespace.
-/

namespace QOU.Machinery.H4

variable {R : Type*} [CommRing R]

theorem gramval_3_0 (z h : R) : trM z h (mulNF h (e (3:Fin 24)) (e (0:Fin 24))) = z := by
  have hmul : mulNF h (e (3:Fin 24)) (e (0:Fin 24)) = e (3 : Fin 24) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (3 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  rw [hh0]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_3_1 (z h : R) : trM z h (mulNF h (e (3:Fin 24)) (e (1:Fin 24))) = z^2 := by
  have hmul : mulNF h (e (3:Fin 24)) (e (1:Fin 24)) = mulσ2 h (e (3 : Fin 24)) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (3 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ2 h (e (3 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  rw [hh1]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_3_2 (z h : R) : trM z h (mulNF h (e (3:Fin 24)) (e (2:Fin 24))) = z^2 := by
  have hmul : mulNF h (e (3:Fin 24)) (e (2:Fin 24)) = mulσ1 h (e (3 : Fin 24)) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (3 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ1 h (e (3 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  rw [hh1]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_3_3 (z h : R) : trM z h (mulNF h (e (3:Fin 24)) (e (3:Fin 24))) = h*z + 1 := by
  have hmul : mulNF h (e (3:Fin 24)) (e (3:Fin 24)) = mulσ0 h (e (3 : Fin 24)) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (3 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ0 h (e (3 : Fin 24)) = ![1, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  rw [hh1]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_3_4 (z h : R) : trM z h (mulNF h (e (3:Fin 24)) (e (4:Fin 24))) = z^3 := by
  have hmul : mulNF h (e (3:Fin 24)) (e (4:Fin 24)) = mulσ2 h (mulσ1 h (e (3 : Fin 24))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (3 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ1 h (e (3 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh2 : mulσ2 h (mulσ1 h (e (3 : Fin 24))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  rw [hh2]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_3_5 (z h : R) : trM z h (mulNF h (e (3:Fin 24)) (e (5:Fin 24))) = z^3 := by
  have hmul : mulNF h (e (3:Fin 24)) (e (5:Fin 24)) = mulσ1 h (mulσ2 h (e (3 : Fin 24))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (3 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ2 h (e (3 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  have hh2 : mulσ1 h (mulσ2 h (e (3 : Fin 24))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  rw [hh2]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_3_6 (z h : R) : trM z h (mulNF h (e (3:Fin 24)) (e (6:Fin 24))) = h*z^2 + z := by
  have hmul : mulNF h (e (3:Fin 24)) (e (6:Fin 24)) = mulσ0 h (mulσ2 h (e (3 : Fin 24))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (3 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ2 h (e (3 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  have hh2 : mulσ0 h (mulσ2 h (e (3 : Fin 24))) = ![0, 1, 0, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  rw [hh2]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_3_7 (z h : R) : trM z h (mulNF h (e (3:Fin 24)) (e (7:Fin 24))) = h*z^2 + z := by
  have hmul : mulNF h (e (3:Fin 24)) (e (7:Fin 24)) = mulσ1 h (mulσ0 h (e (3 : Fin 24))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (3 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ0 h (e (3 : Fin 24)) = ![1, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  have hh2 : mulσ1 h (mulσ0 h (e (3 : Fin 24))) = ![0, 0, 1, 0, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  rw [hh2]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_3_8 (z h : R) : trM z h (mulNF h (e (3:Fin 24)) (e (8:Fin 24))) = h*z^2 + z := by
  have hmul : mulNF h (e (3:Fin 24)) (e (8:Fin 24)) = mulσ0 h (mulσ1 h (e (3 : Fin 24))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (3 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ1 h (e (3 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh2 : mulσ0 h (mulσ1 h (e (3 : Fin 24))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  rw [hh2]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_3_9 (z h : R) : trM z h (mulNF h (e (3:Fin 24)) (e (9:Fin 24))) = h*z^3 + z^2 := by
  have hmul : mulNF h (e (3:Fin 24)) (e (9:Fin 24)) = mulσ1 h (mulσ2 h (mulσ1 h (e (3 : Fin 24)))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (3 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ1 h (e (3 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh2 : mulσ2 h (mulσ1 h (e (3 : Fin 24))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  have hh3 : mulσ1 h (mulσ2 h (mulσ1 h (e (3 : Fin 24)))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh2]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  rw [hh3]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_3_10 (z h : R) : trM z h (mulNF h (e (3:Fin 24)) (e (10:Fin 24))) = h*z^3 + z^2 := by
  have hmul : mulNF h (e (3:Fin 24)) (e (10:Fin 24)) = mulσ2 h (mulσ1 h (mulσ0 h (e (3 : Fin 24)))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (3 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ0 h (e (3 : Fin 24)) = ![1, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  have hh2 : mulσ1 h (mulσ0 h (e (3 : Fin 24))) = ![0, 0, 1, 0, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh3 : mulσ2 h (mulσ1 h (mulσ0 h (e (3 : Fin 24)))) = ![0, 0, 0, 0, 1, 0, 0, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh2]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  rw [hh3]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_3_11 (z h : R) : trM z h (mulNF h (e (3:Fin 24)) (e (11:Fin 24))) = h*z^3 + z^2 := by
  have hmul : mulNF h (e (3:Fin 24)) (e (11:Fin 24)) = mulσ1 h (mulσ0 h (mulσ2 h (e (3 : Fin 24)))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (3 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ2 h (e (3 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  have hh2 : mulσ0 h (mulσ2 h (e (3 : Fin 24))) = ![0, 1, 0, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  have hh3 : mulσ1 h (mulσ0 h (mulσ2 h (e (3 : Fin 24)))) = ![0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh2]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  rw [hh3]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_3_12 (z h : R) : trM z h (mulNF h (e (3:Fin 24)) (e (12:Fin 24))) = h*z^3 + z^2 := by
  have hmul : mulNF h (e (3:Fin 24)) (e (12:Fin 24)) = mulσ0 h (mulσ2 h (mulσ1 h (e (3 : Fin 24)))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (3 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ1 h (e (3 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh2 : mulσ2 h (mulσ1 h (e (3 : Fin 24))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  have hh3 : mulσ0 h (mulσ2 h (mulσ1 h (e (3 : Fin 24)))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0] := by rw [hh2]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  rw [hh3]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_3_13 (z h : R) : trM z h (mulNF h (e (3:Fin 24)) (e (13:Fin 24))) = h^2*z^2 + h*z + z^2 := by
  have hmul : mulNF h (e (3:Fin 24)) (e (13:Fin 24)) = mulσ0 h (mulσ1 h (mulσ0 h (e (3 : Fin 24)))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (3 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ0 h (e (3 : Fin 24)) = ![1, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  have hh2 : mulσ1 h (mulσ0 h (e (3 : Fin 24))) = ![0, 0, 1, 0, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh3 : mulσ0 h (mulσ1 h (mulσ0 h (e (3 : Fin 24)))) = ![0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh2]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  rw [hh3]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_3_14 (z h : R) : trM z h (mulNF h (e (3:Fin 24)) (e (14:Fin 24))) = h*z^3 + z^2 := by
  have hmul : mulNF h (e (3:Fin 24)) (e (14:Fin 24)) = mulσ0 h (mulσ1 h (mulσ2 h (e (3 : Fin 24)))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (3 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ2 h (e (3 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  have hh2 : mulσ1 h (mulσ2 h (e (3 : Fin 24))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh3 : mulσ0 h (mulσ1 h (mulσ2 h (e (3 : Fin 24)))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0] := by rw [hh2]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  rw [hh3]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_3_15 (z h : R) : trM z h (mulNF h (e (3:Fin 24)) (e (15:Fin 24))) = h^2*z^3 + 2*h*z^2 + z := by
  have hmul : mulNF h (e (3:Fin 24)) (e (15:Fin 24)) = mulσ1 h (mulσ2 h (mulσ1 h (mulσ0 h (e (3 : Fin 24))))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (3 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ0 h (e (3 : Fin 24)) = ![1, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  have hh2 : mulσ1 h (mulσ0 h (e (3 : Fin 24))) = ![0, 0, 1, 0, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh3 : mulσ2 h (mulσ1 h (mulσ0 h (e (3 : Fin 24)))) = ![0, 0, 0, 0, 1, 0, 0, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh2]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  have hh4 : mulσ1 h (mulσ2 h (mulσ1 h (mulσ0 h (e (3 : Fin 24))))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh3]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  rw [hh4]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_3_16 (z h : R) : trM z h (mulNF h (e (3:Fin 24)) (e (16:Fin 24))) = h^2*z^3 + h*z^2 + z^3 := by
  have hmul : mulNF h (e (3:Fin 24)) (e (16:Fin 24)) = mulσ0 h (mulσ2 h (mulσ1 h (mulσ0 h (e (3 : Fin 24))))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (3 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ0 h (e (3 : Fin 24)) = ![1, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  have hh2 : mulσ1 h (mulσ0 h (e (3 : Fin 24))) = ![0, 0, 1, 0, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh3 : mulσ2 h (mulσ1 h (mulσ0 h (e (3 : Fin 24)))) = ![0, 0, 0, 0, 1, 0, 0, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh2]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  have hh4 : mulσ0 h (mulσ2 h (mulσ1 h (mulσ0 h (e (3 : Fin 24))))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0] := by rw [hh3]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  rw [hh4]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_3_17 (z h : R) : trM z h (mulNF h (e (3:Fin 24)) (e (17:Fin 24))) = h^2*z^3 + h*z^2 + z^3 := by
  have hmul : mulNF h (e (3:Fin 24)) (e (17:Fin 24)) = mulσ1 h (mulσ0 h (mulσ2 h (mulσ1 h (e (3 : Fin 24))))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (3 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ1 h (e (3 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh2 : mulσ2 h (mulσ1 h (e (3 : Fin 24))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  have hh3 : mulσ0 h (mulσ2 h (mulσ1 h (e (3 : Fin 24)))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0] := by rw [hh2]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  have hh4 : mulσ1 h (mulσ0 h (mulσ2 h (mulσ1 h (e (3 : Fin 24))))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0] := by rw [hh3]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  rw [hh4]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_3_18 (z h : R) : trM z h (mulNF h (e (3:Fin 24)) (e (18:Fin 24))) = h^2*z^3 + 2*h*z^2 + z := by
  have hmul : mulNF h (e (3:Fin 24)) (e (18:Fin 24)) = mulσ0 h (mulσ1 h (mulσ2 h (mulσ1 h (e (3 : Fin 24))))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (3 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ1 h (e (3 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh2 : mulσ2 h (mulσ1 h (e (3 : Fin 24))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  have hh3 : mulσ1 h (mulσ2 h (mulσ1 h (e (3 : Fin 24)))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh2]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh4 : mulσ0 h (mulσ1 h (mulσ2 h (mulσ1 h (e (3 : Fin 24))))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0] := by rw [hh3]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  rw [hh4]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_3_19 (z h : R) : trM z h (mulNF h (e (3:Fin 24)) (e (19:Fin 24))) = h^2*z^3 + h*z^2 + z^3 := by
  have hmul : mulNF h (e (3:Fin 24)) (e (19:Fin 24)) = mulσ0 h (mulσ1 h (mulσ0 h (mulσ2 h (e (3 : Fin 24))))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (3 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ2 h (e (3 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  have hh2 : mulσ0 h (mulσ2 h (e (3 : Fin 24))) = ![0, 1, 0, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  have hh3 : mulσ1 h (mulσ0 h (mulσ2 h (e (3 : Fin 24)))) = ![0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh2]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh4 : mulσ0 h (mulσ1 h (mulσ0 h (mulσ2 h (e (3 : Fin 24))))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, h, 0, 0, 0, 0] := by rw [hh3]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  rw [hh4]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_3_20 (z h : R) : trM z h (mulNF h (e (3:Fin 24)) (e (20:Fin 24))) = h^3*z^3 + h^2*z^2 + 2*h*z^3 + z^2 := by
  have hmul : mulNF h (e (3:Fin 24)) (e (20:Fin 24)) = mulσ1 h (mulσ0 h (mulσ2 h (mulσ1 h (mulσ0 h (e (3 : Fin 24)))))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (3 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ0 h (e (3 : Fin 24)) = ![1, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  have hh2 : mulσ1 h (mulσ0 h (e (3 : Fin 24))) = ![0, 0, 1, 0, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh3 : mulσ2 h (mulσ1 h (mulσ0 h (e (3 : Fin 24)))) = ![0, 0, 0, 0, 1, 0, 0, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh2]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  have hh4 : mulσ0 h (mulσ2 h (mulσ1 h (mulσ0 h (e (3 : Fin 24))))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0] := by rw [hh3]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  have hh5 : mulσ1 h (mulσ0 h (mulσ2 h (mulσ1 h (mulσ0 h (e (3 : Fin 24)))))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, h, 0, 0, 0] := by rw [hh4]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  rw [hh5]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_3_21 (z h : R) : trM z h (mulNF h (e (3:Fin 24)) (e (21:Fin 24))) = h^3*z^3 + 2*h^2*z^2 + h*z^3 + h*z + z^2 := by
  have hmul : mulNF h (e (3:Fin 24)) (e (21:Fin 24)) = mulσ0 h (mulσ1 h (mulσ2 h (mulσ1 h (mulσ0 h (e (3 : Fin 24)))))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (3 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ0 h (e (3 : Fin 24)) = ![1, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  have hh2 : mulσ1 h (mulσ0 h (e (3 : Fin 24))) = ![0, 0, 1, 0, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh3 : mulσ2 h (mulσ1 h (mulσ0 h (e (3 : Fin 24)))) = ![0, 0, 0, 0, 1, 0, 0, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh2]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  have hh4 : mulσ1 h (mulσ2 h (mulσ1 h (mulσ0 h (e (3 : Fin 24))))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh3]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh5 : mulσ0 h (mulσ1 h (mulσ2 h (mulσ1 h (mulσ0 h (e (3 : Fin 24)))))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, h, 0, 0] := by rw [hh4]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  rw [hh5]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_3_22 (z h : R) : trM z h (mulNF h (e (3:Fin 24)) (e (22:Fin 24))) = h^3*z^3 + h^2*z^2 + 2*h*z^3 + z^2 := by
  have hmul : mulNF h (e (3:Fin 24)) (e (22:Fin 24)) = mulσ0 h (mulσ1 h (mulσ0 h (mulσ2 h (mulσ1 h (e (3 : Fin 24)))))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (3 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ1 h (e (3 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh2 : mulσ2 h (mulσ1 h (e (3 : Fin 24))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  have hh3 : mulσ0 h (mulσ2 h (mulσ1 h (e (3 : Fin 24)))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0] := by rw [hh2]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  have hh4 : mulσ1 h (mulσ0 h (mulσ2 h (mulσ1 h (e (3 : Fin 24))))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0] := by rw [hh3]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh5 : mulσ0 h (mulσ1 h (mulσ0 h (mulσ2 h (mulσ1 h (e (3 : Fin 24)))))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1] := by rw [hh4]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  rw [hh5]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_3_23 (z h : R) : trM z h (mulNF h (e (3:Fin 24)) (e (23:Fin 24))) = h^4*z^3 + h^3*z^2 + 3*h^2*z^3 + 2*h*z^2 + z^3 := by
  have hmul : mulNF h (e (3:Fin 24)) (e (23:Fin 24)) = mulσ0 h (mulσ1 h (mulσ0 h (mulσ2 h (mulσ1 h (mulσ0 h (e (3 : Fin 24))))))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (3 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ0 h (e (3 : Fin 24)) = ![1, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  have hh2 : mulσ1 h (mulσ0 h (e (3 : Fin 24))) = ![0, 0, 1, 0, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh3 : mulσ2 h (mulσ1 h (mulσ0 h (e (3 : Fin 24)))) = ![0, 0, 0, 0, 1, 0, 0, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh2]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  have hh4 : mulσ0 h (mulσ2 h (mulσ1 h (mulσ0 h (e (3 : Fin 24))))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0] := by rw [hh3]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  have hh5 : mulσ1 h (mulσ0 h (mulσ2 h (mulσ1 h (mulσ0 h (e (3 : Fin 24)))))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, h, 0, 0, 0] := by rw [hh4]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh6 : mulσ0 h (mulσ1 h (mulσ0 h (mulσ2 h (mulσ1 h (mulσ0 h (e (3 : Fin 24))))))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, h] := by rw [hh5]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  rw [hh6]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_4_0 (z h : R) : trM z h (mulNF h (e (4:Fin 24)) (e (0:Fin 24))) = z^2 := by
  have hmul : mulNF h (e (4:Fin 24)) (e (0:Fin 24)) = e (4 : Fin 24) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (4 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  rw [hh0]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_4_1 (z h : R) : trM z h (mulNF h (e (4:Fin 24)) (e (1:Fin 24))) = h*z^2 + z := by
  have hmul : mulNF h (e (4:Fin 24)) (e (1:Fin 24)) = mulσ2 h (e (4 : Fin 24)) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (4 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ2 h (e (4 : Fin 24)) = ![0, 0, 1, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  rw [hh1]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_4_2 (z h : R) : trM z h (mulNF h (e (4:Fin 24)) (e (2:Fin 24))) = h*z^2 + z := by
  have hmul : mulNF h (e (4:Fin 24)) (e (2:Fin 24)) = mulσ1 h (e (4 : Fin 24)) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (4 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ1 h (e (4 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  rw [hh1]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_4_3 (z h : R) : trM z h (mulNF h (e (4:Fin 24)) (e (3:Fin 24))) = z^3 := by
  have hmul : mulNF h (e (4:Fin 24)) (e (3:Fin 24)) = mulσ0 h (e (4 : Fin 24)) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (4 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ0 h (e (4 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  rw [hh1]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_4_4 (z h : R) : trM z h (mulNF h (e (4:Fin 24)) (e (4:Fin 24))) = h^2*z^2 + h*z + z^2 := by
  have hmul : mulNF h (e (4:Fin 24)) (e (4:Fin 24)) = mulσ2 h (mulσ1 h (e (4 : Fin 24))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (4 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ1 h (e (4 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh2 : mulσ2 h (mulσ1 h (e (4 : Fin 24))) = ![0, 0, 0, 0, 0, 1, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  rw [hh2]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_4_5 (z h : R) : trM z h (mulNF h (e (4:Fin 24)) (e (5:Fin 24))) = h^2*z^2 + 2*h*z + 1 := by
  have hmul : mulNF h (e (4:Fin 24)) (e (5:Fin 24)) = mulσ1 h (mulσ2 h (e (4 : Fin 24))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (4 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ2 h (e (4 : Fin 24)) = ![0, 0, 1, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  have hh2 : mulσ1 h (mulσ2 h (e (4 : Fin 24))) = ![1, 0, h, 0, 0, 0, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  rw [hh2]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_4_6 (z h : R) : trM z h (mulNF h (e (4:Fin 24)) (e (6:Fin 24))) = h*z^3 + z^2 := by
  have hmul : mulNF h (e (4:Fin 24)) (e (6:Fin 24)) = mulσ0 h (mulσ2 h (e (4 : Fin 24))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (4 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ2 h (e (4 : Fin 24)) = ![0, 0, 1, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  have hh2 : mulσ0 h (mulσ2 h (e (4 : Fin 24))) = ![0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  rw [hh2]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_4_7 (z h : R) : trM z h (mulNF h (e (4:Fin 24)) (e (7:Fin 24))) = h*z^3 + z^2 := by
  have hmul : mulNF h (e (4:Fin 24)) (e (7:Fin 24)) = mulσ1 h (mulσ0 h (e (4 : Fin 24))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (4 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ0 h (e (4 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  have hh2 : mulσ1 h (mulσ0 h (e (4 : Fin 24))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  rw [hh2]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_4_8 (z h : R) : trM z h (mulNF h (e (4:Fin 24)) (e (8:Fin 24))) = h*z^3 + z^2 := by
  have hmul : mulNF h (e (4:Fin 24)) (e (8:Fin 24)) = mulσ0 h (mulσ1 h (e (4 : Fin 24))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (4 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ1 h (e (4 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh2 : mulσ0 h (mulσ1 h (e (4 : Fin 24))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  rw [hh2]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_4_9 (z h : R) : trM z h (mulNF h (e (4:Fin 24)) (e (9:Fin 24))) = h^3*z^2 + h^2*z + 2*h*z^2 + z := by
  have hmul : mulNF h (e (4:Fin 24)) (e (9:Fin 24)) = mulσ1 h (mulσ2 h (mulσ1 h (e (4 : Fin 24)))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (4 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ1 h (e (4 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh2 : mulσ2 h (mulσ1 h (e (4 : Fin 24))) = ![0, 0, 0, 0, 0, 1, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  have hh3 : mulσ1 h (mulσ2 h (mulσ1 h (e (4 : Fin 24)))) = ![0, 1, 0, 0, h, h, 0, 0, 0, h^2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh2]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  rw [hh3]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_4_10 (z h : R) : trM z h (mulNF h (e (4:Fin 24)) (e (10:Fin 24))) = h^2*z^3 + h*z^2 + z^3 := by
  have hmul : mulNF h (e (4:Fin 24)) (e (10:Fin 24)) = mulσ2 h (mulσ1 h (mulσ0 h (e (4 : Fin 24)))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (4 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ0 h (e (4 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  have hh2 : mulσ1 h (mulσ0 h (e (4 : Fin 24))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh3 : mulσ2 h (mulσ1 h (mulσ0 h (e (4 : Fin 24)))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0] := by rw [hh2]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  rw [hh3]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_4_11 (z h : R) : trM z h (mulNF h (e (4:Fin 24)) (e (11:Fin 24))) = h^2*z^3 + 2*h*z^2 + z := by
  have hmul : mulNF h (e (4:Fin 24)) (e (11:Fin 24)) = mulσ1 h (mulσ0 h (mulσ2 h (e (4 : Fin 24)))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (4 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ2 h (e (4 : Fin 24)) = ![0, 0, 1, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  have hh2 : mulσ0 h (mulσ2 h (e (4 : Fin 24))) = ![0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  have hh3 : mulσ1 h (mulσ0 h (mulσ2 h (e (4 : Fin 24)))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, h, 0, 0, 0, 0, 0, 0] := by rw [hh2]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  rw [hh3]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_4_12 (z h : R) : trM z h (mulNF h (e (4:Fin 24)) (e (12:Fin 24))) = h^2*z^3 + h*z^2 + z^3 := by
  have hmul : mulNF h (e (4:Fin 24)) (e (12:Fin 24)) = mulσ0 h (mulσ2 h (mulσ1 h (e (4 : Fin 24)))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (4 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ1 h (e (4 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh2 : mulσ2 h (mulσ1 h (e (4 : Fin 24))) = ![0, 0, 0, 0, 0, 1, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  have hh3 : mulσ0 h (mulσ2 h (mulσ1 h (e (4 : Fin 24)))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, h, 0, 0, 0, 0, 0] := by rw [hh2]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  rw [hh3]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_4_13 (z h : R) : trM z h (mulNF h (e (4:Fin 24)) (e (13:Fin 24))) = h^2*z^3 + h*z^2 + z^3 := by
  have hmul : mulNF h (e (4:Fin 24)) (e (13:Fin 24)) = mulσ0 h (mulσ1 h (mulσ0 h (e (4 : Fin 24)))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (4 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ0 h (e (4 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  have hh2 : mulσ1 h (mulσ0 h (e (4 : Fin 24))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh3 : mulσ0 h (mulσ1 h (mulσ0 h (e (4 : Fin 24)))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0] := by rw [hh2]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  rw [hh3]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_4_14 (z h : R) : trM z h (mulNF h (e (4:Fin 24)) (e (14:Fin 24))) = h^2*z^3 + 2*h*z^2 + z := by
  have hmul : mulNF h (e (4:Fin 24)) (e (14:Fin 24)) = mulσ0 h (mulσ1 h (mulσ2 h (e (4 : Fin 24)))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (4 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ2 h (e (4 : Fin 24)) = ![0, 0, 1, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  have hh2 : mulσ1 h (mulσ2 h (e (4 : Fin 24))) = ![1, 0, h, 0, 0, 0, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh3 : mulσ0 h (mulσ1 h (mulσ2 h (e (4 : Fin 24)))) = ![0, 0, 0, 1, 0, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, h, 0, 0, 0, 0, 0] := by rw [hh2]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  rw [hh3]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_4_15 (z h : R) : trM z h (mulNF h (e (4:Fin 24)) (e (15:Fin 24))) = h^3*z^3 + h^2*z^2 + 2*h*z^3 + z^2 := by
  have hmul : mulNF h (e (4:Fin 24)) (e (15:Fin 24)) = mulσ1 h (mulσ2 h (mulσ1 h (mulσ0 h (e (4 : Fin 24))))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (4 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ0 h (e (4 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  have hh2 : mulσ1 h (mulσ0 h (e (4 : Fin 24))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh3 : mulσ2 h (mulσ1 h (mulσ0 h (e (4 : Fin 24)))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0] := by rw [hh2]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  have hh4 : mulσ1 h (mulσ2 h (mulσ1 h (mulσ0 h (e (4 : Fin 24))))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, h, 0, 0, 0] := by rw [hh3]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  rw [hh4]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_4_16 (z h : R) : trM z h (mulNF h (e (4:Fin 24)) (e (16:Fin 24))) = h^3*z^3 + h^2*z^2 + 2*h*z^3 + z^2 := by
  have hmul : mulNF h (e (4:Fin 24)) (e (16:Fin 24)) = mulσ0 h (mulσ2 h (mulσ1 h (mulσ0 h (e (4 : Fin 24))))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (4 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ0 h (e (4 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  have hh2 : mulσ1 h (mulσ0 h (e (4 : Fin 24))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh3 : mulσ2 h (mulσ1 h (mulσ0 h (e (4 : Fin 24)))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0] := by rw [hh2]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  have hh4 : mulσ0 h (mulσ2 h (mulσ1 h (mulσ0 h (e (4 : Fin 24))))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1] := by rw [hh3]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  rw [hh4]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_4_17 (z h : R) : trM z h (mulNF h (e (4:Fin 24)) (e (17:Fin 24))) = h^3*z^3 + h^2*z^2 + 2*h*z^3 + z^2 := by
  have hmul : mulNF h (e (4:Fin 24)) (e (17:Fin 24)) = mulσ1 h (mulσ0 h (mulσ2 h (mulσ1 h (e (4 : Fin 24))))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (4 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ1 h (e (4 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh2 : mulσ2 h (mulσ1 h (e (4 : Fin 24))) = ![0, 0, 0, 0, 0, 1, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  have hh3 : mulσ0 h (mulσ2 h (mulσ1 h (e (4 : Fin 24)))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, h, 0, 0, 0, 0, 0] := by rw [hh2]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  have hh4 : mulσ1 h (mulσ0 h (mulσ2 h (mulσ1 h (e (4 : Fin 24))))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, h, 0] := by rw [hh3]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  rw [hh4]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_4_18 (z h : R) : trM z h (mulNF h (e (4:Fin 24)) (e (18:Fin 24))) = h^3*z^3 + h^2*z^2 + 2*h*z^3 + z^2 := by
  have hmul : mulNF h (e (4:Fin 24)) (e (18:Fin 24)) = mulσ0 h (mulσ1 h (mulσ2 h (mulσ1 h (e (4 : Fin 24))))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (4 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ1 h (e (4 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh2 : mulσ2 h (mulσ1 h (e (4 : Fin 24))) = ![0, 0, 0, 0, 0, 1, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  have hh3 : mulσ1 h (mulσ2 h (mulσ1 h (e (4 : Fin 24)))) = ![0, 1, 0, 0, h, h, 0, 0, 0, h^2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh2]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh4 : mulσ0 h (mulσ1 h (mulσ2 h (mulσ1 h (e (4 : Fin 24))))) = ![0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, h, 0, h, 0, 0, 0, h^2, 0, 0, 0, 0, 0] := by rw [hh3]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  rw [hh4]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_4_19 (z h : R) : trM z h (mulNF h (e (4:Fin 24)) (e (19:Fin 24))) = h^3*z^3 + 2*h^2*z^2 + h*z^3 + h*z + z^2 := by
  have hmul : mulNF h (e (4:Fin 24)) (e (19:Fin 24)) = mulσ0 h (mulσ1 h (mulσ0 h (mulσ2 h (e (4 : Fin 24))))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (4 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ2 h (e (4 : Fin 24)) = ![0, 0, 1, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  have hh2 : mulσ0 h (mulσ2 h (e (4 : Fin 24))) = ![0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  have hh3 : mulσ1 h (mulσ0 h (mulσ2 h (e (4 : Fin 24)))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, h, 0, 0, 0, 0, 0, 0] := by rw [hh2]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh4 : mulσ0 h (mulσ1 h (mulσ0 h (mulσ2 h (e (4 : Fin 24))))) = ![0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, h, 0] := by rw [hh3]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  rw [hh4]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_4_20 (z h : R) : trM z h (mulNF h (e (4:Fin 24)) (e (20:Fin 24))) = h^4*z^3 + h^3*z^2 + 3*h^2*z^3 + 3*h*z^2 + z := by
  have hmul : mulNF h (e (4:Fin 24)) (e (20:Fin 24)) = mulσ1 h (mulσ0 h (mulσ2 h (mulσ1 h (mulσ0 h (e (4 : Fin 24)))))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (4 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ0 h (e (4 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  have hh2 : mulσ1 h (mulσ0 h (e (4 : Fin 24))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh3 : mulσ2 h (mulσ1 h (mulσ0 h (e (4 : Fin 24)))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0] := by rw [hh2]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  have hh4 : mulσ0 h (mulσ2 h (mulσ1 h (mulσ0 h (e (4 : Fin 24))))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1] := by rw [hh3]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  have hh5 : mulσ1 h (mulσ0 h (mulσ2 h (mulσ1 h (mulσ0 h (e (4 : Fin 24)))))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, h] := by rw [hh4]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  rw [hh5]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_4_21 (z h : R) : trM z h (mulNF h (e (4:Fin 24)) (e (21:Fin 24))) = h^4*z^3 + h^3*z^2 + 3*h^2*z^3 + 2*h*z^2 + z^3 := by
  have hmul : mulNF h (e (4:Fin 24)) (e (21:Fin 24)) = mulσ0 h (mulσ1 h (mulσ2 h (mulσ1 h (mulσ0 h (e (4 : Fin 24)))))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (4 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ0 h (e (4 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  have hh2 : mulσ1 h (mulσ0 h (e (4 : Fin 24))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh3 : mulσ2 h (mulσ1 h (mulσ0 h (e (4 : Fin 24)))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0] := by rw [hh2]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  have hh4 : mulσ1 h (mulσ2 h (mulσ1 h (mulσ0 h (e (4 : Fin 24))))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, h, 0, 0, 0] := by rw [hh3]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh5 : mulσ0 h (mulσ1 h (mulσ2 h (mulσ1 h (mulσ0 h (e (4 : Fin 24)))))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, h] := by rw [hh4]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  rw [hh5]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_4_22 (z h : R) : trM z h (mulNF h (e (4:Fin 24)) (e (22:Fin 24))) = h^4*z^3 + h^3*z^2 + 3*h^2*z^3 + 2*h*z^2 + z^3 := by
  have hmul : mulNF h (e (4:Fin 24)) (e (22:Fin 24)) = mulσ0 h (mulσ1 h (mulσ0 h (mulσ2 h (mulσ1 h (e (4 : Fin 24)))))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (4 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ1 h (e (4 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh2 : mulσ2 h (mulσ1 h (e (4 : Fin 24))) = ![0, 0, 0, 0, 0, 1, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  have hh3 : mulσ0 h (mulσ2 h (mulσ1 h (e (4 : Fin 24)))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, h, 0, 0, 0, 0, 0] := by rw [hh2]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  have hh4 : mulσ1 h (mulσ0 h (mulσ2 h (mulσ1 h (e (4 : Fin 24))))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, h, 0] := by rw [hh3]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh5 : mulσ0 h (mulσ1 h (mulσ0 h (mulσ2 h (mulσ1 h (e (4 : Fin 24)))))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, h, 0, h, 0, 0, h^2, 0] := by rw [hh4]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  rw [hh5]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_4_23 (z h : R) : trM z h (mulNF h (e (4:Fin 24)) (e (23:Fin 24))) = h^5*z^3 + h^4*z^2 + 4*h^3*z^3 + 4*h^2*z^2 + 2*h*z^3 + h*z + z^2 := by
  have hmul : mulNF h (e (4:Fin 24)) (e (23:Fin 24)) = mulσ0 h (mulσ1 h (mulσ0 h (mulσ2 h (mulσ1 h (mulσ0 h (e (4 : Fin 24))))))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (4 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ0 h (e (4 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  have hh2 : mulσ1 h (mulσ0 h (e (4 : Fin 24))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh3 : mulσ2 h (mulσ1 h (mulσ0 h (e (4 : Fin 24)))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0] := by rw [hh2]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  have hh4 : mulσ0 h (mulσ2 h (mulσ1 h (mulσ0 h (e (4 : Fin 24))))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1] := by rw [hh3]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  have hh5 : mulσ1 h (mulσ0 h (mulσ2 h (mulσ1 h (mulσ0 h (e (4 : Fin 24)))))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, h] := by rw [hh4]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh6 : mulσ0 h (mulσ1 h (mulσ0 h (mulσ2 h (mulσ1 h (mulσ0 h (e (4 : Fin 24))))))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, h, h, 0, h^2] := by rw [hh5]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  rw [hh6]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_5_0 (z h : R) : trM z h (mulNF h (e (5:Fin 24)) (e (0:Fin 24))) = z^2 := by
  have hmul : mulNF h (e (5:Fin 24)) (e (0:Fin 24)) = e (5 : Fin 24) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (5 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  rw [hh0]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_5_1 (z h : R) : trM z h (mulNF h (e (5:Fin 24)) (e (1:Fin 24))) = h*z^2 + z := by
  have hmul : mulNF h (e (5:Fin 24)) (e (1:Fin 24)) = mulσ2 h (e (5 : Fin 24)) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (5 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ2 h (e (5 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  rw [hh1]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_5_2 (z h : R) : trM z h (mulNF h (e (5:Fin 24)) (e (2:Fin 24))) = h*z^2 + z := by
  have hmul : mulNF h (e (5:Fin 24)) (e (2:Fin 24)) = mulσ1 h (e (5 : Fin 24)) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (5 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ1 h (e (5 : Fin 24)) = ![0, 1, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  rw [hh1]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_5_3 (z h : R) : trM z h (mulNF h (e (5:Fin 24)) (e (3:Fin 24))) = z^3 := by
  have hmul : mulNF h (e (5:Fin 24)) (e (3:Fin 24)) = mulσ0 h (e (5 : Fin 24)) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (5 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ0 h (e (5 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  rw [hh1]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_5_4 (z h : R) : trM z h (mulNF h (e (5:Fin 24)) (e (4:Fin 24))) = h^2*z^2 + 2*h*z + 1 := by
  have hmul : mulNF h (e (5:Fin 24)) (e (4:Fin 24)) = mulσ2 h (mulσ1 h (e (5 : Fin 24))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (5 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ1 h (e (5 : Fin 24)) = ![0, 1, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh2 : mulσ2 h (mulσ1 h (e (5 : Fin 24))) = ![1, h, 0, 0, 0, 0, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  rw [hh2]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_5_5 (z h : R) : trM z h (mulNF h (e (5:Fin 24)) (e (5:Fin 24))) = h^2*z^2 + h*z + z^2 := by
  have hmul : mulNF h (e (5:Fin 24)) (e (5:Fin 24)) = mulσ1 h (mulσ2 h (e (5 : Fin 24))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (5 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ2 h (e (5 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  have hh2 : mulσ1 h (mulσ2 h (e (5 : Fin 24))) = ![0, 0, 0, 0, 1, 0, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  rw [hh2]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_5_6 (z h : R) : trM z h (mulNF h (e (5:Fin 24)) (e (6:Fin 24))) = h*z^3 + z^2 := by
  have hmul : mulNF h (e (5:Fin 24)) (e (6:Fin 24)) = mulσ0 h (mulσ2 h (e (5 : Fin 24))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (5 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ2 h (e (5 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  have hh2 : mulσ0 h (mulσ2 h (e (5 : Fin 24))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  rw [hh2]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_5_7 (z h : R) : trM z h (mulNF h (e (5:Fin 24)) (e (7:Fin 24))) = h*z^3 + z^2 := by
  have hmul : mulNF h (e (5:Fin 24)) (e (7:Fin 24)) = mulσ1 h (mulσ0 h (e (5 : Fin 24))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (5 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ0 h (e (5 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  have hh2 : mulσ1 h (mulσ0 h (e (5 : Fin 24))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  rw [hh2]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_5_8 (z h : R) : trM z h (mulNF h (e (5:Fin 24)) (e (8:Fin 24))) = h*z^3 + z^2 := by
  have hmul : mulNF h (e (5:Fin 24)) (e (8:Fin 24)) = mulσ0 h (mulσ1 h (e (5 : Fin 24))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (5 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ1 h (e (5 : Fin 24)) = ![0, 1, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh2 : mulσ0 h (mulσ1 h (e (5 : Fin 24))) = ![0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  rw [hh2]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_5_9 (z h : R) : trM z h (mulNF h (e (5:Fin 24)) (e (9:Fin 24))) = h^3*z^2 + h^2*z + 2*h*z^2 + z := by
  have hmul : mulNF h (e (5:Fin 24)) (e (9:Fin 24)) = mulσ1 h (mulσ2 h (mulσ1 h (e (5 : Fin 24)))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (5 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ1 h (e (5 : Fin 24)) = ![0, 1, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh2 : mulσ2 h (mulσ1 h (e (5 : Fin 24))) = ![1, h, 0, 0, 0, 0, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  have hh3 : mulσ1 h (mulσ2 h (mulσ1 h (e (5 : Fin 24)))) = ![0, 0, 1, 0, h, h, 0, 0, 0, h^2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh2]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  rw [hh3]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_5_10 (z h : R) : trM z h (mulNF h (e (5:Fin 24)) (e (10:Fin 24))) = h^2*z^3 + 2*h*z^2 + z := by
  have hmul : mulNF h (e (5:Fin 24)) (e (10:Fin 24)) = mulσ2 h (mulσ1 h (mulσ0 h (e (5 : Fin 24)))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (5 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ0 h (e (5 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  have hh2 : mulσ1 h (mulσ0 h (e (5 : Fin 24))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh3 : mulσ2 h (mulσ1 h (mulσ0 h (e (5 : Fin 24)))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0] := by rw [hh2]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  rw [hh3]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_5_11 (z h : R) : trM z h (mulNF h (e (5:Fin 24)) (e (11:Fin 24))) = h^2*z^3 + h*z^2 + z^3 := by
  have hmul : mulNF h (e (5:Fin 24)) (e (11:Fin 24)) = mulσ1 h (mulσ0 h (mulσ2 h (e (5 : Fin 24)))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (5 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ2 h (e (5 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  have hh2 : mulσ0 h (mulσ2 h (e (5 : Fin 24))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  have hh3 : mulσ1 h (mulσ0 h (mulσ2 h (e (5 : Fin 24)))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0] := by rw [hh2]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  rw [hh3]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_5_12 (z h : R) : trM z h (mulNF h (e (5:Fin 24)) (e (12:Fin 24))) = h^2*z^3 + 2*h*z^2 + z := by
  have hmul : mulNF h (e (5:Fin 24)) (e (12:Fin 24)) = mulσ0 h (mulσ2 h (mulσ1 h (e (5 : Fin 24)))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (5 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ1 h (e (5 : Fin 24)) = ![0, 1, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh2 : mulσ2 h (mulσ1 h (e (5 : Fin 24))) = ![1, h, 0, 0, 0, 0, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  have hh3 : mulσ0 h (mulσ2 h (mulσ1 h (e (5 : Fin 24)))) = ![0, 0, 0, 1, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, h, 0, 0, 0, 0, 0] := by rw [hh2]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  rw [hh3]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_5_13 (z h : R) : trM z h (mulNF h (e (5:Fin 24)) (e (13:Fin 24))) = h^2*z^3 + h*z^2 + z^3 := by
  have hmul : mulNF h (e (5:Fin 24)) (e (13:Fin 24)) = mulσ0 h (mulσ1 h (mulσ0 h (e (5 : Fin 24)))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (5 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ0 h (e (5 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  have hh2 : mulσ1 h (mulσ0 h (e (5 : Fin 24))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh3 : mulσ0 h (mulσ1 h (mulσ0 h (e (5 : Fin 24)))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, h, 0, 0, 0, 0] := by rw [hh2]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  rw [hh3]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_5_14 (z h : R) : trM z h (mulNF h (e (5:Fin 24)) (e (14:Fin 24))) = h^2*z^3 + h*z^2 + z^3 := by
  have hmul : mulNF h (e (5:Fin 24)) (e (14:Fin 24)) = mulσ0 h (mulσ1 h (mulσ2 h (e (5 : Fin 24)))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (5 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ2 h (e (5 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  have hh2 : mulσ1 h (mulσ2 h (e (5 : Fin 24))) = ![0, 0, 0, 0, 1, 0, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh3 : mulσ0 h (mulσ1 h (mulσ2 h (e (5 : Fin 24)))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, h, 0, 0, 0, 0, 0] := by rw [hh2]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  rw [hh3]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_5_15 (z h : R) : trM z h (mulNF h (e (5:Fin 24)) (e (15:Fin 24))) = h^3*z^3 + h^2*z^2 + 2*h*z^3 + z^2 := by
  have hmul : mulNF h (e (5:Fin 24)) (e (15:Fin 24)) = mulσ1 h (mulσ2 h (mulσ1 h (mulσ0 h (e (5 : Fin 24))))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (5 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ0 h (e (5 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  have hh2 : mulσ1 h (mulσ0 h (e (5 : Fin 24))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh3 : mulσ2 h (mulσ1 h (mulσ0 h (e (5 : Fin 24)))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0] := by rw [hh2]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  have hh4 : mulσ1 h (mulσ2 h (mulσ1 h (mulσ0 h (e (5 : Fin 24))))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1] := by rw [hh3]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  rw [hh4]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_5_16 (z h : R) : trM z h (mulNF h (e (5:Fin 24)) (e (16:Fin 24))) = h^3*z^3 + 2*h^2*z^2 + h*z^3 + h*z + z^2 := by
  have hmul : mulNF h (e (5:Fin 24)) (e (16:Fin 24)) = mulσ0 h (mulσ2 h (mulσ1 h (mulσ0 h (e (5 : Fin 24))))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (5 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ0 h (e (5 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  have hh2 : mulσ1 h (mulσ0 h (e (5 : Fin 24))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh3 : mulσ2 h (mulσ1 h (mulσ0 h (e (5 : Fin 24)))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0] := by rw [hh2]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  have hh4 : mulσ0 h (mulσ2 h (mulσ1 h (mulσ0 h (e (5 : Fin 24))))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, h, 0, 0] := by rw [hh3]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  rw [hh4]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_5_17 (z h : R) : trM z h (mulNF h (e (5:Fin 24)) (e (17:Fin 24))) = h^3*z^3 + h^2*z^2 + 2*h*z^3 + z^2 := by
  have hmul : mulNF h (e (5:Fin 24)) (e (17:Fin 24)) = mulσ1 h (mulσ0 h (mulσ2 h (mulσ1 h (e (5 : Fin 24))))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (5 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ1 h (e (5 : Fin 24)) = ![0, 1, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh2 : mulσ2 h (mulσ1 h (e (5 : Fin 24))) = ![1, h, 0, 0, 0, 0, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  have hh3 : mulσ0 h (mulσ2 h (mulσ1 h (e (5 : Fin 24)))) = ![0, 0, 0, 1, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, h, 0, 0, 0, 0, 0] := by rw [hh2]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  have hh4 : mulσ1 h (mulσ0 h (mulσ2 h (mulσ1 h (e (5 : Fin 24))))) = ![0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, h, 0] := by rw [hh3]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  rw [hh4]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_5_18 (z h : R) : trM z h (mulNF h (e (5:Fin 24)) (e (18:Fin 24))) = h^3*z^3 + h^2*z^2 + 2*h*z^3 + z^2 := by
  have hmul : mulNF h (e (5:Fin 24)) (e (18:Fin 24)) = mulσ0 h (mulσ1 h (mulσ2 h (mulσ1 h (e (5 : Fin 24))))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (5 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ1 h (e (5 : Fin 24)) = ![0, 1, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh2 : mulσ2 h (mulσ1 h (e (5 : Fin 24))) = ![1, h, 0, 0, 0, 0, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  have hh3 : mulσ1 h (mulσ2 h (mulσ1 h (e (5 : Fin 24)))) = ![0, 0, 1, 0, h, h, 0, 0, 0, h^2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh2]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh4 : mulσ0 h (mulσ1 h (mulσ2 h (mulσ1 h (e (5 : Fin 24))))) = ![0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, h, 0, h, 0, 0, 0, h^2, 0, 0, 0, 0, 0] := by rw [hh3]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  rw [hh4]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_5_19 (z h : R) : trM z h (mulNF h (e (5:Fin 24)) (e (19:Fin 24))) = h^3*z^3 + h^2*z^2 + 2*h*z^3 + z^2 := by
  have hmul : mulNF h (e (5:Fin 24)) (e (19:Fin 24)) = mulσ0 h (mulσ1 h (mulσ0 h (mulσ2 h (e (5 : Fin 24))))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (5 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ2 h (e (5 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  have hh2 : mulσ0 h (mulσ2 h (e (5 : Fin 24))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  have hh3 : mulσ1 h (mulσ0 h (mulσ2 h (e (5 : Fin 24)))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0] := by rw [hh2]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh4 : mulσ0 h (mulσ1 h (mulσ0 h (mulσ2 h (e (5 : Fin 24))))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, h, 0] := by rw [hh3]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  rw [hh4]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_5_20 (z h : R) : trM z h (mulNF h (e (5:Fin 24)) (e (20:Fin 24))) = h^4*z^3 + h^3*z^2 + 3*h^2*z^3 + 2*h*z^2 + z^3 := by
  have hmul : mulNF h (e (5:Fin 24)) (e (20:Fin 24)) = mulσ1 h (mulσ0 h (mulσ2 h (mulσ1 h (mulσ0 h (e (5 : Fin 24)))))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (5 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ0 h (e (5 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  have hh2 : mulσ1 h (mulσ0 h (e (5 : Fin 24))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh3 : mulσ2 h (mulσ1 h (mulσ0 h (e (5 : Fin 24)))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0] := by rw [hh2]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  have hh4 : mulσ0 h (mulσ2 h (mulσ1 h (mulσ0 h (e (5 : Fin 24))))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, h, 0, 0] := by rw [hh3]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  have hh5 : mulσ1 h (mulσ0 h (mulσ2 h (mulσ1 h (mulσ0 h (e (5 : Fin 24)))))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, h] := by rw [hh4]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  rw [hh5]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_5_21 (z h : R) : trM z h (mulNF h (e (5:Fin 24)) (e (21:Fin 24))) = h^4*z^3 + h^3*z^2 + 3*h^2*z^3 + 2*h*z^2 + z^3 := by
  have hmul : mulNF h (e (5:Fin 24)) (e (21:Fin 24)) = mulσ0 h (mulσ1 h (mulσ2 h (mulσ1 h (mulσ0 h (e (5 : Fin 24)))))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (5 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ0 h (e (5 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  have hh2 : mulσ1 h (mulσ0 h (e (5 : Fin 24))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh3 : mulσ2 h (mulσ1 h (mulσ0 h (e (5 : Fin 24)))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0] := by rw [hh2]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  have hh4 : mulσ1 h (mulσ2 h (mulσ1 h (mulσ0 h (e (5 : Fin 24))))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1] := by rw [hh3]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh5 : mulσ0 h (mulσ1 h (mulσ2 h (mulσ1 h (mulσ0 h (e (5 : Fin 24)))))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, h] := by rw [hh4]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  rw [hh5]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_5_22 (z h : R) : trM z h (mulNF h (e (5:Fin 24)) (e (22:Fin 24))) = h^4*z^3 + h^3*z^2 + 3*h^2*z^3 + 3*h*z^2 + z := by
  have hmul : mulNF h (e (5:Fin 24)) (e (22:Fin 24)) = mulσ0 h (mulσ1 h (mulσ0 h (mulσ2 h (mulσ1 h (e (5 : Fin 24)))))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (5 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ1 h (e (5 : Fin 24)) = ![0, 1, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh2 : mulσ2 h (mulσ1 h (e (5 : Fin 24))) = ![1, h, 0, 0, 0, 0, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  have hh3 : mulσ0 h (mulσ2 h (mulσ1 h (e (5 : Fin 24)))) = ![0, 0, 0, 1, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, h, 0, 0, 0, 0, 0] := by rw [hh2]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  have hh4 : mulσ1 h (mulσ0 h (mulσ2 h (mulσ1 h (e (5 : Fin 24))))) = ![0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, h, 0] := by rw [hh3]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh5 : mulσ0 h (mulσ1 h (mulσ0 h (mulσ2 h (mulσ1 h (e (5 : Fin 24)))))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, h, 0, h, 0, 0, h^2, 0] := by rw [hh4]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  rw [hh5]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_5_23 (z h : R) : trM z h (mulNF h (e (5:Fin 24)) (e (23:Fin 24))) = h^5*z^3 + h^4*z^2 + 4*h^3*z^3 + 4*h^2*z^2 + 2*h*z^3 + h*z + z^2 := by
  have hmul : mulNF h (e (5:Fin 24)) (e (23:Fin 24)) = mulσ0 h (mulσ1 h (mulσ0 h (mulσ2 h (mulσ1 h (mulσ0 h (e (5 : Fin 24))))))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (5 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ0 h (e (5 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  have hh2 : mulσ1 h (mulσ0 h (e (5 : Fin 24))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh3 : mulσ2 h (mulσ1 h (mulσ0 h (e (5 : Fin 24)))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0] := by rw [hh2]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  have hh4 : mulσ0 h (mulσ2 h (mulσ1 h (mulσ0 h (e (5 : Fin 24))))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, h, 0, 0] := by rw [hh3]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  have hh5 : mulσ1 h (mulσ0 h (mulσ2 h (mulσ1 h (mulσ0 h (e (5 : Fin 24)))))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, h] := by rw [hh4]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh6 : mulσ0 h (mulσ1 h (mulσ0 h (mulσ2 h (mulσ1 h (mulσ0 h (e (5 : Fin 24))))))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, h, h, 0, h^2] := by rw [hh5]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  rw [hh6]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

end QOU.Machinery.H4
