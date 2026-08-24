import QOU.SchurWeyl.SytInsertMaxTransport
import QOU.SchurWeyl.SeminormalRep
import QOU.SchurWeyl.SeminormalBlockTrace
import QOU.SchurWeyl.HeckeInclusion

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
2. lifting it from generators to all of `H_{|μ|-1}(q)` — **also here**,
   `compress_seminormalRep_heckeIncl` — then the outer reindexing
   `{(λ, corner)} ↔ {(μ, addable corner)}`, now in `QOU.Mathlib.YoungDiagramCornerReindex`;
3. the `λ`-sum with weights, where `OcneanuWeightMarkovCorner`'s corner identities are consumed,
   now in `MarkovAssembly`.

All three are written.  What remains outside Lean is the corner identity itself at general `n`.

The image characterisation is what makes step 2's first half work: lifting to a product needs the
matrix-multiplication sum over the block to be a sum over `SYT (μ ∖ c)`, which is exactly the block
and that image coinciding.

## Base ring (§7c)

`ℝ`, inherited from `genMat`; nothing archimedean is added here.

LaTeX label: `thm:seminormal-block-equality`
-/

namespace QOU.SchurWeyl
namespace SeminormalRep

open QOU.Mathlib QOU.SchurWeyl.TableauCells QOU.SchurWeyl.HeckeInclusion

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

/-! ### From a generator to every element

Compression to the block is multiplicative on block-preserving matrices — the sum over `SYT μ`
collapses to the block, and the block is exactly `insertMax`'s image.  With `genMat_insertMax` for
the generators and `seminormalRep_heckeIncl_mem_blockSubalgebra` for the block-preservation, an
adjoin-induction lifts the block equality to every element of `H_{m+1}(q)`.
-/

/-- Restriction of a matrix to the block of the corner `c`. -/
def compress (c : ℕ × ℕ) (hc : IsCornerCell μ c)
    (X : Matrix (StandardYoungTableau μ) (StandardYoungTableau μ) ℝ) :
    Matrix (StandardYoungTableau (eraseCorner μ c hc))
      (StandardYoungTableau (eraseCorner μ c hc)) ℝ :=
  Matrix.of fun S'' S' => X (insertMax c hc S'') (insertMax c hc S')

theorem compress_one (c : ℕ × ℕ) (hc : IsCornerCell μ c) :
    compress c hc (1 : Matrix (StandardYoungTableau μ) (StandardYoungTableau μ) ℝ) = 1 := by
  ext S'' S'
  show (1 : Matrix _ _ ℝ) (insertMax c hc S'') (insertMax c hc S') = _
  by_cases h : S'' = S'
  · subst h; simp
  · rw [Matrix.one_apply_ne (fun hh => h (insertMax_injective c hc hh)),
      Matrix.one_apply_ne h]

theorem compress_smul (c : ℕ × ℕ) (hc : IsCornerCell μ c) (r : ℝ)
    (X : Matrix (StandardYoungTableau μ) (StandardYoungTableau μ) ℝ) :
    compress c hc (r • X) = r • compress c hc X := rfl

/-- **Compression is multiplicative on block-preserving matrices.**  The sum over `SYT μ` collapses
to a sum over the block, and the block is exactly `insertMax`'s image. -/
theorem compress_mul (c : ℕ × ℕ) (hc : IsCornerCell μ c)
    {X Y : Matrix (StandardYoungTableau μ) (StandardYoungTableau μ) ℝ}
    (hX : BlockPreserving μ.cells.card X) :
    compress c hc (X * Y) = compress c hc X * compress c hc Y := by
  classical
  ext S'' S'
  show (X * Y) (insertMax c hc S'') (insertMax c hc S') = _
  rw [Matrix.mul_apply]
  have hzero : ∀ R : StandardYoungTableau μ,
      R ∉ Finset.univ.image (insertMax c hc) →
      X (insertMax c hc S'') R * Y R (insertMax c hc S') = 0 := by
    intro R hR
    have hne : cellOf (insertMax c hc S'') μ.cells.card ≠ cellOf R μ.cells.card := by
      rw [cellOf_insertMax_top]
      intro h
      exact hR (Finset.mem_image.mpr
        (by obtain ⟨S, hS⟩ := exists_insertMax_of_cellOf_top c hc R h.symm
            exact ⟨S, Finset.mem_univ S, hS⟩))
    rw [hX _ _ hne, zero_mul]
  rw [← Finset.sum_subset (Finset.subset_univ (Finset.univ.image (insertMax c hc)))
      (fun R _ hR => hzero R hR)]
  rw [Finset.sum_image (fun a _ b _ h => insertMax_injective c hc h)]
  rfl

/-- **Step 2, first half.**  The compression of the big seminormal representation, along the
inclusion, IS the small seminormal representation — for every element, not just the generators. -/
theorem compress_seminormalRep_heckeIncl {q : ℝ} (hq0 : q ≠ 0) (hq2 : q ^ 2 ≠ 1)
    (m : ℕ) (hN : μ.cells.card = m + 2) (c : ℕ × ℕ) (hc : IsCornerCell μ c)
    (hNs : (eraseCorner μ c hc).cells.card = m + 1) (y : Hecke ℝ q q⁻¹ m) :
    compress c hc (seminormalRep q hq0 hq2 (m + 1) hN (heckeIncl ℝ q q⁻¹ m y))
      = seminormalRep q hq0 hq2 m hNs y := by
  have hy : y ∈ Algebra.adjoin ℝ (Set.range (Hecke.σ ℝ q q⁻¹ m)) := by
    rw [HeckeInclusion.adjoin_range_σ_eq_top]; trivial
  induction hy using Algebra.adjoin_induction with
  | mem x hx =>
      obtain ⟨i, rfl⟩ := hx
      rw [heckeIncl_σ, seminormalRep_σ, seminormalRep_σ]
      show compress c hc (seminormalGen q (m + 1) hN i.castSucc) = seminormalGen q m hNs i
      have hi := i.isLt
      have hcc : ((i.castSucc : Fin (m + 1)) : ℕ) = (i : ℕ) := rfl
      rw [seminormalGen, seminormalGen]
      ext S'' S'
      exact genMat_insertMax q c hc (by omega) (by omega) (by omega) S' S''
  | algebraMap r =>
      rw [AlgHom.commutes, AlgHom.commutes, Algebra.algebraMap_eq_smul_one,
        Algebra.algebraMap_eq_smul_one, compress_smul, compress_one, map_smul, map_one]
  | add x z hx hz ihx ihz =>
      rw [map_add, map_add, map_add, ← ihx, ← ihz]
      ext S'' S'; rfl
  | mul x z hx hz ihx ihz =>
      have hbp : BlockPreserving μ.cells.card
          (seminormalRep q hq0 hq2 (m + 1) hN (heckeIncl ℝ q q⁻¹ m x)) := by
        rw [hN]
        exact seminormalRep_heckeIncl_mem_blockSubalgebra hq0 hq2 m hN x
      rw [map_mul, map_mul, map_mul, compress_mul c hc hbp, ihx, ihz]


end SeminormalRep
end QOU.SchurWeyl
