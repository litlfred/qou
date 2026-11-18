---
# qou-gwe9
title: 'MEASURED: Copilot review does not arrive — AGENTS.md rule 10''s last surviving Phase-4 gate'
status: in-progress
type: bug
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-23T00:39:14Z
updated_at: 2026-11-15T13:30:00Z
parent: qou-5vkl
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



---

## Data point 2026-08-30 (~10:08–10:40Z) — three PRs, and one is the direct NEGATIVE counterpart to row 2

Recorded because the entry above establishes *"a review on a push with NO
contemporaneous request"* (row 2, 10m28s) and reads as support for the
push-trigger hypothesis. This session ran the same configuration and got the
opposite result at more than twice the observation window.

| PR | head pushed | `request_copilot_review` | merged | reviews, last checked **10:54Z** |
|---|---|---|---|---|
| #6162 | 10:08:42Z | **~10:09Z** | 10:10:45Z | **none** — window ≥ 45 min |
| #6168 | 10:10:53Z | none | 10:12:34Z | **none** — window ≥ 43 min |
| #6174 | 10:35:45Z | none | 10:37:33Z | **none** — window ≥ 18 min (weak) |

> **Re-read 10:54Z by a second session** (`get_reviews` → `[]` on all three,
> plus `#6170` at ≥ 42 min). The bounds above were ≥ 37 / ≥ 35 / ≥ 10 at the
> 10:46Z read and ≥ 31 / ≥ 29 / ~5 at 10:40Z, and the prose below still carried
> the 10:40Z pair while this table carried the 10:46Z one — the same figure
> disagreeing with itself two paragraphs apart. **A censored bound grows until
> the event happens, so it is not a number, it is a number plus a read time.**
> Quote it with the timestamp or a later reader cannot tell a stale figure from
> a different measurement. Prose below aligned to this read.

All three `get_reviews` → `[]`, re-checked after each merge.

**#6168 is the discriminating row.** Push with NO request, ≥ 43 min observed
(re-read 10:54Z), no review. That is the same configuration as row 2 above and the opposite
outcome, at ~3.4x its 10m28s latency. So **a push does not reliably trigger a
review** — row 2 shows it *can* happen, this shows it does not always.

**#6162 is a clean negative for the request-trigger at ≥ 45 min** (re-read
10:54Z), which is ~11x the 3–4 min request→review latency the reopened audit
measured. Unlike the
audit's #6068 and this session's own earlier merges, the observation window
here is not the merge — I kept reading `get_reviews` for half an hour after.

### What this does NOT establish

- **Not "reviews stopped again".** The most economical reading is the **quota**
  the entry above found the hard way: that exhaustion was measured at 07:56Z,
  and 10:08Z is ~2h later with the recharge interval unknown. If the quota was
  still spent, all three rows are explained and neither trigger hypothesis is
  touched. **I did not receive the quota-limit message on any of them** — which
  is the same undetermined signature row 3 above hit, and is the reason this
  cannot be scored either way.
- **Not a latency measurement.** These are censored observations (no event), so
  they bound latency from below and cannot be averaged with row 2's 10m28s or
  the audit's 3–4 min.
- **#6174's window is still too weak to count.** At ≥ 18 min (re-read 10:54Z)
  it is only ~1.7x row 2's own 10m28s, so it barely discriminates. Included for
  completeness.

### The one operational thing that IS true under every candidate

I requested on #6162 and merged **2 min 3 s later** — the exact error the audit
records against its own #6068. It happened not to cost anything (nothing
arrived in the following half hour), but the window was not mine to gamble.
The rule that follows is the audit's, unchanged: **do not wait, but keep
reading after the merge**, because the merge is not the end of the window.


### Observation CLOSED 2026-08-30 11:33Z — final bounds, nothing arrived

Final sweep of all four merged PRs. `get_reviews` → `[]` on every one.

| PR | pushed | requested | final censored window |
|---|---|---|---|
| #6162 | 10:08:42Z | **~10:09Z** | **≥ 84 min** |
| #6168 | 10:10:53Z | none | **≥ 81 min** |
| #6174 | 10:35:45Z | none | ≥ 57 min |
| #6179 | 10:47:00Z | none | ≥ 45 min |

