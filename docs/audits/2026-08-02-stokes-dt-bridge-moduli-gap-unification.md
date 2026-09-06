# The Stokes = DT = BPS bridge: what the QOU drivers derive, and the irreducible residual — unified with the Δ_λ Springer-fibre gap

> **⚠ CONVENTION-C CONDITIONAL — scope note added 2026-09-06 (bean `qou-h6o3`).**
> This document's conclusions depend on the `c_k` precision ladder / `Q_β`, which
> AGENTS.md records as **convention-C-frame throughout and NOT re-derived** under
> the owner ruling of 2026-08-15 making convention D (`z = q³/(q²+1)`) canonical.
> Treat every `c_k`-dependent statement below as **C-conditional** until the
> ladder is re-derived (bean `qou-cds1`). The numbers here are correct *for C*
> and are kept as recorded — they need **scoping, not correction**. This note was
> applied mechanically to the 45 documents in this arc that reference the ladder;
> it asserts dependence on the ladder, not that any particular conclusion changes
> under D.


**Date:** 2026-08-02 · **Bean:** `qou-qnnq` (G3 Stokes keystone, c₃-odd bridge) ·
**Branch:** `claude/dt-count-categorification-qnnq-2026-08-02` ·
**Tier:** synthesis + formalize-first (Lean, sorry-free, machine-verified) ·
**Scope:** (a) throughout; nothing fitted; nothing wired; no bridge axiomatized; L2 unchanged.

- Lean: [`QOU/QBeta/StokesDTCountExceedsRecursionOrder.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/StokesDTCountExceedsRecursionOrder.lean) — `lean`-direct **exit 0** (core-Lean, no Mathlib olean; disk-constrained sandbox, verified machine-checked).

## The question (owner re-scope, 2026-08-02)

The integer `3` is not the open item: `#4554` (`StokesSymmetryConstantQZero`,
sorry-free) reads the q→0 symmetry constant `= 3` off the certified Stokes
matrix. The genuine residual (`qou-qnnq`) is the **identification**
`Stokes = DT = BPS` — the `conj:stokes-dt-bps-bridge` (GGM peacock Conj 3(d) +
GPPV), imported for `4₁`. The directive: chase and formalize the bridge's **first
equality `Stokes = DT`** as a theorem conditional on a QOU structure — derive the
DT count `3` as a **QOU-computable graded Euler characteristic** (owner hint:
"Euler = −6") — or report exactly where the arithmetic fails to close to `3`.

**Headline: it does not close to `3`. The QOU Wedderburn/Springer
Euler-characteristic machinery produces `−2`, not `3`.** The honest negative is
sharp and machine-checked, and it unifies with today's Rossmann-CC verdict for
the per-partition `Δ_λ`.

## The bridge is a chain of three objects, unequally imported

