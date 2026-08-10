---
# qou-3jwy
title: kappa float64 drain traded one gate for the other - padding 13 to 48 on main
status: todo
type: bug
created_at: 2026-08-10T18:46:22Z
updated_at: 2026-08-10T18:46:22Z
---

## The finding

`scripts/precision-gates.sh` is RED on `main` on the **float64-padding
ratchet**: 48 padded occurrences against a baseline of 13, i.e. **35 NEW**.
Verified on a clean worktree of `origin/main`, so it is not a branch artifact.

Two files carry it, both kappa:

    computations/kappa-mirror-split-shell-test.witness.json
    computations/kappa-coulomb-reconciliation.witness.json

## Cause: the raw-float64 drain at 7733a5edb

That commit — *"drain all six kappa witnesses off the raw-float64 ratchet"* —
did exactly what its own message says: *"Each probe now carries values as
mpmath.mpf from source ... and serializes through `_precision.fmt`."*

For a value **computed at full working precision**, that is right. For a value
that **reached `mpf` from a 53-bit source**, it is the padding defect: `fmt`
writes at `OUTPUT_DPS`, so a float64 gets printed with 30+ digits it never
had. The audit shows it plainly:

    claims 1.19999999999999995559107901499373838305473327636718...
    really 1.2

    claims 1.76000000000000000888178419700125232338905334472656...
    really 1.76

    claims 3.53653199999999401370587293058633804321289062500000...
    really 3.536531999999994

`1.2` and `1.76` are hand-written constants; the third is a float-computed
delta. None of them acquired precision by being wrapped in `mpf`.

So this is not a regression in the sense of "someone got sloppy" — it is the
**two gates pulling in opposite directions**, and satisfying one by wrapping
in `mpf` lands you on the other. Worth recording as a pattern, because the
next drain will hit it too.

## The fix already exists and is named

`qou_substrate.precision.str_at_true_precision` exists for exactly this case.
Its docstring states the rule outright: `fmt` *"is right for a value computed
at full working precision and wrong for one that reached mpf from a 53-bit
source — an f64 kernel, a numpy trace, a float-valued dict entry. Printing
that at 50 dps emits the binary64 expansion."*

So the remediation is per-field, not per-file:

* value genuinely computed in mpmath  ->  keep `fmt`
* value that entered as a float64 constant or an f64-computed quantity
  ->  `str_at_true_precision`, **or** fix it further upstream so it is
  genuinely mpf from the source (e.g. `mp.mpf("1.2")` at module scope after
  `set_compute_dps()`, rather than `mp.mpf(1.2)`)

The second is better where the constant is exact-as-written: `mp.mpf("1.76")`
is 1.76 to working precision, while `mp.mpf(1.76)` is the binary64 neighbour
and will pad forever.

## Not done here

Found while verifying PR #4948, which is **exactly neutral** on both ratchets
(identical numbers to main on each). These six probes belong to the arc that
drained them; folding someone else's remediation into an unrelated merge is
what this repo's "do not fold it into an unrelated change" discipline exists
to prevent. Recorded rather than fixed.
