import QOU.BraidsAndKnots.NucleonWeightSpaceTwoTerm

/-!
# Braid covariance of the pairwise electromagnetic insertions on the nucleon weight spaces

Setting as in `NucleonWeightSpaceTraces` / `NucleonWeightSpaceTwoTerm`: the Hecke action
`A₁, A₂` (resp. `B₁, B₂`) of `σ₁, σ₂` on the proton-type `(2,1)` (resp. neutron-type `(1,2)`)
weight space of `(C²)^{⊗3}`, over a generic field `R`.

An insertion `O` is **braid-covariant** when it commutes with both crossing generators.
This file proves:

* **T1** (`commutant_A_iff`, `commutant_B_iff`). The commutant of `{A₁, A₂}` is exactly
  `span{1, M}` with `M` explicit (`q ≠ 0` only). The same set is the commutant of `{B₁, B₂}`.
  Equivalently `span{1, N}` where `N = M + q • 1`, `N_{ij} = q^{i+j-3}`, is the rank-one
  operator on the trivial `(3)` summand (`N * A_i = q • N`).
* **T2** (`QAdjp_not_comm_A₁`, …). The adjacent insertion `Q₁₂ + Q₂₃` commutes with neither
  crossing generator, on either weight space, so it lies outside the commutant.
* **T3** (`trace_QAdjp_eq_neg_Q13p`). On `(2,1)`, `tr((Q₁₂ + Q₂₃) X) = -tr(Q₁₃ X)` for every
  matrix `X` (every word, positive or not, including the Borromean `V³`): the whole proton
  adjacent signal is minus the dropped pair `1–3`.
* **T4** (`covariant_trace`, `covariant_trace_diff_word`). A covariant insertion contributes
  `a · tr(w) + b · q^{|w|} · tr N` on a positive word; the `n − p` difference of any two
  covariant insertions depends on the word only through `tr(w)` and `q^{|w|}`.
* **T5** (`P3`, `P21`, `E`). The isotypic idempotents `P_(3) = (q³/(q⁴+q²+1)) • N`,
  `P_(2,1) = 1 - P_(3)`, the trace-preserving expectation
  `E(Q) = tr(Q P_(3)) • P_(3) + (tr(Q P_(2,1))/2) • P_(2,1)` onto the commutant: `E` lands in
  the commutant, is idempotent, preserves the trace, and fixes covariant insertions.
* **T6** (`E_QPairP`, `E_QPairN`, `E_QPair_Mcoeff_zero`, `trace_twoTerm_E_QPair_diff_word`).
  For the permutation-complete pairwise insertion `Q_pair` the expectation gives `0` on
  `(2,1)` and `(-1/3) • 1` on `(1,2)`: the `M`-coefficient is exactly `0`, and the two-term
  splitting is `(q⁻¹ - q - c_em/3) · tr(w)`, word-independent apart from `tr(w)`.
  By contrast `E(Q₁₂ + Q₂₃)` has `M`-coefficient `q³(q²-1)²/(3(q⁴+q²+1)²)` on `(2,1)`
  (`E_QAdjp_eq`), nonzero off `q² = 1`: a nonzero `M` term arises only from a pair subset.

No numerical value enters.
-/

namespace QOU.BraidsAndKnots.NucleonQEDCovariance

open Matrix
open QOU.BraidsAndKnots.NucleonWeightSpaceTraces
open QOU.BraidsAndKnots.NucleonWeightSpaceTwoTerm

variable {R : Type*} [Field R]

/-! ## 0. The commutant generators `M` and `N` -/

/-- The non-scalar generator of the commutant of `{A₁, A₂}` on `(2,1)`. -/
def M (q : R) : Matrix (Fin 3) (Fin 3) R :=
  !![-q + q⁻¹ ^ 3, q⁻¹ ^ 2, q⁻¹; q⁻¹ ^ 2, -q + q⁻¹, 1; q⁻¹, 1, 0]

/-- `N_{ij} = q^{i+j-3}`: the rank-one operator on the trivial `(3)` summand. -/
def N (q : R) : Matrix (Fin 3) (Fin 3) R :=
  !![q⁻¹ ^ 3, q⁻¹ ^ 2, q⁻¹; q⁻¹ ^ 2, q⁻¹, 1; q⁻¹, 1, q]

theorem M_eq_N_sub (q : R) : M q = N q - q • (1 : Matrix (Fin 3) (Fin 3) R) := by
  ext i j; fin_cases i <;> fin_cases j <;> simp [M, N, Matrix.one_apply] <;> ring

theorem N_mul_A₁ (q : R) (hq : q ≠ 0) : N q * A₁ q = q • N q := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [N, A₁, Matrix.mul_apply, Fin.sum_univ_three] <;> field_simp <;> ring

theorem N_mul_A₂ (q : R) (hq : q ≠ 0) : N q * A₂ q = q • N q := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [N, A₂, Matrix.mul_apply, Fin.sum_univ_three] <;> field_simp <;> ring

theorem A₁_mul_N (q : R) (hq : q ≠ 0) : A₁ q * N q = q • N q := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [N, A₁, Matrix.mul_apply, Fin.sum_univ_three] <;> field_simp <;> ring

theorem A₂_mul_N (q : R) (hq : q ≠ 0) : A₂ q * N q = q • N q := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [N, A₂, Matrix.mul_apply, Fin.sum_univ_three] <;> field_simp <;> ring

