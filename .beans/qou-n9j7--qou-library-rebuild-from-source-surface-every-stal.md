---
# qou-n9j7
title: 'QOU library rebuild from source: surface every stale-cache red at once'
status: in-progress
type: task
priority: normal
created_at: 2026-09-04T12:25:52Z
updated_at: 2026-09-04T13:16:36Z
---

Motivation (measured 2026-09-03/04, PRs #6526/#6579): lean-direct on one file certifies against on-disk oleans; the restored cache is a snapshot, so main carried 10 red modules (retype + mem_addCell victims) for days, and this session also reported one FALSE red from stale dependency oleans. Nothing rebuilds the library (CI dispatch-only). Plan: topologically order every QOU module (library + content-block siblings), rebuild all from current main with lean -o in that order, log per-module status, classify reds (mechanical port vs real), fix the mechanical ones on this branch, record the rest as beans. Branch claude/qou-library-rebuild-2026-09-04.



## 2026-09-04 13:1xZ — library pass DONE: 157/158 green
Dirty closure (source newer than olean ∪ missing olean ∪ importer of dirty) = 158 of 2,597 (63/52/43), rebuilt in 842 s after a 100-module full-order first pass (0 fail). ONE red, real: ParticleInteractions/silver_ratio_beta_decay_null (own bean). The ten reds this week's PRs ported are confirmed gone. Siblings (907) next.
