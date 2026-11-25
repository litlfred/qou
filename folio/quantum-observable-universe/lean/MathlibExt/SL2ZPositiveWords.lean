import Mathlib.LinearAlgebra.Matrix.SpecialLinearGroup
import Mathlib.Tactic

/-!
# Positive `R`/`L` words in `SL(2, ℤ)`

Let `R = !![1, 1; 0, 1]` and `L = !![1, 0; 1, 1]` in `SL(2, ℤ)`, and let
`posProd u` be the product of the letters of a word `u : List Bool`
(`true ↦ R`, `false ↦ L`), read left to right.

We prove two classical facts:

* `exists_posProd_of_nonneg`: every matrix in `SL(2, ℤ)` with all entries
  non-negative is `posProd u` for some word `u` (Euclidean descent on the
  sum of the entries);
* `exists_conj_posProd`: every matrix in `SL(2, ℤ)` with trace `> 2`
  (a hyperbolic element) is conjugate to `posProd u` for some word `u`.

The second is the classical statement that hyperbolic conjugacy classes of
`SL(2, ℤ)` have positive `R`/`L` representatives. The proof picks a
conjugate minimising `|c|` (the lower-left entry), normalises `|a - d| ≤ |c|`
by conjugating with a power of `R`, and uses conjugation by
`S = !![0, -1; 1, 0]` to get `|c| ≤ |b|`; a trace estimate then forces
either the conjugate or its `S`-conjugate to be non-negative.
-/

namespace QOU.MathlibExt.SL2Z

open Matrix

/-- The upper unipotent generator `R = !![1, 1; 0, 1]`. -/
def R : SpecialLinearGroup (Fin 2) ℤ :=
  ⟨!![1, 1; 0, 1], by norm_num [Matrix.det_fin_two_of]⟩

/-- The lower unipotent generator `L = !![1, 0; 1, 1]`. -/
def L : SpecialLinearGroup (Fin 2) ℤ :=
  ⟨!![1, 0; 1, 1], by norm_num [Matrix.det_fin_two_of]⟩

/-- The product of a positive word: `true ↦ R`, `false ↦ L`. -/
def posProd : List Bool → SpecialLinearGroup (Fin 2) ℤ
  | [] => 1
  | true :: u => R * posProd u
  | false :: u => L * posProd u

@[simp] lemma posProd_nil : posProd [] = 1 := rfl
@[simp] lemma posProd_cons_true (u : List Bool) : posProd (true :: u) = R * posProd u := rfl
@[simp] lemma posProd_cons_false (u : List Bool) : posProd (false :: u) = L * posProd u := rfl

lemma det_entries (M : SpecialLinearGroup (Fin 2) ℤ) :
    M 0 0 * M 1 1 - M 0 1 * M 1 0 = 1 := by
  have h := M.det_coe
  rw [Matrix.det_fin_two] at h
  exact h

