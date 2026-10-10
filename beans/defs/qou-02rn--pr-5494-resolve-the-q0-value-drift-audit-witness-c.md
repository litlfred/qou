---
# qou-02rn
title: 'PR #5494: resolve the q0-value-drift-audit witness conflict against main and re-verify'
status: completed
type: task
priority: normal
created_at: 2026-08-23T13:04:34Z
updated_at: 2026-08-23T13:23:27Z
---


## DONE 2026-08-23 — merged main into the head, producer-resolved

Conflict was `computations/q0-value-drift-audit.witness.json` on the counts.
Resolved by re-running the producer on the merged tree; `-10 canonical`
and `-9 STALE` = `+19 proton-pin`, exactly the 19 witnesses the branch
re-pins. The +1 canonical / -1 STALE vs the branch's own pre-merge numbers
is MAIN's (upstream `3f63d180`), not ours.

Full precision-gate battery exit 0, vendor sync in sync, contradictions
still 2. PR now `mergeable_state: clean`. Pushed `8f5f8d94`, no force.

Self-caught error: the first merge commit captured the pre-regeneration
counts because `git add` ran before the producer. The gate run surfaced it;
amended pre-push and verified with `git show HEAD:` rather than the
worktree — reading the worktree is what hid it.

Deliberately NOT committed: `q0-anchor-consistency-audit.witness.json`.
This container lacks clarabel/numpy/scipy and has mpmath 1.3.0 vs the
recorded 1.4.1, so the regenerated copy records a WEAKER environment block.
Not in the branch's change set; reverted.
