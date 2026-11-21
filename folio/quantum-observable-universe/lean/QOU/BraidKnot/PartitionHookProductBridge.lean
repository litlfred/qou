/-
  Bridge (1b) of the `DeltaLambdaSignRule.burnside` reduction roadmap:
  the **custom list-based `Partition.hookProduct`** equals the **corpus list
  `IdentityI.prodHooks`**, hence (via the already-proved geometric bridges) the
  **cell-based `QOU.BraidKnot.hookProduct`** of the associated `YoungDiagram`.

  Chain assembled here:

      Partition.hookProduct Λ                        (custom, nested foldl)
    = IdentityI.prodHooks Λ.parts                    (this file, `hookProduct_eq_prodHooks`)
    = YoungDiagram.hookLengthProduct (ofRowLens …)   (`hookLengthProduct_eq_prodHooks`, upstream)
    = QOU.BraidKnot.hookProduct (ofRowLens …)        (`HookProductHLF.hookProduct_eq_hookLengthProduct`)

  and then, with the FRT hook-length formula `HookProductHLF.numSYT_mul_hookProduct`,
  the roadmap's bridge (1) conclusion `dimIrrep Λ = numSYT (toYoungDiagram Λ)`
  with the `Nat`-division discharged honestly (`hookProduct ≠ 0`).

  Upstream note: the FRT layer this file consumes — the hook bridge and
  `numSYT_mul_hookProduct` — comes from `QOU.BraidKnot.HookProductHLF`, proved
  independently in PR #4692 (session `session_014oQRaNPnFLJHbhrZsiCMWt`). This
  branch had reached the same result in parallel as a separate
  `StandardYoungTableauHLF.lean`; that duplicate is dropped in favour of #4692's
  leaf, which reuses the already-proved `PieceA.armZ_eq_card` / `legZ_eq_card`
  and is scoped in its own sub-namespace.

  The mathematical content is the single observation that, because `Λ.parts` is
  weakly decreasing, the cells of column `j` occupy a **prefix** of the rows: so
  the custom `legLength` (a `filter` over the rows strictly below `i`) equals
  `colLen parts j - i - 1`. Everything else is `foldl`-to-`prod` bookkeeping.

  -- Ref: [sagan2001] Sagan, The Symmetric Group §3.10 (hook-length formula)
  -- Ref: [leitner2026] DeltaLambdaSignRule.lean §REDUCTION ROADMAP, bridge (1)
-/
import QOU.BraidKnot.DeltaLambdaSignRule
import QOU.BraidKnot.HookProductHLF

namespace QOU.BraidKnot

open List DeltaLambdaSignRule

/-! ### `foldl`-to-`prod` bookkeeping -/

/-- A multiplicative `foldl` with an accumulator is the accumulator times the mapped product. -/
theorem foldl_mul_map {α : Type*} (f : α → ℕ) :
    ∀ (L : List α) (acc : ℕ), L.foldl (fun a x => a * f x) acc = acc * (L.map f).prod
  | [], acc => by simp
  | x :: t, acc => by
    rw [List.foldl_cons, foldl_mul_map f t (acc * f x), List.map_cons, List.prod_cons,
      Nat.mul_assoc]

/-! ### Columns of a weakly-decreasing list occupy a prefix of the rows -/

/-- Dropping `k` rows removes exactly `k` cells from every column, because a
weakly-decreasing `l` has each column's cells in a prefix of the rows. -/
theorem colLen_drop (j : ℕ) :
    ∀ (l : List ℕ), l.Sorted (· ≥ ·) → ∀ (k : ℕ),
      IdentityI.colLen (l.drop k) j = IdentityI.colLen l j - k
  | l, _, 0 => by simp
  | [], _, _ + 1 => by simp [IdentityI.colLen]
  | a :: t, hl, k + 1 => by
    obtain ⟨hat, ht⟩ := List.sorted_cons.mp hl
    rw [List.drop_succ_cons, colLen_drop j t ht k, IdentityI.colLen_cons]
    by_cases h : j < a
    · simp [h]
    · have hz : IdentityI.colLen t j = 0 :=
        IdentityI.colLen_eq_zero t j (fun b hb => le_trans (hat b hb) (Nat.not_lt.mp h))
      simp [h, hz]

/-- The custom `legLength` in terms of `colLen`: the rows strictly below `i` holding a
cell in column `j`. -/
theorem legLength_eq_colLen {n : ℕ} (Λ : Partition n) (i j : ℕ) :
    Λ.legLength i j = IdentityI.colLen Λ.parts j - (i + 1) := by
  rw [Partition.legLength, ← colLen_drop j Λ.parts Λ.sorted (i + 1)]
  rfl

/-! ### The per-cell hook lengths agree -/

