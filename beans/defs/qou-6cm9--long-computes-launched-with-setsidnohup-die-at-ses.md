---
# qou-6cm9
title: Long computes launched with setsid/nohup DIE at session boundaries; the harness's own run_in_background survives — 3 losses traced to this
status: in-progress
type: bug
priority: high
tags:
    - reorg-2026-10-04
created_at: 2026-09-08T06:02:23Z
updated_at: 2026-10-04T15:14:36Z
parent: qou-5vkl
---

## UPDATE 2026-09-08: harness tasks survived a 31-min boundary

Relaunched via run_in_background; re-checked 31 min later across a scheduled
check-in. He4 52 -> 58 banked, triton 13 -> 19 rows, both process groups alive at
~1870s elapsed. Under setsid the comparable gap banked ZERO. Mechanism confirmed
as the difference.

STILL NOT the discriminating test: this boundary fired no SessionStart:resume
hook, and the boundaries that killed the setsid jobs did. "Survives a 31-min idle
gap" is measured; "survives a resume" is not.

- **Round 95 (`litlfred/qou#8426`)**: Advanced in `feat/round95-layout-lowerbound-bondrule-maxcontact-simplex-43c1` (Commit 1 `d482ea2750e00fbd6e9e74457e935101b2f8b093`, Commit 2 `8ed5dd0ff69b4804c5e40f393e7c9157a2067a42`, probe sha256 `8b786124c3dfda15d0d1672a05f3bc16f486d17a5f41250533162305ad901679`).
