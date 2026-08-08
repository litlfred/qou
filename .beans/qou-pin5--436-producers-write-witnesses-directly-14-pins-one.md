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


## RESOLVED 2026-08-08 — all 14 now PRODUCE their pin

`computations/audits/q0_backfilled_pin_fix.py` (new) applies the
`stamp_staleness_metadata` recipe to every backfilled pin, with the safety check
that has to come first.

### The 14 confirmed by an independent test

"Writes via `json.dump`" is the wrong detector — it flags **46** witnesses here,
most of which do reach a builder somewhere. The property that matters is whether
the PRODUCER ITSELF maintains the pin:

    produces-pin  the source mentions `q0Anchor`          3
    via-builder   calls WitnessBuilder/wrap_legacy/stamp  559
    BACKFILLED    neither — the pin is unmaintained        14

That returns **exactly 14**, reproducing this bean's count by a different route.

### 🛑 The check that had to come first

`stamp_staleness_metadata` auto-resolves the anchor through `resolve_q0_anchor`,
which **defaults to proton for an undeclared stem**. Stamping a muon-recorded
witness whose producer is undeclared would silently FLIP it to proton —
destroying a correct label under the banner of protecting it, the same trap that
broke the first `witness.py` preserve-forward fix.

Checked before editing: 13 of 14 were safe (every muon-pinned one is already
declared `ideal_muon`, so the stamp reproduces its label). The 14th,
`zhabiro_phiq_production_crosscheck`, was refused by the guard and handled as an
**evidenced correction** instead: its committed `q0Value` is the MUON literal
under a proton `q0_source`, i.e. that witness was generated through the
cross-layer fallback removed the same day. Its muon pin records the DEFECT, not
an intent, so proton is right — declared `physical_proton` and listed in the
tool's `ACCEPT_FLIP` with that reasoning inline, rather than hand-edited.

### A gap in `stamp_staleness_metadata` itself, found by the coverage number

After stamping 13 producers, checkable coverage went **DOWN** (545 → 542). The
helper sets `scriptHash`, `commitSha`, `engine`, `computedAt`, `q0Anchor`… but
**not `scriptFile`** — the key every anchor audit uses to map a witness back to
its producer. These callers rebuild their payload each run, so a `scriptFile`
that had itself only been backfilled vanished on regeneration: 4 witnesses got a
correctly-written pin that nothing could attribute.

Fixed in `witness.py`: `scriptFile` is now stamped first, with the same basename
convention `build()` uses. A pin nothing can attribute is barely better than no
pin. 33/33 substrate tests pass.

### Result

    14/14 pins now PRODUCED (verified by re-running each and confirming survival)
    coverage 545 -> 546 checkable, DECL_MISMATCH 0
    12 witnesses committed; every moved field explained (0 UNEXPLAINED),
    no assertion-state changes

`lw2_c2_independent_hopf_test_attempt` cannot run from its own directory here
(`ModuleNotFoundError: q_parameter` — it does not add `computations/` to
`sys.path`). That fails identically at HEAD, so it is a pre-existing packaging
quirk, not this change; verified instead with `PYTHONPATH` set, and its pin
survives.

Two producers were reverted rather than committed — see qou-pin6.
