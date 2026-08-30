---
# qou-gwe9
title: 'MEASURED: Copilot review does not arrive — AGENTS.md rule 10''s last surviving Phase-4 gate'
status: in-progress
type: bug
priority: normal
created_at: 2026-08-23T00:39:14Z
updated_at: 2026-08-30T09:06:36Z
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


## CLOSED 2026-08-28 — a sibling landed the correction, with better evidence

AGENTS.md rule 10's gate table now carries the corrected row, citing this
bean by name:

  | Copilot review | **Does not arrive.** Measured n=5 (bean `qou-gwe9`):
    requested explicitly via `request_copilot_review` on #5474, #5495,
    #5411, #5459, #5482 -- zero reviews every time, and `get_check_runs`
    returns `total_count: 0` rather than a queued
    `copilot-pull-request-reviewer` run, so nothing is ever enqueued. ... |

That is STRONGER than what this bean recorded. My n=2 controlled cases
established only that no review arrived; the `get_check_runs` observation
establishes the MECHANISM -- nothing is ever enqueued -- which is the
difference between "slow" and "absent", and I had explicitly flagged that
as the thing I could not see.

The banner now also states the consequence I raised: "the Phase-4 gate
table now has ZERO live external gates, not one ... the agent's own
verification is not the last gate standing -- it is the ONLY gate", and
tells agents to skip prepare-merge-auto Phase 1b's 15-minute poll citing
this bean.

