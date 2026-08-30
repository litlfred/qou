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

---

## Independent observation from PR #6120, and how it fits the rationing finding

Recorded from a different session, arrived at before the quota message above was
visible on main. Kept because it is a data point the rationing account does not
otherwise have.

**Copilot reviewed PR #6120 WITHOUT BEING REQUESTED.** `get_check_runs` returned
a live `copilot-pull-request-reviewer` run, `status: in_progress`, started
07:25:25Z — the exact object this bean records as never being created — which
submitted a review at 07:29:29Z against `66dac18c4`: `COMMENTED`, 3 inline
comments plus 1 suppressed, effort "Lite". No `request_copilot_review` call
preceded it; it fired on PR creation.

The comments were substantive. The headline one caught a real over-claim:
a probe said `IwahoriHeckeAlgebra` without qualifying WHICH of the two
declarations of that name it analysed, and chasing that turned up prior art
(`triv_hecke`) the author had missed. See PR #6120 and bean `qou-qcy6`.

### The synthesis neither observation has alone

**Auto-triggered reviews consume the same quota.** The rationing note above
attributes exhaustion to five explicit requests; #6120 was never requested and
still got a review, so the budget is spent by PR creation too, not only by
`request_copilot_review`. That matters for the actionable rule: "request once
per PR, when ready" is necessary but not sufficient — merely OPENING PRs draws
down the same allowance, so a session that opens several in quick succession can
exhaust it without ever calling the request tool.

**It also implicates my own #6093 prepare-merge.** That run requested a Copilot
review per the skill's Phase 1b, on a PR that had already had several pushes.
Under the rationing account that request was part of what drained the budget —
and `prepare-merge-auto` currently prescribes requesting on every run.

**What is still NOT established**, and the note above is right to flag it: the
historical `total_count: 0` with no message is a different signature from
today's announced quota refusal. Silent-exhaustion and off-then-back remain
distinguishable only by evidence nobody has yet.
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
## The historical zeros: one datum that CONSTRAINS the open question above
## (session clinical-derivation-attack-vectors, PR #6131)

The QUOTA section leaves a question open and says it cannot be settled from
there: were the historical zeros "over quota all along", or "off, then back"?
It notes the two imply different operating rules, and that today's exhaustion
ANNOUNCES ITSELF as a posted review.

Measured, on exactly the five PRs this bean's original n=5 was collected from:

    get_reviews  #5474 []   #5495 []   #5411 []   #5459 []   #5482 []

ZERO reviews. Not quota refusals -- nothing posted at all, by either instrument
(get_check_runs was already recorded as total_count 0 on all five).

BEARING ON THE QUESTION, and it is a constraint rather than a settlement: if
those five had been quota exhaustion, and exhaustion announces itself as a
posted review as it did on #6122 and #6131, then get_reviews should show a
refusal on at least some of them. It shows nothing. That FAVOURS "off, then
back" over "over quota all along".

WHAT IT DOES NOT ESTABLISH, stated because the distinction is the whole point of
the open question:
  * the announcing behaviour may itself be new -- if the refusal message shipped
    between 2026-08-23 and 2026-08-30, silent exhaustion then and announced
    exhaustion now are perfectly consistent with "over quota all along". This
    bean already names that possibility and I cannot exclude it either.
  * five PRs from one day is a thin sample for a rationed resource.

So: the observation removes the easy version of "over quota all along" (the one
where refusals would have been visible), and leaves the harder version standing.
Recorded as a constraint on the candidates, in the same spirit as the #6119
unrequested-review row above.

METHOD NOTE for whoever re-measures: this is cheap and non-consuming.
get_reviews on a historical PR spends no quota, unlike a fresh
request_copilot_review. Any PR from the original window can be checked the same
way at no cost.

## Superseded record, kept for the trail

This session independently reached the quota mechanism (trial 2, #6131, 07:56Z,
same refusal text) and independently reached the "check runs are the wrong
instrument" point. BOTH ARE SUPERSEDED by the sections above, which are more
thorough -- they carry the self-sealing diagnosis, four timing rows, the
unrequested-review case and the 5-of-6 findings calibration, none of which I
had. Only the five-PR datum above is additive, and it is why this append exists
rather than a competing account.

I also over-attributed once en route, and record it since the error is
instructive: I blamed the check-run instrument for the n=5 result. The
instrument IS wrong -- Copilot produces no check run in any outcome, so a
check-run poll cannot distinguish reviewed / refused / never-asked -- but the
five PRs show nothing under get_reviews either, so the instrument was not what
produced that reading. Two independent facts; I had collapsed them.

## Second additive datum: exhausted quota is not always a refusal (2026-08-30, 09:08Z)

Same PR (#6131), same account, same day, two `request_copilot_review` calls
~63 minutes apart:

| request | head sha | outcome | latency |
|---|---|---|---|
| 07:55Z | `44f0b7d0` | **refusal posted** ("reached their quota limit") | ~40 s |
| 08:58Z | `38f674db` | **nothing** — `get_reviews` unchanged at 09:08Z | > 9 min, still silent |

The first is 13x faster than the second is old, so the second is silence, not a
slow refusal. **The same exhausted-quota state produces a refusal one hour and
silence the next.**

Consequence for the recommended poll: the sibling account above concludes a
quota refusal is actionable while silence is not. That holds, but silence is now
*less* informative than it looked -- it does not even distinguish "quota
exhausted" from "never asked", because exhausted quota is one of the things that
produces it. There is no instrument that separates those two states: check runs
are `total_count: 0` in every outcome (established above), and `get_reviews` is
`[]` in both. Budget the request, poll ~3 min, and on silence proceed on your
own verification -- which is what rule 10 already says, for a reason that turns
out to be sounder than its stated premise.

Also: quota did not replenish within ~63 minutes, so a retry-after-an-hour
strategy is not viable on the observed window.
