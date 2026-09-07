---
# qou-d0qq
title: 'Step-2 C construction (research): KZ-type connection on the configuration space of the colour cubic''s six branch points at an IMAGINARY level, monodromy computed, Hecke quadratic read off; first measurement = does any level reproduce q0 ≈ 1.11 real'
status: in-progress
type: task
priority: normal
created_at: 2026-09-06T08:13:53Z
updated_at: 2026-09-07T09:43:07Z
parent: qou-2akx
---

2026-09-06 first measurement (exact, mpmath 40 dps at the proton pin): KZ at REAL level cannot give q0 (unit modulus, Lean KZUnitModulusPrune); at IMAGINARY level it can — with q = e^{2πi/(k+2)}, k+2 = 2πi/ln q0 = 60.2179598524791980753 i (ln q0 = 0.10434072031951951232); with q = e^{iπ/(k+2)}, k+2 = 30.1089799262395990377 i. So the prune does not kill C; it fixes the level to be non-unitary. Next: write the KZ connection on Conf of the six branch points at that level and compute its monodromy exactly (Kohno–Drinfeld gives Hecke; the question is whether the framework's connection IS this one).



2026-09-07 claimed (session route-c / step-2 arc). Planning agent dispatched (label kz-level) for the initial plan; q₀ is INPUT only (forever-gate respected). Plan to be filed by the parent session.



2026-09-07 PLAN FILED: docs/audits/2026-09-07-route-c-step3-and-kz-level-plans.md §B (agent kz-level, parent-verified). The bean's stated next step is ill-posed: the six branch points are fixed, so the base is C∖{6 points} (π₁ = F₆), and the only meaningful construction is the sl₂ KZ connection on Conf₃(C) pulled back along the root map. Queue: B1 = braid word of each lasso (half-twist or not), B2 = Lean z_D = U_q(sl₂) quantum trace (already numerically confirmed, diff 5e-31) and z_3 ≠ z_D, B3 = flatness is level-independent + reword the three 'flat at q₀' prose sites, B5 = retitle this bean (the title's 'does any level reproduce q0' is gate-violating wording; q₀ is INPUT). Registry key correction: drinfeld1985, not 1990.
