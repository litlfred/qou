---
doc_id: poincare-proof-outline
doc_title: "Formalization of the Poincare disc model of hyperbolic geometry"
section_id: sec-044-intersection-point-of-a-poincaré-line-with-the-x
section_title: "Intersection point of a Poincaré line with the x-axis in the unit disc"
section_number: null
pages: 101-105
source_pdf: POINCARE-proof-outline.pdf
source_sha256: 8ac25ddb38d360b4
toc_source: outline
doc_brief: "Formalization of the Poincare disc model of hyperbolic geometry — We describe formalization of the Poincaré disc model of hyperbolic geometry within the Isabelle/HOL proof assistant."
---
definition calc-z-axis-intersection-cvec :: complex = complex = compler-vec where
[simp]: calc-x-axis-intersection-cvec A B =
(let diser = (Re B)? — (Re A)? in
(—Re(B) + sgn (Re B) * sqrt(discr), A))

definition calc-x-azis-intersection-cmat-cvec :: complex-mat = complex-vec where [simp]:
calc-z-axis-intersection-cmat-cvec H =
(let (A, B, C, D) = H in
if A # 0 then
calc-x-axis-intersection-cvec A B
else
(0, 1)
)

lift-definition calc-x-axis-intersection-clmat-hcoords :: circline-mat = complex-homo-coords is calc-z-axis-intersection-cmat-cvec
by (auto split: if-split-asm)

lift-definition calc-x-axis-intersection :: circline = complez-homo is calc-x-axis-intersection-clmat-hcoords
proof transfer
fix H1 H2
assume *: hermitean H1 \ H1 # mat-zero hermitean H2 \ H2 # mat-zero
obtain Ai B1 C1 D1 A2 B2 C2 D2 where hh: H1 = (A1, B1, C1, D1) H2 = (A2, B2, C2, D2)
by (cases H1, cases H2, auto)
assume circline-eq-cmat H1 H2
then obtain k where k: k 4 0 H2 = cork *sm H1
by auto

have calc-2-axis-intersection-cvec Al B1 %» calc-a-axis-intersection-cvec A2 B2
using hh k
apply simp
apply (rule-tac c=cor k in ex!)
apply auto
apply (simp add: sgn-mult power-mult-distrib)
apply (subst right-diff-distrib| symmetric])
apply (subst real-sqrt-mult)

101
by (simp add: real-sgn-eq right-diff-distrib)

thus calc-x-axis-intersection-cmat-cvec H1 ~v
calc-z-axis-intersection-cmat-cvec H2
using hh k
by (auto simp del: calc-x-axis-intersection-cvec-def )
qed

lemma calc-2-azis-intersection-in-unit-disc:
assumes is-poincare-line H intersects-x-aris H
shows calc-a-axis-intersection H € unit-disc
proof (cases is-line H)
case True
thus ?thesis
using assms
unfolding unit-disc-def disc-def
by simp (transfer, transfer, auto simp add: vec-cnj-def)
next
case False
thus ?thesis
using assms
unfolding unit-disc-def disc-def
proof (simp, transfer, transfer)
fix H
assume hh: hermitean H \ H # mat-zero
then obtain A B D where *: H = (A, B, cnj B, D) is-real A is-real D
using hermitean-elems
by (cases H) blast
assume is-poincare-line-cmat H
hence *: H = (A, B, cnj B, A) is-real A
using *
by auto

assume 7— circline-A0-cmat H
hence A 4 0

using *

by simp

assume intersects-1-axis-cmat H
hence (Re B)? > (Re A)?
using * (A #4 0»
by (auto simp add: power2-eq-square complex.expand)

hence Re B 4 0
by auto

have Re A # 0
using <is-real Ay «A # 0»
by (auto simp add: complex.expand)

have sqrt((Re B)? — (Re A)*) < sqrt((Re B)?)
using «Re A # 0
by (subst real-sqrt-less-iff) auto

also have ... = sgn (Re B) « (Re B)
by (smt mult-minus-right nonzero-eq-divide-eq real-sgn-eq real-sqrt-abs)
finally

have 1: sqrt((Re B)? — (Re A)*) < sgn (Re B) * (Re B)

have 2: (Re B)? — (Re A)? < sgn (Re B) * (Re B) * sqrt((Re B)? — (Re A)?)
using «(Re B)? > (Re A)?»
using mult-strict-right-mono|OF 1, of sqrt ((Re B)? — (Re A)*)]
by simp

