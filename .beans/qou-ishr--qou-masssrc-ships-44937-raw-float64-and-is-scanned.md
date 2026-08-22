---
# qou-ishr
title: qou-mass/src ships 44,937 raw float64 and is scanned by no ratchet — 97.7% from one producer
status: in-progress
type: task
priority: normal
created_at: 2026-08-22T15:22:10Z
updated_at: 2026-08-22T15:28:03Z
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
