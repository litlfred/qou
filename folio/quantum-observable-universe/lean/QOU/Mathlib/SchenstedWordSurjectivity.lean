import QOU.Mathlib.SchenstedWordRecovery
import QOU.Mathlib.SchenstedCascadeRightInverse
import QOU.Mathlib.SchenstedUninsertInvariants
import QOU.Mathlib.SchenstedCascadeColStrict

/-!
# QOU.Mathlib.SchenstedWordSurjectivity — the recovered word rebuilds the tableau (brick 14)

Brick 3 (`SchenstedWordRecovery`) proved that running the insertions of a word and then undoing
them at their recorded rows returns the word: `uninsertSteps ∘ insertWord = id`. That direction
supports **injectivity**, and it is the one bricks 7 and 8 already consumed.

This file proves the other direction at the word level: run the reverse cascade at a list of corner
positions, collect what falls out, and re-inserting that word rebuilds the tableau you started
from.

  **`foldl_insert_uninsertSteps`** — `(uninsertSteps T is).2.foldl insert (uninsertSteps T is).1 = T`

and, when the run empties the tableau, the form surjectivity actually wants:

  **`insertWord_uninsertSteps`** — `insertWord (uninsertSteps T is).2 = T`.

## What each brick supplies

| step | from |
|---|---|
| a single reverse step is invertible by `insert` | brick 10, `insert_uninsert` |
| `RowsSorted` / `NoEmptyRows` survive a step | brick 11 |
| `ColStrict` survives a step, at a corner | brick 13, `uninsert_colStrict` |
| the step always succeeds, at a corner | brick 13, `uninsert_isSome_of_isCorner` |

Brick 10 takes the three invariants as hypotheses on the tableau it is handed. Iterating it needs
them at every *intermediate* tableau, which is what bricks 11 and 13 supply, and why they had to
come first.

## `CornersAlong`, and why the corner condition lives on the run

`ColStrict` preservation needs the removed cell to be a corner (brick 11 located that, with a
counterexample). At the level of a whole run, the condition is that *every* step removes a corner
**of the tableau as it stands at that step** — not of the original. `CornersAlong` says exactly
that, by the same recursion `uninsertSteps` itself uses.

This is not a hypothesis a caller has to invent. In the RSK inverse the positions come from the
recording tableau, and the cell carrying the largest remaining entry of a standard tableau is a
corner of the current shape. `CornersAlong` is where that fact is consumed; supplying it is the
Q-side's job, one level up.

## Scope

The `P` side, at the word level, conditional on the run's positions being corners and (for the
second form) on the run emptying the tableau. Both are facts about the recording tableau and are
proved elsewhere or not yet — nothing here claims them. `RSKBurnsideHolds` for general `n` remains
open; it is proved for `n ≤ 12` by an unrelated route (`PartitionsOfBridge.rskBurnsideHolds_le12`,
no RSK in it).

Pure combinatorics on `ℕ`; nothing archimedean.

**Scope note superseded (2026-08-23).** The scope paragraph above records the state of the arc when
this brick landed. `RSKBurnsideHolds` is now proved for **every** `n`
(`QOU.Mathlib.rskBurnsideHolds`, brick 42), and `SnIsotypicSpechtSplit` is inhabited, so any
statement here that they "remain open" or hold "only for `n ≤ 12`" describes history rather than the
corpus. The per-brick scope is otherwise unchanged and still accurate.

-/

namespace QOU.Mathlib.Schensted

/-- **Every step of the run removes a corner** — of the tableau as it stands at that step, which is
what `ColStrict` preservation needs. Defined by the same recursion as `uninsertSteps`: the later
steps of `rest` happen first, so the corner condition for `i` is checked against the tableau they
leave behind. -/
def CornersAlong : List (List ℕ) → List ℕ → Prop
  | _, [] => True
  | T, i :: rest => CornersAlong T rest ∧ IsCorner (uninsertSteps T rest).1 i

@[simp] theorem cornersAlong_nil (T : List (List ℕ)) : CornersAlong T [] := trivial

theorem cornersAlong_cons (T : List (List ℕ)) (i : ℕ) (rest : List ℕ) :
    CornersAlong T (i :: rest) ↔
      CornersAlong T rest ∧ IsCorner (uninsertSteps T rest).1 i := Iff.rfl

