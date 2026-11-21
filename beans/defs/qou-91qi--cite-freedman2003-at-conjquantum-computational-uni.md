---
# qou-91qi
title: Cite [freedman2003] at conj:quantum-computational-universality
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T23:34:25Z
updated_at: 2026-11-21T12:26:55Z
parent: qou-1qhv
---

The Lean sub-claim states 'at level k >= 3' where the cited source states 'k >= 3, k != 4'. Restore the exception and add the primary reference; a survey citation for a density theorem should name the paper that proves it.

**From the source**
- p. 5 (main text, near the level-k discussion) — The braid matrices for SU(2) Chern-Simons at level k have been shown to be universal for quantum computation for k >= 3, k != 4 (attributed to refs [8],[9] of the survey).
  Use here: Restore the k != 4 exception to the QuantumUniversalityHolds docstring, and cite the primary source (Freedman-Larsen-Wang CMP 227 (2002)) alongside the survey.

Source: `freedman2003` (bib key; PDF not committed to this repo)
Relevance: **supporting** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

## 2026-11-21 — cite-intake drain (wave 1)

Verdict: **done** (branch `claude/cite-intake-drain-2026-11-21`, PR #8818, issue #8814). k>=3, k!=4 restored in .md and .lean; survey PDF not held (locator rests on bean); primary FLW paper not registered (arXiv blocked).

Superseded-premise check: the edited text was read against `docs/coordination/owner-rulings.md` (photon 1+φ₀σ₀+φ₁σ₁+φ₀₁σ₀σ₁⁻¹; electron σ₀σ₁σ₀ with Hopf closure; up quark an unknot strand; two-term Lagrangian trace; T(2,n_s) withdrawn; no virtual photons). None of these forms is asserted or relied on in the cited sentences.

Status stays in-progress until PR #8818 merges.
