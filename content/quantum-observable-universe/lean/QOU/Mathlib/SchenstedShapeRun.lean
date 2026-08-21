import QOU.Mathlib.SchenstedMaxCorner

/-!
# QOU.Mathlib.SchenstedShapeRun — `CornersAlong` reduces to a shape-level condition (brick 18)

Brick 14 left two hypotheses as the interface between the `P` side of the RSK inverse and the
recording tableau; brick 15 showed they are inhabited; bricks 16 and 17 supplied the corner argument
and the shape bridge. This file spends them.

> **`uninsertSteps_shape_and_corners`** — from a condition stated **entirely on shapes**, both
> `CornersAlong T is` and the shape of the tableau the run returns follow.

The point is the decoupling. `CornersAlong T is` mentions the tableau `T` at every step, so
discharging it looked like it would need `P` and `Q` reasoned about together. It does not:
`IsCorner` is determined by the shape (`isCorner_iff_shape`), and brick 17 says the cascade acts on
shapes as `removeCorner`. So the whole run-level corner condition factors through
`tableauShape T` — and what remains for surjectivity is a statement about `Q`'s shape alone, with
`P` no longer mentioned.

## Why the four conclusions are proved together

`CornersAlong` and the shape identity are mutually dependent along the induction: knowing the shape
at step `k` needs the corner condition to have held at every later step (or the cascade may not even
have succeeded), and checking the corner condition at step `k` needs the shape at step `k`. Brick
14's `uninsertSteps_invariants` is no help on its own — it *takes* `CornersAlong` as a hypothesis,
which is what we are trying to produce. One simultaneous induction resolves all of it.

## Scope

The reduction, and nothing beyond it. Producing `ShapeCornersAlong` from a standard recording
tableau — reading the positions off `Q` and showing each step peels the corner carrying the largest
remaining entry — is the next brick of epic `qou-nrex`. Nothing here claims it, nothing here claims
`rskPair` is bijective, and `RSKBurnsideHolds` for general `n` stays open (proved for `n ≤ 12` by an
unrelated route, `PartitionsOfBridge.rskBurnsideHolds_le12`, with no RSK correspondence in it).

Pure combinatorics on `ℕ`; nothing archimedean.
-/

namespace QOU.Mathlib.Schensted

open QOU.Mathlib.SYTEnum (removeCorner)

/-- Peel the corners named by `is` off a shape, later steps first — the shape-level mirror of
`uninsertSteps`' tableau component. -/
def removeCornerSteps : List ℕ → List ℕ → List ℕ
  | l, [] => l
  | l, i :: rest => removeCorner (removeCornerSteps l rest) i

@[simp] theorem removeCornerSteps_nil (l : List ℕ) : removeCornerSteps l [] = l := rfl

theorem removeCornerSteps_cons (l : List ℕ) (i : ℕ) (rest : List ℕ) :
    removeCornerSteps l (i :: rest) = removeCorner (removeCornerSteps l rest) i := rfl

/-- **The run-level corner condition, stated on shapes.** Every step names a corner of the shape as
it stands at that step. Mirrors `CornersAlong` exactly, with the tableau replaced by its shape. -/
def ShapeCornersAlong : List ℕ → List ℕ → Prop
  | _, [] => True
  | l, i :: rest => ShapeCornersAlong l rest ∧ QOU.Mathlib.SYTEnum.IsCorner (removeCornerSteps l rest) i

@[simp] theorem shapeCornersAlong_nil (l : List ℕ) : ShapeCornersAlong l [] := trivial

theorem shapeCornersAlong_cons (l : List ℕ) (i : ℕ) (rest : List ℕ) :
    ShapeCornersAlong l (i :: rest) ↔
      ShapeCornersAlong l rest ∧ QOU.Mathlib.SYTEnum.IsCorner (removeCornerSteps l rest) i :=
  Iff.rfl

/-- **The reduction.** A shape-level corner condition delivers the tableau-level one, together with
the shape of the tableau the run returns.

