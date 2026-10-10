---
# qou-lqh3
title: 'Migrate misfiled QA reasons: notes -> evidence for the 1302 empty-evidence fail/warn entries'
status: completed
type: task
priority: normal
created_at: 2026-08-25T07:10:38Z
updated_at: 2026-08-25T07:42:00Z
---

DONE. 1302 entries across 645 sidecars; `evidence` copied verbatim from
`notes` (1289) / `referee_argument` (13). Zero skipped. COPY not move —
`notes` is read by qa-flag-preservation-audit, proof-axis-dashboard,
qa-sweep, qa-merge-findings, qa-utils.

Verified semantically against HEAD: 645 files, 1302 keys added, 0 defects.
Two defects caught pre-commit: JSON.stringify un-escaping 57 escaped-UTF8
sidecars (167 unrelated line rewrites), and line-counting mistaken for proof.

Script + 9 safety tests: content/pipeline/qa-evidence-migrate.ts. qou#5745.
