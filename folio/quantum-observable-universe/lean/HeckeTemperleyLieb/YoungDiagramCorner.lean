import Mathlib.Combinatorics.Young.YoungDiagram

/-!
# QOU.Mathlib.YoungDiagramCorner — removable corners and corner removal of Young diagrams

Mathlib's `YoungDiagram` carries `ofRowLens` / `rowLens` / `mem_cells` / `up_left_mem` but **no**
corner / erase / `SDiff` API.  This file supplies the missing structural primitive needed for the
Greene–Nijenhuis–Wilf branching rule
`numStandardYoungTableaux μ = ∑_{removable corners c} numStandardYoungTableaux (μ ∖ c)`:

* `IsCornerCell μ c` — `c` is a **removable corner**: a cell of `μ` with no cell to its right or below.
* `eraseCorner μ c hc` — the Young diagram `μ ∖ c` (delete the corner cell; the result is still a lower
  set, hence a genuine `YoungDiagram`), with its membership and cardinality laws.

Removing a *corner* (a maximal cell) is exactly what keeps `cells.erase c` downward closed: any cell
strictly above-or-right of `c` that stayed in `μ` would force one of `c`'s missing neighbours back in.

Pure combinatorics on `ℕ × ℕ`; nothing archimedean; no fit.
-/

namespace QOU.Mathlib

open YoungDiagram

/-- A **removable corner** of `μ`: a cell `c ∈ μ` whose right neighbour `(i, j+1)` and lower neighbour
`(i+1, j)` are both outside `μ` — i.e. `c` is an outer corner whose deletion leaves a Young diagram. -/
def IsCornerCell (μ : YoungDiagram) (c : ℕ × ℕ) : Prop :=
  c ∈ μ ∧ (c.1 + 1, c.2) ∉ μ ∧ (c.1, c.2 + 1) ∉ μ

/-- **Corner removal `μ ∖ c`.** Deleting a removable corner cell from `μ` yields a Young diagram:
`cells.erase c` is still a lower set, because any `a ∈ μ` with `c ≤ a` and `a ≠ c` would have one of
`c`'s (absent) neighbours `≤ a`, hence in `μ` by `up_left_mem` — contradicting that `c` is a corner. -/
def eraseCorner (μ : YoungDiagram) (c : ℕ × ℕ) (hc : IsCornerCell μ c) : YoungDiagram where
  cells := μ.cells.erase c
  isLowerSet := by
    obtain ⟨_, hc1, hc2⟩ := hc
    intro a b hba ha
    simp only [Finset.coe_erase, Set.mem_diff, Set.mem_singleton_iff] at ha ⊢
    obtain ⟨haμ, hane⟩ := ha
    refine ⟨μ.isLowerSet hba haμ, ?_⟩
    intro hbc
    rw [hbc] at hba                      -- hba : c ≤ a
    have haIn : a ∈ μ := Finset.mem_coe.mp haμ
    have h1 : c.1 ≤ a.1 := hba.1
    have h2 : c.2 ≤ a.2 := hba.2
    have hstrict : c.1 < a.1 ∨ c.2 < a.2 := by
      by_contra h
      push_neg at h
      exact hane (Prod.ext_iff.mpr ⟨by omega, by omega⟩)
    rcases hstrict with hlt | hlt
    · exact hc1 (μ.up_left_mem (by omega : c.1 + 1 ≤ a.1) h2 haIn)
    · exact hc2 (μ.up_left_mem h1 (by omega : c.2 + 1 ≤ a.2) haIn)

@[simp] theorem mem_eraseCorner (μ : YoungDiagram) (c : ℕ × ℕ) (hc : IsCornerCell μ c) (x : ℕ × ℕ) :
    x ∈ eraseCorner μ c hc ↔ x ∈ μ ∧ x ≠ c := by
  show x ∈ μ.cells.erase c ↔ x ∈ μ.cells ∧ x ≠ c
  rw [Finset.mem_erase]
  tauto

/-- The corner cell really is in `μ`, so removal drops the cell count by one. -/
theorem card_eraseCorner (μ : YoungDiagram) (c : ℕ × ℕ) (hc : IsCornerCell μ c) :
    (eraseCorner μ c hc).cells.card + 1 = μ.cells.card := by
  have hcm : c ∈ μ.cells := hc.1
  have hpos : 0 < μ.cells.card := Finset.card_pos.mpr ⟨c, hcm⟩
  rw [show (eraseCorner μ c hc).cells = μ.cells.erase c from rfl,
    Finset.card_erase_of_mem hcm]
  omega

end QOU.Mathlib
