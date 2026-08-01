---
# qou-dw20
title: 'qou-t2sc saddle-value: prove (2π/N)log S_{n*,k*} → 4G (van der Veen Clausen/Lobachevsky max-value; the single open hsaddle input of whitehead_vc_of_saddle_value)'
status: in-progress
type: task
priority: normal
created_at: 2026-08-01T23:54:37Z
updated_at: 2026-08-01T23:55:12Z
---


## Validated (2026-08-01) — hsaddle is TRUE; saddle pinned
- Saddle location (t*,x*)=(1/2,1/4) (discrete argmax of log S_{n,k}).
- Continuum saddle value = 4G EXACTLY (40 dps): 2π∫_0^{1/2}[log2+2log
  sin(π(u+1/4))−log sin(π u)]du = 8Λ(π/4). See computations/whitehead_saddle.py.
- Lean discharge = Riemann-sum→integral convergence at nseq→N/2, kseq→N/4,
  value 4G, via QOU.Knot.Clausen (FigureEightVolumeSaddle analogue). Needs the
  QOU-library build to verify (no longer Mathlib-only).
