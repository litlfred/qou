---
# qou-0yqu
title: 'GAP: prove the 5₂ saddle sum rule Σ_j Re V_j = -3π²/2'
status: todo
type: task
created_at: 2026-08-03T14:28:26Z
updated_at: 2026-08-03T14:28:26Z
---


## What is open

The three 5₂ saddle values satisfy

    Σⱼ Re(Vⱼ) = −3π²/2        (SUM)

with `Vⱼ = 3·Li₂(yⱼ) + (log yⱼ + bⱼπi)²`, `yⱼ` the roots of `y³−2y²+3y−1`,
`b = (−1,+1,+1)`. **Verified to 80 dps (residual 3.4e-80). NOT PROVED.**

Equivalently `V₃ = −2·Re(V₁) − 3π²/2`, and in `V^ext = V + π²/2` it reads
`Σⱼ Vⱼ^ext = 0` — i.e. `π²/2` is the unique *centering* shift, which is why
that convention exists at all.

## Why it matters

It is what makes the corpus's `V₃` literal unnecessary: `V₃` is determined by
`V₁`. Carrying it independently is how a wrong value (`−2.7580990292`) went
unnoticed for months.

## Established, do not redo

- **Specific to 5₂**, not branch bookkeeping: five control cubics of the same
  shape — four sharing the `Πy = 1` constraint — miss the target by 0.16 to
  2.83 while 5₂ hits to 2e-50. So it is an arithmetic property of the 5₂
  saddle cubic (Bloch-group / dilogarithm-ladder shaped).
- **Branch data is exact**: `2 log yⱼ − 3 log(1−yⱼ) = 2πi·εⱼ` with
  `ε = (+1,−1,0)`. This is where the `π²` comes from.
- **One relation is derived** (and Lean-proved, see below). Summing the
  reflection identity over the roots:

      A + B = π²/2 − (2/3)·Σ(log yⱼ)² + (2πi/3)·Σ εⱼ log yⱼ

  with `A = ΣLi₂(yⱼ)`, `B = ΣLi₂(1−yⱼ)`.

## Why it does not close

One equation, two unknowns. `A ≈ 0.9717306815`, `B ≈ 0.3514640301`, neither
with an evident closed form (`B/A = 0.36169`, `B−A = −0.62027`).

## Next honest step

The Kubert/distribution relation `Li₂(zⁿ) = n·Σ_{k<n} Li₂(ζₙᵏ z)` applied to
`Li₂(y²) = Li₂((1−y)³)` supplies the second relation, at the cost of
cube-root-of-unity arguments `ω(1−y)`. Bloch-group computation; not attempted.

## Lean status

`QOU/QBeta/FiveTwoSaddleSumRule.lean` (lean-direct exit 0, sorry-free) proves
the algebraic skeleton, the reflection reduction (with `Li` abstract, the
reflection identity as an explicit hypothesis), and the two bookkeeping
consequences. **Mathlib has no polylogarithm** (checked 2026-08-03: no
`Polylog`, no `dilog`), so (SUM) itself cannot be stated against a Mathlib
`Li₂`. It is recorded as the content-bearing conjecture carrier
`FiveTwoSaddleSumRule` with **no instance**, and the missing input as
`FiveTwoDilogLadder`.

Formalizing the Kubert relation needs a Mathlib dilogarithm first — that is
the real blocker on the Lean side.

## Refs

- probe: `computations/probes/qbeta_5two_saddle_sum_rule_and_provenance_probe.py`
- ledger: `docs/coordination/1ppq-qbeta.md`, 2026-08-02 row
- PR #4624