theorem N_mul_A₁Inv (q : R) (hq : q ≠ 0) : N q * A₁Inv q = q⁻¹ • N q := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [N, A₁Inv, Matrix.mul_apply, Fin.sum_univ_three] <;> field_simp <;> ring

theorem N_mul_A₂Inv (q : R) (hq : q ≠ 0) : N q * A₂Inv q = q⁻¹ • N q := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [N, A₂Inv, Matrix.mul_apply, Fin.sum_univ_three] <;> field_simp <;> ring

theorem N_mul_N (q : R) (hq : q ≠ 0) : N q * N q = (q⁻¹ ^ 3 + q⁻¹ + q) • N q := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [N, Matrix.mul_apply, Fin.sum_univ_three] <;> field_simp <;> ring

theorem trace_N (q : R) : trace (N q) = q⁻¹ ^ 3 + q⁻¹ + q := by
  simp [N, Matrix.trace_fin_three] <;> ring

/-- `B₁ = A₂` and `B₂ = A₁` entrywise. -/
theorem B₁_eq_A₂ (q : R) : B₁ q = A₂ q := rfl
theorem B₂_eq_A₁ (q : R) : B₂ q = A₁ q := rfl

/-- `P(q)` commutes with `N` (the trivial-summand operator is the same on both weight spaces). -/
theorem P_mul_N (q : R) (hq : q ≠ 0) : P q * N q = N q * P q := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [P, N, Matrix.mul_apply, Fin.sum_univ_three] <;> field_simp <;> ring

/-! ## T1. The commutant of `{A₁, A₂}` is `span{1, M}` -/

theorem M_comm_A₁ (q : R) (hq : q ≠ 0) : M q * A₁ q = A₁ q * M q := by
  rw [M_eq_N_sub, Matrix.sub_mul, Matrix.mul_sub, N_mul_A₁ q hq, A₁_mul_N q hq,
    Matrix.smul_mul, Matrix.mul_smul, Matrix.one_mul, Matrix.mul_one]

theorem M_comm_A₂ (q : R) (hq : q ≠ 0) : M q * A₂ q = A₂ q * M q := by
  rw [M_eq_N_sub, Matrix.sub_mul, Matrix.mul_sub, N_mul_A₂ q hq, A₂_mul_N q hq,
    Matrix.smul_mul, Matrix.mul_smul, Matrix.one_mul, Matrix.mul_one]

theorem span_comm (q : R) (a b : R) (X : Matrix (Fin 3) (Fin 3) R)
    (hX : M q * X = X * M q) :
    (a • (1 : Matrix (Fin 3) (Fin 3) R) + b • M q) * X =
      X * (a • (1 : Matrix (Fin 3) (Fin 3) R) + b • M q) := by
  rw [Matrix.add_mul, Matrix.mul_add, Matrix.smul_mul, Matrix.smul_mul, Matrix.mul_smul,
    Matrix.mul_smul, Matrix.one_mul, Matrix.mul_one, hX]

/-- **T1.** `O` commutes with `A₁ q` and `A₂ q` iff `O ∈ span{1, M q}`. -/
theorem commutant_A_iff (q : R) (hq : q ≠ 0) (O : Matrix (Fin 3) (Fin 3) R) :
    (O * A₁ q = A₁ q * O ∧ O * A₂ q = A₂ q * O) ↔
      ∃ a b : R, O = a • (1 : Matrix (Fin 3) (Fin 3) R) + b • M q := by
  constructor
  · rintro ⟨h1, h2⟩
    have hqi : q * q⁻¹ = 1 := mul_inv_cancel₀ hq
    have k11 : O 1 2 - O 2 1 = 0 := by
      have e := congrFun (congrFun h1 1) 1
      simp [A₁, Matrix.mul_apply, Fin.sum_univ_three] at e
      first | linear_combination e | linear_combination -e
    have k01 : O 0 2 - q * O 0 1 = 0 := by
      have e := congrFun (congrFun h1 0) 1
      simp [A₁, Matrix.mul_apply, Fin.sum_univ_three] at e
      first | linear_combination e | linear_combination -e
    have k10 : q * O 1 0 - O 2 0 = 0 := by
      have e := congrFun (congrFun h1 1) 0
      simp [A₁, Matrix.mul_apply, Fin.sum_univ_three] at e
      first | linear_combination e | linear_combination -e
    have k12 : O 1 1 + (q - q⁻¹) * O 1 2 - O 2 2 = 0 := by
      have e := congrFun (congrFun h1 1) 2
      simp [A₁, Matrix.mul_apply, Fin.sum_univ_three] at e
      first | linear_combination e | linear_combination -e
    have l00 : O 0 1 - O 1 0 = 0 := by
      have e := congrFun (congrFun h2 0) 0
      simp [A₂, Matrix.mul_apply, Fin.sum_univ_three] at e
      first | linear_combination e | linear_combination -e
    have l02 : q * O 0 2 - O 1 2 = 0 := by
      have e := congrFun (congrFun h2 0) 2
      simp [A₂, Matrix.mul_apply, Fin.sum_univ_three] at e
      first | linear_combination e | linear_combination -e
    have l01 : O 0 0 + (q - q⁻¹) * O 0 1 - O 1 1 = 0 := by
      have e := congrFun (congrFun h2 0) 1
      simp [A₂, Matrix.mul_apply, Fin.sum_univ_three] at e
      first | linear_combination e | linear_combination -e
    refine ⟨O 2 2, O 2 1, ?_⟩
    ext i j; fin_cases i <;> fin_cases j
    · simp [M] <;> linear_combination (-q + q⁻¹ ^ 3) * k11 + (1 - q⁻¹ ^ 2) * k01 + k12 +
        (q⁻¹ ^ 3 - q⁻¹) * l02 + l01 + (-O 0 1 * q⁻¹ - O 0 2 * q⁻¹ ^ 2 + O 0 2) * hqi
    · simp [M] <;> linear_combination (q⁻¹ ^ 2) * k11 + (-q⁻¹) * k01 + (q⁻¹ ^ 2) * l02 +
        (-O 0 1 - O 0 2 * q⁻¹) * hqi
    · simp [M] <;> linear_combination q⁻¹ * k11 + q⁻¹ * l02 + (-O 0 2) * hqi
    · simp [M] <;> linear_combination (q⁻¹ ^ 2) * k11 + (-q⁻¹) * k01 - l00 +
        (q⁻¹ ^ 2) * l02 + (-O 0 1 - O 0 2 * q⁻¹) * hqi
    · simp [M] <;> linear_combination (-q + q⁻¹) * k11 + k12
    · simp [M] <;> linear_combination k11
    · simp [M] <;> linear_combination q⁻¹ * k11 - k01 - k10 - q * l00 + q⁻¹ * l02 +
        (-O 0 2) * hqi
    · simp [M]
    · simp [M]
  · rintro ⟨a, b, rfl⟩
    exact ⟨span_comm q a b _ (M_comm_A₁ q hq), span_comm q a b _ (M_comm_A₂ q hq)⟩

