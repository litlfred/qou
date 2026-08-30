import QOU.Mathlib.YoungDiagramAddCell
import QOU.Mathlib.SYTBranchingRule

/-!
# `QOU.Mathlib.YoungLatticeUpOperator` — the up-operator identity on SYT counts

The target is

    ∑_{λ = μ + one addable cell}  f^λ  =  (|μ| + 1) · f^μ,                      (UP)

the **up** half of Young's lattice being a `1`-differential poset.  `QOU.Mathlib.SYTBranchingRule`
supplies the **down** half (`numStandardYoungTableaux_branching`), and
`QOU.Mathlib.YoungLatticeCornerCount` shows that (UP) is exactly what is still needed to close

    ∑_{λ ⊢ n} f^λ = I(n)                                (the involution numbers, bean `qou-jlam`).

## The route, and why it is not the operator-algebra one

The textbook derivation puts `D U = U D + I` on the free module `ℚ[Young]` and reads (UP) off
`D U^{m+1} ∅ = (m+1) U^m ∅`.  That needs the **off-diagonal** of `DU − UD = I` — a statement about
*pairs* of diagrams — plus the free-module setup.  This file avoids both: it proves (UP) directly,
by strong induction on `|μ|`, from three ingredients that are already in the corpus or are pure row
arithmetic.

Writing `A(μ)` for the addable cells, `C(μ)` for the removable corners, `a(μ) = |A(μ)|`,
`r(μ) = |C(μ)|`, and expanding each `f^{μ+s}` by the branching rule:

    upSum μ  =  ∑_{s ∈ A(μ)} f^{μ+s}
             =  ∑_{s ∈ A(μ)}  ∑_{c ∈ C(μ+s)} f^{(μ+s) ∖ c}
             =  a(μ)·f^μ  +  ∑_{s ∈ A(μ)} ∑_{c ∈ C(μ+s), c ≠ s} f^{(μ ∖ c) + s}

— the split is by whether the corner removed is the cell just added.  The double sum is then
**transposed**, which is what `isCornerCell_addCell_iff` below is for: it identifies the two
index sets

    {(s, c) : s ∈ A(μ), c ∈ C(μ + s), c ≠ s}  =  {(s, c) : c ∈ C(μ), s ∈ A(μ ∖ c), s ≠ c}.

Applying the induction hypothesis to each `μ ∖ c` (which has `|μ| − 1` cells) and the branching
rule once more to `∑_{c ∈ C(μ)} f^{μ∖c} = f^μ` gives

    upSum μ + r(μ)·f^μ  =  a(μ)·f^μ + |μ|·f^μ,

and `a(μ) = r(μ) + 1` (`card_addableCells_eq_card_cornerCells_succ`) turns that into (UP) by
cancelling `r(μ)·f^μ`.  The identity is arranged so that **no `ℕ` subtraction appears** anywhere in
the argument.

## Everything reduces to row lengths

`corner_iff` and `addable_iff` (in `YoungDiagramAddable`) characterise both notions by the row-length
sequence.  So the two structural facts this file needs about insertion and deletion are

    (μ + (a,b)).rowLen i = μ.rowLen i + [i = a],      (μ ∖ (p,q)).rowLen i = μ.rowLen i − [i = p],

after which `isCornerCell_addCell_iff` is a three-case split (`a = p`, `a = p+1`, neither) closed by
`omega`.  That is the whole mathematical content: a corner `c = (p,q)` is destroyed by inserting `s`
exactly when `s` sits directly right of `c` or directly below it, and those are the same two cases in
which `s` fails to be addable to `μ ∖ c`.

Pure combinatorics; nothing archimedean (§7c), no fit, no `ℕ`-subtraction in the counting identity.

## References

- [stanley1999ec2] Enumerative Combinatorics I, §3.21 (differential posets)
-/

namespace QOU.Mathlib

open YoungDiagram Finset

/-! ### Row lengths of `μ + s` and `μ ∖ c` -/

/-- A row length is pinned by its membership predicate: if row `i` of `ν` is exactly `{0, …, k-1}`
then `ν.rowLen i = k`. -/
theorem rowLen_eq_of_mem_iff {ν : YoungDiagram} {i k : ℕ}
    (h : ∀ j, (i, j) ∈ ν ↔ j < k) : ν.rowLen i = k := by
  have h1 : ¬ (ν.rowLen i < k) := by
    intro hlt
    have hm := (h (ν.rowLen i)).mpr hlt
    exact absurd (YoungDiagram.mem_iff_lt_rowLen.mp hm) (lt_irrefl _)
  have h2 : ¬ (k < ν.rowLen i) := by
    intro hlt
    have hm : (i, k) ∈ ν := YoungDiagram.mem_iff_lt_rowLen.mpr hlt
    exact absurd ((h k).mp hm) (lt_irrefl _)
  omega

