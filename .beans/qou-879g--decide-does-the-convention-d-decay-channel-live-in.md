---
# qou-879g
title: 'DECIDE: does the convention-D decay channel live in H_3(q) or its TL quotient?'
status: todo
type: task
priority: normal
created_at: 2026-08-26T21:07:16Z
updated_at: 2026-08-26T21:08:07Z
---

Opened from `qou-cds1`, on owner instruction to bean-and-queue anything arising.

## The decision

`WenzlWeightVanishing.lean` proves `z_D` is Wenzl level `r = 2` exactly, so the
≥ 3-row blocks are annihilated. The corpus establishes this for the **trace's
support**: `y_(1³) = 0` under convention D, now by four independent routes.

It does **not** establish what the ≥ 3-row annihilation means for the **element**.
Two readings:

1. **Weight reading** — `H_3(q)` is the algebra; the D trace simply has zero
   weight on `(1³)`. The decay element stays in `H_3(q)`.
2. **Quotient reading** — the D-frame theory lives in `H_3(q)/J_(1³)`, the
   Temperley–Lieb quotient; the decay element is `π(Δ)`.

## Why it is not academic — it is worth 1.43× on the best D candidate

The two readings agree for every **trace** (the projection is invisible to
`tr_M^D`, since `y_(1³)` already annihilated that block). They differ for `net`,
which is **not** a trace and does not respect the block ideal. So the
counit-minus-trace gap — hence the ladder phase `α = (ε − tr_M)/2` — moves.

Measured (`computations/qbeta/qbeta_d_frame_tl_quotient_phase_probe.py`, 17/17),
as relative distance of the implied `z_eff` to the anchor-inverted `z*`:

| candidate | \|Δz\|/z* |
|---|---|
| C (as recorded) | 0.00043244 |
| D naive z-swap (banned) | 0.22757466 |
| D naive + bar-odd | 0.01813926 |
| **D quotient + bar-odd** | **0.01268105** |

The central idempotent is unique, so `π(Δ)` carries **no free parameter** — this
is a determined consequence of reading 2, not a tuned one.

## What deciding it needs

A corpus or owner call on whether the D-frame decay channel is `H_3(q)` or its
TL quotient. Not a number to search for: the number is already computed under
each reading. Until it is decided, `qou-cds1`'s best D candidate carries an
interpretive step flagged as such in the probe docstring.
