import QOU.Mathlib.RSKBurnsideTarget
import QOU.Mathlib.SchenstedSYTRoundTrip

/-!
# QOU.Mathlib.SchenstedPartitionShape — partitions of `n` are the Young diagrams with `n` cells

Brick 41 of epic `qou-nrex` (RSK inverse).

Brick 40 gives the correspondence as an `Equiv` onto
`{X : Σ μ, SYT μ × SYT μ // X.1.cells.card = n}`. `RSKBurnsideHolds n` is indexed by
`Nat.Partition n`, not by `YoungDiagram`, so the two do not meet until that index is identified:

**`partitionShapeEquiv n : Nat.Partition n ≃ {μ : YoungDiagram // μ.cells.card = n}`**

The `cells.card` side needs a lemma the corpus did not have and Mathlib does not either — a Young
diagram has as many cells as its row lengths sum to. `card_cells_ofRowLens` proves it from the
pieces `SchenstedCellsBridge` already built for the *content* bridge: the cells are the disjoint
union of the rows (`cells_biUnion`, `rows_pairwiseDisjoint`) and a row is a product with a range
(`row_eq_prod`). The content bridge itself is stated only for a `tableauShape`; these pieces are
general, and this is the general consequence.

The rest is the sorted-list round trip. A partition's shape remembers its parts because
`rowLens_ofRowLens_eq_self` returns the sorted list, and sorting is injective on multisets; a
diagram is a partition's shape because its own `rowLens` is already sorted, and sorting a sorted
list returns it (`sort_coe_of_sorted`, via `List.eq_of_perm_of_sorted`).

## Scope

The index bridge. `RSKBurnsideHolds` for general `n` needs one more step past it — the `Σ`-card
decomposition `Nat.card {X // X.1.cells.card = n} = ∑ p, (dimSYT p)^2` — and is not proved here. It
remains proved only for `n ≤ 12`, by `rskBurnsideHolds_le12`, a route with no RSK correspondence in
it.

Pure combinatorics on `ℕ`; nothing archimedean; no fit.

**Scope note superseded (2026-08-23).** The scope paragraph above records the state of the arc when
this brick landed. `RSKBurnsideHolds` is now proved for **every** `n`
(`QOU.Mathlib.rskBurnsideHolds`, brick 42), and `SnIsotypicSpechtSplit` is inhabited, so any
statement here that they "remain open" or hold "only for `n ≤ 12`" describes history rather than the
corpus. The per-brick scope is otherwise unchanged and still accurate.

-/

namespace QOU.Mathlib

open YoungDiagram Finset

