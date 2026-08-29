---
# qou-879g
title: 'DECIDE: does the convention-D decay channel live in H_3(q) or its TL quotient?'
status: completed
type: task
priority: normal
created_at: 2026-08-26T21:07:16Z
updated_at: 2026-08-26T21:31:16Z
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


## ANSWERED 2026-08-26 — Temperley-Lieb, and the corpus already said so

**The bean was premature.** I opened it as an owner decision without running the
four-path corpus grep first. The grep finds
[`prf:algebraic-gns-embedding`](content/quantum-observable-universe/observations/algebraic-gns-embedding-proof.md),
which states it verbatim:

> *"Under the production convention D this ideal is **not** trivial: `tr_M = Σ_λ
> y_λ χ^λ` with `y_λ = 0` exactly when `ℓ(λ) ≥ 3`, so `N` is the sum of those
> Wedderburn blocks — **the Temperley–Lieb radical** — and the GNS space is the
> Temperley–Lieb quotient `H_∞(q)/rad ≅ TL_∞(q)`, **not** `H_∞(q)` itself.
> (Under the excised convention C every `y_λ` was non-zero and `N` collapsed to
> 0.)"*

Verified at n=3 (`qbeta_which_algebra_the_decay_channel_lives_in_probe.py`,
11/11): the trace annihilates the `(1³)` ideal under D and does **not** under C,
exactly as that parenthetical says.

## The answer is not a label — it breaks the Q_β functional

Descent to a quotient **is** annihilation of the ideal. Measured:

| functional | annihilates `J_(1³)` ? | descends to TL? |
|---|---|---|
| `tr_M` at `z_D` | yes | **yes** |
| augmentation `σ ↦ q` | yes | **yes** |
| `net`, the coordinate sum | **no** — `net(e) = q³(q−1)/((q²+1)(q²+q+1))` | **NO** |

Δ has a nonzero `(1³)` component, so `epsNPq` takes **different values on two
representatives of one TL class**. The Q_β ansatz evaluates a functional that is
not defined on the space the framework's own GNS proof places the theory in —
and it *would* be defined there if it were the counit the corpus calls it.

**So step 8's mislabelling is the obstruction, not a naming quibble.** Recorded
onward on `qou-99qc`, the owner-call bean that asks which ε is meant.

This also retires the interpretive flag on
`qbeta_d_frame_tl_quotient_phase_probe.py`: the quotient reading is what the
corpus says, but evaluating `net` on the canonical lift is a *choice of
representative*, not a well-defined evaluation on TL. That number
(0.01268105) should be read as "net of the canonical lift", not "the TL value".
