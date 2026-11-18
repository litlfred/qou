---
# qou-bstl
title: Open beans whose work has already landed — measured, and it cost this session three times
status: in-progress
type: task
priority: high
tags:
    - reorg-2026-10-04
created_at: 2026-09-04T08:40:00Z
updated_at: 2026-10-04T15:14:59Z
parent: qou-5vkl
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


## Worked 2026-09-05 — the queue read, plus a NEW class this bean does not carry

### The tool's own precision line is now the authority, and it is worse than this bean's tentative note

The body above says *"Three of four survived the read ... n = 4 is small and I am not
turning it into a rate."* The script now prints, from a full read of all twelve
high-priority bodies: **MEASURED PRECISION 2 IN 12** — only `qou-vtau` and `qou-w2vy`
were genuinely stale. Quote the 2/12, not the 3-of-4.

### Independently reproduced on the SEVEN candidates that postdate that read

The high-priority list has grown past the twelve; these were unread. Bodies opened:

| bean | verdict from its own body |
|---|---|
| `qou-56qy` | **open** — a numbered "What is still open" list of 4 items |
| `qou-cite` | **open** — *"Latent, and deliberately not fixed here"* (cause 4, parked) |
| `qou-f8lit` | **open** — *"What remains of item 1"*, a witness description needing a producer re-run |
| `qou-z9fx` | **open** — records *"do not ship this detector"*, a recommendation, not a closure |
| `qou-keu7` | reads complete; left for its owner |
| `qou-i7ju` | body says UNBLOCKED; later commit claims CLOSED — left for its owner |
| `qou-74ns` | **CLOSED by this session** — all three of its "next steps" measured individually |

So **1 of 7 closed**, against a 2-of-12 prior. The two figures agree: this print-out is a
*worth-opening* list and most of it survives the read. That is now measured twice, by two
agents, on disjoint samples.

### NEW CLASS — the bean's own REMEDIATION LIST can be stale on arrival

This bean's taxonomy has four causes, all about the *commit subject* misleading the
matcher. `qou-74ns` supplies a fifth, one level in: **the bean body's own "next honest
step" list can name work that is already done.**

`qou-74ns` item 2 read *"Decide what `hecke_character_symbolic.py` was meant to name. The
Hoefsmit character route does exist in the corpus under other filenames."* Measured: the
file exists at `computations/hecke/hecke_character_symbolic.py`, landed by merge
`b831ff34c3d` on **2026-08-29**, i.e. **six days before that bean's own updated_at of
2026-09-04T11:15:59Z** — and all five citing derivation chains already write exactly that
path. An agent following the remediation list would have hunted for a phantom that had
existed for a week.

This is strictly worse than a stale status, because a status says *"maybe done"* while a
next-step list says *"do this"*. `scripts/bean-completion-candidates.py` cannot see it:
it matches bean IDs in commit subjects, and nothing about that merge names `qou-74ns`.

Item 1 of the same bean carried a **wrong count** in the same way — it says *"the three
`T_w(Z,N)` steps"*; measured across every `computations/*.derivation.json` there are
**five** without a `script:` note, and all five are correct as they stand (their own text
says *"Pure algebra"*, and this bean's item 1 already allows dropping the citation when
the step is not script-backed).

### Four more instances of the headline pattern, from this session

Beans picked up this session that turned out already resolved by sibling work, none of
which the tracker showed:

* `qou-2ht2` — the bare-array tolerance was already retired.
* `qou-1b9c` — four "stale" witnesses: all three producers re-run, 0 substantive diff,
  committed values already matching the bean's own post-fix targets.
* `qou-74ns` — closed above.
* `qou-3v8h` / `qou-eu0r` — the four-schema zod gap, fixed upstream by folio-assistant
  `a117daa` and verified by parse; both closed.

**And this bean's own lesson reproduced on me.** I verified `qou-74ns` green early in the
session, wrote *"cheap honest closeout available"*, and then did not close it — in the
same session in which I had read this bean's sentence *"an agent that has just spent a
session on backlog hygiene will still drop the close."* It took running the audit to
catch it. That is the second recorded instance of the audit catching its own author's
miss, after `qou-vtau`.


---

## 2026-09-05 — the NORMAL-priority tier has a ~4× higher true-positive rate than the high tier

The caveat block in `bean-completion-candidates.py` reports **MEASURED PRECISION
2 IN 12**, and that figure is stamped *"on the full high-priority list"*. It has
since been read as the tool's precision. It is not — it is the precision **of one
tier**, and the tier it does not describe behaves very differently.

**Measured 2026-09-05 on the normal/unset-priority tail** (PRs #6804, this
branch). Eight candidates read in full; **six closed on evidence**:

| bean | verdict | why |
|---|---|---|
| `qou-jgew` | **CLOSED** | both gates cleared; all 6 producers re-run, 0 substantive diffs |
| `qou-tean` | **CLOSED** | all three freeze mechanisms verified live |
| `qou-0a0z` | **CLOSED** | WALL-2 sorry-free on main, 6 days after the bean's last update |
| `qou-jtc6` | **CLOSED** | fix live; and 4 sibling instances surveyed |
| `qou-rjuj` | **CLOSED** | fix live, probe re-run ASSERTIONS PASS |
| `qou-y82a` | **CLOSED** | producer hardening + 3 self-corrections all live |
| `qou-f9th` | open | cause 3, sharply — see below |
| `qou-myk3` | open | cause 1: 1 of 41 scanners fixed, 40 explicitly "candidates, NOT a work order" |

**6 of 8 (75 %) against 2 of 12 (17 %).** Small sample and not a claim about the
whole tail, but the direction is large and has a mechanism behind it, below.

### Why the tiers differ — and it is not about the beans

A high-priority bean is one an agent flagged as *important*, so it gets picked up,
argued with, partially closed, reopened, and superseded — accreting exactly the
four structural causes this tool documents. A normal-priority bean is more often
**one defect, fixed once, status never moved**. The tool is measuring the *shape
of the bean's history*, not its priority, and priority correlates with how much
history a bean has.

**Practical consequence: read the tail, not the head.** The high tier is where
the false positives concentrate, and it is also the tier every prior pass has
already read. The ~70 untouched normal-priority candidates are the cheaper half.

### `qou-f9th` is cause 3 in its purest form, and worth naming

The matched "later" commit is `4d86daa3eab` — *"the certificate corpus is not
reproducible — closed question, do not retry"* — which is **precisely the claim
the bean's own retraction says was wrong**. The bean was reopened by its author
as a scope-(b) over-narrowing (*"I turned a failed probe into a structural
exclusion and told the next agent not to look"*). So the completion verb here is
attached to a *withdrawn* conclusion.

That is worse than a neutral false positive: acting on it would re-close a bean
whose entire current content is the retraction of the thing the commit asserts.
What actually remains in it is an **owner call** — `--write` on 22 re-anchorable
certificates rewrites committed published data — not agent work.

Generalisation for the tool's caveat block: **a completion verb over a claim the
bean later retracted looks identical to a completion verb over work the bean
later absorbed.** Only the body separates them, which is the argument for the
read queue rather than a filter.

In-progress in Round 101 PR litlfred/qou#8450.
