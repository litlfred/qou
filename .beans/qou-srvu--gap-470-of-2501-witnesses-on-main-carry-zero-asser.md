---
# qou-srvu
title: 'GAP: 470 of 2501 witnesses on main carry ZERO assertions and all report allPassed=true'
status: todo
type: task
priority: normal
created_at: 2026-08-30T09:45:49Z
updated_at: 2026-08-30T12:52:25Z
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
