---
doc_id: poincare-proof-outline
doc_title: "Poincaré Disc Model"
section_id: sec-007-h-lines-and-inversion
section_title: "H-lines and inversion"
section_number: null
pages: 7-7
source_pdf: POINCARE-proof-outline.pdf
source_sha256: 8ac25ddb38d360b4
toc_source: outline
---
Every h-line in the Poincaré model contains the inverse (wrt. the unit circle) of each of its points (note that at
most one of them belongs to the unit disc).
lemma is-poincare-line-inverse-point:
assumes is-poincare-line H u ∈circline-set H
shows inversion u ∈circline-set H
using assms
unfolding is-poincare-line-iﬀcircline-set-def perpendicular-def inversion-def
apply simp
proof (transfer, transfer)
ﬁx u H
assume hh: hermitean H ∧H̸ = mat-zero u̸ = vec-zero and
aa: circline-type-cmat H = −1 ∧cos-angle-cmat (of-circline-cmat H) unit-circle-cmat = 0 on-circline-cmat-cvec
H u
obtain A B C D u1 u2 where ∗: H = (A, B, C, D) u = (u1, u2)
by (cases H, cases u, auto)
have is-real A is-real D C = cnj B
using ∗hh hermitean-elems
by auto
moreover
have A = D
using aa(1) ∗‹is-real A› ‹is-real D›
by (auto simp del: pos-oriented-cmat-def simp add: complex.expand split: if-split-asm)
thus on-circline-cmat-cvec H (conjugate-cvec (reciprocal-cvec u))
using aa(2) ∗
by (simp add: vec-cnj-def ﬁeld-simps)
qed
Every h-line in the Poincaré model and is invariant under unit circle inversion.
lemma circline-inversion-poincare-line:
assumes is-poincare-line H
shows circline-inversion H = H
proof−
obtain u v w where ∗: u̸ = v v̸ = w u̸ = w {u, v, w} ⊆circline-set H
using assms is-poincare-line-iﬀ[of H]
using circline-type-neg-card-gt3[of H]
by auto
hence {inversion u, inversion v, inversion w} ⊆circline-set (circline-inversion H)
{inversion u, inversion v, inversion w} ⊆circline-set H
using is-poincare-line-inverse-point[OF assms]
by auto
thus ?thesis
using ∗unique-circline-set[of inversion u inversion v inversion w]
by (metis insert-subset inversion-involution)
qed
4.1.3
