import QOU.Mathlib.SchenstedReverseCascade

/-!
# QOU.Mathlib.SchenstedUninsertInvariants — what the reverse cascade preserves (RSK inverse, brick 11)

Brick 10 proved the cascade right inverse *one step at a time*, taking `RowsSorted`, `ColStrict`
and `NoEmptyRows` as hypotheses on the tableau it is handed. Iterating it — which is what
word-level surjectivity needs — requires knowing that the tableau `uninsert` *returns* still
carries those invariants, so the next step can be taken. That is this file.

Proved here, sorry-free:

* **`uninsert_rowsSorted`** — the reverse cascade keeps rows weakly increasing;
* **`uninsert_noEmptyRows`** — and keeps every row non-empty.

Both hold at **every** row index, with no side condition.

## Why `ColStrict` is not here, and where the corner condition actually belongs

Column-strictness is a different matter, and measuring it located the corner condition I had been
looking for in the wrong place.

`ColStrict` is `List.IsChain StrictBelow`, and `StrictBelow upper lower` asserts *both*
`lower.length ≤ upper.length` and `upper[j] < lower[j]`. Now take the keeping branch at row 0: the
result is `r.dropLast :: T`, so the first comparison becomes `StrictBelow r.dropLast row₁`, whose
length half reads

  `row₁.length ≤ r.length - 1`.

The hypothesis only supplies `row₁.length ≤ r.length`. The two differ exactly when row 1 is *as
long as* row 0 — that is, when the removed cell was **not** a corner of the shape. So:

* the right-inverse identity (brick 10) needs **no** corner condition — see that file's docstring;
* preserving `ColStrict` needs one, and cannot hold without it.

The failure is machine-checked, not asserted: `cornerWitness_colStrict` and
`cornerWitness_not_colStrict` exhibit `T = [[1,3],[2,4]]`, column-strict with a non-corner row 0,
whose reverse cascade at row 0 is not column-strict. `cornerWitness_rowsSorted_survives` and
`cornerWitness_noEmptyRows_survives` show the split is real on that same witness — the two
invariants proved here survive the very step that breaks the third.

That is not a gap in the RSK inverse: the reverse cascade is always run at the cell carrying the
largest entry of the recording tableau, which *is* a corner. The corner condition is supplied by
`Q`, one level up, and belongs in the statement that consumes it rather than here. Stating the two
invariants that hold unconditionally, and saying plainly what the third costs, is the point of
this file.

## Scope

Two invariants, unconditionally. `ColStrict` preservation under a corner hypothesis, word-level
surjectivity, and `RSKBurnsideHolds` for general `n` are the remainder of epic `qou-nrex`. Nothing
here claims them.

Pure combinatorics on `ℕ`; nothing archimedean.
-/

namespace QOU.Mathlib.Schensted

/-- Dropping the last cell keeps a row weakly increasing. -/
theorem sorted_dropLast {r : List ℕ} (h : r.Sorted (· ≤ ·)) : r.dropLast.Sorted (· ≤ ·) :=
  h.sublist (List.dropLast_sublist r)

