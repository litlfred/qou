---
# qou-rlkw
title: 'Infra: compact quantum dilogarithm phi_q'
status: in-progress
pr: 8210
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-04T01:39:43Z
updated_at: 2026-11-22T21:45:00Z
parent: qou-r9ih
---

Blocks: neutron_proton_splitting (1), phi_q_tower_jsj_bridge (1), ToroidalHarmonicsBasis (1 — Liouville-Green ODE). Need phi_q formal definition + Faddeev's functional equation.

## Progress Note (2026-11-16, PR #8210)
- Formalized in `folio/quantum-observable-universe/lean/QOU/QBeta/CompactQuantumDilogAndSaddleOffset.lean` (wired into `QOU.lean`, `0` `sorry`, `0` `axiom`, `0 CRITICAL / 0 advisory` across all 8 Lean static vacuity/borrowed-name audits).
- Verified by 80-dps `mpmath` / exact rational probe `computations/probes/compact_quantum_dilog_and_saddle_offset_probe.py` and witness `computations/probes/compact-quantum-dilog-and-saddle-offset.witness.json` (`scriptCommitSha: 4755c87e9f5eee61dab667d125dbf7cba1a93d8b`, `allPassed: true`, `0` raw `float64` fields).
- PR: https://github.com/litlfred/qou/pull/8210 (`539652a881d79d302fbe60283d4f961bd748a742`).

## 2026-11-22 — wave-2 review of the claiming PR (thread "Work dilogarithm and Bloch beans")

The claim on this bean comes from PR #8210 (`QOU/QBeta/CompactQuantumDilogAndSaddleOffset.lean`, opened 2026-11-16/17, still open, `mergeable_state: dirty`). I read every theorem in that file. Each one is an identity in scalar variables over `ℚ` or `ℝ` (`ring` / `linarith` / `field_simp`), and where the bean's claim appears it appears as a hypothesis (for example `#8224` proves `A_ω = 3` from the hypothesis `a_omega_phi = 3`). No theorem touches the bean's actual objects (no `LiTwo`, `blochD`, `Φ_b`, state integral, measure or limit). **So PR #8210 does not discharge this bean.** The W4 triage (PR #8531, `docs/coordination/2026-11-20-batch-pr-triage.md` on that branch) listed it as NEEDS-REWORK for conflicts only, because its scan deliberately does not flag real- or rational-typed one-liners.

Status left unchanged: resetting the claim and closing the PR are the owner's call, and the recommendation went to the coordinator. The work this bean describes is still open, as stated above this note.
