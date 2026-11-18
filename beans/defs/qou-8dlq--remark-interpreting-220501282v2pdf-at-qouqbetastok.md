---
# qou-8dlq
title: Remark interpreting 2205.01282v2.pdf at QOU.QBeta.StokesDTBPSBridge
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T23:35:19Z
updated_at: 2026-10-04T15:13:46Z
parent: qou-aqfj
---

Record what would have to be checked before this changes any epistemic tier: whether the knot complements / 3-manifolds the folio's A_omega argument uses fall inside this document's plumbed, negative-definite-linking-matrix class. If they do not, the GPPV identification stays conjectural for the folio's purposes and the bridge's class fields must remain as they are.

**From the source**
- main theorem (abstract statement) — For a wide class of plumbed 3-manifolds with negative-definite linking matrix, the WRT invariant is the radial limit of the corresponding homological block; the proof establishes vanishing of the weighted Gauss sums appearing in negative-degree coefficients of the blocks' asymptotic expansions.
  Use here: StokesDTBPSBridge.lean currently carries the GPPV identification as an ASSUMED class field. This document upgrades part of that assumption to a proved statement on a restricted class, so the bridge's epistemic tier could be sharpened — but only if 4_1's relevant 3-manifold is in the plumbed negative-definite class, which I have NOT checked. Until that is checked this is a citation to record, not a hypothesis to discharge.

Source: `library/arxiv-2205.01282v2/2205.01282v2.pdf` — no `references.ts` entry yet
Relevance: **core** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

STALE LINE 2026-08-21 (bean qou-kqbk, PR #5384). The body above says 'no `references.ts` entry yet'. There is one:

  library/arxiv-2205.01282v2/  ->  [murakami-y2022]
  Witten-Reshetikhin-Turaev invariants and homological blocks for plumbed homology spheres

The library registration backlog is drained to zero. NOT closing this bean — the entry existing is necessary for the task in the title and not sufficient. Use [murakami-y2022] as the citation key when you do it.

2026-09-06: RECORDED in stokes-dt-bps-bridge.md, citing [murakami-y2022]. The class check: Murakami-Y's theorem is for CLOSED plumbed 3-manifolds with negative-definite linking matrix; S³∖K for hyperbolic K is cusped and not plumbed, so 4₁ and 5₂ are OUTSIDE the class and dt_eq_bps stays an assumed class field. Epistemic tier unchanged. Bean stays OPEN per owner rule (AGENTS.md 13a): its subject is the bridge's tier, which is an open conjecture.



## 2026-09-07 — the check the body asked for, measured against the corpus and a held source

The conjecture block `conj:stokes-dt-bps-bridge` already carries the interpreting paragraph (mass-theory/stokes-dt-bps-bridge.md, lines 30–35): Murakami 2022 proves WRT = radial limit of Ẑ for plumbed 3-manifolds with negative-definite linking matrix; that class is closed manifolds, S³∖K for hyperbolic K is cusped and not plumbed, so the theorem does not reach the objects the conjecture quantifies over and `dt_eq_bps` stays an assumption.

Sharpening, with the source held: Li–Wang (library/arxiv-math-0604057v2 §5, `sec-012-5-an-example-the-figure-eight-knot.md` lines 197–263) record the TEN exceptional surgery slopes of 4₁ (0, ±1, ±2, ±3, ±4, ∞) and that M(0) is toroidal with non-abelian infinite π₁ — so some closed fillings of 4₁ are graph/Seifert manifolds that MAY lie in the plumbed negative-definite class (that 4₁(±1) is the Brieskorn sphere Σ(2,3,7), a Seifert manifold, is RECALLED, not held). This does not change the tier: the A_ω argument uses the state integral of the cusped complement (GGM Conj 3(d) for 4₁ itself), not a WRT invariant of a closed filling.

Verdict: citation recorded (already in the block), no hypothesis discharged, bridge class fields unchanged. Completed as the remark/citation task it is; the conjecture it interprets stays open in its own block (AGENTS.md 13a does not apply: the bean's subject is the citation, not the conjecture).

## 2026-09-08 — reopened: `status` disagreed with this bean's OWN body (§13a sweep, `qou-7sin`)

This bean was `completed` while the text above says, in its author's own words,
that the bean itself is still open. Nothing about its mathematics was judged
here and no finding was revisited — only the `status` field was made to agree
with the body.

Found by the `qou-7sin` sweep of the tracker against AGENTS.md **§13a** (owner,
2026-09-06: *"Don't close beans with open conjectures!!!"*), which landed after
most of these were closed. 18 of 2627 completed beans carry this
self-contradiction. It is decidable without judgement — the discriminator is
the bean asserting *its own* openness, not merely mentioning something open.

Re-close it when the work its body names is actually done.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-08 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.