/-- **The reverse cascade keeps rows weakly increasing.** Each row it touches changes either by
`dropLast` (a sublist) or by `rowUninsert`, which brick 1's `rowUninsert_sorted` covers; the rest
are carried through unchanged. -/
theorem uninsert_rowsSorted : ∀ (T : List (List ℕ)), RowsSorted T → ∀ (i : ℕ),
    RowsSorted (uninsert T i).1
  | [], _, i => by simp only [uninsert_nil]; exact rowsSorted_nil
  | r :: T, hs, 0 => by
      have hrs : r.Sorted (· ≤ ·) := hs r (List.mem_cons_self ..)
      have hTs : RowsSorted T := fun row hrow => hs row (List.mem_cons_of_mem r hrow)
      rw [uninsert_zero]
      simp only
      by_cases hshort : r.length ≤ 1
      · rw [if_pos hshort]; exact hTs
      · rw [if_neg hshort]
        intro row hrow
        rcases List.mem_cons.mp hrow with rfl | hrow'
        · exact sorted_dropLast hrs
        · exact hTs row hrow'
  | r :: T, hs, i + 1 => by
      have hrs : r.Sorted (· ≤ ·) := hs r (List.mem_cons_self ..)
      have hTs : RowsSorted T := fun row hrow => hs row (List.mem_cons_of_mem r hrow)
      have hrec := uninsert_rowsSorted T hTs i
      obtain ⟨T', w, hT⟩ : ∃ T' w, uninsert T i = (T', w) := ⟨_, _, rfl⟩
      have hT's : RowsSorted T' := by rw [hT] at hrec; exact hrec
      cases w with
      | none =>
          rw [uninsert_succ, hT]
          simp only
          intro row hrow
          rcases List.mem_cons.mp hrow with rfl | hrow'
          · exact hrs
          · exact hT's row hrow'
      | some y =>
          obtain ⟨r', v, hru⟩ : ∃ r' v, rowUninsert r y = (r', v) := ⟨_, _, rfl⟩
          have hr's : r'.Sorted (· ≤ ·) := by
            have := rowUninsert_sorted r hrs y
            rwa [hru] at this
          rw [uninsert_succ, hT]
          simp only
          rw [hru]
          cases v with
          | none =>
              simp only
              intro row hrow
              rcases List.mem_cons.mp hrow with rfl | hrow'
              · exact hrs
              · exact hT's row hrow'
          | some v =>
              simp only
              intro row hrow
              rcases List.mem_cons.mp hrow with rfl | hrow'
              · exact hr's
              · exact hT's row hrow'

/-- **The reverse cascade never leaves an empty row.** A row shortened by `rowUninsert` keeps its
length (`rowUninsert_length`); the one row that loses a cell is deleted outright when that would
empty it, which is the whole reason `uninsert` tests `r.length ≤ 1`. -/
theorem uninsert_noEmptyRows : ∀ (T : List (List ℕ)), NoEmptyRows T → ∀ (i : ℕ),
    NoEmptyRows (uninsert T i).1
  | [], _, i => by simp only [uninsert_nil]; exact noEmptyRows_nil
  | r :: T, hne, 0 => by
      have hTne : NoEmptyRows T := fun row hrow => hne row (List.mem_cons_of_mem r hrow)
      rw [uninsert_zero]
      simp only
      by_cases hshort : r.length ≤ 1
      · rw [if_pos hshort]; exact hTne
      · rw [if_neg hshort]
        intro row hrow
        rcases List.mem_cons.mp hrow with rfl | hrow'
        · intro hcon
          have : r.dropLast.length = 0 := by rw [hcon]; rfl
          rw [List.length_dropLast] at this
          omega
        · exact hTne row hrow'
  | r :: T, hne, i + 1 => by
      have hrne : r ≠ [] := hne r (List.mem_cons_self ..)
      have hTne : NoEmptyRows T := fun row hrow => hne row (List.mem_cons_of_mem r hrow)
      have hrec := uninsert_noEmptyRows T hTne i
      obtain ⟨T', w, hT⟩ : ∃ T' w, uninsert T i = (T', w) := ⟨_, _, rfl⟩
      have hT'ne : NoEmptyRows T' := by rw [hT] at hrec; exact hrec
      cases w with
      | none =>
          rw [uninsert_succ, hT]
          simp only
          intro row hrow
          rcases List.mem_cons.mp hrow with rfl | hrow'
          · exact hrne
          · exact hT'ne row hrow'
      | some y =>
          obtain ⟨r', v, hru⟩ : ∃ r' v, rowUninsert r y = (r', v) := ⟨_, _, rfl⟩
          have hr'ne : r' ≠ [] := by
            have hl : (rowUninsert r y).1.length = r.length := rowUninsert_length r y
            rw [hru] at hl
            simp only at hl
            intro hcon
            rw [hcon] at hl
            exact hrne (List.eq_nil_of_length_eq_zero hl.symm)
          rw [uninsert_succ, hT]
          simp only
          rw [hru]
          cases v with
          | none =>
              simp only
              intro row hrow
              rcases List.mem_cons.mp hrow with rfl | hrow'
              · exact hrne
              · exact hT'ne row hrow'
          | some v =>
              simp only
              intro row hrow
              rcases List.mem_cons.mp hrow with rfl | hrow'
              · exact hr'ne
              · exact hT'ne row hrow'

/-- The witness for the corner discussion above: a row-sorted, column-strict tableau with no empty
rows whose row 0 is *not* a corner — row 1 is exactly as long. -/
theorem cornerWitness_rowsSorted : RowsSorted [[1, 3], [2, 4]] := by
  intro row hrow
  simp only [List.mem_cons, List.not_mem_nil, or_false] at hrow
  rcases hrow with rfl | rfl <;> decide

theorem cornerWitness_noEmptyRows : NoEmptyRows [[1, 3], [2, 4]] := by
  intro row hrow
  simp only [List.mem_cons, List.not_mem_nil, or_false] at hrow
  rcases hrow with rfl | rfl <;> simp

theorem cornerWitness_colStrict : ColStrict [[1, 3], [2, 4]] := by
  rw [ColStrict, List.isChain_cons_cons]
  refine ⟨⟨by simp, ?_⟩, colStrict_singleton _⟩
  intro j hj
  simp only [List.length_cons, List.length_nil] at hj
  -- `interval_cases` is not in scope here; peel the two in-range columns by hand.
  rcases j with _ | _ | j
  · decide
  · decide
  · exact absurd hj (by omega)

/-- **The corner condition is not optional for `ColStrict`** — machine-checked, not asserted.

Undoing at the non-corner row 0 shortens row 0 to `[1]` and leaves row 1 alone, so the shape
becomes `(1, 2)` — not a Young diagram — and `StrictBelow` fails on its length half. -/
theorem cornerWitness_not_colStrict : ¬ ColStrict (uninsert [[1, 3], [2, 4]] 0).1 := by
  have h : (uninsert [[1, 3], [2, 4]] 0).1 = [[1], [2, 4]] := by decide
  rw [h, ColStrict, List.isChain_cons_cons]
  rintro ⟨⟨hl, -⟩, -⟩
  simp at hl

/-- The same witness, showing the split is real: the two invariants proved above *do* survive the
step that breaks `ColStrict`. -/
theorem cornerWitness_rowsSorted_survives : RowsSorted (uninsert [[1, 3], [2, 4]] 0).1 :=
  uninsert_rowsSorted _ cornerWitness_rowsSorted 0

theorem cornerWitness_noEmptyRows_survives : NoEmptyRows (uninsert [[1, 3], [2, 4]] 0).1 :=
  uninsert_noEmptyRows _ cornerWitness_noEmptyRows 0

end QOU.Mathlib.Schensted
