---
# qou-z11r
title: 58 committed witnesses still carry the convention-C z value while source is migrated to D
status: completed
type: task
priority: normal
created_at: 2026-08-23T08:09:25Z
updated_at: 2026-08-23T08:59:50Z
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


## TRIAGE DONE (2026-08-23, PR #5510)

Full result: [`docs/audits/2026-08-23-convention-c-witness-triage.md`](../docs/audits/2026-08-23-convention-c-witness-triage.md)
plus a per-witness JSON twin.

    z-parameter-echo   40   C only in z/markov-named fields
    payload-or-mixed   16   C baked into a COMPUTED field (Gram, tr_M, traces)
    LIVE-C-PRODUCER     2   source computes sqrt(q)/(q+1) today

Both live-C producers also hardcode a **muon** Q0 literal, and
`signed_crossing_feasibility_probe` types `delta` instead of deriving it —
off-canon on three axes at once.

**The finding that matters:** `signed_crossing_feasibility_probe` emits a
durable `"verdict": "signed-ILP-pure-chirality-refuted"` computed on
convention-C z at a muon pin. Per AGENTS.md that refutation is **C-conditional
and has not been re-derived under D**. Not re-derived here — substituting z_D
into a C-frame result is not a valid move
(`QOU.QBeta.decayLadder_zC_threeRow_ne_zero`), so this is research, not cleanup.

Pin split: 28 p50 / 23 muon / 3 other / 4 mixed — convention and pin are not
separable in this backlog.

**Nothing was mass-regenerated**, and 15 of 58 have no locatable producer.

## Method correction, recorded

I ran two re-run sweeps before concluding the instrument was wrong:

1. A **file-level substring test** cannot distinguish a flipped field from an
   untouched one, because a witness can legitimately hold both z_C and z_D.
2. A producer that **exits 0 in 0 s without rewriting its witness** is
   indistinguishable from one that re-emitted C.

The committed classification is therefore **static**. Both sweeps were stopped
and the tree restored; neither produced a verdict that survived.
