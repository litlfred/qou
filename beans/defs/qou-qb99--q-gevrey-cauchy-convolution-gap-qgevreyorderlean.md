---
# qou-qb99
title: q-Gevrey Cauchy convolution gap (QGevreyOrder.lean)
status: completed
pr: 8204
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-12T10:23:09Z
updated_at: 2026-11-21T12:40:00Z
parent: qou-frzo
---

## Progress Note (2026-11-16, PR #8204)
- Formalized in `folio/quantum-observable-universe/lean/QOU/MassTheory/QGevreyCauchyAndFWGGMStokes.lean` (wired into `QOU.lean`, `0` `sorry`, `0` `axiom`, `0 CRITICAL / 0 advisory` across all 8 Lean static vacuity/borrowed-name audits).
- Verified by 80-dps `mpmath` / exact rational probe `computations/probes/qgevrey_cauchy_and_fw_ggm_stokes_probe.py` and witness `computations/probes/qgevrey-cauchy-and-fw-ggm-stokes.witness.json` (`scriptCommitSha: 8ee650e779786706f931cf4f825d18b2810370eb`, `scriptHash: 7ed9e0953101`, `allPassed: true`, `0` raw `float64` fields).
- PR: https://github.com/litlfred/qou/pull/8204 (`6b9e46ecf45f518a03c0a6fb1de251bf59b285da`).


## 2026-11-21T12:40:00Z — alien-calculus drain (thread "Build the q-native alien calculus")

**Done on main; closing.** The q-Gevrey Cauchy convolution gap in `QGevreyOrder.lean` is closed on main 2ae54ab401 by `cauchyMul_order` (sorry-free, re-verified lean-direct exit 0, standard axioms), with the counterexamples `cauchyMul_order_unhypothesised_false` / `cauchyMul_order_noCancellation_insufficient` showing its hypotheses are needed. Batch PR #8204 (W4 triage: NEEDS-REWORK, lean-direct FAIL) is not needed for this. Superseded-premise check: none.
