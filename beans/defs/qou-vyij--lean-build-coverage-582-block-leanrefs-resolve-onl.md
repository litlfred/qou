---
# qou-vyij
title: 'Lean build coverage: 582 block lean.refs resolve only to .lean files no CI Lake target compiles'
status: in-progress
type: task
tags:
    - reorg-2026-10-04
    - orphan-census
    - needs-owner
created_at: 2026-10-04T15:31:23Z
updated_at: 2026-10-04T15:31:23Z
parent: qou-6qbv
---

833 chapter-dir .lean files declare names absent from every lake target; only 654 of 1,309 lean.refs (50%) resolve into the compiled library. The uncompiled siblings are built only by the dispatch-only lean-content-siblings.yml. Decide build coverage before trusting 'sorry-free' as evidence (12 closures tagged verify-build).

Found by the orphaned-content census 2026-10-04 (inventory: 3,383 rows). Report only: no math or physics content is to be changed; this item links, builds or places existing content.
