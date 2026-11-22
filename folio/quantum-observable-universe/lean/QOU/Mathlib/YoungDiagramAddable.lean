import Mathlib.Combinatorics.Young.YoungDiagram
import QOU.Mathlib.YoungDiagramCorner

/-!
# `QOU.Mathlib.YoungDiagramAddable` — addable cells, and `#addable = #removable + 1`

`QOU/Mathlib/YoungDiagramCorner.lean` supplies **removable** corners (`IsCornerCell`,
`eraseCorner`) — the cells whose deletion leaves a Young diagram. This file supplies the
mirror notion, the **addable** cells whose *insertion* leaves a Young diagram, and proves
the counting relation between the two:

    #{addable cells of μ} = #{removable corners of μ} + 1

for **every** Young diagram `μ`, the empty one included.

## Why this identity

It is the diagonal of the `DU − UD = I` relation of Stanley's differential-poset
formulation of the Young lattice, and `DU − UD = I` is what `QOU/Mathlib/BurnsideViaBranching.lean`
needs in order to discharge its remaining hypothesis `hup`
(`Σ_{λ ⊐ μ} f^λ = n · f^μ`), the last obligation on the RSK-free route to

    Σ_{λ ⊢ n} (f^λ)² = n!    (bean `qou-wtny`, SW-3).

That file's companion hypothesis `hdown` is already discharged in the corpus by
`QOU.Mathlib.numStandardYoungTableaux_branching`. **This file does not close `hup`** —
see §"What this does not do" below, which states precisely what is still missing.

## The proof

Both sets are reindexed by their **row**, after which the identity is a shift by one.
Writing `r i := μ.rowLen i`:

* `(i, j)` is a removable corner  ⟺  `r i = j + 1` and `r (i+1) < r i`   (`corner_iff`);
* `(i, j)` is an addable cell     ⟺  `j = r i` and (`i = 0` or `r i < r (i-1)`) (`addable_iff`).

So removable corners biject with `R = {i | r (i+1) < r i}` and addable cells with
`A = {0} ∪ {i+1 | i ∈ R}` — the disjoint union of a single extra element with a shifted
copy of `R` (`addableRows_eq`). Hence `#A = #R + 1`. Row `0` is always addable (one may
always start a new first row); every *other* addable row is the row directly below a
removable corner, and conversely.

Both index sets are cut out of a `Finset` because `r i = 0` once `i ≥ μ.colLen 0`
(`rowLen_pos_iff`), so only finitely many rows can carry either kind of cell.

## `IsAddableCell` is proved to be the right notion, not asserted

`IsAddableCell` is stated as a concrete condition on neighbours (`c ∉ μ`, and each of `c`'s
up/left neighbours is in `μ` or off the board). On its own that is a *definition*, and a
definition cannot be wrong — so it is backed by `addCell`, which **constructs the Young
diagram** `μ ∪ {c}` from it, discharging the `IsLowerSet` obligation. That is what makes
`IsAddableCell` mean "can actually be added" rather than merely naming a predicate.
`card_addCell` records that the construction does add exactly one cell.

## What this does not do

`hup` needs the full `DU − UD = I`, i.e. also the **off-diagonal**: for `μ ≠ ν` of the same
size, `#{λ | λ ⊐ μ, λ ⊐ ν} = #{κ | κ ↗ μ, κ ↗ ν}` (both are `1` when `μ` and `ν` differ by
moving a single cell, and `0` otherwise). That is a statement about *pairs* of diagrams and
is untouched here. The induction assembling diagonal + off-diagonal + `hdown` into `hup` is
also not done. Per AGENTS.md §"Axiomatization is NOT a Proof", this file proves one lemma;
it does not license treating `hup` as established.

## Sanity check

On `μ = (3,2,2)` the file's own definitions evaluate to `#cornerCells = 2` and
`#addableCells = 3`, matching the hand count — corners `(0,2)` and `(2,1)`; addable cells
`(0,3)`, `(1,2)` and `(3,0)`. Both sides are non-empty, so the identity here is not the
vacuous `0 = 0 + 1`-style statement an unguarded cardinality equation can degenerate into.

