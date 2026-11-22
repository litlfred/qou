---
# qou-y1qu
title: Triage the 156 decl-not-found skips in lean-triviality.json
status: completed
type: task
priority: low
tags:
    - lean
created_at: 2026-11-22T09:20:32Z
updated_at: 2026-11-22T09:59:45Z
parent: qou-uwyf
---

The 2026-11-21 sweep skips 156 blocks as decl-not-found (33 in August), because the probe reads only the sibling .lean and those 95 files now elaborate. For each: is the ref wrong, or does the declaration live in the library? Cross-check with computations/audits/lean-ref-resolution-audit.witness.json. Possibly teach the probe to follow the ref into the lake root.

Record: docs/audits/2026-11-22-lean-audit-snapshot-gaps.md (§4). Epic qou-uwyf.



## 2026-11-22 — triaged (thread 'Make the triviality probe see library decls')

156 = 55 declared in own file under a qualified spelling (probe compared only the last component) + 77 declared in one library file (probe read only the sibling) + 24 unresolved refs (snapshot's refs). On current refs at #8977's head, 14 unresolved: 5 already covered (qou-mhzl, qou-02q4 x3, field), 9 new -> qou-5n04. Also found: the probe CLI never configured Lean packages, so 397 library-only blocks drop out of a bare CLI run unseen. Probe fix: litlfred/folio-assistant-sci#213. Record: docs/audits/2026-11-22-triviality-decl-not-found-triage.md. Lean-backed re-probe running.



2026-11-22 Lean-backed re-probe of the 156 + mass_tower (157): 7 closed (trivial 1, omega 1, aesop 4, cases-decide 1), 126 open, 24 unresolved refs, 0 skipped. Closed: MassIdentity.exists, genus_maximal_descent, torus_knot_shell_binding, CategoricalAction.unique, minimal_z5_classification, MassIdentity.unique, mass_tower_coefficient_stratification. Remaining ref defects in qou-5n04 / qou-02q4 / qou-mhzl. Triage done; the snapshot itself is not regenerated here.
