import QOU.Mathlib.SchenstedListOfSYT

/-!
# QOU.Mathlib.SchenstedRecordingOfSYT — a standard Young tableau as a recording tableau

Brick 34 of epic `qou-nrex` (RSK inverse).

Brick 33 read a standard Young tableau off its cells as a list tableau and proved every structural
invariant brick 32 asks of `Q` — except the one that is not structural: **content**. Brick 32's `Q`
holds the timestamps `0, …, n-1`, because `insertWordRec` starts counting at `0`; a
`StandardYoungTableau` holds `1, …, |μ|`, because its bijection is onto `Set.Icc 1 |μ|`. The two
conventions differ by one, and `insertWordSYT` already pays that difference in the other direction
via `shiftT`.

* `mem_flatten_toListTableau` — the entries are the image of the cells;
* `mem_flatten_toListTableau_iff_Icc` — hence exactly `1, …, |μ|`, from `bijOn` (`mapsTo` one way,
  `surjOn` the other);
* `unshiftT` — the down-shift, with the structural invariants transported across it. It is the
  inverse of the existing `shiftT` on a tableau whose entries are positive, which is exactly what
  the content fact supplies.
* **`toRecordingTableau`** and its bundle — the `0`-based tableau, with every hypothesis brick 32
  takes: column-strict, rows strictly increasing, entries distinct, no empty rows, shape
  `μ.rowLens`, and content `{0, …, |μ|-1}`.

## Scope

The `Q` argument of brick 32, assembled. It does **not** yet run brick 32 on it: that also needs the
`P` side (`hshape : tableauShape P = addCellSteps [] (qPositions Q n)`, i.e. that the two tableaux
of the pair share a shape) and, for `rskPair` proper, the round trip
`listStandardYT (toListTableau S) = S` in the other direction. Neither is claimed here, `rskPair`
bijectivity is not claimed, and `RSKBurnsideHolds` for general `n` remains open.

Pure combinatorics on `ℕ`; nothing archimedean; no fit.
-/

namespace QOU.Mathlib.Schensted

open YoungDiagram

variable {μ : YoungDiagram}

/-- **The entries are the image of the cells.** -/
theorem mem_flatten_toListTableau (S : QOU.Mathlib.StandardYoungTableau μ) {a : ℕ} :
    a ∈ (toListTableau S).flatten ↔ ∃ i j, (i, j) ∈ μ ∧ S.entry i j = a := by
  rw [List.mem_flatten]
  constructor
  · rintro ⟨row, hrow, ha⟩
    simp only [toListTableau, List.mem_map, List.mem_range] at hrow
    obtain ⟨i, _, rfl⟩ := hrow
    rw [List.mem_map] at ha
    obtain ⟨j, hj, hja⟩ := ha
    rw [List.mem_range] at hj
    exact ⟨i, j, mem_iff_lt_rowLen.mpr hj, hja⟩
  · rintro ⟨i, j, hij, rfl⟩
    have hi : i < μ.rowLens.length := by
      rw [length_rowLens]
      exact mem_iff_lt_colLen.mp (μ.up_left_mem (le_refl i) (Nat.zero_le j) hij)
    refine ⟨(List.range (μ.rowLen i)).map (fun j => S.entry i j), ?_, ?_⟩
    · simp only [toListTableau, List.mem_map, List.mem_range]
      exact ⟨i, hi, rfl⟩
    · rw [List.mem_map]
      exact ⟨j, List.mem_range.mpr (mem_iff_lt_rowLen.mp hij), rfl⟩

/-- **The entries are exactly `1, …, |μ|`** — both directions of the filling's bijectivity. -/
theorem mem_flatten_toListTableau_iff_Icc (S : QOU.Mathlib.StandardYoungTableau μ) {a : ℕ} :
    a ∈ (toListTableau S).flatten ↔ 1 ≤ a ∧ a ≤ μ.cells.card := by
  rw [mem_flatten_toListTableau]
  constructor
  · rintro ⟨i, j, hij, rfl⟩
    have h := S.mapsTo_cells (QOU.Mathlib.StandardYoungTableau.mem_coe_cells hij)
    exact ⟨h.1, h.2⟩
  · rintro ⟨h1, h2⟩
    obtain ⟨c, hc, hca⟩ := S.bijOn.surjOn (Set.mem_Icc.mpr ⟨h1, h2⟩)
    exact ⟨c.1, c.2, (YoungDiagram.mem_cells c).mp (Finset.mem_coe.mp hc), hca⟩

/-- Every entry is positive — the hypothesis the down-shift needs. -/
theorem pos_of_mem_flatten_toListTableau (S : QOU.Mathlib.StandardYoungTableau μ) :
    ∀ a ∈ (toListTableau S).flatten, 1 ≤ a :=
  fun _ ha => ((mem_flatten_toListTableau_iff_Icc S).mp ha).1

/-- **Shift every entry down by one.** The inverse of `shiftT` on a tableau of positive entries;
it turns a standard tableau's `1`-based filling into the `0`-based timestamps the recording
machinery counts in. -/
def unshiftT (Q : List (List ℕ)) : List (List ℕ) := Q.map (fun row => row.map (· - 1))

/-- Reading an entry commutes with the shift — including past the end, where the default `0` is
already a fixed point of `(· - 1)`. -/
theorem getD_map_pred (l : List ℕ) (j : ℕ) : (l.map (· - 1)).getD j 0 = l.getD j 0 - 1 := by
  by_cases hj : j < l.length
  · rw [getD_eq_getElem_mem (by simpa using hj), getD_eq_getElem_mem hj]
    simp
  · rw [getD_past (by simpa using Nat.not_lt.mp hj), getD_past (Nat.not_lt.mp hj)]

