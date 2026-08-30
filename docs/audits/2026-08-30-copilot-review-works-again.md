# Copilot review works again — and the rule citing its absence was self-sealing

**Date:** 2026-08-30 · **Bean:** `qou-gwe9` (reopened)
**Corrects:** [`AGENTS.md` §"Branch + PR workflow" rule 10](../../AGENTS.md), the Phase-4 gate table

---

## The finding

**GitHub Copilot is reviewing pull requests again, in both repos.** Measured
first-hand today:

| PR | requested | review submitted | latency |
|---|---|---|---|
| `litlfred/qou#6122` | 2026-08-30 07:24Z | 2026-08-30 **07:27:39Z** | ~3 min |
| `litlfred/folio-assistant#153` | 2026-08-30 07:48Z | 2026-08-30 **07:51:52Z** | ~4 min |

Both from `copilot-pull-request-reviewer[bot]` (app id 175728472), both
`COMMENTED` with substantive line-level findings — three on #6122, three on
#153. **Five of the six were real defects**, and four of those were mine.

The second row matters as much as the first: `folio-assistant` is a *different
repository*, so this is not a qou-specific setting.

## 🛑 There is a QUOTA, and I exhausted it in thirty minutes

Added after the fact, because it changes the shape of this finding.

The **third** review request on #6122 returned, from the same bot at
2026-08-30 07:56:06Z:

> *"Copilot was unable to review this pull request because the user who
> requested the review has reached their **quota limit**."*

So Copilot review here is a **rationed** resource, not a binary
available/unavailable one. Five requests across two repos in roughly thirty
minutes — three of which I fired while chasing this very measurement —
exhausted it. That is my own error and it is worth naming: re-requesting a
review after every push is expensive in a way nothing in the repo's docs says.

**What this does and does not establish.** It confirms a quota exists and that
we hit it. It is a *candidate* explanation for the historical zeros, **not an
established one**, and the reason is a signature mismatch: today's exhaustion
**announces itself** as a posted review, whereas `qou-gwe9` recorded
`get_check_runs` returning `total_count: 0` with nothing enqueued and no
message of any kind. Either the older exhaustion was silent and the message is
new, or the two are different failure modes. I cannot tell from here, and the
distinction matters — "we were over quota all along" and "it was off and came
back" imply different operating rules.

**What is safe to act on:** treat Copilot review as a scarce resource. Request
it *once* per PR, at the point the branch is actually ready, and wait the ~3–4
minutes — rather than after every push, which is what burned the quota here.

## The prior measurement was sound and has expired

This is not a case of a bad measurement being repeated. `qou-gwe9` was careful:
it recorded **n=2 controlled cases**, explicitly labelled its five background
PRs weak evidence that "may simply never have requested it", and stated in
terms — *"DOES NOT: prove Copilot is disabled at the org/repo level."* A later
session strengthened it to five explicit requests plus the mechanism
observation (`get_check_runs` returning `total_count: 0`, i.e. nothing
*enqueued*, which is the difference between slow and absent), a sixth request
on #5532, and ~12 merged PRs across #5415–#5880 carrying no reviews of any
kind.

**And it was not merely slow.** `#5495`, the bean's own controlled case,
requested 2026-08-22, still shows **zero reviews eight days later**. Nothing
arrived late; the behaviour genuinely changed somewhere between 2026-08-27 and
2026-08-30.

So the bean was right for its window. What went wrong is what happened to it
afterwards.

## The actual defect: a time-bounded measurement became a standing instruction

AGENTS.md rule 10 does not merely record the observation. It instructs:

> `prepare-merge-auto` Phase 1b still prescribes a 15-minute poll for a check
> run that is never created; **that wait can only expire, so skip it** and
> record why (citing `qou-gwe9`) rather than burning the window.

**That instruction prevents the observation that would falsify it.** An agent
that never waits for a Copilot review never sees one arrive. The claim
therefore cannot be disconfirmed by any agent following the rule — it is
self-sealing.

Measured consequence, in this session alone: I merged **#6068** at 06:59Z
having requested a Copilot review at ~06:57Z, roughly two minutes earlier,
because the rule told me not to wait. #6068 shows zero reviews — not because
none was coming, but because I merged inside the latency window. Its review, if
it came, had nowhere to land. Every finding Copilot later made on #6122 applied
to code that also shipped in #6068.

## Why this generalises

AGENTS.md is full of correctly-scoped measurements that later became standing
facts — the document says so about itself repeatedly (the `4.6e6` slope, the
`~840` muon witnesses, the "five other sites", the 39 %/73 %/58 % witness
figures). This is the same class with an extra turn of the screw: **the stale
fact is not merely quoted, it is wired into an instruction that suppresses
re-measurement.**

The distinguishing question for any such rule: *if this claim became false,
what would notice?* Where the answer is "nothing, because the rule tells agents
not to look", the claim needs an expiry or a cheap periodic probe, not just a
citation.

## Disposition

Recorded here; `AGENTS.md` rule 10 and `prepare-merge-auto` Phase 1b both need
the Copilot row rewritten from "does not arrive" to "arrives in ~3–4 minutes;
wait for it". That edit is **not** made in this audit — it belongs in a change
that also revisits the 15-minute poll duration, and this file is the
measurement that justifies it.

What is safe to act on immediately, and what this session now does: **request a
Copilot review ONCE, when the branch is ready, and give it a few minutes before
merging.** The cost of waiting four minutes is four minutes; the cost of not
waiting is #6068; and the cost of requesting after every push is the quota,
which I spent proving the point.

## A footnote on trusting the reviewer

Of the six findings Copilot produced today, **five were real and one was
false**. The false one claimed the refutation proofs in
`2026-08-30-qns-carriers-are-refutable.lean` "leave goals unsolved" because
`norm_num at h` does not close `False`. It does, when `h` reduces to `False`,
and the file was verified before and after: `lean`-direct **exit 0, 0 errors, 0
`sorry`**, with `#print axioms` on the two named proofs showing only `propext`,
`Classical.choice`, `Quot.sound` — no `sorryAx`.

Recorded because the correct handling was *not* to apply the suggested fix. A
review bot's finding is a bug report to verify, and the verification here was
cheap and decisive. Rewriting two working proofs to satisfy a speculative
comment would have been the same failure as widening a baseline to make a gate
green.