Recorded honestly: that is an `#eval` (compiler) check, **not** a kernel-checked theorem.
`decide` does not close it — reduction gets stuck on `YoungDiagram.ofRowLens` — and
`native_decide` is banned by AGENTS.md §"Strict Lean Discipline" item 6, so no concrete
instance is pinned as a regression test. What *is* kernel-checked is stronger in the
direction that matters: `mem_addableCells` and `mem_cornerCells` prove the two `Finset`s
are exactly the addable cells and the removable corners, so the identity is a statement
about the genuine sets rather than about two conveniently-chosen images.

## Base ring

None — the whole file is `ℕ`-valued counting on `Finset`s. Nothing archimedean, no fit.

-- Ref: [stanley1999] https://doi.org/10.1017/CBO9780511609589
-- Ref: [leitner2026] QOU/Mathlib/BurnsideViaBranching.lean
-/

namespace QOU.Mathlib

open YoungDiagram Finset

variable {μ : YoungDiagram}

/-! ### Rows are eventually empty -/

/-- Row `i` is non-empty exactly when `i` is below the height of the first column. In
particular `μ.rowLen i = 0` for every `i ≥ μ.colLen 0`, which is what makes the row-index
sets below finite. -/
theorem rowLen_pos_iff (μ : YoungDiagram) (i : ℕ) : 0 < μ.rowLen i ↔ i < μ.colLen 0 := by
  constructor
  · intro h; exact YoungDiagram.mem_iff_lt_colLen.mp (YoungDiagram.mem_iff_lt_rowLen.mpr h)
  · intro h; exact YoungDiagram.mem_iff_lt_rowLen.mp (YoungDiagram.mem_iff_lt_colLen.mpr h)

/-! ### Addable cells -/

/-- An **addable cell** of `μ`: a cell outside `μ` whose upper neighbour `(i-1, j)` and left
neighbour `(i, j-1)` each either lie in `μ` or fall off the board. These are exactly the
cells that may be adjoined to `μ` with the result still a Young diagram — see `addCell`. -/
def IsAddableCell (μ : YoungDiagram) (c : ℕ × ℕ) : Prop :=
  c ∉ μ ∧ (c.1 = 0 ∨ (c.1 - 1, c.2) ∈ μ) ∧ (c.2 = 0 ∨ (c.1, c.2 - 1) ∈ μ)

/-- **Cell insertion `μ ∪ {c}`.** Adjoining an addable cell to `μ` yields a Young diagram:
`insert c μ.cells` is still a lower set, because any `b ≤ c` with `b ≠ c` is `≤` one of `c`'s
neighbours, which `IsAddableCell` places in `μ`.

This is what makes `IsAddableCell` a characterisation rather than a bare definition. -/
def addCell (μ : YoungDiagram) (c : ℕ × ℕ) (hc : IsAddableCell μ c) : YoungDiagram where
  cells := insert c μ.cells
  isLowerSet := by
    obtain ⟨-, hup, hleft⟩ := hc
    intro a b hba ha
    simp only [Finset.coe_insert, Set.mem_insert_iff, Finset.mem_coe] at ha ⊢
    by_cases hbc : b = c
    · exact Or.inl hbc
    refine Or.inr ?_
    rcases ha with rfl | ha
    · have h1 : b.1 ≤ a.1 := hba.1
      have h2 : b.2 ≤ a.2 := hba.2
      have hstrict : b.1 < a.1 ∨ b.2 < a.2 := by
        by_contra h; push_neg at h
        exact hbc (Prod.ext_iff.mpr ⟨by omega, by omega⟩)
      rcases hstrict with hlt | hlt
      · have ha1 : ¬ a.1 = 0 := by omega
        have hmem : (a.1 - 1, a.2) ∈ μ := hup.resolve_left ha1
        simpa using μ.up_left_mem (by omega : b.1 ≤ a.1 - 1) h2 hmem
      · have ha2 : ¬ a.2 = 0 := by omega
        have hmem : (a.1, a.2 - 1) ∈ μ := hleft.resolve_left ha2
        simpa using μ.up_left_mem h1 (by omega : b.2 ≤ a.2 - 1) hmem
    · exact μ.isLowerSet hba ha

