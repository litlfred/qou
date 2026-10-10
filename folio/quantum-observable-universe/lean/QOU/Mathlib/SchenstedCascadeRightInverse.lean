import QOU.Mathlib.SchenstedRowRightInverse
import QOU.Mathlib.SchenstedReverseCascade

/-!
# QOU.Mathlib.SchenstedCascadeRightInverse — the cascade right inverse (brick 10)

Brick 9 gave `rowInsert ∘ rowUninsert = id` on one row. This lifts it to the cascade:

> **`insert (uninsert T i).1 z = T`** when the reverse cascade at row `i` displaced `z`.

Brick 2 proved the *other* composite (`uninsert ∘ insert = id`). That one supports injectivity;
this one is what surjectivity needs — running the inverse on a tableau and re-inserting must
return the tableau you started from.

## The hypothesis, and why it is not the corner condition I predicted

I expected to need a **corner condition** (row `i + 1` strictly shorter than row `i`). It is not
that, and it is not a weakening of it. `uninsert` has two branches at the target row and they want
different things:

* **row kept** (`length > 1`) — the row loses its last cell, and re-inserting the displaced value
  appends it straight back: `rowInsert` finds no entry above it, so there is no bump and no
  cascade. This needs nothing but row-sortedness. The corner condition was doing no work here.
* **row deleted** (`length ≤ 1`) — the whole row goes, and the displaced value has to come back as
  a new **top** row. But `insert` only ever appends rows at the *bottom*, so `insert T z = [z] :: T`
  can hold only when `T` is a single column whose entries increase strictly downward: each step
  `rowInsert [b] a` must bump, which needs `a < b`, and that has to hold all the way down.

So the deleting branch needs **column strictness plus the shape condition** — and `ColStrict`,
already in `SchenstedInsertion`, is exactly that: `StrictBelow upper lower` asserts both
`lower.length ≤ upper.length` (the Young-shape half) and `upper[j] < lower[j]` (the strictness
half). The bumping lemma `insert_colStrict` proving `insert` preserves it is already there too.

A first pass here stated the theorem under `2 ≤ (T.getD i []).length`, dodging the deleting branch
and calling the shape condition a later brick. That was under-read: the corpus already carried the
invariant. The general statement below needs no length side condition at all.

For the record, the deleting branch really does fail without the hypothesis — `#eval`-checked, not
asserted: `uninsert [[1],[2,4]] 0 = ([[2,4]], some 1)` while `insert [[2,4]] 1 = [[1,4],[2]]`. Row
lengths there are `(1,2)`, so `StrictBelow` fails on its length half; a genuine tableau excludes it.

## Scope

One insertion step of the cascade, undone and redone. Word-level surjectivity (iterating this the
way brick 3 iterates brick 2) and `RSKBurnsideHolds` for general `n` are the remainder of epic
`qou-nrex`. Nothing here claims them.

Pure combinatorics on `ℕ`; nothing archimedean.

**Scope note superseded (2026-08-23).** The scope paragraph above records the state of the arc when
this brick landed. `RSKBurnsideHolds` is now proved for **every** `n`
(`QOU.Mathlib.rskBurnsideHolds`, brick 42), and `SnIsotypicSpechtSplit` is inhabited, so any
statement here that they "remain open" or hold "only for `n ≤ 12`" describes history rather than the
corpus. The per-brick scope is otherwise unchanged and still accurate.

-/

namespace QOU.Mathlib.Schensted

/-- **Insertion above the whole row appends.** If every entry is `≤ x`, `rowInsert` finds nothing
to bump and puts `x` at the end. -/
theorem rowInsert_of_forall_le : ∀ (r : List ℕ) (x : ℕ), (∀ a ∈ r, a ≤ x) →
    rowInsert r x = (r ++ [x], none)
  | [], _, _ => rfl
  | a :: r, x, h => by
      have ha : ¬ x < a := Nat.not_lt.mpr (h a (List.mem_cons_self ..))
      rw [rowInsert_cons, if_neg ha,
        rowInsert_of_forall_le r x (fun b hb => h b (List.mem_cons_of_mem a hb))]
      simp

/-- Everything before the last entry of a sorted row is `≤` it.

`List.sorted_append` does not exist at this Mathlib pin; `List.Sorted` unfolds to `List.Pairwise`,
so `List.pairwise_append` is the lemma that applies. -/
theorem dropLast_le_getLast {r : List ℕ} (hs : r.Sorted (· ≤ ·)) (h : r ≠ []) :
    ∀ a ∈ r.dropLast, a ≤ r.getLast h := by
  intro a ha
  have hsplit : r.dropLast ++ [r.getLast h] = r := List.dropLast_append_getLast h
  have hp : List.Pairwise (· ≤ ·) (r.dropLast ++ [r.getLast h]) := by rw [hsplit]; exact hs
  obtain ⟨-, -, hcross⟩ := List.pairwise_append.mp hp
  exact hcross a ha (r.getLast h) (List.mem_singleton_self _)

