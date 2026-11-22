---
# qou-y1qu
title: Triage the 156 decl-not-found skips in lean-triviality.json
status: todo
type: task
priority: low
tags:
    - lean
created_at: 2026-11-22T09:20:32Z
updated_at: 2026-11-22T09:20:32Z
parent: qou-uwyf
---

The 2026-11-21 sweep skips 156 blocks as decl-not-found (33 in August), because the probe reads only the sibling .lean and those 95 files now elaborate. For each: is the ref wrong, or does the declaration live in the library? Cross-check with computations/audits/lean-ref-resolution-audit.witness.json. Possibly teach the probe to follow the ref into the lake root.

Record: docs/audits/2026-11-22-lean-audit-snapshot-gaps.md (§4). Epic qou-uwyf.
