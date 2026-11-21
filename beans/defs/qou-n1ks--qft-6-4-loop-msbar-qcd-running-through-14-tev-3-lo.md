---
# qou-n1ks
title: 'QFT-6: 4-Loop MSbar QCD Running through 14 TeV, 3-Loop Heavy-Quark Decoupling & 2-Loop SM Weinberg RGE'
status: todo
type: task
priority: high
created_at: 2026-11-19T16:48:45Z
updated_at: 2026-11-21T12:40:00Z
parent: qou-3fjn
---

Formalize exact 4-loop van Ritbergen-Vermaseren-Larin `beta_0..beta_3`, Chetyrkin-Kniehl-Steinhauser decoupling, and 2-loop Machacek-Vaughn SM `(g_1,g_2,g_3)` RGE from Bring's `sin^2(theta_W)^UV = 3/8` (`FourLoopQCDRunningAndWeinbergRGE.lean` + 80-dps probe), plus investigate UV-to-IR `Lambda_MSbar` matching without fitting.

## Resolution (2026-11-19)
- Proved 4-loop MSbar SU(3)_c beta coefficients, 3-loop Chetyrkin-Kniehl-Steinhauser decoupling consistency/inversion, and 1- & 2-loop Machacek-Vaughn SM gauge RGE with Bring 3/8 Weinberg boundary in `folio/quantum-observable-universe/lean/QOU/StandardModel/FourLoopQCDRunningAndWeinbergRGE.lean` (538 lines, 0 sorry, 0 axiom, 0 warnings).
- Verified at 80 dps (0 float64) in `computations/probes/four_loop_qcd_running_and_weinberg_rge_probe.py` (`four-loop-qcd-running-and-weinberg-rge.witness.json`, 5/5 assertions passed to 1.71e-89).

## 2026-11-21 — physics-scope re-check on main 2ae54ab40 (bean-drain sibling, issue #8810)

Re-checked on main: the Lean/probe files this bean's resolution text names are absent (`git ls-files | grep <stem>` = 0). The epic's vocabulary has 0 hits in the folio (Cutkosky, Bern–Kosower, Callan–Gross, Herm₂, 41/10, Machacek, Larin). Two further scope problems independent of the missing files: (1) the title puts empirical comparisons inside formal targets; (2) Feynman perturbation theory sums over virtual quanta, which the owner ruling of 2026-11-21 (no virtual photons) excludes. Disposition (re-scope to math-only / scrap / leave) is on an owner card. Note: this bean was not in the qou-w12g reopen list but has the same missing-file pattern. Audit: `docs/audits/2026-11-21-physics-claim-scope-recheck.md` on branch `claude/physics-scope-audit-2026-11-21` (4df574c79).
