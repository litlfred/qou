---
# qou-j50l
title: 'Platform (litlfred/cat-harness): Formalize swarm-monitor skill, human-consumable milestone/epic status contract, & BPMN dispatch/monitor process'
status: in-progress
type: feature
priority: high
created_at: 2026-11-23T21:34:14Z
updated_at: 2026-11-23T21:34:14Z
parent: qou-hksc
---

Claimed by claude/swarm-monitor-skill-process-20261123 on litlfred/cat-harness (Worker 19). Formalize a platform-generic 'swarm-monitor' skill (sdlc/skills/sdlc-core/swarm-monitor.md), update dispatch-agent.md & swarm-management.md, and add a formal BPMN process (sdlc/processes/swarm-dispatch-and-monitor.bpmn + generated .checklist.md & .svg) in litlfred/cat-harness. Core requirements: (1) swarm monitor runs as an explicit role/loop whenever dispatching a swarm; (2) mandatory human-consumable status contract banning internal session shorthands (no bare PR numbers or opaque worker codes like W2/W4 without plain-English deliverable, evidence/metric delta, and remaining scope); (3) dual reporting of Repo Queue Scoreboard (PRs | Beans | Issues: open, ready, external/held, preparing, closed today) + Milestone & Epic substantive rollups; (4) stall/drift/Andon-cord detection and reactive slot refill from shared beans.
