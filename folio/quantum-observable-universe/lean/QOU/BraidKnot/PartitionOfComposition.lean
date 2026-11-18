import QOU.BraidKnot.PartitionLex
import Mathlib.Data.List.Sort

/-!
# A composition as a Young diagram, and its column lengths as a part count

Mathas' Garnir lemma replaces two parts of a partition by three, producing a
**composition** — the parts are no longer weakly decreasing.  Turning that back into
a shape means sorting, and reasoning about the sorted list is the expensive part of
the argument.

This file makes it cheap, by never looking at the sorted list again after building
the diagram:

    colLen_ofComposition :  (ofComposition l).colLen m  =  l.countP (m < ·)

`countP` is **permutation-invariant**, so the right-hand side is a statement about
the composition *as given* — no sortedness, no indices, no reasoning about where the
new parts landed.  Everything the Garnir step needs is then `countP` arithmetic on a
list that differs from `μ.rowLens` in three entries.

Together with `PartitionLex.lexGt_of_colLen`, whose hypotheses are exactly two
column-length facts, this reduces "the Garnir shape is lex-greater" to counting.
-/

namespace QOU.BraidKnot.PartitionOfComposition

open QOU.BraidKnot.PartitionLex

/-- The parts of a list, sorted weakly decreasing. -/
def sortDesc (l : List ℕ) : List ℕ := List.insertionSort (· ≥ ·) l

theorem sortDesc_sorted (l : List ℕ) : List.Sorted (· ≥ ·) (sortDesc l) :=
  List.sorted_insertionSort _ l

theorem sortDesc_perm (l : List ℕ) : (sortDesc l).Perm l :=
  List.perm_insertionSort _ l

/-- **A composition as a Young diagram**: sort its parts and read them as row lengths.

Zero parts are harmless — they sort to the end and contribute no cells — so a
composition with a zero part, which the Garnir splitting produces whenever `j = 0`,
needs no special handling. -/
def ofComposition (l : List ℕ) : YoungDiagram :=
  YoungDiagram.ofRowLens (sortDesc l) (sortDesc_sorted l)

/-- On a weakly-decreasing list the entries exceeding `m` form an initial segment, so
"index `i` has an entry exceeding `m`" and "`i` is below the count of such entries"
are the same condition.

This is the only place sortedness is used; everything downstream is `countP`. -/
theorem lt_countP_iff_of_sorted :
    ∀ {w : List ℕ}, List.Sorted (· ≥ ·) w → ∀ (m i : ℕ),
      (i < w.countP (fun x => decide (m < x)) ↔ ∃ h : i < w.length, m < w[i]) := by
  intro w
  induction w with
  | nil => intro _ m i; simp
  | cons a t ih =>
    intro hw m i
    have hsorted : List.Sorted (· ≥ ·) t := hw.of_cons
    have hle : ∀ b ∈ t, b ≤ a := fun b hb => List.rel_of_sorted_cons hw b hb
    rw [List.countP_cons]
    by_cases hma : m < a
    · -- `a` is counted; the rest matches the tail, shifted by one
      simp only [hma, decide_true, if_pos]
      cases i with
      | zero => simpa using hma
      | succ k =>
        have := ih hsorted m k
        simp only [List.length_cons, List.getElem_cons_succ]
        constructor
        · intro hk
          obtain ⟨h, hlt⟩ := this.mp (by omega)
          exact ⟨by omega, hlt⟩
        · rintro ⟨h, hlt⟩
          have := this.mpr ⟨by omega, hlt⟩
          omega
    · -- `a` is not counted, and by sortedness neither is anything after it
      have htail : t.countP (fun x => decide (m < x)) = 0 := by
        rw [List.countP_eq_zero]
        intro b hb
        simp only [decide_eq_true_eq, not_lt]
        exact le_trans (hle b hb) (not_lt.mp hma)
      have hdec : decide (m < a) = false := by simpa using hma
      rw [hdec, htail]
      simp only [Bool.false_eq_true, if_false, Nat.zero_add]
      constructor
      · intro h
        exact absurd h (Nat.not_lt_zero i)
      · rintro ⟨h, hlt⟩
        exfalso
        cases i with
        | zero =>
          simp only [List.getElem_cons_zero] at hlt
          omega
        | succ k =>
          simp only [List.getElem_cons_succ] at hlt
          have hk : k < t.length := by simpa using h
          have hak : t[k] ≤ a := hle _ (List.getElem_mem hk)
          omega

