---
# qou-mogm
title: 'CONVERGENCE: main''s imV41 leading form IS my Route-1 S_K shape. FigureEightComplexVolume.lean now proves Im V41(u) = cuspModulus*(Re^2 u - Im^2 u) with the SAME cuspModulus = sqrt3/4, and imV41_le_cuspModulus_reSq (spin only subtracts) sorry-free. My S_K = A_omega*cuspModulus*(ln^2 q0 - theta^2) is that form with Re u = ln q0, Im u = theta, plus the A_omega=3 Stokes factor. So the shape I was testing empirically is a PROVED leading form. Re-scope the Route-1 witness: promote the shape from hypothesis to proved, and keep only the theta_3 normalisation + the A-dependence as open.'
status: scrapped
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-07T15:04:34Z
updated_at: 2026-10-10T08:30:00Z
parent: qou-avtq
---


## 2026-10-10 — evidence re-check (verification sweep of `qou-avtq`)

**Verdict: SUPERSEDED.** Do not "promote the shape to proved". The Lean proves an identity of a defined quadratic model, and the identification Re u = ln q0 is undischarged (qou-8vt2). Superseded by qou-8vt2.

Evidence: `FigureEightComplexVolume.lean` is sorry-free, but `V₄₁` is *defined* as `Vol + a₂u²` (line 98). `imV₄₁` is algebra on that definition, not a theorem about the deformed volume, and the O(u⁴) tail is a cited residual (docstring lines 60–64). The S_K shape also needs `hRe: Re u = ln q0`, which qou-8vt2 shows is undischarged with a phantom citation.

Status: `todo` → `scrapped`.
Checked against qou `main` at `77695711d2`. Probes were re-run only where cheap and decisive. A numeric result counts as evidence only where it reproduces and its precision exceeds the gap it decides; convention-C numbers are not evidence about convention-D claims.
