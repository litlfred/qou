---
doc_id: poincare-proof-outline
doc_title: "Poincaré Disc Model Danijela Simić Filip Marić Pierre Boutry"
section_id: sec-011-construction-of-the-h-line-between-the-two-given
section_title: "Construction of the h-line between the two given points"
section_number: null
pages: 17-20
source_pdf: POINCARE-proof-outline.pdf
source_sha256: 8ac25ddb38d360b4
doc_brief: "Poincaré Disc Model Danijela Simić Filip Marić Pierre Boutry — We describe formalization of the Poincaré disc model of hyperbolic geometry within the Isabelle/HOL proof assistant."
---
Next we show how to construct the (unique) h-line between the two given points in the Poincaré model
Geometrically, h-line can be constructed by ﬁnding the inverse point of one of the two points and by constructing
the circle (or line) trough it and the two given points.
Algebraically, for two given points u and v in C, the h-line matrix coeﬃcients can be A = i · (uv −vu) and
B =i · (v(|u|2 + 1) −u(|v|2 + 1)).
We need to extend this to homogenous coordinates. There are several degenerate cases.
- If {z,w } = {0h, ∞h} then there is no unique h-line (any line trough zero is an h-line).
- If z and w are mutually inverse, then the construction fails (both geometric and algebraic).
- If z and w are diﬀerent points on the unit circle, then the standard construction fails (only geometric).
- None of this problematic cases occur when z and w are inside the unit disc.
We express the construction algebraically, and construct the Hermitean circline matrix for the two points given
in homogenous coordinates. It works correctly in all cases except when the two points are the same or are
mutually inverse.
deﬁnition mk-poincare-line-cmat :: real⇒ complex⇒ complex-mat where
[simp]: mk-poincare-line-cmat A B = ( cor A, B, cnj B, cor A )
lemma mk-poincare-line-cmat-zero-iﬀ:
mk-poincare-line-cmat A B = mat-zero←→ A = 0∧ B = 0
by auto
lemma mk-poincare-line-cmat-hermitean
[simp]: hermitean (mk-poincare-line-cmat A B )
by simp
lemma mk-poincare-line-cmat-scale:
cor k ∗sm mk-poincare-line-cmat A B = mk-poincare-line-cmat (k∗ A) ( k∗ B)
by simp
deﬁnition poincare-line-cvec-cmat :: complex-vec⇒ complex-vec⇒ complex-mat where
[simp]: poincare-line-cvec-cmat z w =
(let (z1, z2 ) = z;
17
(w1, w2 ) = w;
nom = w1∗cnj w2∗(z1∗cnj z1 + z2∗cnj z2 )− z1∗cnj z2∗(w1∗cnj w1 + w2∗cnj w2 );
den = z1∗cnj z2∗cnj w1∗w2− w1∗cnj w2∗cnj z1∗z2
in if den ⁄= 0 then
mk-poincare-line-cmat (Re(i∗den)) (i∗nom)
else if z1∗cnj z2 ⁄= 0 then
mk-poincare-line-cmat 0 (i∗z1∗cnj z2 )
else if w1∗cnj w2 ⁄= 0 then
mk-poincare-line-cmat 0 (i∗w1∗cnj w2 )
else
mk-poincare-line-cmat 0 i)
lemma poincare-line-cvec-cmat-AeqD:
assumes poincare-line-cvec-cmat z w = ( A, B, C, D)
shows A = D
using assms
by (cases z, cases w ) ( auto split : if-split-asm)
lemma poincare-line-cvec-cmat-hermitean [simp]:
shows hermitean (poincare-line-cvec-cmat z w )
by (cases z, cases w ) ( auto split : if-split-asm simp del : mk-poincare-line-cmat-def)
lemma poincare-line-cvec-cmat-nonzero [simp]:
assumes z⁄= vec-zero w⁄= vec-zero
shows poincare-line-cvec-cmat z w ⁄= mat-zero
proof−
obtain z1 z2 w1 w2 where∗: z = ( z1, z2 ) w = ( w1, w2 )
by (cases z, cases w, auto)
let ?den = z1∗cnj z2∗cnj w1∗w2− w1∗cnj w2∗cnj z1∗z2
show ?thesis
proof (cases ?den ⁄= 0 )
case True
have is-real (i∗ ?den)
using eq-cnj-iﬀ-real[of i∗?den]
by (simp add : ﬁeld-simps)
hence Re (i∗ ?den)⁄= 0
using ‹?den⁄= 0 ›
by (metis complex-i-not-zero complex-surj mult-eq-0-iﬀ zero-complex .code)
thus ?thesis
using∗ ‹?den⁄= 0 ›
by (simp del : mk-poincare-line-cmat-def mat-zero-def add : mk-poincare-line-cmat-zero-iﬀ)
next
case False
thus ?thesis
using∗
by (simp del : mk-poincare-line-cmat-def mat-zero-def add : mk-poincare-line-cmat-zero-iﬀ)
qed
qed
lift-deﬁnition poincare-line-hcoords-clmat:: complex-homo-coords⇒ complex-homo-coords⇒ circline-mat is poincare-line-cvec-cmat
using poincare-line-cvec-cmat-hermitean poincare-line-cvec-cmat-nonzero
by simp
lift-deﬁnition poincare-line :: complex-homo⇒ complex-homo⇒ circline is poincare-line-hcoords-clmat
proof transfer
ﬁx za zb wa wb
assume za⁄= vec-zero zb⁄= vec-zero wa⁄= vec-zero wb⁄= vec-zero
assume za≈v zb wa ≈v wb
obtain za1 za2 zb1 zb2 wa1 wa2 wb1 wb2 where
∗: ( za1, za2 ) = za (zb1, zb2 ) = zb
(wa1, wa2 ) = wa (wb1, wb2 ) = wb
by (cases za, cases zb, cases wa, cases wb, auto)
obtain kz kw where
∗∗: kz⁄= 0 kw ⁄= 0 zb1 = kz∗ za1 zb2 = kz∗ za2 wb1 = kw∗ wa1 wb2 = kw∗ wa2
18
using ‹za≈v zb› ‹wa≈v wb›∗[symmetric]
by auto
let ?nom = λ z1 z2 w1 w2 . w1∗cnj w2∗(z1∗cnj z1 + z2∗cnj z2 )− z1∗cnj z2∗(w1∗cnj w1 + w2∗cnj w2 )
let ?den = λ z1 z2 w1 w2 . z1∗cnj z2∗cnj w1∗w2− w1∗cnj w2∗cnj z1∗z2
show circline-eq-cmat (poincare-line-cvec-cmat za wa )
(poincare-line-cvec-cmat zb wb )
proof−
have∃ k. k⁄= 0∧
poincare-line-cvec-cmat (zb1, zb2 ) ( wb1, wb2 ) = cor k ∗sm poincare-line-cvec-cmat (za1, za2 ) ( wa1, wa2 )
proof (cases ?den za1 za2 wa1 wa2 ⁄= 0 )
case True
hence ?den zb1 zb2 wb1 wb2 ⁄= 0
using∗∗
by (simp add : ﬁeld-simps)
let ?k = kz∗ cnj kz ∗ kw∗ cnj kw
have ?k⁄= 0
using∗∗
by simp
have is-real ?k
using eq-cnj-iﬀ-real[of ?k ]
by auto
have cor (Re ?k ) = ?k
using ‹is-real ?k ›
using complex-of-real-Re
by blast
have Re ?k ⁄= 0
using ‹?k⁄= 0 › ‹cor (Re ?k ) = ?k›
by (metis of-real-0 )
have arg1: Re (i∗ ?den zb1 zb2 wb1 wb2 ) = Re ?k ∗ Re (i∗ ?den za1 za2 wa1 wa2 )
apply (subst∗∗)+
apply (subst Re-mult-real[symmetric, OF ‹is-real ?k ›])
apply (rule arg-cong [where f =Re])
apply (simp add : ﬁeld-simps)
done
have arg2: i ∗ ?nom zb1 zb2 wb1 wb2 = ?k∗ i∗ ?nom za1 za2 wa1 wa2
using∗∗
by (simp add : ﬁeld-simps)
have mk-poincare-line-cmat (Re (i∗?den zb1 zb2 wb1 wb2 )) (i∗?nom zb1 zb2 wb1 wb2 ) =
cor (Re ?k )∗sm mk-poincare-line-cmat (Re (i∗?den za1 za2 wa1 wa2 )) (i∗?nom za1 za2 wa1 wa2 )
using ‹cor (Re ?k ) = ?k› ‹is-real ?k ›
apply (subst mk-poincare-line-cmat-scale)
apply (subst arg1, subst arg2 )
apply (subst ‹cor (Re ?k ) = ?k›)+
apply simp
done
thus ?thesis
using ‹?den za1 za2 wa1 wa2 ⁄= 0 › ‹?den zb1 zb2 wb1 wb2 ⁄= 0 ›
using ‹Re ?k ⁄= 0 › ‹cor (Re ?k ) = ?k›
by (rule-tac x =Re ?k in exI, simp)
next
case False
hence ?den zb1 zb2 wb1 wb2 = 0
using∗∗
by (simp add : ﬁeld-simps)
show ?thesis
proof (cases za1∗cnj za2 ⁄= 0 )
case True
hence zb1∗cnj zb2 ⁄= 0
19
using∗∗
by (simp add : ﬁeld-simps)
let ?k = kz∗ cnj kz
have ?k⁄= 0 is-real ?k
using∗∗
using eq-cnj-iﬀ-real[of ?k ]
by auto
thus ?thesis
using ‹za1∗ cnj za2 ⁄= 0 › ‹zb1∗ cnj zb2 ⁄= 0 ›
using ‹¬ (?den za1 za2 wa1 wa2 ⁄= 0 )› ‹?den zb1 zb2 wb1 wb2 = 0 ›∗∗
by (rule-tac x =Re (kz∗ cnj kz ) in exI, auto simp add : complex.expand)
next
case False
hence zb1∗ cnj zb2 = 0
using∗∗
by (simp add : ﬁeld-simps)
show ?thesis
proof (cases wa1 ∗ cnj wa2 ⁄= 0 )
case True
hence wb1∗cnj wb2 ⁄= 0
using∗∗
by (simp add : ﬁeld-simps)
let ?k = kw∗ cnj kw
have ?k⁄= 0 is-real ?k
using∗∗
using eq-cnj-iﬀ-real[of ?k ]
by auto
thus ?thesis
using ‹¬ (za1∗ cnj za2 ⁄= 0 )›
using ‹wa1∗ cnj wa2 ⁄= 0 › ‹wb1∗ cnj wb2 ⁄= 0 ›
using ‹¬ (?den za1 za2 wa1 wa2 ⁄= 0 )› ‹?den zb1 zb2 wb1 wb2 = 0 ›∗∗
by (rule-tac x =Re (kw∗ cnj kw ) in exI )
(auto simp add : complex.expand)
next
case False
hence wb1∗ cnj wb2 = 0
using∗∗
by (simp add : ﬁeld-simps)
thus ?thesis
using ‹¬ (za1∗ cnj za2 ⁄= 0 )› ‹zb1∗ cnj zb2 = 0 ›
using ‹¬ (wa1∗ cnj wa2 ⁄= 0 )› ‹wb1∗ cnj wb2 = 0 ›
using ‹¬ (?den za1 za2 wa1 wa2 ⁄= 0 )› ‹?den zb1 zb2 wb1 wb2 = 0 ›∗∗
by simp
qed
qed
qed
thus ?thesis
using∗[symmetric]
by simp
qed
qed
