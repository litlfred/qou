---
# qou-j9yk
title: WitnessBuilder.wrap_legacy destroys a payload 'computation' method-description (same bug already fixed one key over for assertions)
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-21T15:58:35Z
updated_at: 2026-10-04T15:25:39Z
parent: qou-5vkl
---

## The defect

`WitnessBuilder.wrap_legacy` (`tools/qou-substrate/python/qou_substrate/witness.py:1069`)
skips a payload `computation` key:

```python
elif key == "computation":
    # Filename already encodes this; skip to avoid duplicate
    continue
```

`build()` then sets `"computation": self.name`. So a payload whose
`computation` field holds a **method description** rather than a name has that
text **silently destroyed** — the key survives, only the value is replaced, so
a key-set diff shows zero loss. Measured on
`theta_jet_gb_grading_probe.witness.json`:

- OLD: `"mpmath dps=60; C1 recurrence [m+2]_q b_{m+2}=b_{m+1}+b_m seeded b_0=b_1=1; theta_m=-log_q|b_m|; ... flatness via window means/drift."`
- NEW: `"theta_jet_gb_grading_probe"`

## It is the same bug already fixed one key over

The comment immediately below that branch documents the identical defect for
`assertions`/`allPassed` — they were in `_RESERVED_LEGACY_KEYS` and fell
through the same `continue`, which "silently DISCARDED them" for a producer
writing checks as a payload literal. That was fixed by ADOPTING the value.
`computation` was not.

## Blast radius — why it was not fixed in PR #5373

`tools/qou-substrate/` has 309 in-repo importers, and changing this branch
changes what **every existing wrap_legacy witness** emits for `computation`.
That is a corpus-wide witness move, not a provenance fix, and does not belong
on a PR whose subject is the completeness audit.

## Worked around locally in #5373

The three `computations/probes/` producers migrated there rename the payload
key to `computation_method` so the author's text survives the wrap. Safe there
because nothing reads them (1 py mention each, 0 content refs). That workaround
is per-producer and does **not** generalise — the fix belongs in `witness.py`.

## Suggested fix

Adopt rather than skip, mirroring the `assertions` fix: keep the payload value
when it is not equal to the witness stem, and only fall back to the stem when
the payload has no `computation`. Then audit whether any already-wrapped
witness lost text this way (grep for witnesses whose `computation` equals their
own filename stem *and* whose producer's pre-wrap payload said otherwise).
