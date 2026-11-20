---
# qou-qs0e
title: 'Quark state: definition on the q-tower, factor relations, SM / eightfold-way correspondence'
status: todo
type: epic
priority: normal
tags:
    - quark-state
created_at: 2026-11-15T08:00:00Z
updated_at: 2026-11-15T08:00:00Z
---

Owner 2026-11-15 ("try all ... bean up"): the missing input behind qou-wqto / qou-ales / qou-99qc / qou-pu2x is a definition of what a quark STATE is.

Corpus facts this starts from (corpus-grep 2026-11-15, origin/main 0b88920e35):
- States are GS normal forms (owner ruling 2026-08-10, `WritheMarkovInvariance.lean:58-63`); the observable is the trace on the lowest part of the tower.
- Photon state = colour content (phi0, phi1, phi01) of gamma = 1 + phi0 s0 + phi1 s1 + phi01 s0 s1 (`rem:knot-basis-color-content`); phi0/phi1 = polarizations at jet degree 1, phi01 at degree 2; the degree-0 part is annihilated at a jet horizon.
- Quark flavour is invisible at order t^0 (t = q-1) and appears at t^1 (`computations/probes/quark_template/results.md:9-13`).
- gamma gamma -> NF(L+ e-) = s1 + h L+ + h L- + h^2 e-, s1 "the up quark" (qou-gpb5).
- Polarization [v1:v2] in P^1(C) = S^2 (`breit-wheeler-vertex.md`); stream 3 proved the chirality unit u must be a point of S^2 that no structure fixes (#7818, #7820).
- Convention D (y = 0 on >= 3-row shapes) is quantum Schur-Weyl at N = 2 (TL / U_q(sl2)); y(1^3) = 0.035 at level 3 (`level_three_colour_channel_probe.py`).

Hypothesis (agent judgement, not a finding): quark state := degree >= 1 part of NF(gamma(phi) gamma(psi)) in H_3(q), projected to the (2,1) channel; observable depth = tower depth (order 0 = gamma gamma core, so quark labels are invisible -> confinement; t^1 = flavour; higher = masses / mixing).

Children: qou-qs1d (definition, Lean), qou-qs2u (u = polarization), qou-qs3l (library citations), qou-qs4c (factor relations + colour channel), qou-qs5m (SM / eightfold-way corpus map).

## 2026-11-20 — W2 cross-workstream briefing (owner: "make sure they know")
Full briefing: PR #8526 comment 7047864732 and docs/coordination/2026-11-20-w2-qbeta-ud-briefing.md. Record: docs/audits/2026-11-20-qbeta-epsilon-is-ruled-not-derived.md sections 1-11.
Key points: Q_beta = (h[2]/2)*y3*E0 and sees only the isospin-3/2 block. The ruled epsilon (z_D, -43%) = label-A round trip = whole-space quantum trace. Label B (J4, strand-4 gamma-gamma) gives +0.33% and is NOT adopted (it labels isospin multiplicity, not n<->p). Label C gives 1/3, 0 and 0.202, none close. The owner made no label ruling ("3 2"). u/d are separate lines of the (3,1) rep of H4, not orientation-only (def:up/down-quark are stale). Convention-D volumes lie past the Phi_q pole. The six-term -2.43e15 was a truncated divergent series (fixed). The +0.17% / ~1 ppm Q_beta values and the April BW run are superseded or circular.
