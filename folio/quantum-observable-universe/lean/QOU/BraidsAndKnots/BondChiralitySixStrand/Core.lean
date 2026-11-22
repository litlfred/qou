import Mathlib.LinearAlgebra.Matrix.Trace
import Mathlib.Data.Matrix.Mul
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FinCases
import Mathlib.Tactic.NormNum

/-!
# Bond chirality on six strands: shared machinery

Full-space Jimbo braiding on `(C²)^{⊗6}`, the restriction of any word to an invariant coordinate
subspace (`diag_word`), the four weight spaces `#0 ∈ {1, 2, 4, 5}`, the row-by-row action of each
generator on them, and the reduction of the functional `F(O±)` to weight-space diagonal entries.
The four values are in `BondChiralitySixStrand.Case*`; the summary is `BondChiralitySixStrand`.
-/

namespace QOU.BraidsAndKnots.BondChiralitySixStrand

open Matrix

variable {R : Type*} [Field R]

set_option linter.unusedVariables false
set_option maxHeartbeats 1000000

/-- A letter: generator index and `true` for an inverse crossing. -/
abbrev Letter := Fin 5 × Bool

/-- `Ř` on strands `i, i+1` of `(C²)^{⊗6}`, as a `64 × 64` matrix (column `s` is `Ř e_s`). -/
def gen64 (q : R) (i : ℕ) : Matrix (Fin 64) (Fin 64) R := fun t s =>
  if s.val.testBit i = s.val.testBit (i + 1) then (if t = s then q else 0)
  else if s.val.testBit i = false then (if t.val = s.val ^^^ (3 <<< i) then 1 else 0)
  else (if t.val = s.val ^^^ (3 <<< i) then 1 else 0) + (if t = s then q - q⁻¹ else 0)

/-- A letter on the full space; the inverse crossing is `σ_i⁻¹ = σ_i − h`. -/
def g64 (q : R) : Letter → Matrix (Fin 64) (Fin 64) R
  | (i, false) => gen64 q i.val
  | (i, true) => gen64 q i.val - (q - q⁻¹) • 1

/-- A braid word on the full space (product in list order). -/
def word64 (q : R) : List Letter → Matrix (Fin 64) (Fin 64) R
  | [] => 1
  | l :: w => g64 q l * word64 q w

/-! ### Restriction to an invariant coordinate subspace -/

section Embedding

variable {d : ℕ}

/-- Inclusion of the coordinate subspace spanned by the states `idx k`. -/
def Emb (idx : Fin d → Fin 64) : Matrix (Fin 64) (Fin d) R :=
  fun s k => if s = idx k then 1 else 0

/-- `M` maps the span of the `idx k` into itself. -/
def Closed (idx : Fin d → Fin 64) (M : Matrix (Fin 64) (Fin 64) R) : Prop :=
  ∀ s k, (∀ j, s ≠ idx j) → M s (idx k) = 0

