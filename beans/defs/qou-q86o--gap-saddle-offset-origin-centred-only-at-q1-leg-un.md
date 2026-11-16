---
# qou-q86o
title: 'GAP: saddle offset ''origin-centred only at q=1'' leg untested — certified DT Stokes series diverge at q=1'
status: in-progress
pr: 8210
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-02T13:46:14Z
updated_at: 2026-10-04T15:12:59Z
parent: qou-r9ih
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
+ Lean [`SaddleOffsetBarGrade.lean`](../folio/quantum-observable-universe/lean/QOU/QBeta/SaddleOffsetBarGrade.lean)
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

## VERDICT (2026-08-02, PR #4587 — fibre leg ANSWERED)

Surviving FIBRE-level leg (bar-odd Habiro element whose bar-fixed coefficient degree n=0 is forced zero — the fibre reading of "centred at q=1"; evaluation at q=±1 is a distinct statement) is NOT a derivation — HONEST NEGATIVE, a vacuous-or-fit dichotomy on 4 proved pillars:
1. q=1 centring is NON-SELECTIVE (new sorry-free Lean BarOddQOneCentringNonselective.lean): involution's only fixed coeff-degree is n=0, so bar-odd vanishes there for the WHOLE class. q1_centring_nonselective: BarAntisym g iff (BarAntisym g and g0=0). Imposing "centred at q=1" selects no element => content-free (vacuous horn).
2. {3,4} DT datum (chiralityOdd 4 3=1) incompatible with bar-odd fixed-degree coeff (#4583) => reproducing it needs FREE root-of-unity interpolation = a fit (fit horn).
3. {3,4} is q-EXACT, no resurgent tail (#4554 symmetryConstant_const) => driver-11/13 q->0 DT count, NOT a Habiro object.
4. Substrate wall (HabiroMagnitudeA3 pochAbs_unbounded, non-summable at q0>1) + bar-odd resummation anchor-blind (#4519).
Scope-(a); nothing wired. Audit: docs/audits/2026-08-02-fibre-habiro-q1-centring-verdict.md. alpha_EM precedent does not transfer (bar-EVEN/finite/fixed). Only live neighbour = DT-count categorification (q->0). Left open for owner to close.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-08-02 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

## Progress Note (2026-11-16, PR #8210)
- Formalized in `folio/quantum-observable-universe/lean/QOU/QBeta/CompactQuantumDilogAndSaddleOffset.lean` (wired into `QOU.lean`, `0` `sorry`, `0` `axiom`, `0 CRITICAL / 0 advisory` across all 8 Lean static vacuity/borrowed-name audits).
- Verified by 80-dps `mpmath` / exact rational probe `computations/probes/compact_quantum_dilog_and_saddle_offset_probe.py` and witness `computations/probes/compact-quantum-dilog-and-saddle-offset.witness.json` (`scriptCommitSha: 4755c87e9f5eee61dab667d125dbf7cba1a93d8b`, `allPassed: true`, `0` raw `float64` fields).
- PR: https://github.com/litlfred/qou/pull/8210 (`539652a881d79d302fbe60283d4f961bd748a742`).
