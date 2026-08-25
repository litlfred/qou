import QOU.Mathlib.SchenstedReverseRow

/-!
# QOU.Mathlib.SchenstedReverseCascade — undoing the insertion cascade (RSK inverse, brick 2)

Brick 1 (`SchenstedReverseRow`) inverted Schensted insertion on a **single row**. This file
lifts that to the **cascade**: `insert T x` drops `x` into row 0, bumps down the rows, and finally
appends a cell in exactly one row; `uninsert T i` removes the last cell of row `i` and pushes the
displaced value back up through rows `i-1, …, 0`, returning what falls out of the top.

Two definitions and one theorem:

* `newRowIndex T x` — which row `insert T x` appends its new cell to. Defined by the same
  recursion as `insert`, so it is not a search: it just records where the recursion stopped.
* `uninsert T i` — the reverse cascade at row `i`.
* **`uninsert_insert`** — the inversion law: `uninsert (insert T x) (newRowIndex T x) = (T, some x)`
  for a row-sorted tableau with no empty rows.

## Why the two side conditions

`RowsSorted T` is what brick 1's `rowUninsert_rowInsert` needs on each row it undoes. The
no-empty-rows condition is what lets `uninsert` decide, at the target row, between *shortening* a
row and *deleting* it: a row that had one cell and loses it must go, or the tableau grows a
spurious empty row and the shapes stop matching. Both are preserved by `insert`
(`insert_rowsSorted` upstream, `insert_noEmptyRows` here), so the cascade composes.

## Scope

One insertion step, undone. Iterating this to invert `insertWordRec` — and thence the RSK
bijection and `RSKBurnsideHolds` — is brick 3 and beyond (epic `qou-nrex`). Nothing here claims
them.

Pure combinatorics on `ℕ`; nothing archimedean.
-/

namespace QOU.Mathlib.Schensted

/-- **Where the new cell lands.** `insert T x` appends a cell to exactly one row; this records its
index, by the same recursion `insert` itself uses. -/
def newRowIndex : List (List ℕ) → ℕ → ℕ
  | [], _ => 0
  | row :: rest, x =>
      match (rowInsert row x).2 with
      | none => 0
      | some y => newRowIndex rest y + 1

/-- **No empty rows** — a tableau well-formedness condition. `uninsert` needs it to know that a row
losing its only cell should be deleted rather than left behind as `[]`. -/
def NoEmptyRows (T : List (List ℕ)) : Prop := ∀ row ∈ T, row ≠ []

@[simp] theorem noEmptyRows_nil : NoEmptyRows [] := by intro _ h; simp at h

/-- **A no-bump insertion appends.** When `rowInsert` reports no bump it has put `x` at the end. -/
theorem rowInsert_eq_append_of_none : ∀ (r : List ℕ) (x : ℕ), (rowInsert r x).2 = none →
    (rowInsert r x).1 = r ++ [x]
  | [], x, _ => rfl
  | a :: r, x, h => by
      rw [rowInsert_cons] at h ⊢
      by_cases hx : x < a
      · rw [if_pos hx] at h; simp at h
      · rw [if_neg hx] at h ⊢
        simp only at h ⊢
        rw [rowInsert_eq_append_of_none r x h]
        simp

/-- `insert` never creates an empty row. -/
theorem insert_noEmptyRows : ∀ {T : List (List ℕ)}, NoEmptyRows T → ∀ x, NoEmptyRows (insert T x)
  | [], _, x => by
      intro row hrow
      simp only [insert, List.mem_singleton] at hrow
      simp [hrow]
  | r :: T, h, x => by
      intro row hrow
      have hrne : ∀ z, (rowInsert r z).1 ≠ [] := by
        intro z
        cases r with
        | nil => simp [rowInsert]
        | cons a rest =>
            rw [rowInsert_cons]
            by_cases hz : z < a <;> simp [hz]
      rw [insert] at hrow
      cases hb : (rowInsert r x).2 with
      | none =>
          rw [hb] at hrow
          simp only [List.mem_cons] at hrow
          rcases hrow with rfl | hrow
          · exact hrne x
          · exact h row (List.mem_cons_of_mem r hrow)
      | some y =>
          rw [hb] at hrow
          simp only [List.mem_cons] at hrow
          rcases hrow with rfl | hrow
          · exact hrne x
          · exact insert_noEmptyRows (fun w hw => h w (List.mem_cons_of_mem r hw)) y row hrow

