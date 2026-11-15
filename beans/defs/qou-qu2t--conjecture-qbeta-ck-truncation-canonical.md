---
# qou-qu2t
title: 'Conjecture: qbeta_ck_truncation_canonical'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-04T01:49:55Z
updated_at: 2026-11-15T17:33:11Z
parent: qou-avtq
blocked_by:
    - qou-cds1
---

qbeta-ck-truncation-canonical.lean: existence of canonical anchor-independent c_k. Only c_2=-1 proved exact.


## 2026-10-10 — evidence re-check (verification sweep of `qou-avtq`)

**Verdict: BLOCKED.** The conjecture is stated over the C-frame ladder. Under D no ladder exists, and the existing c_3 is q0-dependent (2.98% anchor swing). Blocked on qou-cds1; the owner should decide whether to re-state it for D or retire it.

Evidence: `folio/.../appendix-qvalues/qbeta-ck-truncation-canonical.lean`: `QbetaCkTruncationCanonicalExists` is a §3b conjecture class. "sorry" occurs only in docstrings. Only c_2 = -1 is proved, and that is a `ring` tautology under C (red-team). Duplicate qou-7hfy is already scrapped into it.

Status: `todo` → `todo` (unchanged: edited today by another session, or held in-progress).
Checked against qou `main` at `77695711d2`. Probes were re-run only where cheap and decisive. A numeric result counts as evidence only where it reproduces and its precision exceeds the gap it decides; convention-C numbers are not evidence about convention-D claims.
