---
doc_id: poincare-proof-outline
doc_title: "Formalization of the Poincare disc model of hyperbolic geometry"
section_id: sec-013-construction-of-the-h-line-between-the-two-given
section_title: "Construction of the h-line between the two given points"
section_number: null
pages: 17-20
source_pdf: POINCARE-proof-outline.pdf
source_sha256: 8ac25ddb38d360b4
toc_source: outline
doc_brief: "Formalization of the Poincare disc model of hyperbolic geometry — We describe formalization of the Poincaré disc model of hyperbolic geometry within the Isabelle/HOL proof assistant."
---
Next we show how to construct the (unique) h-line between the two given points in the Poincaré model

Geometrically, h-line can be constructed by finding the inverse point of one of the two points and by constructing
the circle (or line) trough it and the two given points.

Algebraically, for two given points u and v in C, the h-line matrix coefficients can be A = i- (uv — vu) and
B=i- (v(\ul? +1) — u(\v|? + 1)).

We need to extend this to homogenous coordinates. There are several degenerate cases.

- If {z,w} = {0),, co),} then there is no unique h-line (any line trough zero is an h-line).

- If z and w are mutually inverse, then the construction fails (both geometric and algebraic).

- If z and w are different points on the unit circle, then the standard construction fails (only geometric).

- None of this problematic cases occur when z and w are inside the unit disc.

We express the construction algebraically, and construct the Hermitean circline matrix for the two points given
in homogenous coordinates. It works correctly in all cases except when the two points are the same or are
mutually inverse.

definition mk-poincare-line-cmat :: real = complex = complex-mat where
[simp]: mk-poincare-line-cmat A B = (cor A, B, cnj B, cor A)

lemma mk-poincare-line-cmat-zero-iff:
mk-poincare-line-cmat A B = mat-zero<—+ A= 0A B=0
by auto

lemma mk-poincare-line-cmat-hermitean
[simp]: hermitean (mk-poincare-line-cmat A B)
by simp

lemma mk-poincare-line-cmat-scale:
cor k *sm mk-poincare-line-cmat A B = mk-poincare-line-cmat (k * A) (k * B)
by simp

definition poincare-line-cvec-cmat :: complex-vec => complex-vec = complez-mat where

[simp]: poincare-line-cvec-cmat zw =
(let (21, 22) = 2;

17
(wl, w2) = w;
nom = wlxcnj w2*(zl*cnj 21 + 22«cnj 22) — z1*cnj z2*(wl*cnj wl + w2xcnj w2);
den = z1*cnj z2xcnj wl*xw2 — wlxcnj w2*cnj z1*z2
in if den 0 then
mk-poincare-line-cmat (Re(ixden)) (ixnom)
else if z1xcnj 22 # 0 then
mk-poincare-line-cmat 0 (i*z1*cnj z2)
else if wl*xcnj w2 # 0 then
mk-poincare-line-cmat 0 (i*w1*cnj w2)
else
mk-poincare-line-cmat 0 i)

lemma poincare-line-cvec-cmat-AeqD:
assumes poincare-line-cvec-cmat z w = (A, B, C, D)
shows A = D
using assms
by (cases z, cases w) (auto split: if-split-asm)

lemma poincare-line-cvec-cmat-hermitean [simp]:
shows hermitean (poincare-line-cvec-cmat z w)
by (cases z, cases w) (auto split: if-split-asm simp del: mk-poincare-line-cmat-def)

lemma poincare-line-cvec-cmat-nonzero [simp]:
assumes z # vec-zero w # vec-zero
shows poincare-line-cvec-cmat z w # mat-zero
proof—

obtain z1 22 wl w2 where *: z = (21, 22) w = (wl, w2)
by (cases z, cases w, auto)

let ?den = z1xcnj z2*cnj wl*w2 — wlxcnj w2*cnj z1*22
show ?thesis
proof (cases ?den # 0)
case True
have is-real (i « ?den)
using eq-cnj-iff-reallof i * ?den]
by (simp add: field-simps)
hence Re (i x ?den) 4 0
using <?den # 0>
by (metis complex-i-not-zero complex-surj mult-eq-0-iff zero-complex. code)
thus ?thesis
using * «?den # 0»
by (simp del: mk-poincare-line-cmat-def mat-zero-def add: mk-poincare-line-cmat-zero-iff )
next
case False
thus ?thesis
using *
by (simp del: mk-poincare-line-cmat-def mat-zero-def add: mk-poincare-line-cmat-zero-iff )
qed
qed

lift-definition poincare-line-hcoords-clmat :: complex-homo-coords = complex-homo-coords => circline-mat is poincare-line-cvec-cmat
using poincare-line-cvec-cmat-hermitean poincare-line-cvec-cmat-nonzero
by simp

