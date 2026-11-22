---
# qou-v0pn
title: 'F3-infra: build Mathlib-absent Sniady genus-expansion machinery for Delta_lambda covariance kernel T3<=0'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-07-19T17:13:51Z
updated_at: 2026-11-22T21:15:00Z
parent: b9cj
---

## Round 78 Formalization Update (2026-11-17)

- **PR**: https://github.com/litlfred/qou/pull/8272 (`be42fef123e1a988fe70707cab448f5763ca2cfc`)
- **Lean Module**: `folio/quantum-observable-universe/lean/QOU/QBeta/FiveTwoAdjointTorsionAndSniadyGenusCovarianceBrick.lean` (wired into `folio/quantum-observable-universe/lean/QOU.lean`, verified with `lean -DautoImplicit=false -s 65536` exit 0, 0 `sorry`/`axiom`/`native_decide`, 0 findings across all 7 static Lean audits).
- **80-dps Probe & Witness**: `computations/probes/five_two_adjoint_torsion_and_sniady_genus_covariance_brick_probe.py` (`scriptCommitSha: f9d16753dbb36bbe177e31872e1864ef809ebf0e`) and `computations/probes/five-two-adjoint-torsion-and-sniady-genus-covariance-brick.witness.json` (`allPassed: true`).

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8272, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.

## 2026-11-22: premise check (session_01Qmmkt8qREoAzcE1YKVx5nz)
The Round 78 entry cites PR #8272, which is not merged, and its Lean file (QOU/QBeta/FiveTwoAdjointTorsionAndSniadyGenusCovarianceBrick.lean) is absent on main 3c4c98fcc. Do not build on it. Note also that the route this infrastructure serves (Śniady genus expansion for the kernel) was eliminated as route #11 (docs/audits/2026-07-25-covariance-kernel-A5-genus-eliminated-A4-lean.md; sibling qou-t5m1 scrapped 2026-11-22). Left todo, not scrapped: the machinery could still serve the k5r5 / M_1 work, which lives inside A. Owner's call.
