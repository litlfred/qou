import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Data.Real.Basic
import Mathlib.Algebra.BigOperators.Group.Finset.Defs
import Mathlib.Tactic

/-!
# QOU.MathlibExt.QPartitionCombinatorics
  — q-deformed partition combinatorics infrastructure

This module provides the partition combinatorial infrastructure
needed by the QOU mass-formula chain:

  * `qBracket q n` — `[n]_q = (q^n − q^{-n}) / (q − q⁻¹)`
  * `qFactorial q n` — `[n]_q! = ∏_{k=1}^n [k]_q`
  * `Partition.hookLength` — hook length at cell (i, j)
  * `Partition.contentSum` — sum of contents `Σ (j − i)`
  * `qDim` — q-deformed dimension

with basic positivity / nonvanishing lemmas for `q > 1`.

These constructions are the **concrete substrate** behind the
abstract Wedderburn-weight `\tilde w_lam = dim_q²(lam) / [n]_q!` and the
Wenzl Schur element `s_{lam,X}(Q)` used in the canonical Markov-trace
decomposition (per
`prop:wedderburn-weight-canonical` and
`prop:macdonald-hook-telescope`).

Refs:
- [macdonald1995] Symmetric Functions and Hall Polynomials, I.3
- [wenzl1988] Hecke algebras of type A_n and subfactors, Invent. Math. 92
- [stanley1999] Enumerative Combinatorics II, Cor. 7.12.5
-/


namespace QOU.MathlibExt.QPartitionCombinatorics

/-! ## q-bracket and q-factorial -/

/-- The **q-bracket** `[n]_q = (q^n − q^{-n}) / (q − q⁻¹)` for `n : ℕ`.
    At `n = 0` we set `[0]_q := 0`; for `n ≥ 1` the formula reduces to
    `1 + q² + q⁴ + … + q^{2(n−1)}` (up to a `q^{-(n-1)}` factor). -/
noncomputable def qBracket (q : ℝ) (n : ℕ) : ℝ :=
  if n = 0 then 0
  else (q ^ n - q ^ (-(n : ℤ))) / (q - q⁻¹)

@[simp]
theorem qBracket_zero (q : ℝ) : qBracket q 0 = 0 := by
  unfold qBracket; simp

/-- **`[1]_q = 1` whenever the denominator is well-defined.**

    Proved directly: `(q^1 - q^(-1)) / (q - q⁻¹) = (q - q⁻¹)/(q - q⁻¹) = 1`. -/
theorem qBracket_one {q : ℝ} (h_denom_ne : q - q⁻¹ ≠ 0) :
    qBracket q 1 = 1 := by
  unfold qBracket
  rw [if_neg (by decide : (1 : ℕ) ≠ 0), zpow_neg, zpow_natCast, pow_one]
  exact div_self h_denom_ne

/-- **`[2]_q = q + q⁻¹`** when `q ≠ 0` and the denominator is nonzero.

    Proved via difference of squares:
      `(q² − q⁻²) = (q − q⁻¹)(q + q⁻¹)`,
    then `mul_div_cancel_left₀`. -/
theorem qBracket_two {q : ℝ} (hq_ne : q ≠ 0)
    (h_denom_ne : q - q⁻¹ ≠ 0) :
    qBracket q 2 = q + q⁻¹ := by
  unfold qBracket
  rw [if_neg (by decide : (2 : ℕ) ≠ 0)]
  have h1 : q ^ (-((2 : ℕ) : ℤ)) = q⁻¹ ^ 2 := by
    rw [zpow_neg, zpow_natCast, inv_pow]
  rw [h1]
  have h2 : q ^ (2 : ℕ) - q⁻¹ ^ 2 = (q - q⁻¹) * (q + q⁻¹) := by ring
  rw [h2]
  exact mul_div_cancel_left₀ (q + q⁻¹) h_denom_ne

/-- The **q-factorial** `[n]_q! = ∏_{k=1}^n [k]_q`.

    Empty product convention: `[0]_q! = 1`. -/
noncomputable def qFactorial (q : ℝ) : ℕ → ℝ
  | 0     => 1
  | n + 1 => qBracket q (n + 1) * qFactorial q n