/-- Inserting `(a, b)` lengthens row `a` by one and leaves every other row alone. -/
theorem rowLen_addCell (μ : YoungDiagram) (a b : ℕ) (h : IsAddableCell μ (a, b)) (i : ℕ) :
    (addCell μ (a, b) h).rowLen i = if i = a then μ.rowLen i + 1 else μ.rowLen i := by
  have hb : b = μ.rowLen a := ((addable_iff μ a b).mp h).1
  by_cases hi : i = a
  · subst hi
    rw [if_pos rfl]
    refine rowLen_eq_of_mem_iff (fun j => ?_)
    rw [mem_addCell]
    simp only [Prod.mk.injEq, true_and]
    rw [YoungDiagram.mem_iff_lt_rowLen]
    omega
  · rw [if_neg hi]
    refine rowLen_eq_of_mem_iff (fun j => ?_)
    rw [mem_addCell]
    simp only [Prod.mk.injEq]
    rw [YoungDiagram.mem_iff_lt_rowLen]
    constructor
    · rintro (⟨h1, -⟩ | h2)
      · exact absurd h1 hi
      · exact h2
    · exact fun hj => Or.inr hj

/-- Deleting the corner `(p, q)` shortens row `p` by one and leaves every other row alone. -/
theorem rowLen_eraseCorner (μ : YoungDiagram) (a b : ℕ) (h : IsCornerCell μ (a, b)) (i : ℕ) :
    (eraseCorner μ (a, b) h).rowLen i = if i = a then μ.rowLen i - 1 else μ.rowLen i := by
  have hb : μ.rowLen a = b + 1 := ((corner_iff μ a b).mp h).1
  by_cases hi : i = a
  · subst hi
    rw [if_pos rfl]
    refine rowLen_eq_of_mem_iff (fun j => ?_)
    rw [mem_eraseCorner]
    simp only [ne_eq, Prod.mk.injEq, true_and]
    rw [YoungDiagram.mem_iff_lt_rowLen]
    omega
  · rw [if_neg hi]
    refine rowLen_eq_of_mem_iff (fun j => ?_)
    rw [mem_eraseCorner]
    simp only [ne_eq, Prod.mk.injEq, not_and]
    rw [YoungDiagram.mem_iff_lt_rowLen]
    constructor
    · rintro ⟨h1, -⟩; exact h1
    · exact fun hj => ⟨hj, fun hc => absurd hc hi⟩

/-! ### The corner-survival correspondence

This is the transposition lemma for the double sum, and the only place where the geometry of the
Young lattice actually enters. -/

/-- **A corner survives an insertion exactly when the inserted cell was addable to the diagram with
that corner removed.**

Concretely: inserting `s` destroys the corner `c` precisely when `s` is `c`'s right neighbour or
`c`'s lower neighbour, and those are exactly the two positions at which `s` fails to be addable to
`μ ∖ c`.  The proof is the three-case split `a = p` / `a = p + 1` / neither on the row indices. -/
theorem isCornerCell_addCell_iff (μ : YoungDiagram) (a b p q : ℕ)
    (hs : IsAddableCell μ (a, b)) (hc : IsCornerCell μ (p, q)) :
    IsCornerCell (addCell μ (a, b) hs) (p, q) ↔ IsAddableCell (eraseCorner μ (p, q) hc) (a, b) := by
  obtain ⟨hb, hrow⟩ := (addable_iff μ a b).mp hs
  obtain ⟨hq, hdrop⟩ := (corner_iff μ p q).mp hc
  rw [corner_iff, addable_iff, rowLen_addCell μ a b hs, rowLen_addCell μ a b hs,
    rowLen_eraseCorner μ p q hc, rowLen_eraseCorner μ p q hc]
  by_cases h1 : a = p
  · subst h1
    rw [if_pos rfl, if_pos rfl]
    constructor
    · rintro ⟨hL, -⟩; omega
    · rintro ⟨hR, -⟩; omega
  by_cases h2 : a = p + 1
  · subst h2
    rw [if_neg (by omega : p ≠ p + 1), if_pos rfl, if_neg (by omega : p + 1 ≠ p),
      show p + 1 - 1 = p from rfl, if_pos rfl]
    constructor
    · rintro ⟨-, hL⟩
      exact ⟨hb, Or.inr (by omega)⟩
    · rintro ⟨-, hR⟩
      refine ⟨hq, ?_⟩
      rcases hR with hR | hR
      · omega
      · omega
  · rw [if_neg (by omega : p ≠ a), if_neg (by omega : p + 1 ≠ a), if_neg h1]
    constructor
    · intro _
      refine ⟨hb, ?_⟩
      rcases hrow with h0 | h0
      · exact Or.inl h0
      · rw [if_neg (by omega : a - 1 ≠ p)]
        exact Or.inr h0
    · intro _
      exact ⟨hq, hdrop⟩

