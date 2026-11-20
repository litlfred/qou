---
# qou-pgzo
title: 'GAP: m_H — T(2,8) identification conjectural; RT level selection + invariant→mass map open; probes within 2×'
status: todo
pr: 8196
type: task
priority: normal
tags:
    - sm-26
    - reorg-2026-10-04
    - 8f-mass
created_at: 2026-09-03T08:31:51Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-8lxd
---

Per-term bean for the Higgs mass (session qou-ggdk, bean qou-bsu0). Tier: conjectural (`conj:electroweak-higgs-torus-link-triplet`; provable base proved, identification not). Owner ruling 2026-06-30: 4₁ is the mass mechanism, T(2,8) the boson (qou-rdbr). Not gated on 4-A/B/C; the gate is a level-selection principle. Sibling of qou-z3x8 (v).

## 🔥 Roast (2026-09-03)

(i) Needs (a) the identification H = T(2,8), (b) a selected level for the Reshetikhin–Turaev evaluation of a Vol = 0 carrier, (c) an invariant→mass map.
(ii) Negatives: the RT colored-Jones probe, N = 2..12 at q₀ and roots of unity, lands within ~2× of m_H/m_e = 244811 (`pentagon-rt-torus-knot-higgs-probe`, 389 raw float64 fields, `qou-5mao`); G-action q-dimensions alone do not pin EW ratios — the self-coupling λ is needed (`higgs-slot-g-action-test`, deprecated); `m_H = √(2λ)v` is a ratio identity only (`CategoricalHiggsIdempotent.lean`).
(iii) Trap: `higgs-t28.md` writes m_H = Vol(Seifert(T(2,8)))/ℏ_q² · c_𝓑 with c_𝓑 the purged λ_scale — a fit by another name; the h⁶ probes solve C₆ from the W, Z anchors then hunt substrate-natural matches (best +0.29 %) — post-hoc.
(iv) Next: not near-term; a derived level principle would be a result even at factor-2 accuracy.
(v) Forecast: factor 2 stays factor 2 without a level principle.
Tower status [reading: qou-ggdk]: MIXED — RT at a root of unity is a fibre-level object, but with the level unselected and the mass map absent every actual number is an order-zero volume or ratio reading.

## Progress (2026-11-16, PR #8196)
- [x] Formalized `twoStrandComponents`, `twoStrandEulerChar`, `twoStrandGenus`, `t27_knot_vs_t28_link_invariants`, `scalarSquaredMass`, and `scalarSquaredMass_strictMono_in_quartic` in `folio/quantum-observable-universe/lean/QOU/Eightfold/LeptonReadoutHiggsScaleMesonSyllableAndIcosahedralOrbit.lean` + 50-dps mpmath witness (`qou_pgzo_t27_t28_surface_and_quartic_scale`) in PR #8196 (`38b68fa660bb34e2ffb7a2e1a09e5c4f5308e2cf`).

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8196, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
