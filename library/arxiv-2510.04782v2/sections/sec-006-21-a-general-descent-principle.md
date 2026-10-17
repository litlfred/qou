---
doc_id: arxiv-2510.04782v2
doc_title: "$q$-Hodge complexes over the Habiro ring"
section_id: sec-006-21-a-general-descent-principle
section_title: "A general descent principle"
section_number: 2.1
pages: 13-14
source_pdf: 2510.04782v2.pdf
source_sha256: 591d0bdf2c48d12f
toc_source: outline
doc_brief: "$q$-Hodge complexes over the Habiro ring — — Peter Scholze has raised the question whether some variant of the q-de Rham complex is already defined over the Habiro ring H := limm∈N Z[q]∧ (qm−1)."
---
To construct HR/A, we’ll first construct the completions (HR/A)∧
Φm(q) for all m ∈N and then
“glue them together” using a very general descent principle that we’ll explain in this subsection.
It will probably seem a little overkill for now, but we’ll use the same descent principle again in
§3.3 to construct the twisted q-de Rham complexes q9dR(m)
R/A.
2.1. Setup. — Let I be a site whose underlying category is a partially ordered set. Let D be
a presentable stable symmetric monoidal ∞-category. Suppose that for every Z ∈I we have a
full stable sub-∞-category DZ satisfying the following conditions:
(a)
The inclusion DZ ⊆D admits a left adjoint LZ : D ! DZ.
(b)
Whenever Z1 ! Z2 is a morphism in I, we have DZ1 ⊆DZ2. Note that LZ1 : DZ2 ! DZ1
is still a left adjoint of this inclusion.
(c)
For all x, y ∈D and all Z ∈I, the canonical morphism LZ(x ⊗y) ! LZ(LZ(x) ⊗y) is an
equivalence in D.
In this case, sending Z 7! DZ and (Z1 ! Z2) 7! (LZ1 : DZ2 ! DZ1) defines a contravariant
functor
D(−) : Iop −! CAlg(PrL
st)
into the ∞-category of presentable stable symmetric monoidal ∞-categories. Indeed, let’s
ignore the symmetric monoidal structure for the moment and let DI ⊆I × D be the full
sub-∞-category spanned fibrewise by DZ ⊆{Z} × D. By (b), DI ! I is still a cocartesian
fibration and so it defines a covariant functor D(−) : I ! Cat∞. By (a), this functor factors
through PrR
st. Using PrL
st ≃(PrR
st)op by [L-HTT, Corollary 5.5.3.4], we get the desired functor
D(−) : Iop ! PrL
st.
To incorporate the symmetric monoidal structure, let D be the ∞-operad D⊗associated to
the given symmetric monoidal structure on D. By (c) and [L-HA, Proposition 2.2.1.9], for all
Z ∈I, the inclusion of the full sub-∞-operad D⊗
Z ⊆D⊗spanned by DZ admits a symmetric
monoidal left adjoint L⊗
Z : D⊗! D⊗
Z which recovers LZ on underlying ∞-categories. Using this
observation, the same argument as above can be repeated with D replaced by D⊗.
2.2. Lemma. — In the situation of 2.1, assume that covers in I always have finite refinements
and that for any finite covering family {Zi ! Z}i=1,...,r, the functors LZi : DZ ! DZi are jointly
conservative. Then
D(−) : Iop −! CAlg(PrL
st)
is a sheaf on I. In particular, CAlg(D(−)): Iop ! PrL is a sheaf as well.
13
