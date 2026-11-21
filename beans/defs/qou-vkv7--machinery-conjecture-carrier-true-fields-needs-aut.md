---
# qou-vkv7
title: Machinery/* conjecture-carrier :True fields (needs author intent)
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-07-11T18:41:39Z
updated_at: 2026-11-21T13:00:00Z
parent: qou-5p7n
---

KLRAlgebraBasic(50,72,85), KashiwaraCrystalBasic(66,72,78), MarkovTraceOnHecke(49,71,86,105), QDilogarithm(104 faddeev), QPochhammer(138 habiro), SpectralSequenceBasic(61,72), DerivedCharacterCatalogue(173). Each field:True encodes a deep conjecture (Stembridge axioms, KLR categorification, Faddeev functional eq, etc.) — real Prop content needs heavy Mathlib machinery + author intent for the precise claim. FLAG, do not fabricate.

## Round 90 Lean 4 + 80-dps Witness Formalization (PR #8481)
- Module: `QOU.Foundations.MachineryConjectureCarrierRegistryThreeBatchDefectDrainDoubleCentralizerBalanceLongExactSequencePayoffParallelogramArgumentPrinciple`
- Commit 1 (code + probe): `a9f0f1224d140032ab84905edb79a825b0ec07fe`
- Commit 2 (`.witness.json`): `2e6c78442e063cad6ad9aa9c49b55c365f4be789`
- PR: https://github.com/litlfred/qou/pull/8481

## 2026-11-21 honesty-audits (bean-drain wave 1, session_01Qmmkt97DGEiUfDvuBj8sVr; issue #8813, branch claude/honesty-audits-2026-11-21)
- Measured: PR #8471 / #8474 / #8481 (2026-11-18, `QOU/Foundations/*` new files) do **not** resolve this bean. Each adds a standalone Lean file whose structures hold the bean's own audit counts as `Int` fields, with a `canonical…` def filling in the counts and theorems such as `x*x = 0 ↔ x = 0`. No corpus file named by this bean is touched, so the defect it tracks is unchanged by those PRs. Read from the PR patches; not merged.
