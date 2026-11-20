---
# qou-qd27
title: 'PROBE C4: Bring Sigma_4 adjoint Reidemeister torsion as a non-algebraic HH^1 pairing'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-07T17:21:00Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-b1je
---

The wall's non-algebraic clause. Does the adjoint Reidemeister torsion of Bring Sigma_4 (genus 4, S_5) give a provably-transcendental regulator pairing on H^1(Sigma_4)? Framing doc: docs/audits/2026-08-07-probe-c4-bring-adjoint-torsion-framing.md. GATED on #4532 Clausen infra + a corpus torsion definition. Next step is COMPUTE (extend merged 1-loop torsion law qou-k00d/qou-pn5j to Sigma_4 NZ data), NOT a premature axiomatized class (anti-laundering). Coordination note posted on #4532.

## Progress Update (Round 92 — lane-cf11)
- Formalized in `folio/quantum-observable-universe/lean/QOU/QBeta/NucleonOrderingAndBringAdjointTorsionBrick.lean` with 80-dps probe `computations/probes/nucleon_ordering_and_bring_adjoint_torsion_brick_probe.py` and witness `computations/probes/nucleon-ordering-and-bring-adjoint-torsion-brick.witness.json`.
- PR: https://github.com/litlfred/qou/pull/8348 (`feat/qou-b9cj-q6h7-qd27-qint-r91v-tvok`, HEAD `e0985c4fc3ff765e1935e3343005512aaca69b2b`).

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8348, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