/-- **The bridge.**  A composition's diagram has, in column `m`, exactly as many cells
as the composition has parts exceeding `m`.

The right-hand side does not mention the sort, and `countP` is permutation-invariant,
so this is a fact about the composition as written. -/
theorem colLen_ofComposition (l : List ℕ) (m : ℕ) :
    (ofComposition l).colLen m = l.countP (fun x => decide (m < x)) := by
  refine eq_of_lt_iff fun i => ?_
  rw [← YoungDiagram.mem_iff_lt_colLen, ofComposition, YoungDiagram.mem_ofRowLens,
    ← (sortDesc_perm l).countP_eq (fun x => decide (m < x))]
  exact (lt_countP_iff_of_sorted (sortDesc_sorted l) m i).symm

/-! ## The round trip, so the bridge applies to any diagram

`colLen_ofComposition` speaks about a diagram *built* from a list.  A Garnir step
starts from an existing `μ`, so it needs the same statement about `μ` itself — which
follows once sorting an already-sorted list is seen to do nothing.
-/

/-- Sorting a weakly-decreasing list does nothing. -/
theorem sortDesc_eq_self {l : List ℕ} (hl : List.Sorted (· ≥ ·) l) : sortDesc l = l :=
  List.eq_of_perm_of_sorted (sortDesc_perm l) (sortDesc_sorted l) hl

/-- Reading a diagram's row lengths back as a composition returns the diagram. -/
theorem ofComposition_rowLens (μ : YoungDiagram) : ofComposition μ.rowLens = μ := by
  unfold ofComposition
  simp only [sortDesc_eq_self μ.rowLens_sorted]
  exact YoungDiagram.ofRowLens_to_rowLens_eq_self

/-- **The bridge, for an arbitrary diagram**: column `m` is as tall as the diagram has
rows longer than `m`.

This is the form `PartitionLex.lexGt_of_colLen` consumes: both of its hypotheses
become counting statements about `μ.rowLens`, and the Garnir list differs from that
in three entries. -/
theorem colLen_eq_countP_rowLens (μ : YoungDiagram) (m : ℕ) :
    μ.colLen m = μ.rowLens.countP (fun x => decide (m < x)) := by
  conv_lhs => rw [← ofComposition_rowLens μ]
  exact colLen_ofComposition _ _

/-! ## Non-vacuity

The bridge would compile just as well if `ofComposition` produced something unrelated
to the parts it was handed, so it is checked against the Garnir composition that made
the whole order question concrete: `λ = (3,3)` at node `(0,1)` gives the composition
`(1, 4, 1)`, whose diagram is `(4,1,1)`.
-/

/-- `(1,4,1)` has exactly one part above `3`, so its diagram's column `3` has one cell
— the `4` that makes `(4,1,1)` lex-greater than `(3,3)`. -/
theorem colLen_ofComposition_garnir_example :
    (ofComposition [1, 4, 1]).colLen 3 = 1 := by
  rw [colLen_ofComposition]
  decide

/-- …and nothing above `4`, which is the other hypothesis `lexGt_of_colLen` wants. -/
theorem colLen_ofComposition_garnir_example_high :
    (ofComposition [1, 4, 1]).colLen 4 = 0 := by
  rw [colLen_ofComposition]
  decide

/-- Subtracting the count of row lengths strictly exceeding m from the m-th column length yields zero. -/
theorem colLen_sub_countP_rowLens_eq_zero (μ : YoungDiagram) (m : ℕ) :
    μ.colLen m - μ.rowLens.countP (fun x => decide (m < x)) = 0 := by
  rw [colLen_eq_countP_rowLens, Nat.sub_self]

end QOU.BraidKnot.PartitionOfComposition
