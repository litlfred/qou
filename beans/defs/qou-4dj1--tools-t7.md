---
# qou-4dj1
title: '[TOOLS T7] compute-QA process (precision-gates, staleness-gates, lp-dual, float64, word-provenance, witness-staleness…'
status: todo
type: feature
priority: normal
tags:
    - migration
    - tools
created_at: 2026-10-04T16:35:43Z
updated_at: 2026-10-04T16:36:19Z
parent: qou-k3er
---

From the TOOLS migration analysis (2026-10-04), story T7. Full report: docs/audits/2026-10-04-workplan-and-migration/TOOLS_report.md.

| T7 | `compute-QA` process (precision-gates, staleness-gates, lp-dual, float64, word-provenance, witness-staleness audits as Tools) | each workflow YAML reduced to a dispatch of the process with a `# bpmn-node:` back-reference; gate verdicts identical on `main` before and after; verdict files written to `qa-reports`, not committed | M | T5 |

Owner hard rule: no math or physics content is changed. Done-when must include the content-parity check.
