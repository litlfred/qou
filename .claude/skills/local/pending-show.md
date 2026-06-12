---
name: pending-show
description: Show the current session's pending work — todos + ledger intent + open queue items the agent is working. Read-only.
roles: [reader, collaborator, owner]
user_invocable: true
---

# /pending-show — what is this session working on?

Quick status display. Read-only. Run any time to answer "where am I?"
or "what did I say I was going to do?".

## What it shows

In order:

1. **Current branch + PR.** Branch name, PR number (if open), PR title.
2. **TodoWrite list.** Current in-memory todos for this session (the
   highest-priority queue per CLAUDE.md §Agent work-plan policy).
3. **Goal scope.** From `STATUS.md`: which goal(s) the current PR
   touches.
4. **Master ledger intent.** The "INTENT" cell of the current
   session-log row in `docs/coordination/<goal>.md`.
5. **Queue assignments.** Items in `.beans/<goal>-queue.json` where
   `assignee == current branch` or `co_assignees` contains it.
6. **Active sibling PRs on the same goal.** From the ledger's
   "Active PRs" table.
7. **Watched events.** Subscribed PR activity (from
   `mcp__github__subscribe_pr_activity` state).

## Output format (compact)

```
## Session pending — 2026-05-31 14:32 UTC

Branch:  claude/coord-infra-1ppq-2026-05-31
PR:      #1580 — coord(infra): STATUS.md + 1ppq-qbeta master ledger

TodoWrite (5 items, 1 in progress):
  ✓ create STATUS.md + master ledger
  ✓ open PR #1580
  ✓ coord post on #1577
  ⟳ implement /session-intent + /pending-show + hook  ← current
  ○ start probe-c3-q0-stability work

Goal: 1ppq-qbeta (also touches: coord-infra)

Ledger intent (docs/coordination/1ppq-qbeta.md):
  (1) create ledger + STATUS.md, (2) coord with #1577,
  (3) ask user about queue-schema formalization,
  (4) probe c_3 q_0-stability if scope permits

Queue (.beans/1ppq-qbeta-queue.json):
  probe-c3-q0-stability     in_progress  high   you
  probe-c4-habiro           blocked      high   waiting on c3
  probe-c5-c7-habiro        blocked      med    waiting on c4
  probe-ck-lean-3bcond      open         med    nobody
  probe-precision-headroom  open         low    nobody

Sibling PRs on 1ppq-qbeta:
  #1577 canonical-watcher (flip-flop prevention) — coord posted
  #1521 Habiro categorical 1-loop (c_k source) — watching

Watched events:
  PR #1580 (own) — open
  PR #1577 (sibling) — subscribed
```

## Implementation

This is a thin reader. No writes. Sources (read order):

1. `git branch --show-current`
2. `mcp__github__list_pull_requests({head: "<branch>"})` for PR number
3. In-session TodoWrite state
4. `STATUS.md` — find row where "Active PRs" contains current PR
5. `docs/coordination/<goal>.md` — find session-log row for current branch
6. `.beans/<goal>-queue.json` — filter `assignee == branch`
7. Subscribed PR activity (session state)

When ANY of these sources is missing or stale, surface it as a
warning rather than silently omitting:

```
⚠ .beans/1ppq-qbeta-queue.json: not found — run /session-intent to initialize
⚠ STATUS.md: current PR not in any goal row — please assign goal
```

## When to invoke

- User asks "what are you working on?" / "what's left?" / "status?".
- Mid-session checkpoint — ensure ledger and queue are consistent
  with TodoWrite state.
- Before a context handoff (compaction event, end of session).

## When NOT to invoke

- During tight tool loops (e.g. iterating on a Lean proof) — would
  spam the chat with status output.
- For another agent's session — this skill is local to the calling
  session.