/-- **T1 (neutron).** The commutant of `{B₁, B₂}` on `(1,2)` is the same `span{1, M q}`. -/
theorem commutant_B_iff (q : R) (hq : q ≠ 0) (O : Matrix (Fin 3) (Fin 3) R) :
    (O * B₁ q = B₁ q * O ∧ O * B₂ q = B₂ q * O) ↔
      ∃ a b : R, O = a • (1 : Matrix (Fin 3) (Fin 3) R) + b • M q := by
  rw [B₁_eq_A₂, B₂_eq_A₁, and_comm]
  exact commutant_A_iff q hq O

/-- Coordinates in `span{1, M q}` are unique. -/
theorem coords_unique (q : R) (a b a' b' : R)
    (h : a • (1 : Matrix (Fin 3) (Fin 3) R) + b • M q = a' • 1 + b' • M q) :
    a = a' ∧ b = b' := by
  have h22 := congrFun (congrFun h 2) 2
  have h21 := congrFun (congrFun h 2) 1
  simp [M] at h22 h21
  exact ⟨h22, h21⟩

/-! ## T2. The adjacent insertion `Q₁₂ + Q₂₃` is not braid-covariant -/

theorem QAdjp_comm_A₁_defect (q : R) (h3 : (3 : R) ≠ 0) :
    (((Q12p + Q23p) * A₁ q - A₁ q * (Q12p + Q23p) : Matrix (Fin 3) (Fin 3) R) 1 2) =
      (-2 / 3 : R) := by
  have h9 : (9 : R) = 3 * 3 := by ring
  simp [Q12p, Q23p, A₁, Matrix.mul_apply, Fin.sum_univ_three]
  rw [h9]; field_simp; ring

/-- **T2.** `Q₁₂ + Q₂₃` on `(2,1)` does not commute with `σ₁`. -/
theorem QAdjp_not_comm_A₁ (q : R) (h2 : (2 : R) ≠ 0) (h3 : (3 : R) ≠ 0) :
    (Q12p + Q23p) * A₁ q ≠ A₁ q * (Q12p + Q23p) := by
  intro h
  have e := QAdjp_comm_A₁_defect q h3
  rw [sub_eq_zero.mpr h, Matrix.zero_apply] at e
  exact div_ne_zero (neg_ne_zero.mpr h2) h3 e.symm

theorem QAdjp_comm_A₂_defect (q : R) (h3 : (3 : R) ≠ 0) :
    (((Q12p + Q23p) * A₂ q - A₂ q * (Q12p + Q23p) : Matrix (Fin 3) (Fin 3) R) 0 1) =
      (2 / 3 : R) := by
  have h9 : (9 : R) = 3 * 3 := by ring
  simp [Q12p, Q23p, A₂, Matrix.mul_apply, Fin.sum_univ_three]
  rw [h9]; field_simp; ring

/-- **T2.** `Q₁₂ + Q₂₃` on `(2,1)` does not commute with `σ₂`. -/
theorem QAdjp_not_comm_A₂ (q : R) (h2 : (2 : R) ≠ 0) (h3 : (3 : R) ≠ 0) :
    (Q12p + Q23p) * A₂ q ≠ A₂ q * (Q12p + Q23p) := by
  intro h
  have e := QAdjp_comm_A₂_defect q h3
  rw [sub_eq_zero.mpr h, Matrix.zero_apply] at e
  exact div_ne_zero h2 h3 e.symm

theorem QAdjn_comm_B₁_defect (q : R) (h3 : (3 : R) ≠ 0) :
    (((Q12n + Q23n) * B₁ q - B₁ q * (Q12n + Q23n) : Matrix (Fin 3) (Fin 3) R) 0 1) =
      (1 / 3 : R) := by
  have h9 : (9 : R) = 3 * 3 := by ring
  simp [Q12n, Q23n, B₁, Matrix.mul_apply, Fin.sum_univ_three]
  rw [h9]; field_simp; ring

