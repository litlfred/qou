---
# qou-ghc6
title: 'BUILD: Lie-algebra-valued 1-forms on a normed space from Mathlib DifferentialForm/extDeriv (replaces the NonAbelianStokes abstract carrier)'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-04T09:07:55Z
updated_at: 2026-10-04T15:16:48Z
parent: qou-c8p8
---

**BUILD.** `QOU/Mathlib/NonAbelianStokes.lean:47` carries `LieValuedOneForm` as an
abstract `Prop`-shaped carrier for `Ω¹(M; 𝔤)` with no model — flagged as
self-certifying in bean `qou-ewc4`.

**A real model is available at the pin.** `Mathlib/Analysis/Calculus/DifferentialForm/Basic.lean`
(231 lines, measured 2026-09-04 against mathlib `f897ebcf72c`) represents an `n`-form as

    ω : E → E [⋀^Fin n]→L[𝕜] F

with `E` and `F` **arbitrary** normed spaces over a `NontriviallyNormedField 𝕜`
(variable block at `Basic.lean:48-53`). So with
`[NormedAddCommGroup 𝔤] [NormedSpace ℝ 𝔤] [LieRing 𝔤] [LieAlgebra ℝ 𝔤]`, a 𝔤-valued
1-form on a normed space is `E → E [⋀^Fin 1]→L[ℝ] 𝔤` — no new type needed. The file
also supplies `extDeriv`, linearity, and **`extDeriv_extDeriv` (`d ∘ d = 0`)**.

**Scope:** carrier + bracket-wedge `[α ∧ β]` + covariant differential
`d_α β = dβ + [α ∧ β]`. ~100-200 lines.

**What this does NOT close:** the multiplicative line/surface integral. Mathlib has
**no** holonomy, parallel transport or path-ordered exponential — measured,
`grep -rln 'holonomy\|parallel transport\|ParallelTransport\|pathOrdered' Mathlib/`
returns **0 files**. That half stays RESEARCH (Yekutieli 2015).

**Why worth doing anyway:** the file's own worked example is `M = ℝ²` (line 107), which
is a normed space, so this replaces an assertion-free carrier with a real object on
exactly the case it cares about.

Related defect: the same file at line 10 misdescribes what Mathlib holds — see the
false-claim bean filed alongside this one.

Source: `docs/audits/2026-09-04-mathlib-infrastructure-inventory.md` §B2.