/-- Indexed sum over a list's positions is its sum. -/
theorem sum_range_getD_nat : ∀ (l : List ℕ), ∑ i ∈ Finset.range l.length, l.getD i 0 = l.sum
  | [] => by simp
  | a :: t => by
      rw [List.length_cons, Finset.sum_range_succ', List.sum_cons]
      simp only [List.getD_cons_succ, List.getD_cons_zero]
      rw [sum_range_getD_nat t]
      omega

/-- **A Young diagram has as many cells as its row lengths sum to.** The cells are the disjoint
union of the rows, and a row is a singleton times a range. -/
theorem card_cells_ofRowLens (L : List ℕ) (hsort : L.Sorted (· ≥ ·)) :
    (ofRowLens L hsort).cells.card = L.sum := by
  rw [QOU.Mathlib.Schensted.cells_biUnion L hsort,
    Finset.card_biUnion (fun i hi i' hi' hne =>
      QOU.Mathlib.Schensted.rows_pairwiseDisjoint _ L.length (by simpa using hi)
        (by simpa using hi') hne)]
  rw [← sum_range_getD_nat L]
  refine Finset.sum_congr rfl (fun i _ => ?_)
  rw [row_eq_prod, Finset.card_product, Finset.card_singleton, Finset.card_range, one_mul,
    QOU.Mathlib.Schensted.rowLen_getD]

/-- A diagram's cell count is the sum of its own row lengths. -/
theorem card_cells_eq_rowLens_sum (μ : YoungDiagram) : μ.cells.card = μ.rowLens.sum := by
  conv_lhs => rw [← ofRowLens_to_rowLens_eq_self (μ := μ)]
  exact card_cells_ofRowLens μ.rowLens μ.rowLens_sorted

/-- Sorting an already-sorted list returns it. -/
theorem sort_coe_of_sorted {l : List ℕ} (h : l.Sorted (· ≥ ·)) :
    (↑l : Multiset ℕ).sort (· ≥ ·) = l :=
  List.eq_of_perm_of_sorted
    (Multiset.coe_eq_coe.mp (Multiset.sort_eq (· ≥ ·) (↑l : Multiset ℕ)))
    (Multiset.sort_sorted _ _) h

variable {n : ℕ}

/-- **A partition's shape has `n` cells.** -/
theorem partitionShape_card (p : Nat.Partition n) : (partitionShape p).cells.card = n := by
  rw [partitionShape, card_cells_ofRowLens]
  have hcoe : ((Multiset.sort (· ≥ ·) p.parts : List ℕ)).sum
      = ((↑(Multiset.sort (· ≥ ·) p.parts) : Multiset ℕ)).sum := rfl
  rw [hcoe, Multiset.sort_eq, p.parts_sum]

/-- **A partition is determined by its shape**: the shape returns the sorted parts, and sorting is
injective on multisets. -/
theorem partitionShape_injective : Function.Injective (partitionShape (n := n)) := by
  intro p q h
  have hp : (partitionShape p).rowLens = p.parts.sort (· ≥ ·) :=
    rowLens_ofRowLens_eq_self (fun x hx => p.parts_pos ((Multiset.mem_sort _).mp hx))
  have hq : (partitionShape q).rowLens = q.parts.sort (· ≥ ·) :=
    rowLens_ofRowLens_eq_self (fun x hx => q.parts_pos ((Multiset.mem_sort _).mp hx))
  have hsort : p.parts.sort (· ≥ ·) = q.parts.sort (· ≥ ·) := by rw [← hp, ← hq, h]
  refine Nat.Partition.ext ?_
  rw [← Multiset.sort_eq (· ≥ ·) p.parts, ← Multiset.sort_eq (· ≥ ·) q.parts, hsort]

/-- **Every diagram with `n` cells is a partition's shape**: its own row lengths are the parts. -/
theorem exists_partitionShape_eq (μ : YoungDiagram) (h : μ.cells.card = n) :
    ∃ p : Nat.Partition n, partitionShape p = μ := by
  refine ⟨⟨(↑μ.rowLens : Multiset ℕ), fun {i} hi => μ.pos_of_mem_rowLens i (by simpa using hi), ?_⟩,
    ?_⟩
  · rw [show ((↑μ.rowLens : Multiset ℕ)).sum = μ.rowLens.sum from rfl,
      ← card_cells_eq_rowLens_sum, h]
  · exact (QOU.Mathlib.Schensted.ofRowLens_congr _ μ.rowLens_sorted
      (sort_coe_of_sorted μ.rowLens_sorted)).trans ofRowLens_to_rowLens_eq_self

/-- **Partitions of `n` are exactly the Young diagrams with `n` cells.** -/
noncomputable def partitionShapeEquiv (n : ℕ) :
    Nat.Partition n ≃ {μ : YoungDiagram // μ.cells.card = n} :=
  Equiv.ofBijective (fun p => ⟨partitionShape p, partitionShape_card p⟩)
    ⟨fun _ _ h => partitionShape_injective (Subtype.ext_iff.mp h), by
      rintro ⟨μ, hμ⟩
      obtain ⟨p, hp⟩ := exists_partitionShape_eq μ hμ
      exact ⟨p, Subtype.ext hp⟩⟩

@[simp] theorem partitionShapeEquiv_apply (n : ℕ) (p : Nat.Partition n) :
    ((partitionShapeEquiv n p : {μ : YoungDiagram // μ.cells.card = n}) : YoungDiagram)
      = partitionShape p := rfl

end QOU.Mathlib
