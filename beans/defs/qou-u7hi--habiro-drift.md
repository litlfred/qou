---
# qou-u7hi
title: Habiro drift
status: completed
type: task
tags:
    - reorg-2026-10-04
created_at: 2026-10-04T15:10:21Z
updated_at: 2026-10-10T08:30:00Z
parent: qou-avtq
---

Extracted 2026-10-04 from the prose of session log `qou-9ot5` (work had no bean).


## 2026-10-10 — evidence re-check (verification sweep of `qou-avtq`)

**Verdict: DONE.** The drift was the convention-C→D regeneration of habiro-coefficients-atomic (2026-09-06). The committed witness now matches it and reproduces. The one remaining defect is the hard-coded "507 % and 362 %" string in qbeta_habiro_pochhammer_convention_probe.py, which should be computed rather than quoted.

Evidence: The drift is the 45–52 % move in `qbeta/qbeta-habiro-pochhammer-convention.witness.json` reported in `qou-9ot5`. The committed witness (computedAt 2026-09-07) now carries p = 0.6293284022029219…, n = 0.4751335171556822…. This equals today's `habiro/habiro-coefficients-atomic.witness.json` (regenerated 2026-09-06 on the convention-D peel route) evaluated at q₀ (I computed p = 0.62932840220292191816). The old 1.14575969… was the pre-regeneration value. Probe re-run: exit 0, payload unchanged. Residual: the probe prints hard-coded "507 % and 362 %" next to computed 359.6 % / 201.5 %.

Status: `todo` → `completed`.
Checked against qou `main` at `77695711d2`. Probes were re-run only where cheap and decisive. A numeric result counts as evidence only where it reproduces and its precision exceeds the gap it decides; convention-C numbers are not evidence about convention-D claims.
