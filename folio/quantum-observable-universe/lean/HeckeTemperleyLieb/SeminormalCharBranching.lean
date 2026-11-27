/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import HeckeTemperleyLieb.SeminormalCornerTrace

/-!
# Branching of seminormal characters

G3.4c (bean `qou-gl343`), identification step D, seminormal half.

For `|λ| = m + 2` and `y ∈ H_{m+1}(q)`,

`χ^λ(ι y) = Σ_{c corner of λ} χ^{λ ∖ c}(y)`  (`trace_seminormalRep_heckeIncl`).

The proof splits `SYT λ` by the cell holding the top entry (`branchEquiv`) and reads each block
off `compress_seminormalRep_heckeIncl`.  It is the same decomposition
`trace_heckeIncl_mul_lastGen_corner` uses, without the last generator.

## Base ring (§7c)

Any field, `q ≠ 0` and not a root of unity (inherited from `seminormalRep`).
-/

namespace QOU.SchurWeyl

variable {K : Type*} [Field K]
namespace SeminormalRep

open QOU.Mathlib QOU.SchurWeyl.TableauCells QOU.SchurWeyl.HeckeInclusion

variable {μ : YoungDiagram}

/-- **Branching of seminormal characters.** -/
theorem trace_seminormalRep_heckeIncl {q : K} (hq0 : q ≠ 0)
    (hq2 : GenericParameter.NotRootOfUnity q) {m : ℕ} (hN : μ.cells.card = m + 2)
    (y : Hecke K q q⁻¹ m) :
    (seminormalRep q hq0 hq2 (m + 1) hN (heckeIncl K q q⁻¹ m y)).trace
      = ∑ c : {c : ℕ × ℕ // IsCornerCell μ c},
          (seminormalRep q hq0 hq2 m (card_eraseCorner_of_card c.1 c.2 hN) y).trace := by
  classical
  have hμ : 0 < μ.cells.card := by omega
  rw [Matrix.trace, ← Equiv.sum_comp (branchEquiv (μ := μ) hμ), Fintype.sum_sigma]
  refine Finset.sum_congr rfl fun c _ => ?_
  rw [Matrix.trace]
  refine Finset.sum_congr rfl fun S _ => ?_
  have hcomp := compress_seminormalRep_heckeIncl hq0 hq2 m hN c.1 c.2
    (card_eraseCorner_of_card c.1 c.2 hN) y
  exact congrArg (fun M => M S S) hcomp

end SeminormalRep
end QOU.SchurWeyl
