
/-! ### The matrices realise `H₄(q)` -/

theorem A31_inv {q : ℝ} (hq : 0 < q) : A31 q .s1 * A31 q .i1 = 1 ∧ A31 q .s2 * A31 q .i2 = 1 ∧
    A31 q .s3 * A31 q .i3 = 1 := by
  have h1 : q ^ 2 + 1 ≠ 0 := by positivity
  have h2 : q ^ 4 + q ^ 2 + 1 ≠ 0 := by positivity
  have h0 : q ≠ 0 := hq.ne'
  refine ⟨?_, ?_, ?_⟩ <;> ext a c <;> fin_cases a <;> fin_cases c <;>
    simp [A31, Matrix.mul_apply, Fin.sum_univ_succ] <;> field_simp <;> ring

theorem A31_braid {q : ℝ} (hq : 0 < q) :
    A31 q .s1 * A31 q .s2 * A31 q .s1 = A31 q .s2 * A31 q .s1 * A31 q .s2 ∧
    A31 q .s2 * A31 q .s3 * A31 q .s2 = A31 q .s3 * A31 q .s2 * A31 q .s3 ∧
    A31 q .s1 * A31 q .s3 = A31 q .s3 * A31 q .s1 := by
  have h1 : q ^ 2 + 1 ≠ 0 := by positivity
  have h2 : q ^ 4 + q ^ 2 + 1 ≠ 0 := by positivity
  have h0 : q ≠ 0 := hq.ne'
  refine ⟨?_, ?_, ?_⟩ <;> ext a c <;> fin_cases a <;> fin_cases c <;>
    simp [A31, Matrix.mul_apply, Fin.sum_univ_succ] <;> field_simp <;> ring

theorem A22_inv {q : ℝ} (hq : 0 < q) : A22 q .s1 * A22 q .i1 = 1 ∧ A22 q .s2 * A22 q .i2 = 1 ∧
    A22 q .s3 * A22 q .i3 = 1 := by
  have h1 : q ^ 2 + 1 ≠ 0 := by positivity
  have h0 : q ≠ 0 := hq.ne'
  refine ⟨?_, ?_, ?_⟩ <;> ext a c <;> fin_cases a <;> fin_cases c <;>
    simp [A22, Matrix.mul_apply, Fin.sum_univ_succ] <;> field_simp <;> ring

theorem A22_braid {q : ℝ} (hq : 0 < q) :
    A22 q .s1 * A22 q .s2 * A22 q .s1 = A22 q .s2 * A22 q .s1 * A22 q .s2 ∧
    A22 q .s2 * A22 q .s3 * A22 q .s2 = A22 q .s3 * A22 q .s2 * A22 q .s3 ∧
    A22 q .s1 * A22 q .s3 = A22 q .s3 * A22 q .s1 := by
  have h1 : q ^ 2 + 1 ≠ 0 := by positivity
  have h0 : q ≠ 0 := hq.ne'
  refine ⟨?_, ?_, ?_⟩ <;> ext a c <;> fin_cases a <;> fin_cases c <;>
    simp [A22, Matrix.mul_apply, Fin.sum_univ_succ] <;> field_simp <;> ring

/-! ### Assembly -/

/-- Products of the seminormal matrices along a letter list. -/
noncomputable def W31 (q : ℝ) (w : List Vtx) : Matrix (Fin 3) (Fin 3) ℝ := ((letters w).map (A31 q)).prod
noncomputable def W22 (q : ℝ) (w : List Vtx) : Matrix (Fin 2) (Fin 2) ℝ := ((letters w).map (A22 q)).prod
noncomputable def W4 (q : ℝ) (w : List Vtx) : ℝ := ((letters w).map (A4 q)).prod

theorem W4_eq_one {q : ℝ} (hq : q ≠ 0) (w : List Vtx) : W4 q w = 1 := by
  induction w with
  | nil => rfl
  | cons v w ih =>
    unfold W4 letters at *
    cases v <;> simp [List.flatMap_cons, Vtx.letters, A4, ih, hq, mul_assoc]

