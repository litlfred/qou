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

## Corroboration 2026-08-22/23 — three more controlled cases (n=2 -> n=5)

Independently observed before this bean was read, in a separate session
running /prepare-merge three times. Same protocol: Copilot requested via
`mcp__github__request_copilot_review`, then polled with
`pull_request_read get_reviews` + `get_check_runs`.

  #5411  requested 2026-08-22 ~12:22Z  polled ~5/~8/~12 min  0 reviews, 0 check runs
  #5459  requested 2026-08-22 ~19:0xZ  polled to 5+ min      0 reviews, 0 check runs
  #5482  requested 2026-08-22 ~20:46Z  polled to 5+ min      0 reviews, 0 check runs

All three merged on agent verification alone. Notes that sharpen the
original measurement:

1. **`get_check_runs` returns `total_count: 0`**, not a queued or
   in_progress `copilot-pull-request-reviewer` run. So this is not a slow
   reviewer that could still land — nothing is ever enqueued. The 15-minute
   wait protocol in prepare-merge-auto Phase 1b polls for a check run that
   does not get created.
2. **Re-requesting after a force-push does not help.** #5459 was requested,
   rebased + force-pushed, then re-requested against the new head per the
   staleness rule. Still 0.
3. **File type is not the discriminator.** The three span new Lean
   (#5459), a 20-file revert (#5411), and a `.beans/`-only change (#5482).
   prepare-merge-auto's "no check run after 2 minutes -> reviewer did not
   trigger for this file type" reads as a file-type quirk; across n=5 it
   looks unconditional.

Consequence for rule 10: with CI dispatch-only and Gemini sunset, the
Phase-4 gate table now has **zero** live external gates, not one. The
agent's own verification is not the last gate standing — it is the only
one. Worth saying plainly in AGENTS.md rather than leaving Copilot listed
as "the one review to wait on", because the wait is what the protocol
still prescribes and it always expires.
