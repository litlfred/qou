---
# qou-jh3m
title: 'M1 machinery: ratio propagation m=rho_P-sigma_D/sigma_A -> explicit C -> verify N0<=78'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-29T01:34:21Z
updated_at: 2026-11-21T14:00:00Z
parent: qou-m6dn
---

## Round 87 Progress (`litlfred/qou#8326`)
- **Lean 4.24.0 Module**: `folio/quantum-observable-universe/lean/QOU/QBeta/JetHorizonHabiroAndSteinMarginBrick.lean` (`0` `sorry`, `0` `axiom`, `0` warnings; `0` CRITICAL, `0` major, `0` advisory across all directory-mode static audits).
- **80-dps Probe & Witness**: `computations/probes/jet_horizon_habiro_and_stein_margin_brick_probe.py` & `computations/probes/jet-horizon-habiro-and-stein-margin-brick.witness.json` (`scriptCommitSha = 34352b344244b9e4cceaf3e3a4c56aa375f7bdc5`, HEAD `10540538cb20efacf68a8b53a97722f79167a3a5`, `allPassed = true`).

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8326, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.

## 2026-11-21: premise check (hecke-gs-conj sibling, session_01Qmmkt5sJX34MCerjRMERJN; owner: nothing rests on replaced results)
The "Round NN progress" entries above cite batch PRs closed on 2026-11-20 as vacuous or superseded. Their Lean/probe/witness paths are ABSENT on main (checked against main 2ae54ab40 file list). Do not build on them or cite them. Open; the reduction skeleton m1_pos_all_of_cs_inputs (YoungDiagramKernelCSMargin.lean:110) is on main and still needs the explicit inputs from tvok/po72/xs2c.
No physics premise in this bean is affected by the rulings in docs/coordination/owner-rulings.md (pure Plancherel combinatorics). Kernel proved for 3<=k<=20 (YoungDiagramKernel.lean:200, kernelValue_nonpos_of_le_twenty); general k open. Status unchanged: an open conjecture stays open.
