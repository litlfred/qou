---
# qou-kx92
title: mass-theory conditional-class theorems conclude :True (2)
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-07-11T18:41:39Z
updated_at: 2026-11-16T18:02:18Z
parent: qou-wp3h
---

reidemeister-mass-invariance.lean:169 [_inst:BorromeanQuark]:True:=trivial and hoefsmit-scattering-pipeline.lean:145 [_inst:HyperbolicVolumeIndependence]:True:=trivial — §3b-cond item 5 degenerate: a class-conditional theorem must DERIVE a real conclusion, not conclude True. Needs the real downstream claim.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-07-18 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

## Verification & Audit Note (2026-11-16 — Owner Ruling `Q-WP3H-1 = 1`)

- Verified on `main` that both `True := trivial` placeholders in `mass-theory/` were already replaced by substantive sorry-free Lean theorems (`0` `sorry`, `0` `: True`):
  1. `folio/quantum-observable-universe/mass-theory/reidemeister-mass-invariance.lean`: de-vacuified in commits `62d3235885` and `a2842b21ac` (`2026-07-12`, plus `6190601130` on `2026-09-04`), proving `calibrated_mass_pos_of_borromeanQuark` (`0 < 4 * Real.pi * h ^ 2 * G * m_e`).
  2. `folio/quantum-observable-universe/mass-theory/hoefsmit-scattering-pipeline.lean`: de-vacuified in commits `0912f1aa53` (`2026-07-12`) and `709b8cc166` / `3bbc8619fb` (`2026-07-18`), proving `conditional_on_HyperbolicVolumeIndependence` (deriving $\mathbb{Q}$-linear independence `a = 0 ∧ b = 0` from `a * vol_fig8 + b * vol_borr = 0` under `[HyperbolicVolumeIndependence]`) and `pipeline_functoriality`.
- Kept at `status: in-progress` per owner rule (no unilateral bean closure; ready for owner review).
