---
# qou-atsd-t4-rank-eq-one
title: 'T4 (reusable infra): LieAlgebra.rank K (sl 2 K) = 1 — upgrade the ≤1 upper bound to equality via finrank(engel h)=1'
status: todo
type: task
priority: normal
parent: qou-atsd
created_at: 2026-07-26T12:30:00Z
updated_at: 2026-07-26T12:30:00Z
---

Reusable Mathlib-grade infra: the RANK of 𝔰𝔩₂ as a Lean fact (general field, 2≠0).

HAVE (T3-lie, #4285): rank K (sl 2 K) ≤ 1 (via natTrailingDegree(charpoly ad h)=1).

UPGRADE to = 1:
- ad h = diag(0,2,−2) on basis (h,e,f) ⇒ generalized 0-eigenspace (engel K h) = span{h}, finrank 1.
- Mathlib bridge: rank_le_finrank_engel (rank ≤ finrank(engel y) any y) gives ≤1 again;
  isRegular_iff_finrank_engel_eq_rank + showing h regular gives rank = finrank(engel h) = 1.
- ≥1 half (the fiddly bit): rank ≠ 0. Route: polyCharpoly.coeff 0 ≡ 0 because ad x is always
  singular (x ∈ ker ad x, self-bracket zero) ⇒ det(ad x) ≡ 0 as a polynomial ⇒ trailing degree ≥ 1.
  Confirm the Mathlib lemma name for "constant coeff of polyCharpoly = det / = 0"; if absent, prove
  via engel: finrank(engel x) ≥ 1 for all x (self_mem_engel) — but that lower-bounds finrank(engel),
  need the rank = min finrank(engel) direction. Scope honestly if ≥1 needs a custom argument.

Deliverable: `sl2_rank_eq_one` in AtomicityLieRank.lean, sorry-free (or ≤1 kept + ≥1 cited-conditional).
