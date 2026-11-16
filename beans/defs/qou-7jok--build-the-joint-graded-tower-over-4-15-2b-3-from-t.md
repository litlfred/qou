---
# qou-7jok
title: 'Build the JOINT graded tower over 4_1/5_2/B_3 from the Ohtsuki expansions (OhtsukiTowerBarParity.lean) and test for a negative-grade annihilator; kappa_n in Q(sqrt3)*pi^ceil(n/2) so conditions are arithmetic. Blockers: V_0 is COMPLEX volume (Vol + i*CS); each knot expands at its own root of unity'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-09T23:10:28Z
updated_at: 2026-11-16T18:00:00Z
parent: qou-10v9
---


## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-08-10 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

## 2026-11-16 — Round 46 execution (`Q-10V9-4 = 1`, PR `litlfred/qou#8144`, commit `8fecf0a5bc64b5831742a0515ad6f634a0202925`)

- **Probe & Witness:** `computations/qbeta/joint_ohtsuki_graded_tower_annihilator_probe.py` & `computations/qbeta/joint-ohtsuki-graded-tower-annihilator.witness.json` (60 dps `mpmath` + exact number-field arithmetic, 0 float64 leaks).
- **Lean 4 Formalization:** `folio/quantum-observable-universe/lean/QOU/QBeta/JointOhtsukiGradedTower.lean` (wired into `folio/quantum-observable-universe/lean/QOU.lean`, `0` `sorry`, standard axioms `[propext, Classical.choice, Quot.sound]`):
  - **Blocker 1 (`chiral_grade0_parity_blocker`):** $\mathrm{CS}_0(4_1) = \mathrm{CS}_0(\mathbb{B}_3) = 0$ by amphicheirality whereas chiral $5_2$ has $\mathrm{CS}_0(5_2) = -3.0241283765\dots \neq 0$, so annihilating the joint grade-$0$ imaginary part forces $\alpha_{5_2} = 0$.
  - **Blocker 2 (`fiveTwo_cubic_mod2_no_root`, `trace_field_discriminants_pairwise_distinct`, `rational_rung12_det_ne_zero`, `amphicheiral_two_rung_annihilator_trivial`, `joint_three_complement_annihilator_trivial`, `single_rung_q_linear_indep_annihilator_trivial`):** Proves $\mathbb{F}_2$ irreducibility of $y^3 - 2y^2 + 3y - 1$ for $K_{5_2}$ (discriminant $-23$), pairwise distinctness of field discriminants $(-3, -23, -4)$, and triviality $(\alpha_{4_1}, \alpha_{5_2}, \alpha_{\mathbb{B}_3}) = (0, 0, 0)$ of both the 3-complement real grade annihilator ($\det M_{\mathrm{joint}} = -0.7783984096\dots \neq 0$) and the single-rung $\mathbb{Q}$-linear-independence annihilator.
