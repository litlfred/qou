---
# k65k
title: 'Narrative-proof .proof.md sidecar (PR #2687)'
status: in-progress
type: milestone
priority: high
created_at: 2026-06-24T03:52:14Z
updated_at: 2026-06-24T04:29:31Z
---

Each provable block gets a linked `proof` block (<name>-proof.{ts,md} + parent proofs + chapter-manifest). MECHANISM ALREADY EXISTS (~170 in use, renders). Audit: content/pipeline/audit-narrative-proof-presence.ts. State 2026-06-24: 170/659 covered, 489 gaps. No schema change needed; only proof-narrative-present QA criterion is new (i4fx).
