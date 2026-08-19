---
doc_id: poincare-proof-outline
doc_title: "Poincaré Disc Model Danijela Simić Filip Marić Pierre Boutry"
section_id: sec-055-pasch-axiom
section_title: "Pasch axiom"
section_number: null
pages: 127-138
source_pdf: POINCARE-proof-outline.pdf
source_sha256: 8ac25ddb38d360b4
doc_brief: "Poincaré Disc Model Danijela Simić Filip Marić Pierre Boutry — We describe formalization of the Poincaré disc model of hyperbolic geometry within the Isabelle/HOL proof assistant."
---
lemma Pasch-fun-mono:
ﬁxes r1 r2 :: real
assumes 0 < r1 and r1≤ r2 and r2 < 1
shows r1 + 1/r1≥ r2 + 1/r2
proof (cases r1 = r2 )
case True
thus ?thesis
by simp
next
case False
hence r2− r1 > 0
using assms
by simp
have r1∗ r2 < 1
using assms
by (smt mult-le-cancel-left1 )
hence 1 / (r1∗ r2 ) > 1
using assms
by simp
hence (r2− r1 ) / (r1∗ r2 ) > (r2− r1 )
using ‹r2− r1 > 0 ›
using mult-less-cancel-left-pos[of r2 − r1 1 1 / (r1∗ r2 )]
by simp
hence 1 / r1− 1 / r2 > r2− r1
using assms
by (simp add : ﬁeld-simps)
thus ?thesis
by simp
127
qed
Pasch axiom, non-degenerative case.
lemma Pasch-nondeg:
assumes x∈ unit-disc and y∈ unit-disc and z∈ unit-disc and u∈ unit-disc and v∈ unit-disc
assumes distinct [x, y, z, u, v]
assumes¬ poincare-collinear{x, y, z}
assumes poincare-between x u z and poincare-between y v z
shows∃ a. a∈ unit-disc∧ poincare-between u a y ∧ poincare-between x a v
proof−
have∀ y z u. distinct [x, y, z, u, v]∧¬ poincare-collinear{x, y, z}∧ y∈ unit-disc∧ z∈ unit-disc∧ u∈ unit-disc∧
poincare-between x u z ∧ poincare-between y v z −→ (∃ a. a∈ unit-disc∧ poincare-between u a y ∧
poincare-between x a v ) ( is ?P x v )
proof (rule wlog-positive-x-axis [where P=?P])
ﬁx v
assume v: is-real v 0 < Re v Re v < 1
hence of-complex v ∈ unit-disc
by (auto simp add : cmod-eq-Re)
show ?P 0 h (of-complex v )
proof safe
ﬁx y z u
assume distinct: distinct [0 h, y, z, u, of-complex v ]
assume in-disc: y∈ unit-disc z ∈ unit-disc u ∈ unit-disc
then obtain y ′ z ′ u ′
where∗: y = of-complex y ′ z = of-complex z ′ u = of-complex u ′
using inf-or-of-complex inf-notin-unit-disc
by metis
have y ′⁄= 0 z ′⁄= 0 u ′⁄= 0 v ⁄= 0 y ′⁄= z ′ y ′⁄= u ′ z ′⁄= u ′ y⁄= z y ⁄= u z ⁄= u
using of-complex-inj distinct ∗
by auto
note distinct = distinct this
assume¬ poincare-collinear{0 h, y, z}
hence nondeg-yz: y ′∗cnj z ′⁄= cnj y ′∗ z ′
using∗ poincare-collinear-zero-iﬀ[of y ′ z ′] in-disc distinct
by auto
assume poincare-between 0h u z
hence Arg u ′ = Arg z ′ cmod u ′≤ cmod z ′
using∗ poincare-between-0uv[of u z ] distinct in-disc
by auto
then obtain ϕ ru rz where
uz-polar: u ′ = cor ru ∗ cis ϕ z ′ = cor rz ∗ cis ϕ 0 < ru ru ≤ rz 0 < rz and
ϕ = Arg u ′ϕ = Arg z ′
using∗ ‹u ′⁄= 0 › ‹z ′⁄= 0 ›
by (smt cmod-cis norm-le-zero-iﬀ )
obtain ϑ ry where
y-polar: y ′ = cor ry ∗ cis ϑ ry > 0 and ϑ = Arg y ′
using ‹y ′⁄= 0 ›
by (smt cmod-cis norm-le-zero-iﬀ )
from in-disc∗ ‹u ′ = cor ru ∗ cis ϕ› ‹z ′ = cor rz ∗ cis ϕ› ‹y ′ = cor ry ∗ cis ϑ›
have ru < 1 rz < 1 ry < 1
by (auto simp : norm-mult)
note polar = this y-polar uz-polar
have nondeg: cis ϑ∗ cis (− ϕ)⁄= cis (− ϑ)∗ cis ϕ
using nondeg-yz polar
by simp
128
let ?yz = poincare-line y z
let ?v = calc-x-axis-intersection ?yz
assume poincare-between y (of-complex v ) z
hence of-complex v ∈ circline-set ?yz
using in-disc ‹of-complex v ∈ unit-disc›
using distinct poincare-between-poincare-collinear[of y of-complex v z ]
using unique-poincare-line[of y z ]
by (auto simp add : poincare-collinear-def)
moreover
have of-complex v ∈ circline-set x-axis
using ‹is-real v ›
unfolding circline-set-x-axis
by auto
moreover
have ?yz⁄= x-axis
proof (rule ccontr )
assume¬ ?thesis
hence{0 h, y, z}⊆ circline-set (poincare-line y z )
unfolding circline-set-def
using distinct poincare-line[of y z ]
by auto
hence poincare-collinear{0 h, y, z}
unfolding poincare-collinear-def
using distinct
by force
thus False
using ‹¬ poincare-collinear{0 h, y, z}›
by simp
qed
ultimately
have ?v = of-complex v intersects-x-axis ?yz
using unique-calc-x-axis-intersection[of poincare-line y z of-complex v ]
using intersects-x-axis-iﬀ [of ?yz ]
using distinct ‹of-complex v ∈ unit-disc›
by (metis IntI is-poincare-line-poincare-line)+
have intersects-x-axis-positive ?yz
using ‹Re v > 0 › ‹of-complex v ∈ unit-disc›
using ‹of-complex v ∈ circline-set ?yz › ‹of-complex v ∈ circline-set x-axis ›
using intersects-x-axis-positive-iﬀ [of ?yz ] ‹y⁄= z› ‹?yz⁄= x-axis›
unfolding positive-x-axis-def
by force
have y /∈ circline-set x-axis
proof (rule ccontr )
assume¬ ?thesis
moreover
hence poincare-line y (of-complex v ) = x-axis
using distinct ‹of-complex v ∈ circline-set x-axis ›
using in-disc ‹of-complex v ∈ unit-disc›
using unique-poincare-line[of y of-complex v x-axis ]
by simp
moreover
have z∈ circline-set (poincare-line y (of-complex v ))
using ‹of-complex v ∈ circline-set ?yz ›
using unique-poincare-line[of y of-complex v poincare-line y z ]
using in-disc ‹of-complex v ∈ unit-disc› distinct
using poincare-line[of y z ]
unfolding circline-set-def
by (metis distinct-length-2-or-more is-poincare-line-poincare-line mem-Collect-eq )
ultimately
have y∈ circline-set x-axis z ∈ circline-set x-axis
by auto
129
hence poincare-collinear{0 h, y, z}
unfolding poincare-collinear-def
by force
thus False
using ‹¬ poincare-collinear{0 h, y, z}›
by simp
qed
moreover
have z /∈ circline-set x-axis
proof (rule ccontr )
assume¬ ?thesis
moreover
hence poincare-line z (of-complex v ) = x-axis
using distinct ‹of-complex v ∈ circline-set x-axis ›
using in-disc ‹of-complex v ∈ unit-disc›
using unique-poincare-line[of z of-complex v x-axis ]
by simp
moreover
have y∈ circline-set (poincare-line z (of-complex v ))
using ‹of-complex v ∈ circline-set ?yz ›
using unique-poincare-line[of z of-complex v poincare-line y z ]
using in-disc ‹of-complex v ∈ unit-disc› distinct
using poincare-line[of y z ]
unfolding circline-set-def
by (metis distinct-length-2-or-more is-poincare-line-poincare-line mem-Collect-eq )
ultimately
have y∈ circline-set x-axis z ∈ circline-set x-axis
by auto
hence poincare-collinear{0 h, y, z}
unfolding poincare-collinear-def
by force
thus False
using ‹¬ poincare-collinear{0 h, y, z}›
by simp
qed
ultimately
haveϕ∗ ϑ <0
using ‹poincare-between y (of-complex v ) z›
using poincare-between-x-axis-intersection[of y z of-complex v ]
using in-disc ‹of-complex v ∈ unit-disc› distinct
using ‹of-complex v ∈ circline-set ?yz › ‹of-complex v ∈ circline-set x-axis ›
using ‹ϕ = Arg z ′› ‹ϑ = Arg y ′›∗
by (simp add : ﬁeld-simps)
haveϕ⁄= pi ϕ⁄= 0
using ‹z /∈ circline-set x-axis ›∗ polar cis-pi
unfolding circline-set-x-axis
by auto
haveϑ⁄= pi ϑ⁄= 0
using ‹y /∈ circline-set x-axis ›∗ polar cis-pi
unfolding circline-set-x-axis
by auto
have phi-sin: ϕ >0←→ sin ϕ >0 ϕ <0←→ sin ϕ <0
using ‹ϕ = Arg z ′› ‹ϕ⁄= 0 › ‹ϕ⁄= pi›
using Arg-bounded[of z ′]
by (smt sin-gt-zero sin-le-zero sin-pi-minus sin-0-iﬀ-canon sin-ge-zero )+
have theta-sin: ϑ >0←→ sin ϑ >0 ϑ <0←→ sin ϑ <0
using ‹ϑ = Arg y ′› ‹ϑ⁄= 0 › ‹ϑ⁄= pi›
using Arg-bounded[of y ′]
130
by (smt sin-gt-zero sin-le-zero sin-pi-minus sin-0-iﬀ-canon sin-ge-zero )+
have sin ϕ∗ sin ϑ <0
using ‹ϕ∗ ϑ <0 › phi-sin theta-sin
by (simp add : mult-less-0-iﬀ )
have sin (ϕ− ϑ)⁄= 0
proof (rule ccontr )
assume¬ ?thesis
hence sin (ϕ− ϑ) = 0
by simp
have− 2∗ pi < ϕ− ϑ ϕ− ϑ <2∗ pi
using ‹ϕ = Arg z ′› ‹ϑ = Arg y ′› Arg-bounded[of z ′] Arg-bounded[of y ′] ‹ϕ⁄= pi› ‹ϑ⁄= pi›
by auto
hence ϕ− ϑ =−pi∨ ϕ− ϑ = 0∨ ϕ− ϑ = pi
using ‹sin (ϕ− ϑ) = 0 ›
by (smt sin-0-iﬀ-canon sin-periodic-pi2 )
moreover
{
assume ϕ− ϑ =− pi
hence ϕ = ϑ− pi
by simp
hence False
using nondeg-yz
using ‹y ′ = cor ry ∗ cis ϑ› ‹z ′ = cor rz ∗ cis ϕ› ‹rz > 0 › ‹ry > 0 ›
by auto
}
moreover
{
assume ϕ− ϑ = 0
hence ϕ = ϑ
by simp
hence False
using ‹y ′ = cor ry ∗ cis ϑ› ‹z ′ = cor rz ∗ cis ϕ› ‹rz > 0 › ‹ry > 0 ›
using nondeg-yz
by auto
}
moreover
{
assume ϕ− ϑ = pi
hence ϕ = ϑ + pi
by simp
hence False
using ‹y ′ = cor ry ∗ cis ϑ› ‹z ′ = cor rz ∗ cis ϕ› ‹rz > 0 › ‹ry > 0 ›
using nondeg-yz
by auto
}
ultimately
show False
by auto
qed
have u /∈ circline-set x-axis
proof−
have¬ is-real u ′
using∗ polar in-disc
using ‹ϕ⁄= 0 › ‹ϕ = Arg u ′› ‹ϕ⁄= pi› phi-sin(1 ) phi-sin(2 )
by (metis is-real-arg2 )
moreover
have u⁄=∞h
using in-disc
by auto
ultimately
show ?thesis
using∗ of-complex-inj[of u ′]
unfolding circline-set-x-axis
131
by auto
qed
let ?yu = poincare-line y u
have nondeg-yu: y ′∗ cnj u ′⁄= cnj u ′∗ u ′
using nondeg-yz polar ‹ru > 0 › ‹rz > 0 › distinct
by auto
{
ﬁx r :: real
assume r > 0
have den: cor ry ∗ cis ϑ∗ cnj 1 ∗ cnj (cor r ∗ cis ϕ)∗ 1− cor r ∗ cis ϕ∗ cnj 1 ∗ cnj (cor ry ∗ cis ϑ)∗ 1⁄= 0
using ‹0 < r› ‹0 < ry› nondeg
by auto
let ?A = 2∗ r∗ ry∗ sin(ϕ− ϑ)
let ?B = i ∗ (r∗ cis ϕ∗ (1 + ry2)− ry∗ cis ϑ∗ (1 + r 2))
let ?ReB = ry∗ (1 + r 2)∗ sin ϑ− r∗ (1 + ry2)∗ sin ϕ
have Re (i∗ (r∗ cis (−ϕ)∗ ry∗ cis (ϑ)− ry∗ cis (−ϑ)∗ r∗ cis (ϕ))) = ?A
by (simp add : sin-diﬀ ﬁeld-simps )
moreover
have cor ry ∗ cis (− ϑ)∗ (cor ry ∗ cis ϑ) = ry2 cor r ∗ cis (− ϕ)∗ (cor r ∗ cis ϕ) = r 2
by (metis cis-inverse cis-neq-zero divide-complex-def cor-squared nonzero-mult-div-cancel-right power2-eq-square
semiring-normalization-rules(15 ))+
ultimately
have 1 : poincare-line-cvec-cmat (of-complex-cvec (cor ry ∗ cis ϑ)) ( of-complex-cvec (cor r ∗ cis ϕ)) = ( ?A, ?B,
cnj ?B, ?A)
using den
unfolding poincare-line-cvec-cmat-def of-complex-cvec-def Let-def prod.case
by (simp add : ﬁeld-simps)
have 2 : is-real ?A
by simp
let ?mix = cis ϑ∗ cis (− ϕ)− cis (− ϑ)∗ cis ϕ
have is-imag ?mix
using eq-minus-cnj-iﬀ-imag[of ?mix ]
by simp
hence Im ?mix ⁄= 0
using nondeg
using complex.expand[of ?mix 0 ]
by auto
hence 3 : Re ?A⁄= 0
using ‹r > 0 › ‹ry > 0 ›
by (simp add : sin-diﬀ ﬁeld-simps )
have ?A⁄= 0
using 2 3
by auto
hence 4 : cor ?A⁄= 0
using 2 3
by (metis zero-complex.simps(1 ))
have 5 : ?ReB / ?A = ( sin ϑ) / (2∗ sin(ϕ− ϑ))∗ (1/r + r)− (sin ϕ) / (2∗ sin (ϕ− ϑ))∗ (1/ry + ry)
using ‹ry > 0 › ‹r > 0 ›
apply (subst diﬀ-divide-distrib )
apply (subst add-frac-num, simp)
apply (subst add-frac-num, simp)
apply (simp add : power2-eq-square mult.commute)
apply (simp add : ﬁeld-simps)
done
have poincare-line-cvec-cmat (of-complex-cvec (cor ry ∗ cis ϑ)) ( of-complex-cvec (cor r ∗ cis ϕ)) = ( ?A, ?B, cnj
?B, ?A)∧
132
is-real ?A∧ Re ?A⁄= 0∧ ?A⁄= 0∧ cor ?A⁄= 0∧
Re ?B = ?ReB∧
?ReB / ?A = ( sin ϑ) / (2∗ sin(ϕ− ϑ))∗ (1/r + r)− (sin ϕ) / (2∗ sin (ϕ− ϑ))∗ (1/ry + ry)
using 1 2 3 4 5
by auto
}
note∗∗ = this
let ?Ayz = 2∗ rz∗ ry∗ sin (ϕ− ϑ)
let ?Byz = i ∗ (rz∗ cis ϕ∗ (1 + ry2)− ry∗ cis ϑ∗ (1 + rz 2))
let ?ReByz = ry∗ (1 + rz 2)∗ sin ϑ− rz∗ (1 + ry2)∗ sin ϕ
let ?Kz = ( sin ϑ) / (2∗ sin(ϕ− ϑ))∗ (1/rz + rz)− (sin ϕ) / (2∗ sin (ϕ− ϑ))∗ (1/ry + ry)
have yz: poincare-line-cvec-cmat (of-complex-cvec (cor ry ∗ cis ϑ)) ( of-complex-cvec (cor rz ∗ cis ϕ)) = ( ?Ayz,
?Byz, cnj ?Byz, ?Ayz)
is-real ?Ayz Re ?Ayz ⁄= 0 ?Ayz ⁄= 0 cor ?Ayz ⁄= 0 Re ?Byz = ?ReByz and Kz: ?ReByz / ?Ayz = ?Kz
using∗∗[OF ‹0 < rz›]
by auto
let ?Ayu = 2∗ ru∗ ry∗ sin (ϕ− ϑ)
let ?Byu = i ∗ (ru∗ cis ϕ∗ (1 + ry2)− ry∗ cis ϑ∗ (1 + ru2))
let ?ReByu = ry∗ (1 + ru2)∗ sin ϑ− ru∗ (1 + ry2)∗ sin ϕ
let ?Ku = ( sin ϑ) / (2∗ sin(ϕ− ϑ))∗ (1/ru + ru)− (sin ϕ) / (2∗ sin (ϕ− ϑ))∗ (1/ry + ry)
have yu: poincare-line-cvec-cmat (of-complex-cvec (cor ry ∗ cis ϑ)) ( of-complex-cvec (cor ru ∗ cis ϕ)) = ( ?Ayu,
?Byu, cnj ?Byu, ?Ayu)
is-real ?Ayu Re ?Ayu ⁄= 0 ?Ayu ⁄= 0 cor ?Ayu ⁄= 0 Re ?Byu = ?ReByu and Ku: ?ReByu / ?Ayu = ?Ku
using∗∗[OF ‹0 < ru›]
by auto
have ?Ayz⁄= 0
using ‹sin (ϕ− ϑ)⁄= 0 › ‹ry > 0 › ‹rz > 0 ›
by auto
have Re ?Byz / ?Ayz <−1
using ‹intersects-x-axis-positive ?yz ›
∗ ‹y ′ = cor ry ∗ cis ϑ› ‹z ′ = cor rz ∗ cis ϕ› ‹u ′ = cor ru ∗ cis ϕ›
apply simp
apply (transfer ﬁxing : ry rz ru ϑ ϕ)
apply (transfer ﬁxing : ry rz ru ϑ ϕ)
proof−
assume intersects-x-axis-positive-cmat (poincare-line-cvec-cmat (of-complex-cvec (cor ry∗ cis ϑ)) ( of-complex-cvec
(cor rz ∗ cis ϕ)))
thus (ry∗ sin ϑ∗ (1 + rz 2)− rz∗ sin ϕ∗ (1 + ry2)) / (2∗ rz∗ ry∗ sin (ϕ− ϑ)) <− 1
using yz
by simp
qed
have ?ReByz / ?Ayz≥ ?ReByu / ?Ayu
proof (cases sin ϕ >0 )
case True
hence sin ϑ <0
using ‹sin ϕ∗ sin ϑ <0 ›
by (smt mult-nonneg-nonneg )
have ?ReByz < 0
proof−
have ry∗ (1 + rz 2)∗ sin ϑ <0
using ‹ry > 0 › ‹rz > 0 ›
using ‹sin ϑ <0 ›
by (smt mult-pos-neg mult-pos-pos zero-less-power )
moreover
have rz∗ (1 + ry2)∗ sin ϕ >0
using ‹ry > 0 › ‹rz > 0 ›
using ‹sin ϕ >0 ›
by (smt mult-pos-neg mult-pos-pos zero-less-power )
ultimately
show ?thesis
133
by simp
qed
have ?Ayz > 0
using ‹Re ?Byz / ?Ayz <−1 › ‹Re ?Byz = ?ReByz› ‹?ReByz < 0 ›
by (smt divide-less-0-iﬀ )
hence sin (ϕ− ϑ) > 0
using ‹ry > 0 › ‹rz > 0 ›
by (smt mult-pos-pos zero-less-mult-pos )
have 1 / ru + ru≥ 1 / rz + rz
using Pasch-fun-mono[of ru rz ] ‹0 < ru› ‹ru≤ rz› ‹rz < 1 ›
by simp
hence sin ϑ∗ (1 / ru + ru)≤ sin ϑ∗ (1 / rz + rz)
using ‹sin ϑ <0 ›
by auto
thus ?thesis
using ‹ru > 0 › ‹rz > 0 › ‹ru≤ rz› ‹rz < 1 › ‹?Ayz > 0 › ‹sin (ϕ− ϑ) > 0 ›
using divide-right-mono[of sin ϑ∗ (1 / ru + ru) sin ϑ∗ (1 / rz + rz) 2∗ sin (ϕ− ϑ)]
by (subst Kz, subst Ku ) simp
next
assume¬ sin ϕ >0
hence sin ϕ <0
using ‹sin ϕ∗ sin ϑ <0 ›
by (cases sin ϕ = 0, simp-all )
hence sin ϑ >0
using ‹sin ϕ∗ sin ϑ <0 ›
by (smt mult-nonpos-nonpos )
have ?ReByz > 0
proof−
have ry∗ (1 + rz 2)∗ sin ϑ >0
using ‹ry > 0 › ‹rz > 0 ›
using ‹sin ϑ >0 ›
by (smt mult-pos-neg mult-pos-pos zero-less-power )
moreover
have rz∗ (1 + ry2)∗ sin ϕ <0
using ‹ry > 0 › ‹rz > 0 ›
using ‹sin ϕ <0 ›
by (smt mult-pos-neg mult-pos-pos zero-less-power )
ultimately
show ?thesis
by simp
qed
have ?Ayz < 0
using ‹Re ?Byz / ?Ayz <−1 › ‹?Ayz⁄= 0 › ‹Re ?Byz = ?ReByz› ‹?ReByz > 0 ›
by (smt divide-less-0-iﬀ )
hence sin (ϕ− ϑ) < 0
using ‹ry > 0 › ‹rz > 0 ›
by (smt mult-nonneg-nonneg )
have 1 / ru + ru≥ 1 / rz + rz
using Pasch-fun-mono[of ru rz ] ‹0 < ru› ‹ru≤ rz› ‹rz < 1 ›
by simp
hence sin ϑ∗ (1 / ru + ru)≥ sin ϑ∗ (1 / rz + rz)
using ‹sin ϑ >0 ›
by auto
thus ?thesis
using ‹ru > 0 › ‹rz > 0 › ‹ru≤ rz› ‹rz < 1 › ‹?Ayz < 0 › ‹sin (ϕ− ϑ) < 0 ›
using divide-right-mono-neg[of sin ϑ∗ (1 / rz + rz) sin ϑ∗ (1 / ru + ru) 2∗ sin (ϕ− ϑ)]
by (subst Kz, subst Ku ) simp
qed
have intersects-x-axis-positive ?yu
using∗ ‹y ′ = cor ry ∗ cis ϑ› ‹z ′ = cor rz ∗ cis ϕ› ‹u ′ = cor ru ∗ cis ϕ›
apply simp
apply (transfer ﬁxing : ry rz ru ϑ ϕ)
apply (transfer ﬁxing : ry rz ru ϑ ϕ)
134
proof−
have Re ?Byu / ?Ayu <−1
using ‹Re ?Byz / ?Ayz <−1 › ‹?ReByz / ?Ayz≥ ?ReByu / ?Ayu›
by (subst (asm) ‹Re ?Byz = ?ReByz›, subst ‹Re ?Byu = ?ReByu›) simp
thus intersects-x-axis-positive-cmat (poincare-line-cvec-cmat (of-complex-cvec (cor ry ∗ cis ϑ)) ( of-complex-cvec
(cor ru ∗ cis ϕ)))
using yu
by simp
qed
let ?a = calc-x-axis-intersection ?yu
have ?a∈ positive-x-axis ?a ∈ circline-set ?yu ?a ∈ unit-disc
using ‹intersects-x-axis-positive ?yu ›
using intersects-x-axis-positive-iﬀ ′[of ?yu ] ‹y⁄= u›
by auto
then obtain a ′ where a ′: ?a = of-complex a ′ is-real a ′ Re a ′> 0 Re a ′< 1
unfolding positive-x-axis-def circline-set-x-axis
by (auto simp add : cmod-eq-Re)
have intersects-x-axis ?yz intersects-x-axis ?yu
using ‹intersects-x-axis-positive ?yz › ‹intersects-x-axis-positive ?yu ›
by auto
show∃ a. a∈ unit-disc∧ poincare-between u a y ∧ poincare-between 0h a (of-complex v )
proof (rule-tac x =?a in exI, safe)
show poincare-between u ?a y
using poincare-between-x-axis-intersection[of y u ?a ]
using calc-x-axis-intersection[OF is-poincare-line-poincare-line[OF ‹y⁄= u›] ‹intersects-x-axis ?yu ›]
using calc-x-axis-intersection-in-unit-disc[OF is-poincare-line-poincare-line[OF ‹y⁄= u›] ‹intersects-x-axis ?yu ›]
using in-disc ‹y⁄= u› ‹y /∈ circline-set x-axis › ‹u /∈ circline-set x-axis ›
using∗ ‹ϕ = Arg u ′› ‹ϑ = Arg y ′› ‹ϕ∗ ϑ <0 ›
by (subst poincare-between-rev, auto simp add : mult.commute)
next
show poincare-between 0h ?a (of-complex v )
proof−
have−?ReByz / ?Ayz≤− ?ReByu / ?Ayu
using ‹?ReByz / ?Ayz≥ ?ReByu / ?Ayu›
by linarith
have outward ?yz ?yu
using∗ ‹y ′ = cor ry ∗ cis ϑ› ‹z ′ = cor rz ∗ cis ϕ› ‹u ′ = cor ru ∗ cis ϕ›
apply simp
apply (transfer ﬁxing : ry rz ru ϑ ϕ)
apply (transfer ﬁxing : ry rz ru ϑ ϕ)
apply (subst yz yu )+
unfolding outward-cmat-def
apply (simp only : Let-def prod.case)
apply (subst yz yu )+
using ‹−?ReByz / ?Ayz≤− ?ReByu / ?Ayu›
by simp
hence Re a ′≤ Re v
using ‹?v = of-complex v ›
using ‹?a = of-complex a ′›
using ‹intersects-x-axis-positive ?yz › ‹intersects-x-axis-positive ?yu ›
using outward[OF is-poincare-line-poincare-line[OF ‹y⁄= z›] is-poincare-line-poincare-line[OF ‹y⁄= u›]]
by simp
thus ?thesis
using ‹?v = of-complex v ›
using poincare-between-x-axis-0uv[of Re a ′ Re v ] a ′ v
by simp
qed
next
show ?a∈ unit-disc
by fact
qed
qed
135
next
show x∈ unit-disc v ∈ unit-disc x ⁄= v
using assms
by auto
next
ﬁx M x v
let ?Mx = moebius-pt M x and ?Mv = moebius-pt M v
assume 1 : unit-disc-ﬁx M x ∈ unit-disc v ∈ unit-disc x ⁄= v
assume 2 : ?P ?Mx ?Mv
show ?P x v
proof safe
ﬁx y z u
let ?My = moebius-pt M y and ?Mz = moebius-pt M z and ?Mu = moebius-pt M u
assume distinct [x, y, z, u, v]¬ poincare-collinear{x, y, z} y∈ unit-disc z ∈ unit-disc u ∈ unit-disc
poincare-between x u z poincare-between y v z
hence∃ Ma. Ma∈ unit-disc∧ poincare-between ?Mu Ma ?My ∧ poincare-between ?Mx Ma ?Mv
using 1 2 [rule-format, of ?My ?Mz ?Mu ]
by simp
then obtain Ma where Ma: Ma∈ unit-disc poincare-between ?Mu Ma ?My ∧ poincare-between ?Mx Ma ?Mv
by blast
let ?a = moebius-pt (−M ) Ma
let ?Ma = moebius-pt M ?a
have ?Ma = Ma
by (metis moebius-pt-invert uminus-moebius-def )
hence ?Ma∈ unit-disc poincare-between ?Mu ?Ma ?My ∧ poincare-between ?Mx ?Ma ?Mv
using Ma
by auto
thus∃ a. a∈ unit-disc∧ poincare-between u a y ∧ poincare-between x a v
using unit-disc-ﬁx-moebius-inv[OF ‹unit-disc-ﬁx M ›] ‹unit-disc-ﬁx M › ‹Ma∈ unit-disc›
using ‹u∈ unit-disc› ‹v∈ unit-disc› ‹x∈ unit-disc› ‹y∈ unit-disc›
by (rule-tac x =?a in exI, simp del : moebius-pt-comp-inv-right)
qed
qed
thus ?thesis
using assms
by auto
qed
Pasch axiom, only degenerative cases.
lemma Pasch-deg:
assumes x∈ unit-disc and y∈ unit-disc and z∈ unit-disc and u∈ unit-disc and v∈ unit-disc
assumes¬ distinct [x, y, z, u, v]∨ poincare-collinear{x, y, z}
assumes poincare-between x u z and poincare-between y v z
shows∃ a. a∈ unit-disc∧ poincare-between u a y ∧ poincare-between x a v
proof (cases poincare-collinear{x, y, z})
case True
hence poincare-between x y z ∨ poincare-between y x z ∨ poincare-between y z x
using assms(1, 2, 3 ) poincare-collinear3-between poincare-between-revby blast
show ?thesis
proof (cases poincare-between x y z )
case True
have poincare-between x y v
using True assms poincare-between-transitivity
by (meson poincare-between-rev)
thus ?thesis
using assms(2 )
by (rule-tac x =y in exI, simp)
next
case False
hence poincare-between y x z ∨ poincare-between y z x
using ‹poincare-between x y z ∨ poincare-between y x z ∨ poincare-between y z x ›
by simp
show ?thesis
proof (cases poincare-between y x z )
case True
hence poincare-between u x y
136
using assms
by (meson poincare-between-rev poincare-between-transitivity)
thus ?thesis
using assms
by (rule-tac x =x in exI, simp)
next
case False
hence poincare-between y z x
using ‹poincare-between y x z ∨ poincare-between y z x ›
by auto
hence poincare-between x z v
using assms
by (meson poincare-between-rev poincare-between-transitivity)
hence poincare-between x u v
using assms poincare-between-transitivity poincare-between-rev
by (smt poincare-between-sum-distances)
thus ?thesis
using assms
by (rule-tac x =u in exI, simp)
qed
qed
next
case False
hence¬ distinct [x, y, z, u, v]
using assms(6 ) by auto
show ?thesis
proof (cases u =z)
case True
thus ?thesis
using assms
apply(rule-tac x =v in exI )
by(simp add :poincare-between-rev)
next
case False
hence x⁄= z
using assms poincare-between-sandwich by blast
show ?thesis
proof (cases v =z)
case True
thus ?thesis
using assms
by (rule-tac x =u in exI, simp)
next
case False
hence y⁄= z
using assms poincare-between-sandwich by blast
show ?thesis
proof (cases u = x)
case True
thus ?thesis
using assms
by (rule-tac x =x in exI, simp)
next
case False
have x⁄= y
using assms ‹¬ poincare-collinear{x, y, z}›
by fastforce
have x⁄= v
using assms ‹¬ poincare-collinear{x, y, z}›
by (metis insert-commute poincare-between-poincare-collinear)
have u⁄= y
using assms ‹¬ poincare-collinear{x, y, z}›
using poincare-between-poincare-collinearby blast
have u⁄= v
proof (rule ccontr )
assume¬ u⁄= v
137
hence poincare-between x v z
using assms by auto
hence x∈ circline-set (poincare-line z v )
using poincare-between-rev[of x v z ]
using poincare-between-poincare-line-uvz[of z v x ]
using assms ‹v⁄= z›
by auto
have y∈ circline-set (poincare-line z v )
using assms ‹¬ u⁄= v›
using poincare-between-rev[of y v z ]
using poincare-between-poincare-line-uvz[of z v y ]
using assms ‹v⁄= z›
by auto
have z∈ circline-set (poincare-line z v )
using ex-poincare-line-two-points[of z v ] ‹v⁄= z›
by auto
have is-poincare-line (poincare-line z v )
using ‹v⁄= z›
by auto
hence poincare-collinear{x, y, z}
using ‹x∈ circline-set (poincare-line z v )›
using ‹y∈ circline-set (poincare-line z v )›
using ‹z∈ circline-set (poincare-line z v )›
unfolding poincare-collinear-def
by (rule-tac x =poincare-line z v in exI, simp)
thus False
using ‹¬ poincare-collinear{x, y, z}› by simp
qed
have v = y
using ‹u⁄= v› ‹u⁄= y› ‹x⁄= v› ‹x⁄= y› ‹u⁄= x› ‹y⁄= z› ‹v⁄= z› ‹x⁄= z› ‹u⁄= z›
using ‹¬ distinct [x, y, z, u, v]›
by auto
thus ?thesis
using assms
by (rule-tac x =y in exI, simp)
qed
qed
qed
qed
Axiom of Pasch
lemma Pasch:
assumes x∈ unit-disc and y∈ unit-disc and z∈ unit-disc and u∈ unit-disc and v∈ unit-disc
assumes poincare-between x u z and poincare-between y v z
shows∃ a. a∈ unit-disc∧ poincare-between u a y ∧ poincare-between x a v
proof (cases distinct [x, y, z, u, v]∧¬ poincare-collinear{x, y, z})
case True
thus ?thesis
using assms Pasch-nondeg by auto
next
case False
thus ?thesis
using assms Pasch-deg by auto
qed
