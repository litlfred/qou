---
# zqtv
title: 'Probe: qbeta_fmap_power_class_prune.py — exact ε-series of Δtr_M^m, half-integer-u + c_1 obstructions'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-07-06T11:48:04Z
updated_at: 2026-11-15T17:33:15Z
parent: qou-avtq
blocked_by:
    - qou-cds1
---


## 2026-10-10 — evidence re-check (verification sweep of `qou-avtq`)

**Verdict: EVIDENCE-UNRELIABLE.** The prune reproduces, but its input Δtr_M is the convention-C object. The D-frame atom-word difference is a different rational function in integer powers of q, so the "half-integer u" obstruction may not even arise there. Rebuild the bridge witness from the D atomic witness and re-run before citing the pure-power refutation.

Evidence: Re-ran `computations/probes/qbeta_fmap_power_class_prune.py`: exit 0, all pass, payload reproduces. Its input Δtr_M is read from `habiro/habiro-mode-to-ladder-bridge.witness.json` (computedAt 2026-08-08, no q0Anchor), which carries half-integer powers of q (z_C). I evaluated the current convention-D `habiro-coefficients-atomic.witness.json` tr_M(n)−tr_M(p) = (q−1)(q+1)(q⁴+1)(2q¹²−6q¹⁰+…+2)/(4q⁷(q²+1)²), and it is not equal to the bridge's Δtr_M (sympy simplify ≠ 0). The pinned a_n (C13) and the half-integer-u obstruction are therefore convention-C facts.

Status: `todo` → `todo` (unchanged: edited today by another session, or held in-progress).
Checked against qou `main` at `77695711d2`. Probes were re-run only where cheap and decisive. A numeric result counts as evidence only where it reproduces and its precision exceeds the gap it decides; convention-C numbers are not evidence about convention-D claims.
