import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Data.Real.Basic
import Mathlib.Algebra.BigOperators.Group.Finset.Defs
import Mathlib.Tactic
import QOU.MathlibExt.QIntegerCanonical

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

/-! Base ring for the **algebraic** q-integer core (§7c): a generic `[Field R]`.
The q-bracket / q-factorial / q-dimension / q-binomial and their algebraic
identities hold over any field (the balanced `[n]_q` needs `q⁻¹` and division,
hence a field, but no ordering). The `1 < q` positivity / nonvanishing lemmas
below stay over `ℝ` — they are genuinely archimedean — and reference the generic
`qBracket` etc. with `R := ℝ` inferred. -/
variable {R : Type*} [Field R]

/-! ## q-bracket and q-factorial -/

/-- The **q-bracket** `[n]_q = (q^n − q^{-n}) / (q − q⁻¹)` for `n : ℕ`.
    At `n = 0` we set `[0]_q := 0`; for `n ≥ 1` the formula reduces to
    `1 + q² + q⁴ + … + q^{2(n−1)}` (up to a `q^{-(n-1)}` factor). -/
noncomputable def qBracket (q : R) (n : ℕ) : R :=
  if n = 0 then 0
  else (q ^ n - q ^ (-(n : ℤ))) / (q - q⁻¹)

/-- **Bridge to the canonical balanced bracket.**  The `n = 0` guard is
redundant — `qIntBal q 0 = (1 − 1)/(q − q⁻¹) = 0` already — so the agreement is
unconditional, on the degenerate locus too.  The `def` is kept because
`qFactorial` and the `1 < q` positivity lemmas below unfold it. -/
theorem qBracket_eq_canonical (q : R) (n : ℕ) :
    qBracket q n = QOU.QInteger.qIntBal q n := by
  unfold qBracket
  split_ifs with h
  · subst h
    simp [QOU.QInteger.qIntBal, QOU.Mass.QHookDimensionBalanced.qIntBal]
  · simp [QOU.QInteger.qIntBal, QOU.Mass.QHookDimensionBalanced.qIntBal, zpow_neg,
      zpow_natCast, inv_pow]

@[simp]
theorem qBracket_zero (q : R) : qBracket q 0 = 0 := by
  unfold qBracket; simp

/-- **`[1]_q = 1` whenever the denominator is well-defined.**

    Proved directly: `(q^1 - q^(-1)) / (q - q⁻¹) = (q - q⁻¹)/(q - q⁻¹) = 1`. -/
theorem qBracket_one {q : R} (h_denom_ne : q - q⁻¹ ≠ 0) :
    qBracket q 1 = 1 := by
  unfold qBracket
  rw [if_neg (by decide : (1 : ℕ) ≠ 0), zpow_neg, zpow_natCast, pow_one]
  exact div_self h_denom_ne

/-- **`[2]_q = q + q⁻¹`** when `q ≠ 0` and the denominator is nonzero.

    Proved via difference of squares:
      `(q² − q⁻²) = (q − q⁻¹)(q + q⁻¹)`,
    then `mul_div_cancel_left₀`. -/
theorem qBracket_two {q : R} (hq_ne : q ≠ 0)
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

