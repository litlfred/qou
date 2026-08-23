import QOU.SchurWeyl.SytInsertMaxTransport
import QOU.SchurWeyl.SeminormalRep

/-!
# QOU.SchurWeyl.SeminormalBlockEquality — a generator's matrix on a corner block

`SytInsertMaxTransport` supplied the four tableau-level compatibilities that `genMat`'s entry rules
read.  This file assembles them into the statement they were for:

`genMat q k (insertMax c hc S'') (insertMax c hc S') = genMat q k S'' S'`

for any `k` with `k + 1 ≤ |μ ∖ c|` — a generator that avoids the top entry has, on the block of the
corner `c`, exactly the matrix it has downstairs on `μ ∖ c`.  It is a case analysis over `genMat`'s
three branches: diagonal, swap partner, zero.

Also here, and needed next: the block of `c` is **exactly** the image of `insertMax`
(`cellOf_insertMax_top` and `exists_insertMax_of_cellOf_top`, the latter a repackaging of
`QOU.Mathlib.insertMax_eraseMax`).

## Where this sits

Step 1 of the three the Markov assembly needs (bean `qou-uer7`):

1. **this file** — the block equality at a generator;
2. lifting it from generators to all of `H_{|μ|-1}(q)`, then the outer reindexing
   `{(λ, corner)} ↔ {(μ, addable corner)}`;
3. the `λ`-sum with weights, where `OcneanuWeightMarkovCorner`'s corner identities are consumed.

Step 2's first half is the reason the image characterisation is here: lifting to a product needs the
matrix-multiplication sum over the block to be a sum over `SYT (μ ∖ c)`, which needs the block and
that image to coincide.  Neither half of step 2 is written.

## Base ring (§7c)

`ℝ`, inherited from `genMat`; nothing archimedean is added here.

LaTeX label: `thm:seminormal-block-equality`
-/

namespace QOU.SchurWeyl
namespace SeminormalRep

open QOU.Mathlib QOU.SchurWeyl.TableauCells

variable {μ : YoungDiagram}

/-- **The block equality.**  A generator that avoids the top entry has, on the block of the corner
`c`, exactly the matrix it has downstairs on `μ ∖ c`. -/
theorem genMat_insertMax (q : ℝ) (c : ℕ × ℕ) (hc : IsCornerCell μ c) {k : ℕ} (hk : 1 ≤ k)
    (hkn : k + 1 ≤ (eraseCorner μ c hc).cells.card) (hbig : k + 1 ≤ μ.cells.card)
    (S' S'' : StandardYoungTableau (eraseCorner μ c hc)) :
    genMat q k hk hbig (insertMax c hc S'') (insertMax c hc S') = genMat q k hk hkn S'' S' := by
  classical
  have hkI : k ∈ Set.Icc 1 (eraseCorner μ c hc).cells.card := ⟨hk, by omega⟩
  have hk1I : k + 1 ∈ Set.Icc 1 (eraseCorner μ c hc).cells.card := ⟨by omega, hkn⟩
  have hax : axialDist (insertMax c hc S') k = axialDist S' k :=
    axialDist_insertMax c hc S' hkI hk1I
  by_cases hEq : S'' = S'
  · subst hEq
    rw [genMat_diag, genMat_diag, hax]
  · have hEq' : insertMax c hc S'' ≠ insertMax c hc S' := fun h => hEq (insertMax_injective c hc h)
    by_cases hadm : SwapAdmissible S' k
    · have hadm' : SwapAdmissible (insertMax c hc S') k :=
        (swapAdmissible_insertMax_iff c hc S' hkI hk1I).mpr hadm
      have hsw : swapTableau (insertMax c hc S') k hk hbig hadm'
          = insertMax c hc (swapTableau S' k hk hkn hadm) :=
        swapTableau_insertMax c hc S' hk hkn hadm hadm'
      by_cases hS : S'' = swapTableau S' k hk hkn hadm
      · have hne_small : swapTableau S' k hk hkn hadm ≠ S' := fun h => hEq (by rw [hS, h])
        have hne_big : swapTableau (insertMax c hc S') k hk hbig hadm' ≠ insertMax c hc S' := by
          rw [hsw]; exact fun h => hne_small (insertMax_injective c hc h)
        have hLHS : insertMax c hc S'' = swapTableau (insertMax c hc S') k hk hbig hadm' := by
          rw [hS, hsw]
        rw [hLHS, genMat_swap q k hk hbig hadm' hne_big, hS,
          genMat_swap q k hk hkn hadm hne_small, hax]
      · have hno_big : insertMax c hc S''
            ≠ swapTableau (insertMax c hc S') k hk hbig hadm' := by
          rw [hsw]; exact fun h => hS (insertMax_injective c hc h)
        rw [genMat_apply_of_ne q k hk hbig hEq' hadm' hno_big,
          genMat_apply_of_ne q k hk hkn hEq hadm hS]
    · have hadm' : ¬ SwapAdmissible (insertMax c hc S') k :=
        fun h => hadm ((swapAdmissible_insertMax_iff c hc S' hkI hk1I).mp h)
      rw [genMat_of_not_admissible q k hk hbig hEq' hadm',
        genMat_of_not_admissible q k hk hkn hEq hadm]

/-- The inserted entry sits at `c`: `insertMax` lands in the block of the corner `c`. -/
theorem cellOf_insertMax_top (c : ℕ × ℕ) (hc : IsCornerCell μ c)
    (S : StandardYoungTableau (eraseCorner μ c hc)) :
    cellOf (insertMax c hc S) μ.cells.card = c := by
  refine cellOf_unique _ ((YoungDiagram.mem_cells c).mpr hc.1) ?_
  show (if c = c then μ.cells.card else S.entry c.1 c.2) = μ.cells.card
  rw [if_pos rfl]

/-- …and conversely the block of `c` is exactly the image of `insertMax`. -/
theorem exists_insertMax_of_cellOf_top (c : ℕ × ℕ) (hc : IsCornerCell μ c)
    (T : StandardYoungTableau μ) (h : cellOf T μ.cells.card = c) :
    ∃ S : StandardYoungTableau (eraseCorner μ c hc), insertMax c hc S = T := by
  have hcard : 0 < μ.cells.card := Finset.card_pos.mpr ⟨c, hc.1⟩
  have hmax : T.entry c.1 c.2 = μ.cells.card := by
    rw [← h]; exact entry_cellOf T ⟨hcard, le_rfl⟩
  exact ⟨eraseMax T c hc hmax, insertMax_eraseMax T c hc hmax⟩

end SeminormalRep
end QOU.SchurWeyl
