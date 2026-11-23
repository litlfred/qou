import QOU.SchurWeyl.SeminormalBlockEquality
import QOU.SchurWeyl.MarkovAssembly

/-!
# QOU.SchurWeyl.PieriSupport — the Pieri rule for the Hecke tower, general `n`

Let `y ∈ H_{m+1}(q)` be supported on one Wedderburn block `λ ⊢ m + 1`: its seminormal matrix is
zero on every other diagram of size `m + 1`. Include `y` into `H_{m+2}(q)` and multiply by any
`a ∈ H_{m+2}(q)`, for example a degree-one element `1 + ∑ φ_i σ_i`. Then the seminormal matrix of
`a · ι(y)` vanishes on every diagram `μ ⊢ m + 2` that is not `λ` plus one box.

**Proof.** `ρ_μ(ι y)` preserves the blocks of `SYT μ` cut out by the cell of the top entry
(`seminormalRep_heckeIncl_mem_blockSubalgebra`). The block of a corner `c` is the image of
`insertMax`, and there `ρ_μ(ι y)` restricts to `ρ_{μ ∖ c}(y)`
(`compress_seminormalRep_heckeIncl`). If no corner `c` has `μ ∖ c = λ`, every block vanishes, so
`ρ_μ(ι y) = 0` and hence `ρ_μ(a · ι y) = ρ_μ(a) · 0 = 0`.

So the support of `a · ι(y)` lies in `{λ + □}`. Within `H_{m+1}(q)` the support of `a · y` stays
`{λ}`, because a block is a two-sided ideal. Removing a box never happens for a product; it is the
restriction `H_{m+1} → H_m`, a different operation.

## Base ring (§7c)

`ℝ`, inherited from `BlockPreserving` and `compress_seminormalRep_heckeIncl`, which are stated
over `ℝ` because `genMat` is. Nothing archimedean is used here; `q` is only required to be nonzero
and not a root of unity.

References: [fulton1997] Ch. 2; [ram1997] for the Hecke branching rule.

LaTeX label: `prop:pieri-photon-shift`
-/

namespace QOU.SchurWeyl
namespace SeminormalRep

open QOU.Mathlib QOU.SchurWeyl.TableauCells QOU.SchurWeyl.HeckeInclusion

variable {q : ℝ} (hq0 : q ≠ 0) (hq2 : GenericParameter.NotRootOfUnity q)

/-- An element of `H_{m+1}(q)` supported on the single block `λ`. -/
def SupportedOn (m : ℕ) (lam : YoungDiagram) (y : Hecke ℝ q q⁻¹ m) : Prop :=
  ∀ (ν : YoungDiagram) (h : ν.cells.card = m + 1), ν ≠ lam → seminormalRep q hq0 hq2 m h y = 0

/-- **The inclusion of a block-supported element vanishes off `λ + □`.** -/
theorem seminormalRep_heckeIncl_eq_zero_of_not_addable (m : ℕ) (lam : YoungDiagram)
    (y : Hecke ℝ q q⁻¹ m) (hy : SupportedOn hq0 hq2 m lam y)
    (μ : YoungDiagram) (hN : μ.cells.card = m + 2)
    (hμ : ∀ (c : ℕ × ℕ) (hc : IsCornerCell μ c), eraseCorner μ c hc ≠ lam) :
    seminormalRep q hq0 hq2 (m + 1) hN (heckeIncl ℝ q q⁻¹ m y) = 0 := by
  have hbp : BlockPreserving μ.cells.card
      (seminormalRep q hq0 hq2 (m + 1) hN (heckeIncl ℝ q q⁻¹ m y)) := by
    rw [hN]
    exact seminormalRep_heckeIncl_mem_blockSubalgebra hq0 hq2 m hN y
  ext T S
  rw [Matrix.zero_apply]
  by_cases hTS : cellOf T μ.cells.card = cellOf S μ.cells.card
  · have hpos : 0 < μ.cells.card := by omega
    have hc : IsCornerCell μ (cellOf T μ.cells.card) := isCornerCell_cellOf_card T hpos
    generalize hcdef : cellOf T μ.cells.card = c at hc hTS
    obtain ⟨T', hT'⟩ := exists_insertMax_of_cellOf_top c hc T hcdef
    obtain ⟨S', hS'⟩ := exists_insertMax_of_cellOf_top c hc S hTS.symm
    rw [← hT', ← hS']
    have hNs : (eraseCorner μ c hc).cells.card = m + 1 := by
      have := card_eraseCorner μ c hc; omega
    have hcomp := compress_seminormalRep_heckeIncl hq0 hq2 m hN c hc hNs y
    have hz := hy _ hNs (hμ c hc)
    have := congrArg (fun X => X T' S') hcomp
    simp only [compress, Matrix.of_apply] at this
    rw [this, hz, Matrix.zero_apply]
  · exact hbp T S hTS

/-- **Pieri rule for the Hecke tower.** For `y ∈ H_{m+1}(q)` supported on `λ` and any
`a ∈ H_{m+2}(q)`, the seminormal matrix of `a · ι(y)` vanishes on every `μ ⊢ m + 2` that is not
`λ` plus one box. -/
theorem pieri_support (m : ℕ) (lam : YoungDiagram) (y : Hecke ℝ q q⁻¹ m)
    (hy : SupportedOn hq0 hq2 m lam y) (a : Hecke ℝ q q⁻¹ (m + 1))
    (μ : YoungDiagram) (hN : μ.cells.card = m + 2)
    (hμ : ∀ (c : ℕ × ℕ) (hc : IsCornerCell μ c), eraseCorner μ c hc ≠ lam) :
    seminormalRep q hq0 hq2 (m + 1) hN (a * heckeIncl ℝ q q⁻¹ m y) = 0 := by
  rw [map_mul, seminormalRep_heckeIncl_eq_zero_of_not_addable hq0 hq2 m lam y hy μ hN hμ,
    mul_zero]

/-- The same, read as a support statement: if `a · ι(y)` acts nontrivially on `μ`, then `μ` is
`λ` plus one box. -/
theorem exists_corner_of_pieri_ne_zero (m : ℕ) (lam : YoungDiagram) (y : Hecke ℝ q q⁻¹ m)
    (hy : SupportedOn hq0 hq2 m lam y) (a : Hecke ℝ q q⁻¹ (m + 1))
    (μ : YoungDiagram) (hN : μ.cells.card = m + 2)
    (hne : seminormalRep q hq0 hq2 (m + 1) hN (a * heckeIncl ℝ q q⁻¹ m y) ≠ 0) :
    ∃ (c : ℕ × ℕ) (hc : IsCornerCell μ c), eraseCorner μ c hc = lam := by
  by_contra h
  push_neg at h
  exact hne (pieri_support hq0 hq2 m lam y hy a μ hN h)

/-- Within one level the support does not move: a block is a two-sided ideal, so `a · y` is still
supported on `λ` for every `a ∈ H_{m+1}(q)`. -/
theorem supportedOn_mul_left (m : ℕ) (lam : YoungDiagram) (y : Hecke ℝ q q⁻¹ m)
    (hy : SupportedOn hq0 hq2 m lam y) (a : Hecke ℝ q q⁻¹ m) :
    SupportedOn hq0 hq2 m lam (a * y) := by
  intro ν h hν
  rw [map_mul, hy ν h hν, mul_zero]

end SeminormalRep
end QOU.SchurWeyl
