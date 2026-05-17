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
abstract Wedderburn-weight `\tilde w_λ = dim_q²(λ) / [n]_q!` and the
Wenzl Schur element `s_{λ,X}(Q)` used in the canonical Markov-trace
decomposition (per
`prop:wedderburn-weight-canonical` and
`prop:macdonald-hook-telescope`).

Refs:
- [macdonald1995] Symmetric Functions and Hall Polynomials, I.3
- [wenzl1988] Hecke algebras of type A_n and subfactors, Invent. Math. 92
- [stanley1999] Enumerative Combinatorics II, Cor. 7.12.5
-/

import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Data.Real.Basic
import Mathlib.Algebra.BigOperators.Group.Finset.Defs
import Mathlib.Tactic

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
  simp only [Nat.one_ne_zero, if_false, pow_one, zpow_neg, zpow_one]
  exact div_self h_denom_ne

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

/-- A **partition** as a list `λ = [λ_1, λ_2, …]` of positive parts.
    No order constraint is imposed at the type level; downstream
    structure theorems may assume weakly decreasing. -/
abbrev Partition := List ℕ

namespace Partition

/-- The size `|λ| = Σ λ_i`. -/
def size (λ : Partition) : ℕ := λ.sum

/-- The number of rows. -/
def length (λ : Partition) : ℕ := λ.length

/-- The maximal row length (= number of columns in the conjugate). -/
def maxPart (λ : Partition) : ℕ := (0 :: λ).foldl Nat.max 0

/-- The **conjugate** (transpose) partition `λ'`.

    Convention: for each column index `j ∈ [0, maxPart λ)`, the
    conjugate part is the number of rows with at least `j + 1`
    boxes. -/
def conjugate (λ : Partition) : Partition :=
  (List.range λ.maxPart).map fun j =>
    (λ.filter (· > j)).length

/-- **Hook length** at cell `(i, j)` (0-indexed) of partition `λ`,
    when `(i, j) ∈ λ`.  For cells outside `λ`, returns 0.

    `h(i, j) = arm(i, j) + leg(i, j) + 1` where
      `arm(i, j) = λ_i - j - 1`  (cells to the right in row i)
      `leg(i, j) = |{ i' > i : λ_{i'} > j }|`  (cells below in col j) -/
def hookLength (λ : Partition) (i j : ℕ) : ℕ :=
  match λ.get? i with
  | none => 0
  | some row_i =>
    if j < row_i then
      let armLen := row_i - j - 1
      let legLen := ((λ.drop (i + 1)).filter (· > j)).length
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

/-- The **q-deformed dimension** of partition `λ ⊢ n`:

      dim_q(λ) = [n]_q! / ∏_{x ∈ λ} [h_x]_q.

    Computed as a fold over rows × columns, using
    `Partition.hookLength` for each cell. -/
noncomputable def qDim (q : ℝ) (λ : Partition) : ℝ :=
  qFactorial q λ.size /
    (List.range λ.length).foldl
      (fun acc i =>
        acc * (List.range ((λ.get? i).getD 0)).foldl
          (fun a j => a * qBracket q (Partition.hookLength λ i j))
          1)
      1

@[simp]
theorem qDim_nil (q : ℝ) : qDim q [] = qFactorial q 0 / 1 := by
  unfold qDim
  simp

end QOU.MathlibExt.QPartitionCombinatorics
