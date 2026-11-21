---
# qou-ir19
title: Cite [kirillov1995] at conj:borromean-bloch-group-element
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T23:36:54Z
updated_at: 2026-11-21T12:26:55Z
parent: qou-1qhv
---

Sec. 2.3 relates dilogarithm identities to K_3 torsion, which is the subject of the Borromean Bloch-group conjecture and of the Borel-rank proposition; neither cites this already-registered reference.

**From the source**
- Sec. 2.3, 'Dilogarithm identities and algebraic K-theory' — Dilogarithm identities of the form sum L(x_i) = c pi^2/6 with algebraic x_i and rational c are related to torsion in K_3 of the relevant ring, and the paper argues that essentially all such identities are consequences of the five-term relation alone.
  Use here: A structural prune in the sense of the formalize-first discipline: a candidate closed form built from Rogers-dilogarithm values at algebraic points must live in this classified family, which narrows the search space before any wide numerical scan is run.

Source: `library/arxiv-hep-th-9408113v2/9408113v2.pdf` (`kirillov1995`)
Relevance: **core** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

## 2026-11-21 — cite-intake drain (wave 1)

Verdict: **done** (commit `e105e6333`, branch `claude/cite-intake-drain-2026-11-21`, PR #8818, issue #8814). §1.1.4 + §2.3.1 at the five-term relation; also fixed nonexistent 'Prop 2.1/2.3' and '§2.1' locators in Li2qUniqueness.lean.

Superseded-premise check: the edited text was read against `docs/coordination/owner-rulings.md` (photon 1+φ₀σ₀+φ₁σ₁+φ₀₁σ₀σ₁⁻¹; electron σ₀σ₁σ₀ with Hopf closure; up quark an unknot strand; two-term Lagrangian trace; T(2,n_s) withdrawn; no virtual photons). None of these forms is asserted or relied on in the cited sentences.

Status stays in-progress until PR #8818 merges.