Superseding the ≥37/≥35 recorded above: these are the same observations carried
to their end, not new ones.

**What the two strong rows now bound.**

- **#6162 — request trigger, ≥ 84 min.** That is ~21× the 3–4 min
  request→review latency the reopened audit measured. A request-triggered review
  did not arrive within twenty-one times its own observed latency.
- **#6168 — push trigger, ≥ 81 min.** ~7.8× the 10m28s push→review latency of
  the data point in `f96325ec1`. A push-triggered review did not arrive within
  nearly eight times its own observed latency.

**Still NOT scored, and this is the point.** The quota exhausted at 07:56Z with
an unknown recharge interval remains the one live explanation that fits all four
rows without touching either trigger hypothesis, and **no quota-limit message
was posted on any of them** — the same undetermined signature row 3 hit. Four
negatives at long windows are consistent with "quota still spent for the whole
session" and say nothing on their own about what triggers a review.

**What would settle it, for whoever picks this up:** a request on a fresh PR
after a known-long quiet period, with the quota-limit message watched for
explicitly. Until then the three candidates in
`docs/audits/2026-08-30-copilot-review-works-again.md` stand unresolved and this
bean stays open.

Observation closed; no further check-in scheduled. Past ~80 min further waiting
adds nothing — a fifth zero at 120 min would not discriminate either.

## Third datum: quota had NOT refilled at 5 hours (2026-08-30, 13:03Z)

Requested on #6167 at **12:56Z** — exactly **5h 00m** after the 07:56Z refusal on
#6131. `get_reviews` at 13:03Z (7 min later, against a ~3 min observed latency for
a real review on #6088): **`[]`**.

