---
# qou-ik5e
title: 'Phase 3 route 3: exact Jack β-derivative dE_β[Σ3]/dβ|_{β=2} (engine for route 1)'
status: todo
type: task
priority: high
tags:
    - reorg-2026-10-04
created_at: 2026-07-24T16:21:37Z
updated_at: 2026-11-21T14:00:00Z
parent: qou-m6dn
---


## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-07-24 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

## Round 86 Progress (`litlfred/qou#8317`)
- **Lean 4.24.0 Module**: `folio/quantum-observable-universe/lean/QOU/QBeta/BesserDeJeuDilogAndMayaHookVarianceBrick.lean` (`0` `sorry`, `0` `axiom`, `0` warnings; `0` CRITICAL, `0` major, `0` advisory across all 7 static audits).
- **80-dps Probe & Witness**: `computations/probes/besser_de_jeu_dilog_and_maya_hook_variance_brick_probe.py` & `computations/probes/besser-de-jeu-dilog-and-maya-hook-variance-brick.witness.json` (`scriptCommitSha = 4d5b778d1b105fc173cd0374f785742bf18bf727`, HEAD `9739386c32e9d7fc534b2e9229d93f0174f0cf95`, `allPassed = true`).

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8317, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.

## 2026-11-21: premise check (hecke-gs-conj sibling, session_01Qmmkt5sJX34MCerjRMERJN; owner: nothing rests on replaced results)
The "Round NN progress" entries above cite batch PRs closed on 2026-11-20 as vacuous or superseded. Their Lean/probe/witness paths are ABSENT on main (checked against main 2ae54ab40 file list). Do not build on them or cite them. Jack beta-derivative route open; no live main artifact for it.
No physics premise in this bean is affected by the rulings in docs/coordination/owner-rulings.md (pure Plancherel combinatorics). Kernel proved for 3<=k<=20 (YoungDiagramKernel.lean:200, kernelValue_nonpos_of_le_twenty); general k open. Status unchanged: an open conjecture stays open.
