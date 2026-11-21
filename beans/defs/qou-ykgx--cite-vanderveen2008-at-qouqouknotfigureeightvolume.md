---
# qou-ykgx
title: Cite [vanderveen2008] at qou:QOU.Knot.FigureEightVolume.borromeanKashaev
status: in-progress
pr: 8438
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T23:35:27Z
updated_at: 2026-11-21T12:26:55Z
parent: qou-1qhv
---

BorromeanVolume.lean sources the Borromean volume conjecture solely from garoufalidis-le-2011. the Whitehead-chain family proved in [vanderveen2008] contains the Borromean rings, so adding [vanderveen2008] there gives an independent second source for the same identification.

**From the source**
- Abstract / main theorem — The volume conjecture holds for the infinite family of Whitehead chains, which contains both the Whitehead link and the Borromean rings.
  Use here: Backs the queued sorry in whitehead_volume_conjecture, and supplies a SECOND, independent literature proof of the Borromean case now carried only by garoufalidis-le-2011 App. A.

Source: `library/arxiv-math-0611181v2/0611181v2.pdf` (`vanderveen2008`)
Relevance: **core** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8438, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.

## 2026-11-21 — cite-intake drain (wave 1)

Verdict: **done** (commit `8d7ee40cf`, branch `claude/cite-intake-drain-2026-11-21`, PR #8818, issue #8814). vanderveen main thm, B=W_{0,1,1,1}

Superseded-premise check: the edited text was read against `docs/coordination/owner-rulings.md` (photon 1+φ₀σ₀+φ₁σ₁+φ₀₁σ₀σ₁⁻¹; electron σ₀σ₁σ₀ with Hopf closure; up quark an unknot strand; two-term Lagrangian trace; T(2,n_s) withdrawn; no virtual photons). None of these forms is asserted or relied on in the cited sentences.

Status stays in-progress until PR #8818 merges.
