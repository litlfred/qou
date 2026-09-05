---
# qou-9tqx
title: The artifact-level tolerance drain is undone by any producer re-run — 26 of 33 producers hand-build
status: completed
type: task
priority: normal
created_at: 2026-09-04T20:54:48Z
updated_at: 2026-09-05T07:48:03Z
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


## RESOLVED — 2026-09-05, PR #6760. The counts in this bean were wrong.

Corrected by `computations/audits/tolerance_guard_bypass_audit.py`, which asks
the ARTIFACT and imports `qou_substrate.witness._tolerance_literal` so its
verdict IS the guard's rather than a restatement.

**1. "Eight open" is ZERO from this list; the true live count was 1, elsewhere.**
Corpus-wide over 3226 committed witnesses, exactly one carried a tolerance the
guard would stringify: `computations/audits/weight-factor-audit.witness.json`
(11 x `1e-12`). It is not on the ten. Fixed at the producer in #6760.

**2. Seven of the ten were NEVER reverted drains.** Their tolerances are
COMPUTED — >5 significant digits — which #5910 deliberately left alone and
which the guard refuses on purpose, because stringifying a computed value
would hide a real precision defect behind a convention:
`1.225887470365857e-06`, `0.0222456607`, `8.486312831226684e-06`,
`1.917721844744708e-06`, `1.4397054075439577`, `1.8078250278728225`,
`0.013661951235981984`.

**The eighth is the same error one step subtler.** This bean records
`molecular-trefoil-scan` at `4.968, 5.37`. On disk they are
`4.967999999999999` and `5.369999999999999` — DIFFERENT doubles, 16 sig, also
computed. `repr(4.968)` is `'4.968'`, so these were never the literals recorded
here. The remaining two were genuine and both were fixed on #6453.

**Root cause of all three errors: this bean asked "is it a float". The
question is "would the guard change it".**

## TRAP — the hand-building test EXCLUDES the only live offender

"`json.dump` AND no `add_assertion`" over- AND under-counts, and the
under-count is what matters. `weight_factor_audit.py` uses `WitnessBuilder`
and `add_assertion` CORRECTLY — its one `assertions[]` entry has
`tolerance: None`. The eleven floats are assertion-SHAPED rows in the **data
payload** (`{check, n, computed, expected, tolerance, passed}`), a third
structure `Assertion.to_dict` cannot reach. So the narrowing filtered out the
one file that was actually dirty.

The over-count is the mirror: two of the 26 "hand-building producers" are the
drain script's own DOCSTRING and the ratchet's own SELF-TEST FIXTURE.

## TRAP — a declared threshold under a different KEY is invisible to everything

`weight_factor_audit.py:160` carries `"tolerance_at_n12": 0.05`. That is a
declared threshold, 1 significant digit, and would be stringified if the key
were `tolerance` — but the guard, the drain and every audit here key on the
exact name, so it is unreachable to all of them. Deliberately NOT changed:
renaming a payload key to satisfy an audit would break consumers to make a
number look better. Recorded so the next reader knows the key-name surface is
unmeasured rather than clean.

## Still open (NOT fixed here)

- **LATENT: 24 producers** carry a float literal in source whose witness is
  clean today. Each re-run re-dirties its file. This is the bean's real
  finding and it survives intact — only the counts were wrong.
- **UNRESOLVED: 7** sources name a witness the audit cannot locate
  (`qbeta_habiro_p8_deep_probe` writes one that is not committed;
  `knot_volumes` writes to `substrate/`). A tool limit, not a clean bill.
- The durable fix — migrating payload rows to `add_assertion` — remains a
  tranche of its own and is not attempted here.

## BASELINE (re-run before quoting; the command is the entry)

    PYTHONPATH=computations:tools/qou-substrate/python \
      python3 computations/audits/tolerance_guard_bypass_audit.py --strict

2026-09-05 on `58ab6f8563`: 3226 scanned, LIVE-DIRTY 1 (now 0), LATENT 24,
NO-TOLERANCE 1, UNRESOLVED 7.
