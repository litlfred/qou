---
# qou-su6h
title: Scaffold Jucys-Murphy
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-07-08T14:00:13Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-1oif
---


## Scoping note 2026-08-01 — blocked on missing Mathlib infra (NOT a session task)

Piece B = `(1/n!) Σ_{λ⊢n} dim(λ)² Σ_c content(c)² = C(n,2)` (the JM content-square
mean, the `n(n-1)` half of Identity I). Unlike Piece A (now proven sorry-free,
`QOU.BraidKnot.PieceA.pieceA` — pure Young-diagram combinatorics), Piece B is
intrinsically a **sum over all partitions weighted by dim²**, which needs one of:
Jucys–Murphy elements in `ℂ[S_n]` + the regular-character coefficient formula, OR
RSK + `Σ_λ (f^λ)² = n!`. **Mathlib provides NONE of these** (grep 2026-08-01:
no RSK, no Jucys–Murphy, no Specht modules, no hook-length formula, no S_n
character theory — only `YoungDiagram` + `SemistandardTableau`). So a clean
sorry-free general proof is a **major multi-week Mathlib contribution**, not a
session task. The math itself is settled (JM argument, brute-verified n=2..6 in
the corpus; and Identity I is decide-verified n≤8 in `WLambdaDefectClosedForm`).
Honest status: OPEN, blocked on infra; do NOT axiomatize JM and pass it off as a
proof (anti-laundering). A conditional reduction "Piece A + (Σf^λ²=n!) ⟹ Piece B"
is possible but still rests on the RSK gap.

## Round 71 Update (lane-e667)
- Formalized in `folio/quantum-observable-universe/lean/QOU/Foundations/RigidGapBraidedThreeStrandClosureWindowCumulativeCommutantBilinearCyclicity.lean`
- 80-dps mpmath probe: `computations/probes/rigid_gap_braided_three_strand_closure_window_cumulative_commutant_bilinear_cyclicity_probe.py`
- Witness: `computations/probes/rigid-gap-braided-three-strand-closure-window-cumulative-commutant-bilinear-cyclicity.witness.json` (`scriptHash = bb0e9e32b9629d9789227d338ed551e0d79651afa39f07ae980772f540b2ef6a`, `scriptCommitSha = b704b4dd3d9c5480efb9471bb8860000327215d9`)
- PR: https://github.com/litlfred/qou/pull/8385 (`7154445b1b227674fa957c8eed34f505f5e0eeae`)

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8385, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
