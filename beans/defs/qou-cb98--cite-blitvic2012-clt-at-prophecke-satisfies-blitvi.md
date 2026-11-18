---
# qou-cb98
title: Cite [blitvic2012-clt] at prop:hecke-satisfies-blitvic-hypothesis
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T23:35:12Z
updated_at: 2026-10-04T15:17:25Z
parent: qou-mub3
---

hecke-satisfies-blitvic-hypothesis-proof.md:82 cites '[blitvic2012], eq. (1.2)', a locator that does not exist in the uploaded Blitvic document and cannot be checked against the un-uploaded one. Cite blitvic2012-clt Thm 2 eq. (12) at t=1, which the corpus can verify from its own uploads.

**From the source**
- Thm 2, eq. (12) — For a sequence satisfying the generalised commutation relation with E(mu)=q t^{-1}, E(mu^2)=1, the limiting mixed *-moments of the normalised partial sums are sum over pair partitions V of P_2(2n) of q^{cross(V)} t^{nest(V)} times the product term; odd moments vanish.
  Use here: At t = 1 this is exactly the moment formula the Hecke-Blitvic proof block needs, with a locator that actually exists. It is also the literature statement the conditional q-CLT class in QCltNonCommutative.lean should cite, since that class is about a CLT and the currently-cited key is not the CLT paper.

Source: `blitvic2012-clt` (bib key; PDF not committed to this repo)
Relevance: **core** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.
