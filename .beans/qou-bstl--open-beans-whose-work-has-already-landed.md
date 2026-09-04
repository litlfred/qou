---
# qou-bstl
title: 'Open beans whose work has already landed — measured, and it cost this session three times'
status: todo
type: task
priority: high
created_at: 2026-09-04T08:40:00Z
updated_at: 2026-09-04T08:40:00Z
---

## The finding

A bean left at `status: todo` after its work has landed is not a bookkeeping
lapse. AGENTS.md §"Agent work-plan policy" makes the bean list the agent's
source of truth for "what next", so a stale high-priority `todo` sends the next
agent to re-derive something the corpus already holds.

**It is the corpus-grep failure one level up**, and it defeats the checklist by
construction: paths 1-6 come back clean *because the work is done*, and the only
thing that disagrees is the tracker the agent trusted enough not to grep.

## Measured, not asserted

Of the first three high-priority `todo` beans this session picked up:

  * `qou-e4eu` — already `completed` by a sibling at 02:12 the same day.
  * `qou-w2vy` — fixed by `d943f2acfac`, *"fix(qou-w2vy): port the COO object
    fallback to atom_character_raw"*, landed after the bean's own `updated_at`.
  * `qou-1ucq` — headline claim fixed four days earlier by `df719b5baf1` and
    `9b00d47036a`, neither absorbed.

Two of three were done; the third was two-thirds done. Each cost several steps
of re-derivation before `git log` stopped it.

Corpus-wide, `scripts/bean-completion-candidates.py` reports **82 open beans
(12 high-priority) whose ID appears in a later commit SUBJECT carrying a
completion verb.**

## The number NOT to quote

**784** open beans have *some* commit naming them after their `updated_at`.
That is an upper bound on staleness and nothing more — it catches progress,
mentions and scope-widening alike. Do not report it as a staleness count; the
script deliberately does not print it.

## The candidate list is ~40 % false positives, and both classes are structural

Measured on the 12 high-priority candidates, at least 5 are visibly not done
from the subject alone:

  * **Partial completion.** *"ITEM 4 CLOSED"* closes one item of a queue;
    *"named failures drained, but the cascade class recurred"* says outright the
    bean survives; *"item 3 fully closed; the remaining item is …"* names what
    is left.
  * **The verb governs a DIFFERENT bean.** *"qou-mfst is fixed on main — close
    it, and name the pattern it shares with qou-lkrd"* matches on `qou-lkrd`
    while the verb governs `qou-mfst`. The script flags a multi-id subject
    rather than guessing.

  * **The verb is QUOTED or NEGATED — the commit reports a REOPENING.** The
    worst class, because it inverts the meaning. `qou-hok7`'s later subject is
    *"resurgence(qou-hok7): deuteron-wall 'resummation closed' is a
    wrong-transform artifact"* — `closed` appears **in scare quotes**, inside a
    subject whose whole point is that the closure was an artifact, and that
    commit **reopened** the bean. A regex over a subject cannot see quotation
    marks.

So this is a READ QUEUE, not a close list. **Do not bulk-close from it.**

## Reading the BODIES raises the rate — measured on four

The ~40 % above is what is visible from subjects alone. Four high-priority
candidates were then opened and read:

| bean | verdict from its own body |
|---|---|
| `qou-hok7` | **open** — *"REOPENED. OPEN next step: q-Borel-Laplace resummation"* |
| `qou-54g5` | **open** — *"Bean stays open on (1)-(4)"* |
| `qou-qspc` | **open** — the later commit records a finding, not a closure |
| `qou-c1ln` | arguably done — *"the axis is finished as far as anything needs it"*; the rows still open are explicitly recorded as having **no downstream consumer** |

**Three of four survived the read.** n = 4 is small and I am not turning it into
a rate, but it points one way: expect most of the print-out to survive. The
tool's value is that it tells you which beans are worth OPENING — not which are
finished.

`qou-c1ln` is left for its owner to close. Its remaining rows are open-but-
consumerless, which is a scope judgement, and making that call on someone else's
bean is exactly the bulk-closing this bean warns against.

## Independently corroborated, months earlier, by another agent

`qou-c1ln`'s own body already reached this finding from the other direction:

> *"Third instance of the same staleness failure in two days … Both are
> summaries that went stale against work recorded elsewhere in the same corpus,
> and both were read as current by a later agent … the pattern is worth a
> systemic look — **a stale-summary check has no owner today**."*

That is this bean's thesis, written by a different agent before this session,
sitting inside one of the very beans the audit flagged. It went unowned until
now. `scripts/bean-completion-candidates.py` is the owner it asked for.

## The audit caught one of mine

`qou-vtau` — I did the work this session, merged it to `main`
(`3bd8b7689c3`, `711a163a8c1`), and left the bean `todo`. It was found by the
audit written in the same session to catch this in *other people's* beans.

That is the argument for the audit rather than for resolving to be more careful:
an agent that has just spent a session on backlog hygiene will still drop the
close. `qou-vtau` is now closed.

## 🛑 CORRECTION — the detector's precision is 2 in 12, not 6 in 10

**I published a false-positive rate of "~4 in 10". Having now read all twelve
high-priority candidates, it is 10 in 12.** That overstates the tool's precision
by roughly 3.5x and it is my error, made by estimating from commit subjects
instead of opening the beans.

