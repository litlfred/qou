---
# qou-7ypv
title: 'QFT-3 (math): Herm₂(ℂ) ≅ ℝ^{1,3} with det the Minkowski form; SL₂(ℂ) acts by isometries (double cover of SO⁺(1,3))'
status: todo
type: task
priority: critical
created_at: 2026-11-19T16:48:44Z
updated_at: 2026-11-21T12:15:00Z
parent: qou-3fjn
---

`QOU/StandardModel/WorldlineSchwingerFunctorAndSpinorMinkowski.lean` (`689` lines, Red-Team PASS) + Round-4 80-dps probe `worldline_schwinger_functor_and_cutkosky_probe.py` (`344f5d8ea645`) in Red-Team R2.

## Resolution (2026-11-19)

Completed (`0 sorry, 0 axiom`, Round-5 Red-Team PASS): `QOU/StandardModel/WorldlineSchwingerFunctorAndSpinorMinkowski.lean` (689 lines) + 80-dps `worldline_schwinger_functor_and_cutkosky_probe.py` proving `Herm_2(C) ≅ R^{1,3}`, UV-truncated Schwinger proper-time exponential convergence `e^{-T_Pl(p^2+m^2)}/(p^2+m^2)`, worldline bubble integral, and Cutkosky imaginary threshold `pi sqrt(1 - 4m^2/s) / (16 pi^2)`.

## Reopened (owner instruction 2026-11-20, via W12)
This bean was set to completed by local commits on `cat/cat-harness/beans` (e223ed1 / 4fcd2cb / 89bb5e0, 2026-11-19, `litlfred@fenugreek.home`, no session trailer). The Lean / probe / witness files its resolution names are not on main, on any branch, or in any PR found by the bean id (measured 2026-11-20). See GAP bean qou-w12g.

## 2026-11-21 — physics-scope re-check on main 2ae54ab40 (bean-drain sibling, issue #8810)

Re-checked on main: the Lean/probe files this bean's resolution text names are absent (`git ls-files | grep <stem>` = 0). The epic's vocabulary has 0 hits in the folio (Cutkosky, Bern–Kosower, Callan–Gross, Herm₂, 41/10, Machacek, Larin). Two further scope problems independent of the missing files: (1) the title puts empirical comparisons inside formal targets; (2) Feynman perturbation theory sums over virtual quanta, which the owner ruling of 2026-11-21 (no virtual photons) excludes. Disposition (re-scope to math-only / scrap / leave) is on an owner card. Audit: `docs/audits/2026-11-21-physics-claim-scope-recheck.md` on branch `claude/physics-scope-audit-2026-11-21` (4df574c79).

## 2026-11-21 — superseded-premise check (owner instruction 2026-11-21, physics-scope sibling)

Superseded basis found: Feynman perturbation theory relies on virtual quanta, excluded by the 2026-11-21 ruling (no virtual photons), and the title's targets are CODATA/PDG comparisons. Do not work this bean on that basis; disposition on the owner card (re-scope to math-only / scrap / leave).

## 2026-11-21 — RE-SCOPED to math only (owner card "Re-scope to math only", 12:09Z; issue #8810)

Previous title: 'QFT-3: Spinor-Minkowski Herm_2(C) ~= R^{1,3}, UV-Truncated Schwinger Propagator & Pius-Sen Cutkosky Unitarity'

Target: the real-linear isomorphism Herm₂(ℂ) ≅ ℝ⁴ under which det is the Minkowski quadratic form, and X ↦ AXA* for A ∈ SL₂(ℂ) preserves it, kernel ±1. Dropped: UV-truncated Schwinger propagator, worldline bubble and Cutkosky threshold (virtual loops).