/-- The perturbation bound gives `‖W − 1‖ ≤ 1` on a pure word in the window. -/
theorem key_bound {n : ℕ} (T : Fin 24 → Matrix (Fin n) (Fin n) ℝ) (P : Fin 3 → Matrix (Fin n) (Fin n) ℝ)
    (A : Gen → Matrix (Fin n) (Fin n) ℝ) (hT0 : T 0 = 1) (hTn : ∀ k, ‖T k‖ ≤ 11 / 6)
    (hstep : ∀ k j, T k * P j = T (nxt k j)) {q : ℝ} (hq : 0 ≤ q - 1)
    (hAP : ∀ g, ‖A g - P g.base‖ ≤ 11 / 10 * (q - 1))
    (l : List Gen) (hl : (l.map (fun g => P g.base)).prod = 1)
    (hsmall : (l.length : ℝ) * (11 / 6) * (11 / 10 * (q - 1)) * (11 / 6 + 1) ≤ 1) :
    ‖(l.map A).prod - 1‖ ≤ 1 := by
  have h1 : (1 : Matrix (Fin n) (Fin n) ℝ) ∈ Set.range T := ⟨0, hT0⟩
  have hS : ∀ g ∈ Set.range T, ‖g‖ ≤ 11 / 6 := by rintro _ ⟨k, rfl⟩; exact hTn k
  have hcl : ∀ g ∈ Set.range T, ∀ x : Gen, g * P x.base ∈ Set.range T := by
    rintro _ ⟨k, rfl⟩ x; exact ⟨nxt k x.base, (hstep k x.base).symm⟩
  have hp := prod_perturb (Set.range T) (fun g => P g.base) A (11 / 6) (11 / 10 * (q - 1))
    (by positivity) h1 hS hcl hAP l 1 h1
  rw [one_mul, one_mul, hl] at hp
  exact hp.trans (perturb_le_one _ _ _ (by norm_num) (by positivity) hsmall)

theorem diag_nonneg_of {n : ℕ} (W : Matrix (Fin n) (Fin n) ℝ) (h : ‖W - 1‖ ≤ 1) (i : Fin n) :
    0 ≤ W i i := by
  have := (abs_entry_le_norm (W - 1) i i).trans h
  simp only [Matrix.sub_apply, Matrix.one_apply_eq] at this
  linarith [neg_abs_le (W i i - 1)]

/-- Diagonal entries of both nontrivial blocks are nonnegative on pure words in the window. -/
theorem diag_nonneg {w : List Vtx} (hw : IsPure w) (hm : w ≠ []) {q : ℝ} (h0 : 1 ≤ q)
    (h1 : q ≤ 1 + (1 / 12) / w.length) :
    (∀ i, 0 ≤ W31 q w i i) ∧ (∀ i, 0 ≤ W22 q w i i) := by
  have hmpos : (0 : ℝ) < w.length := by
    have := List.length_pos_of_ne_nil hm; exact_mod_cast this
  have hm1 : (1 : ℝ) ≤ w.length := by
    have := List.length_pos_of_ne_nil hm; exact_mod_cast this
  have hmq : (w.length : ℝ) * (q - 1) ≤ 1 / 12 := by
    have : q - 1 ≤ (1 / 12) / w.length := by linarith
    rw [le_div_iff₀ hmpos] at this; linarith
  have h11 : q ≤ 11 / 10 := by
    have : (1 / 12 : ℝ) / w.length ≤ 1 / 12 := div_le_self (by norm_num) hm1
    linarith
  have hq : 0 ≤ q - 1 := by linarith
  obtain ⟨k, hF, h31, h22⟩ := joint (letters w)
  have hk : k = 0 := by
    apply F_eq_id
    rw [← hF]; unfold IsPure wordPerm at hw; rw [hw]; rfl
  subst hk
  have hsmall : ((letters w).length : ℝ) * (11 / 6) * (11 / 10 * (q - 1)) * (11 / 6 + 1) ≤ 1 := by
    rw [letters_length]; push_cast; nlinarith
  refine ⟨fun i => diag_nonneg_of _ ?_ i, fun i => diag_nonneg_of _ ?_ i⟩
  · exact key_bound T31 P31 (A31 q) T31_zero T31_norm T31_step hq (A31_sub_P31 h0 h11) _
      (h31.trans T31_zero) hsmall
  · exact key_bound T22 P22 (A22 q) T22_zero T22_norm T22_step hq (A22_sub_P22 h0 h11) _
      (h22.trans T22_zero) hsmall

/-! ### Level characters -/

/-- Symmetric `q`-integer `[n]_q = Σ_{k<n} q^{n−1−2k}`. -/
noncomputable def qint (n : ℕ) (q : ℝ) : ℝ := ∑ k ∈ Finset.range n, q ^ ((n : ℤ) - 1 - 2 * k)

/-- Convention-D Markov weight of the two-row shape `(a, b)`: `[a − b + 1]_q / [2]_q^{a+b}`. -/
noncomputable def yw (q : ℝ) (a b : ℕ) : ℝ := qint (a - b + 1) q / qint 2 q ^ (a + b)

