---
# qou-zwax
title: 'q-zero-stokes-region-identification.lean: encode 3 :True class fields'
status: in-progress
type: task
priority: high
tags:
    - reorg-2026-10-04
created_at: 2026-07-11T18:41:38Z
updated_at: 2026-11-16T19:22:00Z
parent: qou-6qbv
---

UniversalBase.q_inv_property:57 -> q*q_inv=1 (add [Mul R][One R]); MostowPrasadDistinguished.rigid:88 and QZeroStokesIdentification.identification_witness:127 are genuinely open (Mostow-Prasad/the q0 gap) — encode what is statable, leave open as content-bearing carrier or honest sorry, NOT True.

## Progress Update (2026-11-16 — Round 48, PR #8165)

- Verified the 3 encoded class fields in `folio/quantum-observable-universe/nuclear-interactions/q-zero-stokes-region-identification.lean` (`UniversalBase.q_inv_property : q * q_inv = 1`, `MostowPrasadDistinguished.rigid : ∀ r : Rep, IsDiscreteFaithful r → Conjugate r rho_DF`, `QZeroStokesIdentification.identification_witness : q_0 = traceInvariant MPD.rho_DF`) and added proved consumer theorems `q_isUnit`, `q_inv_isUnit`, `q_0_eq_traceInvariant_of_isDiscreteFaithful`, and `trace_field_degree_ne_zero` (`0` `sorry`).
- Opened PR `litlfred/qou#8165` (`cf010d07bb34f2e3118733212559b61ede4b8cc4`) with `ready-to-merge` + `release` labels.
