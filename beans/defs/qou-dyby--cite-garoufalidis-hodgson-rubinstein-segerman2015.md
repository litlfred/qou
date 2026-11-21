---
# qou-dyby
title: Cite [garoufalidis-hodgson-rubinstein-segerman2015] at computations/probes/borromean_3d_index.py
status: scrapped
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T23:35:37Z
updated_at: 2026-11-21T12:26:55Z
parent: qou-1qhv
---

The 3d-index probes compute an index from a specific triangulation and report it as a manifold invariant without citing the triangulation-independence theorem that licenses that. This registered-but-uncited entry is exactly the missing source.

**From the source**
- Main theorem (a)+(b) — An ideal triangulation T admits an index structure iff T is 1-efficient; a hyperbolic M has a canonical set of 1-efficient triangulations related by 2-3 and 0-2 moves preserving the 3d index, so the index is a topological invariant of M.
  Use here: Would license the corpus's Borromean 3d-index probes to speak of 'the 3d index of the manifold' rather than 'of this triangulation' - the step those probes currently leave implicit.

Source: `library/topologicalinvariance3dindex/topological.invariance.3Dindex.pdf` (`garoufalidis-hodgson-rubinstein-segerman2015`)
Relevance: **tangential** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

## 2026-11-21 — cite-intake drain (wave 1)

Verdict: **premise-false** (no commit). borromean_3d_index.py already cites GHRS (arXiv:1303.5278, held path) with Thm 1.1/1.2/1.8; adding the key alone would drift the scriptHash of two witnesses for a comment.

Superseded-premise check: the edited text was read against `docs/coordination/owner-rulings.md` (photon 1+φ₀σ₀+φ₁σ₁+φ₀₁σ₀σ₁⁻¹; electron σ₀σ₁σ₀ with Hopf closure; up quark an unknot strand; two-term Lagrangian trace; T(2,n_s) withdrawn; no virtual photons). None of these forms is asserted or relied on in the cited sentences.

Status set to scrapped.
