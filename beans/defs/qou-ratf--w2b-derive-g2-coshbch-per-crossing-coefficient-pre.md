---
# qou-ratf
title: 'W2b: derive g2 — cosh/BCH per-crossing coefficient prediction + 0.87% residual parity puzzle + Bonatsos q-rotor lit verification'
status: in-progress
pr: 8204
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-07-24T21:10:06Z
updated_at: 2026-10-04T15:25:29Z
parent: qou-frzo
---

## Progress Note (2026-11-16, PR #8204)
- Formalized in `folio/quantum-observable-universe/lean/QOU/MassTheory/QGevreyCauchyAndFWGGMStokes.lean` (wired into `QOU.lean`, `0` `sorry`, `0` `axiom`, `0 CRITICAL / 0 advisory` across all 8 Lean static vacuity/borrowed-name audits).
- Verified by 80-dps `mpmath` / exact rational probe `computations/probes/qgevrey_cauchy_and_fw_ggm_stokes_probe.py` and witness `computations/probes/qgevrey-cauchy-and-fw-ggm-stokes.witness.json` (`scriptCommitSha: 8ee650e779786706f931cf4f825d18b2810370eb`, `scriptHash: 7ed9e0953101`, `allPassed: true`, `0` raw `float64` fields).
- PR: https://github.com/litlfred/qou/pull/8204 (`6b9e46ecf45f518a03c0a6fb1de251bf59b285da`).
