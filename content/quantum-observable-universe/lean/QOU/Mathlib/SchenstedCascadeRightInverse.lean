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

I expected to need a **corner condition** (row `i+1` strictly shorter than row `i`). Measured, the
actual requirement is narrower and different: **the target row must keep at least one cell**
(`2 ≤ (T.getD i []).length`).

The reason is that `uninsert` has two branches at the target row, and only one of them is
invertible by `insert`:

* **row kept** (`length > 1`): the row loses its last cell, and re-inserting the displaced value
  appends it straight back — `rowInsert` finds no entry above it, so there is no bump and no
  cascade. This works for *any* sorted row, corner or not.
* **row deleted** (`length ≤ 1`): the whole row goes, and `insert` then starts at what used to be
  the *next* row. That is not an inverse in general. Concretely `T = [[1],[2,4]]` gives
  `uninsert T 0 = ([[2,4]], some 1)` and `insert [[2,4]] 1 = [[1,4],[2]] ≠ T` — both sides
  `#eval`-checked, not asserted. Note `T` here has a non-Young shape `(1,2)`, which is exactly the
  case a genuine tableau excludes.

So the deleting branch needs a *shape* hypothesis (row lengths weakly decreasing), not a corner
one, and it is left to a later brick. Stating the hypothesis I can discharge, rather than the one
I guessed, is the point of this file.

## Scope

The non-deleting branch of the cascade. The deleting branch, word-level surjectivity, and
`RSKBurnsideHolds` are the remainder of epic `qou-nrex`. Nothing here claims them.

Pure combinatorics on `ℕ`; nothing archimedean.
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

/-- **The cascade right inverse, non-deleting branch.** If the reverse cascade at row `i` leaves
that row with at least one cell and displaces `z`, then re-inserting `z` rebuilds `T`.

The induction is the mirror of brick 2's: above the target row each step is undone by brick 9's
`rowInsert_rowUninsert`, and at the target row `insert_dropLast` puts the removed cell back with
no bump — so the re-insertion never cascades past where the removal started.

The `obtain ⟨_, _, h⟩ : ∃ …, … = (…, …) := ⟨_, _, rfl⟩` idiom names the intermediate results
*without* touching the goal; `rcases h : e with ⟨…⟩` would substitute `e` in the goal but not in
the hypotheses, which leaves the two out of step under the nested `match`. -/
theorem insert_uninsert : ∀ (T : List (List ℕ)) (i : ℕ), RowsSorted T →
    2 ≤ (T.getD i []).length → ∀ (z : ℕ), (uninsert T i).2 = some z →
    insert (uninsert T i).1 z = T
  | [], i, _, hlen, z, _ => by simp at hlen
  | r :: T, 0, hs, hlen, z, hz => by
      have hrs : r.Sorted (· ≤ ·) := hs r (List.mem_cons_self ..)
      simp only [List.getD_cons_zero] at hlen
      have hne : r ≠ [] := by intro h; rw [h] at hlen; simp at hlen
      have hkeep : ¬ r.length ≤ 1 := by omega
      rw [uninsert_zero, if_neg hkeep] at hz ⊢
      simp only at hz ⊢
      rw [List.getLast?_eq_getLast hne] at hz
      have hzl : z = r.getLast hne := (Option.some.inj hz).symm
      subst hzl
      exact insert_dropLast hrs hne T
  | r :: T, i + 1, hs, hlen, z, hz => by
      have hrs : r.Sorted (· ≤ ·) := hs r (List.mem_cons_self ..)
      have hTs : RowsSorted T := fun row hrow => hs row (List.mem_cons_of_mem r hrow)
      simp only [List.getD_cons_succ] at hlen
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
                have := insert_uninsert T i hTs hlen y hrec'
                rwa [hrec] at this
              rw [insert, hrow]
              simp only
              rw [htail]

end QOU.Mathlib.Schensted
