import QOU.Mathlib.YoungDiagramAddable

/-!
# QOU.Mathlib.YoungDiagramAddCell — adjoining a corner, the inverse of `eraseCorner`

`YoungDiagramCorner` supplies `IsCornerCell` and `eraseCorner`.  This file supplies the other
direction — `IsAddableCell` and `addCell` — together with the two round-trips.

| | |
|---|---|
| `IsAddableCell μ s` | `s ∉ μ`, with its up- and left-neighbours present or absent by boundary |
| `addCell μ s hs` | `μ` with `s` adjoined; still a Young diagram |
| `card_addCell` | `\|μ + s\| = \|μ\| + 1` |
| `isCornerCell_addCell` | the added cell is a removable corner of the result |
| `isAddableCell_eraseCorner` | a removable corner is addable to the erased diagram |
| `eraseCorner_addCell`, `addCell_eraseCorner` | the two round-trips |

## Why

The Markov assembly (bean `qou-uer7`, step 2b) needs the reindexing

`{(λ, removable corner of λ) : |λ| = n+1} ≃ {(μ, addable corner of μ) : |μ| = n}`,

and `SYTBranchingRule.branchInv` supplies only the inner half — it fixes `λ` and varies the corner.
The outer exchange needs to *build* `λ` from `(μ, s)`, which `eraseCorner` alone cannot do.  These
lemmas are that construction and its round-trips, and `cornerAddEquiv` below is the exchange itself.

Pure combinatorics; no ring, nothing archimedean.

LaTeX label: `def:young-diagram-add-cell`
-/

namespace QOU.Mathlib

open YoungDiagram

variable {μ : YoungDiagram}

/-! `IsAddableCell`, `addCell`, `mem_addCell` and `card_addCell` are **not redeclared
here** — they come from `QOU.Mathlib.YoungDiagramAddable`, which this module now imports.

They used to be defined in both files, with character-identical bodies, and the
duplication made the two modules MUTUALLY EXCLUSIVE: no module could import both, since
Lean rejects the second declaration of a name already in the environment. That is a real
constraint, not a tidiness point — it is what stopped `YoungLatticeCornerCount` from
reusing `YoungDiagramAddable`'s corner/addable API while needing `cornerAddEquiv` from
here (bean `qou-dup1`).

This file is now a proper EXTENSION of `YoungDiagramAddable`: it adds the `eraseCorner`
round-trips and the outer exchange, and redeclares nothing. Measured before the change:
`card_addCell` and `mem_addCell` have **zero** consumers outside this file, so the
argument-order difference between the two former copies breaks nothing. -/

/-- The added cell is a removable corner of the result. -/
theorem isCornerCell_addCell (s : ℕ × ℕ) (hs : IsAddableCell μ s) :
    IsCornerCell (addCell μ s hs) s := by
  refine ⟨(mem_addCell μ s s hs).mpr (Or.inl rfl), ?_, ?_⟩
  · rw [mem_addCell]
    rintro (h | h)
    · exact absurd h (by simp [Prod.ext_iff])
    · exact hs.1 (μ.up_left_mem (by omega) le_rfl h)
  · rw [mem_addCell]
    rintro (h | h)
    · exact absurd h (by simp [Prod.ext_iff])
    · exact hs.1 (μ.up_left_mem le_rfl (by omega) h)

/-- Adding then erasing is the identity. -/
theorem eraseCorner_addCell (s : ℕ × ℕ) (hs : IsAddableCell μ s) :
    eraseCorner (addCell μ s hs) s (isCornerCell_addCell s hs) = μ := by
  ext x
  simp only [YoungDiagram.mem_cells]
  rw [mem_eraseCorner, mem_addCell]
  constructor
  · rintro ⟨h | h, hne⟩
    · exact absurd h hne
    · exact h
  · intro h
    exact ⟨Or.inr h, fun hx => hs.1 (hx ▸ h)⟩

/-- Erasing then adding is the identity. -/
theorem addCell_eraseCorner (c : ℕ × ℕ) (hc : IsCornerCell μ c)
    (hs : IsAddableCell (eraseCorner μ c hc) c) :
    addCell (eraseCorner μ c hc) c hs = μ := by
  ext x
  simp only [YoungDiagram.mem_cells]
  rw [mem_addCell, mem_eraseCorner]
  constructor
  · rintro (rfl | ⟨h, _⟩)
    · exact hc.1
    · exact h
  · intro h
    by_cases hx : x = c
    · exact Or.inl hx
    · exact Or.inr ⟨h, hx⟩