Both conclusions are proved in one induction because neither is available without the other — see
the module docstring. The step is: the inductive hypothesis gives the shape at the later steps, the
shape-level corner condition transfers to the tableau through `isCorner_iff_shape`, brick 14's
`uninsertSteps_invariants` then supplies `ColStrict` and `NoEmptyRows` at that intermediate tableau,
and brick 17's `tableauShape_uninsert` advances the shape by one `removeCorner`. -/
theorem uninsertSteps_shape_and_corners : ∀ (is : List ℕ) (T : List (List ℕ)),
    RowsSorted T → ColStrict T → NoEmptyRows T → ShapeCornersAlong (tableauShape T) is →
    CornersAlong T is ∧
      tableauShape (uninsertSteps T is).1 = removeCornerSteps (tableauShape T) is
  | [], T, _, _, _, _ => ⟨trivial, rfl⟩
  | i :: rest, T, hs, hc, hne, hsca => by
      obtain ⟨hscaRest, hcornerShape⟩ := hsca
      obtain ⟨hCA, hshape⟩ := uninsertSteps_shape_and_corners rest T hs hc hne hscaRest
      -- the invariants at the intermediate tableau, now that its corner history is known
      obtain ⟨hs', hc', hne'⟩ := uninsertSteps_invariants rest T hs hc hne hCA
      -- the shape-level corner transfers to the tableau
      have hcorner : IsCorner (uninsertSteps T rest).1 i := by
        rw [isCorner_iff_shape, hshape]
        exact hcornerShape
      refine ⟨⟨hCA, hcorner⟩, ?_⟩
      rw [uninsertSteps_cons_fst, tableauShape_uninsert _ i hc' hne' hcorner, hshape,
        removeCornerSteps_cons]

/-- The tableau-level corner condition, on its own. -/
theorem cornersAlong_of_shape {T : List (List ℕ)} {is : List ℕ}
    (hs : RowsSorted T) (hc : ColStrict T) (hne : NoEmptyRows T)
    (hsca : ShapeCornersAlong (tableauShape T) is) : CornersAlong T is :=
  (uninsertSteps_shape_and_corners is T hs hc hne hsca).1

/-- The shape the run returns, on its own. -/
theorem tableauShape_uninsertSteps {T : List (List ℕ)} {is : List ℕ}
    (hs : RowsSorted T) (hc : ColStrict T) (hne : NoEmptyRows T)
    (hsca : ShapeCornersAlong (tableauShape T) is) :
    tableauShape (uninsertSteps T is).1 = removeCornerSteps (tableauShape T) is :=
  (uninsertSteps_shape_and_corners is T hs hc hne hsca).2

/-- **The `P`-side conclusion, from shapes alone.** If the run's positions are corners of the shape
and peel it down to nothing, the word it recovers has `T` as its insertion tableau.

Every hypothesis is now about `T`'s **shape** and the position list — `P` itself appears only in the
conclusion. That is the whole point of the reduction: what remains for surjectivity is to produce
`ShapeCornersAlong` and the emptying condition from a standard recording tableau, with the
insertion tableau no longer involved. -/
theorem insertWord_uninsertSteps_of_shape {T : List (List ℕ)} {is : List ℕ}
    (hs : RowsSorted T) (hc : ColStrict T) (hne : NoEmptyRows T)
    (hsca : ShapeCornersAlong (tableauShape T) is)
    (hempty : removeCornerSteps (tableauShape T) is = []) :
    insertWord (uninsertSteps T is).2 = T := by
  refine insertWord_uninsertSteps T is hs hc hne (cornersAlong_of_shape hs hc hne hsca) ?_
  have hshape := tableauShape_uninsertSteps hs hc hne hsca
  rw [hempty] at hshape
  -- an empty shape means an empty tableau: `tableauShape` is a `map`, so it preserves length
  have hlen : (uninsertSteps T is).1.length = 0 := by
    have := congrArg List.length hshape
    simpa [tableauShape] using this
  exact List.eq_nil_of_length_eq_zero hlen

end QOU.Mathlib.Schensted
