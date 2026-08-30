import QOU.SchurWeyl.TableauCells
import QOU.Mathlib.SYTInsertMax
import QOU.Mathlib.SYTBranchingBijection

/-!
# QOU.SchurWeyl.SytInsertMaxTransport — the tableau side of the branching compatibility

`SeminormalBlockTrace` reduced the Markov condition, for a single `V_λ`, to a sum of diagonal
entries.  Turning that into the Markov condition itself needs one more structural fact:

> the seminormal representation of `λ`, restricted to the block of an addable corner `s`, is the
> seminormal representation of `μ = λ ∖ s`.

`genMat`'s entry rules read exactly four things about a tableau — `cellOf`, `axialDist`,
`SwapAdmissible`, and `swapTableau` — so that fact reduces to their compatibility with
`QOU.Mathlib.insertMax`, the corner-insertion map whose bijectivity `SYTBranchingRule` already
proves.  This file supplies all four, plus injectivity of `insertMax` at a fixed corner.

| lemma | content |
|---|---|
| `cellOf_insertMax` | inserting the max does not move any smaller entry's cell |
| `axialDist_insertMax` | hence axial distances at smaller entries are unchanged |
| `swapAdmissible_insertMax_iff` | `SwapAdmissible` is defined from `cellOf`, so it transfers |
| `swapTableau_insertMax` | `insertMax` intertwines the partial `s_k`-action |
| `insertMax_injective` | at a fixed corner, `insertMax` changes only the cell `c` |

## What is still missing

These are the *ingredients*, not the conclusion.  The block equality itself —
`genMat_λ q k (insertMax S'') (insertMax S') = genMat_μ q k S'' S'` — is a case analysis over
`genMat`'s three branches using the five lemmas above, and is not written here.  Nor is the outer
reindexing `{(λ, corner)} ↔ {(μ, addable corner)}` that the λ-sum needs, though
`SYTBranchingRule.branchInv` (bijective) supplies the inner half of it.

Bean `qou-uer7`.

## Base ring (§7c)

None — pure `ℕ`/cell combinatorics.  No ring at all.

LaTeX label: `thm:syt-insertmax-transport`
-/

namespace QOU.SchurWeyl
namespace TableauCells

open QOU.Mathlib

variable {μ : YoungDiagram}

/-- `insertMax` does not move the cell of any smaller entry. -/
theorem cellOf_insertMax (c : ℕ × ℕ) (hc : IsCornerCell μ c)
    (S : StandardYoungTableau (eraseCorner μ c hc)) {k : ℕ}
    (hk : k ∈ Set.Icc 1 (eraseCorner μ c hc).cells.card) :
    cellOf (insertMax c hc S) k = cellOf S k := by
  have hmem : cellOf S k ∈ (eraseCorner μ c hc).cells := cellOf_mem S hk
  have hmemμ : cellOf S k ∈ μ.cells := by
    have := (mem_eraseCorner μ c hc (cellOf S k)).mp ((YoungDiagram.mem_cells _).mp hmem)
    exact (YoungDiagram.mem_cells _).mpr this.1
  have hne : cellOf S k ≠ c := by
    intro h
    have := (mem_eraseCorner μ c hc (cellOf S k)).mp ((YoungDiagram.mem_cells _).mp hmem)
    exact this.2 h
  refine cellOf_unique _ hmemμ ?_
  show (if (cellOf S k) = c then μ.cells.card else S.entry (cellOf S k).1 (cellOf S k).2) = k
  rw [if_neg hne]
  exact entry_cellOf S hk

/-- Hence `insertMax` preserves the axial distance at any pair of smaller entries. -/
theorem axialDist_insertMax (c : ℕ × ℕ) (hc : IsCornerCell μ c)
    (S : StandardYoungTableau (eraseCorner μ c hc)) {k : ℕ}
    (hk : k ∈ Set.Icc 1 (eraseCorner μ c hc).cells.card)
    (hk1 : k + 1 ∈ Set.Icc 1 (eraseCorner μ c hc).cells.card) :
    axialDist (insertMax c hc S) k = axialDist S k := by
  unfold axialDist
  rw [cellOf_insertMax c hc S hk, cellOf_insertMax c hc S hk1]