lift-definition poincare-line :: complex-homo = complez-homo => circline is poincare-line-hcoords-clmat
proof transfer
fix za zb wa wb
assume za # vec-zero zb # vec-zero wa # vec-zero wh # vec-zero
assume 2a ®y 2b wa %v wh
obtain zal za2 zb1 zb2 wal wa2 whl wb2 where
*: (zal, 2a2) = za (zb1, 2b2) = 2b
(wal, wa2) = wa (wb1, wb2) = wb
by (cases za, cases zb, cases wa, cases wb, auto)
obtain kz kw where
xxi kz A Okw # 0 2b1 = kz * zal 2b2 = kz * za2 whl = kw * wal wb2 = kw * wa2

18
using (za %y zb> (wa %y wh» *[symmetric]
by auto

let ?nom = X 21 22 wl w2. wlxcnj w2*(z1*cnj zl + 22*cnj 22) — z1*enj z2*(wl*cnj wl + w2xcnj w2)
let ?den = X 21 22 wl w2. z1*cnj 22*cnj wl*w2 — wl*cnj w2xcnj z1*22

show circline-eq-cmat (poincare-line-cvec-cmat za wa)
(poincare-line-cvec-cmat zb wb)
proof—
have Jk. kA 0A
poincare-line-cvec-cmat (zb1, 2b2) (wb1, wb2) = cor k *sm poincare-line-cvec-cmat (zal, za2) (wal, wa2)
proof (cases ?den zal za2 wal wa2 # 0)
case True
hence ?den zb1 zb2 wbh1 wh2 4 0
using **
by (simp add: field-simps)

let ?k = kz * cnj kz * kw * cnj kw

have ?k 4 0
using **
by simp

have is-real ?k
using eq-cnj-iff-real[of ?k]
by auto

have cor (Re ’k) = ?k
using <is-real ?k»
using complex-of-real-Re
by blast

have Re ?k #4 0
using <?k # 0» «cor (Re ?k) = ?k»
by (metis of-real-0)

have arg1: Re (i « ?den zb1 zb2 wb1 wb2) = Re ?k * Re (i * ?den zal za2 wal wa2)
apply (subst **)+
apply (subst Re-mult-real[symmetric, OF <is-real ?k»])
apply (rule arg-cong[where f=Re])
apply (simp add: field-simps)
done
have arg2: i * ?nom zb1 zb2 wb1 wb2 = ?k * i * ?nom zal za2 wal wa2
using **
by (simp add: field-simps)
have mk-poincare-line-cmat (Re (ix ?den zb1 zb2 whl wh2)) (ix?nom zb1 z2b2 wb1 wb2) =
cor (Re ?k) *sm mk-poincare-line-cmat (Re (ix ?den zal za2 wal wa2)) (ix?nom zal za2 wal wa2)
using <cor (Re ?k) = ?k» <is-real ?k»
apply (subst mk-poincare-line-cmat-scale)
apply (subst arg1, subst arg2)
apply (subst «cor (Re ?k) = ?k»)+
apply simp
done
thus ?thesis
using <?den zal za2 wal wa2 # 0» «?den zb1 zb2 wbh1 wh2 ¥ 0»
using (Re ?k 4 0) (cor (Re ?k) = ?k»
by (rule-tac c=Re ?k in exl, simp)
next
case False
hence ?den zb1 zb2 wbh1 wh2 = 0
using **
by (simp add: field-simps)
show ?thesis
proof (cases zal*cnj za2 # 0)
case True
hence zb1*cnj zb2 4 0

19
using **
by (simp add: field-simps)

let ?k = kz * cnj kz

have ?k # 0 is-real ?k
using **
using eq-cnj-iff-reallof ?k|
by auto
thus ?thesis
using (zal * cnj za2 # 0) <zb1 * cnj zb2 F 0»
using (7 (?den zal za2 wal wa2 4 0)» <?den zb1 zb2 whl wh2 = 0» **
by (rule-tac c=Re (kz * cnj kz) in exI, auto simp add: complex.expand)
next
case False
hence zb1 * cnj zb2 = 0
using **
by (simp add: field-simps)
show ?thesis
proof (cases wal * cnj wa2 # 0)
case True
hence wh1«cnj wb2 4 0
using **

by (simp add: field-simps)
let ?k = kw * cnj kw

have ?k # 0 is-real ?k
using **
using eq-cnj-iff-reallof ?k]
by auto

thus ?thesis
using (> (zal * cnj za2 # 0)»
using (wal * cnj wa2 # 0» «whl * cnj wh2 4 0»
using (- (?den zal za2 wal wa2 # 0)» «?den zb1 zb2 wbh1 wh2 = 0) **
by (rule-tac c=Re (kw * cnj kw) in ex!)
(auto simp add: complex.expand)
next
case False
hence wh1 * cnj wb2 = 0
using **
by (simp add: field-simps)
thus ?thesis
using (7 (zal * cnj za2 4 0)» <zb1 * cnj zb2 = 0»
using (7 (wal * cnj wa2 # 0)» «whl * cnj wb2 = 0»
using (- (?den zal za2 wal wa2 # 0)» «?den zb1 zb2 wbh1 wh2 = 0) **
by simp
qed
qed
qed
thus ?thesis
using *[symmetric]
by simp
qed
qed