have 3: (Re B)? — 2xsgn (Re B)*Re Bxsqrt((Re B)*? — (Re A)”) + (Re B)? — (Re A)? < (Re A)?

102
using mult-strict-left-mono|OF 2, of 2]
by (simp add: field-simps)

have (sgn (Re B))? = 1
using ‘(Re B # 0
by (simp add: sgn-if)

hence (—Re B + sgn (Re B) * sqrt((Re B)? — (Re A)))? < (Re A)?
using «(Re B)? > (Re A)*) 3
by (simp add: power2-diff field-simps)

thus in-ocircline-cmat-cvec unit-circle-cmat (calc-z-axis-intersection-cmat-cvec H)
using « <(Re B)? > (Re A)»
by (auto simp add: vec-cnj-def power2-eq-square split: if-split-asm)
qed
qed

lemma calc-2-azis-intersection:
assumes is-poincare-line H and intersects-x-axis H
shows calc-a-axis-intersection H € circline-set H \ circline-set x-axis
proof (cases is-line H)
case True
thus ?thesis
using assms
unfolding circline-set-def
by simp (transfer, transfer, auto simp add: vec-cnj-def)
next
case False
thus ?thesis
using assms
unfolding circline-set-def
proof (simp, transfer, transfer)
fix H
assume hh: hermitean H \ H # mat-zero
then obtain A B D where *: H = (A, B, cnj B, D) is-real A is-real D
using hermitean-elems
by (cases H) blast
assume is-poincare-line-cmat H
hence *: H = (A, B, cnj B, A) is-real A
using *
by auto
assume 7— circline-A0-cmat H
hence A 4 0
using *
by auto

assume intersects-1-axis-cmat H
hence (Re B)? > (Re A)?
using * (A #4 0»
by (auto simp add: power2-eq-square complex.expand)

hence Re B 4 0
by auto

show on-circline-cmat-cvec H (calc-a-axis-intersection-cmat-cvec H) A
on-circline-cmat-cvec x-axis-cmat (calc-1-axis-intersection-cmat-cvec H) (is ?P1 A ?P2)
proof
show on-circline-cmat-cvec H (calc-x-axis-intersection-cmat-cvec H)
proof (cases circline-A0-cmat H)
case True
thus ?thesis
using * <is-poincare-line-cmat H) <intersects-x-axis-cmat H»
by (simp add: vec-cnj-def)
next
case False

103
let ?x = calc-2-axis-intersection-cvec A B
let ?nom = fst ?z and ?den = snd ?x
have x: ?z = (?nom, ?den)

by simp

