---
# qou-xs2c
title: 'M1 machinery: explicit de-poissonization O(1/n) constant (reuse GaussianTailBound/GaussianSumBound)'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-29T01:34:21Z
updated_at: 2026-11-21T14:00:00Z
parent: qou-m6dn
---

## Progress Update (Round 94 — PR #8360)

- **Lean 4.24.0 Brick**: `folio/quantum-observable-universe/lean/QOU/QBeta/MagnitudeAssemblyAndConventionFrameBrick.lean` (`0` `sorry`, `0` `axiom`, `0` warnings; `0 CRITICAL, 0 major, 0 advisory` across all 7 directory-mode AST audits).
- **80-dps Probe & Witness**:
  - Probe: `computations/probes/qou_w49j_wjw8_wuxx_wy2h_xs2c_magnitude_and_frame_probe.py` (Commit 1: `f052782a9424286a40e40154d7ef1d0ab55a6d3e`, `scriptHash = 35f305f18243`).
  - Witness: `computations/probes/qou_w49j_wjw8_wuxx_wy2h_xs2c_magnitude_and_frame_probe.witness.json` (Commit 2 / HEAD: `687a015fcc42c84733dfecead6ca9f6e13e3d31d`, `allPassed = true`, `rawFloatCount = 0`).
- **PR**: `litlfred/qou#8360` (`feat/qou-b9cj-w49j-wjw8-wuxx-wy2h-xs2c`).

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8360, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.

## 2026-11-21: premise check (hecke-gs-conj sibling, session_01Qmmkt5sJX34MCerjRMERJN; owner: nothing rests on replaced results)
The "Round NN progress" entries above cite batch PRs closed on 2026-11-20 as vacuous or superseded. Their Lean/probe/witness paths are ABSENT on main (checked against main 2ae54ab40 file list). Do not build on them or cite them. Open; no live main artifact for the O(1/n) de-poissonization constant.
No physics premise in this bean is affected by the rulings in docs/coordination/owner-rulings.md (pure Plancherel combinatorics). Kernel proved for 3<=k<=20 (YoungDiagramKernel.lean:200, kernelValue_nonpos_of_le_twenty); general k open. Status unchanged: an open conjecture stays open.
