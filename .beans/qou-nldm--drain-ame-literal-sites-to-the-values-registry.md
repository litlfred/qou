---
# qou-nldm
title: Drain AME-literal sites to the values registry
status: in-progress
type: task
created_at: 2026-08-30T08:47:57Z
updated_at: 2026-08-30T08:47:57Z
---

Route hardcoded AME binding-energy literals in computations/ to the named registry constants (AME_B_*_MEV_VALIDATION).

Roadmap from probes/ame_registry_routing_triage.py:
- SAFE (byte-exact string match): 9 sites / 4 files
- UNSAFE: 195 sites / 80 files
  - INPUT   25 sites /  7 files -- NEVER route (reaches a scale/calibration name)
  - REVIEW 170 sites / 73 files -- needs reading

Branch: claude/ame-roadmap-replant-2026-08-29 (worktree /tmp/qou-mine).

## Todo
- [x] Route the SAFE sites that survive review — 6 of 9 routed, 3 are self-test fixtures
- [x] Fix the triage: byte-exact string match is NOT sufficient for SAFE
- [x] Split REVIEW into ROUNDING (63, routable) and DIVERGENT (125, needs a ruling)
- [x] Route the 63 ROUNDING sites — verified, 0 unexplained leaves
- [x] DIVERGENT: 110 sites routed, 16 held as per-site INPUT
- [x] Rule on the self-test sites — delta_lambda routed, pin validator and dps
      audit held (each DEMONSTRATES something its own literal is required for)
- [x] REVIEW bucket is 0. The drain is complete; what remains is 25 INPUT sites
      and 6 demonstration literals, all permanently excluded with reasons.
- [x] Close verification loose ends — see qou-fsva, now completed
