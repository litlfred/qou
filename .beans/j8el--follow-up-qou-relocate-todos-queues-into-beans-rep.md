---
# j8el
title: 'FOLLOW-UP (qou): relocate todos/ queues into .beans/ + repoint readers'
status: completed
type: task
priority: normal
created_at: 2026-06-19T17:44:29Z
updated_at: 2026-06-21T19:15:28Z
parent: 5gw5
---

Blocked on folio-asst handoff item 4: the todos/*.json watcher queues are read by runtime code (MCP /api/todos, content/pipeline/qa-agent-drain-queue.ts) + 7 watcher skills. Repoint readers BEFORE relocating JSON. beans != sidecars: watcher/QA queues stay as bulk JSON under .beans/, not converted to beans.

UPDATE (2026-06-20): superseded — a sibling completed this on main (commit ddfbfbba "infra(beans): relocate 3 work-plan goal queues todos/ -> .beans/"). 3 of 4 queues (1ppq-qbeta, lean-discharge, research) now under .beans/; runtime coupling was light (folio-assistant had NO hardcoded todos/ ref; only the throwaway root fix_json.py). One straggler remains in todos/: qa-q-CAL-1-2-3-audit.json (minor). Not re-done here to avoid duplication.
