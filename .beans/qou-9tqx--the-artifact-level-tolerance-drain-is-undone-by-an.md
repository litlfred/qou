---
# qou-9tqx
title: The artifact-level tolerance drain is undone by any producer re-run — 26 of 33 producers hand-build
status: in-progress
type: task
priority: normal
created_at: 2026-09-04T20:54:48Z
updated_at: 2026-09-05T07:18:27Z
---

## What is true

PR **#5910** / commit **`bc8131bd58`** ("drain(float64): 1232 declared tolerances
in 499 witnesses") converted declared assertion tolerances from JSON floats to
strings across 499 witnesses. It is a **good change, honestly described** — its
own message says *"Applied `computations/normalize_assertion_tolerance.py
--apply`"* and *"No producer was re-run and no computed number moved."*

Measured on `origin/main` `46a986c804`, the drain overwhelmingly HOLDS:

    drained witnesses on main:  still-string 489 | float-again 10 | unreadable 0

## The finding: it is a SWEEP, not a fix, and the corpus will undo it

`normalize_assertion_tolerance.py` edits the ARTIFACT. The guard that would
make it permanent — `qou_substrate.witness._tolerance_literal` — runs at
`Assertion.to_dict`, i.e. only for a producer that constructs an `Assertion`.

**Measured: 26 of 33 producers carrying a float-literal `"tolerance":` in
source hand-build their witness (`json.dump`, no `add_assertion`).** For each
of those, the next re-run re-emits the float and silently undoes the drain for
that file. Verified end-to-end on one: I re-ran
`qbeta_ck_basis_constrained_pslq.py` after the drain and the float came back.

Method (re-run before quoting; both numbers move as producers are migrated):

    grep -rln '"tolerance":[[:space:]]*[0-9]' --include=*.py computations/ \
      | grep -v _deprecated                 # 33 files, 110 sites
    # of those, hand-building = has json.dump AND no add_assertion  -> 26

## The 10 already reverted on main, and why

Two mechanisms, both observed:

- **A merge from a stale branch.** `qbeta-ck-basis-constrained-pslq` went
  18 -> 17 (the drain) -> 18, reverted by `9350fe0df4`, a merge of main into
  `claude/q-riemann-hypothesis-gaps-zgxd8m` carrying a pre-drain copy. Same
  shape as the `arc-count`/`bpp` case flagged on #5891 — but NOT the same fix:
  there the sibling had fixed the PRODUCER so a re-run restored it; here a
  re-run does not.
- **A producer re-run** (the structural case above).

The ten, as of `46a986c804`:

    codata-reconciliation                       1.225887470365857e-06
    delta-lambda-categorical-verification       0.0222456607
    mass-from-q-symbolic                        8.486312831226684e-06
    molecular-trefoil-scan                      4.968, 5.37
    probes/aoperator_a5_crosscheck              1.917721844744708e-06
    probes/qbeta-5two-masbaum-block-row         1.4397054075439577
    probes/qbeta-5two-v3-from-borel-poles       1.8078250278728225
    probes/qbeta-ck-basis-constrained-pslq      1e-08     <- fixed, PR #6453
    q-beta-predicted                            0.013661951235981984
    qbeta/qbeta-meridian-holonomy-anchor-swing  1e-40, 1e-05  <- fixed, PR #6453

**Two are fixed at the producer on PR #6453**; the other **eight are open**.

## What to do (NOT claimed as decided)

The durable fix is to migrate the 26 hand-building producers to
`add_assertion`, so the guard runs and the drain cannot be undone. That is a
real tranche and is NOT in #6453's scope — #6453 fixed only the two that were
RED on the raw-float64 ratchet, at the producer, with exactly the string the
guard emits.

Re-running `normalize_assertion_tolerance.py --apply` periodically would keep
the artifacts clean and is cheap, but it treats the symptom: every re-run of a
hand-building producer re-dirties its file between sweeps.

## Why this matters beyond tidiness

A declared tolerance is a THRESHOLD, not a measurement — that is #5910's own
framing and it is right. The hazard is that the corpus now LOOKS drained
(489/499) while the mechanism that produced that state is not self-sustaining,
so a future reader can reasonably conclude the class is closed when it is one
producer re-run away from reopening, one file at a time, invisibly.
