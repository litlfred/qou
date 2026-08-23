---
# qou-z11r
title: 58 committed witnesses still carry the convention-C z value while source is migrated to D
status: todo
type: task
created_at: 2026-08-23T08:09:25Z
updated_at: 2026-08-23T08:09:25Z
---

Found while answering "any other uses of C convention that need to migrate to D?"
(PR #5510). The SOURCE migration is essentially done; the OUTPUTS are not.

## The gap

    scripts/convention-c-producer-audit.py   ->   1 actionable source site
    witnesses carrying z_C = 0.4993203340...  ->  58
    witnesses carrying z_D = 0.6126880505...  ->   5

Measured by the method AGENTS.md prescribes for this class -- **test the
answer, not the source**. Thirteen source spellings are detector-blind
(docs/audits/2026-08-15-detector-blindness-taxonomy.md), but the C *value*
cannot hide in a committed witness.

    grep -rl "0\.4993203340" --include=*.witness.json computations/ qou-mass/

## Verification status -- ONE confirmed, not 58

Do **not** read the 58 as a work order. I confirmed exactly one end to end:

* `terms-2-3-atom-per-gen-mpfr-50dps.witness.json` -- re-running **main's
  unmodified source** reproduces the same C->D move, so it is genuinely a
  stale witness of an already-migrated producer, not something my branch did.
  Refreshed in #5510; q0-value-drift-audit followed, STALE 305 -> 304.

* `hadron-knot-table.witness.json` -- **unverified.** Its producer crashed
  twice (see the sibling bean): missing scipy, then dtype=object into
  scipy.sparse. Nothing was written, so the "did z flip" comparison measured
  nothing. I nearly reported that non-result as a result.

The other 56 are **unclassified**. Each needs to be sorted into one of:
  (a) stale output of a now-D producer  -> re-run the producer
  (b) deliberate C-vs-D comparison       -> leave, it is the point
  (c) live C producer the detector missed -> a real source-side migration
Only (a) is mechanical. Do not mass-regenerate.

## Why the count alone is not the finding

58-vs-5 looks damning and may not be: a witness can carry z_C as a *recorded
historical value* inside a comparison, which is exactly case (b). The
detector reporting 1 actionable site is consistent with the source being
right and the outputs merely old. That is the hypothesis, on one confirmation.
