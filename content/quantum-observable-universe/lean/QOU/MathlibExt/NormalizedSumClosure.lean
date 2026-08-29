import QOU.MathlibExt.MolienFakeDegreeGeneralN
import QOU.MathlibExt.MacdonaldTelescopeGeneralX
import QOU.MathlibExt.CarrierReindexBridge

/-!
# QOU.MathlibExt.NormalizedSumClosure — `normalizedSum n q = 1` from the telescope (assembly)

The general-`n` fake-degree residual `normalizedSum n q = 1` closes from the corpus general-X
Macdonald telescope `MacdonaldTelescopeGeneralX.telescope_generalX` at `X = 0`, via the per-λ
**convention bridge**

  `q^{−κ_λ}/hookProd_q(λ) = schurElement(q², 0, λ)·(1 − q²)^n`

(route verified exact `n≤5` in `computations/qbeta/fake_degree_via_telescope_probe.py`; audit
`docs/audits/2026-08-29-normalizedsum-closes-via-telescope.md`).

This file is the **assembly**: it proves `normalizedSum n q = 1` **given** the convention bridge
(`hconv`), by (i) rewriting each summand, (ii) reindexing `Nat.Partition n → {ν // card = n}` via
`partitionShapeEquiv` (with `dimSYT p = numStandardYoungTableaux (partitionShape p)` definitional and
`(partitionShape p).rowLens = toList p`), and (iii) applying `telescope_generalX` at `X = 0`. The
residual is thus exactly the convention bridge (a `foldl` monomial/sign identity — its per-cell brick
`NormalizedSumTelescopeBridge.one_sub_qsq_pow_eq` is sorry-free — plus the n-statistic identity
`κ_λ = Σ_x h_x − |λ| − 2 n(λ)`). §3b-cond: this is a rigorous conditional result modulo `hconv`.
-/

namespace QOU.MathlibExt.NormalizedSumClosure

open QOU.MathlibExt.MolienFakeDegreeGeneralN
open QOU.MathlibExt.QPartitionCombinatorics
open QOU.MathlibExt.WenzlSchurElement
open QOU.MathlibExt.MacdonaldTelescopeGeneralX
open QOU.Mathlib.PartitionListBridge (toList)
open QOU.Mathlib (dimSYT numStandardYoungTableaux partitionShape partitionShapeEquiv)

/-- **`normalizedSum n q = 1`, given the convention bridge.** Assembles the telescope closure:
the per-λ bridge `hconv`, the `partitionShapeEquiv` reindex, and `telescope_generalX` at `X = 0`. -/
theorem normalizedSum_eq_one_of_convBridge (n : ℕ) (q : ℝ) (hq2 : 1 < q ^ 2)
    (hgen : ∀ k : ℤ, k ≠ 0 → (q ^ 2) ^ k ≠ 1)
    (hconv : ∀ p : Nat.Partition n,
        q ^ (-(QPartitionCombinatorics.contentSum (toList p))) / hookProd q (toList p)
          = schurElement (q ^ 2) 0 (toList p) * (1 - q ^ 2) ^ n) :
    normalizedSum n q = 1 := by
  have hne : (1 : ℝ) - q ^ 2 ≠ 0 := by nlinarith
  -- (i) rewrite each summand via the convention bridge, factoring (1-q²)^n
  have hsum : normalizedSum n q
      = (∑ p : Nat.Partition n,
          (dimSYT p : ℝ) * schurElement (q ^ 2) 0 (toList p)) * (1 - q ^ 2) ^ n := by
    unfold normalizedSum
    rw [Finset.sum_mul]
    refine Finset.sum_congr rfl (fun p _ => ?_)
    rw [mul_div_assoc, hconv p]; ring
  -- (ii) reindex Nat.Partition n → {ν // card = n} via partitionShapeEquiv
  have hreindex :
      (∑ p : Nat.Partition n, (dimSYT p : ℝ) * schurElement (q ^ 2) 0 (toList p))
        = ∑ ν : {ν : YoungDiagram // ν.cells.card = n},
            (numStandardYoungTableaux ν.1 : ℝ) * schurElement (q ^ 2) 0 ν.1.rowLens := by
    refine (Fintype.sum_equiv (partitionShapeEquiv n) _ _ (fun p => ?_))
    rw [QOU.MathlibExt.CarrierReindexBridge.numSTY_partitionShapeEquiv,
        QOU.MathlibExt.CarrierReindexBridge.rowLens_partitionShapeEquiv]
  -- (iii) telescope at X = 0
  rw [hsum, hreindex, telescope_generalX n (q ^ 2) 0 hq2 hgen, sub_zero, div_pow, one_pow]
  exact one_div_mul_cancel (pow_ne_zero n hne)

end QOU.MathlibExt.NormalizedSumClosure
