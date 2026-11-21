---
doc_id: poincare-proof-outline
doc_title: "Formalization of the Poincare disc model of hyperbolic geometry"
section_id: sec-007-h-lines-and-inversion
section_title: "H-lines and inversion"
section_number: null
pages: 7-7
source_pdf: POINCARE-proof-outline.pdf
source_sha256: 8ac25ddb38d360b4
toc_source: outline
doc_brief: "Formalization of the Poincare disc model of hyperbolic geometry — We describe formalization of the Poincaré disc model of hyperbolic geometry within the Isabelle/HOL proof assistant."
---
Every h-line in the Poincaré model contains the inverse (wrt. the unit circle) of each of its points (note that at
most one of them belongs to the unit disc).

lemma is-poincare-line-inverse-point:
assumes is-poincare-line H u € circline-set H
shows inversion u € circline-set H
using assms
unfolding is-poincare-line-iff circline-set-def perpendicular-def inversion-def

apply simp
proof (transfer, transfer)
fix u H
assume hh: hermitean H A H # mat-zero u # vec-zero and
aa: circline-type-cmat H = — 1 \ cos-angle-cmat (of-circline-cmat H) unit-circle-cmat = 0 on-circline-cmat-cvec
Hu

obtain A BC D ul u2 where «: H = (A, B, C, D) u = (ul, u2)
by (cases H, cases u, auto)
have is-real A is-real D C = cnj B
using * hh hermitean-elems
by auto
moreover
have A = D
using aa(1) * <is-real A» <is-real Dy
by (auto simp del: pos-oriented-cmat-def simp add: complex.expand split: if-split-asm)
thus on-circline-cmat-cvec H (conjugate-cvec (reciprocal-cvec u))
using aa(2) *
by (simp add: vec-cnj-def field-simps)
qed

Every h-line in the Poincaré model and is invariant under unit circle inversion.

lemma circline-inversion-poincare-line:
assumes is-poincare-line H
shows circline-inversion H = H
proof—
obtain uv w where *:uZAvv4wuF w {u, v, w} C circline-set H
using assms is-poincare-line-iff [of H]
using circline-type-neg-card-gt3|of H|
by auto
hence {inversion u, inversion v, inversion w} C circline-set (circline-inversion H)
{inversion u, inversion v, inversion w} C circline-set H
using is-poincare-line-inverse-point|OF assms|
by auto
thus ?thesis
using * unique-circline-set[of inversion u inversion v inversion w]
by (metis insert-subset inversion-involution)
qed
