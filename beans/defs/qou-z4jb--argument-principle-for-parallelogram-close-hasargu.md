---
# qou-z4jb
title: 'Argument principle for parallelogram: close HasArgumentPrinciple'
status: in-progress
type: task
priority: normal
tags:
    - lean
    - reorg-2026-10-04
created_at: 2026-08-24T06:36:07Z
updated_at: 2026-11-20T08:27:17Z
parent: qou-c8p8
blocked_by:
    - qou-f6bb
---

Once parallelogram contour API exists (qou-f6bb), prove argument_principle_parallelogram and remove the HasArgumentPrinciple class field from EllipticDivisorDegree.lean. Consumer: HasArgumentPrinciple.argument_principle_parallelogram.

## Round 90 Lean 4 + 80-dps Witness Formalization (PR #8481)
- Module: `QOU.Foundations.MachineryConjectureCarrierRegistryThreeBatchDefectDrainDoubleCentralizerBalanceLongExactSequencePayoffParallelogramArgumentPrinciple`
- Commit 1 (code + probe): `a9f0f1224d140032ab84905edb79a825b0ec07fe`
- Commit 2 (`.witness.json`): `2e6c78442e063cad6ad9aa9c49b55c365f4be789`
- PR: https://github.com/litlfred/qou/pull/8481

## 2026-11-20 — W10 (qou-c8p8 workstream)



W10 finding 2026-11-20: `HasArgumentPrinciple` (EllipticDivisorDegree.lean:217) carries the conclusion of `elliptic_divisor_degree_zero` as its only field and takes no hypotheses (f need not be elliptic, S is any Finset), so it is false in general and can never be instanced honestly. Closing this bean means proving a hypothesis-carrying Liouville-third theorem and deleting the class, not instancing it. Route sketched on #8526: pull back along w = exp(2πi z/ω₁) to an annulus and reuse `argumentPrinciple_annulus_finset` + `circleIntegral_scale`; needs ℤ multiplicities (poles). Multi-session. Owner ask on #8526 for the interim restatement.
