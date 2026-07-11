import Mathlib.Combinatorics.Young.SemistandardTableau
import QOU.Mathlib.SchenstedInsertion

/-!
# Schensted insertion tableaux as Mathlib `SemistandardYoungTableau`

**Brick 7 — SSYT-object realization.**  Bricks 1–6b built the row-insertion map
`insertWord` / `insertWordRec` and proved the list-form invariants
(`RowsSorted`, `ColStrict`) together with the general-index monotonicity lemmas
(`rowsSorted_getD_le`, `colStrict_getD_lt`) and the shape lemmas
(`colShapeYoung_iff_shape`, `colStrict_len_le`).

Here we package any list tableau `T : List (List ℕ)` whose rows are weakly
increasing (`RowsSorted`) and whose columns are strictly increasing
(`ColStrict`) as an honest Mathlib
`SemistandardYoungTableau (YoungDiagram.ofRowLens (tableauShape T) _)`, with

    entry i j := (T.getD i []).getD j 0.

The three structure obligations discharge directly:

* `row_weak'`  ← `rowsSorted_getD_le`,
* `col_strict'` ← `colStrict_getD_lt`,
* `zeros'`     ← `List.getElem?_eq_none` past the row length.

The row-length shape `tableauShape T` is a valid `ofRowLens` argument because
column-strictness forces the row lengths to weakly decrease
(`colShapeYoung_iff_shape` + `IsChain.pairwise`).

Specialising to `T = insertWord w` gives the semistandard insertion tableau
`P(w)` of a word as a Mathlib object (`insertWordSSYT`), the first bridge from
the QOU RSK program into Mathlib's `numStandardYoungTableaux` world.
-/

namespace QOU.Mathlib.Schensted

open YoungDiagram List

/-- The shape list has the same length as the tableau (one entry per row). -/
theorem shape_length (T : List (List ℕ)) : (tableauShape T).length = T.length := by
  simp [tableauShape]

/-- Row-length lookup of the shape is the length of that row (out-of-range rows
    are empty on both sides, so this holds unconditionally). -/
theorem shape_getD (T : List (List ℕ)) (i : ℕ) :
    (tableauShape T).getD i 0 = (T.getD i []).length := by
  unfold tableauShape
  rw [List.getD_eq_getElem?_getD, List.getD_eq_getElem?_getD, List.getElem?_map]
  cases T[i]? <;> simp

/-- Membership in the row-length Young diagram, expressed via `getD` on `T`. -/
theorem mem_shape_iff {T : List (List ℕ)}
    {hw : (tableauShape T).Sorted (· ≥ ·)} {i j : ℕ} :
    (i, j) ∈ ofRowLens (tableauShape T) hw ↔ j < (T.getD i []).length := by
  rw [mem_ofRowLens]
  simp only [tableauShape, List.length_map, List.getElem_map]
  constructor
  · rintro ⟨hi, hj⟩
    rwa [getD_row_eq hi]
  · intro hj
    have hi : i < T.length := by
      by_contra hge; push_neg at hge
      rw [getD_row_past hge] at hj; simp at hj
    exact ⟨hi, by rwa [← getD_row_eq hi]⟩

/-- The shape list of a column-strict tableau is weakly decreasing, hence a valid
    `ofRowLens` argument. -/
theorem tableauShape_sorted {T : List (List ℕ)} (h : ColStrict T) :
    (tableauShape T).Sorted (· ≥ ·) := by
  have hchain : (tableauShape T).IsChain (· ≥ ·) :=
    (colShapeYoung_iff_shape T).mp (colStrict_shapeYoung h)
  exact hchain.pairwise

/-- **The Schensted semistandard Young tableau.**  A list tableau with weakly
    increasing rows (`RowsSorted`) and strictly increasing columns (`ColStrict`)
    is a Mathlib `SemistandardYoungTableau` on its row-length shape, with
    `entry i j = (T.getD i []).getD j 0`. -/
def toSSYT {T : List (List ℕ)} (hrow : RowsSorted T) (hcol : ColStrict T) :
    SemistandardYoungTableau (ofRowLens (tableauShape T) (tableauShape_sorted hcol)) where
  entry i j := (T.getD i []).getD j 0
  row_weak' {i j1 j2} hj hmem := by
    rw [mem_shape_iff] at hmem
    exact rowsSorted_getD_le hrow (le_of_lt hj) hmem
  col_strict' {i1 i2 j} hi hmem := by
    rw [mem_shape_iff] at hmem
    exact colStrict_getD_lt hcol hi hmem
  zeros' {i j} hmem := by
    rw [mem_shape_iff] at hmem
    push_neg at hmem
    rw [List.getD_eq_getElem?_getD, List.getElem?_eq_none hmem, Option.getD_none]

@[simp] theorem toSSYT_entry {T : List (List ℕ)} (hrow : RowsSorted T)
    (hcol : ColStrict T) (i j : ℕ) :
    (toSSYT hrow hcol) i j = (T.getD i []).getD j 0 := rfl

/-- The insertion tableau `P(w)` of a word `w`, realised as a Mathlib
    semistandard Young tableau on the shape `tableauShape (insertWord w)`. -/
def insertWordSSYT (w : List ℕ) :
    SemistandardYoungTableau
      (ofRowLens (tableauShape (insertWord w))
        (tableauShape_sorted (insertWord_colStrict w))) :=
  toSSYT (insertWord_rowsSorted w) (insertWord_colStrict w)

@[simp] theorem insertWordSSYT_entry (w : List ℕ) (i j : ℕ) :
    (insertWordSSYT w) i j = ((insertWord w).getD i []).getD j 0 := rfl

end QOU.Mathlib.Schensted
