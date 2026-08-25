---
doc_id: poincare-proof-outline
doc_title: "Formalization of the Poincare disc model of hyperbolic geometry"
section_id: sec-006-h-lines-and-inversion
section_title: "H-lines and inversion"
section_number: null
pages: 7-8
source_pdf: POINCARE-proof-outline.pdf
source_sha256: 8ac25ddb38d360b4
doc_brief: "Formalization of the Poincare disc model of hyperbolic geometry — We describe formalization of the Poincaré disc model of hyperbolic geometry within the Isabelle/HOL proof assistant."
---
Every h-line in the Poincaré model contains the inverse (wrt. the unit circle) of each of its points (note that at
most one of them belongs to the unit disc).
lemma is-poincare-line-inverse-point:
assumes is-poincare-line H u ∈ circline-set H
shows inversion u ∈ circline-set H
using assms
unfolding is-poincare-line-iﬀ circline-set-def perpendicular-def inversion-def
apply simp
proof (transfer, transfer)
ﬁx u H
assume hh: hermitean H ∧ H⁄= mat-zero u ⁄= vec-zero and
aa: circline-type-cmat H =− 1∧ cos-angle-cmat (of-circline-cmat H ) unit-circle-cmat = 0 on-circline-cmat-cvec
H u
obtain A B C D u1 u2 where∗: H = ( A, B, C, D) u = ( u1, u2 )
by (cases H, cases u, auto)
have is-real A is-real D C = cnj B
using∗ hh hermitean-elems
by auto
moreover
have A = D
using aa(1 )∗ ‹is-real A› ‹is-real D ›
by (auto simp del : pos-oriented-cmat-def simp add : complex.expand split : if-split-asm)
thus on-circline-cmat-cvec H (conjugate-cvec (reciprocal-cvec u))
using aa(2 )∗
by (simp add : vec-cnj-def ﬁeld-simps )
qed
Every h-line in the Poincaré model and is invariant under unit circle inversion.
lemma circline-inversion-poincare-line:
assumes is-poincare-line H
shows circline-inversion H = H
proof−
obtain u v w where∗: u⁄= v v ⁄= w u ⁄= w{u, v, w}⊆ circline-set H
using assms is-poincare-line-iﬀ [of H ]
using circline-type-neg-card-gt3[of H ]
by auto
hence{inversion u, inversion v, inversion w}⊆ circline-set (circline-inversion H )
{inversion u, inversion v, inversion w}⊆ circline-set H
using is-poincare-line-inverse-point[OF assms ]
by auto
thus ?thesis
using∗ unique-circline-set[of inversion u inversion v inversion w ]
by (metis insert-subset inversion-involution )
qed
4.1.3 Classiﬁcation of h-lines into Euclidean segments and circles
If an h-line contains zero, than it also contains inﬁnity (the inverse point of zero) and is by deﬁnition an
Euclidean line.
lemma is-poincare-line-trough-zero-trough-infty [simp]:
assumes is-poincare-line l and 0 h∈ circline-set l
shows∞h∈ circline-set l
using is-poincare-line-inverse-point[OF assms ]
by simp
lemma is-poincare-line-trough-zero-is-line:
7
assumes is-poincare-line l and 0 h∈ circline-set l
shows is-line l
using assms
using inf-in-circline-set is-poincare-line-trough-zero-trough-infty
by blast
If an h-line does not contain zero, than it also does not contain inﬁnity (the inverse point of zero) and is by
deﬁnition an Euclidean circle.
lemma is-poincare-line-not-trough-zero-not-trough-infty [simp]:
assumes is-poincare-line l
assumes 0 h /∈ circline-set l
shows∞h /∈ circline-set l
using assms
using is-poincare-line-inverse-point[OF assms (1 ), of ∞h]
by auto
lemma is-poincare-line-not-trough-zero-is-circle:
assumes is-poincare-line l 0 h /∈ circline-set l
shows is-circle l
using assms
using inf-in-circline-set is-poincare-line-not-trough-zero-not-trough-infty
by auto
