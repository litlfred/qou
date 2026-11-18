---
# qou-wumn
title: lake-cache branch holds DEPENDENCY oleans only — QOU's own modules are absent, blocking per-file lean-direct
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-07T11:13:16Z
updated_at: 2026-10-04T15:21:07Z
parent: qou-5vkl
---

Observed 2026-08-07. lake-cache/qou-v4-24-0 restores 7268 oleans under .lake/packages/{mathlib,batteries,aesop,Qq,proofwidgets,plausible,LeanSearchClient,importGraph}, but ZERO under any QOU path. Consequence: lean-direct verifies only .lean files whose imports are Mathlib-only. Any QOU file with intra-package imports fails with 'unknown module prefix QOU'.\n\nCONCRETE COST this session: QOU/Knot/WhiteheadVolumeConjecture.lean imports no QOU modules -> verified exit 0 (1 documented sorry). QOU/Knot/WhiteheadSaddleClausen.lean imports QOU.Knot.Clausen + QOU.Knot.WhiteheadVolumeConjecture -> could NOT be verified at all, and the only route (lake build) both exceeds a 9-minute budget and destroys the cache (see the sibling bean).\n\nSUGGESTED FIX: seed the cache branch from a tree where the QOU library itself is built, so .lake/build/lib/lean/QOU/**.olean ships too. Then lean-direct covers the whole corpus, which is the actual point of the restore. Worth checking whether the existing variant branches (qou-v4-24-0-new, -repthy-wedderburn, -logbounds-summable) already do this.