/-- **T2 (neutron).** `Q₁₂ + Q₂₃` on `(1,2)` does not commute with `σ₁`. -/
theorem QAdjn_not_comm_B₁ (q : R) (h3 : (3 : R) ≠ 0) :
    (Q12n + Q23n) * B₁ q ≠ B₁ q * (Q12n + Q23n) := by
  intro h
  have e := QAdjn_comm_B₁_defect q h3
  rw [sub_eq_zero.mpr h, Matrix.zero_apply] at e
  exact one_div_ne_zero h3 e.symm

theorem QAdjn_comm_B₂_defect (q : R) (h3 : (3 : R) ≠ 0) :
    (((Q12n + Q23n) * B₂ q - B₂ q * (Q12n + Q23n) : Matrix (Fin 3) (Fin 3) R) 1 2) =
      (-1 / 3 : R) := by
  have h9 : (9 : R) = 3 * 3 := by ring
  simp [Q12n, Q23n, B₂, Matrix.mul_apply, Fin.sum_univ_three]
  rw [h9]; field_simp; ring

/-- **T2 (neutron).** `Q₁₂ + Q₂₃` on `(1,2)` does not commute with `σ₂`. -/
theorem QAdjn_not_comm_B₂ (q : R) (h3 : (3 : R) ≠ 0) :
    (Q12n + Q23n) * B₂ q ≠ B₂ q * (Q12n + Q23n) := by
  intro h
  have e := QAdjn_comm_B₂_defect q h3
  rw [sub_eq_zero.mpr h, Matrix.zero_apply] at e
  exact div_ne_zero (neg_ne_zero.mpr one_ne_zero) h3 e.symm

/-- **T2, commutant form.** `Q₁₂ + Q₂₃` on `(2,1)` is not in `span{1, M q}`. -/
theorem QAdjp_not_mem_span (q : R) (hq : q ≠ 0) (h2 : (2 : R) ≠ 0) (h3 : (3 : R) ≠ 0) :
    ¬ ∃ a b : R, (Q12p + Q23p : Matrix (Fin 3) (Fin 3) R) = a • 1 + b • M q := by
  intro h
  exact QAdjp_not_comm_A₁ q h2 h3 ((commutant_A_iff q hq _).mpr h).1

/-! ## T3. The adjacent proton signal is minus the dropped pair -/

theorem QAdjp_eq_neg_Q13p : (Q12p + Q23p : Matrix (Fin 3) (Fin 3) R) = -Q13p := by
  have h := (QPairP_eq_sum (R := R))
  rw [QPairP] at h
  exact eq_neg_of_add_eq_zero_left h

/-- **T3.** For every matrix `X` (every braid word, with or without inverse letters),
`tr((Q₁₂ + Q₂₃) X) = -tr(Q₁₃ X)` on `(2,1)`. -/
theorem trace_QAdjp_eq_neg_Q13p (X : Matrix (Fin 3) (Fin 3) R) :
    trace ((Q12p + Q23p) * X) = -trace (Q13p * X) := by
  rw [QAdjp_eq_neg_Q13p, Matrix.neg_mul, Matrix.trace_neg]

theorem trace_QAdjp_word_eq_neg_Q13p (q : R) (w : List Bool) :
    trace ((Q12p + Q23p) * word (A₁ q) (A₂ q) w) = -trace (Q13p * word (A₁ q) (A₂ q) w) :=
  trace_QAdjp_eq_neg_Q13p _

theorem trace_QAdjp_borromeanV3_eq_neg_Q13p (q : R) :
    trace ((Q12p + Q23p) * borromeanV3A q) = -trace (Q13p * borromeanV3A q) :=
  trace_QAdjp_eq_neg_Q13p _

/-- **T3 (neutron).** `tr((Q₁₂ + Q₂₃) X) = -(1/3) tr X - tr(Q₁₃ X)` on `(1,2)`. -/
theorem trace_QAdjn_eq (h3 : (3 : R) ≠ 0) (X : Matrix (Fin 3) (Fin 3) R) :
    trace ((Q12n + Q23n) * X) = (-1 / 3 : R) * trace X - trace (Q13n * X) := by
  have h := QPairN_eq_sum (R := R) h3
  have h' : (Q12n + Q23n : Matrix (Fin 3) (Fin 3) R) = QPairN - Q13n := eq_sub_of_add_eq h
  rw [h', QPairN, Matrix.sub_mul, Matrix.trace_sub, Matrix.smul_mul, Matrix.one_mul,
    Matrix.trace_smul, smul_eq_mul]

/-! ## T4. What a braid-covariant insertion can produce -/

theorem N_mul_word_gen (q : R) (X Y : Matrix (Fin 3) (Fin 3) R)
    (hX : N q * X = q • N q) (hY : N q * Y = q • N q) (w : List Bool) :
    N q * word X Y w = q ^ w.length • N q := by
  induction w with
  | nil => simp [word]
  | cons b w ih =>
    simp only [word, List.length_cons]
    rw [← Matrix.mul_assoc]
    cases b
    · simp only [Bool.false_eq_true, if_false]
      rw [hY, Matrix.smul_mul, ih, smul_smul, pow_succ, mul_comm]
    · simp only [if_true]
      rw [hX, Matrix.smul_mul, ih, smul_smul, pow_succ, mul_comm]

theorem trace_N_word (q : R) (hq : q ≠ 0) (w : List Bool) :
    trace (N q * word (A₁ q) (A₂ q) w) = q ^ w.length * trace (N q) := by
  rw [N_mul_word_gen q _ _ (N_mul_A₁ q hq) (N_mul_A₂ q hq), Matrix.trace_smul, smul_eq_mul]

