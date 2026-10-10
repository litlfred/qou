---
# qou-8r6b
title: 'Pose the composition feasibility program: variable = interface letter (1−e)σ + eσ⁻¹, feasible set = reading 3 on the composite; first enumeration at A=2'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-16T05:49:42Z
updated_at: 2026-10-04T15:13:30Z
parent: qou-v2om
---


## 2026-09-16 — posed (Lean) and solved at A = 2 in closed form

Lean: CompositionFeasibilityProgram.lean — CompositionProgram (data B, alphabet L acting on the composite, unit letter), composite, letterDeviation, Feasible := Reading3 on the composite, feasibleSet; proved trM_nonneg_of_reading3, weighted_letterDeviation_ge, feasible_unit_iff, letterDeviation_unit. Probe composition_feasibility_a2_probe.py (8/8): self-contained mpmath Hoefsmit evaluator validated against committed H_3 (5.4e-50) and H_6 Rust/MPFR (1.4e-49) characters FIRST. On the alphabet (1−e)σ₂+eσ₂⁻¹ the feasible set under reading 3 is e ≤ −4.019 — NO e in [0,1] (not σ, not production e_pn=0.49966, not σ⁻¹); (5,1) is negative at both endpoints (−0.607, −0.758). Power letters: σ₂^{±2} feasible (ratios 0.9156 / 1.1281), every odd power fails on (5,1). Bond law tr ratio = z_D − e h along the family to 1.7e-50. Reading: the A=2 defect is the bridge letter's PARITY, not its weight (scope (a): tested alphabet only). Open: A ≥ 3 bands (two-row blocks at H_9 feasible in mpmath), reading 3 scope ruling (#7434 O2), any objective (qou-ypc5). Doc §4.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-16 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.
