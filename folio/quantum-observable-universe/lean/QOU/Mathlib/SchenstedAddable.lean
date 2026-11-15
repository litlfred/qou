import QOU.Mathlib.SchenstedShapeRun
import QOU.Mathlib.SchenstedTableau

/-!
# QOU.Mathlib.SchenstedAddable — addable-cell sequences peel back as corners (brick 20)

Brick 19 reduced the `P`-side run condition to `ShapeCornersAlong`, a statement about shapes alone.
What remains for surjectivity is to produce that condition from a standard recording tableau. This
file does the half of it that needs no tableau at all.

A standard tableau is the same data as a sequence of **addable** cells: entry `0` goes somewhere
addable in the empty shape, entry `1` somewhere addable in what that leaves, and so on. Peeled back
in reverse, such a sequence is exactly a corner sequence:

> **`shapeCornersAlong_addCellSteps`** — if `is` adds cells addably to `l`, then
> `ShapeCornersAlong (addCellSteps l is) is`, and peeling those corners returns `l`.

Everything here is on `List ℕ` shapes — no tableau, no `Q`, no insertion. That is the point: it
isolates the combinatorial content, leaving brick 21 with only the bridge "a standard `Q` gives an
addable sequence".

## The three single-step facts

* `youngShape_addCell` — adding an addable cell keeps the shape weakly decreasing and positive;
* `isCorner_addCell` — the added cell is a corner of the result. This is the shape-level mirror of
  brick 15's `insert_isCorner`, which said the same for Schensted insertion, and it has the same
  one-line reason: the row below was already bounded by the *old* length.
* `removeCorner_addCell` — and peeling it returns the shape you started from.

The third is what makes the run-level statement an exact inverse rather than merely a corner
condition, and it is why `removeCornerSteps … = l` falls out of the same induction.

## Scope

Shapes only. Producing an `AddableAlong` sequence from a standard recording tableau is brick 21;
nothing here claims it, nothing here claims `rskPair` is bijective, and `RSKBurnsideHolds` for
general `n` stays open (proved for `n ≤ 12` by an unrelated route,
`PartitionsOfBridge.rskBurnsideHolds_le12`, with no RSK correspondence in it).

Pure combinatorics on `ℕ`; nothing archimedean.

**Scope note superseded (2026-08-23).** The scope paragraph above records the state of the arc when
this brick landed. `RSKBurnsideHolds` is now proved for **every** `n`
(`QOU.Mathlib.rskBurnsideHolds`, brick 42), and `SnIsotypicSpechtSplit` is inhabited, so any
statement here that they "remain open" or hold "only for `n ≤ 12`" describes history rather than the
corpus. The per-brick scope is otherwise unchanged and still accurate.

-/

namespace QOU.Mathlib.Schensted

open QOU.Mathlib.SYTEnum (removeCorner)

/-- Reading past the end of a shape gives `0`. -/
theorem getD_past {l : List ℕ} {i : ℕ} (h : l.length ≤ i) : l.getD i 0 = 0 := by
  rw [List.getD_eq_getElem?_getD, List.getElem?_eq_none h, Option.getD_none]

/-- A **Young shape**: row lengths weakly decreasing and all positive. -/
def YoungShape (l : List ℕ) : Prop := l.Sorted (· ≥ ·) ∧ ∀ a ∈ l, 0 < a

/-- Row lengths do not increase, read with `getD` so out-of-range indices behave (both sides `0`). -/
theorem getD_succ_le_of_sorted : ∀ (l : List ℕ), l.Sorted (· ≥ ·) → ∀ (i : ℕ),
    l.getD (i + 1) 0 ≤ l.getD i 0
  | [], _, _ => by simp
  | a :: t, h, 0 => by
      rw [List.sorted_cons] at h
      simp only [List.getD_cons_succ, List.getD_cons_zero]
      cases t with
      | nil => simp
      | cons b rest =>
          simp only [List.getD_cons_zero]
          exact h.1 b (List.mem_cons_self ..)
  | a :: t, h, i + 1 => by
      rw [List.sorted_cons] at h
      simp only [List.getD_cons_succ]
      exact getD_succ_le_of_sorted t h.2 i

/-- **Add a cell to row `i`.** In range this lengthens row `i`; one past the end it starts a new row
of length one. -/
def addCell (l : List ℕ) (i : ℕ) : List ℕ :=
  if i < l.length then l.set i (l.getD i 0 + 1) else l ++ [1]

