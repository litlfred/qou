import QOU.SchurWeyl.SeminormalCornerTrace
import QOU.Mathlib.YoungDiagramCornerReindex

/-!
# QOU.SchurWeyl.MarkovAssembly — the λ-sum, and the Markov condition modulo one identity

`SeminormalCornerTrace` decomposed the block trace over the removable corners of a single `λ`.
`YoungDiagramCornerReindex` supplied the exchange `(λ, removable corner) ↔ (λ ∖ c, addable corner)`
as a double-sum reindexing.  This file runs the two together and consumes
`OcneanuWeightMarkovCorner`'s per-corner identity, giving the Markov condition itself:

`∑_{|λ| = m+2} w_λ · tr(ρ_λ(ι y) · σ_{m+1}) = z · ∑_{|ν| = m+1} w_ν · tr(ρ_ν(y))`

for every `y ∈ H_{m+1}(q)`.

## What it is conditional on, and what that is worth

The corner identity is a **hypothesis** of `markov_of_corner_identity`, not an axiom and not a
`sorry`:

`∀ ν with |ν| = m+1, ∀ removable corner r of ν:
   ∑_{s addable to ν} w_{ν+s} · a(c(s) − c(r)) = z · w_ν`.

So what is proved here is *the reduction*: the Markov condition for the weighted seminormal trace
**is** that finite arithmetic identity, for any weight function whatever.  Everything
representation-theoretic — the branching decomposition, the block structure of `σ_{m+1}`, the
Hoefsmit entry, the reindexing — is discharged.  `OcneanuWeightMarkovCorner` proves the hypothesis
at convention D for the ≤2-row diagrams the trace lives on; the general-`n` statement is what
`computations/schurweyl/ocneanu_markov_corner_reduction.py` tests exactly at symbolic `z` for every
partition of `n ≤ 6`.

This closes step 3 of bean `qou-uer7` — and with it the assembly the file docstrings of
`OcneanuWeightMarkovCorner` and `SeminormalBlockEquality` both flag as missing.  Those flags are
now stale in one direction: the *reduction* is formalised; the corner identity **at general `n`**
is not.

## Base ring (§7c)

`ℝ`, inherited from `seminormalRep` and `seminormalParam`; nothing archimedean is added here.

LaTeX label: `thm:markov-assembly`
-/

namespace QOU.SchurWeyl
namespace SeminormalRep

open QOU.Mathlib QOU.SchurWeyl.TableauCells QOU.SchurWeyl.Seminormal QOU.SchurWeyl.HeckeInclusion

variable {μ : YoungDiagram}

/-- The cell carrying a tableau's top entry is a removable corner. -/
theorem isCornerCell_cellOf_card (T : StandardYoungTableau μ) (h : 0 < μ.cells.card) :
    IsCornerCell μ (cellOf T μ.cells.card) := by
  obtain ⟨c, hcν, hc, hmax⟩ := exists_corner_entry_eq_card T h
  rw [cellOf_unique T ((YoungDiagram.mem_cells c).mpr hcν) hmax]
  exact hc

/-- **The Markov condition, modulo the corner identity.**  For any weight function `w` satisfying
the per-corner identity, the `w`-weighted seminormal trace of `ι y · σ_{m+1}` over the diagrams of
size `m + 2` is `z` times the `w`-weighted trace of `y` over those of size `m + 1`.