@[simp] theorem mem_addCell (μ : YoungDiagram) (c x : ℕ × ℕ) (hc : IsAddableCell μ c) :
    x ∈ addCell μ c hc ↔ x = c ∨ x ∈ μ := by
  show x ∈ insert c μ.cells ↔ _
  rw [Finset.mem_insert]; rfl

/-- Adding an addable cell increases the cell count by exactly one. -/
theorem card_addCell (μ : YoungDiagram) (c : ℕ × ℕ) (hc : IsAddableCell μ c) :
    (addCell μ c hc).cells.card = μ.cells.card + 1 := by
  show (insert c μ.cells).card = _
  exact Finset.card_insert_of_notMem hc.1

/-! ### Both notions, reindexed by row -/

/-- A cell is a removable corner exactly when it ends its row and its row is strictly longer
than the next. -/
theorem corner_iff (μ : YoungDiagram) (i j : ℕ) :
    IsCornerCell μ (i, j) ↔ (μ.rowLen i = j + 1 ∧ μ.rowLen (i+1) < μ.rowLen i) := by
  unfold IsCornerCell
  simp only [YoungDiagram.mem_iff_lt_rowLen, not_lt]
  constructor
  · rintro ⟨h1, h2, h3⟩; omega
  · rintro ⟨h1, h2⟩; omega

/-- A cell is addable exactly when it sits just past the end of its row, and that row is
either the first or strictly shorter than the one above. -/
theorem addable_iff (μ : YoungDiagram) (i j : ℕ) :
    IsAddableCell μ (i, j) ↔ (j = μ.rowLen i ∧ (i = 0 ∨ μ.rowLen i < μ.rowLen (i-1))) := by
  unfold IsAddableCell
  simp only [YoungDiagram.mem_iff_lt_rowLen, not_lt]
  constructor
  · rintro ⟨h1, h2, h3⟩
    have hj : j = μ.rowLen i := by rcases h3 with h3 | h3 <;> omega
    refine ⟨hj, ?_⟩
    rcases h2 with h2 | h2
    · exact Or.inl h2
    · exact Or.inr (by omega)
  · rintro ⟨rfl, h2⟩
    refine ⟨le_refl _, ?_, ?_⟩
    · rcases h2 with h2 | h2
      · exact Or.inl h2
      · exact Or.inr h2
    · rcases Nat.eq_zero_or_pos (μ.rowLen i) with h | h
      · exact Or.inl h
      · exact Or.inr (by omega)

/-- The rows that end in a removable corner. -/
def cornerRows (μ : YoungDiagram) : Finset ℕ :=
  (range (μ.colLen 0)).filter (fun i => μ.rowLen (i+1) < μ.rowLen i)

/-- The rows that admit an addable cell. -/
def addableRows (μ : YoungDiagram) : Finset ℕ :=
  (range (μ.colLen 0 + 1)).filter (fun i => i = 0 ∨ μ.rowLen i < μ.rowLen (i-1))

/-- **The shift.** The addable rows are row `0` together with the rows directly below a
removable corner. This is the combinatorial heart of the whole file. -/
theorem addableRows_eq (μ : YoungDiagram) :
    addableRows μ = insert 0 ((cornerRows μ).image (· + 1)) := by
  ext i
  simp only [addableRows, cornerRows, mem_filter, mem_range, mem_insert, mem_image]
  constructor
  · rintro ⟨hlt, h | h⟩
    · exact Or.inl h
    · refine Or.inr ⟨i - 1, ⟨?_, ?_⟩, ?_⟩
      · by_contra hcon
        push_neg at hcon
        have h0 : μ.rowLen (i-1) = 0 := by
          by_contra hne
          exact absurd ((rowLen_pos_iff μ (i-1)).mp (Nat.pos_of_ne_zero hne)) (by omega)
        omega
      · have hi : i ≠ 0 := by rintro rfl; simp at h
        have hs : i - 1 + 1 = i := by omega
        rw [hs]; exact h
      · have hi : i ≠ 0 := by rintro rfl; simp at h
        omega
  · rintro (rfl | ⟨j, ⟨hj, hlt⟩, rfl⟩)
    · exact ⟨by omega, Or.inl rfl⟩
    · refine ⟨by omega, Or.inr ?_⟩
      simpa using hlt