/-- Row `i` is **addable**: in range or exactly one past the end, and strictly shorter than the row
above it (vacuous at the top row). -/
def IsAddable (l : List ℕ) (i : ℕ) : Prop :=
  i ≤ l.length ∧ (i = 0 ∨ l.getD i 0 < l.getD (i - 1) 0)

/-- The added position is in range afterwards. -/
theorem lt_length_addCell (l : List ℕ) {i : ℕ} (hi : i ≤ l.length) : i < (addCell l i).length := by
  rw [addCell]
  by_cases h : i < l.length
  · rw [if_pos h]; simpa using h
  · have heq : i = l.length := by omega
    subst heq
    rw [if_neg h]; simp

/-- The entry at the added position goes up by one. -/
theorem getD_addCell_self (l : List ℕ) {i : ℕ} (hi : i ≤ l.length) :
    (addCell l i).getD i 0 = l.getD i 0 + 1 := by
  rw [addCell]
  by_cases h : i < l.length
  · rw [if_pos h, getD_set_self h]
  · have heq : i = l.length := by omega
    subst heq
    rw [if_neg h, getD_append_end, getD_past (le_refl _)]

/-- Every other position is untouched. -/
theorem getD_addCell_ne (l : List ℕ) {i j : ℕ} (hj : j ≤ l.length) (hij : i ≠ j) :
    (addCell l j).getD i 0 = l.getD i 0 := by
  rw [addCell]
  by_cases h : j < l.length
  · rw [if_pos h, getD_set_ne (fun hc => hij hc.symm)]
  · have heq : j = l.length := by omega
    subst heq
    rw [if_neg h]
    by_cases hi : i < l.length
    · exact getD_append_lt hi
    · rw [getD_past (by simp; omega), getD_past (by omega)]

