---
# qou-4kc0
title: Detector-report witnesses contaminate the witness-copy index — measured, only the self case fixed
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-06T07:31:18Z
updated_at: 2026-10-04T15:18:50Z
parent: qou-5vkl
---

Found by USING the audit (bean `qou-psjm`), while checking whether three values
copied from a retired witness had a live successor. The only "live" carrier
turned out to be the audit's own report.

## The premise being violated

`witness_value_copy_audit`'s own docstring: *"A producer computes a number and
records it in its `*.witness.json`. A second script needs that number and, instead
of reading the witness, types it in."*

An **audit's report witness is not a producer's output.** When a detector
tabulates the literals it found, its witness carries those literals — so my audit
reads it and concludes a producer computed the value. Two detectors agreeing they
saw a number is not evidence of a copy.

## Measured, on 232 NARROW findings before the fix

Top carriers, by how many findings name them:

    232   [report]    computations/witness-value-copy-audit.witness.json   <- MY OWN
     86   [report]    computations/cal4-disguise-hunt.witness.json
     10   [report]    computations/codata-truncation-audit.witness.json
      8   [producer]  computations/qbeta/qbeta-c3-borel-pade-deformed-meridian.witness.json
      7   [producer]  computations/qbeta-5two-route70-sum-rule-proved.witness.json

`cal4_disguise_hunt.py` says in its own docstring that it hunts *"hardcoded
high-precision literals (>= 10 digits)"*. Its witness is a list of literals it
found. That is a report, structurally.

## FIXED: the self case only (PR #6904)

Unambiguous, and the same principle the audit already applied to its own `.py`.
Contamination ran BOTH ways:

  * 2 findings had NO carrier but the audit's own witness — once reported, they
    re-reported themselves forever. Self-sustaining phantoms.
  * every count was inflated by exactly 1, and the NARROW/SHARED cut is `<= 3`,
    so literals carried by 3 real witnesses read as 4 and were filed SHARED.

Measured effect of excluding it:

    NARROW   232 -> 277     (47 promoted from SHARED, 2 phantoms removed)
    SHARED   580 -> 533
    from _deprecated  13 -> 20

So the omission made the gate **LOOSER**, hiding 47 real copies — not noisier.
Guarded by a self-test; `OWN_WITNESS` is derived from `__file__`, not spelled.

## NOT FIXED, deliberately — and here is the counter-evidence

Excluding the OTHER report witnesses too was measured and NOT applied:

    NARROW   232 -> 205     SHARED 580 -> 531     76 findings vanish entirely

76 vanishing means their only carriers were reports — those are probably real
false positives. But the 49 it PROMOTES to NARROW include:

    0.0072973525693        alpha_em
    0.51099894999999995    m_e, in a float64 spelling
    1.109978582751380808   the proton q0

Those are shared reference CONSTANTS. NARROW is defined as "one producer's
output, copied", and these are not that — so the promotion is wrong for them,
which means the `<= 3` threshold does not carry the same meaning once reports
are removed. **Fixing the carrier set without revisiting the threshold would
trade one misclassification for another.**

Note the measurement is a LOWER BOUND either way: `witnesses[]` is truncated to
4 entries in the witness, so only the reports visible in that truncated list can
be subtracted.

## Options

1. Exclude reports AND re-derive the NARROW/SHARED threshold against a
   producer-only carrier set. Correct, and the most work.
2. Exclude reports by a DECLARED list with a reason per entry, plus a self-test
   that each named file still exists. Auditable; decays unless maintained. A
   name-pattern match ('audit'/'hunt'/'scan') is NOT acceptable — AGENTS.md's
   detector-blindness taxonomy is largely a catalogue of pattern-matchers going
   wrong, and this audit has already contributed two rows to it.
3. Discriminate structurally: a report's payload carries `file`/`line` beside
   the literal, a producer's does not. Cheap to test, needs validating against
   the real corpus before it is trusted.
4. Nothing. The self case is fixed; 86 + 10 findings keep a report among their
   carriers, inflating counts and hiding an unknown number of further NARROW
   findings.

**Recommendation (my judgement, not a finding): 3, validated against 2.**
Structural beats a maintained list, but only if it is checked against a declared
list first rather than trusted on its face.

## Default if nobody acts

Option 4. The gate stays correct in the strict direction for the self case and
keeps under-reporting by an unmeasured amount for the rest.

- **Round 94 (`litlfred/qou#8424`)**: Advanced in `feat/round94-parity-level-lever1depth2-tauclosed-chainlog-43c1` (Commit 1 `c1698951b30460bb111c1e97552482f0b0622bd0`, Commit 2 `5a166eac86b999ab31c9bdd39f5908e1c848e122`, probe sha256 `1438398dfd335d3f6e9ebdcaa8df8fdc4613a507b4d480b0c9dde22e4b3c8bcb`).