theorem trace_N_wordB (q : R) (hq : q ≠ 0) (w : List Bool) :
    trace (N q * word (B₁ q) (B₂ q) w) = q ^ w.length * trace (N q) := by
  rw [B₁_eq_A₂, B₂_eq_A₁, N_mul_word_gen q _ _ (N_mul_A₂ q hq) (N_mul_A₁ q hq),
    Matrix.trace_smul, smul_eq_mul]

/-- `N V = N` for the Borromean letter `V = σ₁ σ₂⁻¹`, hence `N V³ = N`. -/
theorem N_mul_borromeanV3A (q : R) (hq : q ≠ 0) : N q * borromeanV3A q = N q := by
  have hV : N q * borromeanVA q = N q := by
    rw [borromeanVA, ← Matrix.mul_assoc, N_mul_A₁ q hq, Matrix.smul_mul, N_mul_A₂Inv q hq,
      smul_smul, mul_inv_cancel₀ hq, one_smul]
  rw [borromeanV3A, ← Matrix.mul_assoc, ← Matrix.mul_assoc, hV, hV, hV]

/-- **T4.** Every braid-covariant insertion `O` contributes `a · tr X + b · tr(M X)`. -/
theorem covariant_trace (q : R) (hq : q ≠ 0) (O : Matrix (Fin 3) (Fin 3) R)
    (h1 : O * A₁ q = A₁ q * O) (h2 : O * A₂ q = A₂ q * O) :
    ∃ a b : R, ∀ X : Matrix (Fin 3) (Fin 3) R,
      trace (O * X) = a * trace X + b * trace (M q * X) := by
  obtain ⟨a, b, rfl⟩ := (commutant_A_iff q hq O).mp ⟨h1, h2⟩
  refine ⟨a, b, fun X => ?_⟩
  rw [Matrix.add_mul, Matrix.trace_add, Matrix.smul_mul, Matrix.smul_mul, Matrix.one_mul,
    Matrix.trace_smul, Matrix.trace_smul, smul_eq_mul, smul_eq_mul]

/-- **T4, positive words.** A covariant insertion gives `a · tr(w) + b · q^{|w|} · tr N`. -/
theorem covariant_trace_word (q : R) (hq : q ≠ 0) (O : Matrix (Fin 3) (Fin 3) R)
    (h1 : O * A₁ q = A₁ q * O) (h2 : O * A₂ q = A₂ q * O) :
    ∃ a b : R, ∀ w : List Bool,
      trace (O * word (A₁ q) (A₂ q) w) =
        a * trace (word (A₁ q) (A₂ q) w) + b * (q ^ w.length * trace (N q)) := by
  obtain ⟨a, b, rfl⟩ := (commutant_A_iff q hq O).mp ⟨h1, h2⟩
  refine ⟨a - b * q, b, fun w => ?_⟩
  rw [M_eq_N_sub, ← trace_N_word q hq w]
  simp only [Matrix.add_mul, Matrix.sub_mul, Matrix.smul_mul, Matrix.one_mul,
    Matrix.trace_add, Matrix.trace_sub, Matrix.trace_smul, smul_eq_mul, smul_sub]
  ring

/-- **T4, Borromean.** A covariant insertion gives `a · tr(V³) + b · tr N` on `V³`. -/
theorem covariant_trace_borromeanV3 (q : R) (hq : q ≠ 0) (O : Matrix (Fin 3) (Fin 3) R)
    (h1 : O * A₁ q = A₁ q * O) (h2 : O * A₂ q = A₂ q * O) :
    ∃ a b : R, trace (O * borromeanV3A q) = a * trace (borromeanV3A q) + b * trace (N q) := by
  obtain ⟨a, b, rfl⟩ := (commutant_A_iff q hq O).mp ⟨h1, h2⟩
  refine ⟨a - b * q, b, ?_⟩
  rw [M_eq_N_sub]
  simp only [Matrix.add_mul, Matrix.sub_mul, Matrix.smul_mul, Matrix.one_mul,
    Matrix.trace_add, Matrix.trace_sub, Matrix.trace_smul, smul_eq_mul, smul_sub,
    N_mul_borromeanV3A q hq]
  ring

/-- **T4, `n − p`.** For covariant insertions `O_p` (on `(2,1)`) and `O_n` (on `(1,2)`), the
`n − p` trace difference depends on the positive word only through `tr(w)` and `q^{|w|}`. -/
theorem covariant_trace_diff_word (q : R) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0)
    (Op On : Matrix (Fin 3) (Fin 3) R)
    (hp1 : Op * A₁ q = A₁ q * Op) (hp2 : Op * A₂ q = A₂ q * Op)
    (hn1 : On * B₁ q = B₁ q * On) (hn2 : On * B₂ q = B₂ q * On) :
    ∃ α β : R, ∀ w : List Bool,
      trace (On * word (B₁ q) (B₂ q) w) - trace (Op * word (A₁ q) (A₂ q) w) =
        α * trace (word (A₁ q) (A₂ q) w) + β * q ^ w.length := by
  obtain ⟨ap, bp, rfl⟩ := (commutant_A_iff q hq Op).mp ⟨hp1, hp2⟩
  obtain ⟨an, bn, rfl⟩ := (commutant_B_iff q hq On).mp ⟨hn1, hn2⟩
  refine ⟨(an - bn * q) - (ap - bp * q), (bn - bp) * trace (N q), fun w => ?_⟩
  rw [M_eq_N_sub]
  simp only [Matrix.add_mul, Matrix.sub_mul, Matrix.smul_mul, Matrix.one_mul,
    Matrix.trace_add, Matrix.trace_sub, Matrix.trace_smul, smul_eq_mul, smul_sub]
  rw [trace_N_word q hq w, trace_N_wordB q hq w, ← trace_word_eq q hq hq2 w]
  ring

