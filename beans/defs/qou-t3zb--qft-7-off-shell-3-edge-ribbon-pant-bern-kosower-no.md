---
# qou-t3zb
title: 'QFT-7: Off-Shell 3-Edge Ribbon Pant / Bern-Kosower Non-Abelian Gluon Worldline Vertex V_3(T_1,T_2,T_3)'
status: todo
type: task
priority: high
created_at: 2026-11-19T16:48:45Z
updated_at: 2026-11-21T12:40:00Z
parent: qou-3fjn
---

Derive the off-shell 3-edge worldline vertex from the braided Hecke pant cobordism to complete the Schwinger-to-Feynman functor `F_SW` for non-Abelian gauge loops without Faddeev-Popov ghosts.

## Resolution (2026-11-19)
- Proved 8-generator SU(3)_c Gell-Mann Fierz completeness, 8-index contracted Jacobi, S_3 Bose symmetry, off-shell ghost-free Slavnov-Taylor Ward identity, and Bern-Kosower worldline pinch + spin decomposition in `folio/quantum-observable-universe/lean/QOU/StandardModel/RibbonPantBernKosowerGluonVertex.lean` (576 lines, 0 sorry, 0 axiom, 0 warnings).

## 2026-11-21 — physics-scope re-check on main 2ae54ab40 (bean-drain sibling, issue #8810)

Re-checked on main: the Lean/probe files this bean's resolution text names are absent (`git ls-files | grep <stem>` = 0). The epic's vocabulary has 0 hits in the folio (Cutkosky, Bern–Kosower, Callan–Gross, Herm₂, 41/10, Machacek, Larin). Two further scope problems independent of the missing files: (1) the title puts empirical comparisons inside formal targets; (2) Feynman perturbation theory sums over virtual quanta, which the owner ruling of 2026-11-21 (no virtual photons) excludes. Disposition (re-scope to math-only / scrap / leave) is on an owner card. Note: this bean was not in the qou-w12g reopen list but has the same missing-file pattern. Audit: `docs/audits/2026-11-21-physics-claim-scope-recheck.md` on branch `claude/physics-scope-audit-2026-11-21` (4df574c79).

## 2026-11-21 — superseded-premise check (owner instruction 2026-11-21, physics-scope sibling)

Superseded basis found: Feynman perturbation theory relies on virtual quanta, excluded by the 2026-11-21 ruling (no virtual photons), and the title's targets are CODATA/PDG comparisons. Do not work this bean on that basis; disposition on the owner card (re-scope to math-only / scrap / leave).
