---
# qou-hytc
title: 64 COMPUTED assertion tolerances are still raw float64 — a producer fix, not a serialization one
status: in-progress
pr: 8290
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-28T19:42:44Z
updated_at: 2026-11-17T08:47:00Z
parent: qou-9nnz
---

Left open deliberately by PR #5910, which drained the other 1232.

## What is left

Of the 1296 raw-float64 `.assertions[].tolerance` fields on `main` at
`60f0937d15`, 1232 were DECLARED literals and are now serialised as such.
The remaining **64 are COMPUTED** — most likely an error budget scaled off
the expected value:

    1025.6028557082007   13221.970394462982   0.0222456607
    130.70734000000002   1.3050938107994625e-12   4.967999999999999

Significant digits split cleanly, with an EMPTY BIN at 6:

    1 sig 1198 | 2 sig 24 | 3 sig 2 | 4 sig 7 | 5 sig 1
    6 sig    0   <- the gap
    7 sig    5 | 8 sig 14 | 9 sig 6 | 16 sig 20 | 17 sig 19

## Why these were NOT converted

`qou_substrate.witness._tolerance_literal` refuses them, on purpose. A
declared threshold written as `"1e-9"` claims one significant digit and
loses nothing. A computed tolerance written as `"1025.6028557082007"`
would claim seventeen digits of a number that reached f64 from an mpf —
which is the laundering the raw-float64 guard exists to stop. Converting
them would drain the ratchet while hiding the defect.

`130.70734000000002` and `4.967999999999999` carry visible
float-arithmetic residue, so at least those two are arithmetic on floats,
not a typed constant.

## The honest fix

Per-producer, one at a time: carry the tolerance as `mpmath.mpf` from
whatever computes it and serialise with `_precision.fmt`, exactly as for
any other computed quantity. There is no shared-path shortcut here —
that is the whole reason this is a separate bean from #5910.

## Also left, and not this bean

* `.assertions[].computed` (84 fields) and `.assertions[].expected` (27)
  in the 1-to-4-field group. Results, not thresholds; same per-producer
  treatment, different field.
* ~200 integral-valued tolerances (`0.0`, `1.0`). Exact in binary64 and
  already excused by the ratchet — nothing to fix.

## Progress 2026-11-17 (PR #8290)

Lifted `computations/tau-lepton-nf.py` to full `mpmath.mpf` (`set_compute_dps()`, `Q_50_DIGIT_STR`, `VOL_FIGURE_EIGHT_50_STR`, `MASS_RATIO_MU_E_STR`, `_precision.fmt`), draining all 4 computed `float64` assertion tolerances and all 64 other raw `float64` fields in `computations/tau-lepton-nf.witness.json` (`68 -> 0` raw `float64`) on PR #8290 (`1c907342f24ac048c99eb24f30832b0b87b024b0`).
