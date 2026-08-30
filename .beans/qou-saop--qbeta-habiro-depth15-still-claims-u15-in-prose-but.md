---
# qou-saop
title: qbeta_habiro_depth15 still claims u^15 in prose but computes u^4 after the C-to-D upstream regen
status: todo
type: task
priority: normal
created_at: 2026-08-30T10:19:31Z
updated_at: 2026-08-30T10:19:53Z
---


## The reversal

`computations/qbeta/qbeta_habiro_depth15_interpretation.py` is named for a
depth of **15**. Its committed witness (2026-06-02) recorded the first
differing u-exponent as 15 and the verdict
`FIRST-DIFFERING-EXPONENT (Test F)`.

Its upstream `habiro/habiro-coefficients-atomic.witness.json` was regenerated
on 2026-08-26 by `126edfa8929` ("fix(precision): a float64 q_0 in the Habiro
witness"). The downstream was never re-run. Re-running it now:

| | committed 2026-06-02 | HEAD source, current inputs |
|---|---|---|
| shared exponents | `u0..u14`, contiguous | `[0,1,2,3,5,6,7,9,10,11,13,14,15]` |
| first differing exponent | **15** | **4** |
| min degree | 15 | 4 |
| `is_u15_min` | true | **false** |
| verdict | FIRST-DIFFERING-EXPONENT (Test F) | **UNCLEAR** |

Reproduced against HEAD source before any edit — pre-existing, not introduced
by the drain.

## Why nothing noticed

The witness's **only** assertion was
`depth15_interpretation_tests_completed: computed=6, expected=6`. A constant
cannot contradict a conclusion, so `allPassed` stayed `true` across a complete
reversal of the probe's finding. This is the sharpest instance of `qou-26f2`
found so far: elsewhere the tautology concealed a number, here it concealed
the verdict.

It is also a second instance of `qou-2364`'s class — a witness stale against a
regenerated upstream — and of `qou-5k8x`'s mechanism, since nothing declared
the edge that would have flagged it.

## Fixed already

The assertion is drained (commit `0e196b9cfd6`) and replaced by two genuinely
disjoint routes: tests recorded in witness data against `test_*` functions
defined, and Test A's min-degree against Test F's first-differing exponent
("equal by linearity; computed by disjoint code paths"). The regenerated
witness records the reversal honestly.

## NOT fixed — the reason for this bean

The module's **docstring, `set_description`, and its own name** still assert
u^15. That prose is now contradicted by the witness sitting beside it, and
correcting it is not a mechanical edit:

* if u^4 is right, the probe's framing, its filename, and any content block
  citing "depth 15" all need revisiting — this is a finding about the Habiro
  depth structure, not a typo;
* if u^15 was right and the C->D upstream regeneration is what broke it, then
  the *upstream* wants scrutiny and this probe is the detector that caught it.

Which of those holds is the question, and it belongs to whoever owns the
Habiro depth work. Both readings are live; nothing here adjudicates between
them.
