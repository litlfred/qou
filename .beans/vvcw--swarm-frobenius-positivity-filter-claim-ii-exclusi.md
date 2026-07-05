---
# vvcw
title: 'Swarm: frobenius_positivity_filter claim_ii_exclusion_count (Config cardinality — likely closeable)'
status: in-progress
type: task
priority: normal
created_at: 2026-07-05T23:07:21Z
updated_at: 2026-07-05T23:08:37Z
parent: uudc
---


## Swarm finding (assessed — WALL, no honest close)
Single sorry `frobenius_positivity_filter : (excludedConfigs P).card = 2^(A-1)` is **false for generic `P`** (all-positive parent/daughter products ⇒ excludedConfigs empty ⇒ card 0 ≠ 2^(A-1)). Only true under the unformalised Hoefsmit spectator-factor sign structure + confinement-LP feasibility `Gx ≥ 0`, absent from Mathlib + this file. Honest cited sorry stays.
**FOLLOW-UP (not this tranche):** restate §3b-cond with the sign-structure as an explicit `[class]` hypothesis so the statement is not universally-false.
