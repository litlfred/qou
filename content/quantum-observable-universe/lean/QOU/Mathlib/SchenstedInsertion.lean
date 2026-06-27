import Mathlib.Data.List.Sort

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
