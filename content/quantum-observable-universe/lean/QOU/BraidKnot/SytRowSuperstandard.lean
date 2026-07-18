import QOU.Mathlib.StandardYoungTableau
import Mathlib.Order.Interval.Finset.Nat

/-!
# QOU.BraidKnot.SytRowSuperstandard — the row-superstandard standard Young tableau

The **row-superstandard** (row-reading) tableau of shape `μ`: fill the cells with `1, 2, …, |μ|`
reading each row left-to-right, top row first. Its entry at `(i, j) ∈ μ` is

> `rowPrefix μ i + j + 1`,   where   `rowPrefix μ i = ∑_{i' < i} μ.rowLen i'`

(the number of cells in the rows strictly above `i`, plus the position `j` within row `i`, plus 1).

This file builds it in two stages:

1. **The underlying semistandard tableau** `rowSuperstandardSsyt μ` — proved sorry-free. Rows are
   (weakly) increasing because `j` grows; columns are *strictly* increasing because
   `rowPrefix` strictly increases with the row index (each skipped row contributes at least one
   cell — `rowLen` is positive down to the bottom row by `rowLen_anti`).

2. **Nonemptiness of `StandardYoungTableau μ`** (the `BijOn` onto `{1, …, |μ|}`) — the base-tableau
   existence brick the Okounkov–Vershik exchange argument (`syt_all_connect_to_some`) needs. *(Stage
   2 is developed incrementally; see the tracked cores.)*

Pure combinatorics on `ℕ` (`§7c`-clean: no `ℝ`, no ordering on a ring, no `Real.*`). Reusable
independently of the seminormal machinery.

Ref: [sagan2001] (The Symmetric Group, §3.9 — the superstandard / row-reading tableau).
-/

namespace QOU.BraidKnot

open YoungDiagram Finset QOU.Mathlib

variable (μ : YoungDiagram)

/-- `rowPrefix μ i` = number of cells in the rows strictly above row `i`
(`∑_{i' < i} μ.rowLen i'`). This is the label offset of the first cell of row `i` in the
row-reading order. -/
def rowPrefix (i : ℕ) : ℕ := ∑ i' ∈ Finset.range i, μ.rowLen i'

@[simp] theorem rowPrefix_zero : rowPrefix μ 0 = 0 := by simp [rowPrefix]

theorem rowPrefix_succ (i : ℕ) : rowPrefix μ (i + 1) = rowPrefix μ i + μ.rowLen i := by
  simp [rowPrefix, Finset.sum_range_succ]

/-- `rowPrefix` is monotone in the row index (a sum of the nonnegative row lengths over a larger
initial range). -/
theorem rowPrefix_mono {i1 i2 : ℕ} (h : i1 ≤ i2) : rowPrefix μ i1 ≤ rowPrefix μ i2 := by
  induction i2, h using Nat.le_induction with
  | base => exact le_refl _
  | succ n _ ih => rw [rowPrefix_succ]; omega

/-- If row `i2` is nonempty (some `(i2, j) ∈ μ`) then any earlier row `i1 ≤ i2` is strictly longer
than the prefix gap allows: `rowPrefix μ i1 < rowPrefix μ i2` whenever `i1 < i2` and row `i1`
contains a cell. Here we get positivity of `rowLen i1` from `rowLen_anti`. -/
theorem rowPrefix_strictMono_of_mem {i1 i2 j : ℕ} (hlt : i1 < i2) (hcell : (i2, j) ∈ μ) :
    rowPrefix μ i1 < rowPrefix μ i2 := by
  have hrl2 : 0 < μ.rowLen i2 := by
    have := mem_iff_lt_rowLen.mp hcell; omega
  have hrl1 : 0 < μ.rowLen i1 :=
    lt_of_lt_of_le hrl2 (μ.rowLen_anti i1 i2 (le_of_lt hlt))
  have hstep : rowPrefix μ (i1 + 1) = rowPrefix μ i1 + μ.rowLen i1 := rowPrefix_succ μ i1
  have hmono : rowPrefix μ (i1 + 1) ≤ rowPrefix μ i2 := rowPrefix_mono μ hlt
  omega

/-- The row-reading entry: `rowPrefix μ i + j + 1` on cells of `μ`, `0` off the diagram. -/
def rowSuperstandardEntry (i j : ℕ) : ℕ :=
  if (i, j) ∈ μ then rowPrefix μ i + j + 1 else 0

