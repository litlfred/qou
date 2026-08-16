import QOU.Mathlib.SchenstedReverseRow

/-!
# QOU.Mathlib.SchenstedRowRightInverse — the other row-level inverse law (brick 9)

Brick 1 proved `rowUninsert ∘ rowInsert = id` on the bumping branch. Surjectivity of RSK needs the
**other** composite: running a reverse insertion and then re-inserting the value it displaced must
give the original row back.

* `mem_of_rowUninsert_some` — the displaced value came from the row.
* **`rowInsert_rowUninsert`** — if `rowUninsert r y = (r', some z)` for a weakly-increasing `r`,
  then `rowInsert r' z = (r, some y)`.

Together with brick 1 the two maps are mutually inverse on their bumping branches, which is what
turns "the inverse machinery exists" into "the forward map is onto".

## Why it works

`rowUninsert` replaces the rightmost entry `z < y` by `y`. In the resulting row everything strictly
before that position is `≤ z` (the row was sorted and `z` sat there), and the position itself now
holds `y > z`. So when `rowInsert` looks for the **leftmost entry `> z`** it lands on exactly that
position — the two rules are looking for the same cell from opposite ends, which is why the
composite is the identity and not merely close to it.

## Scope

One row, one step. The cascade-level right inverse (`insert ∘ uninsert = id` under a corner
condition) and the word-level surjectivity are later bricks of epic `qou-nrex`; nothing here
claims them, and `RSKBurnsideHolds` for general `n` remains open.

Pure combinatorics on `ℕ`; nothing archimedean.
-/

namespace QOU.Mathlib.Schensted

/-- The value a reverse insertion displaces is one of the row's entries. -/
theorem mem_of_rowUninsert_some : ∀ (r : List ℕ) (y z : ℕ), (rowUninsert r y).2 = some z → z ∈ r
  | [], _, _, hz => by simp at hz
  | a :: r, y, z, hz => by
      rw [rowUninsert_cons] at hz
      rcases hr : rowUninsert r y with ⟨r'', w⟩
      rw [hr] at hz
      cases w with
      | some w =>
          simp only [Option.some.injEq] at hz
          subst hz
          exact List.mem_cons_of_mem a (mem_of_rowUninsert_some r y w (by rw [hr]))
      | none =>
          by_cases ha : a < y
          · simp only [ha, if_true, Option.some.injEq] at hz
            subst hz
            exact List.mem_cons_self ..
          · simp [ha] at hz

/-- **The other inversion law.** Re-inserting the displaced value into the reverse-inserted row
recovers the original row, and bumps back the value that was pushed in.

This is the mirror of `rowUninsert_rowInsert`: brick 1 undid an insertion, this redoes an undoing.
-/
theorem rowInsert_rowUninsert : ∀ (r : List ℕ), r.Sorted (· ≤ ·) → ∀ (y z : ℕ),
    (rowUninsert r y).2 = some z → rowInsert (rowUninsert r y).1 z = (r, some y)
  | [], _, y, z, hz => by simp at hz
  | a :: r, hs, y, z, hz => by
      rw [List.sorted_cons] at hs
      obtain ⟨hle, hsr⟩ := hs
      rcases hr : rowUninsert r y with ⟨r'', w⟩
      cases w with
      | some w =>
          -- the replacement happened further right; `a` stays put and the recursion re-does it
          have hfst : (rowUninsert (a :: r) y).1 = a :: r'' := by rw [rowUninsert_cons, hr]
          have hsnd : (rowUninsert (a :: r) y).2 = some w := by rw [rowUninsert_cons, hr]
          rw [hsnd] at hz
          have hwz : w = z := Option.some.inj hz
          subst hwz
          have hz' : (rowUninsert r y).2 = some w := by rw [hr]
          have haw : ¬ w < a := Nat.not_lt.mpr (hle w (mem_of_rowUninsert_some r y w hz'))
          have hrec : rowInsert r'' w = (r, some y) := by
            have hrr := rowInsert_rowUninsert r hsr y w hz'
            rwa [hr] at hrr
          rw [hfst, rowInsert_cons, if_neg haw]
          simp only [hrec]
      | none =>
          by_cases ha : a < y
          · -- `a` itself was the replaced entry, so `z = a` and `rowInsert` bumps `y` straight back
            have hfst : (rowUninsert (a :: r) y).1 = y :: r := by
              rw [rowUninsert_cons, hr]; simp [ha]
            have hsnd : (rowUninsert (a :: r) y).2 = some a := by
              rw [rowUninsert_cons, hr]; simp [ha]
            rw [hsnd] at hz
            have haz : a = z := Option.some.inj hz
            subst haz
            rw [hfst, rowInsert_cons, if_pos ha]
          · have hsnd : (rowUninsert (a :: r) y).2 = none := by
              rw [rowUninsert_cons, hr]; simp [ha]
            rw [hsnd] at hz
            simp at hz

end QOU.Mathlib.Schensted