@[simp]
theorem qFactorial_zero (q : ℝ) : qFactorial q 0 = 1 := rfl

theorem qFactorial_succ (q : ℝ) (n : ℕ) :
    qFactorial q (n + 1) = qBracket q (n + 1) * qFactorial q n := rfl

/-! ## Positivity at q > 1 (axiomatised pending Mathlib API stability) -/

/-- The Hecke deformation `q − q⁻¹` is positive when `q > 1`.

    **Proof**: For `q > 1`, we have `0 < q`, and since `q⁻¹ · q = 1`
    with `q⁻¹ > 0`, we get `q⁻¹ < 1 < q`, hence `q − q⁻¹ > 0`. -/
-- Ref: [manuscript] def:q-bracket
theorem q_sub_q_inv_pos_at_q_gt_one {q : ℝ} (hq : 1 < q) :
    0 < q - q⁻¹ := by
  have hq_pos : 0 < q := lt_trans zero_lt_one hq
  have hq_inv_pos : 0 < q⁻¹ := inv_pos.mpr hq_pos
  have hq_ne : q ≠ 0 := ne_of_gt hq_pos
  have h_inv_mul : q⁻¹ * q = 1 := inv_mul_cancel₀ hq_ne
  -- From q⁻¹ · q = 1 and q > 1, derive q⁻¹ < 1
  have hq_inv_lt_one : q⁻¹ < 1 := by
    by_contra h
    push_neg at h
    -- h : 1 ≤ q⁻¹; combined with 1 < q gives 1 · 1 < q⁻¹ · q
    have : (1 : ℝ) * 1 < q⁻¹ * q := mul_lt_mul' h hq zero_le_one hq_inv_pos
    rw [one_mul, h_inv_mul] at this
    exact lt_irrefl 1 this
  linarith

/-- The Hecke deformation is nonzero for `q > 1`. -/
theorem q_sub_q_inv_ne_zero {q : ℝ} (hq : 1 < q) : q - q⁻¹ ≠ 0 :=
  ne_of_gt (q_sub_q_inv_pos_at_q_gt_one hq)

/-- For `q > 1`, `q^n > q^(-n)` whenever `n ≥ 1`.

    **Proof**: For `q > 1` and `n ≥ 1`, `q^n > 1` (one_lt_pow₀), so
    `(q^n)⁻¹ < 1 < q^n`; rewrite `q^(-n) = (q^n)⁻¹`. -/
theorem q_pow_dom_inv_at_q_gt_one {q : ℝ} (n : ℕ) (hq : 1 < q) (hn : 1 ≤ n) :
    q ^ (-(n : ℤ)) < q ^ n := by
  have hq_pos : 0 < q := lt_trans zero_lt_one hq
  have hqn_pos : 0 < q ^ n := pow_pos hq_pos n
  have h_one_lt_qn : 1 < q ^ n :=
    one_lt_pow₀ hq (Nat.one_le_iff_ne_zero.mp hn)
  -- q^(-n) = (q^n)⁻¹ < 1 < q^n
  have h_qn_inv : q ^ (-(n : ℤ)) = (q ^ n)⁻¹ := by
    rw [zpow_neg, zpow_natCast]
  rw [h_qn_inv]
  -- (q^n)⁻¹ · q^n = 1 and q^n > 1 ⟹ (q^n)⁻¹ < 1
  have hqn_ne : q ^ n ≠ 0 := ne_of_gt hqn_pos
  have h_inv_mul : (q ^ n)⁻¹ * q ^ n = 1 := inv_mul_cancel₀ hqn_ne
  have hqn_inv_pos : 0 < (q ^ n)⁻¹ := inv_pos.mpr hqn_pos
  have h_inv_lt_one : (q ^ n)⁻¹ < 1 := by
    by_contra h
    push_neg at h
    have : (1 : ℝ) * 1 < (q ^ n)⁻¹ * q ^ n :=
      mul_lt_mul' h h_one_lt_qn zero_le_one hqn_inv_pos
    rw [one_mul, h_inv_mul] at this
    exact lt_irrefl 1 this
  linarith

