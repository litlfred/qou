---
# qou-rep6
title: 'GUARD: warn when a commit deletes adjudicated vacuity-ledger verdicts'
status: in-progress
type: task
priority: normal
created_at: 2026-08-30T09:38:38Z
updated_at: 2026-08-30T09:39:01Z
---

## What happened

On 2026-08-30, `main` silently lost **83 adjudicated verdicts** from
`docs/audits/lean-vacuity-review-ledger.json` (368 -> 285 entries) in a sibling
branch's rebase-conflict resolution. It sat on `main` roughly two hours and was
found only because I happened to re-count.

Nothing could have caught it:

- the foreign-entries test guards `--review-ledger`'s delete loop, not a
  conflict resolution that drops entries wholesale;
- `--check-ledger` PASSES on a shrunken ledger — deleting a verdict does not
  make the survivors stale.

`scripts/resolve-vacuity-ledger-conflict.py` (merged) is the repair and only
helps someone who already knows to run it. This bean is the detection.

## What landed

PR #6162, branch `claude/ledger-shrink-guard-2026-08-30`:

- `scripts/lib/ledger_shrink_check.py` — HEAD's ledger vs staged/worktree,
  keyed `<file>::<decl>::<category>`
- `scripts/lib/test_ledger_shrink_check.py` — 5 cases; case 2 replays the real
  event from git objects `6282b3dc5` -> `aaccccac3`
- `scripts/precommit-ledger-shrink-warn.sh` — `--check` mode + hook mode
- `.claude/settings.json` — third `PreToolUse` Bash hook

## TRAP recorded in the process

The first version passed both ledgers through the environment, hit `E2BIG`
("Argument list too long"), and **still exited 0 with an empty result** — i.e.
reported clean on a real shrink. Fixed via temp files, and an empty result is
now `exit 2` / "DID NOT RUN" rather than OK. A guard that reports OK when it
did not run is worse than no guard.