/-- For a genuine cell `(i,j)` the custom hook length equals the corpus list term
`(rowLen − j) + (colLen j − i) − 1`. Both `rowLen − j` and `colLen j − i` are `≥ 1`
on a cell, so the `ℕ` subtractions are exact. -/
theorem hookLength_eq_term {n : ℕ} (Λ : Partition n) (i j : ℕ)
    (hj : j < Λ.parts.getD i 0) :
    Λ.hookLength i j
      = (Λ.parts.getD i 0 - j) + (IdentityI.colLen Λ.parts j - i) - 1 := by
  have hcol : i < IdentityI.colLen Λ.parts j :=
    (IdentityI.colLen_duality Λ.parts Λ.sorted i j).mpr hj
  have harm : Λ.armLength i j = Λ.parts.getD i 0 - j - 1 := by
    have hi : i < Λ.parts.length := by
      by_contra hne
      rw [List.getD_eq_default _ _ (Nat.le_of_not_lt hne)] at hj
      exact Nat.not_lt_zero _ hj
    rw [Partition.armLength, List.getElem?_eq_getElem hi]
    simp only [List.getD_eq_getElem _ _ hi] at hj ⊢
    simp [hj]
  rw [Partition.hookLength, harm, legLength_eq_colLen]
  omega

/-! ### The two list hook products agree -/

/-- **Bridge (1b).** The custom list-based `Partition.hookProduct` equals the corpus
list `IdentityI.prodHooks` of the same parts. -/
theorem hookProduct_eq_prodHooks {n : ℕ} (Λ : Partition n) :
    Λ.hookProduct = IdentityI.prodHooks Λ.parts := by
  rw [Partition.hookProduct, IdentityI.prodHooks]
  simp only [foldl_mul_map, Nat.one_mul]
  congr 1
  apply List.ext_getElem
  · simp
  · intro k h1 h2
    simp only [List.getElem_map, List.getElem_zipIdx, List.getElem_range, Nat.zero_add]
    have hk : k < Λ.parts.length := by simpa using h1
    have hgetD : Λ.parts.getD k 0 = Λ.parts[k] := List.getD_eq_getElem _ _ hk
    rw [hgetD]
    congr 1
    refine List.map_congr_left (fun j hj => ?_)
    rw [List.mem_range] at hj
    have hj' : j < Λ.parts.getD k 0 := by rw [hgetD]; exact hj
    rw [hookLength_eq_term Λ k j hj', hgetD]

/-! ### Bridge (1): `dimIrrep Λ = numSYT (toYoungDiagram Λ)` -/

/-- The `YoungDiagram` of a custom `Partition n` (its parts are its row lengths). -/
def toYoungDiagram {n : ℕ} (Λ : Partition n) : YoungDiagram :=
  YoungDiagram.ofRowLens Λ.parts Λ.sorted

@[simp] theorem rowLens_toYoungDiagram {n : ℕ} (Λ : Partition n) :
    (toYoungDiagram Λ).rowLens = Λ.parts :=
  YoungDiagram.rowLens_ofRowLens_eq_self Λ.pos

@[simp] theorem card_toYoungDiagram {n : ℕ} (Λ : Partition n) :
    (toYoungDiagram Λ).cells.card = n := by
  have h := SpechtClassification.card_eq_rowLens_sum (toYoungDiagram Λ)
  rw [rowLens_toYoungDiagram, Λ.sum_eq] at h
  exact h

/-- `YoungDiagram.card` form of `card_toYoungDiagram` — `YoungDiagram.card` is by
definition `cells.card`, but `rw` needs the syntactic form the FRT statement uses. -/
@[simp] theorem card_toYoungDiagram' {n : ℕ} (Λ : Partition n) :
    (toYoungDiagram Λ).card = n :=
  card_toYoungDiagram Λ

/-- The custom list hook product is the cell-based hook product of the associated diagram. -/
theorem hookProduct_eq_cell {n : ℕ} (Λ : Partition n) :
    Λ.hookProduct = QOU.BraidKnot.hookProduct (toYoungDiagram Λ) := by
  rw [hookProduct_eq_prodHooks, HookProductHLF.hookProduct_eq_hookLengthProduct,
    QOU.Mathlib.hookLengthProduct_eq_prodHooks, rowLens_toYoungDiagram]

/-- **Frame–Robinson–Thrall for the custom `Partition n`**: `#SYT · ∏hooks = n!`. -/
theorem numSYT_mul_hookProduct_partition {n : ℕ} (Λ : Partition n) :
    numSYT (toYoungDiagram Λ) * Λ.hookProduct = n.factorial := by
  rw [hookProduct_eq_cell, HookProductHLF.numSYT_mul_hookProduct, card_toYoungDiagram']

theorem hookProduct_ne_zero {n : ℕ} (Λ : Partition n) : Λ.hookProduct ≠ 0 := by
  intro h
  have hfrt := numSYT_mul_hookProduct_partition Λ
  rw [h, Nat.mul_zero] at hfrt
  exact Nat.factorial_ne_zero n hfrt.symm

/-- **Bridge (1) of the `burnside` reduction roadmap.** The hook-length-formula
dimension of a custom partition is the genuine standard-tableau count of its
diagram — the `ℕ` division in `dimIrrep` is exact, since `hookProduct ∣ n!`
witnessed by `numSYT_mul_hookProduct_partition`. -/
theorem dimIrrep_eq_numSYT {n : ℕ} (Λ : Partition n) :
    Λ.dimIrrep = numSYT (toYoungDiagram Λ) := by
  rw [Partition.dimIrrep]
  exact Nat.div_eq_of_eq_mul_left (Nat.pos_of_ne_zero (hookProduct_ne_zero Λ))
    (numSYT_mul_hookProduct_partition Λ).symm

end QOU.BraidKnot
