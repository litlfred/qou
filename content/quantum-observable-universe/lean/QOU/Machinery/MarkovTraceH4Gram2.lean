import QOU.Machinery.MarkovTraceH4Gram1

/-!
# QOU.Machinery.H4 Gram closure — part 2 of 8

Auto-generated Gram entries `G_(i,j) = tr_M(b_i * b_j)`, emitted by
`computations/markov/gen_gram_closure.py`.

Split across 8 modules, each importing the previous, so the chain is
built serially and peak elaboration memory stays bounded. Held as ONE module the
closure needs ~15 GB and over an hour (bean qou-8hjy); the split is a pure
refactor — same theorems, same proofs, same namespace.
-/

namespace QOU.Machinery.H4

variable {R : Type*} [CommRing R]

theorem gramval_6_0 (z h : R) : trM z h (mulNF h (e (6:Fin 24)) (e (0:Fin 24))) = z^2 := by
  have hmul : mulNF h (e (6:Fin 24)) (e (0:Fin 24)) = e (6 : Fin 24) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (6 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  rw [hh0]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_6_1 (z h : R) : trM z h (mulNF h (e (6:Fin 24)) (e (1:Fin 24))) = h*z^2 + z := by
  have hmul : mulNF h (e (6:Fin 24)) (e (1:Fin 24)) = mulσ2 h (e (6 : Fin 24)) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (6 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ2 h (e (6 : Fin 24)) = ![0, 0, 0, 1, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  rw [hh1]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_6_2 (z h : R) : trM z h (mulNF h (e (6:Fin 24)) (e (2:Fin 24))) = z^3 := by
  have hmul : mulNF h (e (6:Fin 24)) (e (2:Fin 24)) = mulσ1 h (e (6 : Fin 24)) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (6 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ1 h (e (6 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  rw [hh1]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_6_3 (z h : R) : trM z h (mulNF h (e (6:Fin 24)) (e (3:Fin 24))) = h*z^2 + z := by
  have hmul : mulNF h (e (6:Fin 24)) (e (3:Fin 24)) = mulσ0 h (e (6 : Fin 24)) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (6 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ0 h (e (6 : Fin 24)) = ![0, 1, 0, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  rw [hh1]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_6_4 (z h : R) : trM z h (mulNF h (e (6:Fin 24)) (e (4:Fin 24))) = h*z^3 + z^2 := by
  have hmul : mulNF h (e (6:Fin 24)) (e (4:Fin 24)) = mulσ2 h (mulσ1 h (e (6 : Fin 24))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (6 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ1 h (e (6 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh2 : mulσ2 h (mulσ1 h (e (6 : Fin 24))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  rw [hh2]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_6_5 (z h : R) : trM z h (mulNF h (e (6:Fin 24)) (e (5:Fin 24))) = h*z^3 + z^2 := by
  have hmul : mulNF h (e (6:Fin 24)) (e (5:Fin 24)) = mulσ1 h (mulσ2 h (e (6 : Fin 24))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (6 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ2 h (e (6 : Fin 24)) = ![0, 0, 0, 1, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  have hh2 : mulσ1 h (mulσ2 h (e (6 : Fin 24))) = ![0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  rw [hh2]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_6_6 (z h : R) : trM z h (mulNF h (e (6:Fin 24)) (e (6:Fin 24))) = h^2*z^2 + 2*h*z + 1 := by
  have hmul : mulNF h (e (6:Fin 24)) (e (6:Fin 24)) = mulσ0 h (mulσ2 h (e (6 : Fin 24))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (6 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ2 h (e (6 : Fin 24)) = ![0, 0, 0, 1, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  have hh2 : mulσ0 h (mulσ2 h (e (6 : Fin 24))) = ![1, h, 0, h, 0, 0, h^2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  rw [hh2]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_6_7 (z h : R) : trM z h (mulNF h (e (6:Fin 24)) (e (7:Fin 24))) = h*z^3 + z^2 := by
  have hmul : mulNF h (e (6:Fin 24)) (e (7:Fin 24)) = mulσ1 h (mulσ0 h (e (6 : Fin 24))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (6 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ0 h (e (6 : Fin 24)) = ![0, 1, 0, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  have hh2 : mulσ1 h (mulσ0 h (e (6 : Fin 24))) = ![0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  rw [hh2]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_6_8 (z h : R) : trM z h (mulNF h (e (6:Fin 24)) (e (8:Fin 24))) = h*z^3 + z^2 := by
  have hmul : mulNF h (e (6:Fin 24)) (e (8:Fin 24)) = mulσ0 h (mulσ1 h (e (6 : Fin 24))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (6 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ1 h (e (6 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh2 : mulσ0 h (mulσ1 h (e (6 : Fin 24))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  rw [hh2]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_6_9 (z h : R) : trM z h (mulNF h (e (6:Fin 24)) (e (9:Fin 24))) = h^2*z^3 + h*z^2 + z^3 := by
  have hmul : mulNF h (e (6:Fin 24)) (e (9:Fin 24)) = mulσ1 h (mulσ2 h (mulσ1 h (e (6 : Fin 24)))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (6 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ1 h (e (6 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh2 : mulσ2 h (mulσ1 h (e (6 : Fin 24))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  have hh3 : mulσ1 h (mulσ2 h (mulσ1 h (e (6 : Fin 24)))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh2]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  rw [hh3]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_6_10 (z h : R) : trM z h (mulNF h (e (6:Fin 24)) (e (10:Fin 24))) = h^2*z^3 + 2*h*z^2 + z := by
  have hmul : mulNF h (e (6:Fin 24)) (e (10:Fin 24)) = mulσ2 h (mulσ1 h (mulσ0 h (e (6 : Fin 24)))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (6 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ0 h (e (6 : Fin 24)) = ![0, 1, 0, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  have hh2 : mulσ1 h (mulσ0 h (e (6 : Fin 24))) = ![0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh3 : mulσ2 h (mulσ1 h (mulσ0 h (e (6 : Fin 24)))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh2]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  rw [hh3]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_6_11 (z h : R) : trM z h (mulNF h (e (6:Fin 24)) (e (11:Fin 24))) = h^2*z^3 + 2*h*z^2 + z := by
  have hmul : mulNF h (e (6:Fin 24)) (e (11:Fin 24)) = mulσ1 h (mulσ0 h (mulσ2 h (e (6 : Fin 24)))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (6 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ2 h (e (6 : Fin 24)) = ![0, 0, 0, 1, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  have hh2 : mulσ0 h (mulσ2 h (e (6 : Fin 24))) = ![1, h, 0, h, 0, 0, h^2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  have hh3 : mulσ1 h (mulσ0 h (mulσ2 h (e (6 : Fin 24)))) = ![0, 0, 1, 0, 0, h, 0, h, 0, 0, 0, h^2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh2]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  rw [hh3]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_6_12 (z h : R) : trM z h (mulNF h (e (6:Fin 24)) (e (12:Fin 24))) = h^2*z^3 + 2*h*z^2 + z := by
  have hmul : mulNF h (e (6:Fin 24)) (e (12:Fin 24)) = mulσ0 h (mulσ2 h (mulσ1 h (e (6 : Fin 24)))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (6 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ1 h (e (6 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh2 : mulσ2 h (mulσ1 h (e (6 : Fin 24))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  have hh3 : mulσ0 h (mulσ2 h (mulσ1 h (e (6 : Fin 24)))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0] := by rw [hh2]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  rw [hh3]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_6_13 (z h : R) : trM z h (mulNF h (e (6:Fin 24)) (e (13:Fin 24))) = h^2*z^3 + h*z^2 + z^3 := by
  have hmul : mulNF h (e (6:Fin 24)) (e (13:Fin 24)) = mulσ0 h (mulσ1 h (mulσ0 h (e (6 : Fin 24)))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (6 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ0 h (e (6 : Fin 24)) = ![0, 1, 0, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  have hh2 : mulσ1 h (mulσ0 h (e (6 : Fin 24))) = ![0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh3 : mulσ0 h (mulσ1 h (mulσ0 h (e (6 : Fin 24)))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, h, 0, 0, 0, 0] := by rw [hh2]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  rw [hh3]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_6_14 (z h : R) : trM z h (mulNF h (e (6:Fin 24)) (e (14:Fin 24))) = h^2*z^3 + 2*h*z^2 + z := by
  have hmul : mulNF h (e (6:Fin 24)) (e (14:Fin 24)) = mulσ0 h (mulσ1 h (mulσ2 h (e (6 : Fin 24)))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (6 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ2 h (e (6 : Fin 24)) = ![0, 0, 0, 1, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  have hh2 : mulσ1 h (mulσ2 h (e (6 : Fin 24))) = ![0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh3 : mulσ0 h (mulσ1 h (mulσ2 h (e (6 : Fin 24)))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, h, 0, 0, 0, 0] := by rw [hh2]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  rw [hh3]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_6_15 (z h : R) : trM z h (mulNF h (e (6:Fin 24)) (e (15:Fin 24))) = h^3*z^3 + 2*h^2*z^2 + h*z^3 + h*z + z^2 := by
  have hmul : mulNF h (e (6:Fin 24)) (e (15:Fin 24)) = mulσ1 h (mulσ2 h (mulσ1 h (mulσ0 h (e (6 : Fin 24))))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (6 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ0 h (e (6 : Fin 24)) = ![0, 1, 0, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  have hh2 : mulσ1 h (mulσ0 h (e (6 : Fin 24))) = ![0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh3 : mulσ2 h (mulσ1 h (mulσ0 h (e (6 : Fin 24)))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh2]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  have hh4 : mulσ1 h (mulσ2 h (mulσ1 h (mulσ0 h (e (6 : Fin 24))))) = ![0, 0, 0, 0, 1, 0, 0, 0, 0, h, h, 0, 0, 0, 0, h^2, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh3]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  rw [hh4]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_6_16 (z h : R) : trM z h (mulNF h (e (6:Fin 24)) (e (16:Fin 24))) = h^3*z^3 + 2*h^2*z^2 + h*z^3 + h*z + z^2 := by
  have hmul : mulNF h (e (6:Fin 24)) (e (16:Fin 24)) = mulσ0 h (mulσ2 h (mulσ1 h (mulσ0 h (e (6 : Fin 24))))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (6 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ0 h (e (6 : Fin 24)) = ![0, 1, 0, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  have hh2 : mulσ1 h (mulσ0 h (e (6 : Fin 24))) = ![0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh3 : mulσ2 h (mulσ1 h (mulσ0 h (e (6 : Fin 24)))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh2]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  have hh4 : mulσ0 h (mulσ2 h (mulσ1 h (mulσ0 h (e (6 : Fin 24))))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, h, 0, 0] := by rw [hh3]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  rw [hh4]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_6_17 (z h : R) : trM z h (mulNF h (e (6:Fin 24)) (e (17:Fin 24))) = h^3*z^3 + h^2*z^2 + 2*h*z^3 + z^2 := by
  have hmul : mulNF h (e (6:Fin 24)) (e (17:Fin 24)) = mulσ1 h (mulσ0 h (mulσ2 h (mulσ1 h (e (6 : Fin 24))))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (6 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ1 h (e (6 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh2 : mulσ2 h (mulσ1 h (e (6 : Fin 24))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  have hh3 : mulσ0 h (mulσ2 h (mulσ1 h (e (6 : Fin 24)))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0] := by rw [hh2]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  have hh4 : mulσ1 h (mulσ0 h (mulσ2 h (mulσ1 h (e (6 : Fin 24))))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1] := by rw [hh3]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  rw [hh4]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_6_18 (z h : R) : trM z h (mulNF h (e (6:Fin 24)) (e (18:Fin 24))) = h^3*z^3 + 2*h^2*z^2 + h*z^3 + h*z + z^2 := by
  have hmul : mulNF h (e (6:Fin 24)) (e (18:Fin 24)) = mulσ0 h (mulσ1 h (mulσ2 h (mulσ1 h (e (6 : Fin 24))))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (6 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ1 h (e (6 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh2 : mulσ2 h (mulσ1 h (e (6 : Fin 24))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  have hh3 : mulσ1 h (mulσ2 h (mulσ1 h (e (6 : Fin 24)))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh2]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh4 : mulσ0 h (mulσ1 h (mulσ2 h (mulσ1 h (e (6 : Fin 24))))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, h, 0, 0] := by rw [hh3]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  rw [hh4]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_6_19 (z h : R) : trM z h (mulNF h (e (6:Fin 24)) (e (19:Fin 24))) = h^3*z^3 + 2*h^2*z^2 + h*z^3 + h*z + z^2 := by
  have hmul : mulNF h (e (6:Fin 24)) (e (19:Fin 24)) = mulσ0 h (mulσ1 h (mulσ0 h (mulσ2 h (e (6 : Fin 24))))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (6 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ2 h (e (6 : Fin 24)) = ![0, 0, 0, 1, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  have hh2 : mulσ0 h (mulσ2 h (e (6 : Fin 24))) = ![1, h, 0, h, 0, 0, h^2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  have hh3 : mulσ1 h (mulσ0 h (mulσ2 h (e (6 : Fin 24)))) = ![0, 0, 1, 0, 0, h, 0, h, 0, 0, 0, h^2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh2]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh4 : mulσ0 h (mulσ1 h (mulσ0 h (mulσ2 h (e (6 : Fin 24))))) = ![0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, h, h, 0, 0, 0, 0, h^2, 0, 0, 0, 0] := by rw [hh3]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  rw [hh4]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_6_20 (z h : R) : trM z h (mulNF h (e (6:Fin 24)) (e (20:Fin 24))) = h^4*z^3 + h^3*z^2 + 3*h^2*z^3 + 2*h*z^2 + z^3 := by
  have hmul : mulNF h (e (6:Fin 24)) (e (20:Fin 24)) = mulσ1 h (mulσ0 h (mulσ2 h (mulσ1 h (mulσ0 h (e (6 : Fin 24)))))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (6 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ0 h (e (6 : Fin 24)) = ![0, 1, 0, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  have hh2 : mulσ1 h (mulσ0 h (e (6 : Fin 24))) = ![0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh3 : mulσ2 h (mulσ1 h (mulσ0 h (e (6 : Fin 24)))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh2]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  have hh4 : mulσ0 h (mulσ2 h (mulσ1 h (mulσ0 h (e (6 : Fin 24))))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, h, 0, 0] := by rw [hh3]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  have hh5 : mulσ1 h (mulσ0 h (mulσ2 h (mulσ1 h (mulσ0 h (e (6 : Fin 24)))))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, h] := by rw [hh4]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  rw [hh5]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_6_21 (z h : R) : trM z h (mulNF h (e (6:Fin 24)) (e (21:Fin 24))) = h^4*z^3 + 2*h^3*z^2 + 2*h^2*z^3 + h^2*z + 2*h*z^2 + z^3 := by
  have hmul : mulNF h (e (6:Fin 24)) (e (21:Fin 24)) = mulσ0 h (mulσ1 h (mulσ2 h (mulσ1 h (mulσ0 h (e (6 : Fin 24)))))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (6 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ0 h (e (6 : Fin 24)) = ![0, 1, 0, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  have hh2 : mulσ1 h (mulσ0 h (e (6 : Fin 24))) = ![0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh3 : mulσ2 h (mulσ1 h (mulσ0 h (e (6 : Fin 24)))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh2]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  have hh4 : mulσ1 h (mulσ2 h (mulσ1 h (mulσ0 h (e (6 : Fin 24))))) = ![0, 0, 0, 0, 1, 0, 0, 0, 0, h, h, 0, 0, 0, 0, h^2, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh3]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh5 : mulσ0 h (mulσ1 h (mulσ2 h (mulσ1 h (mulσ0 h (e (6 : Fin 24)))))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, h, 0, h, 0, 0, h^2, 0, 0] := by rw [hh4]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  rw [hh5]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_6_22 (z h : R) : trM z h (mulNF h (e (6:Fin 24)) (e (22:Fin 24))) = h^4*z^3 + h^3*z^2 + 3*h^2*z^3 + 2*h*z^2 + z^3 := by
  have hmul : mulNF h (e (6:Fin 24)) (e (22:Fin 24)) = mulσ0 h (mulσ1 h (mulσ0 h (mulσ2 h (mulσ1 h (e (6 : Fin 24)))))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (6 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ1 h (e (6 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh2 : mulσ2 h (mulσ1 h (e (6 : Fin 24))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  have hh3 : mulσ0 h (mulσ2 h (mulσ1 h (e (6 : Fin 24)))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0] := by rw [hh2]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  have hh4 : mulσ1 h (mulσ0 h (mulσ2 h (mulσ1 h (e (6 : Fin 24))))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1] := by rw [hh3]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh5 : mulσ0 h (mulσ1 h (mulσ0 h (mulσ2 h (mulσ1 h (e (6 : Fin 24)))))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, h] := by rw [hh4]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  rw [hh5]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_6_23 (z h : R) : trM z h (mulNF h (e (6:Fin 24)) (e (23:Fin 24))) = h^5*z^3 + h^4*z^2 + 4*h^3*z^3 + 3*h^2*z^2 + 3*h*z^3 + z^2 := by
  have hmul : mulNF h (e (6:Fin 24)) (e (23:Fin 24)) = mulσ0 h (mulσ1 h (mulσ0 h (mulσ2 h (mulσ1 h (mulσ0 h (e (6 : Fin 24))))))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (6 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ0 h (e (6 : Fin 24)) = ![0, 1, 0, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  have hh2 : mulσ1 h (mulσ0 h (e (6 : Fin 24))) = ![0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh3 : mulσ2 h (mulσ1 h (mulσ0 h (e (6 : Fin 24)))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh2]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  have hh4 : mulσ0 h (mulσ2 h (mulσ1 h (mulσ0 h (e (6 : Fin 24))))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, h, 0, 0] := by rw [hh3]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  have hh5 : mulσ1 h (mulσ0 h (mulσ2 h (mulσ1 h (mulσ0 h (e (6 : Fin 24)))))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, h] := by rw [hh4]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh6 : mulσ0 h (mulσ1 h (mulσ0 h (mulσ2 h (mulσ1 h (mulσ0 h (e (6 : Fin 24))))))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, h, 0, h, h^2] := by rw [hh5]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  rw [hh6]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_7_0 (z h : R) : trM z h (mulNF h (e (7:Fin 24)) (e (0:Fin 24))) = z^2 := by
  have hmul : mulNF h (e (7:Fin 24)) (e (0:Fin 24)) = e (7 : Fin 24) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (7 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  rw [hh0]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_7_1 (z h : R) : trM z h (mulNF h (e (7:Fin 24)) (e (1:Fin 24))) = z^3 := by
  have hmul : mulNF h (e (7:Fin 24)) (e (1:Fin 24)) = mulσ2 h (e (7 : Fin 24)) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (7 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ2 h (e (7 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  rw [hh1]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_7_2 (z h : R) : trM z h (mulNF h (e (7:Fin 24)) (e (2:Fin 24))) = h*z^2 + z := by
  have hmul : mulNF h (e (7:Fin 24)) (e (2:Fin 24)) = mulσ1 h (e (7 : Fin 24)) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (7 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ1 h (e (7 : Fin 24)) = ![0, 0, 0, 1, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  rw [hh1]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_7_3 (z h : R) : trM z h (mulNF h (e (7:Fin 24)) (e (3:Fin 24))) = h*z^2 + z := by
  have hmul : mulNF h (e (7:Fin 24)) (e (3:Fin 24)) = mulσ0 h (e (7 : Fin 24)) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (7 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ0 h (e (7 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  rw [hh1]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_7_4 (z h : R) : trM z h (mulNF h (e (7:Fin 24)) (e (4:Fin 24))) = h*z^3 + z^2 := by
  have hmul : mulNF h (e (7:Fin 24)) (e (4:Fin 24)) = mulσ2 h (mulσ1 h (e (7 : Fin 24))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (7 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ1 h (e (7 : Fin 24)) = ![0, 0, 0, 1, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh2 : mulσ2 h (mulσ1 h (e (7 : Fin 24))) = ![0, 0, 0, 0, 0, 0, 1, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  rw [hh2]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_7_5 (z h : R) : trM z h (mulNF h (e (7:Fin 24)) (e (5:Fin 24))) = h*z^3 + z^2 := by
  have hmul : mulNF h (e (7:Fin 24)) (e (5:Fin 24)) = mulσ1 h (mulσ2 h (e (7 : Fin 24))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (7 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ2 h (e (7 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  have hh2 : mulσ1 h (mulσ2 h (e (7 : Fin 24))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  rw [hh2]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_7_6 (z h : R) : trM z h (mulNF h (e (7:Fin 24)) (e (6:Fin 24))) = h*z^3 + z^2 := by
  have hmul : mulNF h (e (7:Fin 24)) (e (6:Fin 24)) = mulσ0 h (mulσ2 h (e (7 : Fin 24))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (7 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ2 h (e (7 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  have hh2 : mulσ0 h (mulσ2 h (e (7 : Fin 24))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  rw [hh2]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_7_7 (z h : R) : trM z h (mulNF h (e (7:Fin 24)) (e (7:Fin 24))) = h^2*z^2 + h*z + z^2 := by
  have hmul : mulNF h (e (7:Fin 24)) (e (7:Fin 24)) = mulσ1 h (mulσ0 h (e (7 : Fin 24))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (7 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ0 h (e (7 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  have hh2 : mulσ1 h (mulσ0 h (e (7 : Fin 24))) = ![0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  rw [hh2]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_7_8 (z h : R) : trM z h (mulNF h (e (7:Fin 24)) (e (8:Fin 24))) = h^2*z^2 + 2*h*z + 1 := by
  have hmul : mulNF h (e (7:Fin 24)) (e (8:Fin 24)) = mulσ0 h (mulσ1 h (e (7 : Fin 24))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (7 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ1 h (e (7 : Fin 24)) = ![0, 0, 0, 1, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh2 : mulσ0 h (mulσ1 h (e (7 : Fin 24))) = ![1, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  rw [hh2]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_7_9 (z h : R) : trM z h (mulNF h (e (7:Fin 24)) (e (9:Fin 24))) = h^2*z^3 + h*z^2 + z^3 := by
  have hmul : mulNF h (e (7:Fin 24)) (e (9:Fin 24)) = mulσ1 h (mulσ2 h (mulσ1 h (e (7 : Fin 24)))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (7 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ1 h (e (7 : Fin 24)) = ![0, 0, 0, 1, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh2 : mulσ2 h (mulσ1 h (e (7 : Fin 24))) = ![0, 0, 0, 0, 0, 0, 1, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  have hh3 : mulσ1 h (mulσ2 h (mulσ1 h (e (7 : Fin 24)))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh2]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  rw [hh3]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_7_10 (z h : R) : trM z h (mulNF h (e (7:Fin 24)) (e (10:Fin 24))) = h^2*z^3 + h*z^2 + z^3 := by
  have hmul : mulNF h (e (7:Fin 24)) (e (10:Fin 24)) = mulσ2 h (mulσ1 h (mulσ0 h (e (7 : Fin 24)))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (7 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ0 h (e (7 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  have hh2 : mulσ1 h (mulσ0 h (e (7 : Fin 24))) = ![0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh3 : mulσ2 h (mulσ1 h (mulσ0 h (e (7 : Fin 24)))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0] := by rw [hh2]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  rw [hh3]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_7_11 (z h : R) : trM z h (mulNF h (e (7:Fin 24)) (e (11:Fin 24))) = h^2*z^3 + h*z^2 + z^3 := by
  have hmul : mulNF h (e (7:Fin 24)) (e (11:Fin 24)) = mulσ1 h (mulσ0 h (mulσ2 h (e (7 : Fin 24)))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (7 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ2 h (e (7 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  have hh2 : mulσ0 h (mulσ2 h (e (7 : Fin 24))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  have hh3 : mulσ1 h (mulσ0 h (mulσ2 h (e (7 : Fin 24)))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0] := by rw [hh2]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  rw [hh3]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_7_12 (z h : R) : trM z h (mulNF h (e (7:Fin 24)) (e (12:Fin 24))) = h^2*z^3 + 2*h*z^2 + z := by
  have hmul : mulNF h (e (7:Fin 24)) (e (12:Fin 24)) = mulσ0 h (mulσ2 h (mulσ1 h (e (7 : Fin 24)))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (7 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ1 h (e (7 : Fin 24)) = ![0, 0, 0, 1, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh2 : mulσ2 h (mulσ1 h (e (7 : Fin 24))) = ![0, 0, 0, 0, 0, 0, 1, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  have hh3 : mulσ0 h (mulσ2 h (mulσ1 h (e (7 : Fin 24)))) = ![0, 1, 0, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0] := by rw [hh2]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  rw [hh3]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_7_13 (z h : R) : trM z h (mulNF h (e (7:Fin 24)) (e (13:Fin 24))) = h^3*z^2 + h^2*z + 2*h*z^2 + z := by
  have hmul : mulNF h (e (7:Fin 24)) (e (13:Fin 24)) = mulσ0 h (mulσ1 h (mulσ0 h (e (7 : Fin 24)))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (7 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ0 h (e (7 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  have hh2 : mulσ1 h (mulσ0 h (e (7 : Fin 24))) = ![0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh3 : mulσ0 h (mulσ1 h (mulσ0 h (e (7 : Fin 24)))) = ![0, 0, 1, 0, 0, 0, 0, h, h, 0, 0, 0, 0, h^2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh2]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  rw [hh3]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_7_14 (z h : R) : trM z h (mulNF h (e (7:Fin 24)) (e (14:Fin 24))) = h^2*z^3 + 2*h*z^2 + z := by
  have hmul : mulNF h (e (7:Fin 24)) (e (14:Fin 24)) = mulσ0 h (mulσ1 h (mulσ2 h (e (7 : Fin 24)))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (7 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ2 h (e (7 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  have hh2 : mulσ1 h (mulσ2 h (e (7 : Fin 24))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh3 : mulσ0 h (mulσ1 h (mulσ2 h (e (7 : Fin 24)))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0] := by rw [hh2]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  rw [hh3]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_7_15 (z h : R) : trM z h (mulNF h (e (7:Fin 24)) (e (15:Fin 24))) = h^3*z^3 + h^2*z^2 + 2*h*z^3 + z^2 := by
  have hmul : mulNF h (e (7:Fin 24)) (e (15:Fin 24)) = mulσ1 h (mulσ2 h (mulσ1 h (mulσ0 h (e (7 : Fin 24))))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (7 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ0 h (e (7 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  have hh2 : mulσ1 h (mulσ0 h (e (7 : Fin 24))) = ![0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh3 : mulσ2 h (mulσ1 h (mulσ0 h (e (7 : Fin 24)))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0] := by rw [hh2]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  have hh4 : mulσ1 h (mulσ2 h (mulσ1 h (mulσ0 h (e (7 : Fin 24))))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, h, 0, 0, 0] := by rw [hh3]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  rw [hh4]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_7_16 (z h : R) : trM z h (mulNF h (e (7:Fin 24)) (e (16:Fin 24))) = h^3*z^3 + h^2*z^2 + 2*h*z^3 + z^2 := by
  have hmul : mulNF h (e (7:Fin 24)) (e (16:Fin 24)) = mulσ0 h (mulσ2 h (mulσ1 h (mulσ0 h (e (7 : Fin 24))))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (7 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ0 h (e (7 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  have hh2 : mulσ1 h (mulσ0 h (e (7 : Fin 24))) = ![0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh3 : mulσ2 h (mulσ1 h (mulσ0 h (e (7 : Fin 24)))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0] := by rw [hh2]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  have hh4 : mulσ0 h (mulσ2 h (mulσ1 h (mulσ0 h (e (7 : Fin 24))))) = ![0, 0, 0, 0, 1, 0, 0, 0, 0, 0, h, 0, h, 0, 0, 0, h^2, 0, 0, 0, 0, 0, 0, 0] := by rw [hh3]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  rw [hh4]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_7_17 (z h : R) : trM z h (mulNF h (e (7:Fin 24)) (e (17:Fin 24))) = h^3*z^3 + h^2*z^2 + 2*h*z^3 + z^2 := by
  have hmul : mulNF h (e (7:Fin 24)) (e (17:Fin 24)) = mulσ1 h (mulσ0 h (mulσ2 h (mulσ1 h (e (7 : Fin 24))))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (7 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ1 h (e (7 : Fin 24)) = ![0, 0, 0, 1, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh2 : mulσ2 h (mulσ1 h (e (7 : Fin 24))) = ![0, 0, 0, 0, 0, 0, 1, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  have hh3 : mulσ0 h (mulσ2 h (mulσ1 h (e (7 : Fin 24)))) = ![0, 1, 0, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0] := by rw [hh2]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  have hh4 : mulσ1 h (mulσ0 h (mulσ2 h (mulσ1 h (e (7 : Fin 24))))) = ![0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, h, 0, 0, 0] := by rw [hh3]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  rw [hh4]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_7_18 (z h : R) : trM z h (mulNF h (e (7:Fin 24)) (e (18:Fin 24))) = h^3*z^3 + 2*h^2*z^2 + h*z^3 + h*z + z^2 := by
  have hmul : mulNF h (e (7:Fin 24)) (e (18:Fin 24)) = mulσ0 h (mulσ1 h (mulσ2 h (mulσ1 h (e (7 : Fin 24))))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (7 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ1 h (e (7 : Fin 24)) = ![0, 0, 0, 1, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh2 : mulσ2 h (mulσ1 h (e (7 : Fin 24))) = ![0, 0, 0, 0, 0, 0, 1, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  have hh3 : mulσ1 h (mulσ2 h (mulσ1 h (e (7 : Fin 24)))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh2]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh4 : mulσ0 h (mulσ1 h (mulσ2 h (mulσ1 h (e (7 : Fin 24))))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, h, 0, 0] := by rw [hh3]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  rw [hh4]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_7_19 (z h : R) : trM z h (mulNF h (e (7:Fin 24)) (e (19:Fin 24))) = h^3*z^3 + h^2*z^2 + 2*h*z^3 + z^2 := by
  have hmul : mulNF h (e (7:Fin 24)) (e (19:Fin 24)) = mulσ0 h (mulσ1 h (mulσ0 h (mulσ2 h (e (7 : Fin 24))))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (7 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ2 h (e (7 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  have hh2 : mulσ0 h (mulσ2 h (e (7 : Fin 24))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  have hh3 : mulσ1 h (mulσ0 h (mulσ2 h (e (7 : Fin 24)))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0] := by rw [hh2]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh4 : mulσ0 h (mulσ1 h (mulσ0 h (mulσ2 h (e (7 : Fin 24))))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1] := by rw [hh3]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  rw [hh4]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_7_20 (z h : R) : trM z h (mulNF h (e (7:Fin 24)) (e (20:Fin 24))) = h^4*z^3 + h^3*z^2 + 3*h^2*z^3 + 3*h*z^2 + z := by
  have hmul : mulNF h (e (7:Fin 24)) (e (20:Fin 24)) = mulσ1 h (mulσ0 h (mulσ2 h (mulσ1 h (mulσ0 h (e (7 : Fin 24)))))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (7 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ0 h (e (7 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  have hh2 : mulσ1 h (mulσ0 h (e (7 : Fin 24))) = ![0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh3 : mulσ2 h (mulσ1 h (mulσ0 h (e (7 : Fin 24)))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0] := by rw [hh2]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  have hh4 : mulσ0 h (mulσ2 h (mulσ1 h (mulσ0 h (e (7 : Fin 24))))) = ![0, 0, 0, 0, 1, 0, 0, 0, 0, 0, h, 0, h, 0, 0, 0, h^2, 0, 0, 0, 0, 0, 0, 0] := by rw [hh3]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  have hh5 : mulσ1 h (mulσ0 h (mulσ2 h (mulσ1 h (mulσ0 h (e (7 : Fin 24)))))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, h, 0, h, 0, 0, h^2, 0, 0, 0] := by rw [hh4]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  rw [hh5]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_7_21 (z h : R) : trM z h (mulNF h (e (7:Fin 24)) (e (21:Fin 24))) = h^4*z^3 + h^3*z^2 + 3*h^2*z^3 + 2*h*z^2 + z^3 := by
  have hmul : mulNF h (e (7:Fin 24)) (e (21:Fin 24)) = mulσ0 h (mulσ1 h (mulσ2 h (mulσ1 h (mulσ0 h (e (7 : Fin 24)))))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (7 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ0 h (e (7 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  have hh2 : mulσ1 h (mulσ0 h (e (7 : Fin 24))) = ![0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh3 : mulσ2 h (mulσ1 h (mulσ0 h (e (7 : Fin 24)))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0] := by rw [hh2]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  have hh4 : mulσ1 h (mulσ2 h (mulσ1 h (mulσ0 h (e (7 : Fin 24))))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, h, 0, 0, 0] := by rw [hh3]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh5 : mulσ0 h (mulσ1 h (mulσ2 h (mulσ1 h (mulσ0 h (e (7 : Fin 24)))))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, h] := by rw [hh4]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  rw [hh5]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_7_22 (z h : R) : trM z h (mulNF h (e (7:Fin 24)) (e (22:Fin 24))) = h^4*z^3 + h^3*z^2 + 3*h^2*z^3 + 2*h*z^2 + z^3 := by
  have hmul : mulNF h (e (7:Fin 24)) (e (22:Fin 24)) = mulσ0 h (mulσ1 h (mulσ0 h (mulσ2 h (mulσ1 h (e (7 : Fin 24)))))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (7 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ1 h (e (7 : Fin 24)) = ![0, 0, 0, 1, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh2 : mulσ2 h (mulσ1 h (e (7 : Fin 24))) = ![0, 0, 0, 0, 0, 0, 1, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  have hh3 : mulσ0 h (mulσ2 h (mulσ1 h (e (7 : Fin 24)))) = ![0, 1, 0, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0] := by rw [hh2]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  have hh4 : mulσ1 h (mulσ0 h (mulσ2 h (mulσ1 h (e (7 : Fin 24))))) = ![0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, h, 0, 0, 0] := by rw [hh3]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh5 : mulσ0 h (mulσ1 h (mulσ0 h (mulσ2 h (mulσ1 h (e (7 : Fin 24)))))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, h, 0, 0, 0, h] := by rw [hh4]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  rw [hh5]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_7_23 (z h : R) : trM z h (mulNF h (e (7:Fin 24)) (e (23:Fin 24))) = h^5*z^3 + h^4*z^2 + 4*h^3*z^3 + 4*h^2*z^2 + 2*h*z^3 + h*z + z^2 := by
  have hmul : mulNF h (e (7:Fin 24)) (e (23:Fin 24)) = mulσ0 h (mulσ1 h (mulσ0 h (mulσ2 h (mulσ1 h (mulσ0 h (e (7 : Fin 24))))))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (7 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ0 h (e (7 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  have hh2 : mulσ1 h (mulσ0 h (e (7 : Fin 24))) = ![0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh3 : mulσ2 h (mulσ1 h (mulσ0 h (e (7 : Fin 24)))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0] := by rw [hh2]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  have hh4 : mulσ0 h (mulσ2 h (mulσ1 h (mulσ0 h (e (7 : Fin 24))))) = ![0, 0, 0, 0, 1, 0, 0, 0, 0, 0, h, 0, h, 0, 0, 0, h^2, 0, 0, 0, 0, 0, 0, 0] := by rw [hh3]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  have hh5 : mulσ1 h (mulσ0 h (mulσ2 h (mulσ1 h (mulσ0 h (e (7 : Fin 24)))))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, h, 0, h, 0, 0, h^2, 0, 0, 0] := by rw [hh4]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh6 : mulσ0 h (mulσ1 h (mulσ0 h (mulσ2 h (mulσ1 h (mulσ0 h (e (7 : Fin 24))))))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, h, h, h^2] := by rw [hh5]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  rw [hh6]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_8_0 (z h : R) : trM z h (mulNF h (e (8:Fin 24)) (e (0:Fin 24))) = z^2 := by
  have hmul : mulNF h (e (8:Fin 24)) (e (0:Fin 24)) = e (8 : Fin 24) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (8 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  rw [hh0]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_8_1 (z h : R) : trM z h (mulNF h (e (8:Fin 24)) (e (1:Fin 24))) = z^3 := by
  have hmul : mulNF h (e (8:Fin 24)) (e (1:Fin 24)) = mulσ2 h (e (8 : Fin 24)) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (8 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ2 h (e (8 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  rw [hh1]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_8_2 (z h : R) : trM z h (mulNF h (e (8:Fin 24)) (e (2:Fin 24))) = h*z^2 + z := by
  have hmul : mulNF h (e (8:Fin 24)) (e (2:Fin 24)) = mulσ1 h (e (8 : Fin 24)) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (8 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ1 h (e (8 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  rw [hh1]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_8_3 (z h : R) : trM z h (mulNF h (e (8:Fin 24)) (e (3:Fin 24))) = h*z^2 + z := by
  have hmul : mulNF h (e (8:Fin 24)) (e (3:Fin 24)) = mulσ0 h (e (8 : Fin 24)) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (8 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ0 h (e (8 : Fin 24)) = ![0, 0, 1, 0, 0, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  rw [hh1]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_8_4 (z h : R) : trM z h (mulNF h (e (8:Fin 24)) (e (4:Fin 24))) = h*z^3 + z^2 := by
  have hmul : mulNF h (e (8:Fin 24)) (e (4:Fin 24)) = mulσ2 h (mulσ1 h (e (8 : Fin 24))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (8 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ1 h (e (8 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh2 : mulσ2 h (mulσ1 h (e (8 : Fin 24))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  rw [hh2]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_8_5 (z h : R) : trM z h (mulNF h (e (8:Fin 24)) (e (5:Fin 24))) = h*z^3 + z^2 := by
  have hmul : mulNF h (e (8:Fin 24)) (e (5:Fin 24)) = mulσ1 h (mulσ2 h (e (8 : Fin 24))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (8 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ2 h (e (8 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  have hh2 : mulσ1 h (mulσ2 h (e (8 : Fin 24))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  rw [hh2]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_8_6 (z h : R) : trM z h (mulNF h (e (8:Fin 24)) (e (6:Fin 24))) = h*z^3 + z^2 := by
  have hmul : mulNF h (e (8:Fin 24)) (e (6:Fin 24)) = mulσ0 h (mulσ2 h (e (8 : Fin 24))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (8 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ2 h (e (8 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  have hh2 : mulσ0 h (mulσ2 h (e (8 : Fin 24))) = ![0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  rw [hh2]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_8_7 (z h : R) : trM z h (mulNF h (e (8:Fin 24)) (e (7:Fin 24))) = h^2*z^2 + 2*h*z + 1 := by
  have hmul : mulNF h (e (8:Fin 24)) (e (7:Fin 24)) = mulσ1 h (mulσ0 h (e (8 : Fin 24))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (8 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ0 h (e (8 : Fin 24)) = ![0, 0, 1, 0, 0, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  have hh2 : mulσ1 h (mulσ0 h (e (8 : Fin 24))) = ![1, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  rw [hh2]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_8_8 (z h : R) : trM z h (mulNF h (e (8:Fin 24)) (e (8:Fin 24))) = h^2*z^2 + h*z + z^2 := by
  have hmul : mulNF h (e (8:Fin 24)) (e (8:Fin 24)) = mulσ0 h (mulσ1 h (e (8 : Fin 24))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (8 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ1 h (e (8 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh2 : mulσ0 h (mulσ1 h (e (8 : Fin 24))) = ![0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  rw [hh2]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_8_9 (z h : R) : trM z h (mulNF h (e (8:Fin 24)) (e (9:Fin 24))) = h^2*z^3 + h*z^2 + z^3 := by
  have hmul : mulNF h (e (8:Fin 24)) (e (9:Fin 24)) = mulσ1 h (mulσ2 h (mulσ1 h (e (8 : Fin 24)))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (8 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ1 h (e (8 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh2 : mulσ2 h (mulσ1 h (e (8 : Fin 24))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  have hh3 : mulσ1 h (mulσ2 h (mulσ1 h (e (8 : Fin 24)))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0] := by rw [hh2]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  rw [hh3]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_8_10 (z h : R) : trM z h (mulNF h (e (8:Fin 24)) (e (10:Fin 24))) = h^2*z^3 + 2*h*z^2 + z := by
  have hmul : mulNF h (e (8:Fin 24)) (e (10:Fin 24)) = mulσ2 h (mulσ1 h (mulσ0 h (e (8 : Fin 24)))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (8 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ0 h (e (8 : Fin 24)) = ![0, 0, 1, 0, 0, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  have hh2 : mulσ1 h (mulσ0 h (e (8 : Fin 24))) = ![1, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh3 : mulσ2 h (mulσ1 h (mulσ0 h (e (8 : Fin 24)))) = ![0, 1, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0] := by rw [hh2]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  rw [hh3]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_8_11 (z h : R) : trM z h (mulNF h (e (8:Fin 24)) (e (11:Fin 24))) = h^2*z^3 + 2*h*z^2 + z := by
  have hmul : mulNF h (e (8:Fin 24)) (e (11:Fin 24)) = mulσ1 h (mulσ0 h (mulσ2 h (e (8 : Fin 24)))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (8 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ2 h (e (8 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  have hh2 : mulσ0 h (mulσ2 h (e (8 : Fin 24))) = ![0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  have hh3 : mulσ1 h (mulσ0 h (mulσ2 h (e (8 : Fin 24)))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, h, 0, 0, 0, 0, 0, 0] := by rw [hh2]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  rw [hh3]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_8_12 (z h : R) : trM z h (mulNF h (e (8:Fin 24)) (e (12:Fin 24))) = h^2*z^3 + h*z^2 + z^3 := by
  have hmul : mulNF h (e (8:Fin 24)) (e (12:Fin 24)) = mulσ0 h (mulσ2 h (mulσ1 h (e (8 : Fin 24)))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (8 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ1 h (e (8 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh2 : mulσ2 h (mulσ1 h (e (8 : Fin 24))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  have hh3 : mulσ0 h (mulσ2 h (mulσ1 h (e (8 : Fin 24)))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0] := by rw [hh2]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  rw [hh3]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_8_13 (z h : R) : trM z h (mulNF h (e (8:Fin 24)) (e (13:Fin 24))) = h^3*z^2 + h^2*z + 2*h*z^2 + z := by
  have hmul : mulNF h (e (8:Fin 24)) (e (13:Fin 24)) = mulσ0 h (mulσ1 h (mulσ0 h (e (8 : Fin 24)))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (8 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ0 h (e (8 : Fin 24)) = ![0, 0, 1, 0, 0, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  have hh2 : mulσ1 h (mulσ0 h (e (8 : Fin 24))) = ![1, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh3 : mulσ0 h (mulσ1 h (mulσ0 h (e (8 : Fin 24)))) = ![0, 0, 0, 1, 0, 0, 0, h, h, 0, 0, 0, 0, h^2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh2]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  rw [hh3]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_8_14 (z h : R) : trM z h (mulNF h (e (8:Fin 24)) (e (14:Fin 24))) = h^2*z^3 + h*z^2 + z^3 := by
  have hmul : mulNF h (e (8:Fin 24)) (e (14:Fin 24)) = mulσ0 h (mulσ1 h (mulσ2 h (e (8 : Fin 24)))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (8 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ2 h (e (8 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  have hh2 : mulσ1 h (mulσ2 h (e (8 : Fin 24))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh3 : mulσ0 h (mulσ1 h (mulσ2 h (e (8 : Fin 24)))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0] := by rw [hh2]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  rw [hh3]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_8_15 (z h : R) : trM z h (mulNF h (e (8:Fin 24)) (e (15:Fin 24))) = h^3*z^3 + 2*h^2*z^2 + h*z^3 + h*z + z^2 := by
  have hmul : mulNF h (e (8:Fin 24)) (e (15:Fin 24)) = mulσ1 h (mulσ2 h (mulσ1 h (mulσ0 h (e (8 : Fin 24))))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (8 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ0 h (e (8 : Fin 24)) = ![0, 0, 1, 0, 0, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  have hh2 : mulσ1 h (mulσ0 h (e (8 : Fin 24))) = ![1, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh3 : mulσ2 h (mulσ1 h (mulσ0 h (e (8 : Fin 24)))) = ![0, 1, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0] := by rw [hh2]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  have hh4 : mulσ1 h (mulσ2 h (mulσ1 h (mulσ0 h (e (8 : Fin 24))))) = ![0, 0, 0, 0, 0, 1, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, h, 0, 0, 0] := by rw [hh3]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  rw [hh4]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_8_16 (z h : R) : trM z h (mulNF h (e (8:Fin 24)) (e (16:Fin 24))) = h^3*z^3 + h^2*z^2 + 2*h*z^3 + z^2 := by
  have hmul : mulNF h (e (8:Fin 24)) (e (16:Fin 24)) = mulσ0 h (mulσ2 h (mulσ1 h (mulσ0 h (e (8 : Fin 24))))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (8 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ0 h (e (8 : Fin 24)) = ![0, 0, 1, 0, 0, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  have hh2 : mulσ1 h (mulσ0 h (e (8 : Fin 24))) = ![1, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh3 : mulσ2 h (mulσ1 h (mulσ0 h (e (8 : Fin 24)))) = ![0, 1, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0] := by rw [hh2]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  have hh4 : mulσ0 h (mulσ2 h (mulσ1 h (mulσ0 h (e (8 : Fin 24))))) = ![0, 0, 0, 0, 0, 0, 1, 0, 0, 0, h, 0, h, 0, 0, 0, h^2, 0, 0, 0, 0, 0, 0, 0] := by rw [hh3]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  rw [hh4]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_8_17 (z h : R) : trM z h (mulNF h (e (8:Fin 24)) (e (17:Fin 24))) = h^3*z^3 + h^2*z^2 + 2*h*z^3 + z^2 := by
  have hmul : mulNF h (e (8:Fin 24)) (e (17:Fin 24)) = mulσ1 h (mulσ0 h (mulσ2 h (mulσ1 h (e (8 : Fin 24))))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (8 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ1 h (e (8 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh2 : mulσ2 h (mulσ1 h (e (8 : Fin 24))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  have hh3 : mulσ0 h (mulσ2 h (mulσ1 h (e (8 : Fin 24)))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0] := by rw [hh2]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  have hh4 : mulσ1 h (mulσ0 h (mulσ2 h (mulσ1 h (e (8 : Fin 24))))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, h, 0, 0, 0] := by rw [hh3]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  rw [hh4]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_8_18 (z h : R) : trM z h (mulNF h (e (8:Fin 24)) (e (18:Fin 24))) = h^3*z^3 + h^2*z^2 + 2*h*z^3 + z^2 := by
  have hmul : mulNF h (e (8:Fin 24)) (e (18:Fin 24)) = mulσ0 h (mulσ1 h (mulσ2 h (mulσ1 h (e (8 : Fin 24))))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (8 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ1 h (e (8 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh2 : mulσ2 h (mulσ1 h (e (8 : Fin 24))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  have hh3 : mulσ1 h (mulσ2 h (mulσ1 h (e (8 : Fin 24)))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0] := by rw [hh2]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh4 : mulσ0 h (mulσ1 h (mulσ2 h (mulσ1 h (e (8 : Fin 24))))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1] := by rw [hh3]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  rw [hh4]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_8_19 (z h : R) : trM z h (mulNF h (e (8:Fin 24)) (e (19:Fin 24))) = h^3*z^3 + h^2*z^2 + 2*h*z^3 + z^2 := by
  have hmul : mulNF h (e (8:Fin 24)) (e (19:Fin 24)) = mulσ0 h (mulσ1 h (mulσ0 h (mulσ2 h (e (8 : Fin 24))))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (8 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ2 h (e (8 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  have hh2 : mulσ0 h (mulσ2 h (e (8 : Fin 24))) = ![0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  have hh3 : mulσ1 h (mulσ0 h (mulσ2 h (e (8 : Fin 24)))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, h, 0, 0, 0, 0, 0, 0] := by rw [hh2]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh4 : mulσ0 h (mulσ1 h (mulσ0 h (mulσ2 h (e (8 : Fin 24))))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, h, 0] := by rw [hh3]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  rw [hh4]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_8_20 (z h : R) : trM z h (mulNF h (e (8:Fin 24)) (e (20:Fin 24))) = h^4*z^3 + h^3*z^2 + 3*h^2*z^3 + 2*h*z^2 + z^3 := by
  have hmul : mulNF h (e (8:Fin 24)) (e (20:Fin 24)) = mulσ1 h (mulσ0 h (mulσ2 h (mulσ1 h (mulσ0 h (e (8 : Fin 24)))))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (8 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ0 h (e (8 : Fin 24)) = ![0, 0, 1, 0, 0, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  have hh2 : mulσ1 h (mulσ0 h (e (8 : Fin 24))) = ![1, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh3 : mulσ2 h (mulσ1 h (mulσ0 h (e (8 : Fin 24)))) = ![0, 1, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0] := by rw [hh2]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  have hh4 : mulσ0 h (mulσ2 h (mulσ1 h (mulσ0 h (e (8 : Fin 24))))) = ![0, 0, 0, 0, 0, 0, 1, 0, 0, 0, h, 0, h, 0, 0, 0, h^2, 0, 0, 0, 0, 0, 0, 0] := by rw [hh3]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  have hh5 : mulσ1 h (mulσ0 h (mulσ2 h (mulσ1 h (mulσ0 h (e (8 : Fin 24)))))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, h, 0, h, 0, 0, h^2, 0, 0, 0] := by rw [hh4]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  rw [hh5]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_8_21 (z h : R) : trM z h (mulNF h (e (8:Fin 24)) (e (21:Fin 24))) = h^4*z^3 + h^3*z^2 + 3*h^2*z^3 + 2*h*z^2 + z^3 := by
  have hmul : mulNF h (e (8:Fin 24)) (e (21:Fin 24)) = mulσ0 h (mulσ1 h (mulσ2 h (mulσ1 h (mulσ0 h (e (8 : Fin 24)))))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (8 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ0 h (e (8 : Fin 24)) = ![0, 0, 1, 0, 0, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  have hh2 : mulσ1 h (mulσ0 h (e (8 : Fin 24))) = ![1, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh3 : mulσ2 h (mulσ1 h (mulσ0 h (e (8 : Fin 24)))) = ![0, 1, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0] := by rw [hh2]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  have hh4 : mulσ1 h (mulσ2 h (mulσ1 h (mulσ0 h (e (8 : Fin 24))))) = ![0, 0, 0, 0, 0, 1, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, h, 0, 0, 0] := by rw [hh3]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh5 : mulσ0 h (mulσ1 h (mulσ2 h (mulσ1 h (mulσ0 h (e (8 : Fin 24)))))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, h, 0, 0, 0, 0, h] := by rw [hh4]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  rw [hh5]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_8_22 (z h : R) : trM z h (mulNF h (e (8:Fin 24)) (e (22:Fin 24))) = h^4*z^3 + h^3*z^2 + 3*h^2*z^3 + 3*h*z^2 + z := by
  have hmul : mulNF h (e (8:Fin 24)) (e (22:Fin 24)) = mulσ0 h (mulσ1 h (mulσ0 h (mulσ2 h (mulσ1 h (e (8 : Fin 24)))))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (8 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ1 h (e (8 : Fin 24)) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh2 : mulσ2 h (mulσ1 h (e (8 : Fin 24))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  have hh3 : mulσ0 h (mulσ2 h (mulσ1 h (e (8 : Fin 24)))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0] := by rw [hh2]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  have hh4 : mulσ1 h (mulσ0 h (mulσ2 h (mulσ1 h (e (8 : Fin 24))))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, h, 0, 0, 0] := by rw [hh3]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh5 : mulσ0 h (mulσ1 h (mulσ0 h (mulσ2 h (mulσ1 h (e (8 : Fin 24)))))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, h] := by rw [hh4]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  rw [hh5]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

theorem gramval_8_23 (z h : R) : trM z h (mulNF h (e (8:Fin 24)) (e (23:Fin 24))) = h^5*z^3 + h^4*z^2 + 4*h^3*z^3 + 4*h^2*z^2 + 2*h*z^3 + h*z + z^2 := by
  have hmul : mulNF h (e (8:Fin 24)) (e (23:Fin 24)) = mulσ0 h (mulσ1 h (mulσ0 h (mulσ2 h (mulσ1 h (mulσ0 h (e (8 : Fin 24))))))) := by
    funext m; simp [mulNF, e, Pi.single_apply]
  rw [hmul]
  have hh0 : (e (8 : Fin 24) : Fin 24 → R) = ![0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by funext m; fin_cases m <;> simp [e, Pi.single_apply]
  have hh1 : mulσ0 h (e (8 : Fin 24)) = ![0, 0, 1, 0, 0, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh0]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  have hh2 : mulσ1 h (mulσ0 h (e (8 : Fin 24))) = ![1, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by rw [hh1]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh3 : mulσ2 h (mulσ1 h (mulσ0 h (e (8 : Fin 24)))) = ![0, 1, 0, 0, h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, h, 0, 0, 0, 0, 0, 0, 0] := by rw [hh2]; funext m; fin_cases m <;> simp [mulσ2] <;> try ring
  have hh4 : mulσ0 h (mulσ2 h (mulσ1 h (mulσ0 h (e (8 : Fin 24))))) = ![0, 0, 0, 0, 0, 0, 1, 0, 0, 0, h, 0, h, 0, 0, 0, h^2, 0, 0, 0, 0, 0, 0, 0] := by rw [hh3]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  have hh5 : mulσ1 h (mulσ0 h (mulσ2 h (mulσ1 h (mulσ0 h (e (8 : Fin 24)))))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, h, 0, h, 0, 0, h^2, 0, 0, 0] := by rw [hh4]; funext m; fin_cases m <;> simp [mulσ1] <;> try ring
  have hh6 : mulσ0 h (mulσ1 h (mulσ0 h (mulσ2 h (mulσ1 h (mulσ0 h (e (8 : Fin 24))))))) = ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, h, h, h^2] := by rw [hh5]; funext m; fin_cases m <;> simp [mulσ0] <;> try ring
  rw [hh6]
  simp only [trM, TRM, Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.cons_val_zero, Matrix.cons_val_succ]; ring

end QOU.Machinery.H4