/-- **The reverse cascade.** `uninsert T i` removes the last cell of row `i` and pushes the removed
value up through rows `i-1, …, 0` by reverse row insertion, returning the value displaced out of
the top row.

At the target row a length-one row is deleted rather than left empty — see `NoEmptyRows`. -/
def uninsert : List (List ℕ) → ℕ → List (List ℕ) × Option ℕ
  | [], _ => ([], none)
  | r :: T, 0 => ((if r.length ≤ 1 then T else r.dropLast :: T), r.getLast?)
  | r :: T, i + 1 =>
      match uninsert T i with
      | (T', some y) =>
          match rowUninsert r y with
          | (r', some z) => (r' :: T', some z)
          | (_, none) => (r :: T', none)
      | (T', none) => (r :: T', none)

@[simp] theorem uninsert_nil (i : ℕ) : uninsert [] i = ([], none) := rfl

theorem uninsert_zero (r : List ℕ) (T : List (List ℕ)) :
    uninsert (r :: T) 0 = ((if r.length ≤ 1 then T else r.dropLast :: T), r.getLast?) := rfl

theorem uninsert_succ (r : List ℕ) (T : List (List ℕ)) (i : ℕ) :
    uninsert (r :: T) (i + 1) =
      match uninsert T i with
      | (T', some y) =>
          match rowUninsert r y with
          | (r', some z) => (r' :: T', some z)
          | (_, none) => (r :: T', none)
      | (T', none) => (r :: T', none) := rfl

/-- **The cascade inversion law.** Undoing `insert T x` at the row where it put its new cell
recovers `T` and reports `x`.

The recursion follows `insert`'s own: at the appending row, brick 1's no-bump case says the row is
`old ++ [x]`, so `dropLast` / `getLast?` recover it; at a bumping row, brick 1's inversion law
(`rowUninsert_rowInsert`) undoes the bump and the recursion supplies the value to push up. -/
theorem uninsert_insert : ∀ (T : List (List ℕ)), RowsSorted T → NoEmptyRows T → ∀ (x : ℕ),
    uninsert (insert T x) (newRowIndex T x) = (T, some x)
  | [], _, _, x => by
      simp [insert, newRowIndex, uninsert_zero]
  | r :: T, hs, hne, x => by
      have hrs : r.Sorted (· ≤ ·) := hs r (List.mem_cons_self ..)
      have hTs : RowsSorted T := fun row hrow => hs row (List.mem_cons_of_mem r hrow)
      have hTne : NoEmptyRows T := fun row hrow => hne row (List.mem_cons_of_mem r hrow)
      have hr0 : r ≠ [] := hne r (List.mem_cons_self ..)
      rw [insert, newRowIndex]
      cases hb : (rowInsert r x).2 with
      | none =>
          -- the new cell is appended here: the row is `r ++ [x]`
          rw [uninsert_zero, rowInsert_eq_append_of_none r x hb]
          have hlen : ¬ (r ++ [x]).length ≤ 1 := by
            have : 1 ≤ r.length := List.length_pos_iff.mpr hr0
            simp only [List.length_append, List.length_singleton]
            omega
          rw [if_neg hlen, List.dropLast_concat, List.getLast?_concat]
      | some y =>
          -- the cell lands further down; undo the bump on the way back up
          rw [uninsert_succ, uninsert_insert T hTs hTne y]
          simp only
          rw [rowUninsert_rowInsert r hrs x y hb]

end QOU.Mathlib.Schensted
