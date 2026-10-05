---
# qou-kumy
title: '[TOOLS T6] witness-refresh BPMN process over run_pipeline.py (+ the overnight drivers)'
status: todo
type: feature
priority: normal
tags:
    - migration
    - tools
created_at: 2026-10-04T16:35:42Z
updated_at: 2026-10-05T08:40:38Z
parent: qou-k3er
---

From the TOOLS migration analysis (2026-10-04), story T6. Full report: docs/audits/2026-10-04-workplan-and-migration/TOOLS_report.md.

| T6 | `witness-refresh` BPMN process over `run_pipeline.py` (+ the overnight drivers) | process loads in `workflow_list`; a dry run lists stale producers identical to `run_pipeline.py --dry-run`; no witness rewritten; f-a bean `1l13` answered | M | T5 |

Owner hard rule: no math or physics content is changed. Done-when must include the content-parity check.


2026-10-05 — process + plan Tool landed on claude/tools-witness-refresh-2026-10-05.
- processes/content/witness-refresh.bpmn (Process_WitnessRefresh, strict): plan → parity → owner approval (userTask) → run → gates → commit; 'no' ends unchanged. loadProcessModel parses it; processFiles finds it via the new 'processes' entry in qou.json.
- tool-defs: Tool 'witness-refresh-plan' wraps run_pipeline.py --dry-run --content-only (satisfies compute-audit). discoverTools(qou) = 205 Tools, 0 failures, 0 missing invoke paths.
- Dry run measured: 227 scripts would run; tree unchanged afterwards.
- Parity: computations/folio/lean index sha unchanged; no witness/lean/md diff.
Still open: answer platform bean folio-assistant-1l13.
