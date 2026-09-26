---
# qou-9ta3
title: 15 live witnesses have no producer that can recompute them
status: todo
type: task
priority: normal
created_at: 2026-08-28T15:43:20Z
updated_at: 2026-08-28T15:43:21Z
parent: qou-a1lw
---

Measured on cdbdc84af1: of the 268 witnesses carrying the OLD-MUON value B (prefix 1.109978595554), 225 cannot be re-run. 210 of those are under computations/_deprecated/ and are out of scope, but 15 are LIVE - 13 with scriptFile: null (including seven keystone-*.witness.json) and 2 whose scriptFile field is prose saying the producer is gone. Nine are PRIMARY class, i.e. the number recorded IS the producer's own working q0. No anchor migration can fix these: the number cannot be recomputed because nothing in the tree knows how it was computed. Re-running a producer that never emitted provenance also DELETES fields backfilled downstream (the aoperator_a5_crosscheck pattern), so this is one producer at a time, not a sweep. Enumerated in docs/audits/2026-08-28-old-muon-b-population-triage.md. PR #5889.
