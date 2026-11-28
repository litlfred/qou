/-
# How fast can the ring mass grow? A degree bound per crossing

Thread "Derive the tau lepton's word", hierarchy follow-up (2026-11-28). Owner card choices
"Derive the source of the hierarchy" and "Prove the q³ growth bound in Lean".
Audit: `docs/audits/2026-11-27-tau-lepton-word.md` §Growth bound.

`def:mass-identity` on three strands (`QOU.Observations.MassReadingForced.massWord`) is
`[2]³ q^{−2w} (y₃ q^w + y₂₁ tr ρ₂₁(β))` with `[2]³ y₃ = [2](q² + q⁻²)` and `[2]³ y₂₁ = [2]`, so

  `m(β) = (q + q⁻¹) · ((q² + q⁻²) q^{−w} + tr ∏ (q^{∓2} ρ₂₁(σ^{±1})))`.

This file writes that mass over the Laurent ring `ℤ[q, q⁻¹]`, letter by letter with the framing
absorbed (`framedGen`), and proves:

* `massL_degree_le`: the top `q`-degree of `m(β)` is at most
  `1 + max (3 n₋ − n₊) (2 + n₋ − n₊)`, where `n₋`, `n₊` count negative and positive letters.
  Each negative crossing raises the bound by at most 3, and each positive crossing lowers it.
* `massL_electron`: the encoding gives `m(σ₀σ₁σ₀) = 1 + q⁻² + q⁻⁴ + q⁻⁶ = [4]/q³`, and the
  bound is attained there (top degree 0).
* `famMass_recurrence` (over any field): on the family `σ₀ σ₁^{−k}` the mass satisfies
  `m_{k+2} = −q(q² − 1) m_{k+1} + q⁴ m_k`, whose characteristic roots are `−q³` and `q`, so the
  per-crossing factor 3 in the degree bound is reached.

This is the algebraic half of the statement. A bound on the absolute value at a real `q > 1` also
needs a bound on the coefficients and belongs under `QOU/Transcendental`; it is not proved here.
No measured value enters.
-/
import QOU.Nuclear.WeightSpaceMarkov
import Mathlib.Algebra.Polynomial.Laurent
import Mathlib.Algebra.MonoidAlgebra.Degree
import Mathlib.Tactic

namespace QOU.Observations.LeptonMassGrowthBound

open LaurentPolynomial

set_option linter.unusedSimpArgs false

/-- The Laurent ring `ℤ[q, q⁻¹]`, with `q = T 1`. -/
abbrev L := LaurentPolynomial ℤ

/-- Top `q`-degree (`⊥` for `0`). -/
noncomputable def deg (f : L) : WithBot ℤ :=
  AddMonoidAlgebra.supDegree (fun n : ℤ => (n : WithBot ℤ)) f

theorem deg_mul_le (f g : L) : deg (f * g) ≤ deg f + deg g :=
  AddMonoidAlgebra.supDegree_mul_le (fun a b => WithBot.coe_add a b)

theorem deg_add_le (f g : L) : deg (f + g) ≤ max (deg f) (deg g) :=
  AddMonoidAlgebra.supDegree_add_le

theorem deg_neg (f : L) : deg (-f) = deg f :=
  AddMonoidAlgebra.supDegree_neg

theorem deg_T (n : ℤ) : deg (T n) = n := by
  unfold deg
  rw [show (T n : L) = AddMonoidAlgebra.single n 1 from rfl,
    AddMonoidAlgebra.supDegree_single_ne_zero _ one_ne_zero]

theorem deg_zero : deg (0 : L) = ⊥ := AddMonoidAlgebra.supDegree_zero

/-- Every entry has top degree at most `d`. -/
def MatLE (d : ℤ) (M : Matrix (Fin 2) (Fin 2) L) : Prop := ∀ i j, deg (M i j) ≤ d

theorem le_of_le_max {a b c : WithBot ℤ} (ha : a ≤ c) (hb : b ≤ c) : max a b ≤ c :=
  max_le ha hb

