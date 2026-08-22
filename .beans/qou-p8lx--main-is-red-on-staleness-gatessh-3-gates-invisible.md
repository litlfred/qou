---
# qou-p8lx
title: main is RED on staleness-gates.sh — 3 gates, invisible because --changed was skipping
status: todo
type: bug
created_at: 2026-08-22T21:04:36Z
updated_at: 2026-08-22T21:04:36Z
---

Found on PR #5474 immediately after fixing the `--changed` predicate
(qou-s2gm defect 1) so the script actually examines committed work.

MEASURED on a pristine origin/main worktree, full run (not --changed):

  git worktree add --detach /tmp/mainwt origin/main
  (cd /tmp/mainwt && bash scripts/staleness-gates.sh)   -> exit 1

  RED: scriptHash + upstream drift
       q0 constant staleness
       qou-mass vendor mirror
  ADVISORY: dependency coverage

Identical set on the #5474 branch, so these are INHERITED, not caused by
that branch. Attribution is by measurement on a clean worktree, not by
assertion.

## Why this was invisible

`scripts/staleness-gates.sh --changed` collected its relevant-file set from
`git diff --name-only HEAD` + `--cached` + `ls-files --others` — the working
tree only. Once a change is committed the set is empty, so it printed
"no witness or computations/ script touched — skipped" and exited 0.
AGENTS.md tells every agent to commit early and often, so that is the
common case. The gate has been red for an unknown length of time with
nothing reporting it.

DISTINCT FROM qou-mnrd, which tracks main being red on the raw-float64
ratchet (a precision-gates gate). These three are staleness-gates gates
and were not previously recorded.

## Do not

* do not narrow the `--changed` predicate again to make this quiet — that
  re-opens the hole #5474 closed;
* do not baseline the offenders — the ratchets drain and never grow
  (AGENTS.md).

## Next step

Triage the three separately; they are unrelated backlogs.
`qou-mass vendor mirror` is `scripts/sync-qou-mass-vendor.py --check` and
may be a one-command `--apply` (the mirror is GENERATED — see AGENTS.md,
all 14 copies had drifted when the sync script was written), so start
there. The other two are corpus-scale.