/-- A shape is weakly decreasing as soon as each adjacent step is. The positional form is what the
`addCell` case analysis produces, so this is the bridge back to `List.Sorted`. -/
theorem sorted_of_getD_step : ∀ (l : List ℕ), (∀ m, l.getD (m + 1) 0 ≤ l.getD m 0) →
    l.Sorted (· ≥ ·)
  | [], _ => List.sorted_nil
  | a :: t, h => by
      have ht : t.Sorted (· ≥ ·) :=
        sorted_of_getD_step t (fun m => by have := h (m + 1); simpa using this)
      rw [List.sorted_cons]
      refine ⟨fun b hb => ?_, ht⟩
      cases t with
      | nil => simp at hb
      | cons c rest =>
          have hca : c ≤ a := by have := h 0; simpa using this
          rw [List.sorted_cons] at ht
          rcases List.mem_cons.mp hb with rfl | hb'
          · exact hca
          · exact le_trans (ht.1 b hb') hca

/-- Adding an addable cell keeps the shape a Young shape. -/
theorem youngShape_addCell {l : List ℕ} (hy : YoungShape l) {i : ℕ} (ha : IsAddable l i) :
    YoungShape (addCell l i) := by
  obtain ⟨hi, hab⟩ := ha
  obtain ⟨hsort, hpos⟩ := hy
  refine ⟨sorted_of_getD_step _ (fun m => ?_), fun a hmem => ?_⟩
  · -- three positions matter: the added one, the one just above it, and everything else
    by_cases hm : m = i
    · subst hm
      rw [getD_addCell_self l hi, getD_addCell_ne l hi (by omega)]
      have := getD_succ_le_of_sorted l hsort m
      omega
    · by_cases hm1 : m + 1 = i
      · -- the position just above the added one: this is where addability is spent
        have h1 : (addCell l i).getD (m + 1) 0 = l.getD i 0 + 1 := by
          rw [hm1]; exact getD_addCell_self l hi
        have h2 : (addCell l i).getD m 0 = l.getD m 0 := getD_addCell_ne l hi hm
        rw [h1, h2]
        rcases hab with h0 | hlt
        · omega
        · have hmi : i - 1 = m := by omega
          rw [hmi] at hlt
          omega
      · rw [getD_addCell_ne l hi hm1, getD_addCell_ne l hi hm]
        exact getD_succ_le_of_sorted l hsort m
  · rw [addCell] at hmem
    by_cases h : i < l.length
    · rw [if_pos h] at hmem
      rcases List.mem_or_eq_of_mem_set hmem with hm | rfl
      · exact hpos a hm
      · omega
    · rw [if_neg h] at hmem
      rcases List.mem_append.mp hmem with hm | hm
      · exact hpos a hm
      · simp only [List.mem_singleton] at hm; omega

/-- **The added cell is a corner of the result.**

The shape-level mirror of brick 15's `insert_isCorner`, with the same one-line reason: the row below
was already bounded by the row's *old* length, so after the increment it is strictly shorter. -/
theorem isCorner_addCell {l : List ℕ} (hy : YoungShape l) {i : ℕ} (ha : IsAddable l i) :
    QOU.Mathlib.SYTEnum.IsCorner (addCell l i) i := by
  obtain ⟨hi, _⟩ := ha
  refine ⟨lt_length_addCell l hi, ?_⟩
  rw [getD_addCell_self l hi, getD_addCell_ne l hi (by omega)]
  have := getD_succ_le_of_sorted l hy.1 i
  omega

/-- **Peeling the added cell returns the shape you started from.** This is what makes the run-level
statement an exact inverse rather than merely a corner condition. -/
theorem removeCorner_addCell {l : List ℕ} (hy : YoungShape l) {i : ℕ} (ha : IsAddable l i) :
    removeCorner (addCell l i) i = l := by
  obtain ⟨hi, _⟩ := ha
  rw [QOU.Mathlib.SYTEnum.removeCorner, getD_addCell_self l hi]
  simp only [Nat.add_sub_cancel]
  rw [addCell]
  by_cases h : i < l.length
  · rw [if_pos h, List.set_set, getD_eq_getElem_mem h, List.set_getElem_self]
    exact filter_ne_zero_of_pos l hy.2
  · have heq : i = l.length := by omega
    subst heq
    rw [if_neg h, getD_past (le_refl _)]
    have hset : ∀ (m : List ℕ) (a b : ℕ), (m ++ [a]).set m.length b = m ++ [b] := by
      intro m
      induction m with
      | nil => intro a b; simp
      | cons c t ih => intro a b; simp [ih]
    rw [hset, List.filter_append]
    simp [filter_ne_zero_of_pos l hy.2]

/-- Build a shape by adding the cells named by `is`, in order. -/
def addCellSteps : List ℕ → List ℕ → List ℕ
  | l, [] => l
  | l, i :: rest => addCellSteps (addCell l i) rest

@[simp] theorem addCellSteps_nil (l : List ℕ) : addCellSteps l [] = l := rfl

theorem addCellSteps_cons (l : List ℕ) (i : ℕ) (rest : List ℕ) :
    addCellSteps l (i :: rest) = addCellSteps (addCell l i) rest := rfl

/-- **Every step of `is` adds an addable cell** to the shape as it stands at that step. -/
def AddableAlong : List ℕ → List ℕ → Prop
  | _, [] => True
  | l, i :: rest => IsAddable l i ∧ AddableAlong (addCell l i) rest

@[simp] theorem addableAlong_nil (l : List ℕ) : AddableAlong l [] := trivial

theorem addableAlong_cons (l : List ℕ) (i : ℕ) (rest : List ℕ) :
    AddableAlong l (i :: rest) ↔ IsAddable l i ∧ AddableAlong (addCell l i) rest := Iff.rfl

/-- **An addable sequence peels back as corners, exactly onto where it started.**

Both halves come out of one induction: the corner at step `i` is `isCorner_addCell` applied at the
shape the *later* steps peel back to, which is what the inductive hypothesis's second half supplies.
Without that half the corner check would have nothing to stand on. -/
theorem shapeCornersAlong_addCellSteps : ∀ (is : List ℕ) (l : List ℕ),
    YoungShape l → AddableAlong l is →
    ShapeCornersAlong (addCellSteps l is) is ∧ removeCornerSteps (addCellSteps l is) is = l
  | [], l, _, _ => ⟨trivial, rfl⟩
  | i :: rest, l, hy, haa => by
      obtain ⟨hadd, haaRest⟩ := haa
      have hy' : YoungShape (addCell l i) := youngShape_addCell hy hadd
      obtain ⟨hsca, hpeel⟩ := shapeCornersAlong_addCellSteps rest (addCell l i) hy' haaRest
      rw [addCellSteps_cons]
      refine ⟨⟨hsca, ?_⟩, ?_⟩
      · rw [hpeel]
        exact isCorner_addCell hy hadd
      · rw [removeCornerSteps_cons, hpeel]
        exact removeCorner_addCell hy hadd

/-- The corner condition, on its own. -/
theorem shapeCornersAlong_of_addable {l : List ℕ} {is : List ℕ}
    (hy : YoungShape l) (haa : AddableAlong l is) :
    ShapeCornersAlong (addCellSteps l is) is :=
  (shapeCornersAlong_addCellSteps is l hy haa).1

/-- **The empty shape is a Young shape** — the starting point for a whole run. -/
@[simp] theorem youngShape_nil : YoungShape [] := ⟨List.sorted_nil, by simp⟩

/-- **Both of brick 18's hypotheses, from an addable sequence out of the empty shape.** This is the
form the recording tableau will supply: a standard `Q` is an addable sequence, and the shape it
builds is the shape of `P`. -/
theorem shapeCornersAlong_and_empty {is : List ℕ} (haa : AddableAlong [] is) :
    ShapeCornersAlong (addCellSteps [] is) is ∧ removeCornerSteps (addCellSteps [] is) is = [] :=
  shapeCornersAlong_addCellSteps is [] youngShape_nil haa

/-! ### The forward shape law

Brick 17 said the reverse cascade acts on shapes as `removeCorner`. The mirror — that Schensted
insertion acts on shapes as `addCell` — was not in the corpus, and it is what connects this file's
machinery to the insertion side. -/

/-- Adding below the top row leaves the top row alone. -/
theorem addCell_cons_succ (a : ℕ) (l : List ℕ) (j : ℕ) :
    addCell (a :: l) (j + 1) = a :: addCell l j := by
  rw [addCell, addCell]
  by_cases h : j < l.length
  · rw [if_pos (by simpa using h), if_pos h, List.set_cons_succ, List.getD_cons_succ]
  · rw [if_neg (by simpa using h), if_neg h]
    simp

/-- **Insertion acts on shapes as `addCell`** — the mirror of brick 17's `tableauShape_uninsert`. -/
theorem tableauShape_insert : ∀ (T : List (List ℕ)) (x : ℕ),
    tableauShape (insert T x) = addCell (tableauShape T) (newRowIndex T x)
  | [], x => by simp [insert, newRowIndex, addCell]
  | r :: T, x => by
      rw [insert, newRowIndex]
      cases hb : (rowInsert r x).2 with
      | none =>
          simp only [tableauShape_cons, rowInsert_length_none hb]
          rw [addCell, if_pos (by simp)]
          simp
      | some y =>
          simp only [tableauShape_cons, rowInsert_length_some hb]
          rw [addCell_cons_succ, tableauShape_insert T y]

/-- The row insertion appends to is within the shape. -/
theorem newRowIndex_le : ∀ (T : List (List ℕ)) (x : ℕ),
    newRowIndex T x ≤ (tableauShape T).length
  | [], _ => by simp [newRowIndex]
  | r :: T, x => by
      rw [newRowIndex]
      cases hb : (rowInsert r x).2 with
      | none => simp
      | some y =>
          simp only [tableauShape_cons, List.length_cons]
          have := newRowIndex_le T y
          omega

/-- **Insertion adds an addable cell.**

Not proved from the bumping-column argument directly — it is read off the fact that `insert`
preserves `ColStrict` (`insert_colStrict`, already in the corpus), whose shape is therefore weakly
decreasing. Spelling that out at the added index *is* addability. -/
theorem isAddable_newRowIndex {T : List (List ℕ)} (hc : ColStrict T) (x : ℕ) :
    IsAddable (tableauShape T) (newRowIndex T x) := by
  refine ⟨newRowIndex_le T x, ?_⟩
  rcases Nat.eq_zero_or_pos (newRowIndex T x) with h0 | hpos
  · exact Or.inl h0
  · refine Or.inr ?_
    -- the inserted tableau is column-strict, so its shape is weakly decreasing
    have hsorted : (tableauShape (insert T x)).Sorted (· ≥ ·) :=
      tableauShape_sorted (insert_colStrict hc x)
    rw [tableauShape_insert] at hsorted
    have hstep := getD_succ_le_of_sorted _ hsorted (newRowIndex T x - 1)
    have hidx : newRowIndex T x - 1 + 1 = newRowIndex T x := by omega
    rw [hidx, getD_addCell_self _ (newRowIndex_le T x),
      getD_addCell_ne _ (newRowIndex_le T x) (by omega)] at hstep
    omega

/-- **A whole insertion run is an addable sequence, and it builds the shape.** -/
theorem addableAlong_rowIndices : ∀ (w : List ℕ) (T : List (List ℕ)),
    ColStrict T →
    AddableAlong (tableauShape T) (rowIndices T w) ∧
      addCellSteps (tableauShape T) (rowIndices T w) = tableauShape (w.foldl insert T)
  | [], T, _ => ⟨trivial, rfl⟩
  | x :: rest, T, hc => by
      obtain ⟨haa, hbuild⟩ := addableAlong_rowIndices rest (insert T x) (insert_colStrict hc x)
      rw [rowIndices_cons, List.foldl_cons, addableAlong_cons, addCellSteps_cons,
        ← tableauShape_insert]
      exact ⟨⟨isAddable_newRowIndex hc x, haa⟩, hbuild⟩

/-- **The insertion-built case, closed.** Both of brick 18's hypotheses now come from brick 20's
machinery rather than from brick 19's iff — an independent route to the same conclusion, which is
what makes the two shape-level pictures agree. -/
theorem addableAlong_insertWord (w : List ℕ) : AddableAlong [] (rowIndices [] w) :=
  (addableAlong_rowIndices w [] colStrict_nil).1

theorem addCellSteps_insertWord (w : List ℕ) :
    addCellSteps [] (rowIndices [] w) = tableauShape (insertWord w) :=
  (addableAlong_rowIndices w [] colStrict_nil).2

/-! ### The shape an addable sequence builds is the count shape

The tool the recording-tableau bridge needs. `addCell` increments one entry, so after a whole run
row `i` holds exactly the cells whose position was `i` — no reference to any tableau. -/

/-- A nonzero entry is in range. -/
theorem lt_length_of_getD_pos {l : List ℕ} {i : ℕ} (h : 0 < l.getD i 0) : i < l.length := by
  by_contra hc
  rw [getD_past (by omega)] at h
  omega

/-- **Row `i` of the built shape counts the steps that landed in row `i`.** -/
theorem getD_addCellSteps : ∀ (is : List ℕ) (l : List ℕ), AddableAlong l is → ∀ (i : ℕ),
    (addCellSteps l is).getD i 0 = l.getD i 0 + is.count i
  | [], l, _, i => by simp
  | j :: rest, l, haa, i => by
      obtain ⟨hadd, haaRest⟩ := haa
      rw [addCellSteps_cons, getD_addCellSteps rest (addCell l j) haaRest i]
      by_cases h : i = j
      · subst h
        rw [getD_addCell_self l hadd.1, List.count_cons]
        simp only [beq_self_eq_true, if_true]
        omega
      · rw [getD_addCell_ne l hadd.1 h, List.count_cons]
        simp only [beq_iff_eq, Ne.symm h, if_false, Nat.add_zero]

/-- The built shape has exactly the rows that were used. -/
theorem lt_length_addCellSteps {is l : List ℕ} (haa : AddableAlong l is) {i : ℕ}
    (h : 0 < l.getD i 0 + is.count i) : i < (addCellSteps l is).length := by
  refine lt_length_of_getD_pos ?_
  rw [getD_addCellSteps is l haa i]
  exact h

/-- **The count shape, from the empty shape** — the form the bridge will use, with the starting
shape gone. -/
theorem getD_addCellSteps_nil {is : List ℕ} (haa : AddableAlong [] is) (i : ℕ) :
    (addCellSteps [] is).getD i 0 = is.count i := by
  rw [getD_addCellSteps is [] haa i]
  simp

/-! ### Appending one step

`AddableAlong` and `addCellSteps` recurse from the front, but a run indexed by timestamps grows at
the **end** — `List.range (n + 1) = List.range n ++ [n]`. These two put the recursion in the form
that induction on the horizon can use. -/

theorem addCellSteps_append_singleton : ∀ (is : List ℕ) (l : List ℕ) (j : ℕ),
    addCellSteps l (is ++ [j]) = addCell (addCellSteps l is) j
  | [], l, j => rfl
  | i :: rest, l, j => by
      rw [List.cons_append, addCellSteps_cons, addCellSteps_cons,
        addCellSteps_append_singleton rest (addCell l i) j]

theorem addableAlong_append_singleton : ∀ (is : List ℕ) (l : List ℕ) (j : ℕ),
    AddableAlong l (is ++ [j]) ↔ AddableAlong l is ∧ IsAddable (addCellSteps l is) j
  | [], l, j => by
      rw [List.nil_append, addableAlong_cons, addCellSteps_nil]
      exact ⟨fun h => ⟨trivial, h.1⟩, fun h => ⟨h.2, trivial⟩⟩
  | i :: rest, l, j => by
      rw [List.cons_append, addableAlong_cons, addableAlong_cons, addCellSteps_cons,
        addableAlong_append_singleton rest (addCell l i) j]
      tauto

end QOU.Mathlib.Schensted
