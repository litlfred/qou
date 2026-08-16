---
# qou-5sg8
title: 'float64-padding ratchet RED on main: categorical-bypass-volmatch-demo carries 4 padded binary64 after the mpf lift'
status: todo
type: bug
created_at: 2026-08-16T02:03:14Z
updated_at: 2026-08-16T02:03:14Z
---

Found 2026-08-16 running `scripts/precision-gates.sh` as the prepare-merge §4b
gate on PR #5165. NOT that branch's regression -- it has never touched this
producer or its witness.

## The red

    float64-padding ratchet: baseline 13 -> 17 occurrences, 4 NEW

All four are in `computations/categorical-bypass-volmatch-demo.witness.json`:

    data.rows[0].ratio_direct_to_AME
        claims  0.43313064724721211939950649139063898473978042602539...
        really  0.4331306472472121
    data.rows[1].B_AME_MeV
        claims  2.2245661999999999380861481768079102039337158203125...
        really  2.2245662
    data.rows[2].B_AME_MeV
        claims  8.4817961999999997857457856298424303531646728515625...
        really  8.4817962
    data.rows[3].B_AME_MeV
        claims  7.71804132000000020497054720181040465831756591796875...
        really  7.71804132

Those tails are the exact decimal expansions of the binary64 values -- the
signature of `mp.mpf(<float>)` serialized at full dps. This is fake precision
in the padding audit's precise sense: 50+ digits claimed, ~16 real.

## Cause: the mpf lift reached the constant but not this consumer

`git log` puts the last touch on this witness at `50cc629802`
("fix(precision): the binding-family producers crashed on mpf JSON; port them
properly"), 2026-08-15. That arc (qou-3wqg / qou-hqjf) lifted `codata_constants`
and `B_AME_MEV` to mpf. This producer takes those constants, and somewhere in
its path a value goes float -> `mp.mpf(<float>)` rather than being carried as
mpf or rebuilt from the decimal string. `mp.mpf(2.2245662)` binds the binary64
value; `mp.mpf("2.2245662")` binds the decimal one -- the distinction the
`B_AME_MEV` comment in `canonical_mass_table_extended.py` already spells out for
its own literals.

## Not fixed here, and why

Different arc's file, and the fix is a producer port, not a serialization tweak.
`qou-hqjf` is COMPLETED and covers a DIFFERENT defect in the neighbourhood -- the
`TypeError: Object of type mpf is not JSON serializable` crash. Its fix made
these producers run again; this bean is about what the now-running producer
writes. Do not close one against the other.

## What a fix looks like

1. Trace where the float enters `categorical_bypass_volmatch_demo.py` -- most
   likely a `float()` on a CODATA/AME constant, or a `knot_volumes` back-compat
   f64 alias, the same aliases `qou-hqjf` names as the root of its own bug.
2. Carry it as mpf from source (or rebuild via `mp.mpf("<decimal>")`) and
   serialize with `_precision.fmt`.
3. Re-run the producer and confirm `witness_float64_padding_audit.py --strict`
   drops back to the 13 baseline.

Do NOT rebaseline. Serializing a binary64 at 50 dps is exactly what the padding
ratchet exists to catch, and the baseline drains rather than grows.

## Wider check worth doing at the same time

`50cc629802` re-ran a family of producers. This one is the only NEW padding
offender the gate reports, but the same float -> `mp.mpf` shape could sit in a
sibling producer whose witness has not been regenerated yet, in which case it is
latent rather than absent. Worth a sweep of that commit's producer list before
closing.
