---
# qou-obmp
title: 'GAP: residual channel-dependent Pade bias plateau (~0.27%) in V3 extraction'
status: in-progress
pr: 8210
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-03T14:28:58Z
updated_at: 2026-10-04T15:20:22Z
parent: qou-r9ih
---


## What is open

Control-channel calibration of the Borel–Padé pole map improves the `V₃`
extraction 3.7× (rel dev 0.0098 → 0.0027) and then **plateaus**. It does not
converge to zero. A residual *channel-dependent* component of the Padé bias
survives calibration, and is unexplained.

## Established

- **The bias is not truncation.** Orders [10/11]→[11/12] move `V₃` by 1.5e-5
  while the offset from the published value is 6.6e-3 — 440× larger.
- **It follows the classical 1/n² branch-cut law**: `(k₁₂−1)·n²` stays O(1)
  with no trend across seven orders. A resurgent Borel transform has a *branch
  point*; Padé renders a cut as a line of poles whose leading pole sits
  systematically outside it.
- **Both channels carry it** with the same sign and comparable size at every
  clean order.

## Retracted — do not cite

An earlier revision claimed the two channels "agree to 4.7e-6". That figure is
real but comes from `[11/12]` **alone** and is ~1000× better than typical. The
worst clean-order disagreement is `4.8e-3` in `|Δk|/k` (~14 % in the bias
`k−1` itself, at [8/9]). The **plateau** is the honest measure of what
calibration achieves.

## Why it matters

It bounds how well `V₃` (or any Stokes constant) can be read off a Padé pole
map at these orders: expect a systematic ~1–5 % radial overshoot, not
machine-precision agreement. Anyone matching pole locations to predicted
Stokes points needs this.

## Next step

Either (a) a theory of the channel-dependent residual — the two channels have
different singularity exponents and distances, which is the obvious suspect —
or (b) a different extraction that avoids Padé's branch-point bias entirely
(conformal mapping / uniformization of the Borel plane before approximation).

## Refs

- probe: `computations/probes/qbeta_5two_v3_from_borel_poles_probe.py` (D1)
- ledger: `docs/coordination/1ppq-qbeta.md`, 2026-08-01 rows
- PR #4454

## Progress Note (2026-11-16, PR #8210)
- Formalized in `folio/quantum-observable-universe/lean/QOU/QBeta/CompactQuantumDilogAndSaddleOffset.lean` (wired into `QOU.lean`, `0` `sorry`, `0` `axiom`, `0 CRITICAL / 0 advisory` across all 8 Lean static vacuity/borrowed-name audits).
- Verified by 80-dps `mpmath` / exact rational probe `computations/probes/compact_quantum_dilog_and_saddle_offset_probe.py` and witness `computations/probes/compact-quantum-dilog-and-saddle-offset.witness.json` (`scriptCommitSha: 4755c87e9f5eee61dab667d125dbf7cba1a93d8b`, `allPassed: true`, `0` raw `float64` fields).
- PR: https://github.com/litlfred/qou/pull/8210 (`539652a881d79d302fbe60283d4f961bd748a742`).