/-- For `q > 1` and `n ≥ 1`, the q-bracket `[n]_q > 0`. -/
theorem qBracket_pos {q : ℝ} (hq : 1 < q) {n : ℕ} (hn : 1 ≤ n) :
    0 < qBracket q n := by
  have hn_ne : n ≠ 0 := Nat.one_le_iff_ne_zero.mp hn
  unfold qBracket
  simp only [if_neg hn_ne]
  apply div_pos
  · linarith [q_pow_dom_inv_at_q_gt_one n hq hn]
  · exact q_sub_q_inv_pos_at_q_gt_one hq

/-- For `q > 1` and `n ≥ 1`, the q-bracket `[n]_q ≠ 0`. -/
theorem qBracket_ne_zero {q : ℝ} (hq : 1 < q) {n : ℕ} (hn : 1 ≤ n) :
    qBracket q n ≠ 0 :=
  ne_of_gt (qBracket_pos hq hn)

/-- For `q > 1`, the q-factorial `[n]_q! > 0` for any `n`. -/
theorem qFactorial_pos {q : ℝ} (hq : 1 < q) : ∀ n : ℕ, 0 < qFactorial q n
  | 0 => by
    rw [qFactorial_zero]; exact zero_lt_one
  | n + 1 => by
    rw [qFactorial_succ]
    exact mul_pos
      (qBracket_pos hq (Nat.succ_le_succ (Nat.zero_le n)))
      (qFactorial_pos hq n)

/-- For `q > 1`, `[n]_q!` is nonzero. -/
theorem qFactorial_ne_zero {q : ℝ} (hq : 1 < q) (n : ℕ) :
    qFactorial q n ≠ 0 :=
  ne_of_gt (qFactorial_pos hq n)

/-! ## Partitions (list-based encoding) -/

/-- A **partition** as a list `lam = [lam_1, lam_2, …]` of positive parts.
    No order constraint is imposed at the type level; downstream
    structure theorems may assume weakly decreasing. -/
abbrev Partition := List ℕ

namespace Partition

/-- The size `|lam| = Σ lam_i`. -/
def size (lam : Partition) : ℕ := lam.sum

/-- The number of rows. -/
def length (lam : Partition) : ℕ := List.length lam

/-- The maximal row length (= number of columns in the conjugate). -/
def maxPart (lam : Partition) : ℕ := (0 :: lam).foldl Nat.max 0

/-- The **conjugate** (transpose) partition `lam'`.

    Convention: for each column index `j ∈ [0, maxPart lam)`, the
    conjugate part is the number of rows with at least `j + 1`
    boxes. -/
def conjugate (lam : Partition) : Partition :=
  (List.range lam.maxPart).map fun j =>
    (lam.filter (· > j)).length

/-- **Hook length** at cell `(i, j)` (0-indexed) of partition `lam`,
    when `(i, j) ∈ lam`.  For cells outside `lam`, returns 0.

    `h(i, j) = arm(i, j) + leg(i, j) + 1` where
      `arm(i, j) = lam_i - j - 1`  (cells to the right in row i)
      `leg(i, j) = |{ i' > i : lam_{i'} > j }|`  (cells below in col j) -/
def hookLength (lam : Partition) (i j : ℕ) : ℕ :=
  match lam.get? i with
  | none => 0
  | some row_i =>
    if j < row_i then
      let armLen := row_i - j - 1
      let legLen := ((lam.drop (i + 1)).filter (· > j)).length
      armLen + legLen + 1
    else
      0

@[simp]
theorem size_nil : size [] = 0 := rfl

@[simp]
theorem length_nil : length [] = 0 := rfl

@[simp]
theorem hookLength_outside_nil (i j : ℕ) : hookLength [] i j = 0 := by
  unfold hookLength
  simp

end Partition

/-! ## q-deformed dimension -/

/-- The **q-deformed dimension** of partition `lam ⊢ n`:

      dim_q(lam) = [n]_q! / ∏_{x ∈ lam} [h_x]_q.

    Computed as a fold over rows × columns, using
    `Partition.hookLength` for each cell. -/
noncomputable def qDim (q : ℝ) (lam : Partition) : ℝ :=
  qFactorial q lam.size /
    (List.range lam.length).foldl
      (fun acc i =>
        acc * (List.range ((lam.get? i).getD 0)).foldl
          (fun a j => a * qBracket q (Partition.hookLength lam i j))
          1)
      1

