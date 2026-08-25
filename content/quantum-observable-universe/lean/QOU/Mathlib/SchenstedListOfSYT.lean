import QOU.Mathlib.SchenstedStandardGeneric
import QOU.Mathlib.SchenstedRSKSurjective

/-!
# QOU.Mathlib.SchenstedListOfSYT — a standard Young tableau as a list tableau

Brick 33 of epic `qou-nrex` (RSK inverse).

Brick 32 proved surjectivity onto standard pairs **in the `List (List ℕ)` representation**.
`rskPair` lands in `Σ μ : YoungDiagram, StandardYoungTableau μ × StandardYoungTableau μ`, so what
stands between the two is a representation bridge. `listStandardYT` (brick 10) crosses it one way;
this file starts the other.

`toListTableau S` reads a standard Young tableau off its cells, row by row, and this file proves it
lands in the class brick 32 consumes:

* `tableauShape_toListTableau` — its shape is `μ.rowLens`, on the nose;
* `rows_strict_toListTableau` / `rowsSorted_toListTableau` — rows strictly (hence weakly) increase;
* `colStrict_toListTableau` — columns are `StrictBelow`, both halves: the length condition is
  `rowLen_anti` and the entry condition is the SSYT's `col_strict`;
* `noEmptyRows_toListTableau`, `nodup_flatten_toListTableau`.

Column strictness is where the two notions differ in shape rather than in content: `StrictBelow`
bundles the Young-shape length condition with the entry comparison, while a `SemistandardYoungTableau`
keeps them apart — the lengths in the diagram, the entries in `col_strict`. The bridge has to supply
both, and `rowLen_anti` is the half that has no counterpart in the tableau's own data.

## Scope

Structure only. The **content** of `toListTableau S` — that its entries are exactly `1 … |μ|`, and
the shift to the `0`-based timestamps brick 32's `Q` hypotheses use — is the next brick, and the
round trip `listStandardYT (toListTableau S) = S` is past it. Nothing here claims `rskPair` is
bijective; `RSKBurnsideHolds` for general `n` remains open.

Pure combinatorics on `ℕ`; nothing archimedean; no fit.

**Scope note superseded (2026-08-23).** The scope paragraph above records the state of the arc when
this brick landed. `RSKBurnsideHolds` is now proved for **every** `n`
(`QOU.Mathlib.rskBurnsideHolds`, brick 42), and `SnIsotypicSpechtSplit` is inhabited, so any
statement here that they "remain open" or hold "only for `n ≤ 12`" describes history rather than the
corpus. The per-brick scope is otherwise unchanged and still accurate.

-/

namespace QOU.Mathlib.Schensted

open YoungDiagram

variable {μ : YoungDiagram}

/-- **A standard Young tableau read off row by row.** Row `i` is the entries at the cells
`(i, 0), …, (i, rowLen i - 1)`; there are as many rows as `μ.rowLens` has entries. -/
def toListTableau (S : QOU.Mathlib.StandardYoungTableau μ) : List (List ℕ) :=
  (List.range μ.rowLens.length).map
    (fun i => (List.range (μ.rowLen i)).map (fun j => S.entry i j))

@[simp] theorem length_toListTableau (S : QOU.Mathlib.StandardYoungTableau μ) :
    (toListTableau S).length = μ.rowLens.length := by simp [toListTableau]

/-- Row `i` of the list tableau, in range. -/
theorem getElem_toListTableau (S : QOU.Mathlib.StandardYoungTableau μ) {i : ℕ}
    (hi : i < (toListTableau S).length) :
    (toListTableau S)[i] = (List.range (μ.rowLen i)).map (fun j => S.entry i j) := by
  simp [toListTableau]

/-- Entry `(i, j)` of the list tableau, in range. -/
theorem getD_getD_toListTableau (S : QOU.Mathlib.StandardYoungTableau μ) {i j : ℕ}
    (hi : i < (toListTableau S).length) (hj : j < μ.rowLen i) :
    ((toListTableau S).getD i []).getD j 0 = S.entry i j := by
  rw [getD_row_eq hi, getElem_toListTableau S hi,
    getD_eq_getElem_mem (by simpa using hj)]
  simp

/-- **The shape is the diagram's row lengths**, on the nose. -/
theorem tableauShape_toListTableau (S : QOU.Mathlib.StandardYoungTableau μ) :
    tableauShape (toListTableau S) = μ.rowLens := by
  rw [tableauShape, toListTableau, List.map_map]
  refine List.ext_getElem (by simp) (fun n h1 h2 => ?_)
  simp only [List.getElem_map, List.getElem_range, Function.comp_apply, List.length_map,
    List.length_range]
  exact get_rowLens.symm

