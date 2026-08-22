import QOU.Mathlib.SchenstedShapeRun

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

end QOU.Mathlib.Schensted
