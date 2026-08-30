import QOU.Mathlib.YoungDiagramAddCell

/-!
# QOU.Mathlib.YoungLatticeDifferential — Young's lattice is 1-differential

The missing Mathlib infrastructure under `Σ_{λ⊢n} f^λ = I(n)` (beans `qou-m3xr`,
`qou-jlam`) — the identity that licenses reading the involution numbers as the
`q = 1` na-Stokes period in `QOU.Mass.SWPeriodSuperExponential`.

## Why this file and not RSK

The obvious route to `Σ_λ f^λ = I(n)` is the **Robinson–Schensted symmetry theorem**
`RSK(σ⁻¹) = swap (RSK σ)`, which restricts the bijection to involutions. The RSK
bijection itself is already in this repo (`QOU.Mathlib.Schensted*`, 40 modules;
`rskEquiv`, `rskBurnsideHolds`). The **symmetry** theorem is not, and it is the hard
half of RSK theory — on a fold-based insertion it needs matrix-ball, growth diagrams,
or Knuth equivalence.

There is a second classical route that avoids it entirely: Young's lattice is a
**1-differential poset** (Stanley), and in any such poset the rank sums `s n = Σ_{λ⊢n} f^λ`
satisfy `s (n+1) = s n + n · s (n-1)` — which is exactly the involution recurrence
`I(n+2) = I(n+1) + (n+1) I(n)`. That route is finite combinatorics on `YoungDiagram`:
no insertion, no bumping, no bijection between permutations and tableau pairs.

**This file proves the differential property itself** — the combinatorial crux:

    #(addable cells of μ)  =  #(removable corners of μ)  +  1.

## The proof

Both families are indexed by *rows*, and the indexing makes the statement a shift:

* row `i` carries a removable corner iff `rowLen (i+1) < rowLen i` (`i < numRows`);
* row `i` carries an addable cell iff `i = 0` or `rowLen i < rowLen (i-1)`.

Those two conditions are the *same* condition, offset by one. So
`addableRows = insert 0 ((cornerRows).image (·+1))` — the addable rows are the corner
rows shifted down, plus row `0`, which is always addable. Counting gives the `+1`.

Verified numerically for every partition of `n = 0..9` before formalisation, together
with the two consequences it is for: `Σ_λ f^λ · r(λ) = n · s(n-1)` and
`s(n+1) = s n + n · s(n-1)`, which reproduce `I` exactly to `n = 12`.

## Scope

Proved here: the differential property, at row level and cell level, with both
families related to the existing `IsAddableCell` / `IsCornerCell` predicates.

**Already proved elsewhere — do not rebuild:** the branching rule is
`QOU.Mathlib.numStandardYoungTableaux_branching` (`SYTBranchingRule`, sorry-free),
stated over the *same* `IsCornerCell` / `eraseCorner` API this file uses:
`#SYT μ = Σ_{c : corners of μ} #SYT (μ ∖ c)`. `cornerCells_eq_corners` below ties this
file's corner count to that theorem's index type, so the two compose directly.

**Not proved here:** the operator step `Σ_λ f^λ r(λ) = n · s(n-1)` (the `DU = UD + I`
consequence). That is the one remaining piece between this file and `Σ_λ f^λ = I(n)`.

Pure combinatorics — no ring, nothing archimedean (§7c).

## References

- [stanley1999] Enumerative Combinatorics I, §3.21 (differential posets)
- [sagan2001] The Symmetric Group, §3.6

LaTeX label: `prop:young-lattice-differential`
-/

namespace QOU.Mathlib

open YoungDiagram Finset

variable {μ : YoungDiagram}

/-! ## Row count -/

/-- The number of non-empty rows of `μ` (the length of the first column). -/
def numRows (μ : YoungDiagram) : ℕ := μ.colLen 0

/-- Row `i` is non-empty exactly when `i` is below the row count. -/
theorem rowLen_pos_iff (μ : YoungDiagram) (i : ℕ) :
    0 < μ.rowLen i ↔ i < numRows μ := by
  constructor
  · intro h
    exact YoungDiagram.mem_iff_lt_colLen.mp (YoungDiagram.mem_iff_lt_rowLen.mpr h)
  · intro h
    exact YoungDiagram.mem_iff_lt_rowLen.mp (YoungDiagram.mem_iff_lt_colLen.mpr h)

/-! ## The two row families -/

