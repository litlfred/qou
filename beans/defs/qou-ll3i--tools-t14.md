---
# qou-ll3i
title: '[TOOLS T14] qou-mass vendor drift → a declared Tool with maintains, plus a drift gate'
status: completed
type: feature
priority: normal
tags:
    - migration
    - tools
    - needs-owner
created_at: 2026-10-04T16:35:46Z
updated_at: 2026-10-05T15:37:04Z
parent: qou-k3er
---

From the TOOLS migration analysis (2026-10-04), story T14. Full report: docs/audits/2026-10-04-workplan-and-migration/TOOLS_report.md.

| T14 | `qou-mass` vendor drift → a declared Tool with `maintains`, plus a drift gate | the gate reports 12/164 today without regenerating anything | S | owner (§5.7) |

Owner hard rule: no math or physics content is changed. Done-when must include the content-parity check.

Done 2026-10-05 (PR to follow). Gate `qou-mass-vendor-drift` (compute-QA, warn, Task_Staleness) runs `sync-qou-mass-vendor.py --check` and writes nothing; today: 7 drifted + 1 missing (`binding-canonical.witness.json`). Tool `qou-mass-vendor-sync` declares the `--apply` with `downstream` (output qou-mass/src/qou_mass/_internal), NOT `maintains` — schemas/tool.ts reserves maintains for published artefacts and _internal/ is not published. Running --apply (a regeneration) still waits on the owner (TOOLS §5.7). Also fixed: compute-qa recorded a non-zero warn/advisory gate as PASS; it now records WARN. Parity: no witness/.lean/folio/qou-mass diff.
