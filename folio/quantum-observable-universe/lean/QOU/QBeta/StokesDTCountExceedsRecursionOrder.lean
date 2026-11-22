import Init.Data.Nat.Basic
import Init.Data.Int.Basic
import Init.Omega

/-!
# QOU.QBeta.StokesDTCountExceedsRecursionOrder — where the QOU Euler-characteristic machinery closes, and where the knot DT count escapes it

**Bean `qou-qnnq`. Branch `claude/dt-count-categorification-qnnq-2026-08-02`.**
Audit: `docs/audits/2026-08-02-stokes-dt-bridge-moduli-gap-unification.md`.

## The question this file answers (formalize-first, honest negative)

The G3 Stokes-keystone directive: prove the bridge's **first equality**
`Stokes = DT` for the figure-eight `4₁` *as a theorem conditional on a QOU
structure*, deriving the DT count `3` as a **QOU-computable graded Euler
characteristic** (the hint: "Euler = −6") — or report exactly where the
arithmetic fails to close to `3`.

**It does not close to `3`. The QOU Wedderburn/Springer Euler-characteristic
machinery produces `−2`, not `3`.** This file makes that precise and decidable.

## What the QOU Euler-characteristic machinery DOES compute (the closed fragment)

The corpus proves (sorry-free, all `n`: `DeltaLambdaDTIndexGeneralN.dtEulerG_collapse`,
`dtEulerG_eq_deltaLambdaG`) that the **per-partition** Donaldson–Thomas /
3d-index graded Euler characteristic of the Springer shadow `G_λ` (`V_λ`
concentrated in cohomological degree `n(λ)`) collapses to

    χ(G_λ) = Σ_k (-1)^k dim (G_λ)_k = (-1)^{n(λ)} · dim V_λ = Δ_λ,

fully from QOU data — the a-function `n(λ)` (Gröbner–Shirshov jet-order) and the
Wedderburn dimension `dim V_λ`. The figure-eight `4₁` is the closure of the
3-braid `(σ₁σ₂⁻¹)²`, so its natural Wedderburn home is `H₃(q)`, whose blocks are
`λ ⊢ 3`. The **total** DT/3d-index Euler characteristic over those blocks is

    Σ_{λ ⊢ 3} Δ_λ = (-1)^0·1 + (-1)^1·2 + (-1)^3·1 = 1 − 2 − 1 = −2.

Strikingly, `−2` **is** the normalization of the GGM Stokes sandwich:
`A·W₋₁(0)·B·W₋₁(0)ᵀ·C = −2·S⁺(0)` (`StokesQZeroDTCount.ggm_sandwich_qzero`).
So the QOU Euler-characteristic machinery cleanly supplies the sandwich
**prefactor** `−2`. (That this equals `Σ_{λ⊢3} Δ_λ` is recorded as an *unclaimed*
single-knot observation — the corpus's standing anti-single-knot-numerology guard
applies until a cross-knot `5₂` check confirms it; it is **not** wired or asserted
as derived here.)

## Where it FAILS to close to 3 (the honest negative)

The knot Stokes / DT / BPS **count** is `S⁺(0)₀₁ = 3` (the *off-diagonal*), not
the sandwich normalization `−2`. And `−2 ≠ 3`: **no QOU-computable Wedderburn /
Springer Euler characteristic produces the knot DT count.** The count `3` is the
Behrend-signed Donaldson–Thomas / BPS invariant of the *spectral curve*
`A_{4₁}(L,M) = 0` (the character variety), i.e. the rotated 3d-index of the knot
complement `T[4₁]` — a geometric object computed from the triangulation /
exponential-network structure, **not** a graded Euler characteristic over any
Wedderburn/moduli grading the drivers build. The per-partition `Δ_λ` DT
(Springer fibre `𝓑_λ`, attached to a Wedderburn block) and the per-knot `A_ω` DT
(character-variety of the complement) are **different DT objects**; the
Euler-characteristic machinery closes the first, not the second.

This is the knot-level twin of the Rossmann-CC verdict for `Δ_λ`
(`docs/audits/2026-08-02-rossmann-cc-bridge-deltalambda-realization.md`): there
the `Δ_λ` *value* is substrate-derived but the Springer-fibre *DT-realization* is
an external Springer-geometry import (the substrate carries the q-Plancherel
measure + cancelling fake degree, not the Green-function/characteristic-cycle
datum). Same missing categorical input — a Behrend-weighted DT *moduli* — two
levels.

## The internally-derivable structural integer that IS available (and is weaker)

The one knot-level count the drivers *do* supply is the **shape**: the order of
the QOU-owned AJ `q`-difference annihilator (proved sorry-free for `4₁`,
`AJFigureEightAnnihilation.figureEightOperator_annihilates`; its `q → 1`
specialization is the classical A-polynomial `A_{4₁}`), equivalently the
A-polynomial `L`-degree, equivalently the GGM Stokes-matrix **dimension**:
`r_{4₁} = 2`, `r_{5₂} = 3`. This is genuinely internal — but it gives the block
*size*, not the DT *count*: the count strictly exceeds it (`3 > 2`; `5₂`: the
spectrum member `4 > 3`). So even the derivable structural integer
under-determines the DT count.

## Scope (STRICT, anti-laundering)

