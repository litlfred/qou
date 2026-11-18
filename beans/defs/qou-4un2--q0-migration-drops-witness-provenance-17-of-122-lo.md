---
# qou-4un2
title: 'q0 migration DROPS witness provenance: 17 of 122 lost scriptFile/commitSha, and the audit is blind to it by construction'
status: in-progress
type: bug
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-28T14:08:26Z
updated_at: 2026-10-04T15:15:47Z
parent: qou-5vkl
---

## Measured 2026-08-28, on origin/main at cdbdc84af1

The `migrate(q0) batch*` sweep (bean `qou-1c4y`, still **in-progress**) regenerates
witnesses through producers that do not emit provenance. Those producers write a
witness WITHOUT the top-level fields, so the regeneration DELETES them.

Method: for each of the 9 `migrate(q0) batch*` commits, diff every modified
`*.witness.json` between `sha~1` and `sha`, and record keys present before and
absent after.

    9 migration batch commits
    122 witness files modified
    17 lost at least one provenance field
    per-field: scriptFile 17, commitSha 17, engine 16, auditOnly 15

Worked case — `sublemma-2-1-alpha-shift-extract.witness.json`:

    c3a7e16856  present: auditOnly, commitSha, engine, scriptFile
    3563e08910  present: NONE          <- migrate(q0) batch 4
    253e2ffaf5  present: NONE          <- still gone on main today

I found this on 2026-08-23 while regression-testing #5517: a fresh run of that
producer dropped exactly those four fields, so I DECLINED to commit the
regeneration. The migration sweep committed it five days later.

## Why no gate caught it

`computations/witness_provenance_attribution_audit.py`, line 12, in its own words:

  > "no `scriptFile` at all are invisible to the method, because there is
  >  nothing to [attribute]"

The gate reports "N witnesses carry a scriptFile claim" — a count over the
witnesses that HAVE one. Deleting the field removes the witness from the
denominator rather than failing anything. A provenance regression is therefore
structurally unobservable to the check meant to police provenance: the metric
is a numerator with no fixed denominator.

## Scope caveat — do NOT quote the aggregate as the loss

Witnesses lacking `scriptFile` went 463 -> 505 across the same window, but the
corpus grew 3060 -> 3170 in it, so most of that +42 is new witnesses that never
had the field. **17 is the defensible number** (per-file before/after); 42 is not.

## Second, separate defect this exposes

These are AGENTS.md "bare producers": the provenance on disk was added
downstream, so re-running one destroys it. That is already recorded as a hazard
in the idle-pass witness policy. What is new here is that a *bulk sweep* is now
executing that hazard at scale, unattended, and `qou-1c4y` has more batches to
run.

## Next honest step (ordered)

1. **Stop the bleed.** Make the migration refuse to write a witness that would
   drop a provenance key present in the committed version. Cheap, and it is the
   only step that must land before the next batch.
2. **Fix the gate.** Make `witness_provenance_attribution_audit` ratchet the
   COUNT of provenance-less witnesses rather than only auditing those that have
   it, so a deletion is a red rather than a smaller denominator.
3. **Restore the 17.** Their prior values are in git; a restore is a JSON merge,
   not a producer re-run (re-running is what deleted them).
4. **Fix the bare producers** so a future re-run emits provenance itself.

Steps 1 and 2 are small and independent of the science. Step 3 is mechanical.
Step 4 is per-producer and is the real fix.


--------

## 2026-08-28 follow-up: the population at risk, and TWO corrections to my own method

### Correction 1 — urgency. The batch sweep already converged.

I first wrote "qou-1c4y is in-progress, so more batches will do the same". Precisely:
the `migrate(q0) batch*` commits ran on 2026-08-24 and ended at batch 8/9
("iteration at practical convergence", "final fixed-point writes"). The 17 are
**static damage, not a growing count.**

The live hazard is different and still real: PR #5818 (MERGED) re-partitioned the
remaining reroute into 12 producers that are safe alone, 5 BLOCKED by a straddle,
4 proton, 3 unlabelled — and recorded them in `qou-aj91` **to be picked up cold**.
Each reroute is a producer RE-RUN, which is the operation that deletes provenance.
So the next agent on `qou-aj91` walks into this unless step 1 lands first.
Nobody is holding that work right now, so this is pre-emptive, not a collision.

### Correction 2 — diagnosis. All 17 are bare; my "4 exceptions" were a grep artifact.

I measured that 4 of the 17 casualties DO use `WitnessBuilder`, which would have
meant the emitter itself can drop provenance — a much worse finding. It is wrong.

The marker `witness_base` matched **line 45 of the Phase-6 path-bridge boilerplate**:

    # Keeps flat-namespace imports (`from witness_base import …`)

a COMMENT, present in nearly every producer. All four have `WitnessBuilder=0`.
Re-measured through `_source_normalise.code_only` (comments and docstrings blanked):

    17 casualties: 17 bare, 0 use WitnessBuilder

