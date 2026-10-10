import QOU.Information.GCTSchurMultiplicity

/-!
# QOU.Information.GCTPerRankObstruction — the TL multiplicity drop at every rank

`GCTSchurMultiplicity` exhibits a *single* proved GCT multiplicity obstruction
(the block `[2]` present at the substrate, dropped at the TL locus `X = Q^{-1}`).
This file extends it to **every rank**: for each `n ≥ 2` there is a size-`n`
partition — the single row `[n]`, whose cell `(0,1)` has content `1` — on which
the substrate and TL-locus multiplicity data are `SeparatedAt`. So the
Temperley–Lieb multiplicity drop is not an isolated coincidence; it occurs at
**all scales**, giving the `∀ n, ∃ λ` structural shape the GCT program needs.

**STRICT honest scope.** This is the shape of a per-rank obstruction for the
**substrate-vs-TL-locus regime** separation. It is deliberately **not** packaged
as a `QouGCTObstruction` instance: that class carries the *counting-hard object
vs every poly-time object* (`VP`-vs-`VNP`) content, which is the open program;
instantiating it from this regime separation would be laundering a proved (but
different) statement into the open one. The class stays instance-free; this file
provides the *structural precedent* (obstructions exist at every rank), not the
`VP`/`VNP` obstruction. All sorry-free; base ring `ℝ` (`schurElement`
archimedean, §7c).
-/

namespace QOU.Information

open QOU.MathlibExt.QPartitionCombinatorics
open QOU.MathlibExt.WenzlSchurElement
open scoped Classical

/-- **The single-row partition `[n]` has a content-`1` cell for `n ≥ 2`.**  Its
    cell `(0,1)` has content `1 − 0 = 1`; the column index `1` is in range
    because the row length `n ≥ 2`. -/
theorem hasContentCell_singleton (n : ℕ) (hn : 2 ≤ n) : HasContentCell [n] 1 := by
  refine ⟨0, ?_, 1, ?_, by decide⟩
  · simp [Partition.length]
  · show (1 : ℕ) < n
    exact lt_of_lt_of_le one_lt_two hn

/-- `[n]` is a size-`n` partition. -/
theorem size_singleton (n : ℕ) : Partition.size [n] = n := by
  simp [Partition.size]

/-- **Per-rank GCT multiplicity obstruction (sorry-free).**  For every `n ≥ 2`,
    the size-`n` single-row partition `[n]` witnesses a `SeparatedAt` between the
    substrate multiplicity data (all blocks present) and the TL-locus data
    (content-`1` blocks dropped at `X = Q^{-1}`).  The multiplicity drop occurs at
    **every** rank. -/
theorem schur_per_rank_obstruction {Q : ℝ} (hQ : 1 < Q) (n : ℕ) (hn : 2 ≤ n) :
    ∃ lam : Partition, lam.size = n ∧
      SeparatedAt (schurMult Q (-1)) (schurMult Q (Q ^ (-(1 : ℤ)))) lam :=
  ⟨[n], size_singleton n, schur_separatedAt hQ (hasContentCell_singleton n hn)⟩

/-- **The obstruction shape at all ranks (sorry-free).**  Packaged as the
    `∀ n, ∃ λ` predicate the GCT program targets — here for the substrate-vs-TL
    *regime* separation.  This is the structural precedent, **not** a
    `QouGCTObstruction` instance (which requires the open `VP`-vs-`VNP` content). -/
theorem schur_obstruction_all_ranks {Q : ℝ} (hQ : 1 < Q) :
    ∀ n : ℕ, 2 ≤ n → ∃ lam : Partition, lam.size = n ∧
      SeparatedAt (schurMult Q (-1)) (schurMult Q (Q ^ (-(1 : ℤ)))) lam :=
  fun n hn => schur_per_rank_obstruction hQ n hn

end QOU.Information