| request | elapsed since 07:56Z exhaustion | outcome |
|---|---|---|
| 07:55Z (#6131) | — | refusal posted, ~40 s |
| 08:58Z (#6131) | 1h 02m | silence |
| 12:56Z (#6167) | **5h 00m** | **silence** |

So the retry-after-an-hour strategy already ruled out is now ruled out at five
hours too. Either the window is longer than 5h, or it is not a simple time-based
refill (per-user-per-day is consistent with all three rows).

**Practical consequence, unchanged in direction but firmer:** budget Copilot as a
resource you get roughly *once*, not as a step in every prepare-merge. Spending it
on the first substantive PR of a session and not re-requesting is the strategy the
data supports. `prepare-merge-auto` Phase 1b's per-run request is exactly the
behaviour that drained it here.


---

## 2026-08-30 13:37Z — four more censored negatives, and what they do NOT bound

Read by hand at **13:37Z**, `get_reviews` → `[]` on all four. Windows run from
PR creation (itself a push), so a push-triggered review had the whole interval:

| PR | repo | created | merged | window @ 13:37Z |
|---|---|---|---|---|
| [`fa#156`](https://github.com/litlfred/folio-assistant/pull/156) | folio-assistant | 10:43:27Z | 11:04:14Z | **≥ 2 h 54 m** |
| [`#6189`](https://github.com/litlfred/qou/pull/6189) | qou | 10:57:06Z | 11:00:52Z | **≥ 2 h 40 m** |
| [`#6204`](https://github.com/litlfred/qou/pull/6204) | qou | 12:17:14Z | 12:31:54Z | **≥ 1 h 20 m** |
| [`#6208`](https://github.com/litlfred/qou/pull/6208) | qou | 12:44:23Z | 12:53:11Z | **≥ 53 m** |

`#6204` and `#6208` were each force-pushed again (rebase) shortly before merge,
which only *adds* trigger opportunities inside the window — it does not shorten
it. Two repositories, so this is not a qou-specific setting.

**These are push-trigger evidence, NOT quota evidence.** No
`request_copilot_review` was fired on any of the four. That matters for how they
may be used:

- **Against the push trigger** they are the strongest rows in this bean. The
  entry that opened the push-trigger hypothesis measured a review arriving
  **10m28s** after an unrequested push; `fa#156` and `#6189` are the same
  configuration at **~15×** that latency, in two different repos, with nothing.
  Together with `#6168` (≥ 43 min) that is four independent censored negatives
  against a trigger whose one positive observation is a single 10m28s event.
- **They say nothing about the quota**, because an un-requested PR would draw no
  review under *either* the quota-exhausted or the request-required reading.
  Do not cite them as evidence the ration is still spent.

**The recharge interval is barely bounded, and by less than the elapsed time
suggests.** The only request fired since exhaustion at **07:56:40Z** is the
sibling's on `#6162` at ~10:09Z, which returned nothing at ≥ 45 min. So the
honest statement is **recharge > ~2 h 13 m**, from that one request — *not*
"> 5 h 40 m" from the wall clock, which would be reading four unrequested PRs
as if they had asked.

**The passive-measurement instruction stands and is now sharper.** The next
successful review after 07:56:40Z bounds the recharge from above — but only a
**requested** one bounds it usefully, and nobody should fire a request to find
out, which is the error that created the shortage. The cheap discriminator is
already scheduled by ordinary work: the next session that requests a review on
its first substantive PR will produce the datapoint for free.

Recorded because the alternative was leaving it in a chat transcript, which is
this corpus's documented way of losing a measurement — and because this bean
already tells future agents to write exactly this observation down.

### 2026-08-30 12:26Z — a FIFTH zero, and this one is the discriminating shape you asked for

The closure above says *"what would settle it is a request on a fresh PR after a
known-long quiet period, watching explicitly for the quota message"*, and stops
because a fifth zero at 120 min would not discriminate. This row is not just a
fifth zero — it has the shape the closure names.

| PR | pushed | requested | checked | window | quota message |
|---|---|---|---|---|---|
| **#6180** | 10:42Z (opened) | **11:25Z** | 12:26Z | **≥ 61 min** | **none** |

Two properties the four closed rows do not have:

1. **The request came ~3.5 h after the 07:56Z presumed exhaustion**, and ~76 min
   after the last request in the table (#6162 at ~10:09Z). If the quota recharge
   interval is anything under ~3 h, this request was made with quota available —
   and still produced nothing at 61 min.
2. **`request_copilot_review` returned no output at all** — no quota-limit
   message, no error. The same undetermined signature row 3 hit, now at a much
   later wall-clock time.

**Reading, scoped.** This weakens "quota exhausted at 07:56Z with a short
recharge" as a complete explanation, because a request 3.5 h later behaves
identically. It does **not** establish the trigger hypothesis either: an
exhaustion with a recharge longer than ~3.5 h, a day-scoped quota, or a
non-quota mechanism all fit this row equally. **Still not scored**, consistent
with the closure's discipline.

**What would now discriminate**, sharpened by this row: a request on a fresh PR
after a **multi-hour** quiet window spanning a UTC day boundary. If a day-scoped
quota is the mechanism, that is the only window where a review can appear.

Recorded, not acted on. I am not re-requesting on #6180 — AGENTS.md's own
corrected row says reviews are rationed and not to re-request after every push,
and the closure above is right that another same-day zero buys nothing.

## THE REQUESTED DATAPOINT, 2026-08-30 14:45Z — recharge > 5 h 40 m, with one honesty caveat

This bean's own closing instruction — *"the next session that requests a review
on its first substantive PR will produce the datapoint for free"* — is now
discharged. It did, and here it is.

| | |
|---|---|
| PR | [`qou#6157`](https://github.com/litlfred/qou/pull/6157) |
| request fired | **2026-08-30 13:36:43Z**, via `request_copilot_review` |
| PR content | 1 Lean file (3 sorry-free defect fixes), 1 new probe + witness, 3 bean bodies — substantive, not a beans-only change |
| merged | 14:25Z (rebase-merge, `85959c78c0`) |
| `get_reviews` at 13:45Z | `[]` |
| `get_reviews` at **14:45Z** | **`[]`** |
| elapsed since request | **≥ 1 h 09 m** |
| elapsed since exhaustion (07:56:40Z) | **5 h 40 m** |

**So the recharge lower bound moves from `> ~2 h 13 m` to `> 5 h 40 m`**, and
unlike the four rows above this one **is** a requested PR, so it bears on the
quota reading rather than only on the push trigger.

### 🛑 The caveat, and it is load-bearing

**I did not record the `request_copilot_review` response body verbatim.** The
call returned without raising and I read that as "not quota-blocked" — but that
was an *inference*, and this bean's earlier entries note that quota refusals
arrive as a message (*"the user who requested the review has reached their quota
limit"*) rather than as an error. So I cannot rule out that the request was
refused in its payload and I did not look.

What is solid either way: **no review existed at ≥ 1 h 09 m after a request
attempt on a substantive PR.** The two readings — request accepted and unserved,
or request refused on quota — differ on *why*, not on the observation. Only the
first tightens the recharge bound; the second would instead be direct evidence
the ration was still spent at 13:36Z, which is also useful and also new.

**Instruction for the next agent, because this is a cheap fix:** when you fire
`request_copilot_review`, **paste its response body into this bean**. It costs
one line and it is the difference between a datapoint that discriminates and one
that does not. I lost that distinction here for no reason.

### A second, weaker row now accruing

[`qou#6254`](https://github.com/litlfred/qou/pull/6254) was created 14:34Z and
has taken three pushes since, **with no review requested**. That is the same
censored-negative configuration as `fa#156` / `#6189` above and will bear on the
push trigger once the window is long enough to matter — at ~16 min it is not yet
worth anything. Noted so it is checked rather than re-derived.


## FOLLOWING MY OWN INSTRUCTION, 14:50Z — the response body, verbatim

Fired `request_copilot_review` on
[`qou#6254`](https://github.com/litlfred/qou/pull/6254) at **2026-08-30 ~14:50Z**.
Response body, verbatim and complete:

```
(mcp__github__request_copilot_review completed with no output)
```

**Empty. Not a quota message.** That is the discriminator this bean has been
missing, and it is cheap: per the entries above, a quota refusal arrives as
*text* (*"the user who requested the review has reached their quota limit"*),
while an accepted request returns **nothing at all**. So the response body does
distinguish the two readings, and recording it costs one line.

### What this does and does not do to the 13:36Z row

**It does not upgrade it.** Same tool, same session, same account, so the 13:36Z
request very likely also returned empty — but that is an inference about an
observation I did not make, and this bean has been burned by exactly that class
of reasoning. The `qou#6157` row above stays as written: *no review at ≥ 1 h
09 m after a request attempt*, cause undetermined between "accepted and unserved"
and "refused on quota".

**It does set up a clean one.** `#6254`'s request is now *known accepted* at
14:50Z, which is **6 h 53 m** after exhaustion at 07:56:40Z. If no review
arrives, the recharge lower bound becomes `> 6 h 53 m` on an **unambiguous**
request — strictly better evidence than the `#6157` row, which cannot separate
the two causes. If one does arrive, it bounds the recharge from **above** for
the first time, which is the measurement this bean has never had.

Either outcome is worth having, and neither costs another request. Check-in
armed; result to be appended here.

### Standing note for the tool, not just this bean

`request_copilot_review` returning empty-on-success and text-on-refusal means
**every** call site that fires it should record the body. An agent that reports
"requested a review" without it has produced an observation that cannot be used
for anything.


## 2026-08-31 02:46Z — THE DAY-BOUNDARY ROW. This is the discriminator the 12:26Z entry asked for, and it comes back zero

The 12:26Z entry above closes by naming what would discriminate:

> a request on a fresh PR after a **multi-hour** quiet window spanning a UTC day
> boundary. If a day-scoped quota is the mechanism, that is the only window
> where a review can appear.

That window has now been observed.

| | |
|---|---|
| PR | [`qou#6254`](https://github.com/litlfred/qou/pull/6254) |
| request fired | **2026-08-30 ~14:50Z** |
| response body | **empty** — recorded verbatim (see the entry above), no quota message |
| `get_reviews` at **2026-08-31 02:46Z** | **`[]`** |
| elapsed | **≥ 11 h 56 m** |
| elapsed since presumed exhaustion (08-30 07:56:40Z) | **18 h 49 m** |
| spans 00:00Z day boundary | **yes** — 9 h 10 m before it, 2 h 46 m after |

**Two things this settles, and one it does not.**

**1. It is absence, not latency.** AGENTS.md's corrected row records the two
measured *positive* latencies: `qou#6122` at **~3 min** and
`folio-assistant#153` at **~4 min**. Eleven hours fifty-six is ~**200×** that.
Nothing about this row is consistent with a review that is merely slow.

**2. Day-scoped quota is now the *worst*-supported of the three candidates.**
Under the working inference that an empty response body means accepted (a
refusal returns text — established one entry above), the request was live and
unserved when 00:00Z passed. A day-scoped ration that reset at the boundary had
**2 h 46 m** to serve it and did not.

**3. What it does NOT settle**, and the assumption is worth naming: I do not
know that an accepted request *persists* across a day boundary. If acceptance
merely acknowledges receipt and the work is dropped when unserved, the boundary
is irrelevant and this row reduces to a very long censored negative. That
alternative is not excluded by anything measured here. So the honest form is:
**either day-scoped quota is refuted, or acceptance does not imply enqueueing** —
and the second is itself a finding, because it would mean the empty response
body carries less information than the entry above credits it with.

Both readings agree the recharge bound is now **> 18 h 49 m** from the presumed
exhaustion, which supersedes the `> 5 h 40 m` two entries up and the `> ~2 h 13 m`
before that.

**Not re-requesting**, per the standing discipline in this bean. The next free
datapoint is whatever a fresh session's first PR produces; nothing here needs to
be bought.

### Request row 2026-08-31 ~04:52Z — qou#6369, accepted-empty

`request_copilot_review` on **litlfred/qou#6369** (q-RH trace-identity tranche,
branch `claude/q-riemann-hypothesis-gaps-zgxd8m`), fired ~04:52Z. Response body
**empty** — the known-accepted shape, not the quota-refusal string.

Recording the timestamp only so the latency is measurable if a review lands.
**Not re-requested**, and it should not be: a sibling session's check-in on
#6254 records `>= 11h56m with no review` from a 2026-08-30 14:50Z accepted
request spanning the UTC day boundary, and reaches the conclusion that firing
requests is what creates the shortage.

Noting for honesty that this request was fired **before** I had read that
sibling's finding. AGENTS.md's live text says reviews do arrive subject to
quota and forbids only re-requesting after every push, so the single request
was within the documented guidance — but the sibling's measurement is newer
than that text, and on its evidence the right default is now **do not request
at all** unless the bean's own guidance changes.

---

## Data point 2026-08-31 ~19:47 UTC — TWO zeros, with a confound I am naming

Requested `request_copilot_review` on **qou#6404** and **qou#6405** at ~19:37-19:38
UTC. Both calls returned with **no output and no quota error** — so neither was
refused for quota, unlike the five-in-30-minutes run of 2026-08-30. Checked
`pull_request_read get_reviews` on both at ~19:43 and again at ~19:47:
**`[]` on both, four checks total.** That is ~10 minutes, well past the 3-4 min
arrival measured on qou#6122 and folio-assistant#153.

**The confound, stated because it may be the whole answer.** I pushed twice to
#6405 after requesting (`be3797f5e5`, `133346a904`). If a review request is
bound to the head SHA it was made against, those pushes could have superseded it
— which would make #6405's zero uninformative. **#6404 has no such confound**:
one commit, `c031248eb9`, unchanged since 19:24, requested at 19:38, zero at
19:47. So the clean observation is n=1, not n=2.

**What this does and does not support.** It is consistent with the historical
zero pattern and inconsistent with the 2026-08-30 correction, but one clean
observation does not overturn that correction, which rested on four arrivals
including two that landed minutes after a merge. Both facts can hold if arrival
is intermittent rather than binary — which is what "mechanism UNSETTLED" already
says.

**Not recorded in `merge-coordinator/MEMORY.md`**, deliberately: a single
observation is not enough to rewrite a TRAP that was corrected yesterday on
stronger evidence, and flipping that row back and forth is worse than leaving it
at "rationed, arrival intermittent, `get_check_runs` does not discriminate".

**What would settle it:** request on a PR and then *do not push*, checking at
5 / 15 / 60 min. Every observation so far, including mine, has confounded the
request with subsequent activity.


---

## 2026-08-31 — TRIAL 2 on qou#6407: the first UNCONTAMINATED observation

Every prior observation on this question (n=5 zeros 2026-08-23, four arrivals
2026-08-30, my two at 19:37) allowed a push between request and read and none
recorded whether one happened. This one did not.

**Protocol run as specified.** Requested once at **21:01:08Z**, after all pushes
to `claude/deuteron-trefoil-writhe-interface-2026-08-31` were finished. No push
since. **Verified rather than remembered:** head at read time was
`b572920a3a9f87f580b53b9a3d650508898c6cc5`, identical to the head at request,
and `updated_at` = 20:59:34Z, *before* the request.

    21:30:49Z   T+29m41s   get_reviews = []   head UNCHANGED

**This is a clean negative at ~30 min** — the first observation on this question
that measures what it claims to. It does **not** settle it: one clean trial
against four recorded arrivals is not a verdict, and 30 min is not 60. But it is
the first data point that is not confounded.

**Trial 1 (qou#6406) — TRUNCATED, still not a negative.** Requested 20:25:30Z,
`[]` at T+5m39s on a verified-clean head, then **merged by litlfred at
T+7m03s** — not by me. Post-merge read at 21:30:49Z (~58 min after the merge,
~65 min after the request): still `[]`. Worth having, because this corpus
records reviews arriving *after* a merge (qou#6104/#6116), but the run was cut
short at 7 minutes and must not be quoted as a 60-minute zero.

**A third protocol condition, learned from trial 1:** *do not merge the subject
PR either.* The protocol in `copilot-review-arrival.md` says request-once and
do-not-push; trial 1 died on a third way to end a run that the protocol did not
name. Add it when that file is next touched (it is on `main` as of #6406, so it
needs its own branch — do not reopen #6406).

**Still NOT changing the `merge-coordinator/MEMORY.md` TRAP row.** One clean
30-minute zero plus one truncated run does not overturn a row corrected on
2026-08-30 from four arrivals. The stable wording holds: rationed, intermittent,
`get_check_runs` = 0 does not discriminate.


### Trial 2 COMPLETE — clean negative at T+6h21m

Final reading **2026-09-01T03:22:41Z**, elapsed **6h 21m 33s** from the
21:01:08Z request. Head still `b572920a3a9f87f580b53b9a3d650508898c6cc5`,
`updated_at` still 20:59:34Z (pre-request). `get_reviews = []`.

    21:30:49Z   T+29m41s   []   head verified unchanged
    03:22:41Z   T+6h21m    []   head verified unchanged   <- trial complete

**So trial 2 is the first end-to-end uncontaminated run this question has had,
and it is a NEGATIVE at six hours** — two orders of magnitude past the 3-4 min
arrival measured on 2026-08-30, and past the 60 min the protocol asked for.

**What it licenses:** the protocol works and has now been run once, cleanly,
start to finish. A silent request that produces no review is real and is not
explained by a subsequent push — which was the live alternative hypothesis and
is now ruled out for at least this instance.

**What it does NOT license.** One clean negative against four recorded arrivals
(`qou#6122`, `fa#153`, `qou#6104`, `qou#6116`, all ~3-4 min, all with
substantive findings) is not a verdict — it is consistent with arrival being
**intermittent**, which is what the TRAP row already says. **The
`merge-coordinator/MEMORY.md` row stays as it is.** It was corrected on
2026-08-30 from stronger evidence than this, and flipping it back on n=1 would
repeat the original error with the sign reversed.

**Next, if anyone wants to settle it:** a second clean trial. The protocol now
has all three conditions — request once, do not push, **do not merge** (trial 1
died on the merge). Two clean negatives against four arrivals would start to
look like a rate; one does not.

**Trial 1 (`qou#6406`) final state:** still `[]` at 03:22:41Z, ~6h50m after its
merge. Remains labelled TRUNCATED and must never be quoted as a timed negative.


---

## 🛑 2026-09-01 — A REVIEW ARRIVED, AND I NEVER REQUESTED IT

`qou#6411`, review `5074008688` by `copilot-pull-request-reviewer[bot]`,
submitted **2026-09-01T04:26:48Z** on commit `128d7e486c`, state `COMMENTED`,
"🟡 Changes recommended", 2 comments, effort level "Lite".

**I did not call `request_copilot_review` on #6411.** Not once. The review
arrived unprompted, minutes after the branch was pushed.

**This changes the shape of the question.** Every trial recorded above assumed
arrival requires a request and measured the request→arrival interval. If
reviews also fire on push, then:

- the trial-2 negative (`[]` at T+6h21m on `qou#6407`) is **still a clean
  negative**, but it is a negative about *that PR*, not about the mechanism —
  #6407 got neither a requested nor an unrequested review;
- the "quota" reading is weakened: a request that returns silently may simply
  be redundant with an automatic trigger that did or did not fire for other
  reasons;
- **the protocol in `copilot-review-arrival.md` is measuring the wrong
  variable.** It controls for pushes after the request. It does not control
  for the push that *creates* the PR, which may be the actual trigger.

**Do NOT conclude "reviews are automatic".** One unrequested arrival against
one clean unrequested-and-unarrived case (#6407) is n=1 each way. What is now
established is narrower and more useful: **arrival is not gated on an explicit
request**, so any future trial must record whether a request was made *and*
treat the PR-creating push as a candidate trigger.

**The findings were real**, which matters for the merge-gate question
separately from the timing one: three findings, all correct, all mine — two
overclaims ("four decades" for a x1024 sweep = 3.0 decades; "constant to 6
digits" for 4 sig figs / 7.14e-5 relative) and an unused `tr`/`dt` pair. Fixed
in `4dafadc2b9`. So when a review does arrive here it is worth having, and the
"merge without waiting" posture has a real cost.

**Still NOT flipping the `merge-coordinator/MEMORY.md` TRAP row.** Its current
wording — rationed, intermittent, `get_check_runs` = 0 does not discriminate —
survives this observation unchanged. What needs updating is
`copilot-review-arrival.md`'s protocol, which controls for the wrong thing.


---

## 2026-09-03 — one more arrival, and a PROTOCOL TRAP the staleness test walks into

Adding a data point rather than a finding: the 2026-09-01 entry above already
records that a review can arrive and that its findings can be real. This
corroborates it and sharpens one mechanic.

**#6441** — two `.beans/*.md` files, 138-line diff, nothing else. Copilot
requested at ~04:17Z via `request_copilot_review`; review **submitted 04:19Z**,
about **two minutes** later. `state: COMMENTED`, *"🟢 Approval recommended"*,
**0 comments generated**, review effort *"Lite"*. So the arrival is not merely
possible, it can be fast — and on the smallest possible diff.

### The trap: a pure rebase makes a current review look stale

`prepare-merge-auto` Phase 1b step 2 says a review whose `commit_id` is an
earlier commit **is stale and does not count**, and to re-request. That rule is
right for a review predating new *work* — and **wrong after a pure rebase**,
which is the repo's standard pre-merge step (rule 8).

Here the review carried `commit_id = 0dfd0f8b6b9`, my **pre-rebase** head; the
merge candidate was `cae9f0fa3ac`. The commit_id test says stale. But the
rebase changed only the parent:

    git diff <old-base>...<old-head>   ->  138 lines, 2 files
    git diff origin/main...HEAD        ->  138 lines, 2 files   BYTE-IDENTICAL

Copilot had reviewed exactly the change being merged. Discarding it and
re-requesting would have thrown away a valid review to wait on a replacement —
in a protocol whose whole problem is waiting.

**The right test is the diff against its own base, not the commit_id.** A sha
comparison cannot distinguish "rebased onto newer main" from "new commits
pushed", and those are opposite situations. I nearly got this wrong twice: first
by trusting the commit_id, then by comparing the two commits' **whole trees**,
which showed 15 files changed and "genuinely stale" — that was main's 17
intervening commits, not my change.

### What this does NOT establish

Nothing about the arrival *rate*. n is now small but nonzero on the arrival
side, and this case is the most favourable possible input — a two-file markdown
diff, reviewed "Lite". It says nothing about whether a large Lean or witness
diff gets reviewed, which is the case that would actually matter at a merge
gate. Do not read "Copilot reviewed my beans PR in two minutes" as "Copilot
reviews."


## 2026-09-13 — one more zero-review observation, and it SHARPENS rather than settles

**PR #7255** (litlfred/qou, new Lean file + a notation-register section).

- `request_copilot_review` called **once**, ~05:41Z. No error returned.
- Re-checked **06:40Z, 59 minutes later**:
  - `get_reviews` -> `[]`
  - `get_review_comments` -> `{"review_threads": [], "totalCount": 0}`
  - `get_check_runs` -> `{"total_count": 0, "check_runs": []}`

**Do NOT read this as support for the original "never arrives" claim.** That
claim is falsified and stays falsified — `qou-80ul` (#6112, 5 comments) and
`qou-g7t2` (#6121) are counterexamples, and AGENTS.md's 2026-08-30 correction
records first-hand arrivals at ~3 min and ~4 min.

**What it does sharpen is the QUOTA hypothesis.** AGENTS.md attributes the zeros
to rationing, on evidence of *five requests across two repos in ~30 minutes*
returning "reached their quota limit". This observation is a different shape:
**one** request, no error, and an hour of silence. So either

  (a) the quota is shared or persistent well beyond a 30-minute window, so a
      single request can land in an already-exhausted bucket with no error and
      no review, or
  (b) something other than quota produces the zeros.

The single-request case does not distinguish them, and that is the point: the
quota story was built on a burst, and a burst cannot tell you what a lone
request does. The discriminator would be a *first* request in a repo that has
been quiet for a day.

**Two honest limits on this datum.** 59 minutes is not forever — the review may
yet land, and if it does this entry should be amended rather than left standing.
And `get_check_runs` returning 0 is uninformative here by AGENTS.md's own note
(a 0 does not mean no review is coming), so it is recorded for completeness, not
as evidence.

**Practical consequence, unchanged:** do not block a merge on a Copilot review,
and do not re-request on every wake. One request per PR, then proceed on the
agent-owned verification gate.


## Fresh data point, 2026-09-14 — two explicit requests, zero reviews, on a repo where reviews DID work on 2026-08-30

This bean was reopened because `qou#6122` (~3 min) and `folio-assistant#153` (~4 min) showed
reviews arriving. Today's measurement is the other outcome, on the same repo, and it is a
clean controlled pair rather than a background scan.

| PR | requested | observed | elapsed | reviews |
|---|---|---|---|---|
| `qou#7360` | 2026-09-14 ~08:40Z | 08:54Z, 09:29Z, 10:27Z | **1 h 47 m** | **0** |
| `qou#7360` (2nd) | 2026-09-14 10:27Z | 11:28Z | **1 h 01 m** | **0** |

Siblings `#7357` and `#7359`, never requested, also show **0** — so the zero is not specific
to the requested PR.

**What this does and does not discriminate.** AGENTS.md records the mechanism as UNSETTLED
with three candidates. This pair rules out one framing only: *"it works now, the 2026-08
zeros were historical."* It does not separate quota-refusal-at-request-time from
per-repo/per-account gating, because `request_copilot_review` returns **no output on
success or refusal alike** — there is no observable difference between "queued" and
"refused" at the call site.

**The signal AGENTS.md warns about held.** `get_check_runs` reports `total_count: 0`
throughout, exactly as it does when a review *is* coming, so it discriminated nothing here
either. Do not read it as "no review is coming" — and do not read it as the opposite.

**The 3-4 minute figure is the useful operational rule.** On the two 2026-08-30 successes a
review landed in 3-4 min. Here, nothing at 14 min, 49 min, 1 h 47 m, or 1 h 01 m. So
**a review that has not arrived within ~10 minutes is not coming**, and further waiting or
re-requesting is spend with no return. Two requests is the cap I applied; a third would have
been superstition.

**Consequence for rule 10 Phase-4, stated plainly:** on `qou#7357`/`#7359`/`#7360` there is
**no external review gate at all** — CI is dispatch-only, Gemini is sunset, Copilot did not
respond to two requests. The agent's own verification tabled in each PR body is not the last
gate standing, it is the only one, which is what AGENTS.md's corrected text already says.

## Claim reset 2026-11-15

Was in-progress with no bean update since October 2026. Reset to todo by the owner-approved bean triage (same rule as the 2026-10-04 reset). Nothing in the work was judged. Re-claim it if you pick it up.
