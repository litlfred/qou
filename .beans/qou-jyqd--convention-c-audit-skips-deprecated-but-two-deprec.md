---
# qou-jyqd
title: convention-C audit skips _deprecated, but two deprecated producers are still named by content
status: in-progress
type: task
created_at: 2026-08-29T19:36:56Z
updated_at: 2026-08-29T19:36:56Z
---


Found 2026-08-29 while re-assessing `qou-jqjx` against main.

## The gap

`scripts/convention-c-producer-audit.py:62` — *"`_deprecated/` is skipped
entirely."* Right for its purpose: nobody runs deprecated code, so a
convention-C binding there is not a defect to fix.

Wrong for the corpus. **Deprecating a producer removes it from the audit's view
without removing its influence on the content**, because the numbers it
computed are already written into blocks. The convention-C arc reports its
remaining work as a count of ACTIONABLE sites (9 on main today, one of which
`qou-1jny` showed is a false positive). This category is not in that count and
structurally cannot be.

## Measured — and it is small, which is the good news

`scripts/convention-c-deprecated-citation-audit.py`, added with this bean:

    deprecated .py producers                 567
      carrying a convention-C shape          139
      ...AND named by something in content/    2

Two, not 139. The blind spot's live surface is tiny and nameable:

| producer | named by |
|---|---|
| `integer-lp-gluon.py` | `categorical-proton-properties.ts`, `categorical-neutron-properties.ts`, `gluon-stabiliser-ledger.ts` |
| `protium-witness.py` | `mass-theory/binding-scale-catalan.qa.json` |

## A hit is a DEPENDENCY or a CITATION, and the difference is the whole point

- **DEPENDENCY** — a block quotes the producer's numbers. Live content resting
  on a convention the corpus retired.
- **CITATION** — a block names it while *withdrawing* or auditing it. That is
  provenance, and it is what a corrected block should look like.

Both current hits are CITATIONS **on this branch**, because `qou-jqjx` already
withdrew the dependency. `protium-witness.py`'s single hit is a QA sidecar
recording a confirmed braid-word error.

**On `main` the same producer is still a DEPENDENCY.** `categorical-neutron-
properties.md` rests "a difference in depth rather than in the number of gluon
crossings" on `tr_M = -0.132 versus -0.006` — the two numbers that come from
this deprecated convention-C producer and do not survive the convention change.
`qou-vtlj` corrected the crossing count on main and, in doing so, moved the
surviving claim onto exactly those figures.

So: the excision is landing `qou-jqjx`, and this bean is the detector change
that stops the category recurring.

## Why a separate script rather than an edit to the audit

The audit is AST-based and deliberately strict; this is a text cross-reference
and deliberately loose, because a false positive costs one line of reading
while a miss costs a silent dependency. They also answer different questions —
"is this binding a defect" versus "does this dead code still reach the
content". Folding the second into the first would blur the ACTIONABLE count the
arc reports.

## One bug worth recording, because it is the trap this whole area is about

The first pattern was `q\s*\*\*\s*0\.5`, anchored on a bare `q`. The
motivating producer writes `z = 1.0 / (q0**0.5 + qi0**0.5)` — `q0`, not `q` —
so the detector **missed the one file it was written for** and reported a
single hit. Caught by running it and noticing the known case was absent, not by
review. Pattern is now `\bq\w*`.

A detector that silently misses its own motivating case is the same failure as
an assertion that compares a value to itself (`qou-26f2`): both report success
without having looked. Verified by re-running against the known answer, which
is the only check that would have caught it.

- [x] Measure the blind spot
- [x] Ship the cross-reference audit
- [x] Land `qou-jqjx` so `integer-lp-gluon.py` stops being a dependency on main
- [ ] Decide whether the main audit should call this script, or whether the two
      stay separate and the arc reports two numbers


---

## Re-measured on the merged tree, 2026-08-29

Main merged in (2,478 commits). Audit re-run:

    deprecated .py producers                 568
      carrying a convention-C shape          139
      ...AND named by something in content/    2

Unchanged at 2, and `integer-lp-gluon.py` now shows **four** content refs
rather than three — the neutron `.md` joined the list, because the merged
paragraph names the producer in prose while withdrawing it.

**That is the transition this bean was opened for.** All four refs are now
CITATIONS: blocks naming the producer as the source of a defect they have
withdrawn. Before `qou-jqjx` the same producer was a DEPENDENCY — the corpus
quoted its numbers as live results. Same file, same count, opposite meaning,
and the count alone cannot tell them apart. That is why the script reports and
does not adjudicate.

`protium-witness.py` is unchanged: one hit, a QA sidecar recording a confirmed
braid-word error. A citation.

So the convention-C blind spot has **no live dependency today**. The detector
stays, because the category will recur the next time a producer is deprecated
while its numbers are already written into a block.