theorem MatLE.mul {a b : ℤ} {M N : Matrix (Fin 2) (Fin 2) L} (hM : MatLE a M) (hN : MatLE b N) :
    MatLE (a + b) (M * N) := by
  intro i j
  rw [Matrix.mul_apply, Fin.sum_univ_two]
  refine (deg_add_le _ _).trans (max_le ?_ ?_) <;>
  · refine (deg_mul_le _ _).trans ?_
    rw [WithBot.coe_add]
    exact add_le_add (hM _ _) (hN _ _)

/-- `ρ₂₁(σᵢ^{±1})` with its framing factor `q^{∓2}` (`true` = positive crossing):
`q⁻²ρ(σ₀) = [[q⁻¹, q⁻²], [0, −q⁻³]]`, `q⁻²ρ(σ₁) = [[−q⁻³, 0], [q⁻², q⁻¹]]`,
`q²ρ(σ₀)⁻¹ = [[q, q²], [0, −q³]]`, `q²ρ(σ₁)⁻¹ = [[−q³, 0], [q², q]]`. -/
noncomputable def framedGen : Fin 2 → Bool → Matrix (Fin 2) (Fin 2) L
  | 0, true => !![T (-1), T (-2); 0, -T (-3)]
  | 1, true => !![-T (-3), 0; T (-2), T (-1)]
  | 0, false => !![T 1, T 2; 0, -T 3]
  | 1, false => !![-T 3, 0; T 2, T 1]

/-- Framing factor `q^{∓1}` of one letter in the `(3)` block. -/
noncomputable def frameGen : Bool → L
  | true => T (-1)
  | false => T 1

noncomputable def prodFramed : List (Fin 2 × Bool) → Matrix (Fin 2) (Fin 2) L
  | [] => 1
  | (i, s) :: w => framedGen i s * prodFramed w

noncomputable def frameProd : List (Fin 2 × Bool) → L
  | [] => 1
  | (_, s) :: w => frameGen s * frameProd w

/-- The ring mass of `def:mass-identity` on three strands, over `ℤ[q, q⁻¹]`. -/
noncomputable def massL (w : List (Fin 2 × Bool)) : L :=
  (T 1 + T (-1)) * ((T 2 + T (-2)) * frameProd w + Matrix.trace (prodFramed w))

/-- Degree budget of the `(2,1)` block: `3 n₋ − n₊`. -/
def budget21 : List (Fin 2 × Bool) → ℤ
  | [] => 0
  | (_, true) :: w => budget21 w - 1
  | (_, false) :: w => budget21 w + 3

/-- Degree budget of the `(3)` block: `n₋ − n₊`. -/
def budget3 : List (Fin 2 × Bool) → ℤ
  | [] => 0
  | (_, true) :: w => budget3 w - 1
  | (_, false) :: w => budget3 w + 1

theorem framedGen_le (i : Fin 2) (s : Bool) :
    MatLE (if s then -1 else 3) (framedGen i s) := by
  have hT : ∀ n m : ℤ, n ≤ m → deg (T n) ≤ m := fun n m h => by
    rw [deg_T]; exact_mod_cast h
  have h0 : ∀ m : ℤ, deg (0 : L) ≤ m := fun m => by rw [deg_zero]; exact bot_le
  have hnT : ∀ n m : ℤ, n ≤ m → deg (-T n) ≤ m := fun n m h => by rw [deg_neg]; exact hT n m h
  intro a b
  fin_cases i <;> cases s <;> fin_cases a <;> fin_cases b <;>
    simp only [framedGen, Matrix.of_apply, Matrix.cons_val', Matrix.cons_val_zero,
      Matrix.cons_val_one, Matrix.empty_val', Matrix.cons_val_fin_one, Matrix.head_cons,
      Matrix.head_fin_const, if_true, if_false, Bool.false_eq_true] <;>
    first
      | exact h0 _
      | exact hT _ _ (by norm_num)
      | exact hnT _ _ (by norm_num)

