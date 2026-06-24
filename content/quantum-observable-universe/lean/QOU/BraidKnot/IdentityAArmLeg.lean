import Mathlib.Combinatorics.Young.YoungDiagram
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Tactic

/-!
# QOU.BraidKnot.IdentityAArmLeg — toward the general (all-`n`) proof of Identity (A)

**Status: WIP scaffold (multi-session).** Builds, on **Mathlib's `YoungDiagram`**, the
keystone-carried identity

  **(A)**  `Σ_cells hook(c)² = Σ_cells content(c)² + n²`,

and reduces it — sorry-free down to a single, precisely-stated heart — so the remaining work is
the per-statistic sums, not the whole identity. It complements
[`IdentityIContentDecomposition.lean`](IdentityIContentDecomposition.lean), whose list-model defs
are tuned for `native_decide` (exhaustive `n ≤ 22`, all 4507 partitions) and are hostile to
symbolic proof; this is the symbolic counterpart.

**Foundation.** Built directly on `Mathlib.Combinatorics.Young.YoungDiagram` (`μ.cells`,
`μ.rowLen`, `μ.colLen`, `μ.transpose`). The `transpose` API
(`rowLen_transpose : μ.transpose.rowLen i = μ.colLen i`, and `colLen_transpose`) is exactly the
**conjugation relation** the heart's leg-sums need — `leg μ` over `μ.cells` matches `arm μ.transpose`
over `μ.transpose.cells` under the cell swap `(i,j) ↦ (j,i)`. Hook/arm/leg/content are `ℤ`-valued
to avoid `ℕ`-subtraction.

## Proved (sorry-free)

- `sum_one_eq_numCells` — `Σ_cells 1 = n`.
- `sumSq_hook_expand` — `Σ hook² = Σ arm² + Σ leg² + Σ 1 + 2 Σ(arm·leg) + 2 Σ arm + 2 Σ leg`
  (`Finset`-linearity + `ring`).
- `identityA` — the identity itself, **reduced** to the single heart `statistics_combine`.
- `content_swap`, `leg_eq_arm_transpose`, `sum_arm_transpose_eq_sum_leg` — the **conjugation
  bridge**: content negates and leg↔arm under the transpose cell-swap, so the leg-sum over `μ`
  equals the arm-sum over `μ.transpose`. This is the structural lever the heart trades on.
- `sum_cells_fiberwise` — **cells decompose into rows** (general; the workhorse for every
  per-statistic computation), and `sum_arm_row` / `sum_arm_cells` — the first concrete statistic,
  `Σ arm = Σ_i Σ_{k < rowLen i} k = Σ_i C(rowLen_i, 2)`.

## Remaining (the heart, `sorry` + `-- Ref:`)

`statistics_combine`: the six statistic sums combine to `Σ content² + n²`. Next-session plan: pin
each statistic in closed form, using `transpose` for the leg↔arm conjugation and `mem_iff_lt_rowLen`
to range over cells.

## References

- [manuscript] `docs/audits/2026-06-23-keystone-identity-I-content-decomposition.md` §"Proof of (A)"
- [manuscript] `docs/coordination/s5-so3-keystone.md` (Identity I is the one carried RT input)
-/

open Finset

namespace QOU.BraidKnot.IdentityAArmLeg

/-- Arm of cell `c = (i, j)` in `μ`: cells strictly to the right in the same row. -/
def arm (μ : YoungDiagram) (c : ℕ × ℕ) : ℤ := (μ.rowLen c.1 : ℤ) - (c.2 : ℤ) - 1

/-- Leg of cell `c = (i, j)` in `μ`: cells strictly below in the same column. -/
def leg (μ : YoungDiagram) (c : ℕ × ℕ) : ℤ := (μ.colLen c.2 : ℤ) - (c.1 : ℤ) - 1

/-- Content of cell `(i, j)` is `j − i`. -/
def content (c : ℕ × ℕ) : ℤ := (c.2 : ℤ) - (c.1 : ℤ)