Scope-(a) structural localization. Derives NO count, axiomatizes NO bridge
(that is `StokesDTBPSBridge`, #4569 — not re-skinned here). The integers `r_K`
are internally-proved recursion orders; the partition Euler characteristic `−2`
is QOU-computable Wedderburn data; the DT counts `3`, `4` are the *imported* GGM
values, recorded only to prove the QOU Euler characteristic and the recursion
order do **not** reproduce them. Nothing fitted, nothing wired. Core-Lean only
(no Mathlib olean dependency); every fact is `decide`/`omega`-checkable.

-- Ref: [garoufalidis-gu-marino2023peacock] GGM 2012.00062 (peacock Conj 3(d); S⁺(0) 4₁; 5₂ blocks)
-- Ref: [nguyen-tran-2021] strong AJ for 4₁ (recursion order 2 = A-polynomial L-degree 2)
-- Ref: [leitner2026] docs/audits/2026-08-02-stokes-dt-bridge-moduli-gap-unification.md
-/

namespace QOU.QBeta.StokesDTCountExceedsRecursionOrder

/-! ## Part 1 — the QOU Euler-characteristic machinery produces `−2`, not `3` -/

/-- The three Wedderburn blocks of `H₃(q)` (partitions `λ ⊢ 3`), each recorded as
its `(a-function grade n(λ), Wedderburn dimension dim V_λ)`:
`(3) ↦ (0,1)`, `(2,1) ↦ (1,2)`, `(1³) ↦ (3,1)`. These are QOU data (the
a-function is the Gröbner–Shirshov jet-order valuation; the dimension is the
`H₃ → Wedderburn` block dimension). -/
def h3Blocks : List (Nat × Nat) := [(0, 1), (1, 2), (3, 1)]

/-- Per-block DT / 3d-index Euler characteristic `(-1)^{n(λ)} · dim V_λ` (the
`dtEulerG` collapse of `DeltaLambdaDTIndexGeneralN`, here evaluated on `H₃`). -/
def blockEuler (b : Nat × Nat) : Int := (-1 : Int) ^ b.1 * (b.2 : Int)

/-- **The total QOU Euler characteristic over the `H₃` Wedderburn blocks.**
`Σ_{λ⊢3} (-1)^{n(λ)} dim V_λ`. This is the machinery the directive proposes for
producing the knot DT count. -/
def partitionEuler3 : Int := (h3Blocks.map blockEuler).sum

/-- **What the QOU Euler-characteristic machinery actually produces: `−2`.**
`Σ_{λ⊢3} Δ_λ = 1 − 2 − 1 = −2`. Decidable. -/
theorem partitionEuler3_eq : partitionEuler3 = -2 := by decide

/-- The imported knot DT / Stokes / BPS off-diagonal count of `4₁`: `S⁺(0)₀₁ = 3`
(recorded, not derived). -/
def dtCount_fourOne : Int := 3

/-- **The honest negative (Part 1).** The QOU Wedderburn/Springer Euler
characteristic (`−2`, the sandwich *normalization*) does **not** equal the knot
DT count (`3`, the *off-diagonal*): the Euler-char arithmetic does not close to
`3`. So the bridge's first equality `Stokes = DT` for `4₁` is **not** produced by
the QOU Euler-characteristic machinery. -/
theorem euler_machinery_misses_dt_count : partitionEuler3 ≠ dtCount_fourOne := by decide

/-! ## Part 2 — the internally-derivable structural integer (recursion order = block
    size) is available but strictly weaker than the DT count -/

/-- The two keystone knots: amphichiral `4₁` (muon anchor), chiral `5₂`. -/
inductive KKnot
  | fourOne
  | fiveTwo
deriving DecidableEq

open KKnot

/-- **Internally-derived structural integer.** The order of the QOU-owned AJ
annihilator of `K` — equivalently the `L`-degree of `A_K`, equivalently the GGM
Stokes-matrix dimension. `4₁`: 2 (2nd-order annihilator, proved sorry-free);
`5₂`: 3 (`3×3` blocks). -/
def recursionOrder : KKnot → Nat
  | fourOne => 2
  | fiveTwo => 3

/-- **Imported DT / BPS off-diagonal count.** `4₁`: `3`; `5₂`: spectrum `{3,4}`,
maximal member `4`. Recorded to contrast with `recursionOrder`; not derived. -/
def dtOffDiagMax : KKnot → Nat
  | fourOne => 3
  | fiveTwo => 4

theorem recursionOrder_fourOne : recursionOrder fourOne = 2 := by decide
theorem recursionOrder_fiveTwo : recursionOrder fiveTwo = 3 := by decide
theorem dtOffDiagMax_fourOne : dtOffDiagMax fourOne = 3 := by decide
theorem dtOffDiagMax_fiveTwo : dtOffDiagMax fiveTwo = 4 := by decide

/-- **The structural gap (per knot).** The imported DT off-diagonal count strictly
exceeds the internally-derivable recursion order: `4₁`: `3 > 2`; `5₂`: `4 > 3`.
Even the derivable structural integer under-determines the DT count. -/
theorem dtOffDiag_gt_recursionOrder : ∀ K : KKnot, recursionOrder K < dtOffDiagMax K := by
  intro K; cases K <;> decide

/-! ## Part 3 — the two negatives packaged: neither QOU count reproduces the DT count -/

/-- **Summary (formalize-first honest negative).** Neither the QOU
Euler-characteristic machinery (`partitionEuler3 = −2`) nor the internally-derived
recursion order (`recursionOrder 4₁ = 2`) reproduces the knot DT count
(`dtCount 4₁ = 3`): `−2 ≠ 3` and `2 < 3`. The bridge's first equality
`Stokes = DT` for the knot is therefore **not** derivable from the assumed-QOU
Wedderburn/Springer structure — it requires the geometric spectral-curve DT count
(the character-variety Behrend/BPS invariant), which is external. -/
theorem qou_counts_miss_dt_count :
    partitionEuler3 ≠ dtCount_fourOne ∧
      (recursionOrder fourOne : Int) < dtCount_fourOne :=
  ⟨euler_machinery_misses_dt_count, by decide⟩

end QOU.QBeta.StokesDTCountExceedsRecursionOrder
