---
# qou-kvgn
title: 'Merge sweep 2026-09-07: rebase-merge every non-draft open PR whose mergeable_state is clean, verify replay per PR, report the table'
status: in-progress
type: task
priority: normal
created_at: 2026-09-07T18:25:28Z
updated_at: 2026-09-07T18:28:16Z
parent: qou-vyvt
---

Owner: 'merge the clean PRs' (2026-09-07). Rule: non-draft AND mergeable_state==clean at the moment of merge, rebase-merge, never delete branches, run scripts/verify-merge-replay.py after each. Drafts skipped. Delegated to a merge-coordinator agent; result table goes here.
