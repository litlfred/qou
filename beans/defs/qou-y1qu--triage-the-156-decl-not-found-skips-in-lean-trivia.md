---
# qou-y1qu
title: Triage the 156 decl-not-found skips in lean-triviality.json
status: in-progress
type: task
priority: low
tags:
    - lean
created_at: 2026-11-22T09:20:32Z
updated_at: 2026-11-22T09:44:01Z
parent: qou-uwyf
---

The 2026-11-21 sweep skips 156 blocks as decl-not-found (33 in August), because the probe reads only the sibling .lean and those 95 files now elaborate. For each: is the ref wrong, or does the declaration live in the library? Cross-check with computations/audits/lean-ref-resolution-audit.witness.json. Possibly teach the probe to follow the ref into the lake root.

Record: docs/audits/2026-11-22-lean-audit-snapshot-gaps.md (§4). Epic qou-uwyf.



## 2026-11-22 — triaged (thread 'Make the triviality probe see library decls')

156 = 55 declared in own file under a qualified spelling (probe compared only the last component) + 77 declared in one library file (probe read only the sibling) + 24 unresolved refs (snapshot's refs). On current refs at #8977's head, 14 unresolved: 5 already covered (qou-mhzl, qou-02q4 x3, field), 9 new -> qou-5n04. Also found: the probe CLI never configured Lean packages, so 397 library-only blocks drop out of a bare CLI run unseen. Probe fix: litlfred/folio-assistant-sci#213. Record: docs/audits/2026-11-22-triviality-decl-not-found-triage.md. Lean-backed re-probe running.
