---
# qou-vfn2
title: 'E1: order-b4 second equation — geometric a4 from the validated gluing solver vs -kappa2*kappaA^2/kappa1^2; decides the linear bridge (refutable, parameter-free) and pins the scale (parent qou-yh67)'
status: completed
type: task
priority: normal
created_at: 2026-08-15T04:09:56Z
updated_at: 2026-08-15T04:14:44Z
---


## Verdict (2026-08-15, probe run, witness qbeta-ohtsuki-nz-bridge-b4)

1. **Method validated**: Richardson a₂ = i·0.433012701892 vs proved i·√3/4,
   |Δ| = 3.2e-25 (the first version's raw-Rogers extraction failed its own
   a₂ gate — Schläfli stationarity — and was replaced by the T2 probe's NZ
   longitude integral; the gate worked exactly as designed).
2. **STRICTLY LINEAR BRIDGE u = c·b REFUTED at order b⁴, scope-(a)**: the
   bridge requires a₄ real; the geometric a₄ = i·0.0721687836487 is purely
   imaginary. The OhtsukiNZBridgeScale.lean theorems stand as implications
   (hypothesis now known false in the strictly-linear form).
3. **Exact-form observation (C14-flagged, not wired)**: a₄ matches √3/24 to
   all extracted digits — with a₂ = i·√3/4, the deformed complex volume
   reads 𝔙 = 𝔙₀ + i√3(u²/4 + u⁴/24 + …), extending the exact ℚ(√3)
   pattern to order u⁴. Lean-fodder candidate (imV₄₁ order-u⁴ extension).
4. **Reopening (well-posed continuation)**: an odd-series bridge
   u = c·b + c₃b³ reopens the match with c₃ FORCED by the b⁴ equation
   (not fitted); the exact κ₃ = 1081√3π³/21870 then makes order b⁶ a
   parameter-free test. That is the next E1 rung if pursued.
