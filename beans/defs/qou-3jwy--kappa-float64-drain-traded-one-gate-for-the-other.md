---
# qou-3jwy
title: kappa float64 drain traded one gate for the other - padding 13 to 48 on main
status: completed
type: bug
priority: normal
created_at: 2026-08-10T18:46:22Z
updated_at: 2026-08-10T19:29:34Z
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

---

## FIXED — padding ratchet is GREEN, and raw-float64 got better too

    float64-padding    48 occurrences / 35 NEW   ->   13 = baseline / 0 NEW
    raw-float64        NEW dirty 2               ->   NEW dirty 0

Three producers, all in the same drain family:

    probe_kappa_mirror_split_shell_test.py
    probe_kappa_coulomb_reconciliation.py
    probe_kappa_provenance.py

### The fix is NOT "swap fmt for str_at_true_precision everywhere"

That would have made the gate green while leaving real precision on the
floor. The 35 findings split into two kinds, and only the second wants the
honest-renderer treatment:

**(1) Precision that existed and was destroyed.** `ce.R0_FM` and
`ce.alpha_em_hbar_c_mev_fm()` already return full-precision `mpf`; the probes
wrapped them in `float()` first. Measured:

    genuine    1.41381693076303648646392691171816600928033518
    via float  1.41381693076303638356705505429999902844429016   <- what shipped

Same for `delta_B_observed_MeV`: `ame_binding` returns `mpf`, but each side
was cast to `float` before subtracting, so the DIFFERENCE was 53-bit. Fixed by
deleting the casts — the precision was already there.

Model constants `1.2` and `1.76` are exact as written, so `mp.mpf("1.2")` is
1.2 while `mp.mpf(1.2)` is the binary64 neighbour. String-constructed.

The Coulomb prefactor `0.6` became `mp.mpf(3)/5`: 3/5 is not representable in
binary, so the literal reintroduced a 53-bit factor into an otherwise-mp
product.

**(2) Precision that never existed.** `probe_kappa_provenance` reads its
values out of a committed deprecated witness where they are stored as JSON
floats. Those ARE 53-bit and cannot be fixed at the source — the source is the
file. There, `str_at_true_precision` is the whole fix: print what 53 bits
determine.

### The docstrings were the tell

All three `_ser` hooks asserted some version of *"no float64 ever reaches the
JSON"* — true of the output TYPE, false of its information content. The
provenance one even said the values came in as raw float64 and then concluded
that lifting them to `mpf` made them safe. That is the trade in one sentence,
sitting in a comment, unread. All three rewritten to say which case is which.

### Verified

All twelve assertions across the three probes still PASS and no verdict
changed — this is a serialization repair, not a result change. Padding gate
GREEN. The raw-float64 gate is still red on ONE entry,
`a-K-via-lp-dual-full` 395 -> 867, which is byte-identical to main's copy and
belongs to `qou-ftuv` (inherent Clarabel float64, needs a change to the shared
`lp_dual_solver.to_dict()` contract). Not touched here.