/-- **The row-superstandard semistandard Young tableau of shape `μ` (sorry-free).** Rows increase
(weakly) because the position `j` grows; columns increase *strictly* because the row-prefix offset
strictly increases with the row index (`rowPrefix_strictMono_of_mem`). -/
def rowSuperstandardSsyt : SemistandardYoungTableau μ where
  entry := rowSuperstandardEntry μ
  row_weak' := by
    intro i j1 j2 hj hcell
    have hcell1 : (i, j1) ∈ μ := μ.up_left_mem (le_refl i) (le_of_lt hj) hcell
    simp only [rowSuperstandardEntry, if_pos hcell, if_pos hcell1]
    omega
  col_strict' := by
    intro i1 i2 j hi hcell
    have hcell1 : (i1, j) ∈ μ := μ.up_left_mem (le_of_lt hi) (le_refl j) hcell
    simp only [rowSuperstandardEntry, if_pos hcell, if_pos hcell1]
    have := rowPrefix_strictMono_of_mem μ hi hcell
    omega
  zeros' := by
    intro i j hnc
    simp only [rowSuperstandardEntry, if_neg hnc]

@[simp] theorem rowSuperstandardSsyt_apply (i j : ℕ) :
    (rowSuperstandardSsyt μ) i j = rowSuperstandardEntry μ i j := rfl

/-! ## Stage 2 — `|μ| = ∑ rowLen`, and the `BijOn` toward `Nonempty (StandardYoungTableau μ)` -/

/-- The cells of `μ` are the union of its (finitely many, indexed by `i < colLen 0`) rows;
distinct rows are disjoint (different first coordinate). -/
theorem cells_eq_biUnion :
    μ.cells = (Finset.range (μ.colLen 0)).biUnion μ.row := by
  ext ⟨i, j⟩
  simp only [Finset.mem_biUnion, Finset.mem_range, mem_row_iff, mem_cells]
  constructor
  · intro h
    exact ⟨i, mem_iff_lt_colLen.mp (μ.up_left_mem (le_refl i) (Nat.zero_le j) h), h, rfl⟩
  · rintro ⟨i', -, hmem, rfl⟩
    exact hmem

