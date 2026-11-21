---
# ckj6
title: 'Harden lean-verify-siblings.sh: distinguish ''module removed from Mathlib'' (FAIL) from ''olean outside cache cone'' (neutral-skip) — this class was masked as neutral-skip'
status: completed
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-06-30T23:32:53Z
updated_at: 2026-11-21T14:33:40Z
parent: qou-5vkl
---

- **Round 94 PR (`litlfred/qou#8500`)**: Formalized `SiblingVerificationClassificationLedger`, `canonicalSiblingVerificationClassificationLedger`, `sibling_classification_polarization`, and `sibling_classification_diff_sq` in `QOU.Foundations.LeafOleanConeBatchingDeferredStructuralCleanupSiblingVerificationClassificationFamilyChainErrorPartitionSubstrateProbeCancelHotspot` with 80-dps witness (`HEAD = 37841388326f8fad43c7ffaa9f1c59e901153736`).

## 2026-11-21 — lean-build-red drain (issue #8817, session https://claude.ai/code/session_01Qmmkt5eovX5GYdZNHqjZdu)

**Completed.** `scripts/lean-verify-siblings.sh` on main distinguishes a module that does not exist at the pinned Mathlib rev (stale, FAIL) from an olean outside the cache cone (neutral-skip), header lines 11-37 at `2ae54ab401`; landed as `9dec8e7537`.
