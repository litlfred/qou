---
# z2bn
title: 'Lever 1 [FOCUS]: derive/test fibre q-difference kernel R(q,x) for binding genfun; kill-switch = magic-A ⁴He +5.87%'
status: in-progress
type: task
priority: normal
created_at: 2026-06-23T14:19:27Z
updated_at: 2026-06-23T14:39:13Z
---


## Coordination breadcrumb (2026-06-24) — ⁴He binding falsification thread

Empirical input for the R(q,x) derivation + the magic-A ⁴He kill-switch, from the
merged binding thread (PRs #2630/#2681/#2703):

- **B_joint^model (|χ| joint trace) is nearly A-INDEPENDENT**: ³H 3.25 → ³He 3.47 →
  ⁴He 3.80 MeV, while B_AME explodes (8.48 / 7.72 / 28.30). ⁴He captures only **13%**
  of its binding. The multiplicative deficit `1−∏f` **saturates**
  (`productModel_3body_nonpos`).
- **Implication for R(q,x):** its solution **must grow with A** (the `Iν` q-Bessel
  growth regime). A saturating/intensive trace object cannot source the extensive
  binding — that is the dominant gap, bigger than any phase/sign correction.
- The q-Reeb phase `|Δθ_λ|` is only a **directional** correlate (the constant-scale
  `0.206 MeV/rad` relation was falsified at ⁴He, +69%), not the magnitude source.

Witnesses: `he4-qreeb-phase-falsification.witness.json`,
`yardstick-free-phase-binding.witness.json`.
Audit: `docs/audits/2026-06-24-he4-qreeb-phase-falsification.md`.
