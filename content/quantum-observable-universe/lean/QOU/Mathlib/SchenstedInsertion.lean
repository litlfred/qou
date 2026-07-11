import Mathlib.Data.List.Sort
import Mathlib.Data.Multiset.Basic
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Tactic.Abel

/-!
# QOU.Mathlib.SchenstedInsertion — Schensted row insertion (RSK foundation, brick 1)

The Robinson–Schensted–Knuth correspondence — whose cardinality consequence
`∑_{λ ⊢ n} #SYT(λ)² = n!` is **Identity-I axiom (i)** (stated as `RSKBurnsideHolds` in
`QOU/Mathlib/RSKBurnsideTarget.lean`) — is built on the **row-insertion** (bumping) operation.
Pinned Mathlib has no `Combinatorics.RSK` (recon 2026-06-26), so this multi-session program
formalises it brick by brick.  **Brick 1 (this file): the atomic row-insertion on a single row**,
modelled as a weakly-increasing `List ℕ`, with its two structural invariants proved sorry-free.

`rowInsert r x` inserts `x` into a weakly-increasing row `r` by the Schensted rule: replace the
**leftmost entry strictly greater than `x`** by `x` and return that bumped entry; if no such entry
exists, append `x` (no bump).  Returned as `(newRow, bumped?)`.

Proved here (sorry-free):
* `mem_rowInsert` — every entry of the new row is an old entry or `x`;
* `rowInsert_length` — the row length is unchanged (a bump) or grows by one (an append);
* `rowInsert_sorted` — **the new row stays weakly increasing** (the key invariant that makes the
  insertion tableau well-formed).

Roadmap for the remaining bricks (each a future PR): the bumping cascade across rows
(insertion tableau `P`), the recording tableau `Q`, the pair `(P, Q)` as the RSK map, its
inverse (reverse bumping), the resulting bijection `Sym n ≃ Σ_λ SYT(λ)²`, and finally the
cardinality count discharging `RSKBurnsideHolds`.  Pure combinatorics on `ℕ`; nothing archimedean.
-/

namespace QOU.Mathlib.Schensted

/-- **Schensted row insertion.** Insert `x` into a (weakly-increasing) row `r`: bump the leftmost
entry `> x`, returning `(newRow, some bumped)`; if none, append `x`, returning `(r ++ [x], none)`. -/
def rowInsert : List ℕ → ℕ → List ℕ × Option ℕ
  | [], x => ([x], none)
  | a :: r, x =>
      if x < a then (x :: r, some a)
      else (a :: (rowInsert r x).1, (rowInsert r x).2)

@[simp] theorem rowInsert_nil (x : ℕ) : rowInsert [] x = ([x], none) := rfl

theorem rowInsert_cons (a : ℕ) (r : List ℕ) (x : ℕ) :
    rowInsert (a :: r) x =
      if x < a then (x :: r, some a) else (a :: (rowInsert r x).1, (rowInsert r x).2) := rfl

