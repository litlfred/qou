---
# qou-reab
title: '4_1 saddle brick 3 (derivative, PROVABLE — focused-session task): clausenPotential(θ)=-∫_0^θ log(2 sin(t/2)); prove HasDerivAt = -log(2 sin(θ/2)) on (0,2π) via integral_hasDerivAt_right (FTC) + intervalIntegrable_log_sin (Mathlib, unconditional log-sin integrability) + a.e.-congr for the 2*sin + StronglyMeasurableAtFilter from ContinuousAt. Formalizes rem:dilog-saddle-regime V''(θ). All Mathlib pieces confirmed present; needs LSP-assisted focused pass.'
status: in-progress
type: task
priority: normal
created_at: 2026-07-13T16:01:09Z
updated_at: 2026-07-14T02:04:58Z
---

Route B Clausen bridge — bricks DONE (PR #3787, all sorry-free, lake build Built): hasDerivAt_clausen (FTC deriv), continuous_Cl_2 (M-test), clausen_pi (=0 via log-sin integral), clausen_eqOn_Cl_2 (reduction via eqOn_of_deriv_eq), clausen_eq_series now DERIVED, Cl_2_pi/Cl_2_two_pi. REMAINING = one atom hasDerivAt_Cl_2_series (∑cos(kθ)/k = -log(2sin(θ/2))), a genuine Mathlib-contribution wall: (i) term-by-term diff of a conditionally-convergent series (hasDerivAt_tsum needs summable deriv bound — fails; Dirichlet's test present but no local-uniform interchange); (ii) Abel's theorem for the boundary ‖z‖=1 (Mathlib has hasSum_taylorSeries_log only ‖z‖<1). Multi-session / upstream-Mathlib. Do NOT wire an ansatz.
