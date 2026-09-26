---
# qou-z9bx
title: 'folio-assistant lake-cache: ''lake build'' after ''restore'' DESTROYS the restore'
status: todo
type: task
priority: normal
created_at: 2026-08-07T11:13:11Z
updated_at: 2026-08-07T11:13:13Z
parent: qou-kemt
---

Measured 2026-08-07 in a fresh cloud container, folio-assistant @ 0c1af34 (the new scripts/lake-cache.sh).\n\nSEQUENCE: lake-cache.sh restore -> 7268 oleans, exit 0. lake-cache.sh doctor -> 'next step: cache is present -- build directly.' Followed that advice: lake build QOU.Knot.WhiteheadSaddleClausen. It ran 9 minutes, timed out, and left 459 oleans -- the restored Mathlib build was GUTTED (7268 -> 459, mathlib alone down to 228).\n\nSo the doctor's recommended next step is the thing that destroys the artifact restore just produced. AGENTS.md already warns about this ('a stray lake build already dropped the olean count ... re-restore the cache branch before lean-direct'), but the new script's own guidance contradicts it.\n\nSUGGESTED FIX: either doctor should recommend lean-direct rather than 'build directly', or restore should record the expected olean count so a post-build check can detect the wipe, or the script should wrap lake build in a guard. At minimum the skill doc should carry the warning AGENTS.md already has.