/-- **Re-inserting into a shortened row rebuilds it.** -/
theorem insert_dropLast {r : List ℕ} (hs : r.Sorted (· ≤ ·)) (h : r ≠ [])
    (T : List (List ℕ)) : insert (r.dropLast :: T) (r.getLast h) = r :: T := by
  have hall : ∀ a ∈ r.dropLast, a ≤ r.getLast h := dropLast_le_getLast hs h
  rw [insert, rowInsert_of_forall_le _ _ hall]
  simp only
  rw [List.dropLast_append_getLast h]

/-- **The bumping branch of the reverse cascade, spelled out.** When the recursion below row `r`
displaces `y` and reverse-inserting `y` into `r` displaces `v`, the whole cascade at row `i + 1`
is `(r' :: T', some v)`.

Stating this separately keeps the main induction from having to rewrite under a `match`. -/
theorem uninsert_succ_of_some (r r' : List ℕ) (T T' : List (List ℕ)) (i y v : ℕ)
    (hrec : uninsert T i = (T', some y)) (hru : rowUninsert r y = (r', some v)) :
    uninsert (r :: T) (i + 1) = (r' :: T', some v) := by
  rw [uninsert_succ, hrec]
  simp only
  rw [hru]

/-- The non-bumping branch: if reverse insertion into `r` finds nothing to displace, the cascade
reports `none`. -/
theorem uninsert_succ_of_none_row (r r' : List ℕ) (T T' : List (List ℕ)) (i y : ℕ)
    (hrec : uninsert T i = (T', some y)) (hru : rowUninsert r y = (r', none)) :
    (uninsert (r :: T) (i + 1)).2 = none := by
  rw [uninsert_succ, hrec]
  simp only
  rw [hru]