/-- A removable corner is addable to the erased diagram. -/
theorem isAddableCell_eraseCorner (c : ℕ × ℕ) (hc : IsCornerCell μ c) :
    IsAddableCell (eraseCorner μ c hc) c := by
  refine ⟨by rw [mem_eraseCorner]; rintro ⟨-, h⟩; exact h rfl, ?_, ?_⟩
  · by_cases h0 : c.1 = 0
    · exact Or.inl h0
    · refine Or.inr ?_
      rw [mem_eraseCorner]
      refine ⟨μ.up_left_mem (by omega) le_rfl hc.1, ?_⟩
      intro hh; rw [Prod.ext_iff] at hh; omega
  · by_cases h0 : c.2 = 0
    · exact Or.inl h0
    · refine Or.inr ?_
      rw [mem_eraseCorner]
      refine ⟨μ.up_left_mem le_rfl (by omega) hc.1, ?_⟩
      intro hh; rw [Prod.ext_iff] at hh; omega

/-! ### The outer branching exchange

`(λ, removable corner) ↔ (λ ∖ c, that corner, now addable)`.

**Phrasing note, and it is the whole trick.**  The natural spelling is a `Sigma` over the diagram,
`Σ L : {μ // |μ| = n+1}, {c // IsCornerCell L.1 c}`.  Don't: the second component's type then depends
on the first, so `left_inv` lands on a `HEq` between corner-proofs over two diagrams that are equal
but not syntactically so, and discharging it needs a transport whose motive does not typecheck
(the card-proof inside the diagram depends on the diagram).  Phrasing **both sides as subtypes of
one product type** removes the dependency: the round-trips are then plain `Subtype.ext` on a pair.
-/

/-- A diagram of size `n + 1` together with one of its removable corners. -/
def CornerPair (n : ℕ) : Type :=
  {p : YoungDiagram × (ℕ × ℕ) // p.1.cells.card = n + 1 ∧ IsCornerCell p.1 p.2}

/-- A diagram of size `n` together with one of its addable corners. -/
def AddPair (n : ℕ) : Type :=
  {p : YoungDiagram × (ℕ × ℕ) // p.1.cells.card = n ∧ IsAddableCell p.1 p.2}

/-- **The outer branching exchange.**  `(λ, removable corner) ↔ (λ ∖ c, that corner as an addable
one)`.  Phrasing both sides as subtypes of one product type — rather than as `Sigma`s over the
diagram — keeps the equality proofs at `Subtype.ext`, with no `HEq` transport. -/
def cornerAddEquiv (n : ℕ) : CornerPair n ≃ AddPair n where
  toFun := fun p =>
    ⟨(eraseCorner p.1.1 p.1.2 p.2.2, p.1.2), by
      refine ⟨?_, isAddableCell_eraseCorner p.1.2 p.2.2⟩
      show (eraseCorner p.1.1 p.1.2 p.2.2).cells.card = n
      have h1 := card_eraseCorner p.1.1 p.1.2 p.2.2
      have h2 := p.2.1
      omega⟩
  invFun := fun p =>
    ⟨(addCell p.1.1 p.1.2 p.2.2, p.1.2), by
      refine ⟨?_, isCornerCell_addCell p.1.2 p.2.2⟩
      show (addCell p.1.1 p.1.2 p.2.2).cells.card = n + 1
      rw [card_addCell, p.2.1]⟩
  left_inv := by
    rintro ⟨⟨L, c⟩, hL, hc⟩
    refine Subtype.ext ?_
    show (addCell (eraseCorner L c hc) c (isAddableCell_eraseCorner c hc), c) = (L, c)
    rw [addCell_eraseCorner]
  right_inv := by
    rintro ⟨⟨M, s⟩, hM, hs⟩
    refine Subtype.ext ?_
    show (eraseCorner (addCell M s hs) s (isCornerCell_addCell s hs), s) = (M, s)
    rw [eraseCorner_addCell]


instance instDecidableIsAddableCell (ν : YoungDiagram) (s : ℕ × ℕ) :
    Decidable (IsAddableCell ν s) := by
  unfold IsAddableCell; infer_instance

/-- **`addCell` made total in the cell.**  A summand quantified over *all* cells cannot mention
`addCell ν s hs`, which needs the addability proof; this is the version that can appear there, and
`addCellOrSelf_of` recovers the real thing wherever the proof is available. -/
noncomputable def addCellOrSelf (ν : YoungDiagram) (s : ℕ × ℕ) : YoungDiagram :=
  if h : IsAddableCell ν s then addCell ν s h else ν

@[simp] theorem addCellOrSelf_of {ν : YoungDiagram} {s : ℕ × ℕ} (h : IsAddableCell ν s) :
    addCellOrSelf ν s = addCell ν s h := dif_pos h

end QOU.Mathlib