/-- Row count form of the main identity. -/
theorem card_addableRows (μ : YoungDiagram) :
    (addableRows μ).card = (cornerRows μ).card + 1 := by
  rw [addableRows_eq]
  have hinj : Set.InjOn (· + 1) (cornerRows μ) := fun a _ b _ h => by simpa using h
  have hnot : (0 : ℕ) ∉ (cornerRows μ).image (· + 1) := by
    simp only [mem_image, not_exists]
    rintro x ⟨-, h⟩
    omega
  rw [Finset.card_insert_of_notMem hnot, Finset.card_image_of_injOn hinj]

/-! ### Back to cells -/

/-- The removable corners of `μ`, as a `Finset` of cells. Defined as the image of
`cornerRows`; `mem_cornerCells` proves this really is the set of removable corners. -/
def cornerCells (μ : YoungDiagram) : Finset (ℕ × ℕ) :=
  (cornerRows μ).image (fun i => (i, μ.rowLen i - 1))

/-- The addable cells of `μ`, as a `Finset` of cells. Defined as the image of `addableRows`;
`mem_addableCells` proves this really is the set of addable cells. -/
def addableCells (μ : YoungDiagram) : Finset (ℕ × ℕ) :=
  (addableRows μ).image (fun i => (i, μ.rowLen i))

/-- `cornerCells` is the set of removable corners — the definition by image is faithful. -/
@[simp] theorem mem_cornerCells (μ : YoungDiagram) (c : ℕ × ℕ) :
    c ∈ cornerCells μ ↔ IsCornerCell μ c := by
  obtain ⟨i, j⟩ := c
  simp only [cornerCells, mem_image, cornerRows, mem_filter, mem_range, Prod.mk.injEq]
  rw [corner_iff]
  constructor
  · rintro ⟨k, ⟨hk, h2⟩, rfl, rfl⟩
    have hpos : 0 < μ.rowLen k := by omega
    exact ⟨by omega, h2⟩
  · rintro ⟨h1, h2⟩
    exact ⟨i, ⟨(rowLen_pos_iff μ i).mp (by omega), h2⟩, rfl, by omega⟩

/-- `addableCells` is the set of addable cells — the definition by image is faithful. -/
@[simp] theorem mem_addableCells (μ : YoungDiagram) (c : ℕ × ℕ) :
    c ∈ addableCells μ ↔ IsAddableCell μ c := by
  obtain ⟨i, j⟩ := c
  simp only [addableCells, mem_image, addableRows, mem_filter, mem_range, Prod.mk.injEq]
  rw [addable_iff]
  constructor
  · rintro ⟨k, ⟨hk, hd⟩, rfl, rfl⟩
    exact ⟨rfl, hd⟩
  · rintro ⟨rfl, hd⟩
    refine ⟨i, ⟨?_, hd⟩, rfl, rfl⟩
    rcases hd with rfl | hd
    · omega
    · have : 0 < μ.rowLen (i - 1) := by omega
      have := (rowLen_pos_iff μ (i-1)).mp this
      by_cases hi : i = 0
      · omega
      · omega

theorem card_cornerCells (μ : YoungDiagram) :
    (cornerCells μ).card = (cornerRows μ).card := by
  rw [cornerCells, Finset.card_image_of_injOn]
  intro a _ b _ h
  simpa using congrArg Prod.fst h

theorem card_addableCells (μ : YoungDiagram) :
    (addableCells μ).card = (addableRows μ).card := by
  rw [addableCells, Finset.card_image_of_injOn]
  intro a _ b _ h
  simpa using congrArg Prod.fst h

/-! ### The identity -/

/-- **A Young diagram has exactly one more addable cell than it has removable corners.**

The diagonal of the `DU − UD = I` relation on the Young lattice. Holds for every `μ`,
including the empty diagram (no corners, one addable cell — the box `(0,0)`). -/
theorem card_addableCells_eq_card_cornerCells_succ (μ : YoungDiagram) :
    (addableCells μ).card = (cornerCells μ).card + 1 := by
  rw [card_addableCells, card_cornerCells, card_addableRows]

end QOU.Mathlib