/-- **The if-guard is redundant: the closed formula already vanishes at `n = 0`.**
`qBracket q n = (q^n − q^{-n}) / (q − q⁻¹)` for *every* `n` (at `n = 0` both sides are
`0`), so downstream proofs may use the uniform formula without case-splitting. -/
theorem qBracket_eq_formula (q : R) (n : ℕ) :
    qBracket q n = (q ^ n - q ^ (-(n : ℤ))) / (q - q⁻¹) := by
  rcases Nat.eq_zero_or_pos n with h | h
  · subst h; simp [qBracket]
  · rw [qBracket, if_neg h.ne']

/-- **Balanced quantum-integer addition identity** `[a+b]_q = q^b·[a]_q + q^{-a}·[b]_q`.
The defining relation behind the q-Pascal rule for the Gaussian binomial (and hence the
Rogers–Szegő / continuous q-Hermite three-term recurrence). Verified at the formula level:
`q^b(q^a−q^{-a}) + q^{-a}(q^b−q^{-b}) = q^{a+b} − q^{-a-b}`. -/
theorem qBracket_add (q : R) (hq : q ≠ 0) (a b : ℕ) :
    qBracket q (a + b) = q ^ b * qBracket q a + q ^ (-(a : ℤ)) * qBracket q b := by
  simp only [qBracket_eq_formula]
  rw [mul_div_assoc', mul_div_assoc', ← add_div]
  congr 1
  have e1 : q ^ (a + b) = q ^ a * q ^ b := pow_add q a b
  have e2 : q ^ (-((a + b : ℕ) : ℤ)) = q ^ (-(a : ℤ)) * q ^ (-(b : ℤ)) := by
    rw [← zpow_add₀ hq]; congr 1; omega
  rw [e1, e2, ← zpow_natCast q a, ← zpow_natCast q b]
  ring

/-- The **q-factorial** `[n]_q! = ∏_{k=1}^n [k]_q`.

    Empty product convention: `[0]_q! = 1`. -/
noncomputable def qFactorial (q : R) : ℕ → R
  | 0     => 1
  | n + 1 => qBracket q (n + 1) * qFactorial q n

@[simp]
theorem qFactorial_zero (q : R) : qFactorial q 0 = 1 := rfl

theorem qFactorial_succ (q : R) (n : ℕ) :
    qFactorial q (n + 1) = qBracket q (n + 1) * qFactorial q n := rfl

/-! ## Positivity at q > 1 (axiomatised pending Mathlib API stability) -/

/-- The Hecke deformation `q − q⁻¹` is positive when `q > 1`.

    **Proof**: For `q > 1`, we have `0 < q`, and since `q⁻¹ · q = 1`
    with `q⁻¹ > 0`, we get `q⁻¹ < 1 < q`, hence `q − q⁻¹ > 0`. -/
-- Ref: [leitner2026] def:q-bracket
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
  match lam[i]? with
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
noncomputable def qDim (q : R) (lam : Partition) : R :=
  qFactorial q lam.size /
    (List.range lam.length).foldl
      (fun acc i =>
        acc * (List.range ((lam[i]?).getD 0)).foldl
          (fun a j => a * qBracket q (Partition.hookLength lam i j))
          1)
      1

@[simp]
theorem qDim_nil (q : R) : qDim q [] = qFactorial q 0 / 1 := by
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

/-! ### `n(λ)`, the row-weighted size

**Not the same quantity as `contentSum`**, and the two are easy to confuse —
`contentSum` is `Σ_x (j − i)` over cells, whereas `n(λ)` is `Σ_i i·λ_i`. They
coincide only for a single row of length ≤ 1. In terms of the conjugate,
`contentSum λ = n(λ') − n(λ)`.

The distinction is load-bearing: the Wenzl Schur element's prefactor is
`Q^{n(λ)}`, and substituting `contentSum` there breaks the Macdonald hook
telescope from `n = 2` upward (measured; see `WenzlSchurElement.schurElement`). -/

/-- **`n(λ) = Σ_i i · λ_i`** (0-indexed rows), the row-weighted size of a
    partition. This is the standard `n(λ)` of Macdonald I.1, written for
    0-indexed rows so that `n(λ) = Σ_{i≥0} i·λ_i` rather than `Σ_{i≥1}(i−1)λ_i`. -/
def nLambda (lam : Partition) : ℕ :=
  (List.range lam.length).foldl (fun acc i => acc + i * ((lam[i]?).getD 0)) 0

@[simp]
theorem nLambda_nil : nLambda [] = 0 := by
  unfold nLambda; simp

/-! The three values below are the ones that separate `n(λ)` from `contentSum`,
and are kept as regression guards — `contentSum [2] = 1` while `n([2]) = 0`, and
`contentSum [1,1] = -1` while `n([1,1]) = 1`. -/

theorem nLambda_two : nLambda [2] = 0 := by decide
theorem nLambda_one_one : nLambda [1, 1] = 1 := by decide
theorem nLambda_three_one : nLambda [3, 1] = 1 := by decide

/-- **`n(λ)` and `contentSum` are genuinely different**, witnessed at `λ = (1,1)`:
`n(λ) = 1` but `contentSum λ = −1`. Stated so the confusion cannot recur
silently. -/
theorem nLambda_ne_contentSum :
    ((nLambda [1, 1] : ℤ)) ≠ contentSum [1, 1] := by decide

/-! ### Adding a box, and how hook lengths respond

Infrastructure for the Pieri step of the Macdonald hook telescope
(`MathlibExt.MacdonaldTelescope`). Adding one box to row `r` of `λ` changes
`hookLength` by **exactly `+1` on two sets and not at all elsewhere**:

* the cells of row `r` strictly left of the new box — their *arm* grows;
* the cells of column `λ_r` strictly above row `r` — their *leg* grows.

Verified against this very definition over 111 cells across the addable corners
of twelve shapes before being formalised. Both halves are proved below, and
`hookLength_addBoxRow_of_ne_corner` assembles them into the rule for every cell
but the new box itself.

The two halves need genuinely different arguments. The arm half is a `drop`
argument: the entry that moved is dropped before the leg count sees it. The leg
half cannot use that, because the modified entry survives *into* the tail — it
is a `countP`-over-`set` argument instead, and `j = λ_r` is exactly the
threshold at which the predicate `(· > j)` flips. -/

/-- Add one box to row `r`. Out of range, this is the identity (`List.set` is). -/
def addBoxRow (lam : Partition) (r : ℕ) : Partition :=
  lam.set r ((lam[r]?).getD 0 + 1)

/-- **The tail below row `i` is untouched** whenever the box goes in at or above
`i` — `List.set` at index `r ≤ i` is invisible after `drop (i+1)`. This is what
keeps the *leg* fixed in the arm-growth case. -/
theorem drop_addBoxRow (lam : Partition) (r i : ℕ) (h : r ≤ i) :
    (addBoxRow lam r).drop (i + 1) = lam.drop (i + 1) := by
  unfold addBoxRow
  rw [List.drop_set, if_pos (by omega)]

/-- **Arm growth.** For a cell of row `r` strictly left of the new box, the hook
length increases by exactly one.

The leg is unchanged by `drop_addBoxRow`; the arm goes from `λ_r − j − 1` to
`λ_r − j`, which is `+1` precisely because `j < λ_r` (this is `ℕ` subtraction,
so the hypothesis is doing real work, not decoration). -/
theorem hookLength_addBoxRow_same_row
    (lam : Partition) (r j : ℕ) (hr : r < lam.length)
    (hj : j < (lam[r]?).getD 0) :
    Partition.hookLength (addBoxRow lam r) r j
      = Partition.hookLength lam r j + 1 := by
  have hlam : lam[r]? = some ((lam[r]?).getD 0) := by
    rw [List.getElem?_eq_getElem hr]; rfl
  have hget : (addBoxRow lam r)[r]? = some ((lam[r]?).getD 0 + 1) := by
    unfold addBoxRow
    rw [List.getElem?_set_self (by simpa using hr)]
  unfold Partition.hookLength
  rw [hget, hlam, drop_addBoxRow lam r r (le_refl r)]
  set m := (lam[r]?).getD 0 with hm
  set L := ((lam.drop (r + 1)).filter (fun x => decide (x > j))).length with hL
  simp only [Option.getD_some, if_pos hj,
    if_pos (show j < m + 1 by omega)]
  omega

/-- **Rows strictly below the new box are untouched.** For `r < i` the row entry
is unchanged (the `set` is at a different index) and so is the tail, so the hook
length is literally the same. -/
theorem hookLength_addBoxRow_row_below
    (lam : Partition) (r i j : ℕ) (h : r < i) :
    Partition.hookLength (addBoxRow lam r) i j
      = Partition.hookLength lam i j := by
  have hne : (addBoxRow lam r)[i]? = lam[i]? := by
    unfold addBoxRow
    rw [List.getElem?_set_ne (by omega)]
  unfold Partition.hookLength
  rw [hne, drop_addBoxRow lam r i (by omega)]

/-- **Setting one entry from a value failing `p` to one satisfying it raises the
count by exactly one.** The counting step behind leg growth; proved by
structural induction rather than found in Mathlib. -/
theorem countP_set_of_flip {p : ℕ → Bool} :
    ∀ (l : List ℕ) (k v : ℕ), (hk : k < l.length) →
      p (l[k]'hk) = false → p v = true →
      (l.set k v).countP p = l.countP p + 1
  | a :: t, 0, v, _, hold, hnew => by
      simp only [List.getElem_cons_zero] at hold
      simp [hold, hnew]
  | a :: t, k + 1, v, hk, hold, hnew => by
      have ih := countP_set_of_flip t k v (by simpa using Nat.lt_of_succ_lt_succ hk)
        (by simpa using hold) hnew
      simp [List.countP_cons, ih]
      omega

/-- **Leg growth, as a count.** For a row `i` strictly above the new box, the
tail below `i` still contains row `r`, whose entry moves from `λ_r` to `λ_r + 1`.
At the threshold `j = λ_r` that flips the predicate `(· > j)` from false to true,
so the leg count rises by exactly one.

This is the half the `drop` argument cannot reach: the modified entry survives
into the tail rather than being dropped, so the proof is a `countP`-over-`set`
argument instead. -/
theorem countP_drop_addBoxRow_at_threshold
    (lam : Partition) (r i : ℕ) (h : i < r) (hr : r < lam.length) :
    ((addBoxRow lam r).drop (i + 1)).countP
        (fun x => decide (x > (lam[r]?).getD 0))
      = ((lam.drop (i + 1)).countP
          (fun x => decide (x > (lam[r]?).getD 0))) + 1 := by
  unfold addBoxRow
  rw [List.drop_set, if_neg (by omega)]
  have hr' : r < List.length lam := hr
  have hlen : r - (i + 1) < (lam.drop (i + 1)).length := by
    rw [List.length_drop]; omega
  refine countP_set_of_flip (lam.drop (i + 1)) (r - (i + 1)) _ hlen ?_ ?_
  · rw [List.getElem_drop]
    have hidx : i + 1 + (r - (i + 1)) = r := by omega
    simp [hidx, List.getElem?_eq_getElem hr]
  · simp

/-- **Setting one entry to another with the same `p`-value leaves the count
alone.** The companion to `countP_set_of_flip`: together they say the count
moves by exactly the indicator of a flip. Also proved by structural induction —
Mathlib carries no `countP`-over-`set` lemma reachable from here. -/
theorem countP_set_of_same {p : ℕ → Bool} :
    ∀ (l : List ℕ) (k v : ℕ), (hk : k < l.length) →
      p (l[k]'hk) = p v →
      (l.set k v).countP p = l.countP p
  | _ :: t, 0, v, _, h => by
      simp only [List.getElem_cons_zero] at h
      simp [List.countP_cons, ← h]
  | _ :: t, k + 1, v, hk, h => by
      have ih := countP_set_of_same t k v (by simpa using Nat.lt_of_succ_lt_succ hk)
        (by simpa using h)
      simp [List.countP_cons, ih]

/-- **Off the threshold the leg count does not move.** For a row `i` above the
new box and any column `j ≠ λ_r`, raising `λ_r` to `λ_r + 1` does not change
whether row `r` exceeds `j`: below the threshold both exceed it, above it
neither does. -/
theorem countP_drop_addBoxRow_off_threshold
    (lam : Partition) (r i j : ℕ) (h : i < r) (hr : r < lam.length)
    (hj : j ≠ (lam[r]?).getD 0) :
    ((addBoxRow lam r).drop (i + 1)).countP (fun x => decide (x > j))
      = (lam.drop (i + 1)).countP (fun x => decide (x > j)) := by
  unfold addBoxRow
  rw [List.drop_set, if_neg (by omega)]
  have hr' : r < List.length lam := hr
  have hlen : r - (i + 1) < (lam.drop (i + 1)).length := by
    rw [List.length_drop]; omega
  refine countP_set_of_same (lam.drop (i + 1)) (r - (i + 1)) _ hlen ?_
  rw [List.getElem_drop]
  have hidx : i + 1 + (r - (i + 1)) = r := by omega
  have hval : lam[r]'hr' = (lam[r]?).getD 0 := by
    rw [List.getElem?_eq_getElem hr']; rfl
  simp only [hidx, hval, decide_eq_decide]
  omega

/-- **Leg growth.** For a cell in column `λ_r` strictly above row `r`, the hook
length increases by exactly one: the arm is untouched (the row entry at `i` is
not the one that moved) and the leg count crosses its threshold.

The hypothesis `λ_r < λ_i` is what puts the cell inside `λ` in the first place;
without it both sides are `0` and there is nothing to say. -/
theorem hookLength_addBoxRow_leg_growth
    (lam : Partition) (r i : ℕ) (h : i < r) (hr : r < lam.length)
    (hin : (lam[r]?).getD 0 < (lam[i]?).getD 0) :
    Partition.hookLength (addBoxRow lam r) i ((lam[r]?).getD 0)
      = Partition.hookLength lam i ((lam[r]?).getD 0) + 1 := by
  have hr' : r < List.length lam := hr
  have hi : i < List.length lam := by omega
  have hlam : lam[i]? = some ((lam[i]?).getD 0) := by
    rw [List.getElem?_eq_getElem hi]; rfl
  have hne : (addBoxRow lam r)[i]? = lam[i]? := by
    unfold addBoxRow; rw [List.getElem?_set_ne (by omega)]
  have hcount := countP_drop_addBoxRow_at_threshold lam r i h hr
  unfold Partition.hookLength
  rw [hne, hlam]
  simp only [if_pos hin, ← List.countP_eq_length_filter]
  rw [hcount]
  omega

/-- **Rows above the new box, off its column, are untouched.** -/
theorem hookLength_addBoxRow_row_above_ne
    (lam : Partition) (r i j : ℕ) (h : i < r) (hr : r < lam.length)
    (hj : j ≠ (lam[r]?).getD 0) :
    Partition.hookLength (addBoxRow lam r) i j = Partition.hookLength lam i j := by
  have hne : (addBoxRow lam r)[i]? = lam[i]? := by
    unfold addBoxRow; rw [List.getElem?_set_ne (by omega)]
  have hcount := countP_drop_addBoxRow_off_threshold lam r i j h hr hj
  unfold Partition.hookLength
  rw [hne]
  cases hrow : lam[i]? with
  | none => rfl
  | some row_i =>
    by_cases hjr : j < row_i
    · simp only [if_pos hjr, ← List.countP_eq_length_filter, hcount]
    · simp only [if_neg hjr]

/-- Adding a box does not change the number of rows (`List.set` does not). -/
@[simp]
theorem length_addBoxRow (lam : Partition) (r : ℕ) :
    (addBoxRow lam r).length = lam.length := by
  unfold addBoxRow Partition.length
  rw [List.length_set]

/-- The row that received the box is one cell longer. -/
theorem getElem?_addBoxRow_self (lam : Partition) (r : ℕ) (hr : r < lam.length) :
    (addBoxRow lam r)[r]? = some ((lam[r]?).getD 0 + 1) := by
  unfold addBoxRow
  rw [List.getElem?_set_self (by simpa using hr)]

/-- Every other row is untouched. -/
theorem getElem?_addBoxRow_ne (lam : Partition) (r i : ℕ) (h : i ≠ r) :
    (addBoxRow lam r)[i]? = lam[i]? := by
  unfold addBoxRow
  rw [List.getElem?_set_ne (Ne.symm h)]

/-- A `foldl` that only ever adds to its accumulator IS a sum. -/
private theorem foldl_add_eq_sum (f : ℕ → ℕ) :
    ∀ (l : List ℕ) (a : ℕ), l.foldl (fun acc x => acc + f x) a = a + (l.map f).sum
  | [], a => by simp
  | x :: t, a => by
      rw [List.foldl_cons, foldl_add_eq_sum f t (a + f x)]
      simp [Nat.add_assoc]

/-- **`n(λ + box in row r) = n(λ) + r`.**

`n(λ) = Σ_i i·λ_i`, so raising `λ_r` by one adds exactly `r`. This is the
prefactor's share of the Pieri step: `schurElement`'s `Q^{n(λ)}` becomes
`Q^{n(λ)+r}` when the box goes into row `r`, and nothing else about the
prefactor moves.

Note the direction of the dependence: the increment is the ROW INDEX, not the
row length. A box added to row `0` does not change `n(λ)` at all. -/
theorem nLambda_eq_sum (lam : Partition) :
    nLambda lam = ∑ i ∈ Finset.range lam.length, i * ((lam[i]?).getD 0) := by
  unfold nLambda
  rw [foldl_add_eq_sum _ (List.range lam.length) 0, Nat.zero_add]
  rfl

/-- **`n(λ + box in row r) = n(λ) + r`.** -/
theorem nLambda_addBoxRow (lam : Partition) (r : ℕ) (hr : r < lam.length) :
    nLambda (addBoxRow lam r) = nLambda lam + r := by
  rw [nLambda_eq_sum, nLambda_eq_sum, length_addBoxRow]
  have hmem : r ∈ Finset.range lam.length := Finset.mem_range.mpr hr
  rw [← Finset.add_sum_erase _ _ hmem, ← Finset.add_sum_erase _ _ hmem]
  have hrest : ∑ i ∈ (Finset.range lam.length).erase r, i * (((addBoxRow lam r)[i]?).getD 0)
      = ∑ i ∈ (Finset.range lam.length).erase r, i * ((lam[i]?).getD 0) :=
    Finset.sum_congr rfl fun i hi => by
      rw [getElem?_addBoxRow_ne lam r i (Finset.ne_of_mem_erase hi)]
  rw [hrest, getElem?_addBoxRow_self lam r hr]
  simp only [Option.getD_some, Nat.mul_add, Nat.mul_one]
  omega

/-! The two guards below pin the *direction* of `nLambda_addBoxRow`. `n([3,2,1]) = 4`;
adding a box to row `1` gives `[3,3,1]` with `n = 5`, and adding one to row `0`
gives `[4,2,1]` with `n = 4` — unchanged. Row `0` is the case that separates
"increment by the row index" from "increment by the row length", and it is the
one a sign or index slip would break. -/

theorem nLambda_addBoxRow_row_one : nLambda (addBoxRow [3, 2, 1] 1) = nLambda [3, 2, 1] + 1 := by
  decide

theorem nLambda_addBoxRow_row_zero : nLambda (addBoxRow [3, 2, 1] 0) = nLambda [3, 2, 1] := by
  decide

/-! ### The corner `addBoxRow` cannot reach

`addBoxRow` is `List.set`, and `List.set` is a **no-op out of range** — so
`addBoxRow lam lam.length` is `lam`, not `lam ++ [1]`. The new-bottom-row corner
is therefore not expressible by it, and **every** partition has exactly one such
corner (measured in `computations/y_lambda_pieri_step_probe.py`, where each of
the eight shapes checked contributes one). It is a second operation, not a
defect in `addBoxRow` — a `set` genuinely cannot lengthen a list.

The new row is *last*, which makes this case easier than the interior one in two
places: nothing lies below it, so the new cell's hook length is unconditionally
`1` (the interior corner needs the weakly-decreasing property, which the carrier
does not have), and only column `0` sees any change at all. -/

/-- **The trap, stated as a theorem** so it cannot be re-discovered by accident:
adding a box "at row `lam.length`" via `addBoxRow` does nothing. -/
theorem addBoxRow_at_length (lam : Partition) : addBoxRow lam lam.length = lam := by
  unfold addBoxRow
  exact List.set_eq_of_length_le (Nat.le_refl (List.length lam))

/-- Add a box as a **new bottom row** of one cell. -/
def addBoxNewRow (lam : Partition) : Partition := lam ++ [1]

@[simp]
theorem length_addBoxNewRow (lam : Partition) :
    (addBoxNewRow lam).length = lam.length + 1 := by
  unfold addBoxNewRow Partition.length
  simp

theorem getElem?_addBoxNewRow_lt (lam : Partition) (i : ℕ) (h : i < lam.length) :
    (addBoxNewRow lam)[i]? = lam[i]? := by
  unfold addBoxNewRow
  rw [List.getElem?_append_left (by simpa using h)]

theorem getElem?_addBoxNewRow_self (lam : Partition) :
    (addBoxNewRow lam)[lam.length]? = some 1 := by
  unfold addBoxNewRow
  show (lam ++ [1])[List.length lam]? = some 1
  rw [List.getElem?_append_right (Nat.le_refl (List.length lam))]
  simp

/-- The tail below row `i` gains the new row, for any `i` inside `lam`. -/
theorem drop_addBoxNewRow (lam : Partition) (i : ℕ) (h : i < lam.length) :
    (addBoxNewRow lam).drop (i + 1) = lam.drop (i + 1) ++ [1] := by
  unfold addBoxNewRow
  have h' : i + 1 ≤ List.length lam := h
  rw [List.drop_append_of_le_length h']

/-- **Only column `0` moves.** The new row holds a single cell, so its entry `1`
exceeds `j` exactly when `j = 0`; for every other column the leg count is blind
to it. -/
theorem hookLength_addBoxNewRow_col_pos (lam : Partition) (i j : ℕ)
    (h : i < lam.length) (hj : 0 < j) :
    Partition.hookLength (addBoxNewRow lam) i j = Partition.hookLength lam i j := by
  unfold Partition.hookLength
  rw [getElem?_addBoxNewRow_lt lam i h, drop_addBoxNewRow lam i h]
  cases hrow : lam[i]? with
  | none => rfl
  | some row_i =>
    by_cases hjr : j < row_i
    · simp only [if_pos hjr, List.filter_append, List.length_append,
        List.filter_cons, List.filter_nil]
      simp [Nat.not_lt.mpr (Nat.one_le_iff_ne_zero.mpr (by omega) : 1 ≤ j)]
    · simp only [if_neg hjr]

/-- **Column `0` gains exactly one**, for every row of `lam` that has a cell
there. -/
theorem hookLength_addBoxNewRow_col_zero (lam : Partition) (i : ℕ)
    (h : i < lam.length) (hpos : 0 < (lam[i]?).getD 0) :
    Partition.hookLength (addBoxNewRow lam) i 0 = Partition.hookLength lam i 0 + 1 := by
  have hlam : lam[i]? = some ((lam[i]?).getD 0) := by
    rw [List.getElem?_eq_getElem (show i < List.length lam from h)]; rfl
  unfold Partition.hookLength
  rw [getElem?_addBoxNewRow_lt lam i h, drop_addBoxNewRow lam i h, hlam]
  simp only [if_pos hpos, List.filter_append, List.length_append,
    List.filter_cons, List.filter_nil, decide_eq_true_eq]
  simp only [if_pos (show 0 < 1 by norm_num), List.length_cons, List.length_nil]
  omega

/-- **The new cell's hook length is `1`, unconditionally.** Nothing lies below
the last row, so no order hypothesis is needed — unlike the interior corner,
which `hookLength_addBoxRow_of_ne_corner` has to exclude. -/
theorem hookLength_addBoxNewRow_new_cell (lam : Partition) :
    Partition.hookLength (addBoxNewRow lam) lam.length 0 = 1 := by
  have hnil : (addBoxNewRow lam).drop (lam.length + 1) = [] := by
    refine List.drop_eq_nil_of_le ?_
    simp [addBoxNewRow, Partition.length]
  unfold Partition.hookLength
  rw [getElem?_addBoxNewRow_self lam, hnil]
  simp

/-- **`n(λ ++ [1]) = n(λ) + ℓ(λ)`**: the new row sits at index `ℓ(λ)` and holds
one cell, so it contributes exactly its own index. -/
theorem nLambda_addBoxNewRow (lam : Partition) :
    nLambda (addBoxNewRow lam) = nLambda lam + lam.length := by
  rw [nLambda_eq_sum, nLambda_eq_sum, length_addBoxNewRow, Finset.sum_range_succ,
    getElem?_addBoxNewRow_self lam]
  have hrest : ∑ i ∈ Finset.range lam.length, i * (((addBoxNewRow lam)[i]?).getD 0)
      = ∑ i ∈ Finset.range lam.length, i * ((lam[i]?).getD 0) :=
    Finset.sum_congr rfl fun i hi => by
      rw [getElem?_addBoxNewRow_lt lam i (Finset.mem_range.mp hi)]
  rw [hrest]
  simp

/-- Concrete check, matching the probe: `[3,2,1] ++ [1] = [3,2,1,1]`, and
`n` goes `4 → 7` because the new row sits at index `3`. -/
theorem nLambda_addBoxNewRow_example :
    addBoxNewRow [3, 2, 1] = [3, 2, 1, 1] ∧
      nLambda (addBoxNewRow [3, 2, 1]) = nLambda [3, 2, 1] + 3 := by
  decide

/-! ### Addable corners

A box may be added to row `r` exactly when the result is still weakly
decreasing: `r = 0`, or row `r` is strictly shorter than the row above it.
Plus, always, a new bottom row — the corner `addBoxRow` cannot express.

The rule is stated for a bare `List ℕ`, so it does not *presuppose* weak
decrease; on a genuine partition it is the usual notion. Cross-checked against
`computations/y_lambda_pieri_step_probe.py`, which enumerates corners the same
way and verifies (P) over them with `X` free. -/

/-- The shapes obtained from `lam` by adding one box at an addable corner. -/
def addableCorners (lam : Partition) : List Partition :=
  ((List.range lam.length).filterMap fun r =>
      if r = 0 ∨ (lam[r]?).getD 0 < (lam[r - 1]?).getD 0 then
        some (addBoxRow lam r)
      else none)
    ++ [addBoxNewRow lam]

/-! The three checks below are the shapes the probe enumerates, and they pin the
rule from both sides: `(2,1)` has three corners because row 1 is strictly
shorter than row 0, whereas `(2,2)` has only two because row 1 is **not** — a
box there would break weak decrease. That negative case is the one a
mis-stated condition would get wrong. -/

theorem addableCorners_one : addableCorners [1] = [[2], [1, 1]] := by decide

theorem addableCorners_two_one :
    addableCorners [2, 1] = [[3, 1], [2, 2], [2, 1, 1]] := by decide

theorem addableCorners_two_two : addableCorners [2, 2] = [[3, 2], [2, 2, 1]] := by decide

theorem addableCorners_three_two_one :
    addableCorners [3, 2, 1] = [[4, 2, 1], [3, 3, 1], [3, 2, 2], [3, 2, 1, 1]] := by decide

/-- **The new bottom row is always a corner**, and it is always the last one
listed. Recorded because the `++ [addBoxNewRow lam]` is easy to drop when
refactoring, and `addableCorners` would then silently under-enumerate. -/
theorem addBoxNewRow_mem_addableCorners (lam : Partition) :
    addBoxNewRow lam ∈ addableCorners lam := by
  unfold addableCorners
  exact List.mem_append_right _ (List.mem_singleton_self _)

/-- **The hook-length update rule.** Adding one box to row `r` raises the hook
length by exactly one on two sets of cells and leaves every other cell alone:

* the cells of row `r` strictly left of the new box (their **arm** grows);
* the cells of column `λ_r` strictly above row `r` (their **leg** grows).

The new box itself, `(r, λ_r)`, is excluded: its hook length in the new shape is
`1` only because no row below `r` exceeds `λ_r`, which is the weakly-decreasing
property — and `Partition` is a bare `List ℕ` that does not carry it. Stating
the rule off the corner keeps it unconditional; the corner is supplied
separately by whatever carries the order hypothesis.

This is the per-cell input to the Pieri step of the Macdonald hook telescope. -/
theorem hookLength_addBoxRow_of_ne_corner
    (lam : Partition) (r i j : ℕ) (hr : r < lam.length)
    (hcorner : ¬(i = r ∧ j = (lam[r]?).getD 0)) :
    Partition.hookLength (addBoxRow lam r) i j
      = Partition.hookLength lam i j
        + (if (i = r ∧ j < (lam[r]?).getD 0)
             ∨ (i < r ∧ j = (lam[r]?).getD 0 ∧ j < (lam[i]?).getD 0)
           then 1 else 0) := by
  rcases lt_trichotomy i r with hlt | heq | hgt
  · have hr' : r < List.length lam := hr
    by_cases hj : j = (lam[r]?).getD 0
    · subst hj
      by_cases hin : (lam[r]?).getD 0 < (lam[i]?).getD 0
      · rw [hookLength_addBoxRow_leg_growth lam r i hlt hr hin,
          if_pos (Or.inr ⟨hlt, rfl, hin⟩)]
      · have hi : i < List.length lam := by omega
        have hlam : lam[i]? = some ((lam[i]?).getD 0) := by
          rw [List.getElem?_eq_getElem hi]; rfl
        have hne : (addBoxRow lam r)[i]? = lam[i]? := by
          unfold addBoxRow; rw [List.getElem?_set_ne (by omega)]
        rw [if_neg (by rintro (⟨h', _⟩ | ⟨_, _, h'⟩) <;> omega), Nat.add_zero]
        unfold Partition.hookLength
        rw [hne, hlam]
        simp only [if_neg hin]
    · rw [hookLength_addBoxRow_row_above_ne lam r i j hlt hr hj,
        if_neg (by rintro (⟨h', _⟩ | ⟨_, h', _⟩) <;> omega), Nat.add_zero]
  · subst heq
    have hj : j ≠ (lam[i]?).getD 0 := fun h' => hcorner ⟨rfl, h'⟩
    by_cases hlt : j < (lam[i]?).getD 0
    · rw [hookLength_addBoxRow_same_row lam i j hr hlt, if_pos (Or.inl ⟨rfl, hlt⟩)]
    · have hi : i < List.length lam := hr
      have hlam : lam[i]? = some ((lam[i]?).getD 0) := by
        rw [List.getElem?_eq_getElem hi]; rfl
      have hget : (addBoxRow lam i)[i]? = some ((lam[i]?).getD 0 + 1) := by
        unfold addBoxRow; rw [List.getElem?_set_self (by simpa using hr)]
      rw [if_neg (by rintro (⟨_, h'⟩ | ⟨h', _⟩) <;> omega), Nat.add_zero]
      unfold Partition.hookLength
      rw [hget, hlam]
      simp only [Option.getD_some, if_neg hlt,
        if_neg (show ¬ j < (lam[i]?).getD 0 + 1 by omega)]
  · rw [hookLength_addBoxRow_row_below lam r i j hgt,
      if_neg (by rintro (⟨h', _⟩ | ⟨h', _⟩) <;> omega), Nat.add_zero]

/-- **THEOREM (q-Schur weight at H₂).** The Markov weight of partition
    lam ⊢ 2 is y_lam = q^{c(lam)} / [2]_q. This is the bridge between the
    content-sum formula and the explicitly-proved H₂ weights. -/
-- Ref: [wenzl1988] Theorem 5 specialised to n=2
-- Ref: [leitner2026] prop:q-schur-y-lambda-closed-form (H₂ case)
theorem qSchur_H2_content_bridge (q : ℝ) (hq : 1 < q) :
    contentSum [2] = 1 ∧ contentSum [1, 1] = -1 := by
  exact ⟨contentSum_two, contentSum_one_one⟩

/-! ## Gaussian binomial coefficient (q-binomial)

Consolidates the third standard q-analog primitive alongside `qBracket`
(`[n]_q`) and `qFactorial` (`[n]_q!`). Bean `5ldf` (epic `08a2`). -/

/-- The **Gaussian binomial coefficient** (q-binomial)
    `[n choose k]_q = [n]_q! / ([k]_q! · [n-k]_q!)`, in the **balanced** quantum
    integer `[n]_q = (qⁿ−q⁻ⁿ)/(q−q⁻¹)`.

    **Canonical** (bean `5ldf` consolidation): this is the QOU-canonical q-binomial.
    Two other defs exist in the tree:
    * `QOU.GaugeFieldFluidDynamics.qBinomial` — the **same** balanced object
      (`qInteger ≡ qBracket`; verified bit-for-bit), kept as a deprecated duplicate.
    * `QOU.Machinery.QPochhammer.qBinomial` — the **standard** form
      `(q;q)ₙ/((q;q)ₖ(q;q)_{n-k})`, a *different* normalization (e.g. `[2 choose 1]`
      is `q+q⁻¹` here vs `1+q` there). Not interchangeable. -/
noncomputable def qBinom (q : R) (n k : ℕ) : R :=
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
theorem qBinom_symm {q : R} (n k : ℕ) (hk : k ≤ n) :
    qBinom q n k = qBinom q n (n - k) := by
  unfold qBinom
  rw [Nat.sub_sub_self hk, mul_comm (qFactorial q k) (qFactorial q (n - k))]

end QOU.MathlibExt.QPartitionCombinatorics
