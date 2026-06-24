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
