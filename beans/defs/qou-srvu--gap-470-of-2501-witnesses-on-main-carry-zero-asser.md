---
# qou-srvu
title: 'GAP: 470 of 2501 witnesses on main carry ZERO assertions and all report allPassed=true'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-30T09:45:49Z
updated_at: 2026-10-04T15:19:37Z
parent: qou-5vkl
---

Surfaced while draining `qou-3e5m`, and this bean exists because **that drain
makes it worse**.

## The measurement

    origin/main : 2501 witnesses
                   470 with ZERO assertions  (19 %)
                   470 of those report allPassed = true  (100 %)

A witness with no assertions is indistinguishable from a passing one to every
consumer that reads `allPassed`. "All zero of them passed" is vacuously true and
semantically misleading.

## Why the existing detector cannot see it

`computations/audits/self_fulfilling_assertion_audit.py` scans `add_assertion`
CALL SITES. A producer that never calls it has no site to scan, so a
zero-assertion witness is invisible to the tool built to catch assertions that
cannot fail — the limiting case of exactly that defect. This is the same shape
as taxonomy row 18 (calling-form blindness): the detector keys on the presence
of a construct, so absence of the construct is its blind spot.

## The drain contributes to it — measured, not hypothetical

Two producers went to zero assertions on the `qou-3e5m` branch, both correctly:

- `casimir_q_factorial_probe` 1 -> 0. Its only assertion was a self-comparison
  on a count that is **0**; a `> 0` flag would have asserted an OPEN conjecture
  (sub-problem 3 of `conj:casimir-epsilon-vacuum`) and failed on correct
  behaviour.
- `intermediate_knot_detection` 2 -> 0. Its assertions compared a knot LABEL to
  itself; a per-atom `cos_sim > 0.7` threshold would fail on 5 of 7 atoms that
  legitimately sit below the bar.

Both demotions are right on their own terms. Together they show the tension:
**honestly removing a fake assertion can leave a witness asserting nothing**,
and nothing currently notices.

## What would close it

1. A detector over `computations/**/*.witness.json` flagging
   `len(assertions) == 0`, agent-triaged like the vacuity ledger — some
   producers are genuinely pure data emitters and that is fine, provided it is
   RECORDED as a deliberate choice rather than a silent state.
2. Decide what `allPassed` should be on an empty list. `true` is the current
   behaviour and is the misleading one; `null` would be honest and would break
   consumers that assume a boolean. That is an owner call, not an agent one.
3. The deeper fix is the same missing constructor the `qou-3e5m` triage doc
   names: `WitnessBuilder` has no way to say "this run measured X and X is a
   result, not a check", so an author with nothing falsifiable to assert either
   writes a fake assertion or writes none.

Not started. Recorded now because the number is measured and because the drain
that produced it is in flight.


## 2026-08-30 — detector landed; the number in the entry above is WRONG twice

Re-measured on current `main` (3280 witnesses, up from the 2501 I first
counted). The figure "470 of 2501, all reporting allPassed=true" is wrong in
both directions:

| category | count | verdict |
|---|---|---|
| has assertions | 2045 | fine |
| no `assertions` key, **no `allPassed` claim** | **756** | **NOT a defect** |
| asserts nothing **AND** claims `allPassed: true` | **478** | the defect |
| — of those, under `_deprecated/` | 58 | ignore |
| — **LIVE** | **420** | |

**The defect is not "has no assertions" — it is "claims green while asserting
nothing".** Those are different states and conflating them inflates the count
2.8x. 756 witnesses are pure data emitters making no claim, so there is nothing
for them to be wrong about. I nearly reported 1235.

## Landed

`computations/audits/vacuous_green_witness_audit.py` + committed baseline.
Ratchet shape: the list may shrink, never grow; NEW entries exit 1.

Its selftest pins the **narrowing**, per taxonomy row 22's own lesson — the
assumption most likely to be wrong is that "no assertions" is one state, so the
no-key-claims-green vs no-key-claims-nothing pair is the fixture that matters.
Eight cases including `allPassed: "true"` as a **string**, which must NOT count
(a truthy test would over-report).

## Still open — and it is an OWNER call, not an agent one

Draining an entry means one of two things, and only the first is safe for an
agent to do case by case:

1. **Give the witness a real assertion** — good where one exists.
2. **Drop the `allPassed` claim** — but `allPassed` is set by
   `WitnessBuilder.save()`, so what it should be for an empty assertion list is
   one decision affecting all 420 at once, and it changes what every consumer
   reading that field sees.