theorem rows_disjoint {i i' : ℕ} (hne : i ≠ i') : Disjoint (μ.row i) (μ.row i') := by
  rw [Finset.disjoint_left]
  rintro ⟨a, b⟩ ha hb
  rw [mem_row_iff] at ha hb
  exact hne (ha.2.symm.trans hb.2)

/-- **`|μ| = ∑_{i < colLen 0} rowLen i`** — the total cell count as the sum of row lengths. -/
theorem card_eq_sum_rowLen :
    μ.cells.card = ∑ i ∈ Finset.range (μ.colLen 0), μ.rowLen i := by
  rw [cells_eq_biUnion, Finset.card_biUnion (fun i _ i' _ hne => rows_disjoint μ hne)]
  exact Finset.sum_congr rfl (fun i _ => (rowLen_eq_card μ).symm)

/-- The label offset up to and including row `i` is at most the total cell count, whenever row `i`
contains a cell (so `i < colLen 0`). This is the upper bound the `BijOn`'s `MapsTo` needs. -/
theorem rowPrefix_succ_le_card {i j : ℕ} (hcell : (i, j) ∈ μ) :
    rowPrefix μ (i + 1) ≤ μ.cells.card := by
  rw [card_eq_sum_rowLen]
  have hi : i < μ.colLen 0 :=
    mem_iff_lt_colLen.mp (μ.up_left_mem (le_refl i) (Nat.zero_le j) hcell)
  have hmono : rowPrefix μ (i + 1) ≤ rowPrefix μ (μ.colLen 0) := rowPrefix_mono μ hi
  simpa [rowPrefix] using hmono

/-- The row-superstandard entry on a cell `(i, j) ∈ μ` is `rowPrefix μ i + j + 1`. -/
theorem rowSuperstandardSsyt_entry_of_mem {i j : ℕ} (h : (i, j) ∈ μ) :
    (rowSuperstandardSsyt μ).entry i j = rowPrefix μ i + j + 1 := by
  show rowSuperstandardEntry μ i j = _
  rw [rowSuperstandardEntry, if_pos h]

/-- **`MapsTo`**: the row-reading filling sends each cell into `{1, …, |μ|}`. Upper bound from
`rowPrefix_succ_le_card` (`j + 1 ≤ rowLen i`, then `rowPrefix (i+1) ≤ |μ|`). -/
theorem rowSuperstandard_mapsTo :
    Set.MapsTo (fun c : ℕ × ℕ => (rowSuperstandardSsyt μ).entry c.1 c.2)
      (μ.cells : Set (ℕ × ℕ)) (Set.Icc 1 μ.cells.card) := by
  rintro ⟨i, j⟩ hc
  rw [Finset.mem_coe, mem_cells] at hc
  simp only [rowSuperstandardSsyt_entry_of_mem μ hc, Set.mem_Icc]
  refine ⟨by omega, ?_⟩
  have hj : j < μ.rowLen i := mem_iff_lt_rowLen.mp hc
  have hb : rowPrefix μ (i + 1) ≤ μ.cells.card := rowPrefix_succ_le_card μ hc
  rw [rowPrefix_succ] at hb
  omega

/-- **`InjOn`**: distinct cells get distinct row-reading labels. If the labels agree, the rows must
agree (a later row's first label already exceeds any earlier row's last label, by
`rowPrefix_mono` + `j < rowLen`), and then the columns agree by cancellation. -/
theorem rowSuperstandard_injOn :
    Set.InjOn (fun c : ℕ × ℕ => (rowSuperstandardSsyt μ).entry c.1 c.2)
      (μ.cells : Set (ℕ × ℕ)) := by
  rintro ⟨i1, j1⟩ hc1 ⟨i2, j2⟩ hc2 heq
  rw [Finset.mem_coe, mem_cells] at hc1 hc2
  simp only [rowSuperstandardSsyt_entry_of_mem μ hc1, rowSuperstandardSsyt_entry_of_mem μ hc2] at heq
  have hj1 : j1 < μ.rowLen i1 := mem_iff_lt_rowLen.mp hc1
  have hj2 : j2 < μ.rowLen i2 := mem_iff_lt_rowLen.mp hc2
  have hi : i1 = i2 := by
    rcases lt_trichotomy i1 i2 with h | h | h
    · exfalso
      have h1 : rowPrefix μ (i1 + 1) ≤ rowPrefix μ i2 := rowPrefix_mono μ (by omega)
      rw [rowPrefix_succ] at h1; omega
    · exact h
    · exfalso
      have h1 : rowPrefix μ (i2 + 1) ≤ rowPrefix μ i1 := rowPrefix_mono μ (by omega)
      rw [rowPrefix_succ] at h1; omega
  subst hi
  have hj : j1 = j2 := by omega
  rw [hj]

/-- **`SurjOn`**: the row-reading filling hits every label in `{1, …, |μ|}`. It is injective
(`rowSuperstandard_injOn`) and maps the `|μ|` cells into `{1, …, |μ|}` (also `|μ|` elements), so it
is onto by counting (`Finset.surjOn_of_injOn_of_card_le`). -/
theorem rowSuperstandard_surjOn :
    Set.SurjOn (fun c : ℕ × ℕ => (rowSuperstandardSsyt μ).entry c.1 c.2)
      (μ.cells : Set (ℕ × ℕ)) (Set.Icc 1 μ.cells.card) := by
  -- The image of the cells is a subset of `Icc 1 |μ|` of the same cardinality (`|μ|`, by
  -- injectivity), hence equal to it; so every label is attained.
  have hsub : μ.cells.image (fun c : ℕ × ℕ => (rowSuperstandardSsyt μ).entry c.1 c.2)
      ⊆ Finset.Icc 1 μ.cells.card := by
    intro b hb
    rw [Finset.mem_image] at hb
    obtain ⟨c, hc, rfl⟩ := hb
    have hmap := rowSuperstandard_mapsTo μ (Finset.mem_coe.mpr hc)
    rw [Set.mem_Icc] at hmap; rw [Finset.mem_Icc]; exact hmap
  have hcardimg : (μ.cells.image (fun c : ℕ × ℕ => (rowSuperstandardSsyt μ).entry c.1 c.2)).card
      = μ.cells.card := Finset.card_image_of_injOn (rowSuperstandard_injOn μ)
  have himg : μ.cells.image (fun c : ℕ × ℕ => (rowSuperstandardSsyt μ).entry c.1 c.2)
      = Finset.Icc 1 μ.cells.card := by
    apply Finset.eq_of_subset_of_card_le hsub
    rw [hcardimg, Nat.card_Icc]; omega
  intro b hb
  rw [Set.mem_Icc] at hb
  have hbIcc : b ∈ Finset.Icc 1 μ.cells.card := Finset.mem_Icc.mpr hb
  rw [← himg, Finset.mem_image] at hbIcc
  obtain ⟨c, hc, hfc⟩ := hbIcc
  exact ⟨c, Finset.mem_coe.mpr hc, hfc⟩

/-- **The row-superstandard standard Young tableau** — the semistandard tableau above upgraded to a
`StandardYoungTableau` by the `BijOn` onto `{1, …, |μ|}` (`MapsTo` + `InjOn` + `SurjOn`). -/
noncomputable def rowSuperstandardStd : StandardYoungTableau μ where
  toSsyt := rowSuperstandardSsyt μ
  bijOn := ⟨rowSuperstandard_mapsTo μ, rowSuperstandard_injOn μ, rowSuperstandard_surjOn μ⟩

/-- **`StandardYoungTableau μ` is nonempty (sorry-free).** The base-tableau existence brick the
Okounkov–Vershik exchange argument (`syt_all_connect_to_some`) needs: the row-superstandard tableau
is an explicit witness. -/
instance instNonemptyStandardYoungTableau : Nonempty (StandardYoungTableau μ) :=
  ⟨rowSuperstandardStd μ⟩

end QOU.BraidKnot