| verdict | n | beans |
|---|---|---|
| **TRUE positive** — work landed, bean stale | **2** | `qou-vtau`, `qou-w2vy` |
| arguable | 1 | `qou-c1ln` (open rows have no consumer) |
| **FALSE positive** | **9** | `qou-rstq`, `qou-lkrd`, `qou-mln9`, `qou-f8lit`, `qou-j3w6`, `qou-hok7`, `qou-54g5`, `qou-qspc`, `qou-9iwt` |

Every one of the nine says it is open, in its own words: *"Closing it does not
close the sum rule"*; *"What blocks end-to-end verification now is not a proof
failure"*; *"REOPENED. OPEN next step"*; *"Bean stays open on (1)-(4)"*;
*"What remains of item 1: ..."*. `qou-9iwt` proposes **three** renames and the
commit did **one**.

### A FOURTH false-positive class: deliberately parked

`qou-mln9` reads *"**Left `todo` deliberately.** ... #5761 is a draft awaiting an
owner merge decision — until it lands, main stays validate-RED ... **Closing is
the author's call.**"* That bean is not stale; it is correctly parked, with the
reason stated. No commit-message heuristic can tell a parked bean from a
forgotten one, because the difference is intent and lives in the body.

### What survives, and what does not

**The phenomenon is real and is NOT weakened by this.** It rests on four
instances established by DIRECT inspection — `git log` on a named file, a
sibling's `completed` status, my own merge commits — not by this tool:
`qou-e4eu`, `qou-w2vy`, `qou-1ucq`, `qou-vtau`. Two of those four the tool found;
`qou-e4eu` it correctly excluded (already `completed`), and `qou-1ucq` I found by
hand.

**The detector does not do what I named it for.** It is not a staleness list. At
2-in-12 it is a "beans with related recent activity, worth opening" list — which
is still worth 12 reads if it prevents one re-derivation, and today it would have
prevented two. But that is a much smaller claim than the one this bean shipped
with, and the earlier wording is corrected rather than softened.

**A better detector cannot be built from commit messages.** All four
false-positive classes — partial completion, verb-governs-another-bean, quoted
or negated verb, deliberately parked — are semantic and live in the bean body or
in the author's intent. The check that works is an agent reading the bean, which
is what produced this table.

## Next

Done: all 12 read, see the correction above. Two were genuinely stale and
are closed (`qou-vtau` here; `qou-w2vy` needs its owner). Nothing further is
queued on this bean.


## A THIRD pathology — duplicates — and a detector for it that DOES NOT WORK

Reported as a measured negative. I built a second heuristic this session and it
failed in both directions; shipping it would have been worse than not having it.

### The pathology is real

`qou-3v8h` (2026-08-26, 158 lines) and `qou-eu0r` (2026-08-30, 70 lines) are
**the same defect filed twice, four days apart**: `authorNotes` silently dropped
on `prose` / `table` / `equation` / `diagram`. The later, thinner one does not
know what the earlier one records — that a fix **exists on a folio-assistant
branch** (`affcec4`, suite green) and has not landed on that repo's `main`. An
agent who picked `qou-eu0r` would reimplement a fix that exists, which commit
`8dfba1fa820` explicitly warns against.

`qou-3v8h` itself is **exemplary** and is correctly left open: *"NOT closing: the
defect is fixed on a branch, not in the product. Closing on 'someone has a fix
somewhere' is the failure mode this corpus keeps paying for."*

### The detector fails on precision AND recall

Title-token Jaccard over open beans, threshold 0.45:

  * **It MISSED the one pair I had found by reading.** `qou-3v8h` /
    `qou-eu0r` score **0.375** — below threshold — because one says
    *"authorNotes is silently dropped on ..."* and the other
    *"Schema silently drops authorNotes on ..."*. Same defect, different verbs.
  * **Nine of its top hits are TITLE TEMPLATES, not duplicates.** Seven
    `cj*` *"Conjecture carrier: X (X.lean) — §3b, famous-open"* beans differ
    only in the declaration (`QCollatz`, `ClassicalRiemannHypothesis`,
    `SingleVolumeIrrationality`, …); two more are *"Remark interpreting
    [madison2000]"* vs *"[gauthier2019]"*. Boilerplate dominates the token set.
  * **A 1.00 title match was still a FALSE POSITIVE.** `qou-r3vt` and
    `qou-ty08` have byte-identical titles — *"PROVE(lean):
    instance:archimedean_agreement"* — and are **different Lean files**:
    `.../protonExample/archimedean_agreement.lean` vs
    `.../HabiroResidueSumEquivalence/archimedean_agreement.lean`. The only
    distinguishing field is the path, which the title omits.

Of three pairs verified by reading: **one likely genuine** (`qou-ii3w`, a 9-line
stub, vs `qou-csdp`, 85 lines, same audit), **one borderline** (`qou-uea1` /
`qou-6n93` — the same PDF ingested twice under `…(1).pdf`, but targeting
different blocks and different sections), **one false positive**.

### Not shipped, deliberately

No `--dupes` mode was added. A detector with poor precision *and* poor recall is
worse than none: it would be quoted, and it would both mislead and reassure.
Recorded here so the next agent does not rebuild it.

**Same shape as the completion heuristic above, which is the durable lesson of
this bean:** what makes two beans the same, or one bean finished, lives in their
bodies and in their authors' intent. Neither is recoverable from titles or
commit subjects. The signal that *does* work — `--active` — works precisely
because it asks only WHEN.
