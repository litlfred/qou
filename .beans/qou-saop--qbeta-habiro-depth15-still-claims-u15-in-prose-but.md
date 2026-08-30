---
# qou-saop
title: qbeta_habiro_depth15 still claims u^15 in prose but computes u^4 after the C-to-D upstream regen
status: in-progress
type: task
priority: normal
created_at: 2026-08-30T10:19:31Z
updated_at: 2026-08-30T10:27:18Z
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

## INVESTIGATED 2026-08-30 — u^4 is correct, and it was already documented

The bean left two readings live. It is the first: **u^4 is right; u^15 was the
convention-C answer.** Established by matching the polynomial, not by argument.

### First, a correction to this bean's own attribution

It blamed `126edfa8929` (2026-08-26, "fix(precision): a float64 q_0 in the
Habiro witness"). **That commit did not change a single coefficient.** Its
entire diff to the upstream witness is:

    timestamp, scriptHash, scriptCommitSha, commitSha, computedAt
    q_0: 1.1099785827513808  ->  "1.1099785827513808"

— the same number retyped as a string, because the producer computes at a
sixteen-digit q by construction (`Rational(int(_Q_CANONICAL * 10**16), 10**16)`)
and the witness was recording a float64 where the exact decimal belonged. It is
provenance-only. Characterising it as a "convention C→D regeneration" was
wrong, and it came from reading the subject line instead of the diff.

### What actually changed it

`f392d75408e` (2026-08-18): **"regen(D-only): atomic witness unmixed, family
migrated — and Φ_k structure does not survive"**, under the owner directive
*"no C family. D only."* That commit records the p−n difference under D:

    u^4(u^2-u+1)(u^2+u+1)(u^4-u^2+1)(u^32+3u^20-2u^16+3u^12-4u^8+3u^4-2)

and the probe's own `test_A_lowest_degree.factored` today is

    -u**4*(u**2 - u + 1)*(u**2 + u + 1)*(u**4 - u**2 + 1)*(u**32 + 3*u**20 - …)

the same polynomial up to overall sign, with `expanded_min_deg: 4`. **The u^4
was written down on 2026-08-18**, eight days before anyone noticed this probe
was stale. The probe was simply never re-run.

So there is no open question about which is right, and no suggestion the D
migration broke anything: that commit anticipated exactly this, saying the Φ_k
mirror structure does not survive under D and that the differences "carry no
cyclotomic content".

### A third species of the qou-26f2 defect, fixed here

Beyond the drained assertion, the probe **hardcoded its own conclusion into
its output**. `interpretation_categorical` was a fixed string asserting u^15,
returned in the same dict as `first_differing_exponent: 4` and
`is_first_diff_u15: false`, and the console narration printed "u^15" on the
line directly below the one printing the computed `first_diff`.

That is not an assertion that cannot fail — it is **narration that cannot
disagree with its own numbers**, and an AST-identity census cannot see it
because there is no assertion involved at all. All of it now derives from
`first_diff`, and a `shared_exponents_are_contiguous_from_zero` field records
that the agreeing set is gapped under D rather than the contiguous u^0..u^14
the key name assumes.

### Still open, and genuinely an author call

The module's **filename, docstring and `set_description`** still say depth 15.
Renaming a producer is not a mechanical edit — it moves a witness path — and
whether "depth 15" survives as a name for a probe whose answer is 4 is a
framing question. Nothing here touches it.