/-! ## T5. Isotypic idempotents and the trace-preserving expectation onto the commutant -/

/-- The central idempotent of the trivial summand `(3)`. -/
def P3 (q : R) : Matrix (Fin 3) (Fin 3) R := (q ^ 3 / (q ^ 4 + q ^ 2 + 1)) • N q

/-- The central idempotent of the `(2,1)` summand. -/
def P21 (q : R) : Matrix (Fin 3) (Fin 3) R := 1 - P3 q

section Idempotents

variable (q : R) (hq : q ≠ 0) (hs : q ^ 4 + q ^ 2 + 1 ≠ 0)
include hq hs

theorem P3_mul_P3 : P3 q * P3 q = P3 q := by
  rw [P3, Matrix.smul_mul, Matrix.mul_smul, N_mul_N q hq, smul_smul, smul_smul]
  congr 1
  generalize hS : q ^ 4 + q ^ 2 + 1 = S at hs ⊢
  field_simp
  rw [← hS]; ring

theorem P3_mul_P21 : P3 q * P21 q = 0 := by
  rw [P21, Matrix.mul_sub, Matrix.mul_one, P3_mul_P3 q hq hs, sub_self]

theorem P21_mul_P3 : P21 q * P3 q = 0 := by
  rw [P21, Matrix.sub_mul, Matrix.one_mul, P3_mul_P3 q hq hs, sub_self]

theorem P21_mul_P21 : P21 q * P21 q = P21 q := by
  rw [P21, Matrix.sub_mul, Matrix.one_mul, Matrix.mul_sub, Matrix.mul_one,
    P3_mul_P3 q hq hs, sub_self, sub_zero]

theorem trace_P3 : trace (P3 q) = 1 := by
  rw [P3, Matrix.trace_smul, trace_N, smul_eq_mul, div_mul_eq_mul_div, div_eq_one_iff_eq hs]
  field_simp
  ring

theorem trace_P21 : trace (P21 q) = 2 := by
  rw [P21, Matrix.trace_sub, trace_P3 q hq hs, Matrix.trace_one]
  simp
  norm_num

end Idempotents

theorem P3_add_P21 (q : R) : P3 q + P21 q = 1 := by
  rw [P21]; abel

theorem P3_comm_A₁ (q : R) (hq : q ≠ 0) : P3 q * A₁ q = A₁ q * P3 q := by
  rw [P3, Matrix.smul_mul, Matrix.mul_smul, N_mul_A₁ q hq, A₁_mul_N q hq]

theorem P3_comm_A₂ (q : R) (hq : q ≠ 0) : P3 q * A₂ q = A₂ q * P3 q := by
  rw [P3, Matrix.smul_mul, Matrix.mul_smul, N_mul_A₂ q hq, A₂_mul_N q hq]

theorem P21_comm_A₁ (q : R) (hq : q ≠ 0) : P21 q * A₁ q = A₁ q * P21 q := by
  rw [P21, Matrix.sub_mul, Matrix.mul_sub, Matrix.one_mul, Matrix.mul_one, P3_comm_A₁ q hq]

theorem P21_comm_A₂ (q : R) (hq : q ≠ 0) : P21 q * A₂ q = A₂ q * P21 q := by
  rw [P21, Matrix.sub_mul, Matrix.mul_sub, Matrix.one_mul, Matrix.mul_one, P3_comm_A₂ q hq]

/-- The trace-preserving expectation onto the commutant:
`E(Q) = tr(Q P_(3))/tr(P_(3)) • P_(3) + tr(Q P_(2,1))/tr(P_(2,1)) • P_(2,1)`. -/
def E (q : R) (Q : Matrix (Fin 3) (Fin 3) R) : Matrix (Fin 3) (Fin 3) R :=
  trace (Q * P3 q) • P3 q + (trace (Q * P21 q) / 2) • P21 q

theorem E_comm_A₁ (q : R) (hq : q ≠ 0) (Q : Matrix (Fin 3) (Fin 3) R) :
    E q Q * A₁ q = A₁ q * E q Q := by
  rw [E, Matrix.add_mul, Matrix.mul_add, Matrix.smul_mul, Matrix.smul_mul, Matrix.mul_smul,
    Matrix.mul_smul, P3_comm_A₁ q hq, P21_comm_A₁ q hq]

theorem E_comm_A₂ (q : R) (hq : q ≠ 0) (Q : Matrix (Fin 3) (Fin 3) R) :
    E q Q * A₂ q = A₂ q * E q Q := by
  rw [E, Matrix.add_mul, Matrix.mul_add, Matrix.smul_mul, Matrix.smul_mul, Matrix.mul_smul,
    Matrix.mul_smul, P3_comm_A₂ q hq, P21_comm_A₂ q hq]

/-- **T5.** `E(Q)` lies in the commutant `span{1, M q}`. -/
theorem E_mem_span (q : R) (hq : q ≠ 0) (Q : Matrix (Fin 3) (Fin 3) R) :
    ∃ a b : R, E q Q = a • (1 : Matrix (Fin 3) (Fin 3) R) + b • M q :=
  (commutant_A_iff q hq _).mp ⟨E_comm_A₁ q hq Q, E_comm_A₂ q hq Q⟩

