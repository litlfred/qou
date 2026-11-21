---
# qou-qssg
title: 'QFT-5: Chiral Weyl-Dirac Clifford Algebra, Callan-Gross F_2 = 2x F_1, 1-Loop F_L Moments & Worldline DIS Cross-Section'
status: todo
type: task
priority: high
created_at: 2026-11-19T16:48:45Z
updated_at: 2026-11-21T12:40:00Z
parent: qou-3fjn
---

`QOU/StandardModel/DiracWeylCliffordCallanGrossAndDISCrossSection.lean` + `dirac_callan_gross_and_dis_cross_section_probe.py` completing verification in `b7ebd36b`.

## Resolution (2026-11-19)

Completed (`0 sorry, 0 axiom`, Red-Team UNCONDITIONAL PASS): `QOU/StandardModel/DiracWeylCliffordCallanGrossAndDISCrossSection.lean` (756 lines) + 80-dps `dirac_callan_gross_and_dis_cross_section_probe.py` formalizing `Cl(1,3)` Weyl/Dirac traces, unpolarized hadronic tensor contraction, partonic Callan-Gross `F_2 = 2x F_1` (`F_L^(0) = 0`), Altarelli-Martinelli NLO longitudinal coefficient `C_{L,q}^{(1)}(x) = (8/3)x`, and full 1-loop singlet `(qq, qg; gq, gg)` DGLAP anomalous matrix.

## Reopened (owner instruction 2026-11-20, via W12)
This bean was set to completed by local commits on `cat/cat-harness/beans` (e223ed1 / 4fcd2cb / 89bb5e0, 2026-11-19, `litlfred@fenugreek.home`, no session trailer). The Lean / probe / witness files its resolution names are not on main, on any branch, or in any PR found by the bean id (measured 2026-11-20). See GAP bean qou-w12g.

## 2026-11-21 — physics-scope re-check on main 2ae54ab40 (bean-drain sibling, issue #8810)

Re-checked on main: the Lean/probe files this bean's resolution text names are absent (`git ls-files | grep <stem>` = 0). The epic's vocabulary has 0 hits in the folio (Cutkosky, Bern–Kosower, Callan–Gross, Herm₂, 41/10, Machacek, Larin). Two further scope problems independent of the missing files: (1) the title puts empirical comparisons inside formal targets; (2) Feynman perturbation theory sums over virtual quanta, which the owner ruling of 2026-11-21 (no virtual photons) excludes. Disposition (re-scope to math-only / scrap / leave) is on an owner card. Audit: `docs/audits/2026-11-21-physics-claim-scope-recheck.md` on branch `claude/physics-scope-audit-2026-11-21` (4df574c79).