Independent confirmation since: 12 merged PRs sampled 2026-08-22..27
spanning #5415-#5880 carry zero reviews of any kind, and a THIRD explicit
request (#5532) also produced none.

Residual fixed here: the banner HEADING still read "Two of the three
original gates no longer exist" while its own table and closing paragraph
both say three. Corrected -- that heading is the line a skimming agent
reads.



## REOPENED 2026-08-30 — Copilot reviews again; the rule was self-sealing

Write-up: `docs/audits/2026-08-30-copilot-review-works-again.md`.

**Measured first-hand today, two repos:**
| PR | requested | review | latency |
|---|---|---|---|
| qou#6122 | 07:24Z | **07:27:39Z** | ~3 min |
| folio-assistant#153 | 07:48Z | **07:51:52Z** | ~4 min |

Both `copilot-pull-request-reviewer[bot]`, both COMMENTED with line-level
findings. 5 of 6 findings were real defects; 4 were mine. The second row is the
important one — a DIFFERENT REPO, so this is not a qou-specific setting.

**This bean was not wrong.** It recorded n=2 controlled, called its five
background PRs weak evidence, and said outright it did NOT prove org-level
disablement. The later strengthening (5 requests + `get_check_runs
total_count: 0` mechanism + #5532 + ~12 background PRs) was also sound. And it
was not merely slow: **#5495, this bean's own controlled case, still shows zero
reviews eight days on.** The behaviour changed between 2026-08-27 and 08-30.

**THE DEFECT IS DOWNSTREAM.** AGENTS.md rule 10 turned the observation into an
instruction: *"that wait can only expire, so skip it and record why (citing
qou-gwe9)"*. That instruction PREVENTS THE OBSERVATION THAT WOULD FALSIFY IT —
an agent who never waits never sees a review arrive. Self-sealing.

**Measured cost this session:** I merged #6068 at 06:59Z having requested
Copilot at ~06:57Z, ~2 min earlier, because the rule said not to wait. #6068
shows zero reviews — not because none was coming, but because I merged inside
the latency window. Every finding Copilot later made on #6122 applied to code
that also shipped in #6068.

**Generalises:** the corpus has many correctly-scoped measurements that became
standing facts (the 4.6e6 slope, ~840 muon witnesses, the 39/73/58 % figures).
This is that class plus a turn of the screw — the stale fact is wired into an
instruction that suppresses re-measurement. Test for any such rule: *if this
became false, what would notice?* If the answer is "nothing, the rule says
don't look", it needs an expiry or a cheap periodic probe.

**Still to do (NOT done here):** rewrite the Copilot row in AGENTS.md rule 10
and prepare-merge-auto Phase 1b from "does not arrive" to "arrives in ~3-4
min; wait for it". Left out of the audit deliberately — it belongs with a
revisit of the 15-minute poll duration, and this file is the measurement that
justifies it.



## 🛑 QUOTA — the mechanism, found the hard way (2026-08-30 07:56Z)

Third request on #6122 returned, from the same bot:

> *"Copilot was unable to review this pull request because the user who
> requested the review has reached their **quota limit**."*

**Copilot review is RATIONED, not binary available/unavailable.** Five requests
across two repos in ~30 min — three of them fired while chasing this very
measurement — exhausted it. That is my own error and nothing in the repo's docs
warns of it.

**Candidate, NOT established, explanation for the historical zeros.** Signature
mismatch: today's exhaustion ANNOUNCES ITSELF as a posted review, whereas this
bean recorded `get_check_runs total_count: 0` with nothing enqueued and no
message at all. Either the older exhaustion was silent and the message is new,
or they are different failure modes. Cannot tell from here, and it matters:
"over quota all along" and "off, then back" imply different operating rules.

**Actionable now:** request Copilot ONCE per PR, when the branch is actually
ready, and wait ~3-4 min. Not after every push.

## Footnote: 5 of 6 findings real, 1 false — and the false one mattered

Copilot's second #6122 review claimed the refutation proofs "leave goals
unsolved" because `norm_num at h` does not close `False`. **It does**, when
`h` reduces to `False`. Verified: lean-direct exit 0, 0 errors, 0 sorry, and
`#print axioms` on both named proofs shows only propext / Classical.choice /
Quot.sound — no sorryAx.

The correct handling was NOT to apply the suggested fix. Rewriting two working
proofs to satisfy a speculative comment is the same failure as widening a
baseline to make a gate green.

**Independent corroboration (second session, same day):** PR #6124 (check run enqueued, in_progress) and PR #6129 (full review submitted ~4 min after request: 4 substantive inline comments, all verified-real, addressed same session). Matches the reopened record above; and the quota mechanism explains that session's later thread-resolution 'rate limit' errors.

## Addendum (session tender-keller, PR #6119): one review arrived UNREQUESTED

Not a separate finding — the sections above are the measurement, and this is one
more row for their table. Recording it only because it differs in the variable
their two rows hold fixed:

  qou#6119   push 07:25:09Z   review 07:27:31Z   ~2.5 min   NOT REQUESTED

I never called `request_copilot_review` on that push. Both rows in the table
above are explicit requests, so this says the trigger is not solely a request —
a push alone can draw one.

**Bearing on the open mechanism question.** The QUOTA section asks whether the
historical zeros were "over quota all along" or "off, then back", and notes the
two imply different operating rules. An unrequested review consumes quota that
nobody spent deliberately, which fits "over quota all along" more comfortably
than the request-only reading does — but it does not settle it, and I am not
claiming it does. One observation, offered as a constraint on the candidates.

The finding itself was correct and substantive (two `rfl` proofs of
`tr_M(1) = 1` that should have used the `MarkovTrace.normalised` axiom, since
the enclosing theorems quantify over an arbitrary decomposition). Fixed,
thread resolved.

**My own AGENTS.md correction is SUPERSEDED and was dropped**, not merged: it
was n=1, request-agnostic, and had none of the quota mechanism or the
self-sealing diagnosis. The rule-10 row on `main` is the sibling's and should
stay that way.


---

## Data point 2026-08-30 — a review on a push with NO contemporaneous request

Recorded because `docs/audits/2026-08-30-copilot-review-works-again.md` states
it **cannot** separate the push-trigger and request-trigger hypotheses — *"in
all three of my cases I pushed and requested within moments of each other. A
push-triggered review and a request-triggered review are indistinguishable from
my timings."* This session happened to separate them, by accident rather than
design.

| PR | push | `request_copilot_review` | outcome |
|---|---|---|---|
| #5744 | `7747b365ff` 03:03:54Z | immediately after, ~03:05Z | **nothing** |
| #5744 | `2e6be9054d` 07:41:50Z | **none at this time** | **review 07:52:18Z, `commit_id = 2e6be9054d`** |
| #6090 | `54958f587e` 08:48:01Z | 08:52Z | nothing by 09:05Z |

**Row 2 is the one the audit lacked.** A review arrived **10m28s after a push**
with no request anywhere near it, carrying that push's commit as its
`commit_id`. That is consistent with the sibling's hypothesis (Copilot reviews
on its own trigger) and is *not* what a request-triggered model predicts, since
the only request on that PR was **4h38m earlier** and had produced nothing for
those 4h38m.

**What this does NOT establish, stated because the audit's own error was
over-reading a single signature:**

* It is not "no request ever" — a request existed on #5744, just 4h38m before.
  A request-triggered review with multi-hour latency is not excluded, though it
  would have to explain why the latency landed 10 minutes after an unrelated
  push.
* **Row 3 discriminates nothing.** It is consistent with quota exhaustion
  (another agent hit the limit at 07:56Z, between rows 2 and 3), and equally
  consistent with a push-trigger that simply had not fired yet. Note it produced
  **no quota message at all**, whereas the audit records exhaustion
  *announcing itself* as a posted review — so either the message is not always
  posted, or row 3 is not quota. Undetermined.
* **Latency: the audit's table says ~3–4 min; this measured 10m28s.** One
  sample, but it is push→review, whereas the audit's is request→review, so the
  two numbers are not measuring the same interval and should not be averaged.

**Operational consequence, which holds under every candidate:** the corrected
rule *"request once, do not wait, but it can arrive"* needs its second half
taken seriously. On #5744 the review landed on the exact head that was merged
minutes later, and was merged over unread — both of its findings were real, and
one pointed at a defect worse than reported (two new `references.ts` entries
inserted **between** the `Kawauchi 1996` banner and its own entry, orphaning
both). Checking back before merging is the part that failed, not the not-waiting.
