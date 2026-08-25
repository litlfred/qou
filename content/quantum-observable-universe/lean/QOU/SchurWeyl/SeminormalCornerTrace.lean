import QOU.SchurWeyl.SeminormalBlockEquality
import QOU.Mathlib.SYTBranchingRule

/-!
# QOU.SchurWeyl.SeminormalCornerTrace — the block trace as a sum over corners

`SeminormalBlockTrace` reduced `tr(ρ_μ(ι y) · σ_{|μ|-1})` to a diagonal sum over `SYT μ`:

`∑_T ρ_μ(ι y)_{TT} · a(axialDist T (|μ|-1))`.

`SeminormalBlockEquality` then showed that on the block of a corner `c` that matrix is the
downstairs matrix `ρ_{μ ∖ c}(y)`.  This file puts the two together and **splits the `T`-sum by the
cell carrying the top entry**, which by `SYTBranchingRule` is exactly a sum over the removable
corners of `μ`:

`tr(ρ_μ(ι y) · σ_{|μ|-1}) = ∑_{c corner of μ} ∑_{S : SYT (μ ∖ c)} ρ_{μ∖c}(y)_{SS} · a(c(c) − c(r_S))`

where `r_S` is the cell of `S` carrying *its* top entry — a removable corner of `μ ∖ c`.

That right-hand side is the shape the Markov condition is stated in: the inner factor depends on the
downstairs tableau only through `r_S`, so summing over `μ` with weights and reindexing
(`YoungDiagramCornerReindex`) turns the whole thing into `OcneanuWeightMarkovCorner`'s per-corner
identity `∑_{s addable} w_{μ+s}·a(c(s) − c(r)) = z·w_μ`.

| | |
|---|---|
| `branchEquiv` | `Σ_{c corner} SYT (μ ∖ c) ≃ SYT μ`, from `branchInv`'s two bijectivity halves |
| `axialDist_insertMax_top` | the last axial distance of a re-inserted tableau is `c(c) − c(r_S)` |
| `trace_heckeIncl_mul_lastGen_corner` | the decomposition itself |

## What is still missing

The `λ`-sum with weights — step 3 of bean `qou-uer7`, and now the only gap.  The per-`λ`
arithmetic is here; the corner identity is in `OcneanuWeightMarkovCorner`; what remains is to sum
over `λ` and reindex.

## Base ring (§7c)

`ℝ`, inherited from `genMat` and `seminormalParam`; nothing archimedean is added here.

LaTeX label: `thm:seminormal-corner-trace`
-/

namespace QOU.SchurWeyl
namespace SeminormalRep

open QOU.Mathlib QOU.SchurWeyl.TableauCells QOU.SchurWeyl.Seminormal QOU.SchurWeyl.HeckeInclusion

variable {μ : YoungDiagram}

/-- Removing a corner from a diagram of size `m + 2` leaves one of size `m + 1`. -/
theorem card_eraseCorner_of_card {m : ℕ} (c : ℕ × ℕ) (hc : IsCornerCell μ c)
    (hN : μ.cells.card = m + 2) : (eraseCorner μ c hc).cells.card = m + 1 := by
  have := card_eraseCorner μ c hc; omega

/-- **The branching rule as an equivalence.**  `SYTBranchingRule` proves `branchInv` injective and
surjective separately (it needed only the cardinality); the assembly needs the map itself. -/
noncomputable def branchEquiv (hμ : 0 < μ.cells.card) :
    (Σ c : {c : ℕ × ℕ // IsCornerCell μ c}, StandardYoungTableau (eraseCorner μ c.1 c.2))
      ≃ StandardYoungTableau μ :=
  Equiv.ofBijective _ ⟨branchInv_injective (μ := μ), branchInv_surjective (μ := μ) hμ⟩

@[simp] theorem branchEquiv_apply (hμ : 0 < μ.cells.card) (p) :
    branchEquiv (μ := μ) hμ p = insertMax p.1.1 p.1.2 p.2 := rfl

/-- **The last axial distance of a re-inserted tableau.**  `insertMax c S` carries `|μ|` at `c` and
`|μ| − 1` wherever `S` carries it, so the distance between the two top cells is `c(c) − c(r_S)`.
This is where the corner `c` enters the arithmetic — as the *content* of the added cell. -/
theorem axialDist_insertMax_top {m : ℕ} (hN : μ.cells.card = m + 2)
    (c : ℕ × ℕ) (hc : IsCornerCell μ c) (S : StandardYoungTableau (eraseCorner μ c hc)) :
    axialDist (insertMax c hc S) (m + 1) = axialDistance (cellOf S (m + 1)) c := by
  have hs : (eraseCorner μ c hc).cells.card = m + 1 := card_eraseCorner_of_card c hc hN
  have h1 : cellOf (insertMax c hc S) (m + 1) = cellOf S (m + 1) :=
    cellOf_insertMax c hc S ⟨by omega, by omega⟩
  have h2 : cellOf (insertMax c hc S) (m + 2) = c := by
    have := cellOf_insertMax_top c hc S
    rwa [hN] at this
  unfold axialDist
  rw [h1, show m + 1 + 1 = m + 2 from rfl, h2]

/-- **The block trace as a sum over corners.**  Splitting the diagonal sum by the cell carrying the
top entry replaces `SYT μ` by `Σ_{c corner} SYT (μ ∖ c)`; on each block the matrix is the downstairs
one and the Hoefsmit parameter is evaluated at `c(c) − c(r_S)`. -/
theorem trace_heckeIncl_mul_lastGen_corner {q : ℝ} (hq0 : q ≠ 0) (hq2 : q ^ 2 ≠ 1)
    {m : ℕ} (hN : μ.cells.card = m + 2) (y : Hecke ℝ q q⁻¹ m) :
    ((seminormalRep q hq0 hq2 (m + 1) hN (heckeIncl ℝ q q⁻¹ m y))
        * genMat q (m + 1) (by omega) (by omega)).trace
      = ∑ c : {c : ℕ × ℕ // IsCornerCell μ c},
          ∑ S : StandardYoungTableau (eraseCorner μ c.1 c.2),
            (seminormalRep q hq0 hq2 m (card_eraseCorner_of_card c.1 c.2 hN) y) S S
              * seminormalParam q (axialDistance (cellOf S (m + 1)) c.1) := by
  classical
  have hμ : 0 < μ.cells.card := by omega
  rw [trace_heckeIncl_mul_lastGen hq0 hq2 m hN y]
  rw [← Equiv.sum_comp (branchEquiv (μ := μ) hμ)]
  rw [Fintype.sum_sigma]
  refine Finset.sum_congr rfl fun c _ => Finset.sum_congr rfl fun S _ => ?_
  have hcomp := compress_seminormalRep_heckeIncl hq0 hq2 m hN c.1 c.2
    (card_eraseCorner_of_card c.1 c.2 hN) y
  have hentry := congrArg (fun M => M S S) hcomp
  simp only at hentry
  rw [show (branchEquiv (μ := μ) hμ ⟨c, S⟩) = insertMax c.1 c.2 S from rfl]
  rw [axialDist_insertMax_top hN c.1 c.2 S, ← hentry]
  rfl

end SeminormalRep
end QOU.SchurWeyl
