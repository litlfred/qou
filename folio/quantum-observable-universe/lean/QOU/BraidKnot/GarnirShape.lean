import QOU.BraidKnot.PartitionOfComposition

/-!
# The Garnir shape, and that it is lex-greater

Mathas' Lemma 3.12 (*Hecke algebras and Schur algebras of the symmetric group*)
attaches to a Garnir node `(i, j)` of `λ` the composition

    ν = (λ₀, …, λᵢ₋₁,  j,  λᵢ + 1,  λᵢ₊₁ − j − 1,  λᵢ₊₂, …)

— rows `i` and `i+1` split at column `j` and rejoined — and asserts that its
partition is **lex-greater** than `λ`.

This file proves that, and the whole argument is counting.  Two inputs do the work:

* `PartitionOfComposition.colLen_ofComposition` — a composition's column lengths are
  its part counts, so nothing here ever looks at the sorted list;
* `PartitionLex.lexGt_of_colLen` — a lex step follows from two column-length facts,
  with the witness named.

So the proof reduces to: the three new parts contribute exactly one part above
`λᵢ` that the two old parts did not, and nothing at all above that.

## Why it is lex and not dominance

Dominance **fails** here, measured 86 times in 910 Garnir nodes, the smallest case
being `λ = (3,3)` at `(0,1)` — see
[`garnir_shape_dominance_probe.py`](../../../../../computations/hecke/garnir_shape_dominance_probe.py)
and `PartitionLex.dom_fails_lex_holds`.  Mathas says which order he means in the
sentence before the lemma; it is the weaker one, and it is also the **total** one,
which is what makes the straightening recursion well-founded.
-/

namespace QOU.BraidKnot.GarnirShape

open QOU.BraidKnot.PartitionLex QOU.BraidKnot.PartitionOfComposition

/-- Splitting a list's count at two consecutive positions.

`countP` is additive over `++`, and `drop` peels one entry at a time, so a list's
count is its count outside a two-entry window plus the two entries' own
contributions.  Both the original shape and the Garnir composition are read this
way, and they share the two outer summands verbatim. -/
theorem countP_split_two (p : ℕ → Bool) (l : List ℕ) (i : ℕ) (h : i + 1 < l.length) :
    l.countP p = (l.take i).countP p + (l.drop (i + 2)).countP p
      + (if p l[i] then 1 else 0) + (if p l[i + 1] then 1 else 0) := by
  have hi : i < l.length := by omega
  conv_lhs => rw [← List.take_append_drop i l]
  rw [List.countP_append, List.drop_eq_getElem_cons hi, List.countP_cons,
    List.drop_eq_getElem_cons h, List.countP_cons, show i + 1 + 1 = i + 2 from rfl]
  omega

variable {μ : YoungDiagram} {i j : ℕ}

/-- **Mathas' Garnir composition**, as a list of parts. -/
def garnirComp (μ : YoungDiagram) (i j : ℕ) : List ℕ :=
  μ.rowLens.take i ++ [j, μ.rowLen i + 1, μ.rowLen (i + 1) - j - 1]
    ++ μ.rowLens.drop (i + 2)

/-- **The Garnir shape**: the partition of that composition. -/
def garnirShape (μ : YoungDiagram) (i j : ℕ) : YoungDiagram :=
  ofComposition (garnirComp μ i j)

/-- A Garnir node makes row `i+1` non-empty, so both rows are inside `rowLens`. -/
theorem succ_lt_length_rowLens (h : (i + 1, j) ∈ μ) : i + 1 < μ.rowLens.length := by
  rw [YoungDiagram.length_rowLens]
  exact YoungDiagram.mem_iff_lt_colLen.mp (μ.up_left_mem le_rfl (Nat.zero_le j) h)

/-- The count of `garnirComp` splits into the shared outer part and the three new
entries; the shared part is the same one `μ.rowLens` contributes. -/
theorem countP_garnirComp (p : ℕ → Bool) :
    (garnirComp μ i j).countP p
      = (μ.rowLens.take i).countP p + (μ.rowLens.drop (i + 2)).countP p
        + ((if p j then 1 else 0) + (if p (μ.rowLen i + 1) then 1 else 0)
          + (if p (μ.rowLen (i + 1) - j - 1) then 1 else 0)) := by
  simp only [garnirComp, List.countP_append, List.countP_cons, List.countP_nil]
  omega

/-- The two column-length facts `lexGt_of_colLen` wants, at the threshold `λᵢ`.