section Expectation

variable (q : R) (hq : q ≠ 0) (hs : q ^ 4 + q ^ 2 + 1 ≠ 0) (h2 : (2 : R) ≠ 0)
include hq hs h2

/-- **T5.** `E` preserves the matrix trace. -/
theorem trace_E (Q : Matrix (Fin 3) (Fin 3) R) : trace (E q Q) = trace Q := by
  have hsum : trace (Q * P3 q) + trace (Q * P21 q) = trace Q := by
    rw [← Matrix.trace_add, ← Matrix.mul_add, P3_add_P21, Matrix.mul_one]
  rw [E, Matrix.trace_add, Matrix.trace_smul, Matrix.trace_smul, smul_eq_mul, smul_eq_mul,
    trace_P3 q hq hs, trace_P21 q hq hs]
  rw [← hsum]
  field_simp

theorem trace_E_mul_P3 (Q : Matrix (Fin 3) (Fin 3) R) :
    trace (E q Q * P3 q) = trace (Q * P3 q) := by
  rw [E, Matrix.add_mul, Matrix.smul_mul, Matrix.smul_mul, P3_mul_P3 q hq hs,
    P21_mul_P3 q hq hs, smul_zero, add_zero, Matrix.trace_smul, trace_P3 q hq hs,
    smul_eq_mul, mul_one]

theorem trace_E_mul_P21 (Q : Matrix (Fin 3) (Fin 3) R) :
    trace (E q Q * P21 q) = trace (Q * P21 q) := by
  rw [E, Matrix.add_mul, Matrix.smul_mul, Matrix.smul_mul, P3_mul_P21 q hq hs,
    P21_mul_P21 q hq hs, smul_zero, zero_add, Matrix.trace_smul, trace_P21 q hq hs,
    smul_eq_mul]
  field_simp

/-- **T5.** `E` is idempotent. -/
theorem E_idem (Q : Matrix (Fin 3) (Fin 3) R) : E q (E q Q) = E q Q := by
  conv_lhs => rw [E, trace_E_mul_P3 q hq hs h2, trace_E_mul_P21 q hq hs h2]
  rfl

/-- **T5.** `E` fixes scalars. -/
theorem E_smul_one (c : R) : E q (c • (1 : Matrix (Fin 3) (Fin 3) R)) = c • 1 := by
  rw [E, Matrix.smul_mul, Matrix.one_mul, Matrix.smul_mul, Matrix.one_mul,
    Matrix.trace_smul, Matrix.trace_smul, trace_P3 q hq hs, trace_P21 q hq hs,
    smul_eq_mul, smul_eq_mul, mul_one, mul_div_assoc, div_self h2, mul_one, ← smul_add,
    P3_add_P21]