| # | object | where it lives | QOU status |
|---|--------|----------------|-----------|
| **Stokes** | q→0 symmetry constant `= 3` | resurgent Stokes datum of the state integral `Z(S³∖4₁)` | **computed sorry-free** (#4554) from the GGM matrix `S⁺(0)`; but that matrix is itself the GGM/DGG q-series `W₋₁(0)` (geometric/state-integral side, per `StokesQZeroDTCount`'s own scope note) |
| **DT / 3d-index** | `Ω_DT(4₁) = 3` (rotated 3d-index of `T[4₁]`) | Behrend/BPS count of the character-variety spectral curve `A_{4₁}=0` | **NOT a QOU Wedderburn/Springer Euler characteristic** — see below |
| **BPS** | `dim ℋ_BPS(T[4₁]) = 3` (GPPV `Ẑ`) | M-theory fivebrane Hilbert space | irreducible physical import |

The owner's plan hoped **DT** is QOU-computable via the just-landed
`Δ_λ = DT/3d-index Euler-characteristic` work (`DeltaLambdaDTIndex`,
`DeltaLambdaDTIndexGeneralN`, sorry-free). The test below shows that machinery
computes a *different* DT object.

## The test of the "Euler → 3" hypothesis, grounded

The `Δ_λ = DT` machinery (`dtEulerG_collapse`, sorry-free, all `n`) is a
**per-partition** graded Euler characteristic of the Springer shadow `G_λ` (`V_λ`
in cohomological degree `n(λ)`):

    χ(G_λ) = Σ_k (-1)^k dim(G_λ)_k = (-1)^{n(λ)}·dim V_λ = Δ_λ.

The figure-eight `4₁` is the closure of the 3-braid `(σ₁σ₂⁻¹)²`, so its Wedderburn
home is `H₃(q)`, blocks `λ ⊢ 3` with `(n(λ), dim V_λ) = (0,1),(1,2),(3,1)`. The
**total** DT/3d-index Euler characteristic over those blocks is

    Σ_{λ⊢3} Δ_λ = (+1)(1) + (−1)(2) + (−1)(1) = **−2**.

**Where the "−6" comes from — and why it is normalization, not the count.** The
GGM q→0 sandwich is `A·W₋₁(0)·B·W₋₁(0)ᵀ·C = −2·S⁺(0)`
(`StokesQZeroDTCount.ggm_sandwich_qzero`), so its `(0,1)` entry is
`−6 = (−2)·3`. The `−6` factors as **normalization `−2` × count `3`**:

- the **normalization `−2`** is exactly the QOU-computable Wedderburn Euler
  characteristic `Σ_{λ⊢3} Δ_λ = −2` (formalized: `partitionEuler3_eq`). *This is
  the one place the QOU Euler-char machinery lands a Stokes-sandwich number.*
- the **count `3`** is the *off-diagonal* `S⁺(0)₀₁`, and `−2 ≠ 3`
  (`euler_machinery_misses_dt_count`). **No QOU Wedderburn/Springer Euler
  characteristic produces `3`.**

So the owner's `Euler = −6` hint is real but resolves the *opposite* way: the
Euler-characteristic machinery supplies the sandwich **prefactor `−2`**, not the
DT **count `3`**. The count is the Behrend-signed DT/BPS invariant of the
*spectral curve* `A_{4₁}=0` (the rotated 3d-index of the complement) — a
geometric object (triangulation / exponential-network), not a graded Euler
characteristic over any Wedderburn/moduli grading the 13 drivers build.

> **Unclaimed observation (anti-numerology guard applies).** That the sandwich
> normalization equals `Σ_{λ⊢3} Δ_λ = −2` is a single-knot (`4₁`/`H₃`) match. Per
> the standing "single-knot count-matching is a trap" rule (`5₂` block is `3×3`),
> it is **not** asserted as derived and **not** wired; it is flagged for a
> cross-knot `5₂` check (does the `5₂` sandwich normalization equal
> `Σ_{λ⊢?} Δ_λ` for its braid's Wedderburn home?). Recorded as a probe, not a
> result.

## The two DT objects are different — the crux

| | per-partition `Δ_λ` | per-knot `A_ω` |
|---|---|---|
| moduli | Springer fibre `𝓑_λ` | character variety `X(S³∖K)` / `T[K]` BPS moduli |
| attached to | a Wedderburn block `λ` (driver-built) | the knot *complement* (geometric) |
| Behrend count | `dim V_λ` — **closed form** from Wedderburn | exponential-network / 3d-index count — **not** closed-form |
| QOU status | DT **value** derived; DT **realization** external (Rossmann-CC) | shape (recursion order) derived; DT **count** external |

The `Δ_λ = DT` Euler-characteristic identity closes because `𝓑_λ` is a *compact,
Wedderburn-attached* variety with a closed-form Behrend count. The `A_ω = DT`
identity does **not** close because `X(S³∖K)` is a *non-compact, complement-attached*
moduli whose Behrend/BPS count is the exponential-network invariant. Same missing
categorical input — a **Behrend-weighted DT moduli built by the drivers** — at two
levels.

## What IS internally derivable (the maximal QOU fragment)

1. **`Δ_λ = DT/3d-index graded Euler characteristic` — PROVED** (partition level,
   all `n`; `DeltaLambdaDTIndexGeneralN`, sorry-free, on main). A genuine
   categorical DT count from Wedderburn.
2. **The knot Stokes-matrix SHAPE** — the order of the QOU-owned AJ annihilator
   (`4₁`: order 2, proved sorry-free `AJFigureEightAnnihilation`; `q→1` gives the
   classical `A_{4₁}`), `= A_{4₁}` `L`-degree `= 2 =` dimension of `S⁺(0)`; `5₂`:
   `3`. This is internally derived.
3. **The sandwich normalization `−2`** — `= Σ_{λ⊢3} Δ_λ`, QOU-computable
   (formalized), matching `sandwich = −2·S⁺(0)` (single-knot, unclaimed).

## The irreducible residual (honest negative, formalized)

The bridge's **first equality `Stokes = DT` for the knot is NOT derivable from the
assumed-QOU Wedderburn/Springer structure.** Two machine-checked facts locate it
(`StokesDTCountExceedsRecursionOrder.lean`, sorry-free):

- `euler_machinery_misses_dt_count` : `partitionEuler3 = −2 ≠ 3` — the QOU
  Euler-characteristic machinery does not produce the DT count.
- `dtOffDiag_gt_recursionOrder` : `recursionOrder K < dtOffDiagMax K` (`4₁`: `2<3`;
  `5₂`: `3<4`) — even the internally-derivable structural integer under-determines
  the DT count.

**The residual is already the `Stokes = DT` leg (not merely `DT = BPS`).** Both
the resurgent Stokes constant and the knot 3d-index are *geometric-side* objects
(state-integral / triangulation of the complement); the `Stokes = DT` equality
(GGM Conj 3(d)) relates two objects that both require the spectral-curve DT count.
The QOU drivers derive the spectral **curve** (the A-polynomial, proved for `4₁`)
but not its Behrend/BPS **count**. Deriving `Stokes = DT` internally would require
QOU to construct the character-variety DT moduli and prove its Behrend count = the
Stokes constant — the exact geometric input the arc (and now this test) shows is
external.

**Named missing driver ("driver-14").** A categorical construction, from the
substrate, of the **Behrend-weighted DT moduli of the character variety /
BPS Hilbert space of `T[K]`** — the knot-level twin of the Springer-fibre DT
realization that Rossmann-CC proved external for `Δ_λ`. This is the object the
DT/3d-index *categorification* literature has not built (arc-ledger literature
verdict: KLW categorify the colored Jones, not the 3d-index; the DT side gives
`{3,4}` from triangulation, not crystal/Hecke).

## Is this already settled in the corpus? (per the coordinator's "report already-done")

**Largely yes, and this PR unifies + sharpens it — it does not manufacture a task.**

- `StokesDTBPSBridge` (#4569) already establishes the bridge is an *imported*
  published conjecture (class carries the two identifications as hypotheses; the
  value `3` is composed from the certified Stokes datum). This PR does **not**
  re-skin it.
- Rossmann-CC (2026-08-02) already proves the `Δ_λ` Springer-fibre DT-realization
  is *external, not forceable from the substrate weights*.
- **New here:** (a) the explicit test of the "DT = QOU Euler characteristic"
  hypothesis for the *knot*, grounding the `−6 = −2·3` split and showing the
  Euler-char machinery lands `−2` (normalization), not `3` (count); (b) the
  unification — `Δ_λ` and `A_ω` are the same missing-DT-moduli obstruction at two
  levels; (c) the maximal derivable fragment + the precise "residual is already
  the `Stokes = DT` leg" statement, formalized sorry-free.

## Anti-laundering / honesty ledger

- **No bridge axiomatized.** No `QOUStructure`/`StokesDTBridge` class carrying the
  `Stokes = DT` conclusion is landed — that would be a re-skin of #4569 and, worse,
  a self-assuming projection (§3b-cond item 5). The honest output is the negative:
  the equality does not follow from the QOU Euler-char / recursion-order data.
- **0 free parameters; nothing inverted; nothing wired.** The DT counts `3`, `{3,4}`
  are recorded imported values, used only to prove the QOU-computable quantities
  (`−2`, recursion order `2/3`) do not reach them.
- **Formalize-first honoured, machine-verified** (core-Lean, `lean`-direct exit 0;
  the ~5 GB Mathlib olean restore is disk-blocked in this sandbox, so the file is
  deliberately Mathlib-free and fully machine-checked without it).
- **`3` not re-derived** (respects #4554); **bridge not re-skinned** (respects
  #4569); **Rossmann-CC verdict extended, not overturned**.

## Cross-references

- Lean (new): [`StokesDTCountExceedsRecursionOrder.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/StokesDTCountExceedsRecursionOrder.lean).
- Bridge (imported): [`StokesDTBPSBridge.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/StokesDTBPSBridge.lean) (#4569); [`conj:stokes-dt-bps-bridge`](../../content/quantum-observable-universe/mass-theory/stokes-dt-bps-bridge.md).
- Stokes q→0 (`−2·S⁺(0)`, count 3): [`StokesQZeroDTCount.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/StokesQZeroDTCount.lean); [`StokesSymmetryConstantQZero.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/StokesSymmetryConstantQZero.lean) (#4554).
- Δ_λ = DT Euler characteristic (partition level, proved): [`DeltaLambdaDTIndex.lean`](../../content/quantum-observable-universe/lean/QOU/BraidsAndKnots/DeltaLambdaDTIndex.lean), [`DeltaLambdaDTIndexGeneralN.lean`](../../content/quantum-observable-universe/lean/QOU/BraidsAndKnots/DeltaLambdaDTIndexGeneralN.lean).
- Δ_λ DT-realization external (the parallel): [`2026-08-02-rossmann-cc-bridge-deltalambda-realization.md`](2026-08-02-rossmann-cc-bridge-deltalambda-realization.md).
- 5₂ split (block size 3, spectrum {3,4}): [`FiveTwoDTSpectrumSplit.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/FiveTwoDTSpectrumSplit.lean); [`2026-08-02-fivetwo-crossknot-34-resolution.md`](2026-08-02-fivetwo-crossknot-34-resolution.md).
- AJ / A-polynomial internal for 4₁ (the spectral curve): [`2026-07-03-aj-conjecture-dialog-assessment.md`](2026-07-03-aj-conjecture-dialog-assessment.md).
- Arc ledger: [`docs/coordination/2026-08-02-c3-odd-aomega-unification.md`](../coordination/2026-08-02-c3-odd-aomega-unification.md).
- AGENTS.md §"Axiomatization is NOT a Proof"; §"Before declaring refuted"; §"Strict Lean Discipline"; §"Conditional-proved ≠ premise-established".