/-- Rows carrying a **removable corner**: `rowLen (i+1) < rowLen i`, among non-empty rows. -/
def cornerRows (μ : YoungDiagram) : Finset ℕ :=
  (range (numRows μ)).filter (fun i => μ.rowLen (i + 1) < μ.rowLen i)

/-- Rows carrying an **addable cell**: row `0` always, and row `i` when the row above is
strictly longer. Row `numRows μ` — the first empty row — is always addable, which is why
the range runs one further. -/
def addableRows (μ : YoungDiagram) : Finset ℕ :=
  (range (numRows μ + 1)).filter (fun i => i = 0 ∨ μ.rowLen i < μ.rowLen (i - 1))

/-- **The shift.** The addable rows are exactly row `0` together with the corner rows
moved down by one — because "row `i` has a corner" and "row `i+1` is addable" are the
same inequality `rowLen (i+1) < rowLen i`. -/
theorem addableRows_eq_insert_image (μ : YoungDiagram) :
    addableRows μ = insert 0 ((cornerRows μ).image (· + 1)) := by
  ext i
  simp only [addableRows, cornerRows, mem_filter, mem_range, mem_insert, mem_image]
  constructor
  · rintro ⟨hi, h0 | hlt⟩
    · exact Or.inl h0
    · refine Or.inr ?_
      cases i with
      | zero => simp at hlt
      | succ j =>
        refine ⟨j, ⟨?_, ?_⟩, rfl⟩
        · omega
        · simpa using hlt
  · rintro (rfl | ⟨j, ⟨hj, hlt⟩, rfl⟩)
    · exact ⟨by omega, Or.inl rfl⟩
    · exact ⟨by omega, Or.inr (by simpa using hlt)⟩

/-- **Young's lattice is 1-differential (row form).** One more addable row than corner rows. -/
theorem card_addableRows_eq (μ : YoungDiagram) :
    (addableRows μ).card = (cornerRows μ).card + 1 := by
  have hinj : Function.Injective (fun j : ℕ => j + 1) := fun a b h => by simpa using h
  have h0 : (0 : ℕ) ∉ (cornerRows μ).image (· + 1) := by
    simp
  rw [addableRows_eq_insert_image, Finset.card_insert_of_notMem h0,
      Finset.card_image_of_injective _ hinj]

/-! ## Cell level -/

/-- The removable corner cells of `μ`, one per corner row. -/
def cornerCells (μ : YoungDiagram) : Finset (ℕ × ℕ) :=
  (cornerRows μ).image (fun i => (i, μ.rowLen i - 1))

/-- The addable cells of `μ`, one per addable row. -/
def addableCells (μ : YoungDiagram) : Finset (ℕ × ℕ) :=
  (addableRows μ).image (fun i => (i, μ.rowLen i))

theorem card_cornerCells (μ : YoungDiagram) :
    (cornerCells μ).card = (cornerRows μ).card :=
  Finset.card_image_of_injective _ (fun _a _b h => (Prod.ext_iff.mp h).1)

theorem card_addableCells (μ : YoungDiagram) :
    (addableCells μ).card = (addableRows μ).card :=
  Finset.card_image_of_injective _ (fun _a _b h => (Prod.ext_iff.mp h).1)

/-- **Young's lattice is 1-differential.** Every Young diagram has exactly one more
addable cell than it has removable corners. This is the `DU − UD = I` relation of the
differential-poset structure, and the crux of the route to `Σ_λ f^λ = I(n)` that does
not pass through Robinson–Schensted symmetry. -/
theorem card_addableCells_eq_card_cornerCells_add_one (μ : YoungDiagram) :
    (addableCells μ).card = (cornerCells μ).card + 1 := by
  rw [card_addableCells, card_cornerCells, card_addableRows_eq]

/-! ## The families are what their names say -/

/-- Every cell listed by `addableCells` really is addable. -/
theorem isAddableCell_of_mem_addableCells {c : ℕ × ℕ} (hc : c ∈ addableCells μ) :
    IsAddableCell μ c := by
  simp only [addableCells, mem_image, addableRows, mem_filter, mem_range] at hc
  obtain ⟨i, ⟨-, hcond⟩, rfl⟩ := hc
  simp only [IsAddableCell]
  refine ⟨?_, ?_, ?_⟩
  · -- (i, rowLen i) ∉ μ
    simp [YoungDiagram.mem_iff_lt_rowLen]
  · -- i = 0, or the cell above is present
    rcases hcond with h0 | hlt
    · exact Or.inl h0
    · exact Or.inr (YoungDiagram.mem_iff_lt_rowLen.mpr hlt)
  · -- rowLen i = 0, or the cell to the left is present
    by_cases h : μ.rowLen i = 0
    · exact Or.inl h
    · exact Or.inr (YoungDiagram.mem_iff_lt_rowLen.mpr (by omega))

