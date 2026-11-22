---
# 6chz
title: 'T3 [BLOCKED]: geometric-Langlands infra (q-opers, eigensheaves, LocSys, Bun_G) → q-GL family'
status: in-progress
type: task
priority: normal
tags:
    - keystone-infra
    - tier3
    - reorg-2026-10-04
created_at: 2026-06-25T17:06:54Z
updated_at: 2026-11-22T22:05:00Z
parent: qou-rtxm
---

q_oper_hecke + q_gl_fiber_functor + q_gl_kummer_filtration + q_gl_classical_limit need geometric-Langlands objects absent from Mathlib AND QOU. Research-grade; keystones stay structurally abstracted (honest §3b). Document the gap; do not fake.

## Round 91 Lean 4 + 80-dps Witness Formalization (PR #8487)
- Module: `QOU.Foundations.SeminormalInversionDescentBranchingBridgeHypothesisLinkStabilisationConjugationFourComponentOperFiltrationJointPeriodBraidSplit`
- Commit 1 (code + probe): `ac300d2c8e5f49854ec28ab33d09e033225201c1`
- Commit 2 (`.witness.json`): `e92637de21c829df89a2f80bfc1da64dc805a438`
- PR: https://github.com/litlfred/qou/pull/8487

## 2026-11-22 — wave-2 applicability review (thread "Build ribbon categories and QFT math cores")

**Verdict: NEEDS-OWNER.** Geometric-Langlands objects (q-opers, Bun_G) are absent from Mathlib and QOU, and nothing on the current derivation chain (γγ, confinement SDP, two-term trace) reads the q-GL family. Recommend leaving it as a documented wall or scrapping; owner call.

Round-91 note cites open batch PR #8487, not evidence.