theorem one_le : MatLE 0 (1 : Matrix (Fin 2) (Fin 2) L) := by
  intro i j
  by_cases h : i = j
  · subst h; rw [Matrix.one_apply_eq, show (1 : L) = T 0 from T_zero.symm, deg_T]
  · rw [Matrix.one_apply_ne h, deg_zero]; exact bot_le

/-- **Each negative letter raises the `(2,1)` budget by 3, each positive letter lowers it by 1.** -/
theorem prodFramed_le (w : List (Fin 2 × Bool)) : MatLE (budget21 w) (prodFramed w) := by
  induction w with
  | nil => exact one_le
  | cons x w ih =>
    obtain ⟨i, s⟩ := x
    have h := (framedGen_le i s).mul ih
    cases s
    · simpa [prodFramed, budget21, add_comm] using h
    · simpa [prodFramed, budget21, add_comm, sub_eq_add_neg] using h

theorem frameProd_le (w : List (Fin 2 × Bool)) : deg (frameProd w) ≤ budget3 w := by
  induction w with
  | nil => rw [frameProd, show (1 : L) = T 0 from T_zero.symm, deg_T]; rfl
  | cons x w ih =>
    obtain ⟨i, s⟩ := x
    refine (deg_mul_le _ _).trans ?_
    cases s
    · simp only [frameGen, deg_T, budget3]
      rw [add_comm (budget3 w), WithBot.coe_add]
      exact add_le_add le_rfl ih
    · simp only [frameGen, deg_T, budget3]
      rw [sub_eq_add_neg, add_comm (budget3 w), WithBot.coe_add]
      exact add_le_add le_rfl ih

theorem deg_T_add_le (n : ℤ) : deg (T n + T (-n)) ≤ max n (-n) := by
  refine (deg_add_le _ _).trans ?_
  rw [deg_T, deg_T]
  exact le_of_eq (by simp)

/-- **Degree bound for the ring mass.** The top `q`-degree of `m(β)` is at most
`1 + max (3 n₋ − n₊) (2 + n₋ − n₊)`. -/
theorem massL_degree_le (w : List (Fin 2 × Bool)) :
    deg (massL w) ≤ (1 + max (budget21 w) (2 + budget3 w) : ℤ) := by
  unfold massL
  refine (deg_mul_le _ _).trans ?_
  have h1 : deg (T 1 + T (-1)) ≤ (1 : ℤ) := (deg_T_add_le 1).trans (by norm_num)
  have h2 : deg ((T 2 + T (-2)) * frameProd w) ≤ (2 + budget3 w : ℤ) := by
    refine (deg_mul_le _ _).trans ?_
    rw [WithBot.coe_add]
    exact add_le_add ((deg_T_add_le 2).trans (by norm_num)) (frameProd_le w)
  have h3 : deg (Matrix.trace (prodFramed w)) ≤ (budget21 w : ℤ) := by
    rw [Matrix.trace_fin_two]
    refine (deg_add_le _ _).trans (max_le ?_ ?_)
    · exact prodFramed_le w 0 0
    · exact prodFramed_le w 1 1
  rw [WithBot.coe_add]
  refine add_le_add h1 ?_
  refine (deg_add_le _ _).trans (max_le ?_ ?_)
  · exact h2.trans (by exact_mod_cast le_max_right _ _)
  · exact h3.trans (by exact_mod_cast le_max_left _ _)