/-- **The tableau component of a run does not depend on the `Option`.** Both branches of
`uninsertSteps`' inner `match` return the same tableau, so a run's tableau is just the composite of
the per-step cascades. Isolating this keeps the induction below from case-splitting on an option it
does not care about. -/
theorem uninsertSteps_cons_fst (T : List (List ℕ)) (i : ℕ) (rest : List ℕ) :
    (uninsertSteps T (i :: rest)).1 = (uninsert (uninsertSteps T rest).1 i).1 := by
  rw [uninsertSteps_cons]
  obtain ⟨T', w, h⟩ : ∃ T' w, uninsertSteps T rest = (T', w) := ⟨_, _, rfl⟩
  obtain ⟨T'', v, h2⟩ : ∃ T'' v, uninsert T' i = (T'', v) := ⟨_, _, rfl⟩
  rw [h]
  simp only
  rw [h2]
  cases v <;> simp

/-- When a step ejects a value, the run's word gains it at the front. -/
theorem uninsertSteps_cons_snd_some (T : List (List ℕ)) (i : ℕ) (rest : List ℕ) {x : ℕ}
    (hx : (uninsert (uninsertSteps T rest).1 i).2 = some x) :
    (uninsertSteps T (i :: rest)).2 = x :: (uninsertSteps T rest).2 := by
  rw [uninsertSteps_cons]
  obtain ⟨T', w, h⟩ : ∃ T' w, uninsertSteps T rest = (T', w) := ⟨_, _, rfl⟩
  obtain ⟨T'', v, h2⟩ : ∃ T'' v, uninsert T' i = (T'', v) := ⟨_, _, rfl⟩
  rw [h] at hx ⊢
  simp only at hx ⊢
  rw [h2] at hx ⊢
  simp only at hx ⊢
  subst hx
  simp

/-- **The three invariants survive a whole run**, given that every step removes a corner. -/
theorem uninsertSteps_invariants : ∀ (is : List ℕ) (T : List (List ℕ)),
    RowsSorted T → ColStrict T → NoEmptyRows T → CornersAlong T is →
    RowsSorted (uninsertSteps T is).1 ∧ ColStrict (uninsertSteps T is).1 ∧
      NoEmptyRows (uninsertSteps T is).1
  | [], T, hs, hc, hne, _ => ⟨hs, hc, hne⟩
  | i :: rest, T, hs, hc, hne, hca => by
      obtain ⟨hcaRest, hcorner⟩ := hca
      obtain ⟨hs', hc', hne'⟩ := uninsertSteps_invariants rest T hs hc hne hcaRest
      rw [uninsertSteps_cons_fst]
      exact ⟨uninsert_rowsSorted _ hs' i, uninsert_colStrict hc' hne' hcorner,
        uninsert_noEmptyRows _ hne' i⟩

/-- **The run's word rebuilds the tableau it was peeled from.**

The mirror of brick 3's `uninsertSteps_foldl`. That one runs insertions and undoes them; this one
undoes and re-inserts. Together they make `insertWord` and `uninsertSteps` mutually inverse on
column-strict tableaux, given the positions.

The induction is one step of brick 10 (`insert_uninsert`) wrapped around the inductive hypothesis,
with bricks 11 and 13 supplying the invariants at the intermediate tableau and brick 13 also ruling
out the `none` branch. -/
theorem foldl_insert_uninsertSteps : ∀ (is : List ℕ) (T : List (List ℕ)),
    RowsSorted T → ColStrict T → NoEmptyRows T → CornersAlong T is →
    (uninsertSteps T is).2.foldl insert (uninsertSteps T is).1 = T
  | [], T, _, _, _, _ => rfl
  | i :: rest, T, hs, hc, hne, hca => by
      obtain ⟨hcaRest, hcorner⟩ := hca
      obtain ⟨hs', hc', hne'⟩ := uninsertSteps_invariants rest T hs hc hne hcaRest
      obtain ⟨x, hx⟩ := uninsert_isSome_of_isCorner hc' hne' hcorner
      rw [uninsertSteps_cons_fst, uninsertSteps_cons_snd_some T i rest hx, List.foldl_cons,
        insert_uninsert _ i hs' hc' hne' x hx]
      exact foldl_insert_uninsertSteps rest T hs hc hne hcaRest

/-- **The form surjectivity wants.** When the run empties the tableau, the word it recovered is a
word whose insertion tableau is exactly `T`.

`insertWord` is `foldl insert []`, so this is `foldl_insert_uninsertSteps` with the starting
tableau known to be empty. Whether a given run empties the tableau is a fact about the positions —
supplied by the recording tableau, not by anything here. -/
theorem insertWord_uninsertSteps (T : List (List ℕ)) (is : List ℕ)
    (hs : RowsSorted T) (hc : ColStrict T) (hne : NoEmptyRows T) (hca : CornersAlong T is)
    (hempty : (uninsertSteps T is).1 = []) :
    insertWord (uninsertSteps T is).2 = T := by
  have h := foldl_insert_uninsertSteps is T hs hc hne hca
  rwa [hempty] at h

end QOU.Mathlib.Schensted
