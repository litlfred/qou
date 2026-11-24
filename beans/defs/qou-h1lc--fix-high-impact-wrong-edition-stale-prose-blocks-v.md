---
# qou-h1lc
title: Fix High-Impact Wrong-Edition & Stale Prose Blocks via Liquid Variable Substitution
status: completed
type: task
priority: high
created_at: 2026-11-19T07:31:23Z
updated_at: 2026-11-24T15:33:25Z
parent: qou-v6so
blocking:
    - qou-t0fc
---

Granular sub-issue of qou-t0fc (G2). Replace high-impact stale/wrong-edition prose numbers with Liquid variable tags backed by 50-dps canonical witnesses across:
- folio/quantum-observable-universe/standard-model-lagrangians/sm-params-gauge-couplings.md (fix CODATA-2018 sign flip)
- folio/quantum-observable-universe/standard-model-lagrangians/em-coupling-bring-zero-mode.md
- folio/quantum-observable-universe/standard-model-lagrangians/neutron-proton-splitting.md (fix hybrid CODATA 2022-2018 subtraction)
- folio/quantum-observable-universe/mass-binding-atlas/mba-step09a-mass-identity.md
- folio/quantum-observable-universe/foundations/mass-comparison-table*.md

## Closed in PR #9356 (a2ad9a3b3d73, 2026-11-24)
Converted remaining stale and wrong-edition prose literals to live Liquid {{ qou.computations... }} and {{ qou.library.codata-2022... }} substitutions across predicted-spectra/em-coupling-bring-zero-mode.{md,ts}, mass-theory/neutron-proton-splitting.{md,ts}, and observations/mass-comparison-table*.{md,ts} (sm-params-gauge-couplings.md was already wired on main, and mba-step09a-mass-identity.md was retired in #9280), while fixing the hybrid 0.9557 -> 0.9601 MeV Delta splitting figure and excising all 5 remaining CAL-1/CAL-2 tags.
