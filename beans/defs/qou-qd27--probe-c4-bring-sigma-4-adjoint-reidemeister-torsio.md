---
# qou-qd27
title: 'PROBE C4: Bring Sigma_4 adjoint Reidemeister torsion as a non-algebraic HH^1 pairing'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-07T17:21:00Z
updated_at: 2026-10-04T15:22:11Z
parent: qou-b1je
---

The wall's non-algebraic clause. Does the adjoint Reidemeister torsion of Bring Sigma_4 (genus 4, S_5) give a provably-transcendental regulator pairing on H^1(Sigma_4)? Framing doc: docs/audits/2026-08-07-probe-c4-bring-adjoint-torsion-framing.md. GATED on #4532 Clausen infra + a corpus torsion definition. Next step is COMPUTE (extend merged 1-loop torsion law qou-k00d/qou-pn5j to Sigma_4 NZ data), NOT a premature axiomatized class (anti-laundering). Coordination note posted on #4532.

## Progress Update (Round 92 — lane-cf11)
- Formalized in `folio/quantum-observable-universe/lean/QOU/QBeta/NucleonOrderingAndBringAdjointTorsionBrick.lean` with 80-dps probe `computations/probes/nucleon_ordering_and_bring_adjoint_torsion_brick_probe.py` and witness `computations/probes/nucleon-ordering-and-bring-adjoint-torsion-brick.witness.json`.
- PR: https://github.com/litlfred/qou/pull/8348 (`feat/qou-b9cj-q6h7-qd27-qint-r91v-tvok`, HEAD `e0985c4fc3ff765e1935e3343005512aaca69b2b`).
