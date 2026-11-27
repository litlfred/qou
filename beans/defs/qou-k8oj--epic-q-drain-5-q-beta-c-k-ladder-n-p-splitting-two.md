---
# qou-k8oj
title: 'EPIC [Q-Drain-5]: Q_beta c_k Ladder, n-p Splitting & Two-Loop 1-ppQ Radiative Dressings'
status: todo
type: epic
priority: high
tags:
    - compute-accuracy
created_at: 2026-11-23T20:55:47Z
updated_at: 2026-11-27T14:18:36Z
parent: qou-hksc
blocking:
    - qou-xip2
---

**Theme:** Q_beta c_k Ladder, n-p Splitting & Two-Loop 1-ppQ Radiative Dressings
**Rationale:** Attacks L2 1-ppQ proton-muon 2-loop dressing (PPQ-2/3), Convention-D Q_beta Habiro rungs c_3/c_4, and n-p braid vs traced-product split.
**Child Beans (13):** `qou-ftas`, `qou-cds1`, `qou-cds2`, `qou-51yf`, `qou-q1a4`, `qou-jwl8`, `qou-bg3w`, `qou-q2oa`, `qou-qb8e`, `qou-z4ba`, `qou-jqhk`, `qou-l4t2`, `qou-qcov`

### Prioritized Beans in This Batch
- **`qou-ftas`** (`critical`, `todo`) — PPQ-2 (L2): Two-Loop (alpha/pi)^2 Radiative Mass Dressing Between 3-Strand Proton & 4_1 Muon (8.058 ppb -> < 0.22 ppb)
- **`qou-cds1`** (`high`, `in-progress`) — S1 (SCIENCE): re-derive the Q_beta c_k ladder under D — not a z-swap, and that is proved *(Rule 13a: 0-instance classes: `BarInvariant, BarInvolution, ComplexVolumeMatch, MassTraceIsFibreCategorical, QBetaSingleHabiroGenerator, QbetaHabiroTaylorBridgeClass`; Rule 13a `stays open`/conjecture guard)*
- **`qou-cds2`** (`high`, `in-progress`) — S2 (SCIENCE): pyhecke.gram.z and the Gram singularity — the ruling answers the convention, not the singularity *(Rule 13a: Rule 13a `stays open`/conjecture guard)*
- **`qou-51yf`** (`high`, `todo`) — Closed-Form Convention-D Q_beta / m_n Habiro-Kashiwara Rungs c_3, c_4 on Mirror-Projected alpha_D^proj + Two-Term QED
- **`qou-q1a4`** (`high`, `todo`) — Trace where u and d first become distinguished in the γγ chain (photons → condensate → nucleons) *(Rule 13a: 0-instance classes: `ScaleHypothesis`; Rule 13a `stays open`/conjecture guard)*
- **`qou-jwl8`** (`high`, `todo`) — The traced_volume product ∏ᵢ∏_{j>i}(σᵢ+dᵢⱼ) is not the half-twist trace
- **`qou-bg3w`** (`high`, `in-progress`) — Which element is Delta? Two nucleon-word models (1-/2-crossing vs 11-crossing) both carry the name, and a possible third in pyhecke
- **`qou-q2oa`** (`high`, `in-progress`) — The ladder phase alpha has no derivation from the actual Wedderburn weights
- **`qou-qb8e`** (`high`, `in-progress`) — HH^1 carrier: the MAGNITUDE channel — the actual open gate for c_3 *(Rule 13a: Rule 13a `stays open`/conjecture guard)*
- **`qou-z4ba`** (`high`, `todo`) — The c1 mirror asymmetry has the WRONG SIGN, 0/230 against AME -- and it is scale-free
- **`qou-jqhk`** (`high`, `todo`) — PPQ-3 (L2): Two-Loop Electroweak / Top-Yukawa Threshold Correction to Bring-Schwinger v_EW (29.37 ppb -> < 2.57 ppb)
- **`qou-l4t2`** (`high`, `todo`) — Closed-Form Two-Loop O(alpha_EM^2) Bloch-B_3(C) / zeta(3) Schwinger Coefficient c_2 in 1/alpha_EM *(Rule 13a: Rule 13a `stays open`/conjecture guard)*
- **`qou-qcov`** (`high`, `todo`) — GAP: braid-covariant non-pairwise QED insertion with derived M-coefficient b and scale c_em *(Rule 13a: Rule 13a `stays open`/conjecture guard)*

### Worker Protocol
- Claim individual child beans via `beans update <bean-id> --status in-progress --body-append "Claimed by <branch> (YYYY-MM-DD)"`.
- Never mark a bean `completed` while an uninstantiated conjecture `class` or explicit `stays open` item remains (AGENTS.md Rule 13a).
- Enforce single-thread CPU caps (`LEAN_NUM_THREADS=1`, `nice -n 15`), zero float64 (`mpmath` >= 50-80 dps), and zero fitting.