/-- **Sanity check against `massWord_e`**: `m(σ₀σ₁σ₀) = 1 + q⁻² + q⁻⁴ + q⁻⁶ = [4]/q³`, top degree
`0`, which is the bound `1 + max (−3) (−1)`. -/
theorem massL_electron :
    massL [(0, true), (1, true), (0, true)] = T 0 + T (-2) + T (-4) + T (-6) := by
  simp only [massL, prodFramed, frameProd, framedGen, frameGen, Matrix.trace_fin_two,
    Matrix.mul_apply, Fin.sum_univ_two, Matrix.one_apply, Matrix.of_apply, Matrix.cons_val',
    Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.empty_val', Matrix.cons_val_fin_one,
    Matrix.head_cons, Fin.isValue]
  simp only [← T_add, mul_one, one_mul, mul_zero, zero_mul, add_zero, zero_add, mul_neg,
    neg_mul, neg_neg, Fin.one_eq_zero_iff, if_true, if_false, OfNat.ofNat_ne_one,
    one_ne_zero, zero_ne_one, Fin.zero_eq_one_iff]
  norm_num
  simp only [add_mul, mul_add, ← T_add]
  norm_num
  abel

/-! ### The family `σ₀ σ₁^{−k}`: the factor `q³` per crossing is reached -/

section Family

open QOU.QBeta.WeightSpaceMarkov QOU.Observations

variable {R : Type*} [Field R]

/-- `ρ₂₁(σ₁)⁻¹ = [[−q, 0], [1, q⁻¹]]`. -/
def bInv (q : R) : Matrix (Fin 2) (Fin 2) R := !![-q, 0; 1, q⁻¹]

/-- Ring mass of `σ₀ σ₁^{−k}` (writhe `1 − k`), `k ≥ 1`, in the form above. -/
def famMass (q : R) (k : ℕ) : R :=
  (q + q⁻¹) * ((q ^ 2 + q⁻¹ ^ 2) * q ^ (k - 1) +
    q ^ (2 * (k - 1)) * Matrix.trace (r21a q * bInv q ^ k))

theorem bInv_sq (q : R) (hq : q ≠ 0) : bInv q ^ 2 = (q⁻¹ - q) • bInv q + 1 := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [bInv, sq, Matrix.mul_apply, Fin.sum_univ_two] <;> field_simp <;> ring

/-- **Recurrence on `σ₀ σ₁^{−k}`**: `m_{k+2} = −q(q² − 1) m_{k+1} + q⁴ m_k` for `k ≥ 1`.
Its characteristic roots are `−q³` and `q`. -/
theorem famMass_recurrence (q : R) (hq : q ≠ 0) (k : ℕ) (hk : 1 ≤ k) :
    famMass q (k + 2) = -q * (q ^ 2 - 1) * famMass q (k + 1) + q ^ 4 * famMass q k := by
  obtain ⟨j, rfl⟩ : ∃ j, k = j + 1 := ⟨k - 1, by omega⟩
  have htr : Matrix.trace (r21a q * bInv q ^ (j + 1 + 2)) =
      (q⁻¹ - q) * Matrix.trace (r21a q * bInv q ^ (j + 1 + 1)) +
        Matrix.trace (r21a q * bInv q ^ (j + 1)) := by
    rw [show j + 1 + 2 = (j + 1) + 2 from rfl, pow_add, bInv_sq q hq]
    simp only [Matrix.mul_add, Matrix.mul_smul, Matrix.mul_one, Matrix.trace_add,
      Matrix.trace_smul, smul_eq_mul, ← pow_succ]
  unfold famMass
  rw [htr]
  simp only [show j + 1 + 2 - 1 = j + 2 from rfl, show j + 1 + 1 - 1 = j + 1 from rfl,
    show j + 1 - 1 = j from rfl]
  field_simp
  ring

/-- Characteristic polynomial check: `x = −q³` and `x = q` solve `x² + q(q² − 1)x − q⁴ = 0`. -/
theorem famMass_char_roots (q : R) :
    (-q ^ 3) ^ 2 + q * (q ^ 2 - 1) * (-q ^ 3) - q ^ 4 = 0 ∧
      q ^ 2 + q * (q ^ 2 - 1) * q - q ^ 4 = 0 := by
  constructor <;> ring

end Family

end QOU.Observations.LeptonMassGrowthBound
