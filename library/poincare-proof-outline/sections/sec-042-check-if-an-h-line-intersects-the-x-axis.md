---
doc_id: poincare-proof-outline
doc_title: "Formalization of the Poincare disc model of hyperbolic geometry"
section_id: sec-042-check-if-an-h-line-intersects-the-x-axis
section_title: "Check if an h-line intersects the x-axis"
section_number: null
pages: 97-100
source_pdf: POINCARE-proof-outline.pdf
source_sha256: 8ac25ddb38d360b4
toc_source: outline
doc_brief: "Formalization of the Poincare disc model of hyperbolic geometry — We describe formalization of the Poincaré disc model of hyperbolic geometry within the Isabelle/HOL proof assistant."
---
lemma z-azis-intersection-equation:
assumes
H = mk-circline A B C D and
(A, B, C, D) € hermitean-nonzero
shows of-complex z € circline-set x-axis M circline-set H <—+
Axz? + 2xRe Bez + D = 0 A is-real z (is ?lhs <> ?rhs)
proof—
have ?lhs <> Axz* + (B+ cnj B)xzx + D=0 A z= cnjz
using assms
using circline-equation-x-axis| of z]
using circline-cquation|of H A B C D z|
using hermitean-elems
by (auto simp add: power2-eq-square field-simps)
thus ?thesis
using eq-cnj-iff-reallof 2]
using hermitean-elems|of A B C D|
by (simp add: complex-add-cnj complex-eq-if-Re-eq)
qed

Check if an h-line intersects x-axis within the unit disc - this could be generalized to checking if an arbitrary

97
circline intersects the x-axis, but we do not need that.

definition intersects-a-axis-cmat :: complex-mat = bool where
[simp]: intersects-x-axis-cmat H = (let (A, B, C, D) = H in A= 0 V (Re B)? > (Re A)?)

lift-definition intersects-2-axis-clmat :: circline-mat = bool is intersects-x-axis-cmat
done

lift-definition intersects-x-azis :: circline = bool is intersects-x-axis-clmat
proof (transfer)
fix H1 H2
assume hh: hermitean H1 A H1 4 mat-zero and hermitean H2 \ H2 4 mat-zero
obtain Ai B1 C1 D1 A2 B2 C2 D2 where *: H1 = (A1, B1, C1, D1) H2 = (A2, B2, C2, D2)
by (cases H1, cases H2, auto)
assume circline-eq-cmat H1 H2
then obtain k where k: k 4 0 \ H2 = cork *sm H1
by auto
show intersects-z-azis-cmat H1 = intersects-x-axis-cmat H2
proof —
have k #4 0 => (Re Al)? < (Re B1)? <-> (k * Re A1)? < (k * Re B1)?
by (smt mult-strict-left-mono power2-eq-square semiring-normalization-rules(13) zero-less-power2)
thus ?thesis
using * k
by auto
qed
qed

lemma intersects-x-axis-mk-circline:
assumes is-real Aand A#0V B40
shows intersects-x-axis (mk-circline A B (cnj B) A) + A= 0 V (Re B)? > (Re A)?
proof—
let ?H = (A, B, (cnj B), A)
have hermitean ?H
using <is-real A»
unfolding hermitean-def mat-adj-def mat-cnj-def
using eq-cnj-iff-real
by auto
moreover
have ?H 4 mat-zero
using assms
by auto
ultimately
show ?thesis
by (transfer, transfer, auto simp add: Let-def)
qed

lemma intersects-x-axis-iff :
assumes is-poincare-line H
shows (3 x € unit-disc. x € circline-set H / circline-set x-axis) > intersects-x-axis H
proof—
obtain Ac B C Dc where *: H = mk-circline Ac B C Dc hermitean (Ac, B, C, Dc) (Ac, B, C, De) # mat-zero
using ex-mk-circline|of H]
by auto
hence (cmod B)? > (emod Ac)? Ac = De
using assms
using is-poincare-line-mk-circline
by auto

hence H = mk-circline (Re Ac) B (cnj B) (Re Ac) hermitean (cor (Re Ac), B, (cnj B), cor (Re Ac)) (cor (Re Ac),
B, (cnj B), cor (Re Ac)) # mat-zero
using hermitean-elems|of Ac B C Dc] *
by auto
then obtain A where
*: H = mk-circline (cor A) B (cnj B) (cor A) (cor A, B, (cnj B), cor A) € hermitean-nonzero
by auto

show ?thesis

98
proof (cases A = 0)
case True
thus ?thesis
using *
using 2-axis-intersection-equation[OF *(1—2), of 0]
using intersects-z-axis-mk-circline|of cor A B|
by auto
next
case False
show ?thesis
proof
assume J x € unit-disc. x € circline-set H 1 circline-set x-axis
then obtain x where *+: of-complex x € unit-disc of-complex x € circline-set H 1 circline-set x-axis
by (metis inf-or-of-complex inf-notin-unit-disc)
hence is-real ©
unfolding circline-set-x-azxis
using of-complez-inj

by auto

hence eq: A * (Rez)? + 2* Re Bx Rex+A=0
using **
using 2-azis-intersection-equation[OF *(1—2), of Re ]
by simp

hence (2 * Re B)? —4*AxA>0O
using discriminant-iff[of A - 2 * Re B A|
using discrim-def[of A 2 « Re B A] False
by auto
hence (Re B)? > (Re A)?
by (simp add: power2-eq-square)
moreover
have (Re B)? #4 (Re A)?
proof (rule ccontr)
assume 7— ?thesis
hence Re B = Re AV Re B=— Re A
using power2-eq-iff by blast
hence A * (Rex)? + Ax 2x Rex+A=O0VAx (Rex)? —Ax2*Rex+A=0
using eq
by auto
hence A * ((Re xz)? + 2* Rex + 1)=0V Ax ((Rea)? — 2% Rexr+1)=0
by (simp add: field-simps)
hence (Rez)? + 2* Rea+1=0V (Rez)? —-2*Rexr+1=0
using <A # 0>
by simp
hence (Re x + 1)? = 0 V (Rex — 1)? =0
by (simp add: power2-sum power2-diff field-simps)
hence Rex = —1 V Rex=1
by auto
thus False
using <is-real x) <of-complex x € unit-discy
by (auto simp add: cmod-eq-Re)
qed
ultimately
show intersects-1-axis H
using intersects-z-axis-mk-circline
using *
by auto
next
assume intersects-x-axis H
hence (Re B)? > (Re A)?
using * False
using intersects-z-axis-mk-circline
by simp
hence discr: (2 * Re B)?? — 4% A*A>0O
by (simp add: power2-eq-square)
then obtain «1 +2 where
eqs: Ax cl? + 2% ReBxal+A=O0A*%22°?4+ 2% REBx224+A=O021 £22
using discriminant-pos-ex[OF (A # 0», of 2 * Re B A|

99
using discrim-def[of A 2 « Re B A]
by auto

hence z1 * 72 = 1
using viette2(OF «A # 0), of 2 * Re BA x1 x2] discr ‘A # 0>
by auto

have abs 11 # 1 abs x2 # 1
using eqs discr (x1 * 2 = 1)
by (auto simp add: abs-if power2-eq-square)

hence abs t1 < 1 V abs 72 < 1
using (z/ * 22 = 1)
by (smt mult-le-cancel-left1 mult-minus-right)

thus dz € unit-disc. x € circline-set H 1 circline-set x-axis
using 2-azis-intersection-equation[OF *(1—2), of x1]
using 2-azis-intersection-equation[OF *(1—2), of x2]
using eqs
by auto

qed
qed
qed
