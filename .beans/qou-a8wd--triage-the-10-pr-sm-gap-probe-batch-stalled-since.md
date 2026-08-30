---
# qou-a8wd
title: Triage the 10-PR SM-gap probe batch stalled since 2026-08-02
status: completed
type: task
priority: normal
created_at: 2026-08-10T02:48:41Z
updated_at: 2026-08-10T03:04:32Z
parent: qou-531z
---

Landing analysis over all 17 stalled PRs. RESULT REFUTES THE HYPOTHESIS: only 1 of 17 is absorbed, not most. #4589 fully absorbed (3 files byte-identical) -> CLOSED. 15 are LIVE with real unlanded content (#4684 1373 unique lines, #4600 890, #4565 861, #4588 563, #4584 555, #4614 480, #4618 410, #4656 302, #4617 258, #4564 235, #4561 181, #4562 171, #4608 87, #4582 8, #4682 50 in a bean). #4514 UNDETERMINED - no merge-base at depth 2000; my first-pass script false-reported it ABSORBED from an empty file list. Retraction posted on #4514.
