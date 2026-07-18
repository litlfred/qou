import QOU.Mathlib.StandardYoungTableau
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Data.Nat.Factorial.Basic

/-!
# QOU.Mathlib.HookLengthFormula — arm / leg / hook lengths and the HLF target

Foundation for the **hook-length formula** (Frame–Robinson–Thrall 1954), the
Mathlib-gap infra that computes `#SYT(μ)` in closed form — the unlock for the
tabulated character coefficients `c_λ ∈ {1,3,8,10}` of `symbolic_character_table`
(bean `qou-tqab`; see `QOU.BraidKnot.SytSmallShapeCounts` for the hand-enumerated
`c_λ = 1` case that this generalises).

This file supplies the **definitional layer** — arm, leg, and hook lengths of a
cell, and the hook-length product over a diagram — sorry-free, plus the small
structural facts (positivity, the closed arm+leg+1 form on cells). The HLF itself,

  `#SYT(μ) · ∏_{c ∈ μ} hook(c) = |μ|!`,

is stated as the target with a single cited `sorry`: its proof (via RSK or the
Frame–Robinson–Thrall / Novelli–Pak–Stoyanovskii bijection) is a substantial
Mathlib-upstream-scale contribution, tracked as the next step.

## Main definitions

* `YoungDiagram.armLength` / `legLength` / `hookLength` — of a cell `(i,j)`.
* `YoungDiagram.hookLengthProduct` — `∏_{c ∈ μ} hook(c)`.

## Main statements

* `hookLength_pos` — hook lengths are positive.
* `hookLengthProduct_pos` — the product is positive.
* `numStandardYoungTableaux_mul_hookLengthProduct` — the HLF (stated; one cited `sorry`).

-- Ref: [manuscript] hook-length formula (Frame–Robinson–Thrall 1954); Mathlib-upstream target
-/

open scoped BigOperators

namespace YoungDiagram

variable (μ : YoungDiagram)

/-- **Arm length** of cell `(i, j)`: the number of cells strictly to its right in
    row `i` (`rowLen i − j − 1`). -/
def armLength (i j : ℕ) : ℕ := μ.rowLen i - j - 1

/-- **Leg length** of cell `(i, j)`: the number of cells strictly below it in
    column `j` (`colLen j − i − 1`). -/
def legLength (i j : ℕ) : ℕ := μ.colLen j - i - 1

/-- **Hook length** of cell `(i, j)`: arm + leg + 1 (the cell, its arm, and its leg). -/
def hookLength (i j : ℕ) : ℕ := μ.armLength i j + μ.legLength i j + 1

/-- Hook lengths are always positive (the `+ 1` counts the cell itself). -/
theorem hookLength_pos (i j : ℕ) : 0 < μ.hookLength i j := Nat.succ_pos _

/-- On a **cell** `(i, j) ∈ μ`, the hook length is the closed form
    `(rowLen i − j) + (colLen j − i) − 1`. On a cell `j < rowLen i` and
    `i < colLen j`, so arm `= rowLen i − j − 1` and leg `= colLen j − i − 1`
    are the honest right/below counts. -/
theorem hookLength_eq_of_mem {i j : ℕ} (h : (i, j) ∈ μ) :
    μ.hookLength i j = (μ.rowLen i - j) + (μ.colLen j - i) - 1 := by
  have hj : j < μ.rowLen i := mem_iff_lt_rowLen.mp h
  have hi : i < μ.colLen j := mem_iff_lt_colLen.mp h
  simp only [hookLength, armLength, legLength]
  omega

/-- **The hook-length product** `∏_{c ∈ μ} hook(c)` — the denominator of the HLF. -/
def hookLengthProduct : ℕ := ∏ c ∈ μ.cells, μ.hookLength c.1 c.2

/-- The hook-length product is positive (a product of positive hook lengths). -/
theorem hookLengthProduct_pos : 0 < μ.hookLengthProduct := by
  rw [hookLengthProduct]
  exact Finset.prod_induction _ (0 < ·) (fun _ _ ha hb => Nat.mul_pos ha hb)
    Nat.zero_lt_one (fun c _ => μ.hookLength_pos c.1 c.2)

end YoungDiagram

namespace QOU.Mathlib

open YoungDiagram

/-- **The hook-length formula (target)**: for every Young diagram `μ` with
    `n = |μ|` cells, the number of standard Young tableaux times the hook-length
    product equals `n!`:

      `#SYT(μ) · ∏_{c ∈ μ} hook(c) = n!`.

    Equivalently `#SYT(μ) = n! / ∏ hook(c)`. This is the closed form that pins the
    per-shape counts (e.g. the hook `(2,1)`: hooks `3·1·1 = 3`, so
    `#SYT = 3!/3 = 2`, matching `SytSmallShapeCounts.card_SYT_mu21`).

    Stated as the infra target; the proof (RSK, or the
    Frame–Robinson–Thrall / Novelli–Pak–Stoyanovskii probabilistic bijection) is
    the tracked next step — a Mathlib-upstream-scale contribution. -/
theorem numStandardYoungTableaux_mul_hookLengthProduct (μ : YoungDiagram) :
    numStandardYoungTableaux μ * μ.hookLengthProduct = (μ.cells.card).factorial := by
  -- Ref: [manuscript] hook-length formula (Frame–Robinson–Thrall 1954). The RSK /
  --   FRT bijection is not yet in Mathlib at the pinned toolchain; this states the
  --   target with the definitional layer (arm/leg/hook, hookLengthProduct) proved
  --   above. Discharging it is the Mathlib-upstream infra step (bean qou-tqab).
  sorry

end QOU.Mathlib
