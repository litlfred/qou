---
# qou-dtd3
title: "CORRECTION: T4 probe used S = A_ω·Im \U0001D519₄₁ linearly. But the actual Stokes phenomenon is exponential: δf ~ A_ω·exp(−\U0001D519/ℏ). Also: A_ω is a discrete integer (DT invariant), NOT a continuous phase source. Median resummation is single-valued — cannot tune ϑ_K. The linear formula S = 3κ(ln²q₀ − ϑ²) may be wrong. Need to re-derive the correct S(\U0001D532_K) relation from the bridge equation."
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-07-27T15:17:03Z
updated_at: 2026-10-10T08:30:00Z
parent: qou-avtq
---


## 2026-10-10 — evidence re-check (verification sweep of `qou-avtq`)

**Verdict: OPEN.** The re-derivation from the bridge equation is still owed. The one exponential test (2026-08-01 MISS) used convention-C targets and quotes a stale 4.075 (the witness says 3.937), so it decides nothing in the D frame.

Evidence: The exponential-bridge test was run (`computations/qbeta/qbeta_c3_magnitude_exp_bridge_windings_probe.py`, audit `docs/audits/2026-08-01-c3-magnitude-exp-bridge-canonical-windings-miss.md`). The re-run reproduces the witness: target 3.9369, prediction 1.042/1.040, ΔN 33.26/35.02. Problems: (a) it uses `c3_target_at(...)` with the default `convention="C"` (`qbeta_utils.py:339-340`); (b) the probe text and audit quote target 4.075, but the witness and the re-run give 3.937 (the muon anchor moved from 0.00968 to 0.01002); (c) under ℏ=log q₀ the needed ΔN **is** a canonical pair difference (`…_hbar_log: true`). The derivation of S(𝔙_K) from the bridge equation that the bean asks for was never done.

Status: `todo` → `todo` (unchanged: edited today by another session, or held in-progress).
Checked against qou `main` at `77695711d2`. Probes were re-run only where cheap and decisive. A numeric result counts as evidence only where it reproduces and its precision exceeds the gap it decides; convention-C numbers are not evidence about convention-D claims.
