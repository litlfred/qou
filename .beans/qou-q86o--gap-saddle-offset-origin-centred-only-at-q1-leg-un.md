---
# qou-q86o
title: 'GAP: saddle offset ''origin-centred only at q=1'' leg untested — certified DT Stokes series diverge at q=1'
status: in-progress
type: task
priority: normal
created_at: 2026-08-02T13:46:14Z
updated_at: 2026-08-02T14:34:11Z
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

## Update 2026-08-02 (#4583 — archimedean leg ANSWERED; fibre leg remains open)

Probe [`saddle_offset_zero_location_probe.py`](../computations/probes/saddle_offset_zero_location_probe.py)
+ Lean [`SaddleOffsetBarGrade.lean`](../content/quantum-observable-universe/lean/QOU/QBeta/SaddleOffsetBarGrade.lean)
(sorry-free) + audit [`2026-08-02-saddle-offset-zero-location-qou-q86o.md`](../docs/audits/2026-08-02-saddle-offset-zero-location-qou-q86o.md).

- **What is q≈0.08?** q\* = **0.08931**, truncation-STABLE (converges by N=6,
  spread 7e-4), pinned by the quadratic balance `1−9q−28q²=0` ⇒ `(−9+√193)/56`.
  It is **NOT a substrate quantity** (misses q₀−1, ℏ_q, ℏ_q², 1/q₀, radius all
  by ≫1%; closest ℏ_q at ~10%). It is the DT series' **own** convergence-region
  root, set by the low-order Stokes coeffs {9,28}. → honest negative.
- **Does q=1 survive?** As an *independent DT placement*, **NO** [scope-(a)
  refutation, Lean-backed]: the certified `o(q)=c⁺−c⁻` has `o(0)=1≠0`, so it is
  a cross-chirality difference, NOT a bar-covariant `f(q)−f(q⁻¹)`; its q=1
  vanishing is only the *trivial* bar-fixed-point vanishing (#4577's gate applied
  to q), a different object. `barAntisym_const_zero` +
  `certified_offset_not_barAntisym` prove this.
- **c₃ hook?** **Absent.** Offset diverges at q₀ (inaccessible); structurally the
  offset is built from the **resummed** Stokes constants (geometric growth,
  radius ~0.6), whereas c₃ is a coefficient of the **divergent** Φ_5₂
  (Fantini-Wheeler Borel domain) — opposite sides of the Borel transform, no
  identity. Nothing fitted, nothing wired.

**Still OPEN (re-scoped, NOT closed):** the **fibre-level** reading — the owner's
"centred at q=1" as the bar-fixed point of the *formal* q, where a bar-covariant
Habiro/fibre element vanishes by construction (AGENTS.md Im(q) banner). The q→0
DT series neither tests nor refutes this; it is a *different object*. Next honest
step: exhibit (or refute) a fibre-level Habiro element whose bar-odd part vanishes
at q=1 AND whose q→0 archimedean evaluation reproduces the `{3,4}` datum — the
route to the QBeta c₃ Borel/Habiro program, not the archimedean sandwich.
