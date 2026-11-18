---
# qou-r8hb
title: 'Lean-prove Gap 1, 2 & 5: Concrete Matrix Instantiation of CategoricalLagrangian on W_p/W_n, Stokes Boundary Commutator, and E_0 * q(q-1) = m_e Scale Bridge'
status: in-progress
type: task
priority: high
created_at: 2026-11-18T20:58:52Z
updated_at: 2026-11-18T20:58:52Z
parent: qou-7xl8
---

Close Gaps 1, 2, and 5 in `CategoricalLagrangianTwoTermBridge.lean` and `NucleonWeightSpaceTwoTerm.lean`:
1. Gap 2 (Eliminate abstract `hProtonCoulomb` / `hNeutronCoulomb` hypotheses): Prove concrete matrix-algebra specialization theorems connecting `CategoricalLagrangian`'s two-term expansion directly to the 3x3 weight-space matrices `borromeanV3A`, `borromeanV3B`, `Q12p + Q23p`, and `Q12n + Q23n` (both full and `e_(2,1)`-projected).
2. Gap 1 (Non-Abelian Stokes Seifert Boundary Factorisation): Prove that the Borromean word `V^3 = (σ₁ σ₂⁻¹)^3` is the 3-period boundary holonomy product `borromeanVA^3` / `borromeanVB^3` whose cyclic trace derivative across all 6 boundary crossings reduces to `3 * tr((Q12 + Q23) V^3)`.
3. Gap 5 (Lagrangian Scale Hierarchy `E_0 * q(q-1) = m_e`): Prove over any `[Field R]` that with `E₀(q) = m_e / (q * (q - 1))` and `ħ_q = (q - 1) / q = 1 - q⁻¹`, the ratio between the `O(ħ_q^2)` strong prefactor and the `O(ħ_q^1)` matter prefactor satisfies `E₀(q) * (q ^ 2 * (1 - q⁻¹)) = m_e` (and `E₀(q) * (q * (q - 1)) = m_e`), deriving the `m_e` scale of the matter term directly from `E₀` with zero free parameters.
4. Verify with `scripts/lean-verify.sh` and strict vacuity audits, then submit to adversarial review.
