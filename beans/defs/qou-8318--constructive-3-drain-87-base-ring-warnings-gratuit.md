---
# qou-8318
title: 'Constructive 3: drain 87 base-ring warnings (gratuitous R/C on algebraic side)'
status: todo
type: task
priority: normal
tags:
    - constructive
created_at: 2026-11-27T14:50:13Z
updated_at: 2026-11-27T18:52:39Z
parent: qou-dk7p
---

Doc item 3. bun run scripts/check-base-ring.ts --sweep folio/quantum-observable-universe -> 87 warn files, 800 hits (2026-11-27). Options 3.1 drain per chapter (recommended); 3.2 ratchet baseline; 3.3 leave. Needs owner yes (ask-first rule).

2026-11-27: PR #9572 (head 128fb9e7). 15 Field->CommRing swaps in 11 files, 88->85 warn files, 809->794 hits. Remaining 76 files need division-free restatement (q⁻¹/field_simp) or are concrete ℚ data; awaiting owner choice for a units-restatement pass.