@[simp] theorem tableauShape_unshiftT (Q : List (List ℕ)) :
    tableauShape (unshiftT Q) = tableauShape Q := by
  simp [tableauShape, unshiftT, List.map_map, Function.comp]

theorem unshiftT_flatten (Q : List (List ℕ)) :
    (unshiftT Q).flatten = Q.flatten.map (· - 1) := List.map_flatten.symm

theorem unshiftT_noEmptyRows {Q : List (List ℕ)} (h : NoEmptyRows Q) :
    NoEmptyRows (unshiftT Q) := by
  intro row hrow
  simp only [unshiftT, List.mem_map] at hrow
  obtain ⟨r, hr, rfl⟩ := hrow
  intro hnil
  simp only [List.map_eq_nil_iff] at hnil
  exact h r hr hnil

/-- The down-shift preserves `StrictBelow`: lengths are untouched by a `map`, and on positive
entries `(· - 1)` is strictly monotone. -/
theorem unshiftT_strictBelow {u l : List ℕ} (h : StrictBelow u l) (hu : ∀ a ∈ u, 1 ≤ a) :
    StrictBelow (u.map (· - 1)) (l.map (· - 1)) := by
  obtain ⟨hlen, hlt⟩ := h
  refine ⟨by simpa using hlen, fun j hj => ?_⟩
  simp only [List.length_map] at hj
  rw [getD_map_pred, getD_map_pred]
  have h1 := hlt j hj
  have h2 : 1 ≤ u.getD j 0 := hu _ (getD_mem (by omega))
  omega

theorem unshiftT_colStrict {Q : List (List ℕ)} (hc : ColStrict Q)
    (hpos : ∀ a ∈ Q.flatten, 1 ≤ a) : ColStrict (unshiftT Q) := by
  rw [ColStrict, List.isChain_iff_getElem]
  intro i hi
  simp only [unshiftT, List.length_map] at hi
  simp only [unshiftT, List.getElem_map]
  refine unshiftT_strictBelow ?_ (fun a ha =>
    hpos a (List.mem_flatten.mpr ⟨Q[i], List.getElem_mem (by omega), ha⟩))
  have h := colStrict_adjacent hc (i := i) hi
  rwa [getD_row_eq (by omega), getD_row_eq hi] at h

theorem unshiftT_rows_strict {Q : List (List ℕ)} (hs : ∀ row ∈ Q, row.Sorted (· < ·))
    (hpos : ∀ a ∈ Q.flatten, 1 ≤ a) : ∀ row ∈ unshiftT Q, row.Sorted (· < ·) := by
  intro row hrow
  simp only [unshiftT, List.mem_map] at hrow
  obtain ⟨r, hr, rfl⟩ := hrow
  rw [List.Sorted, List.pairwise_map]
  refine (hs r hr).imp_of_mem (fun {a b} ha _ hab => ?_)
  have := hpos a (List.mem_flatten.mpr ⟨r, hr, ha⟩)
  omega

theorem unshiftT_nodup {Q : List (List ℕ)} (hnd : Q.flatten.Nodup)
    (hpos : ∀ a ∈ Q.flatten, 1 ≤ a) : (unshiftT Q).flatten.Nodup := by
  rw [unshiftT_flatten]
  refine hnd.map_on (fun x hx y hy hxy => ?_)
  have := hpos x hx
  have := hpos y hy
  omega

/-- **A standard Young tableau as a recording tableau** — entries shifted into the `0`-based
timestamps `insertWordRec` counts in. -/
def toRecordingTableau (S : QOU.Mathlib.StandardYoungTableau μ) : List (List ℕ) :=
  unshiftT (toListTableau S)

@[simp] theorem tableauShape_toRecordingTableau (S : QOU.Mathlib.StandardYoungTableau μ) :
    tableauShape (toRecordingTableau S) = μ.rowLens := by
  rw [toRecordingTableau, tableauShape_unshiftT, tableauShape_toListTableau]

theorem colStrict_toRecordingTableau (S : QOU.Mathlib.StandardYoungTableau μ) :
    ColStrict (toRecordingTableau S) :=
  unshiftT_colStrict (colStrict_toListTableau S) (pos_of_mem_flatten_toListTableau S)

theorem rows_strict_toRecordingTableau (S : QOU.Mathlib.StandardYoungTableau μ) :
    ∀ row ∈ toRecordingTableau S, row.Sorted (· < ·) :=
  unshiftT_rows_strict (rows_strict_toListTableau S) (pos_of_mem_flatten_toListTableau S)

theorem nodup_flatten_toRecordingTableau (S : QOU.Mathlib.StandardYoungTableau μ) :
    (toRecordingTableau S).flatten.Nodup :=
  unshiftT_nodup (nodup_flatten_toListTableau S) (pos_of_mem_flatten_toListTableau S)

theorem noEmptyRows_toRecordingTableau (S : QOU.Mathlib.StandardYoungTableau μ) :
    NoEmptyRows (toRecordingTableau S) :=
  unshiftT_noEmptyRows (noEmptyRows_toListTableau S)

/-- **The content is `{0, …, |μ|-1}`** — both halves of the horizon condition brick 32 takes. -/
theorem mem_flatten_toRecordingTableau (S : QOU.Mathlib.StandardYoungTableau μ) {a : ℕ} :
    a ∈ (toRecordingTableau S).flatten ↔ a < μ.cells.card := by
  rw [toRecordingTableau, unshiftT_flatten, List.mem_map]
  constructor
  · rintro ⟨b, hb, rfl⟩
    have := (mem_flatten_toListTableau_iff_Icc S).mp hb
    omega
  · intro ha
    exact ⟨a + 1, (mem_flatten_toListTableau_iff_Icc S).mpr ⟨by omega, by omega⟩, by omega⟩

end QOU.Mathlib.Schensted
