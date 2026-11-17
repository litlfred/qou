---
# qou-z7sb
title: 'F3 research: Δ_λ covariance kernel ∀k via Śniady genus expansion (Mathlib-absent machinery scoped)'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-07-19T01:52:06Z
updated_at: 2026-11-17T08:12:00Z
parent: b9cj
---

## Round 78 Formalization Update (2026-11-17)

- **PR**: https://github.com/litlfred/qou/pull/8272 (`be42fef123e1a988fe70707cab448f5763ca2cfc`)
- **Lean Module**: `folio/quantum-observable-universe/lean/QOU/QBeta/FiveTwoAdjointTorsionAndSniadyGenusCovarianceBrick.lean` (wired into `folio/quantum-observable-universe/lean/QOU.lean`, verified with `lean -DautoImplicit=false -s 65536` exit 0, 0 `sorry`/`axiom`/`native_decide`, 0 findings across all 7 static Lean audits).
- **80-dps Probe & Witness**: `computations/probes/five_two_adjoint_torsion_and_sniady_genus_covariance_brick_probe.py` (`scriptCommitSha: f9d16753dbb36bbe177e31872e1864ef809ebf0e`) and `computations/probes/five-two-adjoint-torsion-and-sniady-genus-covariance-brick.witness.json` (`allPassed: true`).

