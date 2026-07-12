import QOU.Mathlib.SchenstedRecording
import QOU.Mathlib.SchenstedTableau

/-!
# Standard-labelling shift of the recording tableau

**Brick 9a.**  QOU's `StandardYoungTableau μ` ties its `bijOn` obligation to
`toSsyt.entry` mapping the cells onto `Set.Icc 1 μ.cells.card` — a **1-based**
labelling.  The recording tableau `Q(w)` produced by `insertWordRec` is
**0-based** (its timestamps are `0, …, |w|-1`, Brick 8).  A naive "+1 to every
entry" breaks the SSYT `zeros'` obligation off the shape (`0 + 1 ≠ 0`), so the
relabelling is applied to the underlying **list** tableau
`Q̃ = shiftT Q = Q.map (·.map (·+1))`, whose out-of-shape lookups are still `0`.

This file supplies the shift-invariance the realisation needs:

* `shiftT_shape` — the shape is unchanged;
* `shiftT_rowsSorted` / `shiftT_colStrict` — the SSYT order invariants survive the
  shift (`+1` is strictly monotone);
* `content_shiftT` — `content` commutes with the shift, so the shifted recording
  content is `{1, …, |w|}` (`content_shiftT_recording`), still `Nodup`;
* `recordingSSYT` — the shifted recording tableau `Q̃(w)` as a Mathlib
  `SemistandardYoungTableau`, its entries `1, …, |w|`.

The remaining `bijOn` bridge (`Q̃`'s entry map bijects the cells onto
`Icc 1 |w|`), yielding `insertWordSYT w : StandardYoungTableau _`, is Brick 9b.

Pure combinatorics on `ℕ`; nothing archimedean.
-/

namespace QOU.Mathlib.Schensted

open YoungDiagram List

/-- Increment every entry of a list tableau by one — the `0`-based → `1`-based
    relabelling that turns the recording tableau into a standard filling. -/
def shiftT (Q : List (List ℕ)) : List (List ℕ) := Q.map (fun row => row.map (· + 1))

@[simp] theorem shiftT_nil : shiftT [] = [] := rfl

@[simp] theorem shiftT_cons (r : List ℕ) (T : List (List ℕ)) :
    shiftT (r :: T) = r.map (· + 1) :: shiftT T := rfl

/-- Indexed lookup of a shifted row, in range: `(l.map (·+1)).getD j 0 = l.getD j 0 + 1`. -/
theorem getD_map_succ {l : List ℕ} {j : ℕ} (hj : j < l.length) :
    (l.map (· + 1)).getD j 0 = l.getD j 0 + 1 := by
  rw [List.getD_eq_getElem?_getD, List.getD_eq_getElem?_getD, List.getElem?_map,
    List.getElem?_eq_getElem hj]
  simp

/-- The shift preserves the shape (row lengths unchanged). -/
theorem shiftT_shape (Q : List (List ℕ)) : tableauShape (shiftT Q) = tableauShape Q := by
  simp [shiftT, tableauShape, List.map_map, Function.comp]

/-- The shift preserves weak-row sortedness (`+1` is monotone). -/
theorem shiftT_rowsSorted {Q : List (List ℕ)} (h : RowsSorted Q) : RowsSorted (shiftT Q) := by
  intro row hrow
  simp only [shiftT, List.mem_map] at hrow
  obtain ⟨r, hr, rfl⟩ := hrow
  exact List.pairwise_map.mpr ((h r hr).imp fun hab => Nat.add_le_add_right hab 1)

/-- The shift preserves the `StrictBelow` column relation, entry-wise. -/
theorem shiftT_strictBelow {u l : List ℕ} (h : StrictBelow u l) :
    StrictBelow (u.map (· + 1)) (l.map (· + 1)) := by
  obtain ⟨hlen, hval⟩ := h
  refine ⟨by simpa using hlen, ?_⟩
  intro j hj
  rw [List.length_map] at hj
  have hju : j < u.length := lt_of_lt_of_le hj hlen
  rw [getD_map_succ hj, getD_map_succ hju]
  exact Nat.add_lt_add_right (hval j hj) 1

/-- The shift preserves strict-column order. -/
theorem shiftT_colStrict {Q : List (List ℕ)} (h : ColStrict Q) : ColStrict (shiftT Q) := by
  rw [ColStrict, shiftT, List.isChain_map]
  exact h.imp fun _ _ hab => shiftT_strictBelow hab

/-- `content` commutes with the shift: `content (shiftT Q) = (content Q).map (·+1)`. -/
theorem content_shiftT (Q : List (List ℕ)) :
    content (shiftT Q) = (content Q).map (· + 1) := by
  induction Q with
  | nil => simp [content]
  | cons r T ih =>
      simp only [shiftT_cons, content_cons, ih, Multiset.map_add, Multiset.map_coe]

/-- Weak-row sortedness of the recording tableau (strict rows ⇒ weak). -/
theorem insertWordRec_snd_rowsSorted (w : List ℕ) : RowsSorted (insertWordRec w).2 := by
  intro row hrow
  exact (insertWordRec_rowsStrict w row hrow).imp (fun h => le_of_lt h)

/-- **The shifted recording tableau is filled with `1, 2, …, |w|`.** -/
theorem content_shiftT_recording (w : List ℕ) :
    content (shiftT (insertWordRec w).2) = (↑(List.range w.length) : Multiset ℕ).map (· + 1) := by
  rw [content_shiftT, insertWordRec_snd_content]

/-- The shifted recording timestamps are still distinct. -/
theorem content_shiftT_recording_nodup (w : List ℕ) :
    (content (shiftT (insertWordRec w).2)).Nodup := by
  rw [content_shiftT_recording, Multiset.map_coe, Multiset.coe_nodup]
  exact List.nodup_range.map (fun a b h => by omega)

/-- **The standard-labelled recording SSYT `Q̃(w)`.**  The shifted recording
    tableau realised as a Mathlib semistandard Young tableau on the recording
    shape; its entries are `1, …, |w|` (setting up the standard-tableau `bijOn`). -/
noncomputable def recordingSSYT (w : List ℕ) :
    SemistandardYoungTableau
      (ofRowLens (tableauShape (shiftT (insertWordRec w).2))
        (tableauShape_sorted (shiftT_colStrict (insertWordRec_colStrict w)))) :=
  toSSYT (shiftT_rowsSorted (insertWordRec_snd_rowsSorted w))
    (shiftT_colStrict (insertWordRec_colStrict w))

end QOU.Mathlib.Schensted
