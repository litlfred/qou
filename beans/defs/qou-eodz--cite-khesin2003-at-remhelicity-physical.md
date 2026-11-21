---
# qou-eodz
title: Cite [khesin2003] at rem:helicity-physical
status: completed
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T23:35:47Z
updated_at: 2026-11-21T12:54:01Z
parent: qou-1qhv
---

A fully-read, load-bearing helicity source with no citation site in content/; rem:helicity-physical is the block whose subject it is.

**From the source**
- Rmk 4.8; Rmk 3.4-3.5 — Linking forms are symmetric or antisymmetric according to the parity of the product of codimensions (1-forms in 3D force antisymmetry), signed invariants cancel between oppositely-linked pairs, and the asymptotic crossing number is the symmetric substitute that is nonzero when the linking number vanishes.
  Use here: Already consumed in docs/audits/2026-08-01-em-linking-reads-round1.md as the structural explanation of obstruction O1; the fluid-dynamics helicity block should carry the citation so the antisymmetry constraint is visible in the narrative, not only in an audit.

Source: `library/helicity03mmj/helicity03mmj.pdf` (`khesin2003`)
Relevance: **supporting** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

## 2026-11-21 — cite-intake drain (wave 1)

Verdict: **done** (commit `8391ca402`, branch `claude/cite-intake-drain-2026-11-21`, PR #8818, issue #8814). Thm 2.2 + Thm 2.5 (held copy) placed at the conservation sentence; bean's Rmk 4.8 locators not relevant to this block.

Superseded-premise check: the edited text was read against `docs/coordination/owner-rulings.md` (photon 1+φ₀σ₀+φ₁σ₁+φ₀₁σ₀σ₁⁻¹; electron σ₀σ₁σ₀ with Hopf closure; up quark an unknot strand; two-term Lagrangian trace; T(2,n_s) withdrawn; no virtual photons). None of these forms is asserted or relied on in the cited sentences.

Status stays in-progress until PR #8818 merges.

## 2026-11-21 — PR #8818 merged

The cite-intake work above landed on main. Status set to completed.