/-- Every entry of the inserted row is an old entry of `r` or the inserted value `x`. -/
theorem mem_rowInsert {r : List ℕ} {x b : ℕ} (hb : b ∈ (rowInsert r x).1) : b ∈ r ∨ b = x := by
  induction r with
  | nil => simp only [rowInsert_nil, List.mem_singleton] at hb; exact Or.inr hb
  | cons a r ih =>
    rw [rowInsert_cons] at hb
    by_cases hx : x < a
    · rw [if_pos hx] at hb
      rcases List.mem_cons.mp hb with h | h
      · exact Or.inr h
      · exact Or.inl (List.mem_cons_of_mem _ h)
    · rw [if_neg hx] at hb
      rcases List.mem_cons.mp hb with h | h
      · exact Or.inl (List.mem_cons.mpr (Or.inl h))
      · rcases ih h with h' | h'
        · exact Or.inl (List.mem_cons_of_mem _ h')
        · exact Or.inr h'

/-- Row insertion either keeps the length (a bump) or increases it by one (an append). -/
theorem rowInsert_length (r : List ℕ) (x : ℕ) :
    (rowInsert r x).1.length = r.length ∨ (rowInsert r x).1.length = r.length + 1 := by
  induction r with
  | nil => simp [rowInsert]
  | cons a r ih =>
    rw [rowInsert_cons]
    by_cases hx : x < a
    · rw [if_pos hx]; exact Or.inl rfl
    · rw [if_neg hx]
      simp only [List.length_cons]
      rcases ih with h | h
      · exact Or.inl (by rw [h])
      · exact Or.inr (by rw [h])

/-- **The inserted row stays weakly increasing.**  This is the structural invariant that keeps the
RSK insertion tableau well-formed: bumping the leftmost entry `> x` by the smaller `x` preserves
sortedness, and appending `x` past a row all `≤ x` does too. -/
theorem rowInsert_sorted {r : List ℕ} (h : r.Sorted (· ≤ ·)) (x : ℕ) :
    (rowInsert r x).1.Sorted (· ≤ ·) := by
  induction r with
  | nil => simp [rowInsert]
  | cons a r ih =>
    rw [List.sorted_cons] at h
    rw [rowInsert_cons]
    by_cases hx : x < a
    · rw [if_pos hx, List.sorted_cons]
      exact ⟨fun b hb => le_of_lt (lt_of_lt_of_le hx (h.1 b hb)), h.2⟩
    · rw [if_neg hx, List.sorted_cons]
      refine ⟨fun b hb => ?_, ih h.2⟩
      rcases mem_rowInsert hb with hbr | hbx
      · exact h.1 b hbr
      · exact hbx ▸ not_lt.mp hx

/-! ## Brick 2 — the bumping cascade (insertion tableau) -/

/-- **Schensted insertion into a tableau** (a `List (List ℕ)` of rows).  Row-insert `x` into the
first row; if an entry is bumped, cascade the bumped value into the next row; if the cascade falls
off the bottom, start a new one-cell row. -/
def insert : List (List ℕ) → ℕ → List (List ℕ)
  | [], x => [[x]]
  | row :: rest, x =>
      match (rowInsert row x).2 with
      | none => (rowInsert row x).1 :: rest
      | some y => (rowInsert row x).1 :: insert rest y

/-- The insertion tableau `P(w)` of a word `w`: insert its letters left to right into the empty
tableau. -/
def insertWord (w : List ℕ) : List (List ℕ) := w.foldl insert []

/-- Every row of a tableau is weakly increasing. -/
def RowsSorted (T : List (List ℕ)) : Prop := ∀ row ∈ T, row.Sorted (· ≤ ·)

@[simp] theorem rowsSorted_nil : RowsSorted [] := by intro _ h; simp at h

/-- **The cascade preserves row-sortedness.**  Each row that changes does so by `rowInsert`, which
keeps it weakly increasing (`rowInsert_sorted`); untouched rows are unchanged.  So `insert`
maps row-sorted tableaux to row-sorted tableaux — the invariant making `insertWord w` a tableau
with weakly-increasing rows. -/
theorem insert_rowsSorted : ∀ {T : List (List ℕ)}, RowsSorted T → ∀ x, RowsSorted (insert T x)
  | [], _, x => by
      intro row hrow
      rw [insert] at hrow
      rw [List.mem_singleton] at hrow
      exact hrow ▸ List.sorted_singleton x
  | row :: rest, h, x => by
      have hrow : row.Sorted (· ≤ ·) := h row List.mem_cons_self
      have hrest : RowsSorted rest := fun r hr => h r (List.mem_cons_of_mem _ hr)
      have hrow' : (rowInsert row x).1.Sorted (· ≤ ·) := rowInsert_sorted hrow x
      rw [insert]
      cases hb : (rowInsert row x).2 with
      | none =>
        intro r hr
        rcases List.mem_cons.mp hr with h1 | h1
        · exact h1 ▸ hrow'
        · exact hrest r h1
      | some y =>
        intro r hr
        rcases List.mem_cons.mp hr with h1 | h1
        · exact h1 ▸ hrow'
        · exact insert_rowsSorted hrest y r h1

/-- `insertWord w` has weakly-increasing rows, for every word `w`. -/
theorem insertWord_rowsSorted (w : List ℕ) : RowsSorted (insertWord w) := by
  unfold insertWord
  suffices h : ∀ (T : List (List ℕ)), RowsSorted T → RowsSorted (w.foldl insert T) by
    exact h [] rowsSorted_nil
  induction w with
  | nil => intro T hT; simpa using hT
  | cons a w ih =>
    intro T hT
    rw [List.foldl_cons]
    exact ih _ (insert_rowsSorted hT a)

/-! ## Brick 3 — cell count: `|P(w)| = |w|` (each insertion adds exactly one cell) -/

/-- A no-bump row insertion (append) grows the row by one. -/
theorem rowInsert_length_none {r : List ℕ} {x : ℕ} (h : (rowInsert r x).2 = none) :
    (rowInsert r x).1.length = r.length + 1 := by
  induction r with
  | nil => simp [rowInsert]
  | cons a r ih =>
    rw [rowInsert_cons] at h ⊢
    by_cases hx : x < a
    · rw [if_pos hx] at h; simp at h
    · rw [if_neg hx] at h ⊢
      have := ih h
      simp only [List.length_cons]; omega

/-- A bumping row insertion keeps the row length fixed. -/
theorem rowInsert_length_some {r : List ℕ} {x y : ℕ} (h : (rowInsert r x).2 = some y) :
    (rowInsert r x).1.length = r.length := by
  induction r with
  | nil => simp [rowInsert] at h
  | cons a r ih =>
    rw [rowInsert_cons] at h ⊢
    by_cases hx : x < a
    · rw [if_pos hx] at h ⊢; simp
    · rw [if_neg hx] at h ⊢
      have := ih h
      simp only [List.length_cons]; omega

/-- Total number of cells of a tableau. -/
def totalCells (T : List (List ℕ)) : ℕ := (T.map List.length).sum

@[simp] theorem totalCells_nil : totalCells [] = 0 := rfl

@[simp] theorem totalCells_cons (a : List ℕ) (l : List (List ℕ)) :
    totalCells (a :: l) = a.length + totalCells l := by simp [totalCells]

/-- **Each insertion adds exactly one cell.**  A bump replaces an entry (no length change in that
row) but cascades the bumped value downward, which eventually appends one cell (or starts a new
row); a no-bump appends directly.  Either way the total grows by exactly one. -/
theorem insert_totalCells : ∀ (T : List (List ℕ)) (x : ℕ),
    totalCells (insert T x) = totalCells T + 1
  | [], x => by simp [insert]
  | row :: rest, x => by
      rw [insert]
      cases hb : (rowInsert row x).2 with
      | none => rw [totalCells_cons, totalCells_cons, rowInsert_length_none hb]; omega
      | some y =>
        rw [totalCells_cons, totalCells_cons, rowInsert_length_some hb,
            insert_totalCells rest y]; omega

/-- `|P(w)| = |w|`: the insertion tableau of a word has exactly as many cells as the word has
letters — the cell-count fact RSK's cardinality argument rests on. -/
theorem insertWord_totalCells (w : List ℕ) : totalCells (insertWord w) = w.length := by
  have key : ∀ (v : List ℕ) (T : List (List ℕ)),
      totalCells (v.foldl insert T) = totalCells T + v.length := by
    intro v
    induction v with
    | nil => intro T; simp
    | cons a v ih =>
      intro T
      rw [List.foldl_cons, ih (insert T a), insert_totalCells]
      simp only [List.length_cons]; omega
  simpa using key w []

/-! ## Brick 4 — content preservation: `P(w)` holds exactly the multiset of `w`'s letters -/

/-- The bumped value as a multiset (`∅` if no bump, `{a}` if `a` is bumped). -/
def bumpMs : Option ℕ → Multiset ℕ
  | none => 0
  | some a => {a}

/-- The multiset of entries of a tableau (sum of its rows' multisets). -/
def content : List (List ℕ) → Multiset ℕ
  | [] => 0
  | r :: T => (↑r : Multiset ℕ) + content T

@[simp] theorem content_nil : content [] = 0 := rfl

@[simp] theorem content_cons (r : List ℕ) (T : List (List ℕ)) :
    content (r :: T) = (↑r : Multiset ℕ) + content T := rfl

/-- **Row insertion conserves entries**: the new row plus the bumped value (if any) carries exactly
the old row's entries together with the inserted `x`. -/
theorem rowInsert_content (r : List ℕ) (x : ℕ) :
    (↑(rowInsert r x).1 : Multiset ℕ) + bumpMs (rowInsert r x).2 = (↑r : Multiset ℕ) + {x} := by
  induction r with
  | nil => simp [rowInsert, bumpMs]
  | cons a r ih =>
    rw [rowInsert_cons]
    by_cases hx : x < a
    · rw [if_pos hx]
      simp only [bumpMs, ← Multiset.cons_coe, ← Multiset.singleton_add]
      abel
    · rw [if_neg hx]
      simp only [← Multiset.cons_coe, ← Multiset.singleton_add]
      rw [add_assoc, ih]
      abel

/-- **The insertion cascade conserves entries**: `insert T x` holds exactly the entries of `T`
together with `x`.  (The bumped value is never lost — it cascades down until appended.) -/
theorem insert_content : ∀ (T : List (List ℕ)) (x : ℕ),
    content (insert T x) = content T + {x}
  | [], x => by simp [insert, content]
  | row :: rest, x => by
      rw [insert]
      cases hb : (rowInsert row x).2 with
      | none =>
        have hc := rowInsert_content row x
        rw [hb, bumpMs, add_zero] at hc
        rw [content_cons, content_cons, hc]; abel
      | some y =>
        have hc := rowInsert_content row x
        rw [hb, bumpMs] at hc
        rw [content_cons, content_cons, insert_content rest y]
        have h2 : (↑(rowInsert row x).1 : Multiset ℕ) + (content rest + {y})
                = ((↑(rowInsert row x).1 : Multiset ℕ) + {y}) + content rest := by abel
        rw [h2, hc]; abel

/-- `content (P(w)) = ↑w`: the insertion tableau of a word holds exactly the multiset of its
letters — the content-preservation fact RSK's bijection content-matching rests on. -/
theorem insertWord_content (w : List ℕ) : content (insertWord w) = (↑w : Multiset ℕ) := by
  have key : ∀ (v : List ℕ) (T : List (List ℕ)),
      content (v.foldl insert T) = content T + (↑v : Multiset ℕ) := by
    intro v
    induction v with
    | nil => intro T; simp
    | cons a v ih =>
      intro T
      rw [List.foldl_cons, ih (insert T a), insert_content]
      simp only [← Multiset.cons_coe, ← Multiset.singleton_add]; abel
  simpa using key w []

/-! ## Brick 5 — bumping monotonicity (toward column-strictness)

The column-strictness of the insertion tableau (columns strictly increasing —
the invariant making `P(w)` a genuine semistandard tableau) rests on the
**bumping lemma**.  Its atomic seed is proved here: a `rowInsert` bump ejects
an entry *strictly greater* than the inserted value.  So the value cascading
into the next row is always `> x`, which is what forces each new cell to sit
strictly below a smaller entry.  (The full cascade column-strictness is the
next sub-brick.) -/

/-- **The bumped entry is strictly greater than the inserted value.**  `rowInsert`
bumps the *leftmost entry `> x`*, so whenever it returns `some y`, `x < y`. -/
theorem rowInsert_bumped_gt {r : List ℕ} {x y : ℕ}
    (h : (rowInsert r x).2 = some y) : x < y := by
  induction r with
  | nil => simp [rowInsert] at h
  | cons a r ih =>
    rw [rowInsert_cons] at h
    by_cases hx : x < a
    · rw [if_pos hx] at h
      simp only [Option.some.injEq] at h
      exact h ▸ hx
    · rw [if_neg hx] at h
      exact ih h

/-- **The bumped entry is a genuine entry of the original row.**  Together with
`rowInsert_bumped_gt`, the value cascading downward is an old entry `> x`. -/
theorem rowInsert_bumped_mem {r : List ℕ} {x y : ℕ}
    (h : (rowInsert r x).2 = some y) : y ∈ r := by
  induction r with
  | nil => simp [rowInsert] at h
  | cons a r ih =>
    rw [rowInsert_cons] at h
    by_cases hx : x < a
    · rw [if_pos hx] at h
      simp only [Option.some.injEq] at h
      exact h ▸ List.mem_cons_self
    · rw [if_neg hx] at h
      exact List.mem_cons_of_mem a (ih h)

/-- **No bump ⟺ every entry is `≤ x`.**  When `rowInsert` appends (no bump), the
inserted `x` is `≥` every entry of the row — so the append lands `x` as the new
row-maximum, the base case of the column-strictness cascade. -/
theorem rowInsert_none_forall_le {r : List ℕ} {x : ℕ}
    (h : (rowInsert r x).2 = none) : ∀ a ∈ r, a ≤ x := by
  induction r with
  | nil => intro a ha; simp at ha
  | cons b r ih =>
    rw [rowInsert_cons] at h
    by_cases hx : x < b
    · rw [if_pos hx] at h; simp at h
    · rw [if_neg hx] at h
      intro a ha
      rcases List.mem_cons.mp ha with rfl | ha'
      · exact not_lt.mp hx
      · exact ih h a ha'

/-- Row insertion changes the length by `0` (a bump) or `+1` (an append) — never
more.  A structural bound the later Young-diagram *shape* reasoning consumes. -/
theorem rowInsert_length_le {r : List ℕ} {x : ℕ} :
    r.length ≤ (rowInsert r x).1.length ∧ (rowInsert r x).1.length ≤ r.length + 1 := by
  cases h : (rowInsert r x).2 with
  | none => rw [rowInsert_length_none h]; omega
  | some y => rw [rowInsert_length_some h]; omega

/-- An inserted row is never empty (it always contains at least `x`). -/
theorem rowInsert_ne_nil {r : List ℕ} {x : ℕ} : (rowInsert r x).1 ≠ [] := by
  cases r with
  | nil => simp [rowInsert]
  | cons a r =>
    rw [rowInsert_cons]
    by_cases hx : x < a <;> simp [hx]

/-! ### Positional characterization of a bump (column-reasoning foundation)

To reason about *columns*, the bump must be located: a `rowInsert` bump replaces
the **leftmost entry `> x`** — at `List.findIdx (x < ·)` — by `x`.  These two
lemmas pin that index (`< row length`) and the `List.set` form of the new row;
they are the positional bridge Brick 5's column-strictness argument indexes
against. -/

/-- **Positional characterization of a bump.**  When `rowInsert` bumps, the new
row is the old row with its leftmost entry `> x` (at `findIdx`) replaced by `x`. -/
theorem rowInsert_bump_eq_set {r : List ℕ} {x y : ℕ}
    (h : (rowInsert r x).2 = some y) :
    (rowInsert r x).1 = r.set (r.findIdx (x < ·)) x := by
  induction r with
  | nil => simp [rowInsert] at h
  | cons a r ih =>
    rw [rowInsert_cons] at h ⊢
    by_cases hx : x < a
    · rw [if_pos hx] at h ⊢
      have hd : decide (x < a) = true := by simp [hx]
      rw [List.findIdx_cons, hd, cond_true, List.set_cons_zero]
    · rw [if_neg hx] at h ⊢
      have hd : decide (x < a) = false := by simp [hx]
      rw [List.findIdx_cons, hd, cond_false, List.set_cons_succ, ih h]

/-- **The bump position is valid** (`< row length`): there is an entry `> x`
(the bumped one, `∈ r` and `> x`), so `findIdx` lands inside the row. -/
theorem rowInsert_findIdx_lt {r : List ℕ} {x y : ℕ}
    (h : (rowInsert r x).2 = some y) : r.findIdx (x < ·) < r.length :=
  List.findIdx_lt_length_of_exists
    ⟨y, rowInsert_bumped_mem h, by simpa using rowInsert_bumped_gt h⟩

/-- **The bumped value is exactly the old entry at the bump index.**  Completing
the positional picture: a bump reads off `r[findIdx]` (as `y`) and writes `x`
there.  Stated with `getElem?` to avoid threading the `< length` proof. -/
theorem rowInsert_bump_getElem? {r : List ℕ} {x y : ℕ}
    (h : (rowInsert r x).2 = some y) :
    r[r.findIdx (x < ·)]? = some y := by
  induction r with
  | nil => simp [rowInsert] at h
  | cons a r ih =>
    rw [rowInsert_cons] at h
    by_cases hx : x < a
    · rw [if_pos hx] at h
      simp only [Option.some.injEq] at h
      have hd : decide (x < a) = true := by simp [hx]
      rw [List.findIdx_cons, hd, cond_true, List.getElem?_cons_zero, h]
    · rw [if_neg hx] at h
      have hd : decide (x < a) = false := by simp [hx]
      rw [List.findIdx_cons, hd, cond_false, List.getElem?_cons_succ]
      exact ih h

/-! ### Bump-column monotonicity (the bumping-lemma heart)

The insertion tableau is column-strict because **bump columns weakly decrease
down the rows**: if `x` bumps `y` from an upper row, `y` re-inserts into the
lower row at a column no further right.  The proof rests on a general
`List.findIdx` fact — if the predicate already holds at position `c`, the first
witness is `≤ c` — plus column-strictness of the input (`upper[j] < lower[j]`). -/

/-- **`findIdx` upper bound.**  If the predicate holds at index `c`, the first
index where it holds is `≤ c`.  (General `List` fact; the monotonicity engine.) -/
theorem findIdx_le_of_getElem {α : Type*} (p : α → Bool) (l : List α) :
    ∀ (c : ℕ) (hc : c < l.length), p l[c] = true → l.findIdx p ≤ c := by
  induction l with
  | nil => intro c hc _; simp at hc
  | cons a l ih =>
    intro c hc hp
    rw [List.findIdx_cons]
    by_cases hpa : p a = true
    · rw [hpa]; simp
    · rw [Bool.not_eq_true] at hpa
      rw [hpa, cond_false]
      cases c with
      | zero => simp only [List.getElem_cons_zero] at hp; rw [hp] at hpa; simp at hpa
      | succ c =>
        simp only [List.getElem_cons_succ] at hp
        have hc' : c < l.length := by simpa using hc
        have := ih c hc' hp
        omega

/-- **Entries strictly before the bump index are `≤ x`.**  `findIdx` is the
*leftmost* entry `> x`, so everything to its left is `≤ x`.  This is what makes
the new-bottom-row cell (column `0`) sit strictly below a smaller entry when the
bump came from a later column. -/
theorem getD_le_of_lt_findIdx (x : ℕ) (l : List ℕ) (j : ℕ)
    (hj : j < l.findIdx (x < ·)) : l.getD j 0 ≤ x := by
  induction l generalizing j with
  | nil => rw [List.findIdx_nil] at hj; omega
  | cons a l ih =>
    rw [List.findIdx_cons] at hj
    by_cases hx : x < a
    · rw [show decide (x < a) = true from by simp [hx], cond_true] at hj; omega
    · rw [show decide (x < a) = false from by simp [hx], cond_false] at hj
      cases j with
      | zero => simpa using le_of_not_gt hx
      | succ j => rw [List.getD_cons_succ]; exact ih j (by omega)

/-- **Bump-column monotonicity** — the bumping lemma's heart.  If the value `y`
bumped from `upper` (at `upper.findIdx (x < ·)`) sits at every column strictly
below a larger entry of `lower` (column-strictness, `upper[j] < lower[j]`), then
`y` re-inserts into `lower` at a column no further right:
`lower.findIdx (y < ·) ≤ upper.findIdx (x < ·)`.  This is exactly why columns of
the insertion tableau stay strictly increasing. -/
theorem bump_findIdx_mono (upper lower : List ℕ) (x y : ℕ)
    (hy : upper[upper.findIdx (x < ·)]? = some y)
    (hcol : ∀ (j : ℕ) (_hj : j < lower.length) (_hu : j < upper.length),
              upper[j] < lower[j]) :
    lower.findIdx (y < ·) ≤ upper.findIdx (x < ·) := by
  set c := upper.findIdx (x < ·) with hc
  by_cases hcl : c < lower.length
  · rw [List.getElem?_eq_some_iff] at hy
    obtain ⟨hcu, hyc⟩ := hy
    have hlt : y < lower[c] := hyc ▸ hcol c hcl hcu
    exact findIdx_le_of_getElem _ lower c hcl (by simpa using hlt)
  · push_neg at hcl
    exact le_trans List.findIdx_le_length hcl

/-! ### Column-strictness invariant

`StrictBelow upper lower` — `lower` is no longer than `upper` and each of its
entries strictly exceeds the one directly above (`getD _ 0` reads in-range
entries, dodging dependent-index proofs).  `ColStrict T` — consecutive rows of
the tableau satisfy `StrictBelow`, i.e. columns strictly increase downward.
Two entry-level preservation lemmas (append a cell to the upper row; lower an
upper entry) feed the cascade preservation. -/

/-- `lower` sits strictly below `upper`: no longer, each entry strictly exceeds
the one directly above. -/
def StrictBelow (upper lower : List ℕ) : Prop :=
  lower.length ≤ upper.length ∧ ∀ j < lower.length, upper.getD j 0 < lower.getD j 0

/-- A tableau has strictly-increasing columns iff consecutive rows are
`StrictBelow`. -/
def ColStrict (T : List (List ℕ)) : Prop := T.IsChain StrictBelow

@[simp] theorem colStrict_nil : ColStrict [] := List.isChain_nil

@[simp] theorem colStrict_singleton (r : List ℕ) : ColStrict [r] := by
  simp [ColStrict]

/-- **Appending a cell to the upper row preserves `StrictBelow`**: the new column
sits beyond `lower`, so existing comparisons are untouched.  (The no-bump /
append case of the cascade.) -/
theorem strictBelow_append_upper {upper lower : List ℕ} {x : ℕ}
    (h : StrictBelow upper lower) : StrictBelow (upper ++ [x]) lower := by
  obtain ⟨hlen, hlt⟩ := h
  refine ⟨by simp; omega, fun j hj => ?_⟩
  have hju : j < upper.length := lt_of_lt_of_le hj hlen
  have heq : (upper ++ [x]).getD j 0 = upper.getD j 0 := by
    simp [List.getD_eq_getElem?_getD, List.getElem?_append_left hju]
  rw [heq]; exact hlt j hj

/-- **Lowering an upper entry preserves `StrictBelow`**: replacing `upper[k]` by
a strictly smaller `x` keeps every column comparison (the changed column only
gets smaller above).  This is the bump case's effect on the upper row
(`rowInsert` writes `x < y` at the bump index). -/
theorem strictBelow_set_smaller {upper lower : List ℕ} {k x : ℕ}
    (h : StrictBelow upper lower) (hk : x < upper.getD k 0) :
    StrictBelow (upper.set k x) lower := by
  obtain ⟨hlen, hlt⟩ := h
  refine ⟨by simpa using hlen, fun j hj => ?_⟩
  by_cases hjk : k = j
  · subst hjk
    have hju : k < upper.length := lt_of_lt_of_le hj hlen
    have hset : (upper.set k x).getD k 0 = x := by
      simp [List.getD_eq_getElem?_getD, hju]
    rw [hset]; exact lt_trans hk (hlt k hj)
  · have hset : (upper.set k x).getD j 0 = upper.getD j 0 := by
      simp [List.getD_eq_getElem?_getD, List.getElem?_set_ne hjk]
    rw [hset]; exact hlt j hj

/-! ### Cascade column-strictness — `insert_colStrict` (the bumping lemma)

The four building blocks above (`bump_findIdx_mono`, `getD_le_of_lt_findIdx`,
`strictBelow_append_upper`, `strictBelow_set_smaller`) assemble into the
**bumping lemma**: one Schensted insertion step preserves `ColStrict`.  The
crux is `strictBelow_bump_step` — when `x` bumps `y` from an upper row, the
ejected `y` re-inserts into the lower row at a column no further right, so
every `StrictBelow` column comparison survives.  Iterating down the cascade
gives `insert_colStrict`, and folding over a word gives `insertWord_colStrict`:
the insertion tableau `P(w)` has strictly-increasing columns.  Together with
`insertWord_rowsSorted` this makes `P(w)` a genuine semistandard tableau — the
shape-validity Brick 6+ (recording tableau, RSK bijection) builds on. -/

/-- `getD` at the set index reads the written value (index in range). -/
theorem getD_set_self {l : List ℕ} {k x : ℕ} (hk : k < l.length) :
    (l.set k x).getD k 0 = x := by
  simp [List.getD_eq_getElem?_getD, hk]

/-- `getD` away from the set index is unchanged. -/
theorem getD_set_ne {l : List ℕ} {k j x : ℕ} (hkj : k ≠ j) :
    (l.set k x).getD j 0 = l.getD j 0 := by
  simp [List.getD_eq_getElem?_getD, List.getElem?_set_ne hkj]

/-- In-range `getD` equals the plain indexed entry. -/
theorem getD_eq_getElem_mem {l : List ℕ} {j : ℕ} (hj : j < l.length) :
    l.getD j 0 = l[j] := by
  rw [List.getD_eq_getElem?_getD, List.getElem?_eq_getElem hj]; rfl

/-- A no-bump row insertion appends: the new row is exactly `r ++ [x]`. -/
theorem rowInsert_none_eq_append {r : List ℕ} {x : ℕ}
    (h : (rowInsert r x).2 = none) : (rowInsert r x).1 = r ++ [x] := by
  induction r with
  | nil => simp [rowInsert]
  | cons a r ih =>
    rw [rowInsert_cons] at h ⊢
    by_cases hx : x < a
    · rw [if_pos hx] at h; simp at h
    · rw [if_neg hx] at h ⊢
      rw [ih h]; rfl

/-- The insertion cascade never yields the empty tableau (it always adds a cell). -/
theorem insert_ne_nil (T : List (List ℕ)) (x : ℕ) : insert T x ≠ [] := by
  cases T with
  | nil => simp [insert]
  | cons row rest => rw [insert]; cases (rowInsert row x).2 <;> simp

/-- The head row of `insert rest y` is the head row of `rest` after `rowInsert`
    with `y` (reading the empty row when `rest = []`). -/
theorem insert_headD_eq (rest : List (List ℕ)) (y : ℕ) :
    (insert rest y).headD [] = (rowInsert (rest.headD []) y).1 := by
  cases rest with
  | nil => simp [insert]
  | cons row2 rest2 => rw [insert]; cases (rowInsert row2 y).2 <;> simp

/-- **The bumping lemma (single step).**  If `lower` sits strictly below `row`
    (`StrictBelow`) and `rowInsert row x` bumps `y`, then after `y` re-inserts
    into `lower` the new upper row still sits strictly below the new lower row.
    This is the structural heart of RSK column-strictness: the ejected `y > x`
    lands in `lower` at a column no further right than where `x` landed in
    `row`, so every column comparison is preserved. -/
theorem strictBelow_bump_step {row lower : List ℕ} {x y : ℕ}
    (hsb : StrictBelow row lower) (hb : (rowInsert row x).2 = some y) :
    StrictBelow (rowInsert row x).1 (rowInsert lower y).1 := by
  obtain ⟨hlen, hlt⟩ := hsb
  set k := row.findIdx (x < ·)
  have hk : k < row.length := rowInsert_findIdx_lt hb
  have hxy : x < y := rowInsert_bumped_gt hb
  have hup : (rowInsert row x).1 = row.set k x := rowInsert_bump_eq_set hb
  have hrowk : row.getD k 0 = y := by
    rw [List.getD_eq_getElem?_getD, rowInsert_bump_getElem? hb]; rfl
  have hxk : x < row.getD k 0 := hrowk ▸ hxy
  have hsb2 : StrictBelow (row.set k x) lower := strictBelow_set_smaller ⟨hlen, hlt⟩ hxk
  obtain ⟨_, hlt2⟩ := hsb2
  rw [hup]
  cases hbl : (rowInsert lower y).2 with
  | none =>
    have hle : ∀ a ∈ lower, a ≤ y := rowInsert_none_forall_le hbl
    have hrowlt : ∀ j, j < lower.length → row.getD j 0 < y := by
      intro j hj
      have h1 := hlt j hj
      rw [getD_eq_getElem_mem hj] at h1
      exact lt_of_lt_of_le h1 (hle _ (List.getElem_mem hj))
    have hlowk : lower.length ≤ k := by
      by_contra hcon
      push_neg at hcon
      have := hrowlt k hcon
      rw [hrowk] at this; exact lt_irrefl y this
    rw [rowInsert_none_eq_append hbl]
    refine ⟨?_, fun j hj => ?_⟩
    · simp only [List.length_append, List.length_cons, List.length_nil,
        List.length_set]
      omega
    · rw [List.length_append, List.length_cons, List.length_nil] at hj
      by_cases hjl : j < lower.length
      · have heq : (lower ++ [y]).getD j 0 = lower.getD j 0 := by
          rw [List.getD_eq_getElem?_getD, List.getElem?_append_left hjl,
            ← List.getD_eq_getElem?_getD]
        rw [heq]; exact hlt2 j hjl
      · have hjeq : j = lower.length := by omega
        subst hjeq
        have heqy : (lower ++ [y]).getD lower.length 0 = y := by
          rw [List.getD_eq_getElem?_getD, List.getElem?_append_right (Nat.le_refl _)]
          simp
        rw [heqy]
        rcases lt_or_eq_of_le hlowk with hlk | hek
        · rw [getD_set_ne (by omega : k ≠ lower.length)]
          have hle_x : row.getD lower.length 0 ≤ x :=
            getD_le_of_lt_findIdx x row lower.length hlk
          omega
        · rw [hek, getD_set_self hk]; exact hxy
  | some z =>
    have hk' : lower.findIdx (y < ·) < lower.length := rowInsert_findIdx_lt hbl
    set k' := lower.findIdx (y < ·)
    have hmono : k' ≤ k := by
      apply bump_findIdx_mono row lower x y (rowInsert_bump_getElem? hb)
      intro j hjl hju
      have h1 := hlt j hjl
      rw [getD_eq_getElem_mem hjl, getD_eq_getElem_mem hju] at h1
      exact h1
    rw [rowInsert_bump_eq_set hbl]
    refine ⟨?_, fun j hj => ?_⟩
    · simp only [List.length_set]; exact hlen
    · rw [List.length_set] at hj
      by_cases hjk' : j = k'
      · subst hjk'
        rw [getD_set_self hk']
        rcases eq_or_lt_of_le hmono with hek | hlk
        · rw [hek, getD_set_self hk]; exact hxy
        · rw [getD_set_ne (by omega : k ≠ k')]
          have hle_x : row.getD k' 0 ≤ x := getD_le_of_lt_findIdx x row k' hlk
          omega
      · rw [getD_set_ne (fun h => hjk' h.symm)]
        exact hlt2 j hj

/-- `ColStrict` is inherited by the tail of the tableau. -/
theorem colStrict_tail {r : List ℕ} {T : List (List ℕ)} (h : ColStrict (r :: T)) :
    ColStrict T := by
  cases T with
  | nil => exact colStrict_nil
  | cons r2 T2 => rw [ColStrict, List.isChain_cons_cons] at h; exact h.2

/-- **The insertion cascade preserves column-strictness.**  `insert T x` keeps
    a column-strict tableau column-strict: the no-bump case appends a cell past
    the lower row (`strictBelow_append_upper`); the bump case lowers the upper
    entry and cascades the ejected value down, preserving every column
    comparison by `strictBelow_bump_step`.  This is the last structural
    invariant needed to make `P(w)` a semistandard tableau. -/
theorem insert_colStrict : ∀ {T : List (List ℕ)}, ColStrict T → ∀ x,
    ColStrict (insert T x)
  | [], _, x => by simp only [insert]; exact colStrict_singleton [x]
  | row :: rest, h, x => by
      rw [insert]
      cases hb : (rowInsert row x).2 with
      | none =>
        rw [rowInsert_none_eq_append hb]
        cases rest with
        | nil => exact colStrict_singleton (row ++ [x])
        | cons row2 rest2 =>
          rw [ColStrict, List.isChain_cons_cons]
          rw [ColStrict, List.isChain_cons_cons] at h
          exact ⟨strictBelow_append_upper h.1, h.2⟩
      | some y =>
        show ColStrict ((rowInsert row x).1 :: insert rest y)
        cases hins : insert rest y with
        | nil => exact absurd hins (insert_ne_nil rest y)
        | cons row2 tail2 =>
          rw [ColStrict, List.isChain_cons_cons]
          refine ⟨?_, ?_⟩
          · have hhead : (insert rest y).headD [] = (rowInsert (rest.headD []) y).1 :=
              insert_headD_eq rest y
            rw [hins] at hhead
            simp only [List.headD_cons] at hhead
            rw [hhead]
            apply strictBelow_bump_step _ hb
            cases rest with
            | nil => exact ⟨Nat.zero_le _, fun j hj => (Nat.not_lt_zero j hj).elim⟩
            | cons r3 rest3 =>
              simp only [List.headD_cons]
              rw [ColStrict, List.isChain_cons_cons] at h
              exact h.1
          · have : ColStrict (insert rest y) := insert_colStrict (colStrict_tail h) y
            rw [hins] at this
            rw [ColStrict] at this
            exact this

/-- `insertWord w` is column-strict for every word `w`: the insertion tableau
    `P(w)` has strictly-increasing columns. -/
theorem insertWord_colStrict (w : List ℕ) : ColStrict (insertWord w) := by
  unfold insertWord
  suffices h : ∀ (T : List (List ℕ)), ColStrict T → ColStrict (w.foldl insert T) by
    exact h [] colStrict_nil
  induction w with
  | nil => intro T hT; simpa using hT
  | cons a w ih =>
    intro T hT
    rw [List.foldl_cons]
    exact ih _ (insert_colStrict hT a)

/-! ## Brick 6 — recording tableau `Q` (insertion-step bookkeeping)

`P(w)` records WHICH values sit where; the **recording tableau** `Q(w)` records
WHEN each cell was added — the step index of the insertion that created it.
`insertRec P Q x s` performs one Schensted insertion of `x` into `P` while, in
lockstep, writing the step index `s` into the matching new cell of `Q`: the
single new cell of `insert P x` (Brick 3) gets value `s` in `Q`.

This brick's **seed** (this section) establishes the bookkeeping foundation
sorry-free: the P-component of `insertRec` is exactly `insert`
(`insertRec_fst_eq_insert`), and `P`/`Q` stay shape-aligned (`insertRec_shape`),
so `Q(w)` has the same shape as `P(w)` (`insertWordRec_shape_eq_P`).  The
remaining Brick 6 content — that `Q(w)` is *standard* (entries `1…n` increasing
along rows and columns) — is the follow-on sub-brick, built on this shape match
plus `insertWord_colStrict`. -/

/-- Row-length profile (shape) of a tableau. -/
def tableauShape (T : List (List ℕ)) : List ℕ := T.map List.length

@[simp] theorem tableauShape_nil : tableauShape [] = [] := rfl

@[simp] theorem tableauShape_cons (r : List ℕ) (T : List (List ℕ)) :
    tableauShape (r :: T) = r.length :: tableauShape T := rfl

/-- **Combined P/Q insertion.**  Insert `x` into `P` by the Schensted cascade,
    writing the step index `s` into the matching new cell of `Q`.  A bump leaves
    the current row's Q-length unchanged and cascades to the next row; an append
    writes `s` at the end of the Q-row; falling off the bottom starts a new `[s]`
    Q-row (mirroring the new `[x]` P-row).  `Q` is read via `headD`/`tail`; when
    `P` and `Q` are shape-aligned (the maintained invariant) these are the true
    head row and tail. -/
def insertRec : List (List ℕ) → List (List ℕ) → ℕ → ℕ →
    List (List ℕ) × List (List ℕ)
  | [], _, x, s => ([[x]], [[s]])
  | prow :: prest, Q, x, s =>
      match (rowInsert prow x).2 with
      | none => ((rowInsert prow x).1 :: prest, (Q.headD [] ++ [s]) :: Q.tail)
      | some y =>
          ((rowInsert prow x).1 :: (insertRec prest Q.tail y s).1,
           Q.headD [] :: (insertRec prest Q.tail y s).2)

/-- **The P-component of `insertRec` is exactly Schensted insertion.**  The
    recording bookkeeping never perturbs the insertion tableau: `Q` and `s` only
    fill the Q-component. -/
theorem insertRec_fst_eq_insert :
    ∀ (P Q : List (List ℕ)) (x s : ℕ), (insertRec P Q x s).1 = insert P x
  | [], _, x, s => by simp [insertRec, insert]
  | prow :: prest, Q, x, s => by
      rw [insert, insertRec]
      cases hb : (rowInsert prow x).2 with
      | none => simp
      | some y =>
        show (rowInsert prow x).1 :: (insertRec prest Q.tail y s).1
            = (rowInsert prow x).1 :: insert prest y
        rw [insertRec_fst_eq_insert prest Q.tail y s]

/-- **`insertRec` keeps `P` and `Q` shape-aligned.**  Given a shape-aligned
    input (`tableauShape P = tableauShape Q`), the output tableaux still share a
    shape — a bump preserves every row length, an append/new-row grows both `P`
    and `Q` by one cell in the same row.  So `Q` tracks `P`'s Young-diagram shape
    exactly. -/
theorem insertRec_shape :
    ∀ (P Q : List (List ℕ)) (x s : ℕ), tableauShape P = tableauShape Q →
      tableauShape (insertRec P Q x s).2 = tableauShape (insertRec P Q x s).1
  | [], Q, x, s => by
      intro h
      simp only [tableauShape_nil] at h
      -- shape Q = [] ⇒ Q = []
      have : Q = [] := by
        cases Q with
        | nil => rfl
        | cons q qs => simp [tableauShape] at h
      subst this
      simp [insertRec, tableauShape]
  | prow :: prest, Q, x, s => by
      intro h
      -- shape agreement forces Q = qrow :: qrest with qrow.length = prow.length
      cases Q with
      | nil => simp [tableauShape] at h
      | cons qrow qrest =>
        simp only [tableauShape_cons] at h
        obtain ⟨hql, hqs⟩ := List.cons.injEq .. ▸ h
        rw [insertRec]
        cases hb : (rowInsert prow x).2 with
        | none =>
          have h1 : (rowInsert prow x).1.length = prow.length + 1 :=
            rowInsert_length_none hb
          simp only [List.headD_cons, List.tail_cons, tableauShape_cons,
            List.length_append, List.length_singleton, h1, hql, hqs]
        | some y =>
          simp only [List.headD_cons, List.tail_cons, tableauShape_cons,
            rowInsert_length_some hb]
          rw [insertRec_shape prest qrest y s hqs, hql]

/-- Recording-aware word insertion: fold the letters of `w` left to right,
    threading the P/Q tableaux and the step counter `s`. -/
def insertWordRecAux : List ℕ → ℕ → List (List ℕ) → List (List ℕ) →
    List (List ℕ) × List (List ℕ)
  | [], _, P, Q => (P, Q)
  | x :: rest, s, P, Q =>
      insertWordRecAux rest (s + 1) (insertRec P Q x s).1 (insertRec P Q x s).2

/-- The `P`/`Q` tableaux of a word: `P(w)` is the insertion tableau, `Q(w)` the
    recording tableau (0-based step indices). -/
def insertWordRec (w : List ℕ) : List (List ℕ) × List (List ℕ) :=
  insertWordRecAux w 0 [] []

/-- The P-component of the recording fold is exactly `insertWord`'s fold. -/
theorem insertWordRecAux_fst :
    ∀ (w : List ℕ) (s : ℕ) (P Q : List (List ℕ)),
      (insertWordRecAux w s P Q).1 = w.foldl insert P
  | [], s, P, Q => by simp [insertWordRecAux]
  | x :: rest, s, P, Q => by
      rw [insertWordRecAux, List.foldl_cons, insertWordRecAux_fst rest (s + 1),
        insertRec_fst_eq_insert]

/-- The recording fold keeps `P` and `Q` shape-aligned throughout. -/
theorem insertWordRecAux_shape :
    ∀ (w : List ℕ) (s : ℕ) (P Q : List (List ℕ)),
      tableauShape P = tableauShape Q →
      tableauShape (insertWordRecAux w s P Q).2
        = tableauShape (insertWordRecAux w s P Q).1
  | [], s, P, Q => by intro h; simpa [insertWordRecAux] using h.symm
  | x :: rest, s, P, Q => by
      intro h
      rw [insertWordRecAux]
      exact insertWordRecAux_shape rest (s + 1) _ _ (insertRec_shape P Q x s h).symm

/-- `(insertWordRec w).1 = insertWord w`: the recording tableau's P-component is
    the insertion tableau. -/
theorem insertWordRec_fst (w : List ℕ) : (insertWordRec w).1 = insertWord w := by
  rw [insertWordRec, insertWordRecAux_fst]; rfl

/-- **`Q(w)` has the same shape as `P(w)`.**  The recording tableau matches the
    insertion tableau cell-for-cell — the shape agreement the RSK bijection's
    `(P, Q)` pairing rests on. -/
theorem insertWordRec_shape_eq_P (w : List ℕ) :
    tableauShape (insertWordRec w).2 = tableauShape (insertWord w) := by
  rw [insertWordRec, ← insertWordRec_fst, insertWordRec]
  exact insertWordRecAux_shape w 0 [] [] rfl

/-! ## Brick 6b — the recording tableau `Q(w)` is standard

`Q(w)` is a *standard* tableau: its rows and columns strictly increase.  The
whole result rests on one monotone invariant — at step `s`, **every entry of `Q`
is `< s`** (`tableauAllLt`), because prior insertions used step indices `0…s−1`.
The step-`s` cell is written at a row end (`insertRec`'s none / new-row branches)
and, being larger than every existing entry, exceeds both its left neighbour
(row strictness) and its upper neighbour (column strictness).  Everything below
is bookkeeping around that single fact. -/

/-- Every entry of the tableau `Q` is strictly `< s`. -/
def tableauAllLt (Q : List (List ℕ)) (s : ℕ) : Prop :=
  ∀ row ∈ Q, ∀ e ∈ row, e < s

/-- Every row of `Q` strictly increases (left to right). -/
def RowsStrict (Q : List (List ℕ)) : Prop := ∀ row ∈ Q, row.Sorted (· < ·)

/-- The Q-component of a no-bump `insertRec` appends the step index to the head
    Q-row. -/
theorem insertRec_snd_none {prow : List ℕ} {prest Q : List (List ℕ)} {x s : ℕ}
    (hb : (rowInsert prow x).2 = none) :
    (insertRec (prow :: prest) Q x s).2 = (Q.headD [] ++ [s]) :: Q.tail := by
  rw [insertRec]; simp only [hb]

/-- The Q-component of a bumping `insertRec` keeps the head Q-row and cascades
    into the tail. -/
theorem insertRec_snd_some {prow : List ℕ} {prest Q : List (List ℕ)} {x s y : ℕ}
    (hb : (rowInsert prow x).2 = some y) :
    (insertRec (prow :: prest) Q x s).2
      = Q.headD [] :: (insertRec prest Q.tail y s).2 := by
  rw [insertRec]; simp only [hb]

/-- If an entry lies in the head row `Q.headD []`, that row is genuinely in `Q`
    (it is nonempty, so `Q ≠ []`). -/
theorem headD_mem_of_mem {Q : List (List ℕ)} {e : ℕ} (he : e ∈ Q.headD []) :
    Q.headD [] ∈ Q := by
  cases Q with
  | nil => simp at he
  | cons qh qt => exact List.mem_cons_self

/-- **The monotone invariant.**  If every entry of `Q` is `< s`, then after
    writing step `s` every entry of the new `Q` is `< s + 1`: the old entries are
    `< s < s + 1`, and the single new cell holds `s < s + 1`. -/
theorem insertRec_snd_allLt :
    ∀ (P Q : List (List ℕ)) (x s : ℕ), tableauAllLt Q s →
      tableauAllLt (insertRec P Q x s).2 (s + 1)
  | [], Q, x, s => by
      intro _ row hrow e he
      simp only [insertRec, List.mem_singleton] at hrow
      subst hrow
      simp only [List.mem_singleton] at he
      omega
  | prow :: prest, Q, x, s => by
      intro h
      cases hb : (rowInsert prow x).2 with
      | none =>
        rw [insertRec_snd_none hb]
        intro row hrow e he
        rcases List.mem_cons.mp hrow with hr | hr
        · subst hr
          rcases List.mem_append.mp he with he1 | he2
          · exact Nat.lt_succ_of_lt (h _ (headD_mem_of_mem he1) e he1)
          · simp only [List.mem_singleton] at he2; omega
        · exact Nat.lt_succ_of_lt (h row (List.tail_subset Q hr) e he)
      | some y =>
        rw [insertRec_snd_some hb]
        intro row hrow e he
        rcases List.mem_cons.mp hrow with hr | hr
        · subst hr
          exact Nat.lt_succ_of_lt (h _ (headD_mem_of_mem he) e he)
        · have htail : tableauAllLt Q.tail s :=
            fun r hr' e' he' => h r (List.tail_subset Q hr') e' he'
          exact insertRec_snd_allLt prest Q.tail y s htail row hr e he

/-- Appending a strictly-larger element to a strictly-sorted list keeps it
    strictly sorted. -/
theorem sorted_lt_append_singleton :
    ∀ {l : List ℕ} {s : ℕ}, l.Sorted (· < ·) → (∀ a ∈ l, a < s) →
      (l ++ [s]).Sorted (· < ·)
  | [], s, _, _ => List.sorted_singleton s
  | a :: t, s, hl, hs => by
      rw [List.sorted_cons] at hl
      rw [List.cons_append, List.sorted_cons]
      refine ⟨fun b hb => ?_,
        sorted_lt_append_singleton hl.2 (fun c hc => hs c (List.mem_cons_of_mem a hc))⟩
      rcases List.mem_append.mp hb with hbt | hbs
      · exact hl.1 b hbt
      · simp only [List.mem_singleton] at hbs; subst hbs; exact hs a List.mem_cons_self

/-- **`insertRec` preserves row-strictness of `Q`.**  A no-bump appends the step
    index `s` to the head row; since `s` exceeds every entry (the monotone
    invariant), the row stays strictly increasing.  A bump leaves the head row
    untouched and cascades. -/
theorem insertRec_snd_rowsStrict :
    ∀ (P Q : List (List ℕ)) (x s : ℕ), RowsStrict Q → tableauAllLt Q s →
      RowsStrict (insertRec P Q x s).2
  | [], Q, x, s => by
      intro _ _ row hrow
      simp only [insertRec, List.mem_singleton] at hrow
      subst hrow
      exact List.sorted_singleton s
  | prow :: prest, Q, x, s => by
      intro hrs hlt
      cases hb : (rowInsert prow x).2 with
      | none =>
        rw [insertRec_snd_none hb]
        intro row hrow
        rcases List.mem_cons.mp hrow with hr | hr
        · subst hr
          refine sorted_lt_append_singleton ?_ ?_
          · rcases Q with _ | ⟨qh, qt⟩
            · simp
            · exact hrs qh List.mem_cons_self
          · intro a ha
            exact hlt _ (headD_mem_of_mem ha) a ha
        · exact hrs row (List.tail_subset Q hr)
      | some y =>
        rw [insertRec_snd_some hb]
        intro row hrow
        rcases List.mem_cons.mp hrow with hr | hr
        · subst hr
          rcases Q with _ | ⟨qh, qt⟩
          · simp
          · exact hrs qh List.mem_cons_self
        · have hrs' : RowsStrict Q.tail :=
            fun r hr' => hrs r (List.tail_subset Q hr')
          have hlt' : tableauAllLt Q.tail s :=
            fun r hr' e' he' => hlt r (List.tail_subset Q hr') e' he'
          exact insertRec_snd_rowsStrict prest Q.tail y s hrs' hlt' row hr

/-- The recording fold advances the entry bound by the word length: after
    inserting `w` starting at step `s`, every `Q` entry is `< s + |w|`. -/
theorem insertWordRecAux_allLt :
    ∀ (w : List ℕ) (s : ℕ) (P Q : List (List ℕ)), tableauAllLt Q s →
      tableauAllLt (insertWordRecAux w s P Q).2 (s + w.length)
  | [], s, P, Q => by intro h; simpa [insertWordRecAux] using h
  | x :: rest, s, P, Q => by
      intro h
      rw [insertWordRecAux]
      have := insertWordRecAux_allLt rest (s + 1) (insertRec P Q x s).1
        (insertRec P Q x s).2 (insertRec_snd_allLt P Q x s h)
      simpa [List.length_cons, Nat.add_right_comm, Nat.add_assoc] using this

/-- The recording fold preserves row-strictness of `Q`, threading the monotone
    invariant through each step. -/
theorem insertWordRecAux_rowsStrict :
    ∀ (w : List ℕ) (s : ℕ) (P Q : List (List ℕ)),
      RowsStrict Q → tableauAllLt Q s → RowsStrict (insertWordRecAux w s P Q).2
  | [], s, P, Q => by intro hrs _; simpa [insertWordRecAux] using hrs
  | x :: rest, s, P, Q => by
      intro hrs hlt
      rw [insertWordRecAux]
      exact insertWordRecAux_rowsStrict rest (s + 1) (insertRec P Q x s).1
        (insertRec P Q x s).2
        (insertRec_snd_rowsStrict P Q x s hrs hlt)
        (insertRec_snd_allLt P Q x s hlt)

/-- **`Q(w)` has strictly increasing rows.**  Half of standardness: reading any
    row of the recording tableau left to right gives a strictly increasing
    sequence of step indices, because each cell records the (strictly larger)
    step at which it was appended. -/
theorem insertWordRec_rowsStrict (w : List ℕ) : RowsStrict (insertWordRec w).2 := by
  rw [insertWordRec]
  exact insertWordRecAux_rowsStrict w 0 [] []
    (by intro r hr; simp at hr) (by intro r hr; simp at hr)

/-- **Every entry of `Q(w)` is `< |w|`.**  Combined with the cell count
    `|Q(w)| = |w|` (`insertWordRec_shape_eq_P` + `insertWord_totalCells`), the
    recording tableau's entries are the step indices `0 … |w| − 1`. -/
theorem insertWordRec_entries_lt (w : List ℕ) :
    tableauAllLt (insertWordRec w).2 w.length := by
  rw [insertWordRec]
  have := insertWordRecAux_allLt w 0 [] [] (by intro r hr; simp at hr)
  simpa using this

/-! ### Sub-brick 6c — column-strictness of `Q`

`ColStrict` bundles two independent facts about consecutive rows `(u, l)`: the
**shape** half `l.length ≤ u.length` (the tableau is a Young diagram) and the
**value** half `∀ j < l.length, u.getD j < l.getD j` (columns strictly increase).
For `Q` these decouple cleanly:

* the shape half transfers from `P` — `Q(w)` has the same shape as `P(w)`
  (`insertWordRec_shape_eq_P`) and `P(w)` is column-strict (`insertWord_colStrict`),
  so its shape is a Young diagram;
* the value half follows from the monotone `AllLt` invariant — given the shape is
  Young, the cell directly above a freshly-written step-`s` cell already exists
  and holds an older (hence smaller) step index.
-/

/-- Shape half of `StrictBelow`: consecutive rows have weakly-decreasing lengths
    (the tableau shape is a Young diagram). -/
def ColShapeYoung (T : List (List ℕ)) : Prop :=
  T.IsChain (fun u l => l.length ≤ u.length)

/-- Value half of `StrictBelow`: over the in-range positions, each column entry
    strictly exceeds the one directly above it. -/
def ColValStrict (T : List (List ℕ)) : Prop :=
  T.IsChain (fun u l => ∀ j < l.length, u.getD j 0 < l.getD j 0)

/-- `IsChain` of a pointwise conjunction splits into a conjunction of `IsChain`s. -/
theorem isChain_and {α : Type*} (A B : α → α → Prop) :
    ∀ l : List α, l.IsChain (fun a b => A a b ∧ B a b) ↔ l.IsChain A ∧ l.IsChain B
  | [] => by simp
  | [_] => by simp
  | a :: b :: t => by
      rw [List.isChain_cons_cons, List.isChain_cons_cons, List.isChain_cons_cons,
        isChain_and A B (b :: t)]
      tauto

/-- **`ColStrict` decomposes** into the shape (Young) and value (strict) halves. -/
theorem colStrict_iff (T : List (List ℕ)) :
    ColStrict T ↔ ColShapeYoung T ∧ ColValStrict T := by
  unfold ColStrict ColShapeYoung ColValStrict StrictBelow
  exact isChain_and _ _ T

/-- `ColShapeYoung` reads only row lengths, so it is exactly a chain condition on
    the shape list. -/
theorem colShapeYoung_iff_shape (T : List (List ℕ)) :
    ColShapeYoung T ↔ (tableauShape T).IsChain (fun u l => l ≤ u) := by
  unfold ColShapeYoung tableauShape
  rw [List.isChain_map]

/-- `ColShapeYoung` transfers across equal shapes. -/
theorem colShapeYoung_of_shape_eq {T1 T2 : List (List ℕ)}
    (hsh : tableauShape T1 = tableauShape T2) (h : ColShapeYoung T1) :
    ColShapeYoung T2 := by
  rw [colShapeYoung_iff_shape] at h ⊢; rwa [← hsh]

/-- `ColStrict` implies its shape half. -/
theorem colStrict_shapeYoung {T : List (List ℕ)} (h : ColStrict T) :
    ColShapeYoung T := ((colStrict_iff T).mp h).1

/-- `ColShapeYoung` passes to the tail. -/
theorem colShapeYoung_tail {r : List ℕ} {T : List (List ℕ)}
    (h : ColShapeYoung (r :: T)) : ColShapeYoung T := by
  cases T with
  | nil => simp [ColShapeYoung]
  | cons r2 T2 => rw [ColShapeYoung, List.isChain_cons_cons] at h; exact h.2

/-- `ColValStrict` passes to the tail. -/
theorem colValStrict_tail {r : List ℕ} {T : List (List ℕ)}
    (h : ColValStrict (r :: T)) : ColValStrict T := by
  cases T with
  | nil => simp [ColValStrict]
  | cons r2 T2 => rw [ColValStrict, List.isChain_cons_cons] at h; exact h.2

/-- `getD` in the left part of an append. -/
theorem getD_append_lt {l1 l2 : List ℕ} {j : ℕ} (hj : j < l1.length) :
    (l1 ++ l2).getD j 0 = l1.getD j 0 := by
  simp [List.getD_eq_getElem?_getD, List.getElem?_append_left hj]

/-- `getD` at the join index of `l1 ++ [s]` reads the appended `s`. -/
theorem getD_append_end {l1 : List ℕ} {s : ℕ} :
    (l1 ++ [s]).getD l1.length 0 = s := by
  rw [List.getD_eq_getElem?_getD, List.getElem?_append_right (Nat.le_refl _)]
  simp

/-- The Q-component of `insertRec` is never empty. -/
theorem insertRec_snd_ne_nil (P Q : List (List ℕ)) (x s : ℕ) :
    (insertRec P Q x s).2 ≠ [] := by
  cases P with
  | nil => simp [insertRec]
  | cons prow prest =>
    cases hb : (rowInsert prow x).2 with
    | none => rw [insertRec_snd_none hb]; simp
    | some y => rw [insertRec_snd_some hb]; simp

/-- The head Q-row after `insertRec` is either the old head row or that row with
    the step index appended. -/
theorem insertRec_snd_headD (P Q : List (List ℕ)) (x s : ℕ)
    (hsh : tableauShape P = tableauShape Q) :
    (insertRec P Q x s).2.headD [] = Q.headD []
    ∨ (insertRec P Q x s).2.headD [] = Q.headD [] ++ [s] := by
  cases P with
  | nil =>
    have hQ : Q = [] := by
      cases Q with | nil => rfl | cons a b => simp [tableauShape] at hsh
    subst hQ; right; simp [insertRec]
  | cons prow prest =>
    cases hb : (rowInsert prow x).2 with
    | none => rw [insertRec_snd_none hb]; right; simp
    | some y => rw [insertRec_snd_some hb]; left; simp

/-- **`insertRec` preserves column value-strictness of `Q`.**  Given the result
    shape is a Young diagram (`ColShapeYoung`, supplied from the `P` side), each
    freshly-written step-`s` cell sits below an older (smaller) entry, so columns
    strictly increase.  The append and cascade cases mirror the `rowsStrict`
    proof, with the Young shape supplying `q1.length < qh.length` at the new
    cell. -/
theorem insertRec_snd_colValStrict :
    ∀ (P Q : List (List ℕ)) (x s : ℕ), ColStrict Q → tableauAllLt Q s →
      tableauShape P = tableauShape Q → ColShapeYoung (insertRec P Q x s).2 →
      ColValStrict (insertRec P Q x s).2
  | [], Q, x, s => by
      intro _ _ hsh _
      have hQ : Q = [] := by
        cases Q with | nil => rfl | cons a b => simp [tableauShape] at hsh
      subst hQ; simp [insertRec, ColValStrict]
  | prow :: prest, Q, x, s => by
      intro hcs hlt hsh hyoung
      obtain ⟨qh, qt, rfl⟩ : ∃ qh qt, Q = qh :: qt := by
        cases Q with
        | nil => simp [tableauShape] at hsh
        | cons a b => exact ⟨a, b, rfl⟩
      cases hb : (rowInsert prow x).2 with
      | none =>
        rw [insertRec_snd_none hb] at hyoung ⊢
        simp only [List.headD_cons, List.tail_cons] at hyoung ⊢
        cases qt with
        | nil => simp [ColValStrict]
        | cons q1 rest =>
          rw [ColValStrict, List.isChain_cons_cons]
          rw [ColStrict, List.isChain_cons_cons] at hcs
          obtain ⟨hlen, hval⟩ := hcs.1
          refine ⟨fun j hj => ?_, ?_⟩
          · have hjqh : j < qh.length := lt_of_lt_of_le hj hlen
            rw [getD_append_lt hjqh]
            exact hval j hj
          · exact ((colStrict_iff _).mp hcs.2).2
      | some y =>
        rw [insertRec_snd_some hb] at hyoung ⊢
        simp only [List.headD_cons, List.tail_cons] at hyoung ⊢
        have hcsqt : ColStrict qt := colStrict_tail hcs
        have hltqt : tableauAllLt qt s :=
          fun r hr e he => hlt r (List.mem_cons_of_mem qh hr) e he
        have hshqt : tableauShape prest = tableauShape qt := by
          have h := hsh; simp only [tableauShape_cons, List.cons.injEq] at h; exact h.2
        have hyoungR : ColShapeYoung (insertRec prest qt y s).2 :=
          colShapeYoung_tail hyoung
        have hvalR : ColValStrict (insertRec prest qt y s).2 :=
          insertRec_snd_colValStrict prest qt y s hcsqt hltqt hshqt hyoungR
        obtain ⟨rh, rt, hRcons⟩ :
            ∃ rh rt, (insertRec prest qt y s).2 = rh :: rt := by
          cases hR : (insertRec prest qt y s).2 with
          | nil => exact absurd hR (insertRec_snd_ne_nil prest qt y s)
          | cons a b => exact ⟨a, b, rfl⟩
        rw [hRcons] at hvalR hyoung ⊢
        rw [ColValStrict, List.isChain_cons_cons]
        refine ⟨fun j hj => ?_, hvalR⟩
        -- head-row characterization: rh = qt.headD [] or qt.headD [] ++ [s]
        have hhead := insertRec_snd_headD prest qt y s hshqt
        rw [hRcons, List.headD_cons] at hhead
        -- shape: rh.length ≤ qh.length (from result Young)
        rw [ColShapeYoung, List.isChain_cons_cons] at hyoung
        have hrhlen : rh.length ≤ qh.length := hyoung.1
        rcases hhead with hh | hh
        · -- rh = qt.headD []
          rw [hh] at hj ⊢
          rcases qt with _ | ⟨q1, qrest⟩
          · simp at hj
          · simp only [List.headD_cons] at hj ⊢
            rw [ColStrict, List.isChain_cons_cons] at hcs
            exact hcs.1.2 j hj
        · -- rh = qt.headD [] ++ [s]
          rw [hh] at hj hrhlen ⊢
          by_cases hjlt : j < (qt.headD []).length
          · rw [getD_append_lt hjlt]
            rcases qt with _ | ⟨q1, qrest⟩
            · simp at hjlt
            · simp only [List.headD_cons] at hjlt ⊢
              rw [ColStrict, List.isChain_cons_cons] at hcs
              exact hcs.1.2 j hjlt
          · have hjeq : j = (qt.headD []).length := by
              simp only [List.length_append, List.length_singleton] at hj; omega
            subst hjeq
            rw [getD_append_end]
            simp only [List.length_append, List.length_singleton] at hrhlen
            have hlt' : (qt.headD []).length < qh.length := by omega
            rw [getD_eq_getElem_mem hlt']
            exact hlt qh List.mem_cons_self _ (List.getElem_mem hlt')

/-- **`insertRec` preserves column-strictness of `Q`.**  Combines the two halves:
    the shape (Young) half transfers from `insert P x` (`insert_colStrict`) via
    the `P`/`Q` shape agreement, and the value half is `insertRec_snd_colValStrict`. -/
theorem insertRec_snd_colStrict (P Q : List (List ℕ)) (x s : ℕ)
    (hcsP : ColStrict P) (hcs : ColStrict Q) (hlt : tableauAllLt Q s)
    (hsh : tableauShape P = tableauShape Q) :
    ColStrict (insertRec P Q x s).2 := by
  have hyoung : ColShapeYoung (insertRec P Q x s).2 := by
    refine colShapeYoung_of_shape_eq (T1 := (insertRec P Q x s).1)
      (insertRec_shape P Q x s hsh).symm ?_
    rw [insertRec_fst_eq_insert]
    exact colStrict_shapeYoung (insert_colStrict hcsP x)
  exact (colStrict_iff _).mpr
    ⟨hyoung, insertRec_snd_colValStrict P Q x s hcs hlt hsh hyoung⟩

/-- The recording fold preserves `Q` column-strictness, threading `ColStrict`
    on both `P` and `Q` plus the monotone invariant. -/
theorem insertWordRecAux_colStrict :
    ∀ (w : List ℕ) (s : ℕ) (P Q : List (List ℕ)),
      ColStrict P → ColStrict Q → tableauAllLt Q s → tableauShape P = tableauShape Q →
      ColStrict (insertWordRecAux w s P Q).2
  | [], s, P, Q => by intro _ hcs _ _; simpa [insertWordRecAux] using hcs
  | x :: rest, s, P, Q => by
      intro hcsP hcs hlt hsh
      rw [insertWordRecAux]
      refine insertWordRecAux_colStrict rest (s + 1) (insertRec P Q x s).1
        (insertRec P Q x s).2 ?_ ?_ ?_ ?_
      · rw [insertRec_fst_eq_insert]; exact insert_colStrict hcsP x
      · exact insertRec_snd_colStrict P Q x s hcsP hcs hlt hsh
      · exact insertRec_snd_allLt P Q x s hlt
      · exact insertRec_shape P Q x s hsh |>.symm

/-- **`Q(w)` has strictly increasing columns.**  The remaining half of
    standardness: reading any column of the recording tableau top to bottom gives
    a strictly increasing sequence of step indices. -/
theorem insertWordRec_colStrict (w : List ℕ) : ColStrict (insertWordRec w).2 := by
  rw [insertWordRec]
  exact insertWordRecAux_colStrict w 0 [] [] colStrict_nil colStrict_nil
    (by intro r hr; simp at hr) rfl

/-- **`Q(w)` is a standard tableau.**  Rows and columns strictly increase, and
    the entries are exactly the step indices `0 … |w| − 1` (bounded by
    `insertWordRec_entries_lt`; the cell count `|Q(w)| = |w|` follows from
    `insertWordRec_shape_eq_P` + `insertWord_totalCells`).  Together with
    `insertWord_rowsSorted` + `insertWord_colStrict` making `P(w)` semistandard,
    this completes the `(P, Q)` pair the RSK bijection is built from. -/
theorem insertWordRec_standard (w : List ℕ) :
    RowsStrict (insertWordRec w).2 ∧ ColStrict (insertWordRec w).2
      ∧ tableauAllLt (insertWordRec w).2 w.length :=
  ⟨insertWordRec_rowsStrict w, insertWordRec_colStrict w, insertWordRec_entries_lt w⟩