theorem mul_Emb_eq (idx : Fin d → Fin 64) (hinj : Function.Injective idx)
    (M : Matrix (Fin 64) (Fin 64) R) (hM : Closed idx M) :
    M * Emb idx = Emb idx * M.submatrix idx idx := by
  ext s k
  simp only [Matrix.mul_apply, Emb, Matrix.submatrix_apply, mul_ite, mul_one, mul_zero,
    ite_mul, one_mul, zero_mul]
  rw [Finset.sum_ite_eq' Finset.univ (idx k), if_pos (Finset.mem_univ _)]
  by_cases h : ∃ j, s = idx j
  · obtain ⟨j, rfl⟩ := h
    rw [Finset.sum_eq_single j]
    · simp
    · intro b _ hb; rw [if_neg]; exact fun e => hb (hinj e).symm
    · simp
  · push_neg at h
    rw [hM s k h]
    symm; apply Finset.sum_eq_zero; intro j _; rw [if_neg (h j)]

/-- The coordinate set is closed under the swap of strands `i, i+1` where they differ. -/
def SwapClosed (idx : Fin d → Fin 64) (i : ℕ) : Prop :=
  ∀ k, (idx k).val.testBit i ≠ (idx k).val.testBit (i + 1) →
    ∃ j, (idx j).val = (idx k).val ^^^ (3 <<< i)

theorem closed_gen64 (idx : Fin d → Fin 64) (i : ℕ) (hc : SwapClosed idx i) (q : R) :
    Closed idx (gen64 q i) := by
  intro s k hs
  have hne : s ≠ idx k := hs k
  unfold gen64
  by_cases hb : (idx k).val.testBit i = (idx k).val.testBit (i + 1)
  · rw [if_pos hb, if_neg hne]
  · obtain ⟨j, hj⟩ := hc k hb
    have hsv : s.val ≠ (idx k).val ^^^ (3 <<< i) := by
      intro e; exact hs j (Fin.ext (e.trans hj.symm))
    rw [if_neg hb]
    split_ifs <;> simp_all

theorem closed_g64 (idx : Fin d → Fin 64) (hsc : ∀ i : Fin 5, SwapClosed idx i.val) (q : R)
    (l : Letter) : Closed idx (g64 q l) := by
  obtain ⟨i, b⟩ := l
  cases b
  · exact closed_gen64 idx i.val (hsc i) q
  · intro s k hs
    simp only [g64, Matrix.sub_apply, Matrix.smul_apply, Matrix.one_apply, if_neg (hs k),
      smul_zero, sub_zero]
    exact closed_gen64 idx i.val (hsc i) q s k hs

/-- A letter restricted to the subspace. -/
def gW (q : R) (idx : Fin d → Fin 64) (l : Letter) : Matrix (Fin d) (Fin d) R :=
  (g64 q l).submatrix idx idx

/-- A word restricted to the subspace (product in list order). -/
def wordW (q : R) (idx : Fin d → Fin 64) : List Letter → Matrix (Fin d) (Fin d) R
  | [] => 1
  | l :: w => gW q idx l * wordW q idx w

theorem emb_word (q : R) (idx : Fin d → Fin 64) (hinj : Function.Injective idx)
    (hsc : ∀ i : Fin 5, SwapClosed idx i.val) (w : List Letter) :
    word64 q w * Emb idx = Emb idx * wordW q idx w := by
  induction w with
  | nil => simp [word64, wordW]
  | cons l w ih =>
    simp only [word64, wordW]
    rw [Matrix.mul_assoc, ih, ← Matrix.mul_assoc,
      mul_Emb_eq idx hinj (g64 q l) (closed_g64 idx hsc q l), Matrix.mul_assoc]
    rfl

/-- **The reduction, entrywise.** A diagonal entry of a word on the full space, at a state of an
invariant coordinate subspace, is the diagonal entry of the restricted word. -/
theorem diag_word (q : R) (idx : Fin d → Fin 64) (hinj : Function.Injective idx)
    (hsc : ∀ i : Fin 5, SwapClosed idx i.val) (w : List Letter) (k : Fin d) :
    word64 q w (idx k) (idx k) = wordW q idx w k k := by
  have e := congrFun (congrFun (emb_word q idx hinj hsc w) (idx k)) k
  simp only [Matrix.mul_apply, Emb, mul_ite, mul_one, mul_zero, ite_mul, one_mul, zero_mul] at e
  rw [Finset.sum_ite_eq' Finset.univ (idx k), if_pos (Finset.mem_univ _)] at e
  rw [e, Finset.sum_eq_single k]
  · simp
  · intro b _ hb; rw [if_neg]; exact fun h => hb (hinj h).symm
  · simp

/-- The inverse letter on the subspace is the forward letter minus `h`. -/
theorem gW_inv_mulVec (q : R) (idx : Fin d → Fin 64) (hinj : Function.Injective idx) (i : Fin 5)
    (v : Fin d → R) :
    (gW q idx (i, true)).mulVec v = fun t => (gW q idx (i, false)).mulVec v t - (q - q⁻¹) * v t := by
  funext t
  simp only [gW, g64, Matrix.mulVec, dotProduct, Matrix.submatrix_apply, Matrix.sub_apply,
    Matrix.smul_apply, Matrix.one_apply, hinj.eq_iff, sub_mul, Finset.sum_sub_distrib, smul_eq_mul,
    mul_ite, mul_one, mul_zero, ite_mul, zero_mul]
  simp

theorem wordW_mulVec_cons (q : R) (idx : Fin d → Fin 64) (l : Letter) (w : List Letter)
    (v : Fin d → R) :
    (wordW q idx (l :: w)).mulVec v = (gW q idx l).mulVec ((wordW q idx w).mulVec v) := by
  simp [wordW, Matrix.mulVec_mulVec]

theorem wordW_nil (q : R) (idx : Fin d → Fin 64) : wordW q idx [] = 1 := rfl

theorem entry_eq_mulVec_single (M : Matrix (Fin d) (Fin d) R) (i j : Fin d) :
    M i j = (M.mulVec (Pi.single j 1)) i := by
  simp [Matrix.mulVec, dotProduct, Pi.single_apply]

end Embedding

/-! ### The weight space with 1 zero (dimension 6) -/

/-- The states with 1 zero, in increasing order. -/
def idx1 : Fin 6 → Fin 64 := ![31, 47, 55, 59, 61, 62]
theorem idx1_inj : Function.Injective idx1 := by decide
theorem idx1_sc : ∀ i : Fin 5, SwapClosed idx1 i.val := by unfold SwapClosed; decide +kernel

/-- `σ_0` on the 1-zero weight space, row by row. -/
def act1_0 (q : R) (v : Fin 6 → R) : Fin 6 → R :=
  ![q * v 0, q * v 1, q * v 2, q * v 3, v 5 + (q - q⁻¹) * v 4, v 4]
theorem bridge1_0 (q : R) (v : Fin 6 → R) :
    (gW q idx1 (0, false)).mulVec v = act1_0 q v := by
  funext t; fin_cases t <;>
    simp +decide [gW, g64, gen64, Matrix.mulVec, dotProduct, Fin.sum_univ_succ, idx1, act1_0] <;> (try ring)

/-- `σ_1` on the 1-zero weight space, row by row. -/
def act1_1 (q : R) (v : Fin 6 → R) : Fin 6 → R :=
  ![q * v 0, q * v 1, q * v 2, v 4 + (q - q⁻¹) * v 3, v 3, q * v 5]
theorem bridge1_1 (q : R) (v : Fin 6 → R) :
    (gW q idx1 (1, false)).mulVec v = act1_1 q v := by
  funext t; fin_cases t <;>
    simp +decide [gW, g64, gen64, Matrix.mulVec, dotProduct, Fin.sum_univ_succ, idx1, act1_1] <;> (try ring)

/-- `σ_2` on the 1-zero weight space, row by row. -/
def act1_2 (q : R) (v : Fin 6 → R) : Fin 6 → R :=
  ![q * v 0, q * v 1, v 3 + (q - q⁻¹) * v 2, v 2, q * v 4, q * v 5]
theorem bridge1_2 (q : R) (v : Fin 6 → R) :
    (gW q idx1 (2, false)).mulVec v = act1_2 q v := by
  funext t; fin_cases t <;>
    simp +decide [gW, g64, gen64, Matrix.mulVec, dotProduct, Fin.sum_univ_succ, idx1, act1_2] <;> (try ring)

/-- `σ_3` on the 1-zero weight space, row by row. -/
def act1_3 (q : R) (v : Fin 6 → R) : Fin 6 → R :=
  ![q * v 0, v 2 + (q - q⁻¹) * v 1, v 1, q * v 3, q * v 4, q * v 5]
theorem bridge1_3 (q : R) (v : Fin 6 → R) :
    (gW q idx1 (3, false)).mulVec v = act1_3 q v := by
  funext t; fin_cases t <;>
    simp +decide [gW, g64, gen64, Matrix.mulVec, dotProduct, Fin.sum_univ_succ, idx1, act1_3] <;> (try ring)

/-- `σ_4` on the 1-zero weight space, row by row. -/
def act1_4 (q : R) (v : Fin 6 → R) : Fin 6 → R :=
  ![v 1 + (q - q⁻¹) * v 0, v 0, q * v 2, q * v 3, q * v 4, q * v 5]
theorem bridge1_4 (q : R) (v : Fin 6 → R) :
    (gW q idx1 (4, false)).mulVec v = act1_4 q v := by
  funext t; fin_cases t <;>
    simp +decide [gW, g64, gen64, Matrix.mulVec, dotProduct, Fin.sum_univ_succ, idx1, act1_4] <;> (try ring)

/-! ### The weight space with 2 zeros (dimension 15) -/

/-- The states with 2 zeros, in increasing order. -/
def idx2 : Fin 15 → Fin 64 := ![15, 23, 27, 29, 30, 39, 43, 45, 46, 51, 53, 54, 57, 58, 60]
theorem idx2_inj : Function.Injective idx2 := by decide
theorem idx2_sc : ∀ i : Fin 5, SwapClosed idx2 i.val := by unfold SwapClosed; decide +kernel

/-- `σ_0` on the 2-zero weight space, row by row. -/
def act2_0 (q : R) (v : Fin 15 → R) : Fin 15 → R :=
  ![q * v 0, q * v 1, q * v 2, v 4 + (q - q⁻¹) * v 3, v 3, q * v 5, q * v 6, v 8 + (q - q⁻¹) * v 7, v 7, q * v 9, v 11 + (q - q⁻¹) * v 10, v 10, v 13 + (q - q⁻¹) * v 12, v 12, q * v 14]
theorem bridge2_0 (q : R) (v : Fin 15 → R) :
    (gW q idx2 (0, false)).mulVec v = act2_0 q v := by
  funext t; fin_cases t <;>
    simp +decide [gW, g64, gen64, Matrix.mulVec, dotProduct, Fin.sum_univ_succ, idx2, act2_0] <;> (try ring)

/-- `σ_1` on the 2-zero weight space, row by row. -/
def act2_1 (q : R) (v : Fin 15 → R) : Fin 15 → R :=
  ![q * v 0, q * v 1, v 3 + (q - q⁻¹) * v 2, v 2, q * v 4, q * v 5, v 7 + (q - q⁻¹) * v 6, v 6, q * v 8, v 10 + (q - q⁻¹) * v 9, v 9, q * v 11, q * v 12, v 14 + (q - q⁻¹) * v 13, v 13]
theorem bridge2_1 (q : R) (v : Fin 15 → R) :
    (gW q idx2 (1, false)).mulVec v = act2_1 q v := by
  funext t; fin_cases t <;>
    simp +decide [gW, g64, gen64, Matrix.mulVec, dotProduct, Fin.sum_univ_succ, idx2, act2_1] <;> (try ring)

/-- `σ_2` on the 2-zero weight space, row by row. -/
def act2_2 (q : R) (v : Fin 15 → R) : Fin 15 → R :=
  ![q * v 0, v 2 + (q - q⁻¹) * v 1, v 1, q * v 3, q * v 4, v 6 + (q - q⁻¹) * v 5, v 5, q * v 7, q * v 8, q * v 9, v 12 + (q - q⁻¹) * v 10, v 13 + (q - q⁻¹) * v 11, v 10, v 11, q * v 14]
theorem bridge2_2 (q : R) (v : Fin 15 → R) :
    (gW q idx2 (2, false)).mulVec v = act2_2 q v := by
  funext t; fin_cases t <;>
    simp +decide [gW, g64, gen64, Matrix.mulVec, dotProduct, Fin.sum_univ_succ, idx2, act2_2] <;> (try ring)

/-- `σ_3` on the 2-zero weight space, row by row. -/
def act2_3 (q : R) (v : Fin 15 → R) : Fin 15 → R :=
  ![v 1 + (q - q⁻¹) * v 0, v 0, q * v 2, q * v 3, q * v 4, q * v 5, v 9 + (q - q⁻¹) * v 6, v 10 + (q - q⁻¹) * v 7, v 11 + (q - q⁻¹) * v 8, v 6, v 7, v 8, q * v 12, q * v 13, q * v 14]
theorem bridge2_3 (q : R) (v : Fin 15 → R) :
    (gW q idx2 (3, false)).mulVec v = act2_3 q v := by
  funext t; fin_cases t <;>
    simp +decide [gW, g64, gen64, Matrix.mulVec, dotProduct, Fin.sum_univ_succ, idx2, act2_3] <;> (try ring)

/-- `σ_4` on the 2-zero weight space, row by row. -/
def act2_4 (q : R) (v : Fin 15 → R) : Fin 15 → R :=
  ![q * v 0, v 5 + (q - q⁻¹) * v 1, v 6 + (q - q⁻¹) * v 2, v 7 + (q - q⁻¹) * v 3, v 8 + (q - q⁻¹) * v 4, v 1, v 2, v 3, v 4, q * v 9, q * v 10, q * v 11, q * v 12, q * v 13, q * v 14]
theorem bridge2_4 (q : R) (v : Fin 15 → R) :
    (gW q idx2 (4, false)).mulVec v = act2_4 q v := by
  funext t; fin_cases t <;>
    simp +decide [gW, g64, gen64, Matrix.mulVec, dotProduct, Fin.sum_univ_succ, idx2, act2_4] <;> (try ring)

/-! ### The weight space with 4 zeros (dimension 15) -/

/-- The states with 4 zeros, in increasing order. -/
def idx4 : Fin 15 → Fin 64 := ![3, 5, 6, 9, 10, 12, 17, 18, 20, 24, 33, 34, 36, 40, 48]
theorem idx4_inj : Function.Injective idx4 := by decide
theorem idx4_sc : ∀ i : Fin 5, SwapClosed idx4 i.val := by unfold SwapClosed; decide +kernel

/-- `σ_0` on the 4-zero weight space, row by row. -/
def act4_0 (q : R) (v : Fin 15 → R) : Fin 15 → R :=
  ![q * v 0, v 2 + (q - q⁻¹) * v 1, v 1, v 4 + (q - q⁻¹) * v 3, v 3, q * v 5, v 7 + (q - q⁻¹) * v 6, v 6, q * v 8, q * v 9, v 11 + (q - q⁻¹) * v 10, v 10, q * v 12, q * v 13, q * v 14]
theorem bridge4_0 (q : R) (v : Fin 15 → R) :
    (gW q idx4 (0, false)).mulVec v = act4_0 q v := by
  funext t; fin_cases t <;>
    simp +decide [gW, g64, gen64, Matrix.mulVec, dotProduct, Fin.sum_univ_succ, idx4, act4_0] <;> (try ring)

/-- `σ_1` on the 4-zero weight space, row by row. -/
def act4_1 (q : R) (v : Fin 15 → R) : Fin 15 → R :=
  ![v 1 + (q - q⁻¹) * v 0, v 0, q * v 2, q * v 3, v 5 + (q - q⁻¹) * v 4, v 4, q * v 6, v 8 + (q - q⁻¹) * v 7, v 7, q * v 9, q * v 10, v 12 + (q - q⁻¹) * v 11, v 11, q * v 13, q * v 14]
theorem bridge4_1 (q : R) (v : Fin 15 → R) :
    (gW q idx4 (1, false)).mulVec v = act4_1 q v := by
  funext t; fin_cases t <;>
    simp +decide [gW, g64, gen64, Matrix.mulVec, dotProduct, Fin.sum_univ_succ, idx4, act4_1] <;> (try ring)

/-- `σ_2` on the 4-zero weight space, row by row. -/
def act4_2 (q : R) (v : Fin 15 → R) : Fin 15 → R :=
  ![q * v 0, v 3 + (q - q⁻¹) * v 1, v 4 + (q - q⁻¹) * v 2, v 1, v 2, q * v 5, q * v 6, q * v 7, v 9 + (q - q⁻¹) * v 8, v 8, q * v 10, q * v 11, v 13 + (q - q⁻¹) * v 12, v 12, q * v 14]
theorem bridge4_2 (q : R) (v : Fin 15 → R) :
    (gW q idx4 (2, false)).mulVec v = act4_2 q v := by
  funext t; fin_cases t <;>
    simp +decide [gW, g64, gen64, Matrix.mulVec, dotProduct, Fin.sum_univ_succ, idx4, act4_2] <;> (try ring)

/-- `σ_3` on the 4-zero weight space, row by row. -/
def act4_3 (q : R) (v : Fin 15 → R) : Fin 15 → R :=
  ![q * v 0, q * v 1, q * v 2, v 6 + (q - q⁻¹) * v 3, v 7 + (q - q⁻¹) * v 4, v 8 + (q - q⁻¹) * v 5, v 3, v 4, v 5, q * v 9, q * v 10, q * v 11, q * v 12, v 14 + (q - q⁻¹) * v 13, v 13]
theorem bridge4_3 (q : R) (v : Fin 15 → R) :
    (gW q idx4 (3, false)).mulVec v = act4_3 q v := by
  funext t; fin_cases t <;>
    simp +decide [gW, g64, gen64, Matrix.mulVec, dotProduct, Fin.sum_univ_succ, idx4, act4_3] <;> (try ring)

/-- `σ_4` on the 4-zero weight space, row by row. -/
def act4_4 (q : R) (v : Fin 15 → R) : Fin 15 → R :=
  ![q * v 0, q * v 1, q * v 2, q * v 3, q * v 4, q * v 5, v 10 + (q - q⁻¹) * v 6, v 11 + (q - q⁻¹) * v 7, v 12 + (q - q⁻¹) * v 8, v 13 + (q - q⁻¹) * v 9, v 6, v 7, v 8, v 9, q * v 14]
theorem bridge4_4 (q : R) (v : Fin 15 → R) :
    (gW q idx4 (4, false)).mulVec v = act4_4 q v := by
  funext t; fin_cases t <;>
    simp +decide [gW, g64, gen64, Matrix.mulVec, dotProduct, Fin.sum_univ_succ, idx4, act4_4] <;> (try ring)

/-! ### The weight space with 5 zeros (dimension 6) -/

/-- The states with 5 zeros, in increasing order. -/
def idx5 : Fin 6 → Fin 64 := ![1, 2, 4, 8, 16, 32]
theorem idx5_inj : Function.Injective idx5 := by decide
theorem idx5_sc : ∀ i : Fin 5, SwapClosed idx5 i.val := by unfold SwapClosed; decide +kernel

/-- `σ_0` on the 5-zero weight space, row by row. -/
def act5_0 (q : R) (v : Fin 6 → R) : Fin 6 → R :=
  ![v 1 + (q - q⁻¹) * v 0, v 0, q * v 2, q * v 3, q * v 4, q * v 5]
theorem bridge5_0 (q : R) (v : Fin 6 → R) :
    (gW q idx5 (0, false)).mulVec v = act5_0 q v := by
  funext t; fin_cases t <;>
    simp +decide [gW, g64, gen64, Matrix.mulVec, dotProduct, Fin.sum_univ_succ, idx5, act5_0] <;> (try ring)

/-- `σ_1` on the 5-zero weight space, row by row. -/
def act5_1 (q : R) (v : Fin 6 → R) : Fin 6 → R :=
  ![q * v 0, v 2 + (q - q⁻¹) * v 1, v 1, q * v 3, q * v 4, q * v 5]
theorem bridge5_1 (q : R) (v : Fin 6 → R) :
    (gW q idx5 (1, false)).mulVec v = act5_1 q v := by
  funext t; fin_cases t <;>
    simp +decide [gW, g64, gen64, Matrix.mulVec, dotProduct, Fin.sum_univ_succ, idx5, act5_1] <;> (try ring)

/-- `σ_2` on the 5-zero weight space, row by row. -/
def act5_2 (q : R) (v : Fin 6 → R) : Fin 6 → R :=
  ![q * v 0, q * v 1, v 3 + (q - q⁻¹) * v 2, v 2, q * v 4, q * v 5]
theorem bridge5_2 (q : R) (v : Fin 6 → R) :
    (gW q idx5 (2, false)).mulVec v = act5_2 q v := by
  funext t; fin_cases t <;>
    simp +decide [gW, g64, gen64, Matrix.mulVec, dotProduct, Fin.sum_univ_succ, idx5, act5_2] <;> (try ring)

/-- `σ_3` on the 5-zero weight space, row by row. -/
def act5_3 (q : R) (v : Fin 6 → R) : Fin 6 → R :=
  ![q * v 0, q * v 1, q * v 2, v 4 + (q - q⁻¹) * v 3, v 3, q * v 5]
theorem bridge5_3 (q : R) (v : Fin 6 → R) :
    (gW q idx5 (3, false)).mulVec v = act5_3 q v := by
  funext t; fin_cases t <;>
    simp +decide [gW, g64, gen64, Matrix.mulVec, dotProduct, Fin.sum_univ_succ, idx5, act5_3] <;> (try ring)

/-- `σ_4` on the 5-zero weight space, row by row. -/
def act5_4 (q : R) (v : Fin 6 → R) : Fin 6 → R :=
  ![q * v 0, q * v 1, q * v 2, q * v 3, v 5 + (q - q⁻¹) * v 4, v 4]
theorem bridge5_4 (q : R) (v : Fin 6 → R) :
    (gW q idx5 (4, false)).mulVec v = act5_4 q v := by
  funext t; fin_cases t <;>
    simp +decide [gW, g64, gen64, Matrix.mulVec, dotProduct, Fin.sum_univ_succ, idx5, act5_4] <;> (try ring)

/-! ### The functional on the full space -/

/-- Number of zeros (`false` bits) of `s` on the strands in `js`. -/
def zerosIn (js : List ℕ) (s : Fin 64) : ℕ := (js.filter (fun j => !s.val.testBit j)).length

/-- Table of `zerosIn [0, 1, 2, 3, 4, 5]`. -/
def zTab : Fin 64 → ℕ := ![6, 5, 5, 4, 5, 4, 4, 3, 5, 4, 4, 3, 4, 3, 3, 2, 5, 4, 4, 3, 4, 3, 3, 2, 4, 3, 3, 2, 3, 2, 2, 1, 5, 4, 4, 3, 4, 3, 3, 2, 4, 3, 3, 2, 3, 2, 2, 1, 4, 3, 3, 2, 3, 2, 2, 1, 3, 2, 2, 1, 2, 1, 1, 0]
/-- Table of `zerosIn [0, 1, 2]`. -/
def pLTab : Fin 64 → ℕ := ![3, 2, 2, 1, 2, 1, 1, 0, 3, 2, 2, 1, 2, 1, 1, 0, 3, 2, 2, 1, 2, 1, 1, 0, 3, 2, 2, 1, 2, 1, 1, 0, 3, 2, 2, 1, 2, 1, 1, 0, 3, 2, 2, 1, 2, 1, 1, 0, 3, 2, 2, 1, 2, 1, 1, 0, 3, 2, 2, 1, 2, 1, 1, 0]
/-- Table of `zerosIn [3, 4, 5]`. -/
def pRTab : Fin 64 → ℕ := ![3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]
theorem zeros6_eq : ∀ s, zerosIn [0, 1, 2, 3, 4, 5] s = zTab s := by decide +kernel
theorem zerosL_eq : ∀ s, zerosIn [0, 1, 2] s = pLTab s := by decide +kernel
theorem zerosR_eq : ∀ s, zerosIn [3, 4, 5] s = pRTab s := by decide +kernel

/-- `F(O₊) = Σ_s T³(s)·W s s` over the states whose proton strands `js` carry two zeros;
`T³ = (#0 − #1)/2 = #0 − 3`. -/
def Fp64 (js : List ℕ) (W : Matrix (Fin 64) (Fin 64) R) : R :=
  ∑ s, if zerosIn js s = 2 then (((zerosIn [0, 1, 2, 3, 4, 5] s : ℕ) : R) - 3) * W s s else 0
/-- `F(O₋)`: the proton strands carry one zero. -/
def Fm64 (js : List ℕ) (W : Matrix (Fin 64) (Fin 64) R) : R :=
  ∑ s, if zerosIn js s = 1 then (((zerosIn [0, 1, 2, 3, 4, 5] s : ℕ) : R) - 3) * W s s else 0

set_option maxRecDepth 20000 in
theorem Fp64_L_eq (W : Matrix (Fin 64) (Fin 64) R) :
    Fp64 [0, 1, 2] W = 2 * W 1 1 + 2 * W 2 2 + 2 * W 4 4 + W 9 9 + W 10 10 + W 12 12 + W 17 17 + W 18 18 + W 20 20 + W 33 33 + W 34 34 + W 36 36 - W 57 57 - W 58 58 - W 60 60 := by
  simp only [Fp64, zeros6_eq, zerosL_eq, Fin.sum_univ_succ, Fin.sum_univ_zero]
  simp [zTab, pLTab, Fin.succ]
  norm_num; ring

/-- **Reduction, proton on strands `0–2`.** For every word, `F(O₊)` on the full space is a sum of
weight-space diagonal entries. -/
theorem Fp_L_reduction (q : R) (w : List Letter) :
    Fp64 [0, 1, 2] (word64 q w) = 2 * wordW q idx5 w 0 0 + 2 * wordW q idx5 w 1 1 + 2 * wordW q idx5 w 2 2 + wordW q idx4 w 3 3 + wordW q idx4 w 4 4 + wordW q idx4 w 5 5 + wordW q idx4 w 6 6 + wordW q idx4 w 7 7 + wordW q idx4 w 8 8 + wordW q idx4 w 10 10 + wordW q idx4 w 11 11 + wordW q idx4 w 12 12 - wordW q idx2 w 12 12 - wordW q idx2 w 13 13 - wordW q idx2 w 14 14 := by
  rw [Fp64_L_eq]
  have e0 : word64 q w 1 1 = wordW q idx5 w 0 0 := diag_word q idx5 idx5_inj idx5_sc w 0
  have e1 : word64 q w 2 2 = wordW q idx5 w 1 1 := diag_word q idx5 idx5_inj idx5_sc w 1
  have e2 : word64 q w 4 4 = wordW q idx5 w 2 2 := diag_word q idx5 idx5_inj idx5_sc w 2
  have e3 : word64 q w 9 9 = wordW q idx4 w 3 3 := diag_word q idx4 idx4_inj idx4_sc w 3
  have e4 : word64 q w 10 10 = wordW q idx4 w 4 4 := diag_word q idx4 idx4_inj idx4_sc w 4
  have e5 : word64 q w 12 12 = wordW q idx4 w 5 5 := diag_word q idx4 idx4_inj idx4_sc w 5
  have e6 : word64 q w 17 17 = wordW q idx4 w 6 6 := diag_word q idx4 idx4_inj idx4_sc w 6
  have e7 : word64 q w 18 18 = wordW q idx4 w 7 7 := diag_word q idx4 idx4_inj idx4_sc w 7
  have e8 : word64 q w 20 20 = wordW q idx4 w 8 8 := diag_word q idx4 idx4_inj idx4_sc w 8
  have e9 : word64 q w 33 33 = wordW q idx4 w 10 10 := diag_word q idx4 idx4_inj idx4_sc w 10
  have e10 : word64 q w 34 34 = wordW q idx4 w 11 11 := diag_word q idx4 idx4_inj idx4_sc w 11
  have e11 : word64 q w 36 36 = wordW q idx4 w 12 12 := diag_word q idx4 idx4_inj idx4_sc w 12
  have e12 : word64 q w 57 57 = wordW q idx2 w 12 12 := diag_word q idx2 idx2_inj idx2_sc w 12
  have e13 : word64 q w 58 58 = wordW q idx2 w 13 13 := diag_word q idx2 idx2_inj idx2_sc w 13
  have e14 : word64 q w 60 60 = wordW q idx2 w 14 14 := diag_word q idx2 idx2_inj idx2_sc w 14
  rw [e0, e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12, e13, e14]

set_option maxRecDepth 20000 in
theorem Fm64_L_eq (W : Matrix (Fin 64) (Fin 64) R) :
    Fm64 [0, 1, 2] W = W 3 3 + W 5 5 + W 6 6 - W 27 27 - W 29 29 - W 30 30 - W 43 43 - W 45 45 - W 46 46 - W 51 51 - W 53 53 - W 54 54 - 2 * W 59 59 - 2 * W 61 61 - 2 * W 62 62 := by
  simp only [Fm64, zeros6_eq, zerosL_eq, Fin.sum_univ_succ, Fin.sum_univ_zero]
  simp [zTab, pLTab, Fin.succ]
  norm_num; ring

/-- **Reduction, proton on strands `0–2`.** For every word, `F(O₋)` on the full space is a sum of
weight-space diagonal entries. -/
theorem Fm_L_reduction (q : R) (w : List Letter) :
    Fm64 [0, 1, 2] (word64 q w) = wordW q idx4 w 0 0 + wordW q idx4 w 1 1 + wordW q idx4 w 2 2 - wordW q idx2 w 2 2 - wordW q idx2 w 3 3 - wordW q idx2 w 4 4 - wordW q idx2 w 6 6 - wordW q idx2 w 7 7 - wordW q idx2 w 8 8 - wordW q idx2 w 9 9 - wordW q idx2 w 10 10 - wordW q idx2 w 11 11 - 2 * wordW q idx1 w 3 3 - 2 * wordW q idx1 w 4 4 - 2 * wordW q idx1 w 5 5 := by
  rw [Fm64_L_eq]
  have e0 : word64 q w 3 3 = wordW q idx4 w 0 0 := diag_word q idx4 idx4_inj idx4_sc w 0
  have e1 : word64 q w 5 5 = wordW q idx4 w 1 1 := diag_word q idx4 idx4_inj idx4_sc w 1
  have e2 : word64 q w 6 6 = wordW q idx4 w 2 2 := diag_word q idx4 idx4_inj idx4_sc w 2
  have e3 : word64 q w 27 27 = wordW q idx2 w 2 2 := diag_word q idx2 idx2_inj idx2_sc w 2
  have e4 : word64 q w 29 29 = wordW q idx2 w 3 3 := diag_word q idx2 idx2_inj idx2_sc w 3
  have e5 : word64 q w 30 30 = wordW q idx2 w 4 4 := diag_word q idx2 idx2_inj idx2_sc w 4
  have e6 : word64 q w 43 43 = wordW q idx2 w 6 6 := diag_word q idx2 idx2_inj idx2_sc w 6
  have e7 : word64 q w 45 45 = wordW q idx2 w 7 7 := diag_word q idx2 idx2_inj idx2_sc w 7
  have e8 : word64 q w 46 46 = wordW q idx2 w 8 8 := diag_word q idx2 idx2_inj idx2_sc w 8
  have e9 : word64 q w 51 51 = wordW q idx2 w 9 9 := diag_word q idx2 idx2_inj idx2_sc w 9
  have e10 : word64 q w 53 53 = wordW q idx2 w 10 10 := diag_word q idx2 idx2_inj idx2_sc w 10
  have e11 : word64 q w 54 54 = wordW q idx2 w 11 11 := diag_word q idx2 idx2_inj idx2_sc w 11
  have e12 : word64 q w 59 59 = wordW q idx1 w 3 3 := diag_word q idx1 idx1_inj idx1_sc w 3
  have e13 : word64 q w 61 61 = wordW q idx1 w 4 4 := diag_word q idx1 idx1_inj idx1_sc w 4
  have e14 : word64 q w 62 62 = wordW q idx1 w 5 5 := diag_word q idx1 idx1_inj idx1_sc w 5
  rw [e0, e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12, e13, e14]

set_option maxRecDepth 20000 in
theorem Fp64_R_eq (W : Matrix (Fin 64) (Fin 64) R) :
    Fp64 [3, 4, 5] W = 2 * W 8 8 + W 9 9 + W 10 10 + W 12 12 - W 15 15 + 2 * W 16 16 + W 17 17 + W 18 18 + W 20 20 - W 23 23 + 2 * W 32 32 + W 33 33 + W 34 34 + W 36 36 - W 39 39 := by
  simp only [Fp64, zeros6_eq, zerosR_eq, Fin.sum_univ_succ, Fin.sum_univ_zero]
  simp [zTab, pRTab, Fin.succ]
  norm_num; ring

/-- **Reduction, proton on strands `3–5`.** For every word, `F(O₊)` on the full space is a sum of
weight-space diagonal entries. -/
theorem Fp_R_reduction (q : R) (w : List Letter) :
    Fp64 [3, 4, 5] (word64 q w) = 2 * wordW q idx5 w 3 3 + wordW q idx4 w 3 3 + wordW q idx4 w 4 4 + wordW q idx4 w 5 5 - wordW q idx2 w 0 0 + 2 * wordW q idx5 w 4 4 + wordW q idx4 w 6 6 + wordW q idx4 w 7 7 + wordW q idx4 w 8 8 - wordW q idx2 w 1 1 + 2 * wordW q idx5 w 5 5 + wordW q idx4 w 10 10 + wordW q idx4 w 11 11 + wordW q idx4 w 12 12 - wordW q idx2 w 5 5 := by
  rw [Fp64_R_eq]
  have e0 : word64 q w 8 8 = wordW q idx5 w 3 3 := diag_word q idx5 idx5_inj idx5_sc w 3
  have e1 : word64 q w 9 9 = wordW q idx4 w 3 3 := diag_word q idx4 idx4_inj idx4_sc w 3
  have e2 : word64 q w 10 10 = wordW q idx4 w 4 4 := diag_word q idx4 idx4_inj idx4_sc w 4
  have e3 : word64 q w 12 12 = wordW q idx4 w 5 5 := diag_word q idx4 idx4_inj idx4_sc w 5
  have e4 : word64 q w 15 15 = wordW q idx2 w 0 0 := diag_word q idx2 idx2_inj idx2_sc w 0
  have e5 : word64 q w 16 16 = wordW q idx5 w 4 4 := diag_word q idx5 idx5_inj idx5_sc w 4
  have e6 : word64 q w 17 17 = wordW q idx4 w 6 6 := diag_word q idx4 idx4_inj idx4_sc w 6
  have e7 : word64 q w 18 18 = wordW q idx4 w 7 7 := diag_word q idx4 idx4_inj idx4_sc w 7
  have e8 : word64 q w 20 20 = wordW q idx4 w 8 8 := diag_word q idx4 idx4_inj idx4_sc w 8
  have e9 : word64 q w 23 23 = wordW q idx2 w 1 1 := diag_word q idx2 idx2_inj idx2_sc w 1
  have e10 : word64 q w 32 32 = wordW q idx5 w 5 5 := diag_word q idx5 idx5_inj idx5_sc w 5
  have e11 : word64 q w 33 33 = wordW q idx4 w 10 10 := diag_word q idx4 idx4_inj idx4_sc w 10
  have e12 : word64 q w 34 34 = wordW q idx4 w 11 11 := diag_word q idx4 idx4_inj idx4_sc w 11
  have e13 : word64 q w 36 36 = wordW q idx4 w 12 12 := diag_word q idx4 idx4_inj idx4_sc w 12
  have e14 : word64 q w 39 39 = wordW q idx2 w 5 5 := diag_word q idx2 idx2_inj idx2_sc w 5
  rw [e0, e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12, e13, e14]

set_option maxRecDepth 20000 in
theorem Fm64_R_eq (W : Matrix (Fin 64) (Fin 64) R) :
    Fm64 [3, 4, 5] W = W 24 24 - W 27 27 - W 29 29 - W 30 30 - 2 * W 31 31 + W 40 40 - W 43 43 - W 45 45 - W 46 46 - 2 * W 47 47 + W 48 48 - W 51 51 - W 53 53 - W 54 54 - 2 * W 55 55 := by
  simp only [Fm64, zeros6_eq, zerosR_eq, Fin.sum_univ_succ, Fin.sum_univ_zero]
  simp [zTab, pRTab, Fin.succ]
  norm_num; ring

/-- **Reduction, proton on strands `3–5`.** For every word, `F(O₋)` on the full space is a sum of
weight-space diagonal entries. -/
theorem Fm_R_reduction (q : R) (w : List Letter) :
    Fm64 [3, 4, 5] (word64 q w) = wordW q idx4 w 9 9 - wordW q idx2 w 2 2 - wordW q idx2 w 3 3 - wordW q idx2 w 4 4 - 2 * wordW q idx1 w 0 0 + wordW q idx4 w 13 13 - wordW q idx2 w 6 6 - wordW q idx2 w 7 7 - wordW q idx2 w 8 8 - 2 * wordW q idx1 w 1 1 + wordW q idx4 w 14 14 - wordW q idx2 w 9 9 - wordW q idx2 w 10 10 - wordW q idx2 w 11 11 - 2 * wordW q idx1 w 2 2 := by
  rw [Fm64_R_eq]
  have e0 : word64 q w 24 24 = wordW q idx4 w 9 9 := diag_word q idx4 idx4_inj idx4_sc w 9
  have e1 : word64 q w 27 27 = wordW q idx2 w 2 2 := diag_word q idx2 idx2_inj idx2_sc w 2
  have e2 : word64 q w 29 29 = wordW q idx2 w 3 3 := diag_word q idx2 idx2_inj idx2_sc w 3
  have e3 : word64 q w 30 30 = wordW q idx2 w 4 4 := diag_word q idx2 idx2_inj idx2_sc w 4
  have e4 : word64 q w 31 31 = wordW q idx1 w 0 0 := diag_word q idx1 idx1_inj idx1_sc w 0
  have e5 : word64 q w 40 40 = wordW q idx4 w 13 13 := diag_word q idx4 idx4_inj idx4_sc w 13
  have e6 : word64 q w 43 43 = wordW q idx2 w 6 6 := diag_word q idx2 idx2_inj idx2_sc w 6
  have e7 : word64 q w 45 45 = wordW q idx2 w 7 7 := diag_word q idx2 idx2_inj idx2_sc w 7
  have e8 : word64 q w 46 46 = wordW q idx2 w 8 8 := diag_word q idx2 idx2_inj idx2_sc w 8
  have e9 : word64 q w 47 47 = wordW q idx1 w 1 1 := diag_word q idx1 idx1_inj idx1_sc w 1
  have e10 : word64 q w 48 48 = wordW q idx4 w 14 14 := diag_word q idx4 idx4_inj idx4_sc w 14
  have e11 : word64 q w 51 51 = wordW q idx2 w 9 9 := diag_word q idx2 idx2_inj idx2_sc w 9
  have e12 : word64 q w 53 53 = wordW q idx2 w 10 10 := diag_word q idx2 idx2_inj idx2_sc w 10
  have e13 : word64 q w 54 54 = wordW q idx2 w 11 11 := diag_word q idx2 idx2_inj idx2_sc w 11
  have e14 : word64 q w 55 55 = wordW q idx1 w 2 2 := diag_word q idx1 idx1_inj idx1_sc w 2
  rw [e0, e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12, e13, e14]

set_option hygiene false in
macro "stepTac" : tactic => `(tactic| (funext t; fin_cases t <;>
  simp [act1_0, act1_1, act1_2, act1_3, act1_4, act2_0, act2_1, act2_2, act2_3, act2_4,
    act4_0, act4_1, act4_2, act4_3, act4_4, act5_0, act5_1, act5_2, act5_3, act5_4,
    Pi.single_apply] <;> (try field_simp) <;> (try ring)))

end QOU.BraidsAndKnots.BondChiralitySixStrand
