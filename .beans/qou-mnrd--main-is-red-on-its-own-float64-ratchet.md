---
# qou-mnrd
title: 'origin/main is RED on its own raw-float64 ratchet — three witnesses landed undrained'
status: todo
type: task
priority: high
tags:
    - ci
    - precision
    - no-float64
    - ratchet
    - coordination
created_at: 2026-08-08T22:45:00Z
updated_at: 2026-08-08T22:45:00Z
---

## The finding

`computations/witness_raw_float64_audit.py --strict` **exits 1 on `origin/main`**
(9d6fa7f2c, 2026-08-08). Three witnesses carry raw float64 and are not in
`computations/raw-float64-baseline.json`:

     16  computations/qbeta/qborel-growth-budget-probe.witness.json
     15  computations/qbeta/cauchymul-order-cancellation-witness.witness.json
      4  computations/qbeta/c3-w2-c1-pole-divisor.witness.json

Landed by, respectively, `6cd4f9567` (plan+beans(W2)), `a62c65204`
(probe(qou-6e88)), `54c41e4cd` (compute+lean(qou-wgnx)) — three different
sibling sessions.

## How it was found, and why that matters

Surfaced by `/prepare-merge` on `claude/drain-float64-ratchet`: the ratchet was
0 NEW / 0 REGRESSED for the whole of that branch's work, and went to 3 NEW the
moment `origin/main` was merged in. Confirmed as inherited, not merge damage:

  * all three files exist on `origin/main` (`git cat-file -e origin/main:<f>`);
  * `raw-float64-baseline.json` is byte-identical between `origin/main` and the
    merged branch, so the merge did not weaken the baseline;
  * none of the three appears in that baseline.

So `main` fails its own gate. **This is exactly the leak the ratchet exists to
stop** — see the audit's own motivating example, `jpsi-boundstate-mass.witness.json`
reaching `main` with 30 raw float64 fields while the padding audit stayed green.
The ratchet caught it this time; nothing enforced the catch.

## Do not fix it the easy way

The audit says so in its own output: *"fix AT THE PRODUCER (carry mpmath.mpf
from the source, serialize with `_precision.fmt`), then re-run it. Do NOT add
the file to the baseline to silence this."* Adding three lines to the baseline
would close the bean and defeat the mechanism.

## What to do

1. Fix each at its producer. `jpsi_boundstate_mass_probe.py` is the worked
   conversion the audit points to, including the case where a library has its
   own precision ceiling that must be recorded rather than assumed.
2. Separately: **why did these land?** The ratchet is a script, not a required
   check. If it is not wired into CI as blocking, three more will land next
   week. That wiring is the durable fix and is the more important half of this
   bean.

## Not claimed here

This branch does not fix them. They are other sessions' witnesses and draining
them is their arc's work, not this one's. Recorded so that
`claude/drain-float64-ratchet` is not read as having regressed the gate it is
named after — it did not; it inherited a red main.
