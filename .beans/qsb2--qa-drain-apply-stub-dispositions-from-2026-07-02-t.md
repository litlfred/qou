---
# qsb2
title: 'QA drain: apply stub dispositions from 2026-07-02 triage'
status: in-progress
type: task
priority: normal
tags:
    - qa-drain
    - lean-proof-progress-table
created_at: 2026-07-02T16:43:24Z
updated_at: 2026-07-02T16:43:24Z
---

Apply the per-block honest dispositions (prove / real-statement+cited-sorry / demote-to-conjecture / delete shadowing stub) produced by the stub triage on branch claude/lean-proof-progress-table-gchfqu (PR #3222). Gate Lean edits on lake-cache restore + lean-direct verification per lean-environment-setup.

**2026-07-02 progress:** 19 shadow-stub siblings DELETED (triage doc docs/audits/2026-07-02-stub-triage.md); remaining: 6 needs-real-statement, 1 needs-proof (transfer-matrix-identities), 13 projection residuals, hecke-baer-star-generic stray example.