**Explicitly NOT a third option: inventing an assertion to justify the claim.**
That is this defect re-introduced, and this branch has a worked case of why —
`casimir_q_factorial_probe` lost its only assertion *because* asserting it
would have encoded an open conjecture (sub-problem 3 of
`conj:casimir-epsilon-vacuum`) and failed on correct behaviour.

Two entries this branch added (`casimir_q_factorial_probe`,
`intermediate_knot_detection`) are deliberately left in the baseline pending
that decision.


## 🛑 SAME DAY — this is NOT new, and the "owner call" I was about to raise is SETTLED

Caught by corpus-grep path 3 one step before putting a question to the author
that the corpus had already answered.

**`scripts/check-computation-status.py` already classifies this exact shape**
and calls it **vacuous** — `allPassed: true` over an empty assertions array,
where `all([]) is True` means the witness reports everything passed having
tested nothing. Bean **`qou-vfy1`**, measured 2026-08-22: of 221 blocks marked
`status: "verified"`, **43 were vacuous**. It ships a `--strict-unbacked` flag.

**And the fix I was about to propose is already investigated and WITHDRAWN.**
Making `WitnessBuilder` emit `allPassed: null` for an empty assertion list was
rejected under `qou-vfy1` on measurement: about a dozen producers hand-roll
`return 0 if wit["allPassed"] else 1`, and `None` is falsy, so it converts a
silent false positive into a **loud false negative**. Do not re-propose it.
That checker reads `len(assertions)` directly and needs no schema or producer
change.

### What this bean still adds — a different population, not a duplicate

`check-computation-status.py` walks content blocks, so it only sees a witness
that some block CITES while claiming `verified`. That is the consequential
subset and the right thing to gate a paper on. It cannot see a vacuous witness
no block cites, or one cited by a block with any other status.

    qou-vfy1  :  43 vacuous of  221 `verified` BLOCKS    (consequential subset)
    qou-srvu  : 420 vacuous of 3280 WITNESSES on main    (superset)

So the detector landed here is the wider hygiene net, and it **ratchets** —
count may fall, never rise — which the block-level checker does not do. Both
are now cross-referenced in each other's terms in the new script's docstring.

**Division of labour:** `check-computation-status.py --strict-unbacked` gates
what a paper CLAIMS; `vacuous_green_witness_audit.py` stops the population
growing.

**No owner question is outstanding on this bean.** The `allPassed` semantics
question is closed by `qou-vfy1`. What remains is ordinary draining, one
witness at a time, and the two entries this branch added stay in the baseline
as legitimate cases (`casimir_q_factorial_probe` lost its only assertion
BECAUSE asserting it would have encoded an open conjecture).


## The drain is a contributor, but a SMALL one — measured

My entries above imply the `qou-3e5m` / `qou-26f2` drain is a significant
driver of this population. Measured, it is not.

Of the 420 live vacuous-green witnesses, a producer could be located by name
for **185**. Of those 185, **7 cite `qou-26f2` or `qou-3e5m`** — so the drain
campaign accounts for roughly 4 % of what is locatable, and the population
overwhelmingly **predates** it. (235 producers were not locatable by the
filename heuristic and are unmeasured, not counted as either.)

### The worked example is a sibling's, and it is better evidence than mine

`computations/audits/braid_encoding_audit.py`. A sibling removed three
`add_assertion(computed=True, expected=True)` calls under `qou-26f2` and
recorded what they documented as **data**, with this reasoning in the source:

> *"they passed by construction and contributed to `allPassed` without checking
> anything ... Each documents a finding this audit made by reading; none of the
> three is a computation this script performs, so the remedy is to record them
> as findings rather than dress them as checks."*

That disposition is exactly right. And the witness it produces has
`assertions: 0` and `allPassed: true`.

**So a correctly-drained producer lands in this population by default**, because
`allPassed` is emitted regardless of whether anything was asserted. It is not
that the drain is careless — it is that the two mechanisms are independent, and
nothing connects "I removed the fake check" to "so stop claiming green".

This is the sharpest statement of the gap: **the defect is not created by bad
drains, it is created by `save()` emitting a verdict for a run that reached no
verdict.** `qou-vfy1` already measured the consequential subset and withdrew
the `allPassed: null` fix for a good reason (~12 producers hand-roll
`return 0 if wit["allPassed"] else 1`, and `None` is falsy). So the remedy has
to be something else — a per-witness opt-out, a separate field, or leaving the
detection to the two audits and never gating on `allPassed` for an empty list.
Not proposed here; recorded so the next attempt starts from the constraint
rather than rediscovering it.
