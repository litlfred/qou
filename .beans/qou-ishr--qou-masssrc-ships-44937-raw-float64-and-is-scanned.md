---
# qou-ishr
title: qou-mass/src ships 44,937 raw float64 and is scanned by no ratchet — 97.7% from one producer
status: in-progress
type: task
priority: normal
created_at: 2026-08-22T15:22:10Z
updated_at: 2026-08-22T16:12:19Z
---

Follow-up to `qou-cdj8` (#5431), which surfaced the number, and to the owner's
question: *how do you resolve the float64 going up by 12,054, and why isn't that
a regression?*

## The gap

The raw-float64 ratchet's default root is `computations/`, so `qou-mass/src`
had **never been scanned by anything**. 129 witnesses / **44,937 raw float64
fields** shipped unobserved.

## The drain is ONE producer, and it fixes both trees

    43,901  canonical_isotope_witness.py   <- 97.7 %
       277  adjacent_vs_full_probe.py
       273  canonical_tower.py
       208  mass_tower_operator_valued.py
       120  sublemma_2_1_deuteron_branching.py
        90  brane_tower_isospin_diagnosis.py

Not a 45k-field sweep. And the **same 43,901 fields** sit in the 119
`computations/canonical-isotope-witness-Z*.json` that producer also writes, so
fixing it at source (carry `mpmath.mpf`, serialize with `_precision.fmt`)
drains **both** trees: `computations/` directly, and the package automatically
on the next `sync-qou-mass-vendor.py --apply` — which only works because #5431
put the package data under the sync. Before that, a corpus drain would have left
the package stale.

Needs a re-run across Z00–Z96, so it is **long-compute with a teed log**, not an
idle-pass job. Not started.

## Done here: hold the line

Established a baseline (129 / 44,937) and wired
`--scan-root qou-mass/src --strict` **blocking** into `precision-gates.sh`.

**This is coverage, not laundering, and the distinction is the whole point.**
This repo's rule — *never make a red run green by widening a baseline* — governs
SILENCING AN EXISTING GATE. There was no gate. Establishing a ratchet where none
existed is the opposite act: from here the count can only shrink.

Shown to fire on **both** failure modes, which is what makes it a ratchet rather
than a rug:

    A  backlog of 44,937 tolerated                          exit 0
    B  count increase in a baselined file (58 -> 59)  REGRESSED, exit 1
    C  brand-new dirty witness in the package              NEW, exit 1
    D  restored                                                exit 0

## Also fixed

`drain_owner` hardcoded `bean qou-irzg` for every non-default root — it was
written for the audits tree and was stamping that id onto the qou-mass baseline,
sending the next agent to the wrong arc. Now points at the per-root gate entry in
`precision-gates.sh`.


---

## DRAIN DONE — 43,901 -> 0 (commit 921a5304f3d, PR #5453)

`_as_mpf(x) = mp.mpf(str(x))` (**not** `mpf(x)`), mpmath arithmetic throughout,
`_precision.fmt` on every emit. Removed `float(U_MEV)` / `float(M_E_MEV)` at
four sites — those constants arrive from the registry as ~70-digit mpf and were
being cast back to doubles.

    computations/ isotope witnesses   119 / 43,901  ->  0 / 0
    corpus ratchet                    529,087 -> 488,300 fields
    qou-mass/src (one --apply)         44,937 -> 1,036, 129 -> 10 files

The qou-mass half cost **one command** — the propagation #5431 built.

### The values moved, and that IS the result

52 of 54,533 fields moved beyond 1e-15, and **every one is an error/difference
field**; **zero** primary quantities moved. Catastrophic cancellation: these
subtract two near-equal ~940 MeV numbers, so a 1e-16 float64 input becomes
~1e-8 in the difference. Largest correction **9.29e-08** relative. The old
numbers were wrong.

### Two corrections to my own claims

1. **"Long-compute, needs a wall-time go-ahead"** — WRONG. **43 seconds** for
   all 119 shards. I inferred cost from "Z00-Z96 re-run" without measuring.
2. **`--max-z` defaults to 20**, so my first full-looking run silently left 98
   shards dirty and the drain read as 7% complete. Caught by re-measuring, not
   by the run's success message.

### Method note worth keeping

I compared **old code vs new code on the same data**, not against the committed
witnesses. The committed Z01 differed from the old code's own current output at
the 9th digit — it was already stale — so comparing against it would have
attributed an upstream staleness to my change.

### Left for its owner

Upstream L1 `prediction_MeV_50dps` (`canonical-mass-table-extended`) is a
49-place string with a **dyadic tail** — it came from binary floating point, so
its "50dps" is nominal. Carried faithfully now instead of truncated; fixing the
origin is that arc's.

### Remaining here

1,036 fields across 10 files in qou-mass, long tail:
`adjacent_vs_full_probe` 277, `canonical_tower` 273,
`mass_tower_operator_valued` 208, `sublemma_2_1_deuteron_branching` 120,
`brane_tower_isospin_diagnosis` 90. Same recipe, much smaller.
