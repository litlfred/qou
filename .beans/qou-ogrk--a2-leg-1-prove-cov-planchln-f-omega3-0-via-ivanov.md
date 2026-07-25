---
# qou-ogrk
title: 'A2 (leg 1): prove Cov_Planch(ln f, omega3) <= 0 via Ivanov-Olshanski 2nd-order covariance'
status: todo
type: task
priority: high
created_at: 2026-07-25T03:30:08Z
updated_at: 2026-07-25T12:03:36Z
parent: qou-v8t7
---

A2 — leg 1: Cov_Planch(ln f, ω₃) ≤ 0. SHARPENED (2026-07-25): the dim²→dim³ threshold synthesis (A1+A5) shows the obstruction is uniform — ln f = ½ln M_n + ½ln n! involves ln dim λ, which (like dim) is NOT shifted-symmetric (∉ algebra A), so the exact character-covariance engine (IO Prop 5.1 + Śniady product rule, which gives any Cov(p#_j,p#_k)) does NOT reach Cov(ln f,ω₃). CONCRETE TARGET: an expansion of the Vershik-Kerov ln-dim functional against Plancherel (or Schur-measure / hook-content generating function), then pair with ω₃∈A. This is the one missing tool for the whole kernel. Numerics: Cov(ln f,ω₃)<0 all n≤19 (leading term, the g'(0) of the tilted mean). Open.
