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

--- SHARPENED 2026-07-26 (T4 landed: sl2_finrank_engel_h_eq_one, rank 𝔰𝔩₂ = 1) ---
The reduction is now pinned to a SINGLE residual fact. Clean spine (all Mathlib, confirmed):
  rank 𝔤 = finrank(engel_𝔤 x*)   [isRegular_iff_finrank_engel_eq_rank, x* a 𝔤-regular elt, Infinite K]
  rank 𝔤 ≤ finrank(engel_𝔤 y)    [rank_le_finrank_engel, ANY y ∈ 𝔤]
  engel_𝔤 y = maxGenEigenspace(ad_𝔤 y, 0), and ad_𝔤 y = (ad_𝔰𝔩₂ y)|_𝔤 (bracket agrees) ⇒
    engel_𝔤 y ↪ engel_𝔰𝔩₂ y  (generalized-0-eigvec in 𝔤 is one in 𝔰𝔩₂).
Two viable routes to rank 𝔤 ≤ 1:
  (R1) ∃ y ∈ 𝔤 with finrank(engel_𝔤 y) ≤ 1. Verified by hand for the three subalgebra classes
       (span{e}: y=e, ad=0, engel=span{e}; Borel span{h,e}: y=h, engel=span{h}; 𝔰𝔩₂: y=h) — but the
       witness y is 𝔤-dependent, so a UNIFORM proof still needs 𝔰𝔩₂ structure.
  (R2) engel_𝔤 x* (x* 𝔤-regular) is a nilpotent (Cartan) subalgebra of 𝔤 ⊆ 𝔰𝔩₂; residual =
       "a nilpotent subalgebra of 𝔰𝔩₂ has finrank ≤ 1" (2-dim subalgebras = Borel, non-nilpotent;
       3-dim = 𝔰𝔩₂, semisimple). Needs: (a) LieRing.IsNilpotent(engel of regular) [Cartan], (b) the
       sub-of-sub embedding as a LieSubalgebra of 𝔰𝔩₂, (c) classify: nilpotent ⊆ 𝔰𝔩₂ ⇒ abelian
       ⇒ dim ≤ 1 (max abelian in 𝔰𝔩₂ is a Cartan, dim 1). (c) is the genuine new 𝔰𝔩₂-structure lemma.
GENERAL reusable one-liner already available to package the reduction:
  rank L ≤ n  ⇐  ∃ y, finrank(engel y) ≤ n   (just `rank_le_finrank_engel K y |>.trans`).
Next-session start point: prove (c) — "abelian (or nilpotent) subalgebra of sl 2 K has finrank ≤ 1"
— as the keystone; everything else is plumbing on the confirmed spine.