/-- And if the recursion itself reports nothing, so does the cascade. -/
theorem uninsert_succ_of_none (r : List ℕ) (T T' : List (List ℕ)) (i : ℕ)
    (hrec : uninsert T i = (T', none)) : (uninsert (r :: T) (i + 1)).2 = none := by
  rw [uninsert_succ, hrec]

/-- The head-to-head column comparison carried by `ColStrict`, in the form the single-column
recursion consumes. -/
theorem strictBelow_head_of_colStrict {r : List ℕ} {T : List (List ℕ)} (h : ColStrict (r :: T)) :
    ∀ row ∈ T.head?, StrictBelow r row := by
  cases T with
  | nil => intro row hrow; simp at hrow
  | cons row1 rest =>
      intro row hrow
      simp only [List.head?_cons, Option.mem_def, Option.some.injEq] at hrow
      subst hrow
      rw [ColStrict, List.isChain_cons_cons] at h
      exact h.1

/-- **Re-inserting a deleted top cell rebuilds a single column.** `insert` only ever appends rows
at the *bottom*, so `insert T a = [a] :: T` needs every row of `T` to be a single cell strictly
above the next — which is what `ColStrict` gives once the top row has length one. -/
theorem insert_eq_cons_of_colStrict : ∀ (T : List (List ℕ)), ColStrict T → NoEmptyRows T →
    ∀ (a : ℕ), (∀ row ∈ T.head?, row.length ≤ 1 ∧ a < row.getD 0 0) →
    insert T a = [a] :: T
  | [], _, _, _, _ => rfl
  | row :: rest, hc, hne, a, h => by
      obtain ⟨hlen, hlt⟩ := h row (by simp)
      have hrne : row ≠ [] := hne row (List.mem_cons_self ..)
      obtain ⟨b, rfl⟩ : ∃ b, row = [b] := by
        cases row with
        | nil => exact absurd rfl hrne
        | cons b t =>
            cases t with
            | nil => exact ⟨b, rfl⟩
            | cons c t' => simp at hlen
      have hab : a < b := by simpa using hlt
      have hri : rowInsert [b] a = ([a], some b) := by rw [rowInsert_cons, if_pos hab]
      have hstep : insert rest b = [b] :: rest := by
        refine insert_eq_cons_of_colStrict rest (colStrict_tail hc)
          (fun w hw => hne w (List.mem_cons_of_mem _ hw)) b ?_
        intro row1 hrow1
        obtain ⟨hl, hlt1⟩ := strictBelow_head_of_colStrict hc row1 hrow1
        have hr1ne : row1 ≠ [] := hne row1 (List.mem_cons_of_mem _ (List.mem_of_mem_head? hrow1))
        exact ⟨by simpa using hl, by simpa using hlt1 0 (List.length_pos_iff.mpr hr1ne)⟩
      rw [insert, hri]
      simp only
      rw [hstep]

/-- **The cascade right inverse.** If the reverse cascade at row `i` displaces `z`, re-inserting
`z` rebuilds `T`.

Together with brick 2's `uninsert_insert` this makes `insert` and `uninsert` mutually inverse on a
column-strict tableau: brick 2 gives `uninsert ∘ insert = id`, which supports injectivity, and this
gives `insert ∘ uninsert = id`, which is what surjectivity needs.

The induction mirrors brick 2's. Above the target row each step is undone by brick 9's
`rowInsert_rowUninsert`. At the target row there are two cases: a row that keeps a cell is rebuilt
by `insert_dropLast` with no bump, and a row that is deleted is rebuilt by
`insert_eq_cons_of_colStrict`, which is where column strictness is spent.

The `obtain ⟨_, _, h⟩ : ∃ …, … = (…, …) := ⟨_, _, rfl⟩` idiom names the intermediate results
*without* touching the goal; `rcases h : e with ⟨…⟩` would substitute `e` in the goal but not in
the hypotheses, which leaves the two out of step under the nested `match`. -/
theorem insert_uninsert : ∀ (T : List (List ℕ)) (i : ℕ), RowsSorted T → ColStrict T →
    NoEmptyRows T → ∀ (z : ℕ), (uninsert T i).2 = some z →
    insert (uninsert T i).1 z = T
  | [], i, _, _, _, z, hz => by simp at hz
  | r :: T, 0, hs, hc, hne, z, hz => by
      have hrs : r.Sorted (· ≤ ·) := hs r (List.mem_cons_self ..)
      have hrne : r ≠ [] := hne r (List.mem_cons_self ..)
      have hz' : r.getLast? = some z := by rw [uninsert_zero] at hz; simpa using hz
      rw [uninsert_zero]
      simp only
      by_cases hshort : r.length ≤ 1
      · -- the row is deleted; the displaced cell comes back as a new top row
        rw [if_pos hshort]
        obtain ⟨a, rfl⟩ : ∃ a, r = [a] := by
          cases r with
          | nil => exact absurd rfl hrne
          | cons a t =>
              cases t with
              | nil => exact ⟨a, rfl⟩
              | cons b t' => simp at hshort
        have hza : z = a := by simpa using hz'.symm
        subst hza
        refine insert_eq_cons_of_colStrict T (colStrict_tail hc)
          (fun w hw => hne w (List.mem_cons_of_mem _ hw)) z ?_
        intro row1 hrow1
        obtain ⟨hl, hlt1⟩ := strictBelow_head_of_colStrict hc row1 hrow1
        have hr1ne : row1 ≠ [] := hne row1 (List.mem_cons_of_mem _ (List.mem_of_mem_head? hrow1))
        exact ⟨by simpa using hl, by simpa using hlt1 0 (List.length_pos_iff.mpr hr1ne)⟩
      · -- the row keeps a cell; re-inserting appends it straight back
        rw [if_neg hshort]
        rw [List.getLast?_eq_getLast hrne] at hz'
        have hzl : z = r.getLast hrne := (Option.some.inj hz').symm
        subst hzl
        exact insert_dropLast hrs hrne T
  | r :: T, i + 1, hs, hc, hne, z, hz => by
      have hrs : r.Sorted (· ≤ ·) := hs r (List.mem_cons_self ..)
      have hTs : RowsSorted T := fun row hrow => hs row (List.mem_cons_of_mem r hrow)
      have hTc : ColStrict T := colStrict_tail hc
      have hTne : NoEmptyRows T := fun row hrow => hne row (List.mem_cons_of_mem r hrow)
      obtain ⟨T', w, hrec⟩ : ∃ T' w, uninsert T i = (T', w) := ⟨_, _, rfl⟩
      cases w with
      | none => rw [uninsert_succ_of_none r T T' i hrec] at hz; simp at hz
      | some y =>
          obtain ⟨r', v, hru⟩ : ∃ r' v, rowUninsert r y = (r', v) := ⟨_, _, rfl⟩
          cases v with
          | none => rw [uninsert_succ_of_none_row r r' T T' i y hrec hru] at hz; simp at hz
          | some v =>
              rw [uninsert_succ_of_some r r' T T' i y v hrec hru] at hz ⊢
              simp only at hz ⊢
              have hzv : v = z := Option.some.inj hz
              subst hzv
              have hru' : (rowUninsert r y).2 = some v := by rw [hru]
              have hrow : rowInsert r' v = (r, some y) := by
                have := rowInsert_rowUninsert r hrs y v hru'
                rwa [hru] at this
              have hrec' : (uninsert T i).2 = some y := by rw [hrec]
              have htail : insert T' y = T := by
                have := insert_uninsert T i hTs hTc hTne y hrec'
                rwa [hrec] at this
              rw [insert, hrow]
              simp only
              rw [htail]

end QOU.Mathlib.Schensted
