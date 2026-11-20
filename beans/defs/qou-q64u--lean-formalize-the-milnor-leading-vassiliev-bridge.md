---
# qou-q64u
title: Lean-formalize the Milnor = leading-Vassiliev bridge (Habegger–Masbaum 2000; Bar-Natan 1995; Meilhan–Yasuhara)
status: todo
type: task
priority: normal
tags:
    - formalization
    - knot-theory
    - reorg-2026-10-04
created_at: 2026-08-01T19:01:04Z
updated_at: 2026-11-20T16:06:50Z
parent: b9cj
---

The general proof of the exact-order Milnor law (order(D_A) = 2(A−1), i.e. leading coeff = μ̄(12…A) ≠ 0) rests on: the first non-vanishing Vassiliev invariant of an A-component Brunnian link at degree 2(A−1) is ±μ̄(12…A) = ±1. Currently CITATION-ONLY (Bar-Natan, 'On the Vassiliev knot invariants', 1995; Habegger–Masbaum, 'The Kontsevich integral and Milnor's invariants', 2000; Meilhan–Yasuhara). The Vassiliev/finite-type infra scaffold (branch claude/vassiliev-finite-type-infra-2026-08-01) states this as an instance-less conjecture class — NOT axiomatized. This task: eventually Lean-prove the bridge on top of that scaffold (chord diagrams → 4T → weight systems → finite-type invariants → Kontsevich universality → the Milnor bridge). Large multi-session effort; caveat: verify the cited theorems' exact hypotheses match our Brunnian iterated-commutator generator (papers are not infallible / may need adaptation).


## Round 81 Execution Note (2026-11-17T08:44:47Z)

- **Status**: `in-progress` (PR awaiting merge; no unilateral closure).
- **PR**: [`litlfred/qou#8288`](https://github.com/litlfred/qou/pull/8288) (`feat/qou-b9cj-6poy-q64u-regz-w3eg-xq3f`, HEAD `3f9d9bb7e2af7c3353cc2779b429d84aae572cda`).
- **Lean Module**: `folio/quantum-observable-universe/lean/QOU/QBeta/NeumannZagierDeterminantAndVassilievMilnorBrick.lean` (wired into `QOU.lean`, compiled with Lean 4.24.0, 0 findings across all 7 static Lean audits).
- **80-dps Probe & Witness**: `computations/probes/neumann_zagier_determinant_and_vassiliev_milnor_brick_probe.py` & `computations/probes/neumann-zagier-determinant-and-vassiliev-milnor-brick.witness.json` (`scriptCommitSha = b4b438fbfa2d06efdb0e7b096ec45a7a03973e2b`, `scriptHash = cf7e93178098`, `outputHash = c7210b5eb72906d3c61c7e19a0c46a0a3457be0f703d99c7dd7475108da381b1`).

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8288, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