/-- **Rows strictly increase** — the standard-tableau strengthening of the SSYT's weak rows. -/
theorem rows_strict_toListTableau (S : QOU.Mathlib.StandardYoungTableau μ) :
    ∀ row ∈ toListTableau S, row.Sorted (· < ·) := by
  intro row hrow
  simp only [toListTableau, List.mem_map] at hrow
  obtain ⟨i, _, rfl⟩ := hrow
  refine List.pairwise_iff_getElem.mpr (fun a b ha hb hab => ?_)
  simp only [List.length_map, List.length_range] at ha hb
  simp only [List.getElem_map, List.getElem_range]
  exact S.row_strict hab (mem_iff_lt_rowLen.mpr hb)

theorem rowsSorted_toListTableau (S : QOU.Mathlib.StandardYoungTableau μ) :
    RowsSorted (toListTableau S) :=
  fun row hrow => (rows_strict_toListTableau S row hrow).imp le_of_lt

/-- No row of a Young diagram has length zero, so no row of the list tableau is empty. -/
theorem noEmptyRows_toListTableau (S : QOU.Mathlib.StandardYoungTableau μ) :
    NoEmptyRows (toListTableau S) := by
  intro row hrow
  simp only [toListTableau, List.mem_map] at hrow
  obtain ⟨i, hi, rfl⟩ := hrow
  rw [List.mem_range] at hi
  have hpos : 0 < μ.rowLen i := by
    have := μ.pos_of_mem_rowLens μ.rowLens[i] (List.getElem_mem hi)
    rwa [get_rowLens] at this
  intro hnil
  have := congrArg List.length hnil
  simp only [List.length_map, List.length_range, List.length_nil] at this
  omega

/-- **Columns are `StrictBelow`.** Both halves are needed and they come from different places: the
length condition is the diagram's `rowLen_anti`, the entry condition the tableau's `col_strict`. -/
theorem colStrict_toListTableau (S : QOU.Mathlib.StandardYoungTableau μ) :
    ColStrict (toListTableau S) := by
  rw [ColStrict, List.isChain_iff_getElem]
  intro i hi
  have hi0 : i < (toListTableau S).length := by omega
  have hle : μ.rowLen (i + 1) ≤ μ.rowLen i := μ.rowLen_anti i (i + 1) (by omega)
  rw [getElem_toListTableau S hi0, getElem_toListTableau S hi]
  refine ⟨by simp [hle], fun j hj => ?_⟩
  simp only [List.length_map, List.length_range] at hj
  rw [getD_eq_getElem_mem (by simpa using (by omega : j < μ.rowLen i)),
    getD_eq_getElem_mem (by simpa using hj)]
  simp only [List.getElem_map, List.getElem_range]
  exact S.toSsyt.col_strict (by omega) (mem_iff_lt_rowLen.mpr hj)

/-- **The entries are distinct.** Within a row this is strictness; across rows it is injectivity of
the filling — two cells carrying the same value are the same cell, hence in the same row. -/
theorem nodup_flatten_toListTableau (S : QOU.Mathlib.StandardYoungTableau μ) :
    (toListTableau S).flatten.Nodup := by
  rw [List.nodup_flatten]
  refine ⟨fun row hrow => (rows_strict_toListTableau S row hrow).nodup, ?_⟩
  simp only [toListTableau, List.pairwise_map]
  refine List.pairwise_iff_getElem.mpr (fun a b ha hb hab => ?_)
  simp only [List.length_range] at ha hb
  simp only [List.getElem_range]
  intro x hxa hxb
  rw [List.mem_map] at hxa hxb
  obtain ⟨ja, hja, hxa'⟩ := hxa
  obtain ⟨jb, hjb, hxb'⟩ := hxb
  rw [List.mem_range] at hja hjb
  have heq : S.entry a ja = S.entry b jb := by rw [hxa', hxb']
  have hcell := S.injOn_cells
    (QOU.Mathlib.StandardYoungTableau.mem_coe_cells (mem_iff_lt_rowLen.mpr hja))
    (QOU.Mathlib.StandardYoungTableau.mem_coe_cells (mem_iff_lt_rowLen.mpr hjb)) heq
  exact absurd (congrArg Prod.fst hcell) (Nat.ne_of_lt hab)

end QOU.Mathlib.Schensted
