---
# qou-atsd-t5-toral-bound
title: 'T5 (HARD reusable infra, tiered): 𝔤 ⊆ 𝔰𝔩₂ ⟹ rank 𝔤 ≤ 1 — the toral/Cartan dimension bound (the real Mathlib gap for atomicity)'
status: completed
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

--- WORKED KEYSTONE PROOF (2026-07-26, transcription-ready) ---
KEYSTONE: sl2_ker_ad_le_span {K} [Field K] (h2 : 2≠0) (X : sl (Fin 2) K) (hX : X ≠ 0) :
  LinearMap.ker (ad K (sl 2 K) X) ≤ Submodule.span K {X}.
API pinned: sl_bracket : ⁅A,B⁆.val = A.val*B.val - B.val*A.val (rfl); sl membership = trace 0
  (X.2 : X.val ∈ ker (traceLinearMap); Matrix.trace_fin_two ⇒ X.val 1 1 = - X.val 0 0);
  ZeroMemClass.coe_zero; Submodule.mem_span_singleton (∃ λ, λ•X = y); Submodule.coe_smul;
  Matrix.mul_apply + Fin.sum_univ_two + Matrix.sub_apply.
Proof: y ∈ ker ⇒ ⁅X,y⁆=0 ⇒ hcomm : X.val*y.val - y.val*X.val = 0. Let a=X00,b=X01,c=X10 (X11=-a);
  s=y00,t=y01,u=y10 (y11=-s). The 4 commutator entries give (using 2≠0):
    (0,0): b*u - c*t = 0 ;  (0,1): 2(a*t - b*s)=0 ;  (1,0): 2(c*s - a*u)=0 ;  (1,1) = -(0,0).
  [This is exactly (a,b,c) × (s,t,u) = 0 in K³.]  Case split on X ≠ 0 (¬(a=b=c=0)):
    a≠0: λ:=s/a; t=bs/a=λb (from at=bs), u=cs/a=λc (from cs=au), s=λa. 
    a=0,b≠0: λ:=t/b; s=0 (bs=at=0), u=ct/b=λc (from bu=ct), t=λb.
    a=0,b=0,c≠0: λ:=u/c; s=0 (cs=au=0), t=0 (ct=bu=0), u=λc.
  Then y=λ•X via Subtype.ext; funext i j; fin_cases; Submodule.coe_smul; field_simp; ring.
FINRANK COROLLARY: sl2_centralizer_finrank_le_one : X≠0 ⇒ finrank(ker(ad X)) ≤ 1 :=
  (Submodule.finrank_mono (sl2_ker_ad_le_span ..)).trans (by rw finrank_span_singleton hX; ...).
TIER-B ASSEMBLY (all Mathlib-supported): H nilpotent subalgebra of 𝔤⊆𝔰𝔩₂, H≠0 ⇒
  non_trivial_center_of_isNilpotent ⇒ ∃ X∈Z(H), X≠0 ⇒ H ⊆ ker(ad_𝔰𝔩₂ X) ⇒ finrank H ≤ 1.
  rank 𝔤 = finrank(engel_𝔤 x*) [engel of regular = Cartan, nilpotent] ⇒ rank 𝔤 ≤ 1.
STATUS: math complete + API pinned; NOT transcribed/verified (blind ~2.5min compile loop, lsp down).

--- LANDED 2026-07-26 (#4285, AtomicityLieRank.lean, all sorry-free, lean-direct exit 0) ---
- sl2_ker_ad_le_span (KEYSTONE): ker(ad X) ≤ K∙X for X ≠ 0 — the hard core; cross-product /
  pivot-case-split coordinate proof, exactly as the worked proof above.
- sl2_centralizer_finrank_le_one: finrank(ker(ad X)) ≤ 1 for X ≠ 0.
- sl2_finrank_le_one_of_central: subalgebra A ⊆ 𝔰𝔩₂ with a nonzero element central in A has
  finrank A ≤ 1 (the Tier-B bridge).
- sl2_abelian_finrank_le_one: abelian subalgebra of 𝔰𝔩₂ (Nontrivial) has finrank ≤ 1.

CLOSED 2026-07-26 (#4285): sl2_subalgebra_rank_le_one — rank 𝔤 ≤ 1 for every 𝔤 ⊆ 𝔰𝔩₂,
sorry-free. Final wiring landed via exists_isCartanSubalgebra_engel + rank_le_finrank_engel +
non_trivial_center_of_isNilpotent + the inclusion ι:H↪𝔰𝔩₂ range ⊆ ker(ad (ιZ)) + the keystone.
Needed generous heartbeat limits (maxHeartbeats 1.6M / synthInstance 400k) for the nested-type
typeclass search. The ENTIRE Tier-B atomicity upper bound is now proved from the keystone up.

--- (historical) REMAINING (final wiring only — the hard math is done): rank 𝔤 ≤ 1 for 𝔤 ⊆ 𝔰𝔩₂.
Chain: rank 𝔤 = finrank(engel_𝔤 x*) at 𝔤-regular x* [isRegular_iff_finrank_engel_eq_rank, Infinite K];
engel_𝔤 x* is a nilpotent Cartan [IsCartanSubalgebra ⇒ LieRing.IsNilpotent];
non_trivial_center_of_isNilpotent ⇒ ∃ nonzero central X ∈ engel_𝔤 x*;
X central ⇒ ∀ y ∈ (engel viewed in 𝔰𝔩₂), ⁅X,y⁆=0 ⇒ sl2_finrank_le_one_of_central ⇒ finrank ≤ 1.
Plumbing risk: engel_𝔤 as a LieSubalgebra of 𝔰𝔩₂ (sub-of-sub), center-element coercion, the
∀ y ∈ A hypothesis across the inclusion. Consumer plumbing on the landed bridge, not new math.
