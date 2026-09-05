# The chain closes end-to-end — and the majorant route structurally cannot carry the size

**Date:** 2026-09-05 · **Bean:** `qou-o6ov` · **Scope:** (a) scope-limited — complete n=9 census. Nothing wired, no witness, no fit.

## What was composed

Every link of this arc existed but had never been composed and checked against the quantity the
bean is actually about — the **signed** trace `tr_λ(ρ·Ω₂^P)`. Each was verified in isolation, on a
different and usually dim-capped sample:

```
|tr_λ(ρ·Ω₂^P)| ≤ Σ|eig(M_λ)| ≤ √(dim_λ·tr_λ(X*X)) ≤ dim_λ·√(E(b(λ)))
```

with `E(b) = max_{b(λ)=b} tr_λ(X*X)/dim_λ` strictly decreasing over all seven complete levels
(#6729). Composing: `|tr_λ|/dim_λ ≤ √(E(b(λ)))`.

Both links **hold on every one of the 30 shapes**, and the composed bound is strictly decreasing:

```
b=1  68.6922 > b=2 58.977 > b=3 40.8807 > b=4 31.3242 > b=5 24.6086 > b=6 14.5453 > b=7 5.6175
```

That is the arc's target reached: a *derived*, per-dimension bound on the original signed trace that
falls with `b`. **And it is much less than it sounds.**

## The tightness, which is the actual result

| | b=1 | b=7 | falls by |
|---|---|---|---|
| composed bound `√E(b)` | 68.69 | 5.62 | **12.2×** |
| actual `|tr|/dim` envelope | 33.65 | 0.178 | **189×** |
| actual worst-case shape | 33.65 | 0.0142 (at b=6) | 2360× |

**The bound captures 12× of a 189× effect.** Worse, its looseness is not uniform — it grows exactly
where the decay matters:

| link | best case | worst case |
|---|---|---|
| 1 — spectrum → Frobenius | 2.041× at `(8,1)`, b=1 | **550.2×** at `(3,2,1⁴)`, b=6 |
| 2 — shape → level envelope | 1.0× | 8.513× |

Link 2 is fine: replacing a shape by its level maximum costs at most 8.5×, which is the price of
wanting a bound in `b` alone. **Link 1 is where the bound dies.** At `(3,2,1,1,1,1)` the true
`|tr|/dim` is 0.0142 against a bound of 7.84.

## What that means, and it is a correction to this arc's strategy

Link 1 is `|tr X| ≤ √(dim·‖X‖_F²)` — it replaces the signed trace by a norm, discarding every
cancellation among the eigenvalues. The measurement says that discarded cancellation is **the
dominant part of the effect at large `b`**, and that it *grows* with `b`. So the majorant route —
the strategy since #6556 — establishes the **shape** of the decay and structurally cannot carry its
**size**.

**This refines, and partly corrects, my own framing in #6556.** That PR compared conjugate pairs and
found the majorant `‖M_λ‖_F²` itself decaying 213× against only 1.4× in the input norm, and I wrote
that the decay is *"overwhelmingly output-spectrum collapse, not phase cancellation"*. The first half
stands — the majorant genuinely decays hard (`E` falls 149× per-dimension across the levels). What
was overstated is the dismissal of the second: there **is** substantial trace-level cancellation on
top of it, reaching 550×. The two measurements are not in conflict — #6556 compared a majorant
between conjugates, this compares a signed trace against its own majorant — but "overwhelmingly"
was too strong, and this is the first time the signed trace has been set against its own majorant
across a complete census, which is why the second effect only becomes visible now.

## What this does and does not settle

- **Settles:** the decay in `b` is real for the signed trace, derived rather than measured, and
  monotone on complete data. Nothing in the chain is a fit.
- **Does not settle:** any quantitative claim. A bound loose by 550× cannot support a numerical
  statement about the row-truncation error, which is what the bean wants it for.
- **Redirects:** a quantitatively useful bound must keep the sign information — the route through
  `‖X‖_F` cannot be repaired by tightening links 2 or 3, because link 1 alone accounts for the loss.

## Method notes worth keeping

- `tr` and `‖X‖_F²` are computed **together** from the same `X e_j` in one column-wise sweep, so
  they are guaranteed to describe the same matrix. Taking them from two passes would let a
  discrepancy hide as a mismatch between runs.
- **No eigenvalues are needed:** `|tr X| ≤ Σ|eig X| ≤ √(dim·‖X‖_F²)` lets the middle term be
  bypassed, which is what makes every shape up to dim 216 affordable.
- `E(b)` is **recomputed** in the same run, not quoted from #6729 — a chain check that quotes its
  own inputs is re-checking arithmetic it already did.
- The inequalities are theorems, so the ✓ marks test the **arithmetic**, not the mathematics. A
  failure would have meant the kernel or the envelope was wrong. The tightness columns are the part
  that carries information.

## Limits

- Complete n=9 census only. The tightness figures are for this `n` and this atom word.
- The two exact-zero endpoints (`b=0`, `b=n−1`) report infinite slack trivially and are excluded.
- Nothing here is proved for general `n`.
