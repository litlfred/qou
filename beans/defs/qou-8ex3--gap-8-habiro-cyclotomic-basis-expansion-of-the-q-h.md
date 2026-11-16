---
# qou-8ex3
title: 'GAP-8: Habiro / cyclotomic-basis expansion of the q-heat kernel — expand exp(-mu_lambda s_*) in the (q;q)_n basis rather than Taylor (q-dilog-habiro-ring, z-habiro-ring). Fibre-level object per the AGENTS.md Im(q) fibre-vs-observable rule; Garoufalidis et al 3D index (library/topologicalinvariance3dindex/topological.invariance.3Dindex.pdf) is a topologically-invariant q-series candidate of exactly this type. (parent qou-xu6t)'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-07-28T02:25:44Z
updated_at: 2026-11-16T18:00:00Z
parent: qou-avtq
---


## 2026-10-10 — evidence re-check (verification sweep of `qou-avtq`)

**Verdict: OPEN.** No work recorded. Still an open proposal.

Evidence: Empty body. No producer or witness found for a Habiro/(q;q)_n expansion of the q-heat kernel: grep over `computations/` for heat-kernel files mentioning habiro/cyclotomic finds only unrelated alpha_em/photon probes.

Status: `todo` → `todo` (unchanged: edited today by another session, or held in-progress).
Checked against qou `main` at `77695711d2`. Probes were re-run only where cheap and decisive. A numeric result counts as evidence only where it reproduces and its precision exceeds the gap it decides; convention-C numbers are not evidence about convention-D claims.

## 2026-11-16 — Round 46 execution (`Q-10V9-4 = 1`, PR `litlfred/qou#8144`, commit `8fecf0a5bc64b5831742a0515ad6f634a0202925`)

- **Probe & Witness:** `computations/qbeta/q_heat_kernel_habiro_cyclotomic_expansion_probe.py` & `computations/qbeta/q-heat-kernel-habiro-cyclotomic-expansion.witness.json` (60 dps `mpmath` + exact $\mathbb{Q}[\varepsilon]$ triangular elimination, 0 float64 leaks).
- **Lean 4 Formalization:** `folio/quantum-observable-universe/lean/QOU/QBeta/QHeatKernelHabiroExpansion.lean` (wired into `folio/quantum-observable-universe/lean/QOU.lean`, `0` `sorry`, standard axioms `[propext, Classical.choice, Quot.sound]`):
  - `habiroPartialSum`, `habiroPartialSum_eq_of_pow_eq_one` (exact finite truncation at $N$-th roots of unity $q^N = 1$).
  - `qPoch_one_in_eps`, `qPoch_two_in_eps`, `qPoch_three_in_eps`, `heatKernelHabiroCoeff`, `triangular_solve_order3_unique`, `habiro_quadratic_jet_remainder`, `habiro_cubic_jet_remainder` ($a_0 = 1, a_1 = \alpha, a_2 = \alpha^2/4, a_3 = \alpha^2(2\alpha+3)/72, a_4 = \alpha^2(\alpha+3)^2/576$).
  - `habiroTerm_reflection`, `habiroTerm_abs_ge_of_one_lt`, `habiro_heat_kernel_trichotomy` (exact $q$-Borel reflection factor $q^{n(n+1)/2}$ and archimedean divergence on $q_0 > 1$ past turnaround threshold $N_0 = 6$).
