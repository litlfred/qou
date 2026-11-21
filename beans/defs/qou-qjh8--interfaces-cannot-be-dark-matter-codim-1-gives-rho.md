---
# qou-qjh8
title: 'Interfaces CANNOT be dark matter: codim-1 gives rho ~ a^-1 vs DM a^-3; 8.25e-7 short at recombination; sigma^(1/3)=18.9 MeV vs ZKO bound 1 MeV (6775x)'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-07T12:58:02Z
updated_at: 2026-11-21T12:40:00Z
parent: qou-ddmn
---


## Progress (PR #8452)
- Formalized in `folio/quantum-observable-universe/lean/QOU/Eightfold/PolarizationArgumentDiscardDecayWindowFractionSurprisalVolumeTermStepUnitDomainWallDilution.lean` (wired in `QOU.lean`).
- 80-dps numerical witness stamped in `computations/probes/qou_10v9_k6is_kh7e_lsvj_mumr_qjh8_probe.witness.json` (`Commit 1` = `ffa2d78ef5414a49bba12e0efccca6fbb72626d5`, `HEAD` = `078aa49b3db67c82ebbd4ebd6bd00b088ab2f9d9`).

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8452, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.

## 2026-11-21 — physics-scope re-check on main 2ae54ab40 (bean-drain sibling, issue #8810)

Nothing of PR #8452's Lean is on main (batch PR closed). The a⁻¹ vs a⁻³ dilution argument compares a model object with an observed component: it belongs in an empirical-comparison remark, never in a theorem. Audit: `docs/audits/2026-11-21-physics-claim-scope-recheck.md` on branch `claude/physics-scope-audit-2026-11-21` (4df574c79).
