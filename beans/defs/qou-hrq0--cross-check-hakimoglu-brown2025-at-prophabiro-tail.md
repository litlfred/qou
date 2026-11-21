---
# qou-hrq0
title: Cross-check [hakimoglu-brown2025] at prop:habiro-tail-archimedean-action
status: completed
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T23:34:50Z
updated_at: 2026-11-21T12:54:01Z
parent: qou-1qhv
---

The registered entry credits this source with Li2(phi^-2) = pi^2/15 - ln^2 phi, which its full text does not contain (its golden-ratio result is pi^2/100 = Re Li2(r_0)). Since A_0 = pi^2/5 for 4_1 is derived from that evaluation, re-source the evaluation and re-check the derivation against the corrected source before relying on it further.

**From the source**
- Thm 3 / Example 4, §6 — pi^2/100 = Re Li2(r_0) with r_0 a root of r^4 - 3r^3 + 4r^2 - 2r + 1 = 0, expressible via the golden ratio, proving a previously conjectured identity.
  Use here: This is the document's actual golden-ratio content and is NOT the Li2(phi^-2) = pi^2/15 - ln^2 phi evaluation the corpus attributes to it.

Source: `library/arxiv-2506.10206v2/2506.10206v2.pdf` (`hakimoglu-brown2025`)
Relevance: **supporting** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

## 2026-11-21 — cite-intake drain (wave 1)

Verdict: **done** (commit `2a5686b5a`, branch `claude/cite-intake-drain-2026-11-21`, PR #8818, issue #8814). HB does not contain the π²/15 value (its golden result is π²/100, §6); value re-sourced to zagier-dilogarithm §1; reference note corrected.

Superseded-premise check: the edited text was read against `docs/coordination/owner-rulings.md` (photon 1+φ₀σ₀+φ₁σ₁+φ₀₁σ₀σ₁⁻¹; electron σ₀σ₁σ₀ with Hopf closure; up quark an unknot strand; two-term Lagrangian trace; T(2,n_s) withdrawn; no virtual photons). None of these forms is asserted or relied on in the cited sentences.

Status stays in-progress until PR #8818 merges.

## 2026-11-21 — PR #8818 merged

The cite-intake work above landed on main. Status set to completed.
