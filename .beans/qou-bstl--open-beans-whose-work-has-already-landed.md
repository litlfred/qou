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

So this is a READ QUEUE, not a close list. **Do not bulk-close from it.**

## The audit caught one of mine

`qou-vtau` — I did the work this session, merged it to `main`
(`3bd8b7689c3`, `711a163a8c1`), and left the bean `todo`. It was found by the
audit written in the same session to catch this in *other people's* beans.

That is the argument for the audit rather than for resolving to be more careful:
an agent that has just spent a session on backlog hygiene will still drop the
close. `qou-vtau` is now closed.

## Next

Read the 12 high-priority candidates and close the ones that are genuinely
done. Not a sweep — one read each, given the false-positive rate above.