/-- `SwapAdmissible` is defined from `cellOf`, so it too transfers. -/
theorem swapAdmissible_insertMax_iff (c : ℕ × ℕ) (hc : IsCornerCell μ c)
    (S : StandardYoungTableau (eraseCorner μ c hc)) {k : ℕ}
    (hk : k ∈ Set.Icc 1 (eraseCorner μ c hc).cells.card)
    (hk1 : k + 1 ∈ Set.Icc 1 (eraseCorner μ c hc).cells.card) :
    SwapAdmissible (insertMax c hc S) k ↔ SwapAdmissible S k := by
  unfold SwapAdmissible
  rw [cellOf_insertMax c hc S hk, cellOf_insertMax c hc S hk1]

/-- `insertMax` intertwines the partial `s_k`-action: swapping then inserting is inserting then
swapping.  With `axialDist_insertMax` and `swapAdmissible_insertMax_iff` this is everything
`genMat`'s entry rules read, so the seminormal matrix of a generator that avoids the top entry has
the same entries on the block as it does downstairs. -/
theorem swapTableau_insertMax (c : ℕ × ℕ) (hc : IsCornerCell μ c)
    (S : StandardYoungTableau (eraseCorner μ c hc)) {k : ℕ} (hk : 1 ≤ k)
    (hkn : k + 1 ≤ (eraseCorner μ c hc).cells.card)
    (hadm : SwapAdmissible S k)
    (hadm' : SwapAdmissible (insertMax c hc S) k) :
    swapTableau (insertMax c hc S) k hk (by
      have := card_eraseCorner μ c hc; omega) hadm'
      = insertMax c hc (swapTableau S k hk hkn hadm) := by
  apply syt_ext
  intro i j
  rw [swapTableau_entry]
  by_cases hij : (i, j) = c
  · have hcard : (eraseCorner μ c hc).cells.card + 1 = μ.cells.card := by
      have := card_eraseCorner μ c hc; omega
    show swapVal k (if (i, j) = c then μ.cells.card else S.entry i j)
        = if (i, j) = c then μ.cells.card else _
    rw [if_pos hij, if_pos hij]
    unfold swapVal
    rw [if_neg (by omega), if_neg (by omega)]
  · show swapVal k (if (i, j) = c then μ.cells.card else S.entry i j)
        = if (i, j) = c then μ.cells.card else (swapTableau S k hk hkn hadm).entry i j
    rw [if_neg hij, if_neg hij, swapTableau_entry]

/-- `insertMax` is injective for a fixed corner: it changes only the cell `c`. -/
theorem insertMax_injective (c : ℕ × ℕ) (hc : IsCornerCell μ c) :
    Function.Injective (insertMax (μ := μ) c hc) := by
  intro S1 S2 h
  apply syt_ext
  intro i j
  by_cases hij : (i, j) = c
  · have h1 : S1.entry i j = 0 := by
      apply S1.toSsyt.zeros
      intro hin
      exact ((mem_eraseCorner μ c hc (i, j)).mp hin).2 hij
    have h2 : S2.entry i j = 0 := by
      apply S2.toSsyt.zeros
      intro hin
      exact ((mem_eraseCorner μ c hc (i, j)).mp hin).2 hij
    rw [h1, h2]
  · have hh : (insertMax c hc S1).entry i j = (insertMax c hc S2).entry i j := by rw [h]
    have e1 : (insertMax c hc S1).entry i j
        = if (i, j) = c then μ.cells.card else S1.entry i j := rfl
    have e2 : (insertMax c hc S2).entry i j
        = if (i, j) = c then μ.cells.card else S2.entry i j := rfl
    rw [e1, e2, if_neg hij, if_neg hij] at hh
    exact hh

end TableauCells
end QOU.SchurWeyl
