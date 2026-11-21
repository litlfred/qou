---
# qou-krtl
title: Cite [garoufalidis-le-2011] at qou:QOU.Knot.FigureEightVolume.borromeanKashaev
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T23:35:26Z
updated_at: 2026-11-21T12:26:55Z
parent: qou-1qhv
---

BorromeanVolume.lean cites the paper only by DOI in the header. Naming 'Appendix A, Theorem A.1' at the point where the docstring asserts the identification would make the epistemic-status paragraph checkable without opening the PDF.

**From the source**
- Thm A.1 — For the Borromean rings B, lim (1/n) log |J_{B,n}(e^{2 pi i/n})| = vol(S^3 - B)/(2 pi); proved via Habiro's cyclotomic formula for the Borromean colored Jones.
  Use here: The literature input that licenses identifying QOU's explicitly-DEFINED borromeanKashaev sum with the Kashaev invariant / colored Jones at the root of unity, i.e. the epistemic hinge of BorromeanVolume.lean.

Source: `library/arxiv-math-0508100v6/0508100v6.pdf` (`garoufalidis-le-2011`)
Relevance: **core** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

## 2026-11-21 — cite-intake drain (wave 1)

Verdict: **done** (commit `8d7ee40cf`, branch `claude/cite-intake-drain-2026-11-21`, PR #8818, issue #8814). GL2011 Thm A.1 sec-039

Superseded-premise check: the edited text was read against `docs/coordination/owner-rulings.md` (photon 1+φ₀σ₀+φ₁σ₁+φ₀₁σ₀σ₁⁻¹; electron σ₀σ₁σ₀ with Hopf closure; up quark an unknot strand; two-term Lagrangian trace; T(2,n_s) withdrawn; no virtual photons). None of these forms is asserted or relied on in the cited sentences.

Status stays in-progress until PR #8818 merges.
