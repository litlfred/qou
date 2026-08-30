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
- [ ] Route the SAFE sites that survive review
- [ ] Fix the triage: byte-exact string match is NOT sufficient for SAFE
- [ ] Work the REVIEW bucket
- [ ] Close verification loose ends (4 unmapped witnesses, catalan_binding empty witness)