The proof is the three steps the bean names: decompose each block trace over corners
(`trace_heckeIncl_mul_lastGen_corner`), reindex the resulting double sum
(`sum_corner_eq_sum_addable`), then swap the inner sums so the corner identity applies at
`r = ` the cell carrying each downstairs tableau's top entry. -/
theorem markov_of_corner_identity {q z : ℝ} (hq0 : q ≠ 0) (hq2 : q ^ 2 ≠ 1) {m : ℕ}
    (w : YoungDiagram → ℝ)
    (hcorner : ∀ ν : YoungDiagram, ν.cells.card = m + 1 → ∀ r : ℕ × ℕ, IsCornerCell ν r →
      ∑ s : {s : ℕ × ℕ // IsAddableCell ν s},
          w (addCell ν s.1 s.2) * seminormalParam q (axialDistance r s.1) = z * w ν)
    (y : Hecke ℝ q q⁻¹ m) :
    ∑ L : {ρ : YoungDiagram // ρ.cells.card = m + 2},
        w L.1 * ((seminormalRep q hq0 hq2 (m + 1) L.2 (heckeIncl ℝ q q⁻¹ m y))
          * genMat q (m + 1) (by omega) L.2.ge).trace
      = z * ∑ ν : {ν : YoungDiagram // ν.cells.card = m + 1},
          w ν.1 * (seminormalRep q hq0 hq2 m ν.2 y).trace := by
  classical
  set f : {ν : YoungDiagram // ν.cells.card = m + 1} → (ℕ × ℕ) → ℝ :=
    fun ν s => w (addCellOrSelf ν.1 s) *
      ∑ S : StandardYoungTableau ν.1,
        (seminormalRep q hq0 hq2 m ν.2 y) S S * seminormalParam q (axialDistance (cellOf S (m + 1)) s)
    with hf
  -- Step 1: the per-`λ` corner decomposition, with the weight rewritten on the erased diagram.
  have step1 : ∀ L : {ρ : YoungDiagram // ρ.cells.card = m + 2},
      w L.1 * ((seminormalRep q hq0 hq2 (m + 1) L.2 (heckeIncl ℝ q q⁻¹ m y))
          * genMat q (m + 1) (by omega) L.2.ge).trace
        = ∑ c : {c : ℕ × ℕ // IsCornerCell L.1 c},
            f ⟨eraseCorner L.1 c.1 c.2, by
              have := card_eraseCorner L.1 c.1 c.2
              have := L.2
              omega⟩ c.1 := by
    intro L
    rw [trace_heckeIncl_mul_lastGen_corner hq0 hq2 L.2 y, Finset.mul_sum]
    refine Finset.sum_congr rfl fun c _ => ?_
    rw [hf]
    have hadd : addCellOrSelf (eraseCorner L.1 c.1 c.2) c.1 = L.1 := by
      rw [addCellOrSelf_of (isAddableCell_eraseCorner c.1 c.2), addCell_eraseCorner]
    simp only [hadd]
  rw [Finset.sum_congr rfl fun L _ => step1 L]
  -- Step 2: the reindexing.
  rw [sum_corner_eq_sum_addable (m + 1) f]
  -- Step 3: swap the two inner sums and consume the corner identity.
  rw [Finset.mul_sum]
  refine Finset.sum_congr rfl fun ν _ => ?_
  rw [hf]
  simp only
  have hcell : ∀ S : StandardYoungTableau ν.1, IsCornerCell ν.1 (cellOf S (m + 1)) := by
    intro S
    have h := isCornerCell_cellOf_card S (by rw [ν.2]; omega)
    rwa [ν.2] at h
  have hstep : ∀ x : {s : ℕ × ℕ // IsAddableCell ν.1 s},
      w (addCellOrSelf ν.1 x.1) *
          ∑ S : StandardYoungTableau ν.1,
            (seminormalRep q hq0 hq2 m ν.2 y) S S
              * seminormalParam q (axialDistance (cellOf S (m + 1)) x.1)
        = ∑ S : StandardYoungTableau ν.1,
            (seminormalRep q hq0 hq2 m ν.2 y) S S
              * (w (addCell ν.1 x.1 x.2) * seminormalParam q (axialDistance (cellOf S (m + 1)) x.1)) := by
    intro x
    rw [addCellOrSelf_of x.2, Finset.mul_sum]
    exact Finset.sum_congr rfl fun S _ => by ring
  rw [Finset.sum_congr rfl fun x _ => hstep x, Finset.sum_comm]
  have hinner : ∀ S : StandardYoungTableau ν.1,
      ∑ x : {s : ℕ × ℕ // IsAddableCell ν.1 s},
          (seminormalRep q hq0 hq2 m ν.2 y) S S
            * (w (addCell ν.1 x.1 x.2) * seminormalParam q (axialDistance (cellOf S (m + 1)) x.1))
        = (seminormalRep q hq0 hq2 m ν.2 y) S S * (z * w ν.1) := by
    intro S
    rw [← Finset.mul_sum, hcorner ν.1 ν.2 (cellOf S (m + 1)) (hcell S)]
  rw [Finset.sum_congr rfl fun S _ => hinner S, ← Finset.sum_mul, Matrix.trace]
  simp only [Matrix.diag_apply]
  ring

end SeminormalRep
end QOU.SchurWeyl
