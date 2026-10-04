---
# qou-qb6t
title: '[TOOLS T1] f-a: computation-witness graph kind + Zod computation-witness/v1 (sci)'
status: todo
type: feature
priority: normal
tags:
    - migration
    - tools
    - upstream-fa
created_at: 2026-10-04T16:35:40Z
updated_at: 2026-10-04T16:36:17Z
parent: qou-k3er
---

From the TOOLS migration analysis (2026-10-04), story T1. Full report: docs/audits/2026-10-04-workplan-and-migration/TOOLS_report.md.

| T1 | f-a: `computation-witness` graph kind + Zod `computation-witness/v1` (sci) | kind registered with `holds: derived`; Zod parses all 3,509 qou witnesses (or lists the failures as a finding, without "fixing" them); `ComputationWitness` reconciled with `scriptHash`/`scriptFile`; `check:kind-validators` green | M | — |

Also proposed independently as TARGET T3 (Zod ComputationWitnessSchema, cat-harness).

Owner hard rule: no math or physics content is changed. Done-when must include the content-parity check.