/-- Hook length of `c` is `arm + leg + 1` — the number of cells in the hook of `c`. -/
def hook (μ : YoungDiagram) (c : ℕ × ℕ) : ℤ := arm μ c + leg μ c + 1

/-- Number of cells, `n = |μ|`. -/
def numCells (μ : YoungDiagram) : ℤ := (μ.cells.card : ℤ)

/-- The constant term: `Σ_cells 1 = n`. -/
theorem sum_one_eq_numCells (μ : YoungDiagram) :
    (∑ _c ∈ μ.cells, (1 : ℤ)) = numCells μ := by
  simp [numCells]

/-- **Algebraic expansion of `Σ hook²`** (sorry-free): pure `Finset`-linearity + `ring`.
Reduces Identity (A) to the six per-statistic sums. -/
theorem sumSq_hook_expand (μ : YoungDiagram) :
    ∑ c ∈ μ.cells, (hook μ c) ^ 2
      = (∑ c ∈ μ.cells, (arm μ c) ^ 2) + (∑ c ∈ μ.cells, (leg μ c) ^ 2)
        + (∑ _c ∈ μ.cells, (1 : ℤ)) + 2 * (∑ c ∈ μ.cells, arm μ c * leg μ c)
        + 2 * (∑ c ∈ μ.cells, arm μ c) + 2 * (∑ c ∈ μ.cells, leg μ c) := by
  have hpt : ∀ c, (hook μ c) ^ 2
      = (arm μ c) ^ 2 + (leg μ c) ^ 2 + (1 : ℤ) + 2 * (arm μ c * leg μ c)
        + 2 * (arm μ c) + 2 * (leg μ c) := by
    intro c; simp only [hook]; ring
  simp only [hpt, Finset.sum_add_distrib, Finset.mul_sum]

/-- Content negates under the transpose cell-swap `(i,j) ↦ (j,i)`: `content (j,i) = − content (i,j)`.
Hence `Σ content²` is transpose-invariant — one of the symmetries the heart exploits. -/
theorem content_swap (c : ℕ × ℕ) : content c.swap = - content c := by
  simp only [content, Prod.fst_swap, Prod.snd_swap]; ring

/-- **Pointwise conjugation.** The leg of `c` in `μ` is the arm of `c.swap` in `μ.transpose`:
`leg μ (i,j) = μ.colLen j − i − 1 = μ.transpose.rowLen j − i − 1 = arm μ.transpose (j,i)`. -/
theorem leg_eq_arm_transpose (μ : YoungDiagram) (c : ℕ × ℕ) :
    leg μ c = arm μ.transpose c.swap := by
  simp only [leg, arm, Prod.fst_swap, Prod.snd_swap, YoungDiagram.rowLen_transpose]

/-- **Conjugation relation (leg-sum = transpose arm-sum).** Via the cell swap
`μ.transpose.cells = (prodComm) '' μ.cells`, the arm-sum over `μ.transpose` equals the leg-sum over
`μ`. This is the structural bridge the heart uses to trade leg-statistics for arm-statistics. -/
theorem sum_arm_transpose_eq_sum_leg (μ : YoungDiagram) :
    ∑ c ∈ μ.transpose.cells, arm μ.transpose c = ∑ c ∈ μ.cells, leg μ c := by
  have hmap : μ.transpose.cells = μ.cells.map (Equiv.prodComm ℕ ℕ).toEmbedding := by
    simp [YoungDiagram.transpose, Equiv.finsetCongr_apply]
  rw [hmap, Finset.sum_map]
  refine Finset.sum_congr rfl (fun c _ => ?_)
  simp only [Equiv.coe_toEmbedding, Equiv.prodComm_apply]
  exact (leg_eq_arm_transpose μ c).symm

