---
# qou-9mrz
title: Cite [blitvic2012-clt] at QOU.Observations.QCltNonCommutative
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T23:35:13Z
updated_at: 2026-11-21T12:26:55Z
parent: qou-1qhv
---

QOU/Observations/QCltNonCommutative.lean:25-26 pairs the (q,t)-Gaussian title/journal with the arXiv id of the CLT paper — the two keys are conflated in one reference line, in the file whose subject is precisely a non-commutative CLT. The CLT key blitvic2012-clt is the correct citation there.

**From the source**
- Thm 2, eq. (12) — For a sequence satisfying the generalised commutation relation with E(mu)=q t^{-1}, E(mu^2)=1, the limiting mixed *-moments of the normalised partial sums are sum over pair partitions V of P_2(2n) of q^{cross(V)} t^{nest(V)} times the product term; odd moments vanish.
  Use here: At t = 1 this is exactly the moment formula the Hecke-Blitvic proof block needs, with a locator that actually exists. It is also the literature statement the conditional q-CLT class in QCltNonCommutative.lean should cite, since that class is about a CLT and the currently-cited key is not the CLT paper.

Source: `blitvic2012-clt` (bib key; PDF not committed to this repo)
Relevance: **core** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

## 2026-11-21 — cite-intake drain (wave 1)

Verdict: **done** (branch `claude/cite-intake-drain-2026-11-21`, PR #8818, issue #8814). CLT key and (q,t)-Gaussian key separated; neither PDF held.

Superseded-premise check: the edited text was read against `docs/coordination/owner-rulings.md` (photon 1+φ₀σ₀+φ₁σ₁+φ₀₁σ₀σ₁⁻¹; electron σ₀σ₁σ₀ with Hopf closure; up quark an unknot strand; two-term Lagrangian trace; T(2,n_s) withdrawn; no virtual photons). None of these forms is asserted or relied on in the cited sentences.

Status stays in-progress until PR #8818 merges.
