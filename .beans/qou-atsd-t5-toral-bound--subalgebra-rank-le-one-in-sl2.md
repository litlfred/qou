---
# qou-atsd-t5-toral-bound
title: 'T5 (HARD reusable infra, tiered): 𝔤 ⊆ 𝔰𝔩₂ ⟹ rank 𝔤 ≤ 1 — the toral/Cartan dimension bound (the real Mathlib gap for atomicity)'
status: todo
type: task
priority: normal
parent: qou-atsd
created_at: 2026-07-26T12:30:00Z
updated_at: 2026-07-26T12:30:00Z
---

THE load-bearing atomicity gap. Group-rank(G) ≤ 1 for G ↪ SL₂ reduces to rank 𝔤 ≤ 1 for
𝔤 = Lie(G) ⊆ 𝔰𝔩₂. NOT free monotonicity (rank is not monotone under arbitrary inclusion).

CORRECTNESS: true because a Cartan (toral) subalgebra of 𝔰𝔩₂ has dim ≤ 1 (max torus of 𝔰𝔩₂
is 1-dim). rank 𝔤 = dim(Cartan of 𝔤). Cartan of 𝔤 is nilpotent+self-normalizing; inside 𝔰𝔩₂
its dimension is ≤ 1.

MATHLIB SPINE (confirmed present):
- rank K 𝔤 = finrank K (engel_𝔤 x) at a regular x (isRegular_iff_finrank_engel_eq_rank).
- rank_le_finrank_engel: rank ≤ finrank(engel y) for any y.
- exists_isRegular [Infinite K]; exists_isCartanSubalgebra_engel.
- IsCartanSubalgebra class (nilpotent + self_normalizing).

HARD CORE (the genuine new infra — TIER this):
- No Mathlib IsToral, no LieSubalgebra rank-monotonicity, no "toral subalgebra of 𝔰𝔩₂ has dim ≤ 1".
- Build: (a) a Cartan H of 𝔤 embeds as a nilpotent self-normalizing subalgebra of 𝔰𝔩₂;
  (b) such an H in 𝔰𝔩₂ has finrank ≤ 1 (𝔰𝔩₂-specific: classify — the toral/Cartan is 1-dim).
- Likely needs: engel-in-𝔰𝔩₂ dimension analysis, or a direct "abelian ad-semisimple ⊆ 𝔰𝔩₂ ⇒ dim ≤ 1".

DISCIPLINE: mark residual as cited conditional (-- Ref: [manuscript]/[Bourbaki-Lie]) — do NOT
launder a fabricated instance. rank-one stays a premise until the toral bound is genuinely proved.
This is epic 08a2 (hard Mathlib-gap infra, tiered) material — multi-session.
