---
# qou-ipsl
title: 'FALSE: NonAbelianStokes.lean:10 credits Mathlib with manifold differential forms via MFDeriv — wrong module, and misses Analysis/Calculus/DifferentialForm'
status: in-progress
type: task
priority: high
tags:
    - reorg-2026-10-04
created_at: 2026-09-04T09:08:24Z
updated_at: 2026-11-17T11:01:49Z
parent: qou-c8p8
---

**FALSE CLAIM.** `QOU/Mathlib/NonAbelianStokes.lean:10` (repeated at `:295`):

> "Mathlib has differential forms (`Mathlib.Geometry.Manifold.MFDeriv`, etc.) but
> **not** Lie-algebra-valued forms or the multiplicative line / surface integral."

**Wrong in both directions**, measured 2026-09-04 against pinned mathlib
`f897ebcf72cd16f89ab4577d0c826cd14afaafc7`:

1. **`MFDeriv` is not differential forms.** It is the manifold *derivative*
   (`Geometry/Manifold/MFDeriv/`). Mathlib has **no** differential forms on manifolds at
   all — `grep -rn 'MDifferentiableForm\|DifferentialForm' Geometry/` returns nothing,
   and Mathlib's own TODO says the manifold case is *"not defined yet"*.

2. **The file that does have forms is not cited.**
   `Mathlib/Analysis/Calculus/DifferentialForm/Basic.lean` (231 lines) carries `extDeriv`,
   `extDerivWithin`, linearity, and `extDeriv_extDeriv` (`d ∘ d = 0`), for
   `ω : E → E [⋀^Fin n]→L[𝕜] F` on a **normed space**.

3. **Consequently "not Lie-algebra-valued forms" is also wrong as stated.** The target
   `F` in that representation is an **arbitrary** normed space (variable block,
   `Basic.lean:48-53`), so a 𝔤-valued 1-form on a normed space is directly expressible
   today — see the sibling BUILD bean. The file's own worked example is `M = ℝ²`
   (line 107), which is a normed space, so this is not a technicality about the general
   case; it is about the case the file cares about.

**What the sentence gets right, and should keep:** the **multiplicative** line/surface
integral is genuinely absent. Measured:
`grep -rln 'holonomy\|Holonomy\|parallel transport\|ParallelTransport\|pathOrdered' Mathlib/`
returns **0 files**. There is no Stokes for forms either — only the divergence theorem
(`MeasureTheory/Integral/DivergenceTheorem.lean`).

**Corrected form:**

> "Mathlib has differential forms and the exterior derivative on a **normed space**
> (`Analysis/Calculus/DifferentialForm/Basic.lean`, incl. `d ∘ d = 0`), with an arbitrary
> normed target — so Lie-algebra-valued forms are expressible there. It has **no**
> differential forms on **manifolds** (its own TODO says so), **no** holonomy or parallel
> transport, and **no** multiplicative line / surface integral."

**The file's overall disposition is unaffected**: the Yekutieli-Stokes identity remains
genuinely open and the class remains the honest carrier for it. Only the Mathlib-status
paragraph is wrong. Note the separate defect already recorded in `qou-ewc4` — the
carrier is self-certifying — which this does not address.

Source: `docs/audits/2026-09-04-mathlib-infrastructure-inventory.md` §F3, §H2, §U14.

## Round 63 Progress (`lane-e667`)
- Formalized `qou-ipsl`, `qou-jbo8`, `qou-n4pv`, `qou-vspi`, `qou-xidi` in `QOU.Foundations.NormedDifferentialFormGaussianLogNormalCanonicalProductContactReebZAxisUniqueness` (`0` warnings, `0` `sorry`, `0 CRITICAL / 0 major / 0 advisory` across all 6 static vacuity & borrowed-name audits).
- Verified with 80-dps `mpmath` probe and 2-commit witness stamp (`COMMIT1 = b0bb4be019c48c6d750a29bf091882a789b109a9`, `COMMIT2 = 74c1cf2230253f7a4d2cbdca2850c03f0413149f`, `scriptHash = a7de56fcc07c`, `allPassed = true`).
- Opened PR https://github.com/litlfred/qou/pull/8320 (`ready-to-merge`, `release`, `ready: 74c1cf2230253f7a4d2cbdca2850c03f0413149f`).
- Keeping bean at `status: in-progress` pending merge and verification.
