---
# j8el
title: 'FOLLOW-UP (qou): relocate todos/ queues into .beans/ + repoint readers'
status: completed
type: task
priority: normal
created_at: 2026-06-19T17:44:29Z
updated_at: 2026-06-20T17:30:33Z
parent: 5gw5
---

Blocked on folio-asst handoff item 4: the todos/*.json watcher queues are read by runtime code (MCP /api/todos, content/pipeline/qa-agent-drain-queue.ts) + 7 watcher skills. Repoint readers BEFORE relocating JSON. beans != sidecars: watcher/QA queues stay as bulk JSON under .beans/, not converted to beans.
