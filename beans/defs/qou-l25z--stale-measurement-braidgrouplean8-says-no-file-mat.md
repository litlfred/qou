---
# qou-l25z
title: 'STALE MEASUREMENT: BraidGroup.lean:8 says no file matches *braid* in Mathlib — four do (braided monoidal categories); verdict correct, evidence wrong'
status: in-progress
type: task
priority: low
tags:
    - reorg-2026-10-04
created_at: 2026-09-04T09:08:24Z
updated_at: 2026-11-18T08:59:30Z
parent: qou-o9ge
---

**STALE MEASUREMENT — correct verdict, wrong evidence.** Low severity, cheap fix.

`QOU/MathlibExt/BraidGroup.lean:8-9`:

> "**Mathlib has no braid groups.** Verified by search: **no file matching `*braid*`
> anywhere in `Mathlib/`**, and `Mathlib/GroupTheory/` carries `Coxeter` but not the
> braid group itself."

**The conclusion is correct.** Measured 2026-09-04 against pinned mathlib
`f897ebcf72cd16f89ab4577d0c826cd14afaafc7`: `grep -rl 'BraidGroup' Mathlib/` → **0
files**. There is no Artin braid group.

**The stated measurement is false.** `find Mathlib -iname '*braid*'` returns **four**
hits:

    CategoryTheory/GradedObject/Braiding.lean
    CategoryTheory/Monoidal/DayConvolution/Braided.lean
    CategoryTheory/Monoidal/Braided/            (directory: Basic, Multifunctor,
                                                 Opposite, Reflection, Transport)
    CategoryTheory/Monoidal/Rigid/Braided.lean

All are **braided monoidal categories** — a different object, and one the corpus uses
heavily elsewhere (`MathlibExt/{BraidedSlide,BraidedTensorDual,BraidedQuantumDimension}.lean`).
A case-insensitive `grep -l braid` returns 56 files for the same reason.

**Why it is worth fixing despite being harmless.** A reader who re-runs the quoted
command gets a different answer than the file promises, and the natural inference is
that the verdict is stale too — when it is not. In a corpus whose discipline is
"measured, not assumed", a measurement that does not reproduce costs more than its
size.

**Corrected form:**

> "**Mathlib has no braid groups.** Measured: `grep -rl 'BraidGroup' Mathlib/` → 0
> files. (`find Mathlib -iname '*braid*'` does return four files, all **braided monoidal
> categories** — `CategoryTheory/Monoidal/Braided/` and friends — which is a different
> object.) `Mathlib/GroupTheory/` carries `Coxeter` but not the braid group."

The rest of the file is unaffected: `exponentSum` and its well-definedness argument
stand, and the `PresentedGroup` construction is the right one.

Source: `docs/audits/2026-09-04-mathlib-infrastructure-inventory.md` §F6, §U3.

- Round 76 (`lane-e667`): Formalized `qou-gmfz`, `qou-img9`, `qou-phir`, `qou-siin`, `qou-l25z` in `QOU.Foundations.TriangularBarInvolutionLengthTwoQuadraticDefectRightMultiplicationDichotomyRootParameterRescalingWritheHomomorphism` with 80-dps `mpmath` 2-commit witness stamp (`1d514d8cc14cab86cdbfe50f0bca4313a91a6db7` -> `8fbc40e0a853ba6aa21eab5cf4d1947155a2d115`, `scriptHash=b5b4b562fbd04cd73aa5a68e31eebc858e55abd805cb24915d3a249d657d689c`) in PR `litlfred/qou#8409` (`status: in-progress`).
