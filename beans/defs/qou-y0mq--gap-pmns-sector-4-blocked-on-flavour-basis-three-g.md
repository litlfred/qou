---
# qou-y0mq
title: 'GAP: PMNS sector (4) — blocked on flavour basis + three-generation structure'
status: todo
type: task
priority: normal
tags:
    - sm-26
    - reorg-2026-10-04
    - 8f-ew
created_at: 2026-07-31T20:15:08Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-20sx
blocked_by:
    - qou-y7vg
    - qou-x4qm
    - qou-qydm
---

## 🔥 Roast (2026-09-03, qou-bsu0)

(i) Needs everything CKM needs (a flavour basis, 4-A; a generation count, `qou-x4qm`) PLUS a neutrino mass basis (`qou-qydm`) and a carrier that can carry lepton number — the unknot cannot (`LeptonNumberCarrierChirality.lean`, `qou-kl39`).
(ii) Excluded: nothing PMNS-specific; the neutrino volume–density route is scope-b excluded (~10¹⁰, `neutrino-mass-volume-exclusion.witness.json`), so there is not even a mass eigenbasis to mix.
(iii) Trap: tri-bimaximal-style angles from S₃/A₄ subgroups of the corpus's S₅ — the Weyl group W(A₂) = S₃ is available and is exactly what `qou-y7vg` warns "yields the hexagon symmetry, not the fundamental"; a Majorana/Dirac choice asserted to fit δ_CP.
(iv) Next: not near-term; the only tractable upstream step is the carrier repair (chiral carrier, or L on framed knots = `def:strand-twist-datum`).
(v) Forecast: the last sector to move; nothing before m_ν has a mechanism.
Tower status [reading: qou-ggdk]: no attack at any order; a full-tower formulation would need the neutrino to be a non-trivial object of the tower at all — on the unknot every order vanishes. None exists.

## 2026-10-10 — reparented under qou-20sx

Owner decision 7b (ofri, 2026-10-10): the electroweak (`8f-ew`) beans are grouped under `qou-20sx`, the electroweak front's node, instead of directly under the epic `qou-8lxd`. Only the parent changed. Status, scope and body are untouched.

## Round 66 Update (PR #8239)
- Formalized in `WeakIsospinGradingColourFibreRoutesLightQuarkExtractionTauLogConvexityAndPmnsCarrier.lean` and verified via 80-dps `mpmath` witness in PR #8239.

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8239, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