hence on-circline-cmat-cvec H (calc-x-axis-intersection-cvec A B)
proof (subst *, subst x, subst on-circline-cmat-cvec-circline-equation)
have (sgn(Re B))? = 1
using (Re B # 0) sgn-pos zero-less-power2 by fastforce
have (sgrt((Re B)? — (Re A)”))? = (Re B)? — (Re A)?
using «(Re B)? > (Re A)?»
by simp

have (—(Re B) + sgn(Re B)xsqrt((Re B)? — (Re A)*)
(—(Re B))? + (sgn(Re B)*sqrt((Re B)? — (Re A)
by (simp add: power2-diff)
( By have ... = (Re B)*(Re B) + (sgn(Re B)«sqrt((Re B)? — (Re A)?))? — 2«(Re B)*sgn(Re B)xsqrt((Re B)?
— (Re A)?
by (simp add: power2-eq-square)
also have ... = (Re B)*(Re B) + (sgn(Re B))?*(sqrt((Re B)? — (Re A)?))? — 2(Re B)xsgn(Re B)xsqrt((Re
B)? — (Re A)?)
by (simp add: power-mult-distrib)
also have ... = (Re B)*(Re B) + (Re B)? — (Re A)? — 2x(Re B)xsgn(Re B)xsqrt((Re B)? — (Re A)?)
using <(sgrt((Re B)? — (Re A)?))? = (Re B)? — (Re A)» «(sgn(Re B))? = 1»
by simp
finally have (—(Re B) + sgn(Re B)«sqrt((Re B)? — (Re A)?))? =
(Re B)*(Re B) + (Re B)? — (Re A)? — 2x(Re B)xsgn(Re B)*sqrt((Re B)? — (Re A)?)
by simp

P=
?))? — 2x(Re B)*sgn(Re B)*sqrt((Re B)? — (Re A)*)

have is-real ?nom is-real ?den
using <is-real A»
by simp+
hence cnj (?nom) = ?nom cnj (?den) = ?den
by (simp add: eq-cnj-iff-real) +
hence Ax ?nomx(cnj (2nom)) + Bx ?denx(enj (?nom)) + (cnj B)*(enj (?den))* ?nom + Ax?denx(cnj (?den))
= Ax?nomx ?nom + Bx ?denx?nom + (cnj B)* ?denx?nom + Ax ?denx ?den

by auto

also have ... = A*?nom*?nom + (B + (enj B))*?denx ?nom + Ax ?denx ?den
by (simp add:field-simps)

also have ... = Ax?nom*?nom + 2*(Re B)*?den*?nom + Ax ?denx ?den
by (simp add:complez-add-cnj)

also have ... = Ax?nom? + 2«(Re B)*?den*?nom + Ax?denx?den

by (simp add:power2-eq-square)

also have ... = Ax(—(Re B) + sgn(Re B)xsqrt((Re B)? — (Re A)?))?

+ 2x(Re B)xAx(—(Re B) + sgn(Re B)*sqrt((Re B)? — (Re A)*)) + AxAxA

unfolding calc-x-azxis-intersection-cvec-def
by auto

also have ... = Ax((Re B)*(Re B) + (Re B)? — (Re A)? — 2x(Re B)xsgn(Re B)xsqrt((Re B)? — (Re A)?))

+ 2x(Re B)xAx(—(Re B) + sgn(Re B)xsqrt((Re B)? — (Re A)?)) + AxAxA
using «(—(Re B) + sgn(Re B)*sqrt((Re B)? — (Re A)*))? =
(Re B)*(Re B) + (Re B)? — (Re A)? — 2«(Re B)*sgn(Re B)*sqrt((Re B)? — (Re A)?)>

by simp

also have ... = Ax((Re B)*(Re B) + (Re B)? — A? — 2x(Re B)xsgn(Re B)xsgrt((Re B)? — (Re A)?))

+ 2x(Re B)xAx(—(Re B) + sgn(Re B)xsqrt((Re B)? — (Re A)?)) + AxAxA

using <is-real A»
by simp

also have ... = 0
apply (simp add:field-simps)
by (simp add: power2-eq-square)

finally have Ax?nomx(cnj (?nom)) + Bx ?denx(cnj (?nom)) + (enj B)*(enj (?den))*?nom + Ax?denx(cnj

(?den)) = 0

by simp

thus circline-equation A B (cnj B) A ?nom ?den
by simp

qed
thus ?thesis

104
using * <is-poincare-line-cmat H) <intersects-x-axis-cmat H»
by (simp add: vec-cnj-def)
qed
next
show on-circline-cmat-cvec x-axis-cmat (calc-x-axis-intersection-cmat-cvec H)
using * <is-poincare-line-cmat H»> ‘intersects-x-axis-cmat H» <is-real Ay
using eq-cnj-iff-real[of A]
by (simp add: vec-cnj-def)
qed
qed
qed

lemma unique-calc-x-axis-intersection:
assumes is-poincare-line H and H # s-azis
assumes «x € unit-disc and « € circline-set H ™ circline-set z-axis
shows x = calc-x-axis-intersection H
proof—
have *: intersects-z-aris H
using assms
using intersects-x-avis-iff|OF assms(1)]
by auto
show «x = calc-z-axis-intersection H
using calc-x-axis-intersection|OF assms(1) *]
using calc-x-axis-intersection-in-unit-disc|OF assms(1) *]
using assms
using unique-is-poincare-line|of x calc-z-axis-intersection H H x-axis]
by auto
qed
