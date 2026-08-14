---
# qou-ohaz
title: 'GAP: model-to-PDE uniformity of the two-regime pair-collision model — the surviving lock-uniformity caveat. Phase-1 ODE calculus is theorem-grade (pair_phase1_riccati.lean); Gamma-growth escape closed in-model; what is NOT established is that the NS/q-NS PDE dynamics follows the two-regime ODE through the approach (strain locality, core deformation, V1-d2 phase-plane fidelity). Next honest step: derive the ODE system as a controlled reduction of the vortex-filament/Biot-Savart PDE with error bounds, or find the PDE effect that breaks it.'
status: in-progress
type: task
priority: normal
created_at: 2026-08-14T16:06:54Z
updated_at: 2026-08-14T16:19:42Z
---


## Progress 2026-08-14 (same session, post-#5019)

Decomposed into U1-U4; see
docs/audits/2026-08-14-qns-model-to-pde-uniformity-decomposition.md.
U2 substantially closed: the viscous core-growth race
(pair_viscous_core_race.lean, sorry-free) — Lamb–Oseen a² = a₀²+4νt
(exact NS) vs approach d² = d₀²−(Γ/π)t crosses strictly before
collision at positive separation for every ν > 0, no strain-driven
core growth assumed. Remaining open content of this bean = U3 (3D
effects: Crow instability, axial flow) + U4 saturation-value
derivation. Next steps written in the audit §4.
