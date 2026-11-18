---
# qou-mp3m
title: 'R3: prove (1)↔(3) Jones = Potts/Temperley-Lieb partition function (state-sum = vertex-model Z)'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-02T18:33:15Z
updated_at: 2026-10-04T15:23:10Z
parent: qou-0cyu
---

Research, historically grounded. Jones (1985) derived the polynomial FROM the Temperley-Lieb algebra of the Potts-model transfer matrix (Baxter). Kauffman bracket IS a lattice state-sum = vertex-model Z. Prove the QOU Markov-trace knot state-sum equals a Potts/vertex partition function. Cite Jones 1985 + Baxter. Corpus: skein-mass-relation-proof, braiding-unit-circle-convention.

## Round 70 Update (lane-e667)
- Formalized in `folio/quantum-observable-universe/lean/QOU/Foundations/DyadicShellSummationCentralIdempotentFiberAdjointPlanarTransferPivotalMonoidality.lean`
- 80-dps mpmath probe: `computations/probes/dyadic_shell_summation_central_idempotent_fiber_adjoint_planar_transfer_pivotal_monoidality_probe.py`
- Witness: `computations/probes/dyadic-shell-summation-central-idempotent-fiber-adjoint-planar-transfer-pivotal-monoidality.witness.json` (`scriptHash = 65da05b0114c`, `scriptCommitSha = e3073696f062c7ba6a16becdc35a768b99bba3c2`)
- PR: https://github.com/litlfred/qou/pull/8382 (`eaf480ab4ed647b2e4dc199177fe5aeacf717fb8`)
