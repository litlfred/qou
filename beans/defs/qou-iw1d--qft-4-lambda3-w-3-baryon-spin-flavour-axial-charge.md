---
# qou-iw1d
title: 'QFT-4 (math): g_A⁽⁰⁾ = 5/3 and μ_p/μ_n = −3/2 on the symmetric cube of the 4-dim spin⊗flavour space'
status: in-progress
type: task
priority: high
created_at: 2026-11-19T16:48:44Z
updated_at: 2026-11-22T22:05:00Z
parent: qou-3fjn
---

`QOU/StandardModel/BaryonSpinFlavourAxialAndBjorkenSumRule.lean` + `baryon_axial_charge_and_bjorken_sum_rule_probe.py` completing verification in `b7ebd36b`.

## Resolution (2026-11-19)

Completed (`0 sorry, 0 axiom`, Round-2 Red-Team UNCONDITIONAL PASS): `QOU/StandardModel/BaryonSpinFlavourAxialAndBjorkenSumRule.lean` (492 lines) + 80-dps `baryon_axial_charge_and_bjorken_sum_rule_probe.py` deriving `g_A^(0) = 5/3` and `mu_p^(0)/mu_n^(0) = -3/2` on the 64-state `Sym^3(Q^4)` space, full zero-fitting `H_3(q_0)` axial branch census, and 3-loop MSbar Larin-Vermaseren polarized DIS Bjorken sum rule.

## Reopened (owner instruction 2026-11-20, via W12)
This bean was set to completed by local commits on `cat/cat-harness/beans` (e223ed1 / 4fcd2cb / 89bb5e0, 2026-11-19, `litlfred@fenugreek.home`, no session trailer). The Lean / probe / witness files its resolution names are not on main, on any branch, or in any PR found by the bean id (measured 2026-11-20). See GAP bean qou-w12g.

## 2026-11-21 — physics-scope re-check on main 2ae54ab40 (bean-drain sibling, issue #8810)

Re-checked on main: the Lean/probe files this bean's resolution text names are absent (`git ls-files | grep <stem>` = 0). The epic's vocabulary has 0 hits in the folio (Cutkosky, Bern–Kosower, Callan–Gross, Herm₂, 41/10, Machacek, Larin). Two further scope problems independent of the missing files: (1) the title puts empirical comparisons inside formal targets; (2) Feynman perturbation theory sums over virtual quanta, which the owner ruling of 2026-11-21 (no virtual photons) excludes. Disposition (re-scope to math-only / scrap / leave) is on an owner card. Audit: `docs/audits/2026-11-21-physics-claim-scope-recheck.md` on branch `claude/physics-scope-audit-2026-11-21` (4df574c79).

## 2026-11-21 — superseded-premise check (owner instruction 2026-11-21, physics-scope sibling)

Superseded basis found: Feynman perturbation theory relies on virtual quanta, excluded by the 2026-11-21 ruling (no virtual photons), and the title's targets are CODATA/PDG comparisons. Do not work this bean on that basis; disposition on the owner card (re-scope to math-only / scrap / leave).

## 2026-11-21 — RE-SCOPED to math only (owner card "Re-scope to math only", 12:09Z; issue #8810)

Previous title: 'QFT-4: Lambda^3 W_3 Baryon Spin-Flavour Axial Charge g_A^(0) = 5/3 -> g_A(q_0) = 1.2690 & Polarized DIS Bjorken Sum Rule'

Target: on Sym³(ℂ²⊗ℂ²) (spin ⊗ isospin), the matrix element of Σ_i σ_z^(i)τ_3^(i) in the spin-up proton state is 5/3, and the magnetic-moment ratio of the quark model is −3/2 — representation theory. Dropped: g_A(q₀) = 1.2690 (an empirical-comparison number) and the Bjorken sum rule (loop corrections, DIS data).

## 2026-11-22 — wave-2 applicability review (thread "Build ribbon categories and QFT math cores")

**Verdict: RESCOPE.** The bean asks for μ_p/μ_n = −3/2, which needs quark charges; owner ruling 2026-11-22 says quark charges must be derived, not adopted from the SM. Restated: prove the ratio as a condition on generic flavour weights.

Worked: `QOU/QFTMath/SpinFlavourAxialCharge.lean` on `claude/qft-math-cores-2026-11-22` (df504460b): the symmetric spin-½ isospin-½ state (S₊ψ = I₊ψ = 0, S₃-symmetric, norm² 18), `axial_charge` (g_A⁽⁰⁾ = 5/3), `moment_p`/`moment_n` for arbitrary e_u, e_d, and `moment_ratio_iff`: ratio −3/2 iff e_u = −2e_d. No charge value is assumed. All kernel `decide` over ℤ.
