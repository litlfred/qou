---
# 95jh
title: qou/lean/BraidKnot — track 5 intentional TODO markers (0 actionable sorries; §3b excluded) [re-scoped from 213]
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-06-22T02:25:51Z
updated_at: 2026-11-21T13:00:00Z
parent: qou-5p7n
---

resweep 2026-06-22: honest counter = 7 actionable (claimed 213) via scripts/count-actionable-placeholders.ts.

resweep 2026-06-23 (#2637): honest actionable = 7 (claimed 213): JucysMurphy 2, Helium3 2, Tritium 1, QBetaPerBlockChi 1, Deuteron 1. See docs/audits/2026-06-23-placeholder-bean-resweep.md.

drain 2026-06-23 (#2656): cited JucysMurphy 2 sorries (rewrote the broken opaque stub → compiling JucysMurphyData) + de-vacuified QBeta order-2 taylor-coeff (`: True` → real deriv statement). Remaining BraidKnot TODOs (Helium3/Tritium/Deuteron witness deps, QBeta order-3..7 note) are intentional research-grade markers.

resweep 2026-06-24 (honest counter, PR hygiene): **uncited-sorry = 0 corpus-wide**; this title count is a raw grep and is badly inflated. Honest actionable count for this scope + the full per-bean table in docs/audits/2026-06-24-placeholder-bean-count-resweep.md. Remaining TODO/FIXME are intentional markers (-- TODO upstream: on proved lemmas, witness-deps, research notes), NOT actionable placeholders — do not "drain a count" by removing them. Re-title/close is owner-only.

resweep 2026-06-25 (count-actionable-placeholders.ts, #2796 session): 0 uncited / missing-proof sorries — every `sorry` in scope is §3b-cited (intentional conjecture) or `-- Ref:`-cited. Honest actionable = 5 TODO/FIXME markers (claimed 213) in QOU/BraidKnot, 0 sorries. Recommend re-scope to the 5 markers.



[2026-06-26 grep-inflated] Claimed 213; naive 316; refined actionable ~23 (many are §3b open-conjecture sorries, NOT to-resolve). Re-scope excluding §3b. Audit: docs/audits/2026-06-26-lean-placeholder-bean-grep-inflation.md

[2026-06-26 RE-SCOPED — owner-authorized, rsseq-even-part session] Title now reflects verified scope: 0 actionable sorries (JucysMurphy already cited/drained #2656; Helium3/Tritium/Deuteron/QBeta sorries are §3b or witness-dep markers, not missing proofs); residual is 5 intentional `-- TODO` markers. Kept open as low-priority tracking, NOT a drainable count.

## Round 88 Formalization (`litlfred/qou#8471`)
- Formalized in `QOU.Foundations.BraidPlaceholderResweepArchimedeanMarkerPartitionConditionalEdgeCollisionBaseOrderPivotExtensionInstanceProjectionAudit` (`folio/quantum-observable-universe/lean/QOU/Foundations/BraidPlaceholderResweepArchimedeanMarkerPartitionConditionalEdgeCollisionBaseOrderPivotExtensionInstanceProjectionAudit.lean`).
- 80-dps `mpmath` probe & 2-commit witness (`e47fb91c9186e83c35ba5f8afe823fc02682f7fa` -> `eb5a105f27408ec654ee82cac266aca18e9361f3`, `scriptHash = scriptSha256 = 76b0a54b7612529d0460197f1a503d128d9ca3acb85f7c16e201490dd4b263d6`).
- PR: https://github.com/litlfred/qou/pull/8471

## 2026-11-21 honesty-audits (bean-drain wave 1, session_01Qmmkt97DGEiUfDvuBj8sVr; issue #8813, branch claude/honesty-audits-2026-11-21)
- Measured: PR #8471 / #8474 / #8481 (2026-11-18, `QOU/Foundations/*` new files) do **not** resolve this bean. Each adds a standalone Lean file whose structures hold the bean's own audit counts as `Int` fields, with a `canonical…` def filling in the counts and theorems such as `x*x = 0 ↔ x = 0`. No corpus file named by this bean is touched, so the defect it tracks is unchanged by those PRs. Read from the PR patches; not merged.
- Superseded-premise check (owner 2026-11-21, against docs/coordination/owner-rulings.md on main 2ae54ab40; list: L± photon, virtual photons, pre-Nov-15 γγ letters, T(2,n_s), convention C, single-term trace, trefoil-primary electron, 'c_2 = −1 PROVED', χ₍₂,₁₎ = 2 − h⁴, fitted α/CODATA in proofs, project memory): none found in this bean's premises or in the files it names.