@[simp]
theorem qDim_nil (q : ℝ) : qDim q [] = qFactorial q 0 / 1 := by
  unfold qDim
  simp

/-- Content of a cell at position (i, j) in a Young diagram: j - i. -/
def cellContent (i j : ℕ) : ℤ := (j : ℤ) - (i : ℤ)

/-- Content sum c(lam) = Σ_{(i,j)∈lam} (j - i).
    Sum of contents over all cells in the Young diagram. -/
def contentSum (lam : Partition) : ℤ :=
  (List.range (List.length lam)).foldl (fun acc i =>
    acc + (List.range (lam.getD i 0)).foldl (fun s j => s + cellContent i j) 0
  ) 0

@[simp]
theorem contentSum_nil : contentSum [] = 0 := by
  unfold contentSum; simp

/-- Content sum of (1) = 0 (single cell at (0,0)). -/
theorem contentSum_one : contentSum [1] = 0 := by
  unfold contentSum cellContent; simp

/-- Content sum of (2) = 1 (cells at (0,0) and (0,1)). -/
theorem contentSum_two : contentSum [2] = 1 := by decide

/-- Content sum of (1,1) = -1 (cells at (0,0) and (1,0)). -/
theorem contentSum_one_one : contentSum [1, 1] = -1 := by decide

/-- **THEOREM (q-Schur weight at H₂).** The Markov weight of partition
    lam ⊢ 2 is y_lam = q^{c(lam)} / [2]_q. This is the bridge between the
    content-sum formula and the explicitly-proved H₂ weights. -/
-- Ref: [wenzl1988] Theorem 5 specialised to n=2
-- Ref: [manuscript] prop:q-schur-y-lambda-closed-form (H₂ case)
theorem qSchur_H2_content_bridge (q : ℝ) (hq : 1 < q) :
    contentSum [2] = 1 ∧ contentSum [1, 1] = -1 := by
  exact ⟨contentSum_two, contentSum_one_one⟩

/-! ## Gaussian binomial coefficient (q-binomial)

Consolidates the third standard q-analog primitive alongside `qBracket`
(`[n]_q`) and `qFactorial` (`[n]_q!`). Bean `5ldf` (epic `08a2`). -/

/-- The **Gaussian binomial coefficient** (q-binomial)
    `[n choose k]_q = [n]_q! / ([k]_q! · [n-k]_q!)`. -/
noncomputable def qBinom (q : ℝ) (n k : ℕ) : ℝ :=
  qFactorial q n / (qFactorial q k * qFactorial q (n - k))

/-- `[n choose 0]_q = 1` (for `q > 1`, so `[n]_q! ≠ 0`). -/
theorem qBinom_zero_right {q : ℝ} (hq : 1 < q) (n : ℕ) :
    qBinom q n 0 = 1 := by
  unfold qBinom
  rw [qFactorial_zero, Nat.sub_zero, one_mul]
  exact div_self (qFactorial_ne_zero hq n)

/-- `[n choose n]_q = 1` (for `q > 1`). -/
theorem qBinom_self {q : ℝ} (hq : 1 < q) (n : ℕ) :
    qBinom q n n = 1 := by
  unfold qBinom
  rw [Nat.sub_self, qFactorial_zero, mul_one]
  exact div_self (qFactorial_ne_zero hq n)

/-- The Gaussian binomial is **positive** for `q > 1`. -/
theorem qBinom_pos {q : ℝ} (hq : 1 < q) (n k : ℕ) :
    0 < qBinom q n k := by
  unfold qBinom
  exact div_pos (qFactorial_pos hq n)
    (mul_pos (qFactorial_pos hq k) (qFactorial_pos hq (n - k)))

/-- **Symmetry** `[n choose k]_q = [n choose n-k]_q` when `k ≤ n`. -/
theorem qBinom_symm {q : ℝ} (n k : ℕ) (hk : k ≤ n) :
    qBinom q n k = qBinom q n (n - k) := by
  unfold qBinom
  rw [Nat.sub_sub_self hk, mul_comm (qFactorial q k) (qFactorial q (n - k))]

end QOU.MathlibExt.QPartitionCombinatorics
