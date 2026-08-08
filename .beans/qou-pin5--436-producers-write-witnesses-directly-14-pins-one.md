---
# qou-pin5
title: '436 producers write witnesses with a raw json.dump — 14 pinned witnesses are one rerun away from losing their pin'
status: todo
type: task
priority: normal
created_at: 2026-08-08T21:40:00Z
updated_at: 2026-08-08T21:40:00Z
---

Found by causing it. On 2026-08-08 I fixed `t25_cinquefoil_deltalambda_sign_probe`'s
cross-layer fallback, re-ran the producer to check it still worked, and **silently
dropped its `q0Anchor: proton`** — visible only because the consistency audit's
counts moved by one on a later run (`Q0_OK` 566→565).

## The mechanism

`t25_cinquefoil_deltalambda_sign_probe.py` writes its witness with a raw

    with open(out, "w") as f:
        json.dump(witness, f, indent=2)

It never goes through `WitnessBuilder.save()`. So **neither** of the two
mechanisms that maintain the pin ever runs:

- `build()`'s stamping of a positively-declared pin, and
- `save()`'s preserve-forward of a recorded pin.

Its `q0Anchor: proton` had therefore been **backfilled by a sweep**, not written
by the producer — and the first regeneration after that backfill drops it. The
witness had carried a correct pin that nothing was keeping alive.

## Scale

    producers writing a witness via raw json.dump (no WitnessBuilder) : 436
    pinned witnesses whose producer writes that way                   :  14

Those **14 are each one rerun away** from the loss. They are not wrong today;
they are unmaintained. And since `witness.py`'s own comment records that only
184 of ~780 producers call `stamp_staleness_metadata`, this is the same root
cause seen from the other side.

## Fixed here (1 of 15)

`t25_cinquefoil_deltalambda_sign_probe` now stamps its own pin via
`WitnessBuilder.stamp_staleness_metadata(...)` — the documented helper for
exactly this case ("used when the legacy filename is non-standard and
`wrap_legacy().save()` cannot be applied without breaking consumers"). Also
declared `physical_proton` (inert; it already resolved proton). Verified: the
witness now reads `q0Anchor: proton` **written by the producer**, so it survives
regeneration.

Implementation note for whoever does the rest: import
`from qou_substrate.witness import WitnessBuilder`, **not** the `witness_base`
shim — many subdirectory producers put only `tools/qou-substrate/python` on
`sys.path`, so the shim in `computations/substrate/` is not importable from
them. The first attempt here failed exactly that way.

## Next step

Identify the remaining **14** (the scan in this bean's history: pinned witnesses
whose `scriptFile` stem belongs to the direct-writing set) and give each the same
one-call fix. That converts a backfilled, decaying pin into a produced one.

The broader 436 mostly carry no pin at all, which is a tolerated state — they do
not need converting unless and until someone wants them audited. Do **not** bulk-
convert: the point is that a pin should be *produced* by whatever writes it, not
that every witness needs a pin.


## CONFIRMED IN THE WILD 2026-08-08 — `zhabiro_phiq_production_crosscheck`

This bean predicted that a backfilled pin dies on the first regeneration. Here
is the second instance, caught before it was committed.

Regenerating that producer drops the **entire** top-level provenance block:

    lost: commitSha, computedAt, durationMs, engineVersion,
          q0Anchor, q0Value, scriptCommitSha, scriptFile, scriptHash

It writes its own `_provenance` key with a raw `json.dump` and never calls
`WitnessBuilder.save()`, so every one of those top-level keys was **backfilled
by a sweep**. Exactly the mechanism this bean describes, now observed on a
second producer.

Extra finding, and the sharper one: its committed `q0Value` is
`1.109978595557334719899763…` — the **MUON** literal — while its `q0_source`
labels a proton accessor. That witness was therefore generated through the
cross-layer `except`-handler fallback that was removed corpus-wide on
2026-08-08 (`q0_cross_layer_fallback_fix.py`). It is a preserved artifact of the
defect class, not merely an unmaintained pin.

Consequence: it must NOT be declared in `q0_anchor_manifest.json` until the
producer stamps its own pin. Declaring first would turn an UNDETERMINED pin into
a DECL_MISMATCH the next regeneration cannot clear. Held out mechanically in
`computations/audits/q0_undetermined_triage.py` (`HOLD_OUT`).

Order of operations for this one: give it the `stamp_staleness_metadata` fix
this bean prescribes → regenerate (its q₀ becomes proton, honestly) → then
declare `physical_proton`.
