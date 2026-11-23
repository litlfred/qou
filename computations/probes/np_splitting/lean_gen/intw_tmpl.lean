--WORD--
theorem PN_letter (q : R) (hq : q ≠ 0) (l : Letter) : PN q * glSRC q l = glDST q l * PN q := by
  obtain ⟨i, b⟩ := l
  fin_cases i <;> cases b <;> simp only [glSRC, glDST] <;>
    first
    | exact PN_g0 q hq | exact PN_g1 q hq | exact PN_g2 q hq
    | exact PN_g0i q hq | exact PN_g1i q hq | exact PN_g2i q hq

theorem PN_word (q : R) (hq : q ≠ 0) (w : List Letter) :
    PN q * wordSRC q w = wordDST q w * PN q := by
  induction w with
  | nil => simp [wordSRC, wordDST]
  | cons l w ih =>
    simp only [wordSRC, wordDST]
    rw [← Matrix.mul_assoc, PN_letter q hq l, Matrix.mul_assoc, ih, Matrix.mul_assoc]
--WORD--
set_option maxHeartbeats 4000000 in
theorem M1_eq (q : R) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) : M1 q = P21 q * N21 q := by matTac
set_option maxHeartbeats 4000000 in
theorem M2_eq (q : R) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) :
    M2 q = P32 q * N32 q - N21 q * P21 q := by matTac
set_option maxHeartbeats 4000000 in
theorem M3_eq (q : R) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) : M3 q = -(N32 q * P32 q) := by matTac

/-- `tn − q⁻² tp` is a sum of weighted block traces. -/
theorem phi_eq_traces (q : R) (hq : q ≠ 0) (W1 W3 : Matrix (Fin 4) (Fin 4) R)
    (W2 : Matrix (Fin 6) (Fin 6) R) :
    tnL q W1 W3 W2 - q⁻¹ ^ 2 * tpL q W1 W3 W2
      = trace (M1 q * W1) + trace (M2 q * W2) + trace (M3 q * W3) := by
  simp only [tnL, tpL, M1, M2, M3, Matrix.trace, Matrix.diag, Matrix.diagonal_mul,
    Fin.sum_univ_four, Fin.sum_univ_six]
  simp
  field_simp
  ring

/-- **Left placement keeps the ratio, for every word.** With the nucleon on strands `0–2`
and the ruled functional, `E_n = q⁻² · E_p` for every braid word on four strands. -/
theorem left_ratio (q : R) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) (w : List Letter) :
    tnL q (word1 q w) (word3 q w) (word2 q w)
      = q⁻¹ ^ 2 * tpL q (word1 q w) (word3 q w) (word2 q w) := by
  have key := phi_eq_traces q hq (word1 q w) (word3 q w) (word2 q w)
  have i21 := P21_word q hq w
  have i32 := P32_word q hq w
  have t1 : trace (P21 q * N21 q * word1 q w) = trace (N21 q * P21 q * word2 q w) := by
    rw [Matrix.trace_mul_cycle, ← i21, Matrix.trace_mul_cycle]
  have t2 : trace (P32 q * N32 q * word2 q w) = trace (N32 q * P32 q * word3 q w) := by
    rw [Matrix.trace_mul_cycle, ← i32, Matrix.trace_mul_cycle]
  rw [M1_eq q hq h2, M2_eq q hq h2, M3_eq q hq h2, Matrix.sub_mul, Matrix.trace_sub,
    Matrix.neg_mul, Matrix.trace_neg, t1, t2] at key
  linear_combination key
