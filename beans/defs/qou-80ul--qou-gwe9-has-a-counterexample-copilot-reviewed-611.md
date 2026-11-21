---
# qou-80ul
title: 'qou-gwe9 has a COUNTEREXAMPLE: Copilot reviewed #6112 (5 comments). n=5 zero-review measurement is falsified'
status: completed
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-30T07:47:23Z
updated_at: 2026-11-21T12:30:00Z
parent: qou-nu9d
---


2026-08-30. Copilot submitted a real review on PR #6112 -- state "commented",
5 review comments, 15/15 files reviewed, effort "Lite" -- roughly 40 minutes
after the PR was opened and without an explicit request_copilot_review on that
PR (one was issued on the PREDECESSOR #6101, which got nothing).

WHY THIS MATTERS. AGENTS.md rule 10 and this bean's parent record
qou-gwe9 as n=5, zero reviews, get_check_runs total_count:0, and conclude
"Copilot never enqueues". prepare-merge-auto Phase 1b tells agents to skip the
wait and record "not enqueued (measured, qou-gwe9)". I followed that on #6101
and it was correct there. It is NOT universally correct.

WHAT I DID NOT ESTABLISH, and someone should before editing rule 10:
  - whether the trigger was the PR's size/content, elapsed time, or a change
    on GitHub's side;
  - whether check_runs now reports a copilot-pull-request-reviewer run (the
    check_suite.completed event on dd484a48 says no third-party suite is
    running/failed, which is not the same as one existing);
  - whether #6101 would have received one had it not merged ~20 min in.

The review's content was USEFUL, not boilerplate: 4 of 5 comments were real
defects (a copy/paste splice of mine, a stale H1 under a re-scope banner, a
stale See-also scope label, and a surviving sentence contradicting a correction
three paragraphs above it). The 5th was a dependency claim that does not hold
(canonical_braid_crossings imports hecke_core internally at line 159), which I
checked rather than accepted.

So the operational advice "do not WAIT for Copilot" may still be right on
median, while "Copilot never enqueues" is now false. Rule 10's table row and
prepare-merge-auto's banner should be re-measured rather than edited from this
single observation.


## 2026-11-21 — verified on main and closed (bean drain wave 1, cat-harness-migr)

Session: https://claude.ai/code/session_01Qmmkt7b8yRZEmMY5Qwa33W. Checked against `origin/main` `2ae54ab4010`.

- The counterexample was taken in: AGENTS.md rule 10's Copilot row now reads 'CORRECTED 2026-08-30 — reviews DO arrive, and are RATIONED', citing `docs/audits/2026-08-30-copilot-review-works-again.md` and reopening `qou-gwe9`. The re-measurement this bean asked for continues in `qou-gwe9`.