Above `λᵢ` nothing changes: the three new parts are `j ≤ λᵢ₊₁ − 1 ≤ λᵢ`,
`λᵢ + 1`, and `λᵢ₊₁ − j − 1 ≤ λᵢ`, and the two they replace are `λᵢ` and `λᵢ₊₁` —
so for a threshold `m > λᵢ` every one of the five is at most `m`, except `λᵢ + 1`,
which is at most `m` too.  At `m = λᵢ` exactly one of the five clears the bar, and
it is `λᵢ + 1`. -/
theorem colLen_garnirShape_of_lt (h : (i + 1, j) ∈ μ) {m : ℕ} (hm : μ.rowLen i < m) :
    μ.colLen m = (garnirShape μ i j).colLen m := by
  have hj : j < μ.rowLen (i + 1) := YoungDiagram.mem_iff_lt_rowLen.mp h
  have hanti : μ.rowLen (i + 1) ≤ μ.rowLen i := μ.rowLen_anti i (i + 1) (by omega)
  have hlen := succ_lt_length_rowLens h
  rw [colLen_eq_countP_rowLens, garnirShape, colLen_ofComposition,
    countP_split_two _ _ i hlen, countP_garnirComp]
  rw [YoungDiagram.get_rowLens, YoungDiagram.get_rowLens]
  -- every one of the five parts is at most `m`, so no `if` fires on either side
  have e1 : ¬ (m < j) := by omega
  have e2 : ¬ (m < μ.rowLen i + 1) := by omega
  have e3 : ¬ (m < μ.rowLen (i + 1) - j - 1) := by omega
  have e4 : ¬ (m < μ.rowLen i) := by omega
  have e5 : ¬ (m < μ.rowLen (i + 1)) := by omega
  simp only [e1, e2, e3, e4, e5, if_false, Bool.false_eq_true, decide_false]

/-- At the threshold `λᵢ` the Garnir shape has exactly one more part above it. -/
theorem colLen_garnirShape_at (h : (i + 1, j) ∈ μ) :
    μ.colLen (μ.rowLen i) < (garnirShape μ i j).colLen (μ.rowLen i) := by
  have hj : j < μ.rowLen (i + 1) := YoungDiagram.mem_iff_lt_rowLen.mp h
  have hanti : μ.rowLen (i + 1) ≤ μ.rowLen i := μ.rowLen_anti i (i + 1) (by omega)
  have hlen := succ_lt_length_rowLens h
  rw [colLen_eq_countP_rowLens, garnirShape, colLen_ofComposition,
    countP_split_two _ _ i hlen, countP_garnirComp]
  rw [YoungDiagram.get_rowLens, YoungDiagram.get_rowLens]
  have e1 : ¬ (μ.rowLen i < j) := by omega
  have e2 : μ.rowLen i < μ.rowLen i + 1 := by omega
  have e3 : ¬ (μ.rowLen i < μ.rowLen (i + 1) - j - 1) := by omega
  have e4 : ¬ (μ.rowLen i < μ.rowLen i) := by omega
  have e5 : ¬ (μ.rowLen i < μ.rowLen (i + 1)) := by omega
  simp only [e1, e2, e3, e4, e5, if_false, if_true, Bool.false_eq_true,
    decide_false, decide_true]
  omega

/-- **Mathas' Lemma 3.12, shape half.**  The Garnir shape is lex-greater than `μ`.

The witness is `μ.colLen (μ.rowLen i)` — the number of rows longer than row `i` —
which is the `c = #{r : λ_r > λᵢ}` measured 1435/1435 by the probe, and is **not**
the Garnir row `i`: at `λ = (2,2,2)` with node `(1,0)` the shape moves at row `0`,
because the merged part overtakes the rows above `i` that tie with `λᵢ`. -/
theorem garnirShape_lexGt (h : (i + 1, j) ∈ μ) : garnirShape μ i j >ₗ μ :=
  lexGt_of_colLen (fun _ hm => colLen_garnirShape_of_lt h hm) (colLen_garnirShape_at h)

/-! ## Non-vacuity

`garnirShape_lexGt` carries a hypothesis, and a theorem whose hypothesis nothing
satisfies proves nothing.  It is met by the shape that made the order question
concrete in the first place: `λ = (3,3)` has a cell at `(1,1)`, so `(i, j) = (0, 1)`
is a Garnir node of it.

That is the same node whose composition `(1, 4, 1)` sorts to `(4,1,1)` — the pair
`PartitionLex.dom_fails_lex_holds` uses to show dominance fails.  What is checked
here is that the hypothesis is satisfiable and the theorem fires, **not** that
`garnirShape lam33 0 1` is definitionally `nu411`: `lam33.rowLens` does not reduce
(`decide` gets stuck on `hasDecEq`), so identifying the two shapes would need a
separate argument and is not claimed. -/
theorem garnirShape_lexGt_example : garnirShape lam33 0 1 >ₗ lam33 :=
  garnirShape_lexGt (by rw [YoungDiagram.mem_iff_lt_rowLen, rowLen_lam33_one]; omega)

end QOU.BraidKnot.GarnirShape
