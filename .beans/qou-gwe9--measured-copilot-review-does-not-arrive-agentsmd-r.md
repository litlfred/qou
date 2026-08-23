---
# qou-gwe9
title: 'MEASURED: Copilot review does not arrive — AGENTS.md rule 10''s last surviving Phase-4 gate'
status: todo
type: bug
created_at: 2026-08-23T00:39:14Z
updated_at: 2026-08-23T00:39:14Z
---

Recorded from the #5495 check-in loop, on the third consecutive no-change
check.

## The claim in AGENTS.md

Rule 10's table (§"Branch + PR workflow", the 2026-08-07 correction) marks
two of the three original Phase-4 gates as gone and keeps one:

  | CI green       | Unavailable. Auto-triggers disabled repo-wide.        |
  | Gemini review  | Gone. Consumer Gemini Code Assist sunset 2026-08-01.  |
  | Copilot review | Still expected — this is the one review to wait on.   |

## What was measured (2026-08-23, ~00:40 UTC)

CONTROLLED CASE — Copilot review explicitly requested via
`mcp__github__request_copilot_review`:

  #5474   requested 2026-08-22 ~19:56Z   merged 21:08Z   0 reviews (75+ min)
  #5495   requested 2026-08-22 ~21:23Z   still open       0 reviews (3+ hrs)

BACKGROUND — five other agents' recently-merged PRs, `get_reviews`:

  #5415  0    #5464  0    #5481  0    #5487  0    #5490  0

Seven PRs, zero reviews of any kind.

## What this does and does not establish

DOES: on both PRs where Copilot review was explicitly requested, none
arrived, over 75 minutes and 3+ hours respectively. And no review of any
kind appears on the five sampled sibling PRs.

DOES NOT: prove Copilot is disabled at the org/repo level. The five
background PRs may simply never have requested it, so they are weak
evidence; the two controlled cases are the strong ones, and n=2.

## Why it matters

If Copilot is in fact not reviewing, then ALL THREE gates rule 10 names for
Phase 4 are absent, and the §"QA is agent-owned; CI is a backup"
verification gate — the agent's own run — is not a backstop but the
ENTIRE gate. That is already the operating reality this session has been
working under (every merge verified by hand), but AGENTS.md still tells
agents to "wait for Copilot (up to 15 min)", which is a wait on something
that may never arrive.

## Next step (NOT done here — needs the owner)

Do not edit rule 10 on the strength of n=2. Either:
  (a) the owner confirms Copilot is off for this repo, and the table's
      third row is corrected the way the other two already were; or
  (b) someone checks the repo's GitHub App / Copilot settings directly,
      which no agent in this session can see.

Until then the honest posture is the one already in force: verify by hand,
state the evidence in the PR, and do not write "waiting on Copilot" as if
it were a live gate.
