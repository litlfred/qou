---
# qou-8r6b
title: 'Pose the composition feasibility program: variable = interface letter (1−e)σ + eσ⁻¹, feasible set = reading 3 on the composite; first enumeration at A=2'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-16T05:49:42Z
updated_at: 2026-11-15T17:25:00Z
parent: qou-v2om
---


## 2026-09-16 — posed (Lean) and solved at A = 2 in closed form

Lean: CompositionFeasibilityProgram.lean — CompositionProgram (data B, alphabet L acting on the composite, unit letter), composite, letterDeviation, Feasible := Reading3 on the composite, feasibleSet; proved trM_nonneg_of_reading3, weighted_letterDeviation_ge, feasible_unit_iff, letterDeviation_unit. Probe composition_feasibility_a2_probe.py (8/8): self-contained mpmath Hoefsmit evaluator validated against committed H_3 (5.4e-50) and H_6 Rust/MPFR (1.4e-49) characters FIRST. On the alphabet (1−e)σ₂+eσ₂⁻¹ the feasible set under reading 3 is e ≤ −4.019 — NO e in [0,1] (not σ, not production e_pn=0.49966, not σ⁻¹); (5,1) is negative at both endpoints (−0.607, −0.758). Power letters: σ₂^{±2} feasible (ratios 0.9156 / 1.1281), every odd power fails on (5,1). Bond law tr ratio = z_D − e h along the family to 1.7e-50. Reading: the A=2 defect is the bridge letter's PARITY, not its weight (scope (a): tested alphabet only). Open: A ≥ 3 bands (two-row blocks at H_9 feasible in mpmath), reading 3 scope ruling (#7434 O2), any objective (qou-ypc5). Doc §4.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-16 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

## 2026-11-15 — re-scoped by the γγ rule

The owner ruled that the γγ selection rule also covers the nuclear bond letters. Any number in this bean computed on the single-crossing interface letters of `atom_braid_word_3A` (`d_k`, `μ_e`, the chain law `∏(z_D + d_k)`, the `b₃` magnitudes −1.2277 / −0.7973 MeV, or a sign map on that word) is now a record of a superseded word, not a current result. Lean results stated for generic bond weights are unaffected. The redo waits on a γγ-selected word per nucleus (PR #7876). Record: `docs/audits/2026-11-15-gg-rule-rescopes-old-letter-binding.md`. The bean stays open.


## 2026-10-12 — SCOPE CORRECTION of the A = 2 parity finding (convolution flow)
'Every odd power fails on (5,1)' was measured for |m| ≤ 3 only, and is FALSE beyond it. Exact split (ConvolutionFlowParity.lean, exit 0; probe convolution_flow_parity_probe.py 5/5): χ(Wσ^m) = q^m a_S + (−q⁻¹)^m a_A with (5,1) a_S = 0.021792, a_A = 0.700431. Odd m infeasible iff q^{2m} < a_A/a_S ≈ 32.1, i.e. m < 16.63: odd m ≤ 15 fail, odd m ≥ 17 feasible (checked directly at m = 17). Even m ≥ 0 all feasible; negative odd m fail. Feasible power letters for m ∈ [−8, 20]: −8,−6,−4,−2, 0..16 even, 17..20. The parity is the cos(πt) of the convolution flow σ^t = q^t P_S + q^{−t} e^{±iπt} P_A, and it holds only until the Sym channel's q^{2m} overtakes a_A/a_S. Not fitted; no letter selected.