This is exactly the defect class PR #5818 built `code_only` for — a name in a
comment is not a usage — and I walked into it with the module already on main.
(An earlier pass also resolved producers by `rglob(base)[0]`, arbitrary among
duplicate basenames; re-run with sibling-preferring resolution the casualty
result was unchanged, so that bug did not affect the count.)

### The population at risk

Witnesses that currently CARRY `scriptFile` but whose producer never calls
`WitnessBuilder` — i.e. a re-run drops provenance, as it did for the 17.
Measured through `code_only`, excluding `_deprecated`:

    carry scriptFile, producer really uses WitnessBuilder : 2226
    carry scriptFile, producer does NOT                   :  281   <-- AT RISK
    no scriptFile at all                                  :  325
    producer unresolvable / ambiguous                     :    8

So the 17 are the realised part of a **281-witness** exposure. Any sweep that
re-runs producers — the `qou-aj91` reroute, an idle-pass witness refresh, a
convention migration — draws from that pool.

**The 8 unresolvable are a separate small finding**: `scriptFile` names a producer
that is not uniquely locatable, so provenance is recorded but not followable.

### Step 1 restated, now that the diagnosis is right

Because all 17 are bare, step 1 does not need to change any producer to land:
a pre-write guard that refuses to drop a provenance key present in the committed
witness covers every one of the 281 regardless of how it writes. Step 4 (make the
producers emit it themselves) remains the real fix, and is now scoped: 281 files,
none of which currently touch `WitnessBuilder`.


--------

## 2026-08-28 — CORRECTION 3: step 1 was designed at the wrong layer, and a guard already exists

Corpus-grepped before writing the guard, per the checklist. **It already exists**:
`_check_producer_takeover` in `tools/qou-substrate/python/qou_substrate/witness.py`
(bean `qou-okl8`), with its own test file and a
`QOU_WITNESS_ALLOW_PRODUCER_TAKEOVER` override. It raises with, literally,
*"drops N field(s) the committed one carries"*.

It cannot catch this class, for a reason that invalidates my step 1 as written.

**1. It lives inside the writer, and these producers bypass the writer.**
`_check_producer_takeover` has exactly ONE call site — `witness.py:2022`, inside
`WitnessBuilder.save()`. Measured on the casualties through `code_only`:

    sweeps/low_isotope_binding_sweep.py      WitnessBuilder=False  json.dump=True
    probes/gt_matrix_pslq_probe.py           WitnessBuilder=False  json.dump=True
    sublemma_2_1_alpha_shift_extract.py      WitnessBuilder=False  json.dump=True

A producer writing json.dump(...) directly never reaches line 2022. **No amount
of strengthening the in-writer guard helps.**

**2. Even if reached, two early returns skip this case by design.**

    if not isinstance(new_script, str): return    # a bare producer has NO scriptFile
    if PurePath(old).name == PurePath(new).name: return

The second is deliberate and documented: *"The same producer dropping a field is
schema evolution and is not this function's business."* That is the right scope
for `qou-okl8` (producer TAKEOVER) and the wrong scope for this bean (provenance
DELETION by the owning producer).

### Revised step 1 — one tree-level ratchet, replacing steps 1 AND 2

The check must be independent of how a producer writes, so it belongs where the
repo already puts this idiom: a **pre-commit ratchet over the tree**, alongside
the raw-float64 and float64-padding ratchets in `scripts/precision-gates.sh`.

    for each changed *.witness.json:
        committed = git show HEAD:<path>
        if any of (scriptFile, commitSha, engine, auditOnly) present in
           committed and absent in the working tree  ->  RED

Properties, none of which the in-writer guard has:

  * catches all 281 at-risk AND the 325 that already carry no scriptFile,
    because it keys on the FILE, not on the producer;
  * needs no producer edits at all;
  * subsumes old step 2 — a deletion becomes a red rather than a smaller
    denominator, so there is no separate "fix the gate" item;
  * `--changed` makes it free when no witness was touched.

**Do NOT extend `_check_producer_takeover` for this.** Widening its early returns
would make it fire on ordinary schema evolution by the owning producer, which is
the exact false positive its author measured against ("how a guard like this
earns a reputation for crying wolf and gets switched off"). Two guards, two
scopes.

### Plan, as revised

  1. tree-level provenance ratchet in precision-gates.sh   (was steps 1 + 2)
  2. restore the 17 from git (JSON merge, not a re-run)     (was step 3)
  3. route the 281 through WitnessBuilder                   (was step 4, the real fix)

- **Round 94 (`litlfred/qou#8424`)**: Advanced in `feat/round94-parity-level-lever1depth2-tauclosed-chainlog-43c1` (Commit 1 `c1698951b30460bb111c1e97552482f0b0622bd0`, Commit 2 `5a166eac86b999ab31c9bdd39f5908e1c848e122`, probe sha256 `1438398dfd335d3f6e9ebdcaa8df8fdc4613a507b4d480b0c9dde22e4b3c8bcb`).
