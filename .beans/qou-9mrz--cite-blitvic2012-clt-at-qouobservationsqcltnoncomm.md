---
# qou-9mrz
title: Cite [blitvic2012-clt] at QOU.Observations.QCltNonCommutative
status: todo
type: task
created_at: 2026-08-08T23:35:13Z
updated_at: 2026-08-08T23:35:13Z
---

QOU/Observations/QCltNonCommutative.lean:25-26 pairs the (q,t)-Gaussian title/journal with the arXiv id of the CLT paper — the two keys are conflated in one reference line, in the file whose subject is precisely a non-commutative CLT. The CLT key blitvic2012-clt is the correct citation there.

**From the source**
- Thm 2, eq. (12) — For a sequence satisfying the generalised commutation relation with E(mu)=q t^{-1}, E(mu^2)=1, the limiting mixed *-moments of the normalised partial sums are sum over pair partitions V of P_2(2n) of q^{cross(V)} t^{nest(V)} times the product term; odd moments vanish.
  Use here: At t = 1 this is exactly the moment formula the Hecke-Blitvic proof block needs, with a locator that actually exists. It is also the literature statement the conditional q-CLT class in QCltNonCommutative.lean should cite, since that class is about a CLT and the currently-cited key is not the CLT paper.

Source: `library/blitvic2012.pdf` (`blitvic2012-clt`)
Relevance: **core** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.
