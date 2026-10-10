---
# qou-reab
title: '4_1 saddle brick 3 (derivative, PROVABLE — focused-session task): clausenPotential(θ)=-∫_0^θ log(2 sin(t/2)); prove HasDerivAt = -log(2 sin(θ/2)) on (0,2π) via integral_hasDerivAt_right (FTC) + intervalIntegrable_log_sin (Mathlib, unconditional log-sin integrability) + a.e.-congr for the 2*sin + StronglyMeasurableAtFilter from ContinuousAt. Formalizes rem:dilog-saddle-regime V''(θ). All Mathlib pieces confirmed present; needs LSP-assisted focused pass.'
status: completed
type: task
priority: normal
created_at: 2026-07-13T16:01:09Z
updated_at: 2026-07-19T13:05:03Z
---

Route B Clausen bridge — bricks DONE (PR #3787, sorry-free, lake build Built): hasDerivAt_clausen, continuous_Cl_2, clausen_pi, clausen_eqOn_Cl_2 (reduction), clausen_eq_series (derived), Cl_2_pi/Cl_2_two_pi. REMAINING atom hasDerivAt_Cl_2_series (Σcos(kθ)/k=-log(2sin(θ/2))). CORRECTION 2026-07-14: earlier 'Mathlib lacks Abel's theorem' was WRONG — Mathlib HAS it (Real.tendsto_tsum_powerSeries_nhdsWithin_lt, Analysis.Complex.AbelLimit) + hasSum_taylorSeries_log (‖z‖<1). So the atom is an ASSEMBLY, not a wall: (1) g_r=Σr^k sin(kθ)/k²→Cl_2 and g_r'=Σr^k cos(kθ)/k→-log(2sin(θ/2)) by Abel; (2) g_r'=Re(-log(1-re^{iθ})) by the complex log series; (3) term diff of g_r for r<1 by hasDerivAt_tsum (r^k summable); (4) derivative-under-limit (needs locally-uniform convergence, the subtlest brick). Multi-brick but attemptable — no ansatz.
