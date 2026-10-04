---
# qou-a3l1
title: '[TOOLS T5] Wrap the 170 content-wired producers as Tool nodes (downstream = witness)'
status: todo
type: feature
priority: normal
tags:
    - migration
    - tools
created_at: 2026-10-04T16:35:42Z
updated_at: 2026-10-04T18:23:08Z
parent: qou-k3er
---

From the TOOLS migration analysis (2026-10-04), story T5. Full report: docs/audits/2026-10-04-workplan-and-migration/TOOLS_report.md.

| T5 | Wrap the 170 content-wired producers as Tool nodes (`downstream` = witness) | one Tool per producer, generated from the block manifests rather than hand-listed; global invariant holds; T4 run on a sample of ≥10 cheap producers, each pass or unknown, zero fail | L | T1, T3, T4 |

Owner hard rule: no math or physics content is changed. Done-when must include the content-parity check.


## Owner ruling 2026-10-04
Verbatim: "all witnesses tools will need to go into the KG". Every witness producer becomes a declared Tool node whose output is a witness graph node. This needs T1 (the platform computation-witness graph kind) and T5 (wrap the content-wired producers). Recorded by session_01NdDGeP1SyShmoUssLuRZ91.
