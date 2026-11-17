---
# qou-ohaz
title: 'GAP: model-to-PDE uniformity of the two-regime pair-collision model — the surviving lock-uniformity caveat. Phase-1 ODE calculus is theorem-grade (pair_phase1_riccati.lean); Gamma-growth escape closed in-model; what is NOT established is that the NS/q-NS PDE dynamics follows the two-regime ODE through the approach (strain locality, core deformation, V1-d2 phase-plane fidelity). Next honest step: derive the ODE system as a controlled reduction of the vortex-filament/Biot-Savart PDE with error bounds, or find the PDE effect that breaks it.'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-14T16:06:54Z
updated_at: 2026-10-04T15:12:57Z
parent: qou-a3n3
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

## Progress 2026-09-03 — U1-U4 are ALL closed; the headline is what remains

U3 (bean qou-7fi2) and U4 (bean qou-zuz0) are both COMPLETED, and have been
since 2026-08-14 — the same day the decomposition audit was written, which is
why its §4 'next honest steps' still listed them. Corrected in that audit.

So all four sub-items carry results:
  U1 exact (Biot-Savart reduction for straight anti-parallel filaments)
  U2 theorem-grade, sorry-free (pair_viscous_core_race: Lamb-Oseen vs approach)
  U3 completed (Crow: bounded power law A = (d0^2/V1_0)^{s*/3}, no linear
     finite-time 3D runaway)
  U4 completed (burgers_core_strain_cap: cap Gamma/(4*pi*a^2) derived from the
     Gaussian profile)

THIS BEAN IS NOT CLOSED. Its headline is a controlled reduction of the
two-regime ODE from the Biot-Savart PDE WITH ERROR BOUNDS, or the PDE effect
that breaks it. U1-U4 constrain that reduction from four directions; none of
them IS it. Do not close this on the strength of the sub-items.

Related landing, same session: the pair channel's Levi exponent is EXACTLY 1
(branch B), not the fitted 0.99628 which formally sits in the undetermined
window C. Exact closed form C_L = (2*Gamma/pi)*(1+eps)/eps under the lock;
Lean linear_condNumber_forces_beta_one derives beta = 1 from linear growth
without using any fitted number. Still conditional on the lock formula, which
is a model input -- so it sharpens the branch reading for one channel and does
not touch this bean's uniformity question.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-03 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

## Progress Update (Round 91 — lane-cf11)
- Formalized in `folio/quantum-observable-universe/lean/QOU/QBeta/HookEvenMomentAndBorromeanTripleBrick.lean` with 80-dps probe `computations/probes/hook_even_moment_and_borromean_triple_brick_probe.py` and witness `computations/probes/hook-even-moment-and-borromean-triple-brick.witness.json`.
- PR: https://github.com/litlfred/qou/pull/8343 (`feat/qou-b9cj-ogrk-ohaz-omr7-ooqh-po72`, HEAD `8c185bc247a4dfba4e6316715175039c0defb340`).