theorem qint_pos {q : ℝ} (hq : 0 < q) {n : ℕ} (hn : 0 < n) : 0 < qint n q :=
  Finset.sum_pos (fun _ _ => zpow_pos hq _) (Finset.nonempty_range_iff.mpr (by omega))

theorem yw_pos {q : ℝ} (hq : 0 < q) (a b : ℕ) : 0 < yw q a b :=
  div_pos (qint_pos hq (by omega)) (pow_pos (qint_pos hq (by norm_num)) _)

/-- The eight level characters (levels 1–4, two-row shapes). -/
inductive LevelShape
  | l4_4 | l4_31 | l4_22 | l3_3 | l3_21 | l2_2 | l2_11 | l1_1

/-- Level character `χ_{(m,μ)}(w) = Σ_λ (y_λ / y_μ) Σ_{T ↓ m = μ} W^λ_{TT}`, with the
Gelfand–Tsetlin tableaux ordered as in the seminormal matrices: on `(3,1)` the entry `4`, `3`, `2`
sits in the second row; on `(2,2)` the second row is `{3,4}`, then `{2,4}`. -/
noncomputable def levelChar (q : ℝ) (w : List Vtx) : LevelShape → ℝ
  | .l4_4 => W4 q w
  | .l4_31 => W31 q w 0 0 + W31 q w 1 1 + W31 q w 2 2
  | .l4_22 => W22 q w 0 0 + W22 q w 1 1
  | .l3_3 => yw q 4 0 / yw q 3 0 * W4 q w + yw q 3 1 / yw q 3 0 * W31 q w 0 0
  | .l3_21 => yw q 3 1 / yw q 2 1 * (W31 q w 1 1 + W31 q w 2 2) +
      yw q 2 2 / yw q 2 1 * (W22 q w 0 0 + W22 q w 1 1)
  | .l2_2 => yw q 4 0 / yw q 2 0 * W4 q w + yw q 3 1 / yw q 2 0 * (W31 q w 0 0 + W31 q w 1 1) +
      yw q 2 2 / yw q 2 0 * W22 q w 0 0
  | .l2_11 => yw q 3 1 / yw q 1 1 * W31 q w 2 2 + yw q 2 2 / yw q 1 1 * W22 q w 1 1
  | .l1_1 => yw q 4 0 / yw q 1 0 * W4 q w +
      yw q 3 1 / yw q 1 0 * (W31 q w 0 0 + W31 q w 1 1 + W31 q w 2 2) +
      yw q 2 2 / yw q 1 0 * (W22 q w 0 0 + W22 q w 1 1)

/-- **Main theorem.** Every pure γγ word of length `m ≥ 1` on four strands passes reading 3
(all level characters `≥ 0`) for `1 ≤ q ≤ 1 + (1/12)/m`. -/
theorem pure_gg_reading3 {w : List Vtx} (hw : IsPure w) (hm : w ≠ []) {q : ℝ} (h0 : 1 ≤ q)
    (h1 : q ≤ 1 + (1 / 12) / w.length) (s : LevelShape) : 0 ≤ levelChar q w s := by
  obtain ⟨d31, d22⟩ := diag_nonneg hw hm h0 h1
  have hq : 0 < q := by linarith
  have h4 : W4 q w = 1 := W4_eq_one hq.ne' w
  have p : ∀ a b c d : ℕ, 0 ≤ yw q a b / yw q c d :=
    fun a b c d => (div_pos (yw_pos hq a b) (yw_pos hq c d)).le
  have a0 := d31 0; have a1 := d31 1; have a2 := d31 2; have b0 := d22 0; have b1 := d22 1
  cases s <;> simp only [levelChar, h4]
  · norm_num
  · linarith
  · linarith
  · exact add_nonneg (mul_nonneg (p 4 0 3 0) zero_le_one) (mul_nonneg (p 3 1 3 0) a0)
  · exact add_nonneg (mul_nonneg (p 3 1 2 1) (by linarith)) (mul_nonneg (p 2 2 2 1) (by linarith))
  · exact add_nonneg (add_nonneg (mul_nonneg (p 4 0 2 0) zero_le_one)
      (mul_nonneg (p 3 1 2 0) (by linarith))) (mul_nonneg (p 2 2 2 0) b0)
  · exact add_nonneg (mul_nonneg (p 3 1 1 1) a2) (mul_nonneg (p 2 2 1 1) b1)
  · exact add_nonneg (add_nonneg (mul_nonneg (p 4 0 1 0) zero_le_one)
      (mul_nonneg (p 3 1 1 0) (by linarith))) (mul_nonneg (p 2 2 1 0) (by linarith))

end QOU.QuarkState.GammaGammaFourStrandPureBound