/-- Euclidean descent, bounded form. -/
lemma exists_posProd_of_nonneg_aux (n : ℕ) :
    ∀ M : SpecialLinearGroup (Fin 2) ℤ, (∀ i j, 0 ≤ M i j) →
      M 0 0 + M 0 1 + M 1 0 + M 1 1 ≤ n → ∃ u, posProd u = M := by
  induction n with
  | zero =>
    intro M hM hs
    have h := det_entries M
    have h00 := hM 0 0; have h01 := hM 0 1; have h10 := hM 1 0; have h11 := hM 1 1
    push_cast at hs
    nlinarith
  | succ n ih =>
    intro M hM hs
    have h := det_entries M
    have h00 := hM 0 0; have h01 := hM 0 1; have h10 := hM 1 0; have h11 := hM 1 1
    push_cast at hs
    by_cases hbc : M 0 1 = 0 ∧ M 1 0 = 0
    · obtain ⟨hb, hc⟩ := hbc
      rw [hb, hc] at h
      have h' : M 0 0 * M 1 1 = 1 := by linarith
      have ha : M 0 0 = 1 := Int.eq_one_of_mul_eq_one_right h00 h'
      have hd : M 1 1 = 1 := Int.eq_one_of_mul_eq_one_left h11 h'
      refine ⟨[], ?_⟩
      ext i j
      fin_cases i <;> fin_cases j <;> simp [ha, hb, hc, hd]
    by_cases hA : M 1 0 ≤ M 0 0 ∧ M 1 1 ≤ M 0 1
    · obtain ⟨hA1, hA2⟩ := hA
      have hcd : 1 ≤ M 1 0 + M 1 1 := by
        by_contra hlt
        have hc : M 1 0 = 0 := by omega
        have hd : M 1 1 = 0 := by omega
        rw [hc, hd] at h
        simp at h
      let M' : SpecialLinearGroup (Fin 2) ℤ :=
        ⟨!![M 0 0 - M 1 0, M 0 1 - M 1 1; M 1 0, M 1 1], by
          rw [Matrix.det_fin_two_of]; linarith⟩
      have hM' : ∀ i j, 0 ≤ M' i j := by
        intro i j
        fin_cases i <;> fin_cases j <;> simp [M'] <;> omega
      obtain ⟨u, hu⟩ := ih M' hM' (by simp [M']; omega)
      refine ⟨true :: u, ?_⟩
      rw [posProd_cons_true, hu]
      ext i j
      rw [SpecialLinearGroup.coe_mul]
      fin_cases i <;> fin_cases j <;>
        simp [R, M', Matrix.mul_apply, Fin.sum_univ_two]
    by_cases hB : M 0 0 ≤ M 1 0 ∧ M 0 1 ≤ M 1 1
    · obtain ⟨hB1, hB2⟩ := hB
      have hab : 1 ≤ M 0 0 + M 0 1 := by
        by_contra hlt
        have ha : M 0 0 = 0 := by omega
        have hb : M 0 1 = 0 := by omega
        rw [ha, hb] at h
        simp at h
      let M' : SpecialLinearGroup (Fin 2) ℤ :=
        ⟨!![M 0 0, M 0 1; M 1 0 - M 0 0, M 1 1 - M 0 1], by
          rw [Matrix.det_fin_two_of]; linarith⟩
      have hM' : ∀ i j, 0 ≤ M' i j := by
        intro i j
        fin_cases i <;> fin_cases j <;> simp [M'] <;> omega
      obtain ⟨u, hu⟩ := ih M' hM' (by simp [M']; omega)
      refine ⟨false :: u, ?_⟩
      rw [posProd_cons_false, hu]
      ext i j
      rw [SpecialLinearGroup.coe_mul]
      fin_cases i <;> fin_cases j <;>
        simp [L, M', Matrix.mul_apply, Fin.sum_univ_two]
    -- mixed cases are impossible
    exfalso
    rcases lt_or_ge (M 0 0) (M 1 0) with hac | hca
    · have hbd : M 1 1 < M 0 1 := by
        by_contra hh; exact hB ⟨hac.le, by omega⟩
      nlinarith
    · have hdb : M 0 1 < M 1 1 := by
        by_contra hh; exact hA ⟨hca, by omega⟩
      have hca' : M 1 0 < M 0 0 := by
        by_contra hh; exact hB ⟨by omega, hdb.le⟩
      have : M 0 1 + M 1 0 = 0 := by nlinarith
      exact hbc ⟨by omega, by omega⟩

/-- Every non-negative matrix in `SL(2, ℤ)` is a positive word in `R` and `L`. -/
theorem exists_posProd_of_nonneg (M : SpecialLinearGroup (Fin 2) ℤ)
    (hM : ∀ i j, 0 ≤ M i j) : ∃ u : List Bool, posProd u = M :=
  exists_posProd_of_nonneg_aux (M 0 0 + M 0 1 + M 1 0 + M 1 1).toNat M hM
    (Int.self_le_toNat _)

/-! ### Hyperbolic classes -/

/-- The rotation `S = !![0, -1; 1, 0]`. -/
def S : SpecialLinearGroup (Fin 2) ℤ :=
  ⟨!![0, -1; 1, 0], by norm_num [Matrix.det_fin_two_of]⟩

/-- The upper unipotent `T k = !![1, k; 0, 1]` (so `T 1 = R`). -/
def T (k : ℤ) : SpecialLinearGroup (Fin 2) ℤ :=
  ⟨!![1, k; 0, 1], by norm_num [Matrix.det_fin_two_of]⟩

lemma S_conj_apply (N : SpecialLinearGroup (Fin 2) ℤ) :
    (S * N * S⁻¹) 0 0 = N 1 1 ∧ (S * N * S⁻¹) 0 1 = -N 1 0 ∧
      (S * N * S⁻¹) 1 0 = -N 0 1 ∧ (S * N * S⁻¹) 1 1 = N 0 0 := by
  refine ⟨?_, ?_, ?_, ?_⟩ <;>
    rw [SpecialLinearGroup.coe_mul, SpecialLinearGroup.coe_mul, SpecialLinearGroup.coe_inv] <;>
    simp [S, SpecialLinearGroup.coe_inv, Matrix.adjugate_fin_two, Matrix.mul_apply,
      Matrix.vecMul, dotProduct, Fin.sum_univ_two]

lemma T_conj_apply (k : ℤ) (N : SpecialLinearGroup (Fin 2) ℤ) :
    (T k * N * (T k)⁻¹) 0 0 = N 0 0 + k * N 1 0 ∧
      (T k * N * (T k)⁻¹) 0 1 = N 0 1 + k * N 1 1 - k * (N 0 0 + k * N 1 0) ∧
      (T k * N * (T k)⁻¹) 1 0 = N 1 0 ∧ (T k * N * (T k)⁻¹) 1 1 = N 1 1 - k * N 1 0 := by
  refine ⟨?_, ?_, ?_, ?_⟩ <;>
    rw [SpecialLinearGroup.coe_mul, SpecialLinearGroup.coe_mul, SpecialLinearGroup.coe_inv] <;>
    simp [T, SpecialLinearGroup.coe_inv, Matrix.adjugate_fin_two, Matrix.mul_apply,
      Matrix.vecMul, dotProduct, Fin.sum_univ_two] <;> ring

lemma trace_conj (g N : SpecialLinearGroup (Fin 2) ℤ) :
    (g * N * g⁻¹) 0 0 + (g * N * g⁻¹) 1 1 = N 0 0 + N 1 1 := by
  have h : ((g * N * g⁻¹ : SpecialLinearGroup (Fin 2) ℤ) : Matrix (Fin 2) (Fin 2) ℤ).trace =
      (N : Matrix (Fin 2) (Fin 2) ℤ).trace := by
    rw [SpecialLinearGroup.coe_mul, SpecialLinearGroup.coe_mul, Matrix.trace_mul_comm,
      ← Matrix.mul_assoc, ← SpecialLinearGroup.coe_mul, inv_mul_cancel,
      SpecialLinearGroup.coe_one, Matrix.one_mul]
  rwa [Matrix.trace_fin_two, Matrix.trace_fin_two] at h

/-- For `c ≠ 0`, some shift `x + 2 k c` lands in `[-|c|, |c|]`. -/
lemma exists_shift (c : ℤ) (hc : c ≠ 0) (x : ℤ) : ∃ k : ℤ, |x + 2 * k * c| ≤ |c| := by
  have hpos : 0 < |c| := abs_pos.mpr hc
  have hm : 0 < 2 * |c| := by linarith
  have h1 := Int.emod_add_mul_ediv (x + |c|) (2 * |c|)
  have h2 := Int.emod_nonneg (x + |c|) hm.ne'
  have h3 := Int.emod_lt_of_pos (x + |c|) hm
  generalize (x + |c|) % (2 * |c|) = r at h1 h2 h3
  generalize (x + |c|) / (2 * |c|) = q at h1
  rcases lt_or_gt_of_ne hc with hneg | hpos'
  · have hac : |c| = -c := abs_of_neg hneg
    rw [hac] at h1 h3
    refine ⟨q, ?_⟩
    rw [hac, abs_le]; constructor <;> nlinarith
  · have hac : |c| = c := abs_of_pos hpos'
    rw [hac] at h1 h3
    refine ⟨-q, ?_⟩
    rw [hac, abs_le]; constructor <;> nlinarith

/-- The arithmetic core: a reduced hyperbolic matrix has a definite sign pattern. -/
lemma reduced_sign (a b c d : ℤ) (hdet : a * d - b * c = 1) (ht : 2 < a + d)
    (hc : c ≠ 0) (had : |a - d| ≤ |c|) (hcb : |c| ≤ |b|) :
    (0 < a ∧ 0 < b ∧ 0 < c ∧ 0 < d) ∨ (0 < a ∧ b < 0 ∧ c < 0 ∧ 0 < d) := by
  have h1 : (a - d) ^ 2 ≤ c ^ 2 := sq_le_sq.mpr (by simpa using had)
  have h9 : 9 ≤ (a + d) ^ 2 := by nlinarith
  have hb : b ≠ 0 := by
    rintro rfl
    simp only [abs_zero] at hcb
    exact hc (abs_nonpos_iff.mp hcb)
  have hpos_ad : ∀ bc : ℤ, b * c = bc → 0 < bc → 0 < a ∧ 0 < d := by
    intro bc hbc hbc0
    have had' : 0 < a * d := by linarith
    constructor
    · by_contra hh; push_neg at hh; nlinarith
    · by_contra hh; push_neg at hh; nlinarith
  rcases lt_or_gt_of_ne hc with hcn | hcp <;> rcases lt_or_gt_of_ne hb with hbn | hbp
  · right
    obtain ⟨ha, hd⟩ := hpos_ad _ rfl (mul_pos_of_neg_of_neg hbn hcn)
    exact ⟨ha, hbn, hcn, hd⟩
  · exfalso
    rw [abs_of_neg hcn, abs_of_pos hbp] at hcb
    nlinarith [mul_nonpos_of_nonneg_of_nonpos (sub_nonneg.2 hcb) hcn.le]
  · exfalso
    rw [abs_of_pos hcp, abs_of_neg hbn] at hcb
    nlinarith [mul_nonneg (sub_nonneg.2 hcb) hcp.le]
  · left
    obtain ⟨ha, hd⟩ := hpos_ad _ rfl (mul_pos hbp hcp)
    exact ⟨ha, hbp, hcp, hd⟩

/-- **Hyperbolic classes have positive representatives.** Every element of
`SL(2, ℤ)` with trace `> 2` is conjugate to a positive word in `R` and `L`. -/
theorem exists_conj_posProd (M : SpecialLinearGroup (Fin 2) ℤ)
    (hM : 2 < (M : Matrix (Fin 2) (Fin 2) ℤ).trace) :
    ∃ u : List Bool, IsConj M (posProd u) := by
  classical
  have htr : 2 < M 0 0 + M 1 1 := by rwa [Matrix.trace_fin_two] at hM
  have htrc : ∀ N, IsConj M N → N 0 0 + N 1 1 = M 0 0 + M 1 1 := by
    intro N hN
    obtain ⟨g, rfl⟩ := isConj_iff.mp hN
    exact trace_conj g M
  have hex : ∃ k : ℕ, ∃ N, IsConj M N ∧ (N 1 0).natAbs = k := ⟨_, M, IsConj.refl M, rfl⟩
  obtain ⟨N0, hN0, hk0⟩ := Nat.find_spec hex
  have hmin : ∀ N, IsConj M N → Nat.find hex ≤ (N 1 0).natAbs :=
    fun N hN => Nat.find_min' hex ⟨N, hN, rfl⟩
  -- the lower-left entry of a hyperbolic matrix is non-zero
  have hc_ne : ∀ N : SpecialLinearGroup (Fin 2) ℤ, 2 < N 0 0 + N 1 1 → N 1 0 ≠ 0 := by
    intro N hN hc
    have h := det_entries N
    rw [hc, mul_zero, sub_zero] at h
    rcases Int.eq_one_or_neg_one_of_mul_eq_one h with ha | ha
    · rw [ha, one_mul] at h; rw [ha, h] at hN; norm_num at hN
    · rw [ha] at h
      have hd : N 1 1 = -1 := by linarith
      rw [ha, hd] at hN; norm_num at hN
  have hc0 : N0 1 0 ≠ 0 := hc_ne N0 (by rw [htrc N0 hN0]; exact htr)
  obtain ⟨k, hk⟩ := exists_shift (N0 1 0) hc0 (N0 0 0 - N0 1 1)
  obtain ⟨e00, e01, e10, e11⟩ := T_conj_apply k N0
  set N1 := T k * N0 * (T k)⁻¹ with hN1def
  have hN1 : IsConj M N1 := hN0.trans (isConj_iff.mpr ⟨T k, rfl⟩)
  obtain ⟨s00, s01, s10, s11⟩ := S_conj_apply N1
  have hN2 : IsConj M (S * N1 * S⁻¹) := hN1.trans (isConj_iff.mpr ⟨S, rfl⟩)
  have hcb : |N1 1 0| ≤ |N1 0 1| := by
    have h := hmin _ hN2
    rw [s10, Int.natAbs_neg, ← hk0, ← e10] at h
    zify at h
    simpa using h
  have had : |N1 0 0 - N1 1 1| ≤ |N1 1 0| := by
    rw [e00, e11, e10]
    convert hk using 2
    ring
  have htr1 : 2 < N1 0 0 + N1 1 1 := by rw [htrc N1 hN1]; exact htr
  rcases reduced_sign _ _ _ _ (det_entries N1) htr1 (hc_ne N1 htr1) had hcb with
    ⟨ha, hb, hc, hd⟩ | ⟨ha, hb, hc, hd⟩
  · obtain ⟨u, hu⟩ := exists_posProd_of_nonneg N1 (by
      intro i j
      fin_cases i <;> fin_cases j <;> simp only [Fin.zero_eta, Fin.mk_one, Fin.isValue] <;> omega)
    exact ⟨u, hu ▸ hN1⟩
  · obtain ⟨u, hu⟩ := exists_posProd_of_nonneg (S * N1 * S⁻¹) (by
      intro i j
      fin_cases i <;> fin_cases j <;>
        simp only [Fin.zero_eta, Fin.mk_one, Fin.isValue, s00, s01, s10, s11] <;> omega)
    exact ⟨u, hu ▸ hN2⟩

end QOU.MathlibExt.SL2Z