/-- **T5.** `E` fixes `N`, hence (with `E_smul_one`) every covariant insertion. -/
theorem E_N : E q (N q) = N q := by
  have hN : N q = (q⁻¹ ^ 3 + q⁻¹ + q) • P3 q := by
    rw [P3, smul_smul]
    have : (q⁻¹ ^ 3 + q⁻¹ + q) * (q ^ 3 / (q ^ 4 + q ^ 2 + 1)) = 1 := by
      rw [mul_div_assoc', div_eq_one_iff_eq hs]
      field_simp
      ring
    rw [this, one_smul]
  rw [E, hN, Matrix.smul_mul, Matrix.smul_mul, P3_mul_P3 q hq hs,
    P3_mul_P21 q hq hs, smul_zero, Matrix.trace_zero, zero_div, zero_smul, add_zero,
    Matrix.trace_smul, trace_P3 q hq hs, smul_eq_mul, mul_one]

theorem E_add (Q Q' : Matrix (Fin 3) (Fin 3) R) : E q (Q + Q') = E q Q + E q Q' := by
  simp only [E, Matrix.add_mul, Matrix.trace_add, add_smul, add_div]
  abel

theorem E_smul (c : R) (Q : Matrix (Fin 3) (Fin 3) R) : E q (c • Q) = c • E q Q := by
  simp only [E, Matrix.smul_mul, Matrix.trace_smul, smul_eq_mul, smul_add, smul_smul,
    mul_div_assoc]

/-- **T5.** `E` restricts to the identity on the commutant. -/
theorem E_of_comm (O : Matrix (Fin 3) (Fin 3) R)
    (h1 : O * A₁ q = A₁ q * O) (h2' : O * A₂ q = A₂ q * O) : E q O = O := by
  obtain ⟨a, b, rfl⟩ := (commutant_A_iff q hq O).mp ⟨h1, h2'⟩
  have hO : a • (1 : Matrix (Fin 3) (Fin 3) R) + b • M q = (a - b * q) • 1 + b • N q := by
    rw [M_eq_N_sub, smul_sub, smul_smul, sub_smul]; abel
  rw [hO, E_add q hq hs h2, E_smul_one q hq hs h2, E_smul q hq hs h2, E_N q hq hs h2]

/-! ## T6. The permutation-complete pairwise insertion has zero `M`-coefficient -/

/-- **T6.** On `(2,1)`: `E(Q_pair) = 0`. -/
theorem E_QPairP : E q (QPairP : Matrix (Fin 3) (Fin 3) R) = 0 := by
  rw [QPairP, E]; simp

/-- **T6.** On `(1,2)`: `E(Q_pair) = (-1/3) • 1`. -/
theorem E_QPairN : E q (QPairN : Matrix (Fin 3) (Fin 3) R) = (-1 / 3 : R) • 1 := by
  rw [QPairN, E_smul_one q hq hs h2]

/-- **T6.** In the coordinates of `span{1, M q}` the derived covariant pairwise Coulomb term has
`M`-coefficient exactly `0` on both weight spaces, and these coordinates are unique. -/
theorem E_QPair_Mcoeff_zero (a b : R) :
    (E q (QPairP : Matrix (Fin 3) (Fin 3) R) = a • 1 + b • M q → a = 0 ∧ b = 0) ∧
    (E q (QPairN : Matrix (Fin 3) (Fin 3) R) = a • 1 + b • M q → a = -1 / 3 ∧ b = 0) := by
  constructor
  · intro h
    rw [E_QPairP q hq hs h2] at h
    have := coords_unique q 0 0 a b (by rw [zero_smul, zero_smul, add_zero]; exact h)
    exact ⟨this.1.symm, this.2.symm⟩
  · intro h
    rw [E_QPairN q hq hs h2] at h
    have := coords_unique q (-1 / 3) 0 a b (by rw [zero_smul, add_zero]; exact h)
    exact ⟨this.1.symm, this.2.symm⟩

/-- **T6.** The derived two-term splitting with the projected permutation-complete Coulomb
term: `(q⁻¹ - q - c_em/3) · tr(w)` on every positive word `w`. -/
theorem trace_twoTerm_E_QPair_diff_word (c_em : R) (hq2 : q ^ 2 + 1 ≠ 0) (w : List Bool) :
    trace ((Kn q + c_em • E q QPairN) * word (B₁ q) (B₂ q) w) -
      trace ((Kp q + c_em • E q QPairP) * word (A₁ q) (A₂ q) w) =
      (q⁻¹ - q - c_em / 3) * trace (word (A₁ q) (A₂ q) w) := by
  rw [E_QPairN q hq hs h2, E_QPairP q hq hs h2]
  exact trace_twoTerm_QPair_diff_word q c_em hq hq2 w

end Expectation

/-! ## T6, contrast: the pair subset `Q₁₂ + Q₂₃` has a nonzero `M`-coefficient -/

theorem trace_QAdjp_P3 (q : R) (hq : q ≠ 0) (hs : q ^ 4 + q ^ 2 + 1 ≠ 0) (h3 : (3 : R) ≠ 0) :
    trace ((Q12p + Q23p) * P3 q) = 2 * (q ^ 2 - 1) ^ 2 / (9 * (q ^ 4 + q ^ 2 + 1)) := by
  have h9 : (9 : R) = 3 * 3 := by ring
  simp [Q12p, Q23p, P3, N, Matrix.trace_fin_three, Matrix.mul_apply, Fin.sum_univ_three]
  rw [h9]; field_simp; ring

/-- `E(Q₁₂ + Q₂₃)` on `(2,1)`, in the coordinates of `span{1, M q}`. -/
theorem trace_QAdjp_zero : trace ((Q12p + Q23p : Matrix (Fin 3) (Fin 3) R)) = 0 := by
  rw [Matrix.trace_add, trace_Q12p_zero, trace_Q23p_zero, add_zero]

theorem E_QAdjp_eq (q : R) (hq : q ≠ 0) (hs : q ^ 4 + q ^ 2 + 1 ≠ 0) (h2 : (2 : R) ≠ 0)
    (h3 : (3 : R) ≠ 0) :
    E q (Q12p + Q23p) =
      ((q - 1) ^ 3 * (q + 1) ^ 3 * (2 * q ^ 2 + 1) / (9 * (q ^ 4 + q ^ 2 + 1) ^ 2)) • 1 +
      (q ^ 3 * (q ^ 2 - 1) ^ 2 / (3 * (q ^ 4 + q ^ 2 + 1) ^ 2)) • M q := by
  have h9 : (9 : R) ≠ 0 := by
    have : (9 : R) = 3 * 3 := by ring
    rw [this]; exact mul_ne_zero h3 h3
  have hP21 : trace ((Q12p + Q23p) * P21 q) = -trace ((Q12p + Q23p) * P3 q) := by
    rw [P21, Matrix.mul_sub, Matrix.mul_one, Matrix.trace_sub, trace_QAdjp_zero, zero_sub]
  have key : E q (Q12p + Q23p) =
      (-(trace ((Q12p + Q23p) * P3 q) / 2)) • (1 : Matrix (Fin 3) (Fin 3) R) +
      (trace ((Q12p + Q23p) * P3 q) * (q ^ 3 / (q ^ 4 + q ^ 2 + 1)) +
        trace ((Q12p + Q23p) * P3 q) / 2 * (q ^ 3 / (q ^ 4 + q ^ 2 + 1))) • N q := by
    rw [E, hP21, P21, P3]; module
  have hrhs : ∀ α β : R, α • (1 : Matrix (Fin 3) (Fin 3) R) + β • M q =
      (α - β * q) • 1 + β • N q := by
    intro α β; rw [M_eq_N_sub]; module
  rw [key, hrhs, trace_QAdjp_P3 q hq hs h3]
  congr 2
  · generalize hS : q ^ 4 + q ^ 2 + 1 = S at hs ⊢
    field_simp
    rw [← hS]; ring
  · generalize hS : q ^ 4 + q ^ 2 + 1 = S at hs ⊢
    field_simp
    ring

end QOU.BraidsAndKnots.NucleonQEDCovariance
