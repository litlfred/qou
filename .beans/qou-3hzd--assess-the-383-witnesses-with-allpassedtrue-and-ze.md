---
# qou-3hzd
title: Assess the ~383 witnesses with allPassed:true and zero assertions (NOT the wrap_legacy bug)
status: completed
type: task
priority: normal
created_at: 2026-08-14T20:03:32Z
updated_at: 2026-08-15T00:19:50Z
---



## Assessment 2026-08-15 — the population is benign; ONE real defect

Answered. The 389 is **not** a defect count, confirming the correction already
made under `qou-l5zi`. Classified all 389 by whether the producer intends to
assert anything:

| class | count | reading |
|---|---|---|
| no check machinery at all (data-only witnesses) | **212** | benign — nothing to assert |
| check-like language, no `add_assertion` | **175** | mostly incidental wording |
| has `add_assertion`, none fired | **2** | benign |

Of the 175, **66** carry pass/fail or verdict data *outside* the `assertions`
array. That sounds alarming and mostly is not: a probe whose finding is
"EXCLUDED" or "NEGATIVE" can legitimately record that as a **passed** check —
a negative *verdict* is not a failed *check*. Confusing the two is how the 389
got over-claimed in the first place.

So the discriminator applied was narrower: does the witness contain an explicit
**failing** check in its own body while claiming `allPassed: true`?

**3 of 389.** And two of those are content rather than defects:

* `awzero-asymptotics` — `A5_failure_map.transitions[*].holds = False`. It is a
  *failure map*; recording False is its purpose.
* `lever1-binding-habiro-single-element-test` — `survives_heldout = False`. A
  held-out test whose finding is that candidates do not survive.

### The one real defect: `canonical-derivation-pipeline-compliance`

A **compliance dashboard** — the one place where a false green actually costs
something. It joins six upstream audits into seven contracts, and carried
`allPassed: true` with **zero assertions** while `data.contracts` recorded
failures. It also exited 0 unconditionally, so a caller could not distinguish a
compliant pipeline from a failing one without parsing the witness — the same
silent-success shape as `qou-9d6h`.

Fixed: one assertion per contract, so `allPassed` reports what the dashboard
found, and a non-zero exit when any contract fails. Current run:

```
allPassed: False   (7 assertions, 2 failing)
  ✗ WitnessBuilder usage (P30)        142 of 730 files bypass WitnessBuilder
  ✗ Witness reproducibility (P32)
  ⚠ CODATA registry (P31) · ⚠ provenance completeness (I14) · 4 pass
```

`warn` counts as passed — it is a threshold the dashboard deliberately scores at
0.5, and collapsing it into `fail` would swap one wrong verdict for another.
`missing` fails, since an unverifiable contract is not a satisfied one.

**A latent bug came with it.** `_summarize_repro` now serialises `pass_ratio` as
a string (draining 3 raw-float64 fields from the baseline — ratios of counts,
same class as `collision_fraction`), and `_contract_witness_reproducibility`
reads that same summary. Its `pass_ratio == 1.0` test would have silently
compared `"1.000000"` to `1.0` and always been False — masked by the
`or pass_n > 0` fallback beside it, which is exactly how such an accident
survives review. Coerced explicitly.

### Verdict on the class

`allPassed: true` with zero assertions is **weak, not wrong**, for the 386. It
asserts nothing and should probably be `null`, but changing the schema across
2086 witnesses is a much larger and lower-value change than it first appears —
and this audit found no evidence the field is misleading anyone in those cases.

**Where it does matter is where the witness is a gate.** That is the rule worth
carrying forward: a witness that scores, aggregates or gates must register its
findings as assertions. One such witness existed; it is fixed.