/-- Every cell listed by `cornerCells` really is a removable corner. -/
theorem isCornerCell_of_mem_cornerCells {c : ℕ × ℕ} (hc : c ∈ cornerCells μ) :
    IsCornerCell μ c := by
  simp only [cornerCells, mem_image, cornerRows, mem_filter, mem_range] at hc
  obtain ⟨i, ⟨hi, hlt⟩, rfl⟩ := hc
  have hpos : 0 < μ.rowLen i := (rowLen_pos_iff μ i).mpr hi
  simp only [IsCornerCell]
  refine ⟨?_, ?_, ?_⟩
  · exact YoungDiagram.mem_iff_lt_rowLen.mpr (by omega)
  · -- the cell below is absent: rowLen (i+1) < rowLen i
    simp only [YoungDiagram.mem_iff_lt_rowLen]
    omega
  · -- the cell to the right is absent
    simp only [YoungDiagram.mem_iff_lt_rowLen]
    omega

/-- **Converse.** Every removable corner is listed by `cornerCells` — so the family is
exactly the corner set, not merely a subset of it. Without this the count could be an
undercount and `card_addableCells_eq_card_cornerCells_add_one` would not be about
corners at all. -/
theorem mem_cornerCells_of_isCornerCell {c : ℕ × ℕ} (hc : IsCornerCell μ c) :
    c ∈ cornerCells μ := by
  obtain ⟨i, j⟩ := c
  obtain ⟨hmem, hdown, hright⟩ := hc

  have hj : j < μ.rowLen i := YoungDiagram.mem_iff_lt_rowLen.mp hmem
  have hj1 : ¬ (j + 1 < μ.rowLen i) := fun h => hright (YoungDiagram.mem_iff_lt_rowLen.mpr h)
  have hrow : μ.rowLen i = j + 1 := by omega
  have hdn : ¬ (j < μ.rowLen (i + 1)) := fun h => hdown (YoungDiagram.mem_iff_lt_rowLen.mpr h)
  have hi : i < numRows μ := (rowLen_pos_iff μ i).mp (by omega)
  simp only [cornerCells, mem_image, cornerRows, mem_filter, mem_range]
  exact ⟨i, ⟨hi, by omega⟩, by simp [hrow]⟩

/-- **Converse for addable cells.** Every addable cell is listed by `addableCells`. With
`isAddableCell_of_mem_addableCells` this makes the addable family exactly the addable
set, mirroring `mem_cornerCells_iff`. -/
theorem mem_addableCells_of_isAddableCell {c : ℕ × ℕ} (hc : IsAddableCell μ c) :
    c ∈ addableCells μ := by
  obtain ⟨i, j⟩ := c
  obtain ⟨hout, hup, hleft⟩ := hc
  have hle : μ.rowLen i ≤ j := by
    by_contra h
    exact hout (YoungDiagram.mem_iff_lt_rowLen.mpr (by omega))
  -- the cell sits at the end of its row: j = rowLen i
  have hrow : μ.rowLen i = j := by
    rcases hleft with h0 | hmem
    · simp only at h0; omega
    · have := YoungDiagram.mem_iff_lt_rowLen.mp hmem
      simp only at this ⊢
      omega
  -- and the row is addable: i = 0, or the row above is strictly longer
  refine Finset.mem_image.mpr ⟨i, ?_, by simp [hrow]⟩
  simp only [addableRows, mem_filter, mem_range]
  rcases hup with h0 | hmem
  · exact ⟨by omega, Or.inl (by simpa using h0)⟩
  · simp only at hmem
    have hlt : j < μ.rowLen (i - 1) := YoungDiagram.mem_iff_lt_rowLen.mp hmem
    have hprev : 0 < μ.rowLen (i - 1) := by omega
    have hi1 : i - 1 < numRows μ := (rowLen_pos_iff μ (i - 1)).mp hprev
    exact ⟨by omega, Or.inr (by omega)⟩

/-- Membership in `addableCells` characterises addable cells. -/
theorem mem_addableCells_iff {c : ℕ × ℕ} : c ∈ addableCells μ ↔ IsAddableCell μ c :=
  ⟨isAddableCell_of_mem_addableCells, mem_addableCells_of_isAddableCell⟩

