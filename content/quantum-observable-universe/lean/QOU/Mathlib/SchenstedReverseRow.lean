import QOU.Mathlib.SchenstedInsertion

/-!
# QOU.Mathlib.SchenstedReverseRow — reverse row insertion (the RSK inverse, brick 1)

The Schensted programme has built the forward map as far as
`SchenstedPairingMap.rskPair : Equiv.Perm (Fin n) → Σ_λ SYT(λ) × SYT(λ)`. What its own roadmap
names next is the **inverse** — reverse bumping — and that is what this file starts, mirroring
`SchenstedInsertion`'s brick 1 on the other side.

**Why the inverse and not injectivity of the forward map.** Injectivity of `rskPair` would give
`n! ≤ Σ_λ (f^λ)²`, and that inequality is *already available* by a completely different route:
`BraidKnot.SpechtActionInjective.factorial_le_sum_sq`, from injectivity of the Specht action map.
The two programmes deliver the same direction. What neither has is the reverse, and on the RSK
side the reverse is exactly the inverse map. So reverse bumping is the non-redundant next step.

`rowUninsert r y` undoes `rowInsert`: it replaces the **rightmost** entry of `r` strictly less
than `y` by `y`, and returns that entry. If no entry is `< y` it reports `none` — the signal that
this row was not the one bumped into.

Proved here, sorry-free:

* `rowUninsert_of_forall_le` — a row all of whose entries are `≥ y` is untouched (`none`);
* **`rowUninsert_rowInsert`** — the inversion law: if inserting `x` into a weakly-increasing `r`
  bumps `y`, then reverse-inserting `y` into the result returns `r` and reports `x`;
* `rowUninsert_length` / `rowUninsert_sorted` — the two structural invariants, mirroring
  `rowInsert_length` / `rowInsert_sorted`.

## Scope

One row. The cascade across rows (undoing `insertRec`), the recovery of the word, and the
resulting bijection are later bricks; nothing here claims them, and `RSKBurnsideHolds` for
general `n` remains open. (It is *proved* for `n ≤ 12` by a different route entirely —
`PartitionsOfBridge.rskBurnsideHolds_le12`, no RSK involved.)

Pure combinatorics on `ℕ`; nothing archimedean.

**Scope note superseded (2026-08-23).** The scope paragraph above records the state of the arc when
this brick landed. `RSKBurnsideHolds` is now proved for **every** `n`
(`QOU.Mathlib.rskBurnsideHolds`, brick 42), and `SnIsotypicSpechtSplit` is inhabited, so any
statement here that they "remain open" or hold "only for `n ≤ 12`" describes history rather than the
corpus. The per-brick scope is otherwise unchanged and still accurate.

-/

namespace QOU.Mathlib.Schensted

/-- **Reverse row insertion.** Undo a bump: replace the rightmost entry of `r` strictly less than
`y` by `y`, returning `(newRow, some removed)`. If every entry is `≥ y` there is nothing to undo,
and the row is returned unchanged with `none`.

The recursion descends to the end of the list first, so the *rightmost* eligible entry is the one
replaced — the mirror of `rowInsert`, which stops at the *leftmost* entry strictly greater than
the inserted value. -/
def rowUninsert : List ℕ → ℕ → List ℕ × Option ℕ
  | [], _ => ([], none)
  | a :: r, y =>
      match rowUninsert r y with
      | (r', some z) => (a :: r', some z)
      | (_, none) => if a < y then (y :: r, some a) else (a :: r, none)

@[simp] theorem rowUninsert_nil (y : ℕ) : rowUninsert [] y = ([], none) := rfl

theorem rowUninsert_cons (a : ℕ) (r : List ℕ) (y : ℕ) :
    rowUninsert (a :: r) y =
      match rowUninsert r y with
      | (r', some z) => (a :: r', some z)
      | (_, none) => if a < y then (y :: r, some a) else (a :: r, none) := rfl

/-- **Nothing to undo.** If every entry of `r` is at least `y`, reverse insertion leaves `r` alone
and reports `none`. This is what makes the inversion law's base case go through: past the
insertion point a Schensted row is entirely `≥` the bumped value. -/
theorem rowUninsert_of_forall_le : ∀ (r : List ℕ) (y : ℕ), (∀ a ∈ r, y ≤ a) →
    rowUninsert r y = (r, none)
  | [], _, _ => rfl
  | a :: r, y, h => by
      have hr : rowUninsert r y = (r, none) :=
        rowUninsert_of_forall_le r y (fun b hb => h b (List.mem_cons_of_mem a hb))
      have ha : ¬ a < y := Nat.not_lt.mpr (h a (List.mem_cons_self ..))
      rw [rowUninsert_cons, hr]
      simp [ha]

/-- **The inversion law.** If inserting `x` into a weakly-increasing row `r` bumps `y`, then
reverse-inserting `y` into the resulting row recovers `r` and reports the inserted `x`.

`rowInsert` and `rowUninsert` are therefore mutually inverse on the bumping branch, which is the
branch the RSK cascade runs on. -/
theorem rowUninsert_rowInsert : ∀ (r : List ℕ), r.Sorted (· ≤ ·) → ∀ (x y : ℕ),
    (rowInsert r x).2 = some y → rowUninsert (rowInsert r x).1 y = (r, some x)
  | [], _, x, y, hy => by simp [rowInsert] at hy
  | a :: r, hs, x, y, hy => by
      rw [List.sorted_cons] at hs
      obtain ⟨hle, hsr⟩ := hs
      rw [rowInsert_cons] at hy ⊢
      by_cases hx : x < a
      · -- leftmost bump: `y = a`, and the tail is entirely `≥ a`, so nothing further undoes
        rw [if_pos hx] at hy ⊢
        simp only at hy
        injection hy with hy
        subst hy
        rw [rowUninsert_cons, rowUninsert_of_forall_le r a hle]
        simp [hx]
      · -- no bump here: recurse into the tail
        rw [if_neg hx] at hy ⊢
        simp only at hy ⊢
        rw [rowUninsert_cons, rowUninsert_rowInsert r hsr x y hy]