/-! ### The two one-directional transfers

`isCornerCell_addCell_iff` is stated for `s` addable to `μ` *and* `c` a corner of `μ`.  These two
lemmas supply the hypotheses from the other side, so that the two index sets of the double sum are
literally the same subset of `A(μ) ×ˢ C(μ)`. -/

variable {μ : YoungDiagram}

/-- A corner of `μ + s` other than `s` itself was already a corner of `μ`. -/
theorem isCornerCell_of_addCell {s c : ℕ × ℕ} (hs : IsAddableCell μ s)
    (h : IsCornerCell (addCell μ s hs) c) (hne : c ≠ s) : IsCornerCell μ c := by
  obtain ⟨h1, h2, h3⟩ := h
  rw [mem_addCell] at h1 h2 h3
  exact ⟨h1.resolve_left hne, fun hm => h2 (Or.inr hm), fun hm => h3 (Or.inr hm)⟩

/-- A cell addable to `μ ∖ c`, other than `c` itself, is addable to `μ`. -/
theorem isAddableCell_of_eraseCorner (a b p q : ℕ) (hc : IsCornerCell μ (p, q))
    (hs : IsAddableCell (eraseCorner μ (p, q) hc) (a, b)) (hne : (a, b) ≠ (p, q)) :
    IsAddableCell μ (a, b) := by
  obtain ⟨hq, hdrop⟩ := (corner_iff μ p q).mp hc
  rw [addable_iff, rowLen_eraseCorner μ p q hc, rowLen_eraseCorner μ p q hc] at hs
  obtain ⟨hb, hrow⟩ := hs
  rw [addable_iff]
  by_cases h1 : a = p
  · subst h1
    rw [if_pos rfl] at hb
    have hbq : b = q := by omega
    exact absurd (by rw [hbq]) hne
  rw [if_neg h1] at hb hrow
  refine ⟨hb, ?_⟩
  rcases hrow with h0 | h0
  · exact Or.inl h0
  by_cases h2 : a - 1 = p
  · rw [if_pos h2] at h0
    exact Or.inr (by omega)
  · rw [if_neg h2] at h0
    exact Or.inr h0

/-- Insertion and corner removal commute at distinct cells: `(μ + s) ∖ c = (μ ∖ c) + s`. -/
theorem eraseCorner_addCell_comm {s c : ℕ × ℕ} (hs : IsAddableCell μ s)
    (hc : IsCornerCell (addCell μ s hs) c) (hne : c ≠ s)
    (hc' : IsCornerCell μ c) (hs' : IsAddableCell (eraseCorner μ c hc') s) :
    eraseCorner (addCell μ s hs) c hc = addCell (eraseCorner μ c hc') s hs' := by
  ext x
  simp only [YoungDiagram.mem_cells, mem_eraseCorner, mem_addCell]
  constructor
  · rintro ⟨hx | hx, hne'⟩
    · exact Or.inl hx
    · exact Or.inr ⟨hx, hne'⟩
  · rintro (rfl | ⟨hx, hxc⟩)
    · exact ⟨Or.inl rfl, Ne.symm hne⟩
    · exact ⟨Or.inr hx, hxc⟩

/-! ### Total versions, and the branching rule as a `Finset` sum -/

/-- **`eraseCorner` made total in the cell**, the mirror of `addCellOrSelf`.  A summand quantified
over a `Finset` of cells cannot mention `eraseCorner ν c hc`, which needs the corner proof. -/
noncomputable def eraseCornerOrSelf (ν : YoungDiagram) (c : ℕ × ℕ) : YoungDiagram :=
  if h : IsCornerCell ν c then eraseCorner ν c h else ν

@[simp] theorem eraseCornerOrSelf_of {ν : YoungDiagram} {c : ℕ × ℕ} (h : IsCornerCell ν c) :
    eraseCornerOrSelf ν c = eraseCorner ν c h := dif_pos h

/-- The branching rule, restated as a sum over the `Finset` `cornerCells μ`. -/
theorem branching_finset (μ : YoungDiagram) (hμ : 0 < μ.cells.card) :
    numStandardYoungTableaux μ
      = ∑ c ∈ cornerCells μ, numStandardYoungTableaux (eraseCornerOrSelf μ c) := by
  rw [numStandardYoungTableaux_branching hμ, ← Finset.sum_coe_sort (cornerCells μ)]
  refine Fintype.sum_equiv (Equiv.subtypeEquivRight (fun c => (mem_cornerCells μ c).symm)) _ _ ?_
  intro c
  rw [show ((Equiv.subtypeEquivRight (fun x => (mem_cornerCells μ x).symm)) c : ℕ × ℕ) = (c : ℕ × ℕ)
      from rfl, eraseCornerOrSelf_of c.2]

end QOU.Mathlib