/-- **Cells decompose into rows** (general, reusable). Any cell-sum is the sum over rows
`i < μ.colLen 0` (the number of rows) of the sum over that row. The workhorse for turning a
cell-statistic into a row-by-row computation. -/
theorem sum_cells_fiberwise (μ : YoungDiagram) (f : ℕ × ℕ → ℤ) :
    (∑ c ∈ μ.cells, f c) = ∑ i ∈ Finset.range (μ.colLen 0), ∑ c ∈ μ.row i, f c := by
  rw [← Finset.sum_fiberwise_of_maps_to (g := Prod.fst) (t := Finset.range (μ.colLen 0))]
  · refine Finset.sum_congr rfl (fun i _ => ?_)
    refine Finset.sum_congr ?_ (fun _ _ => rfl)
    ext c; simp [YoungDiagram.row, YoungDiagram.mem_cells, and_comm]
  · intro c hc
    rw [Finset.mem_range]
    rw [YoungDiagram.mem_cells] at hc
    have h0 : (c.fst, 0) ∈ μ := μ.up_left_mem (le_refl _) (Nat.zero_le _) hc
    rwa [YoungDiagram.mem_iff_lt_colLen] at h0

/-- **Per-row arm sum** = Gauss sum of the row length: `Σ_{c ∈ row i} arm = Σ_{k < rowLen i} k`
(`= rowLen_i·(rowLen_i − 1)/2`), via `row_eq_prod` + the reflection `b ↦ rowLen_i − 1 − b`. -/
theorem sum_arm_row (μ : YoungDiagram) (i : ℕ) :
    (∑ c ∈ μ.row i, arm μ c) = ∑ k ∈ Finset.range (μ.rowLen i), (k : ℤ) := by
  rw [YoungDiagram.row_eq_prod, Finset.sum_product]
  simp only [Finset.sum_singleton, arm]
  rw [← Finset.sum_range_reflect (fun k => (k : ℤ)) (μ.rowLen i)]
  refine Finset.sum_congr rfl (fun b hb => ?_)
  rw [Finset.mem_range] at hb; omega

/-- **`Σ arm` in closed form**: the arm-sum over all cells is `Σ_i Σ_{k < rowLen i} k`
(`= Σ_i C(rowLen_i, 2)`). Combines `sum_cells_fiberwise` with `sum_arm_row`; the first concrete
statistic of the heart. -/
theorem sum_arm_cells (μ : YoungDiagram) :
    (∑ c ∈ μ.cells, arm μ c)
      = ∑ i ∈ Finset.range (μ.colLen 0), ∑ k ∈ Finset.range (μ.rowLen i), (k : ℤ) := by
  rw [sum_cells_fiberwise]
  exact Finset.sum_congr rfl (fun i _ => sum_arm_row μ i)

/-- **The heart (deferred, multi-session).** The six statistic sums combine to `Σ content² + n²`.
This is the only remaining gap in `identityA`; the next-session plan uses the `transpose` API for
the leg↔arm conjugation (`rowLen_transpose`/`colLen_transpose`) and `mem_iff_lt_rowLen` to range
over the cells.
-- Ref: [manuscript] docs/audits/2026-06-23-keystone-identity-I-content-decomposition.md §"Proof of (A)" -/
theorem statistics_combine (μ : YoungDiagram) :
    (∑ c ∈ μ.cells, (arm μ c) ^ 2) + (∑ c ∈ μ.cells, (leg μ c) ^ 2)
        + (∑ _c ∈ μ.cells, (1 : ℤ)) + 2 * (∑ c ∈ μ.cells, arm μ c * leg μ c)
        + 2 * (∑ c ∈ μ.cells, arm μ c) + 2 * (∑ c ∈ μ.cells, leg μ c)
      = (∑ c ∈ μ.cells, (content c) ^ 2) + (numCells μ) ^ 2 := by
  sorry

/-- **Identity (A), general form** — `Σ hook² = Σ content² + n²`, for every Young diagram `μ`.
Proved by the algebraic expansion (`sumSq_hook_expand`) composed with the deferred heart
(`statistics_combine`); discharging `statistics_combine` discharges (A) for all partitions. -/
theorem identityA (μ : YoungDiagram) :
    ∑ c ∈ μ.cells, (hook μ c) ^ 2
      = (∑ c ∈ μ.cells, (content c) ^ 2) + (numCells μ) ^ 2 := by
  rw [sumSq_hook_expand, statistics_combine]

end QOU.BraidKnot.IdentityAArmLeg
