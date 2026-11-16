---
# qou-zbcj
title: 'Identify Phi_n(x;q) as the Yekutieli non-abelian multiplicative integral of the C-connection; verify refinement order = iterated (rho then q). Resolves MQ1: path-ordered exponential forbids the joint limit.'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-07-26T12:23:35Z
updated_at: 2026-11-16T18:02:18Z
parent: qou-wp3h
---


## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-07-26 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

## Progress Update (2026-11-16 — Owner Ruling `Q-WP3H-1 = 1`, PR #8143)

- Added `folio/quantum-observable-universe/lean/QOU/Torsion/MultiplicativeIntegralCurvature.lean` (`0` `sorry`, wired into `QOU/Torsion.lean` and `QOU.lean`, plus `QOU.Archimedean.DilogNaStokesHolonomyOrdering` in `QOU.lean`, PR `litlfred/qou#8143`, commit `7df80d1c2e228518b2ca15ec1d314be46da8e524`):
  - `iteratedHolonomy_eq_commutatorDefect_mul`, `commutatorHolonomyDefect_eq_one_iff`, `iteratedHolonomy_eq_iff_commute`: proves that for any group `G` and step transports `g_ρ, g_q : G`, the two iterated 2-step holonomies `holonomy [g_ρ, g_q]` and `holonomy [g_q, g_ρ]` differ by left multiplication by `commutatorHolonomyDefect g_ρ g_q = g_ρ * g_q * (g_q * g_ρ)⁻¹`, which is `1` iff `g_ρ * g_q = g_q * g_ρ`.
  - `bch_first_order_commutator_defect`: proves `(1 + A_ρ) * (1 + B_q) - (1 + B_q) * (1 + A_ρ) = A_ρ * B_q - B_q * A_ρ` over any non-commutative ring `R`.
  - `phiN_eq_yekutieli_holonomy`: identifies $\Phi_n(x; q) = \prod_{k < n} (1 - x q^k)^{-1}$ with the discrete Yekutieli holonomy `partBHolonomy x q n`.
- Added 50+ dps `mpmath` probe `computations/probes/yekutieli_multiplicative_integral_curvature_probe.py` and witness `computations/probes/yekutieli-multiplicative-integral-curvature.witness.json` (registered in `computations/q0_anchor_manifest.json` under `physical_proton`).
- Kept at `status: in-progress` pending PR #8143 merge and owner verification.