/-- **The corner family is exactly the corner set.** Combined with
`isCornerCell_of_mem_cornerCells`, membership in `cornerCells` *characterises* removable
corners. This is what lets `card_addableCells_eq_card_cornerCells_add_one` compose with
`QOU.Mathlib.numStandardYoungTableaux_branching`, whose sum is indexed by the subtype
`{c // IsCornerCell μ c}`. -/
theorem mem_cornerCells_iff {c : ℕ × ℕ} : c ∈ cornerCells μ ↔ IsCornerCell μ c :=
  ⟨isCornerCell_of_mem_cornerCells, mem_cornerCells_of_isCornerCell⟩

/-! ## Bridge to the branching theorem's index type

`QOU.Mathlib.numStandardYoungTableaux_branching` sums over the SUBTYPE
`{c // IsCornerCell μ c}`. This file counts with the FINSET `cornerCells μ`. The two
agree — that is what `mem_cornerCells_iff` buys — so the differential property counts
exactly the terms of the branching sum. -/

/-- The corner Finset and the branching theorem's corner subtype have the same
cardinality. So `#SYT μ = Σ_{c : corners} #SYT (μ ∖ c)` has exactly
`(cornerCells μ).card` summands. -/
theorem card_cornerCells_eq_card_subtype (μ : YoungDiagram)
    [Fintype {c : ℕ × ℕ // IsCornerCell μ c}] :
    (cornerCells μ).card = Fintype.card {c : ℕ × ℕ // IsCornerCell μ c} :=
  (Fintype.card_of_subtype (cornerCells μ) (fun _ => mem_cornerCells_iff)).symm

/-- **The differential property, in the form the branching sum sees it.** The number of
summands in `numStandardYoungTableaux_branching` for `μ` is one less than the number of
addable cells of `μ`. This is the bridge that lets the `DU = UD + I` step be run against
the already-proved branching rule. -/
theorem card_subtype_corners_add_one (μ : YoungDiagram)
    [Fintype {c : ℕ × ℕ // IsCornerCell μ c}] :
    Fintype.card {c : ℕ × ℕ // IsCornerCell μ c} + 1 = (addableCells μ).card := by
  rw [← card_cornerCells_eq_card_subtype, card_addableCells_eq_card_cornerCells_add_one]

/-! ## Non-vacuity

A `card = card + 1` theorem is worth nothing if both families are empty — it would then
read `1 = 0 + 1` on every diagram and assert nothing about corners at all. `decide`
cannot settle a concrete shape here (`colLen` does not reduce), so both families are
shown inhabited *structurally*, which is stronger than a spot check:

* every diagram has an addable cell (row `0`);
* every **non-empty** diagram has a removable corner (the last non-empty row, whose
  successor row is empty).
-/

/-- Row `0` is always addable, so the addable family is never empty. -/
theorem addableRows_nonempty (μ : YoungDiagram) : (addableRows μ).Nonempty := by
  refine ⟨0, ?_⟩
  simp only [addableRows, mem_filter, mem_range]
  exact ⟨by omega, Or.inl trivial⟩

theorem addableCells_nonempty (μ : YoungDiagram) : (addableCells μ).Nonempty := by
  obtain ⟨i, hi⟩ := addableRows_nonempty μ
  exact ⟨(i, μ.rowLen i), Finset.mem_image_of_mem _ hi⟩

/-- The last non-empty row carries a removable corner, so any diagram with a cell has one.
This is what stops `card_addableCells_eq_card_cornerCells_add_one` from being the vacuous
`1 = 0 + 1`. -/
theorem cornerRows_nonempty (μ : YoungDiagram) (h : 0 < numRows μ) :
    (cornerRows μ).Nonempty := by
  refine ⟨numRows μ - 1, ?_⟩
  simp only [cornerRows, mem_filter, mem_range]
  refine ⟨by omega, ?_⟩
  have h1 : 0 < μ.rowLen (numRows μ - 1) := (rowLen_pos_iff μ _).mpr (by omega)
  have h2 : ¬ (0 < μ.rowLen (numRows μ - 1 + 1)) := by
    rw [rowLen_pos_iff]
    omega
  omega

theorem cornerCells_nonempty (μ : YoungDiagram) (h : 0 < numRows μ) :
    (cornerCells μ).Nonempty := by
  obtain ⟨i, hi⟩ := cornerRows_nonempty μ h
  exact ⟨(i, μ.rowLen i - 1), Finset.mem_image_of_mem _ hi⟩

end QOU.Mathlib
