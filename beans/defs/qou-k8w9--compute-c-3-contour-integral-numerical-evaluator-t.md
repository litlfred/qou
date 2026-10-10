---
# qou-k8w9
title: Compute c_3 contour integral numerical evaluator to arbitrary dps
status: scrapped
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-07-07T19:12:42Z
updated_at: 2026-10-10T08:30:00Z
parent: qou-avtq
---


## 2026-10-10 — evidence re-check (verification sweep of `qou-avtq`)

**Verdict: SUPERSEDED.** The Φ_b evaluator it asked for exists (phi_b_evaluator.py, precision set by mp.dps). The c_3 route it was meant to serve is closed at the substrate by ModularDoubleReciprocity (qou-dvlt option B). Scrap.

Evidence: Empty body. The evaluator exists: `computations/qbeta/phi_b_evaluator.py` (contour quadrature with dps-scaled truncation, L66-97, plus the modular-double product, validated 10/10 per the lean-route memo). c_3 is not the output of any contour integral: it is extracted from Q_β. The Φ_b-carrier route to c_3 at the substrate is closed by `ModularDoubleReciprocity.lean` (qou-dvlt option B).

Status: `todo` → `scrapped`.
Checked against qou `main` at `77695711d2`. Probes were re-run only where cheap and decisive. A numeric result counts as evidence only where it reproduces and its precision exceeds the gap it decides; convention-C numbers are not evidence about convention-D claims.
