---
# qou-4kr1
title: 'The hypersensitivity crux: where does slope k≈2.2e6 (S vs ~1e-8 anchor gap) come from geometrically? resonance/near-degeneracy? — the open frontier, no fit'
status: completed
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-07-27T02:54:47Z
updated_at: 2026-10-10T08:30:00Z
parent: qou-avtq
---


## 2026-10-10 — evidence re-check (verification sweep of `qou-avtq`)

**Verdict: CLOSED-REFUTED.** The slope is not geometric. It is the O(1) log-derivative of the smooth N=2 ladder prediction times the extractor's 1/u³ ≈ 1.6e6 (dc3/dq = 3.838e6 reproduced to 3e-5 from c3_target_at). Any "resonance" search is explaining the inversion's amplification.

Evidence: `dc3/dq = 3.83841e6` equals `-(d ln Q_N2/dq)/u³ = 3.83831e6` to 3e-5 (mpmath 60 dps, `qbeta/qbeta_utils.c3_target_at`). `d ln Q_N2/dq = -2.37`, `1/u³ = 1.618e6`. This follows from the definition `c3=(Q_codata/Q_N2−1)/u³`.

Status: `todo` → `completed`.
Checked against qou `main` at `77695711d2`. Probes were re-run only where cheap and decisive. A numeric result counts as evidence only where it reproduces and its precision exceeds the gap it decides; convention-C numbers are not evidence about convention-D claims.
