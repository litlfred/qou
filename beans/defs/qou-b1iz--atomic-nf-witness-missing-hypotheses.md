---
# qou-b1iz
title: atomic nf witness missing hypotheses
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-11T00:00:00Z
updated_at: 2026-11-22T21:55:07Z
parent: qou-iqjk
---

File: `folio/quantum-observable-universe/lean/QOU/ParticleInteractions/atomic_nf_witness.lean`
The `atomic_nf_witness` theorem is unprovable. `AtomicNfWitnessContext` provides `F_Pauli`, `trAlt`, and `net` as free unconstrained variables, so `F_Pauli = |trAlt / net|` does not logically follow.



Also known as `atnw` (its former front-matter header id; the beans CLI uses the filename id `atomic_nf_witness`). Recorded 2026-10-04.

- **Round 93 PR (`litlfred/qou#8497`)**: Formalized `NormalFormHypothesisBridgeLedger`, `canonicalNormalFormHypothesisBridgeLedger`, `normal_form_telescoping_bridge`, and `normal_form_cubic_reduction_factor` in `QOU.Foundations.InertCheckerVerdictAuditPerPartitionAtomWordGateNoFitChiralitySeparationNormalFormHypothesisBridgeSeventySevenPartitionCompletion` with 80-dps witness (`HEAD = 25e6a2cd52af041cf68fa20d385161f4542be774`).

## 2026-11-22 — id renamed `atomic_nf_witness` → `qou-b1iz` (bean-hygiene, owner-approved)

Session https://claude.ai/code/session_01Qmmkt95ogQs6aFq9zdMmwF. The old id contained underscores, which the tracker's id pattern `[A-Za-z0-9-]+` rejects, so `scripts/check-beans.sh` reported this file as having no id and every `beans` query missed it. Renamed on the owner's approval of qou-w3yy (project-chat card, 2026-11-22 21:53Z). Content unchanged; the old id stays greppable here.
