---
# qou-iw1d
title: 'QFT-4: Lambda^3 W_3 Baryon Spin-Flavour Axial Charge g_A^(0) = 5/3 -> g_A(q_0) = 1.2690 & Polarized DIS Bjorken Sum Rule'
status: todo
type: task
priority: high
created_at: 2026-11-19T16:48:44Z
updated_at: 2026-11-21T12:40:00Z
parent: qou-3fjn
---

`QOU/StandardModel/BaryonSpinFlavourAxialAndBjorkenSumRule.lean` + `baryon_axial_charge_and_bjorken_sum_rule_probe.py` completing verification in `b7ebd36b`.

## Resolution (2026-11-19)

Completed (`0 sorry, 0 axiom`, Round-2 Red-Team UNCONDITIONAL PASS): `QOU/StandardModel/BaryonSpinFlavourAxialAndBjorkenSumRule.lean` (492 lines) + 80-dps `baryon_axial_charge_and_bjorken_sum_rule_probe.py` deriving `g_A^(0) = 5/3` and `mu_p^(0)/mu_n^(0) = -3/2` on the 64-state `Sym^3(Q^4)` space, full zero-fitting `H_3(q_0)` axial branch census, and 3-loop MSbar Larin-Vermaseren polarized DIS Bjorken sum rule.

## Reopened (owner instruction 2026-11-20, via W12)
This bean was set to completed by local commits on `cat/cat-harness/beans` (e223ed1 / 4fcd2cb / 89bb5e0, 2026-11-19, `litlfred@fenugreek.home`, no session trailer). The Lean / probe / witness files its resolution names are not on main, on any branch, or in any PR found by the bean id (measured 2026-11-20). See GAP bean qou-w12g.

## 2026-11-21 — physics-scope re-check on main 2ae54ab40 (bean-drain sibling, issue #8810)

Re-checked on main: the Lean/probe files this bean's resolution text names are absent (`git ls-files | grep <stem>` = 0). The epic's vocabulary has 0 hits in the folio (Cutkosky, Bern–Kosower, Callan–Gross, Herm₂, 41/10, Machacek, Larin). Two further scope problems independent of the missing files: (1) the title puts empirical comparisons inside formal targets; (2) Feynman perturbation theory sums over virtual quanta, which the owner ruling of 2026-11-21 (no virtual photons) excludes. Disposition (re-scope to math-only / scrap / leave) is on an owner card. Audit: `docs/audits/2026-11-21-physics-claim-scope-recheck.md` on branch `claude/physics-scope-audit-2026-11-21` (4df574c79).