/-- Reverse insertion never changes the row length. -/
theorem rowUninsert_length : ∀ (r : List ℕ) (y : ℕ), (rowUninsert r y).1.length = r.length
  | [], _ => rfl
  | a :: r, y => by
      rw [rowUninsert_cons]
      rcases hr : rowUninsert r y with ⟨r', z⟩
      cases z with
      | some z =>
          simp only [List.length_cons]
          have := rowUninsert_length r y
          rw [hr] at this
          simp [this]
      | none =>
          by_cases ha : a < y <;> simp [ha]

/-- Every entry of a reverse-inserted row is an old entry or the value `y` put in. -/
theorem mem_rowUninsert : ∀ (r : List ℕ) (y b : ℕ), b ∈ (rowUninsert r y).1 → b ∈ r ∨ b = y
  | [], _, _, hb => by simp at hb
  | a :: r, y, b, hb => by
      rw [rowUninsert_cons] at hb
      rcases hr : rowUninsert r y with ⟨r', z⟩
      rw [hr] at hb
      cases z with
      | some z =>
          simp only [List.mem_cons] at hb
          rcases hb with rfl | hb
          · exact Or.inl (List.mem_cons_self ..)
          · rcases mem_rowUninsert r y b (by rw [hr]; exact hb) with h | h
            · exact Or.inl (List.mem_cons_of_mem a h)
            · exact Or.inr h
      | none =>
          by_cases ha : a < y
          · simp only [ha, if_true, List.mem_cons] at hb
            rcases hb with rfl | hb
            · exact Or.inr rfl
            · exact Or.inl (List.mem_cons_of_mem a hb)
          · simp only [ha, if_false] at hb
            exact Or.inl hb

/-- `none` means every entry was at least `y` — the converse of `rowUninsert_of_forall_le`. -/
theorem forall_le_of_rowUninsert_none : ∀ (r : List ℕ) (y : ℕ), (rowUninsert r y).2 = none →
    ∀ a ∈ r, y ≤ a
  | [], _, _, _, hb => by simp at hb
  | a :: r, y, hnone, b, hb => by
      rw [rowUninsert_cons] at hnone
      rcases hr : rowUninsert r y with ⟨r', z⟩
      rw [hr] at hnone
      cases z with
      | some z => simp at hnone
      | none =>
          by_cases ha : a < y
          · simp [ha] at hnone
          · have htail := forall_le_of_rowUninsert_none r y (by rw [hr])
            rcases List.mem_cons.mp hb with rfl | hb'
            · exact Nat.not_lt.mp ha
            · exact htail b hb'

/-- `some` means some entry was strictly below `y` — there was something to replace. -/
theorem exists_lt_of_rowUninsert_some : ∀ (r : List ℕ) (y z : ℕ), (rowUninsert r y).2 = some z →
    ∃ c ∈ r, c < y
  | [], _, _, hz => by simp at hz
  | a :: r, y, z, hz => by
      rw [rowUninsert_cons] at hz
      rcases hr : rowUninsert r y with ⟨r', w⟩
      rw [hr] at hz
      cases w with
      | some w =>
          obtain ⟨c, hc, hcy⟩ := exists_lt_of_rowUninsert_some r y w (by rw [hr])
          exact ⟨c, List.mem_cons_of_mem a hc, hcy⟩
      | none =>
          by_cases ha : a < y
          · exact ⟨a, List.mem_cons_self .., ha⟩
          · simp [ha] at hz

/-- Reverse insertion keeps the row weakly increasing.

The replaced entry is the rightmost one strictly below `y`, so everything after it is already
`≥ y`; and everything before it is `≤` the old entry, which is `< y`. -/
theorem rowUninsert_sorted : ∀ (r : List ℕ), r.Sorted (· ≤ ·) → ∀ (y : ℕ),
    (rowUninsert r y).1.Sorted (· ≤ ·)
  | [], _, _ => by simp
  | a :: r, hs, y => by
      rw [List.sorted_cons] at hs
      obtain ⟨hle, hsr⟩ := hs
      rw [rowUninsert_cons]
      rcases hr : rowUninsert r y with ⟨r', z⟩
      cases z with
      | some z =>
          simp only
          rw [List.sorted_cons]
          refine ⟨fun b hb => ?_, ?_⟩
          · -- every entry of the rewritten tail is an old entry or `y`, and `a ≤` both
            rcases mem_rowUninsert r y b (by rw [hr]; exact hb) with h | h
            · exact hle b h
            · -- `b = y`; and a replacement happened, so some tail entry is `< y`, and `a` is
              -- below every tail entry
              rw [h]
              obtain ⟨c, hc, hcy⟩ := exists_lt_of_rowUninsert_some r y z (by rw [hr])
              exact le_of_lt (lt_of_le_of_lt (hle c hc) hcy)
          · have := rowUninsert_sorted r hsr y
            rw [hr] at this
            exact this
      | none =>
          by_cases ha : a < y
          · simp only [ha, if_true]
            rw [List.sorted_cons]
            refine ⟨fun b hb => ?_, hsr⟩
            -- the tail was untouched and is entirely `≥ y`
            have hall := forall_le_of_rowUninsert_none r y (by rw [hr])
            exact hall b hb
          · simp only [ha, if_false]
            rw [List.sorted_cons]
            exact ⟨hle, hsr⟩

end QOU.Mathlib.Schensted
