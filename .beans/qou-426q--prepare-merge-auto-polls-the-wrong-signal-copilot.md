---
# qou-426q
title: 'prepare-merge-auto polls the wrong signal: Copilot reviews without ever creating a check run'
status: todo
type: task
priority: normal
created_at: 2026-08-30T07:56:54Z
updated_at: 2026-08-30T07:57:27Z
---

`qou-gwe9` (n=5) concluded that Copilot "never enqueues" and
`.claude/skills/local/prepare-merge-auto.md` acts on it with a 🛑 banner:
"**MEASURED 2026-08-23 — do NOT run this wait. Copilot never enqueues.**" and
"proceed immediately with 0 comments".

**That conclusion is half right, and the wrong half is the operative one.**

MEASURED 2026-08-30 on PRs #6104, #6116, #6132:

  get_check_runs -> {"total_count": 0, "check_runs": []}      <- qou-gwe9 CORRECT
  Copilot review arrived on #6104 and #6116                    <- qou-gwe9 WRONG

Both PRs were merged on the strength of the "do not wait" guidance, and the
reviews landed MINUTES LATER. They carried six findings, one of which was a
real correctness regression I had introduced (a tautology in a three-path
cross-check: seeding the markov_peel column from the bridge witness, so
`peel_vs_bridge_ratio` — printed under "should be ~ 1.0" — read exactly 1.0
by construction). See PR #6132.

## The mechanism

Copilot delivers a review as a `pull_request_review.submitted` WEBHOOK EVENT.
It does NOT create a `copilot-pull-request-reviewer` CHECK RUN.

The skill's wait protocol, step 1, polls `get_check_runs` for exactly that
check run. So the poll is structurally incapable of observing the thing it is
waiting for, and `total_count: 0` was read as "no review is coming" when it
only ever meant "this is not delivered as a check run".

This is the detector-blindness pattern AGENTS.md catalogues, applied to the
merge pipeline itself: **the signal was measured correctly and the wrong
signal was measured.** n=5 on a blind instrument is n=0 on the question.

## What to change

- `prepare-merge-auto.md` Phase 1b: stop citing `get_check_runs` as evidence
  that no review is coming. The observable channel is the
  `pull_request_review.submitted` event delivered through
  `subscribe_pr_activity` / ReadNotifications.
- Do NOT restore a 15-minute blocking poll on check runs — that half of
  qou-gwe9 stands, and the poll would still see nothing.
- An agent that has subscribed to the PR will RECEIVE the review as a wake.
  The honest posture is: merge is not gated on a check run that does not
  exist, but a subscribed session should expect a review wake and must handle
  it — which, post-merge, means a follow-up PR rather than nothing.

## What is NOT established

Latency. Both observed reviews arrived within a few minutes, but I have not
measured a distribution, so I cannot say how long a wait would need to be to
be reliable. Do not write a specific wait window into the skill on the
strength of n=2.

Nor whether the earlier n=5 sample genuinely received no reviews: those PRs
may have been reviewed and the review missed for the same reason — nobody was
watching the event channel. That would make qou-gwe9's negative an artefact of
its own instrument end to end, but it is UNVERIFIED and should not be asserted.
