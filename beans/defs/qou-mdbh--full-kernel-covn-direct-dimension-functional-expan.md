---
# qou-mdbh
title: 'Full kernel cov(n) direct: dimension-functional expansion vs Plancherel (dim²→dim³)'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-07-25T16:37:35Z
updated_at: 2026-11-21T14:00:00Z
parent: qou-m6dn
---

## Progress Update (Round 90 — lane-cf11)
- Formalized in `folio/quantum-observable-universe/lean/QOU/QBeta/BipartitionTransseriesAndCubicDimensionKernelBrick.lean` with 80-dps probe `computations/probes/bipartition_transseries_and_cubic_dimension_kernel_brick_probe.py` and witness `computations/probes/bipartition-transseries-and-cubic-dimension-kernel-brick.witness.json`.
- PR: https://github.com/litlfred/qou/pull/8339 (`feat/qou-b9cj-m0bv-m6gp-mbz4-mdbh-mssy`, HEAD `8369032c8c6c736ecfb79467000a84fa918a7d04`).

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8339, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.

## 2026-11-21: premise check (hecke-gs-conj sibling, session_01Qmmkt5sJX34MCerjRMERJN; owner: nothing rests on replaced results)
The "Round NN progress" entries above cite batch PRs closed on 2026-11-20 as vacuous or superseded. Their Lean/probe/witness paths are ABSENT on main (checked against main 2ae54ab40 file list). Do not build on them or cite them. Open; this is the dim^2 -> dim^3 obstruction that every route in the epic synthesis hits.
No physics premise in this bean is affected by the rulings in docs/coordination/owner-rulings.md (pure Plancherel combinatorics). Kernel proved for 3<=k<=20 (YoungDiagramKernel.lean:200, kernelValue_nonpos_of_le_twenty); general k open. Status unchanged: an open conjecture stays open.
