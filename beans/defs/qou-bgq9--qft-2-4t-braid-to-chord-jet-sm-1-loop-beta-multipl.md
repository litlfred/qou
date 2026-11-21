---
# qou-bgq9
title: 'QFT-2: 4T Braid-to-Chord Jet, SM 1-Loop Beta Multiplicities (7, 19/6, -41/10), (g-2)_e Pin Audit & DIS Valence Moments'
status: todo
type: task
priority: critical
created_at: 2026-11-19T16:48:44Z
updated_at: 2026-11-21T12:40:00Z
parent: qou-3fjn
---

`QOU/StandardModel/InfraredQFTSubsumptionAndPartonMoments.lean` (`935` lines, wired in `QOU.lean`) + `qft_subsumption_gm2_alphas_and_dis_probe.py` (`47875996083d`) — Red-Team PASS.

## Reopened (owner instruction 2026-11-20, via W12)
This bean was set to completed by local commits on `cat/cat-harness/beans` (e223ed1 / 4fcd2cb / 89bb5e0, 2026-11-19, `litlfred@fenugreek.home`, no session trailer). The Lean / probe / witness files its resolution names are not on main, on any branch, or in any PR found by the bean id (measured 2026-11-20). See GAP bean qou-w12g.

## 2026-11-21 — physics-scope re-check on main 2ae54ab40 (bean-drain sibling, issue #8810)

Re-checked on main: the Lean/probe files this bean's resolution text names are absent (`git ls-files | grep <stem>` = 0). The epic's vocabulary has 0 hits in the folio (Cutkosky, Bern–Kosower, Callan–Gross, Herm₂, 41/10, Machacek, Larin). Two further scope problems independent of the missing files: (1) the title puts empirical comparisons inside formal targets; (2) Feynman perturbation theory sums over virtual quanta, which the owner ruling of 2026-11-21 (no virtual photons) excludes. Disposition (re-scope to math-only / scrap / leave) is on an owner card. Audit: `docs/audits/2026-11-21-physics-claim-scope-recheck.md` on branch `claude/physics-scope-audit-2026-11-21` (4df574c79).

## 2026-11-21 — superseded-premise check (owner instruction 2026-11-21, physics-scope sibling)

Superseded basis found: Feynman perturbation theory relies on virtual quanta, excluded by the 2026-11-21 ruling (no virtual photons), and the title's targets are CODATA/PDG comparisons. Do not work this bean on that basis; disposition on the owner card (re-scope to math-only / scrap / leave).
