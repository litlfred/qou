---
# qou-q86o
title: 'GAP: saddle offset ''origin-centred only at q=1'' leg untested — certified DT Stokes series diverge at q=1'
status: todo
type: task
created_at: 2026-08-02T13:46:14Z
updated_at: 2026-08-02T13:46:14Z
---

## Context

Saddle-offset probe (#4578, `computations/probes/saddle_offset_fourone_fivetwo_probe.py`;
audit `docs/audits/2026-08-02-saddle-offset-fourone-fivetwo-probe.md`) CONFIRMED the
DT-limit legs of the owner's saddle-vector picture: the ι-odd offset
`o(q)=c⁺(q)−c⁻(q)` has q→0 value **1** for chiral 5₂ (the `{3,4}` datum) and **0**
for amphichiral 4₁ (matches the Lean gate #4577, `offset = 0 ⇔ ι-fixed`).

## The gap

The *specific* leg "the saddle is origin-centred **only** at q=1" is **untested /
unsupported** by the certified data:

1. The certified Stokes series (`qbeta_g3_5two_stokes_sandwich.py`) are Taylor
   series around q→0; the `(q;q)`-type factors **diverge at q=1**, so `o(q)` cannot
   be evaluated there.
2. Within the convergent radius the offset `o(q) = 1 − 9q − 28q² + …` **crosses zero
   at a small finite q ≈ 0.08** (not q=1), arguing *against* the q=1 placement.

So "ι-fixed locus = q=1" is a modelling convention (correctly flagged scope-(a) in
#4577), not something the DT-anchored Stokes data establish.

## What was attempted / why it failed

- Direct evaluation at q=1: divergence (out of series domain).
- Reading the q→0-anchored `o(q)` as the offset: gives the correct DT datum but is a
  cross-chirality difference (leading `1 ≠ 0`), not an ι-covariant object that must
  vanish at q=1.

## Next honest step (surviving candidates)

- A representation of `S±(q)` valid near `|q|=1` (two-sided / Borel-resummed /
  modular-completed), so the offset can actually be continued to the ι-fixed point.
- OR recast the offset as a genuinely ι-covariant object `o(q) = f(q) − f(q⁻¹)`
  whose q=1 vanishing is structural — then check whether its q→0 expansion still
  reproduces the `{3,4}` datum. Neither is available from the current q→0 sandwich.

Refute-friendly: if no ι-covariant object valid at q=1 reproduces the `{3,4}` datum,
the honest verdict is that the DT offset lives at q→0, not q=1 — a scope-(a)
narrowing of the picture, not a structural exclusion.

