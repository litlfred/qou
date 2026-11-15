---
name: pending-show
description: Show the current session's pending work — beans list + ledger intent. Read-only.
roles: [reader, collaborator, owner]
user_invocable: true
---

# /pending-show — what is this session working on?

Quick status display. Read-only. Run any time to answer "where am I?"
or "what did I say I was going to do?".

## What it shows

In order:

1. **Current branch + PR.** Branch name, PR number (if open), PR title.
2. **Beans list.** Current in-progress or todo beans for this session (via `beans list`).
3. **Goal scope.** From `STATUS.md`: which goal(s) the current PR touches.
4. **Master ledger intent.** The "INTENT" cell of the current session-log row in `docs/coordination/<goal>.md`.

## Output format (compact)

```
## Session pending — 2026-05-31 14:32 UTC

Branch:  claude/coord-infra-1ppq-2026-05-31
PR:      #1580 — coord(infra): STATUS.md + 1ppq-qbeta master ledger

Beans (via `beans list`):
  [epic-123] Formalization Tracker (In Progress)
  [task-124] Subtask 1 (Completed)
  [task-125] Subtask 2 (In Progress)

Goal: 1ppq-qbeta (also touches: coord-infra)

Ledger intent (docs/coordination/1ppq-qbeta.md):
  (1) create ledger + STATUS.md, (2) coord with #1577,
```

## Implementation

This is a thin reader. No writes. Sources (read order):

1. `git branch --show-current`
2. `mcp__github__list_pull_requests({head: "<branch>"})` for PR number
3. Run the CLI tool `beans list` to find tasks matching the current scope.
4. `STATUS.md` — find row where "Active PRs" contains current PR
5. `docs/coordination/<goal>.md` — find session-log row for current branch

## When to invoke

- User asks "what are you working on?" / "what's left?" / "status?".
- Mid-session checkpoint — ensure ledger is consistent with Beans state.
- Before a context handoff (compaction event, end of session).
