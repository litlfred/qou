---
doc_id: arxiv-2510.04782v2
doc_title: "q-Hodge complexes over the Habiro ring Ferdinand Wagner"
section_id: sec-005-21-a-general-descent-principle
section_title: "A general descent principle"
section_number: 2.1
pages: 13-14
source_pdf: 2510.04782v2.pdf
source_sha256: 591d0bdf2c48d12f
doc_brief: "q-Hodge complexes over the Habiro ring Ferdinand Wagner — — Peter Scholze has raised the question whether some variant of the q-de Rham complex is already defined over theHabiro ringH := limm∈N Z[q]∧"
---
To constructHR/A, we’ll first construct the completions(HR/A)∧
Φm(q) for allm∈ N and then
“glue them together” using a very general descent principle that we’ll explain in this subsection.
It will probably seem a little overkill for now, but we’ll use the same descent principle again in
§3.3 to construct the twistedq-de Rham complexesq9dR(m)
R/A.
2.1. Setup. — LetI be a site whose underlying category is a partially ordered set. LetD be
a presentable stable symmetric monoidal∞-category. Suppose that for everyZ∈I we have a
full stable sub-∞-categoryDZ satisfying the following conditions:
(a) The inclusionDZ⊆D admits a left adjointLZ :D/∫hortrightarrowDZ.
(b) WheneverZ1/∫hortrightarrowZ2 is a morphism inI, we haveDZ1⊆D Z2. Note thatLZ1 :DZ2/∫hortrightarrowDZ1
is still a left adjoint of this inclusion.
(c) For allx,y∈D and allZ∈I , the canonical morphismLZ(x⊗y)/∫hortrightarrowLZ(LZ(x)⊗y) is an
equivalence inD.
In this case, sendingZ↦/∫hortrightarrowDZ and (Z1/∫hortrightarrowZ2)↦/∫hortrightarrow(LZ1 :DZ2/∫hortrightarrowDZ1) defines a contravariant
functor
D(−) :Iop−/∫hortrightarrowCAlg(PrL
st)
into the∞-category of presentable stable symmetric monoidal∞-categories. Indeed, let’s
ignore the symmetric monoidal structure for the moment and letDI ⊆I×D be the full
sub-∞-category spanned fibrewise byDZ⊆{ Z}×D . By (b),DI/∫hortrightarrowI is still a cocartesian
fibration and so it defines a covariant functorD(−) :I/∫hortrightarrowCat∞. By (a), this functor factors
through PrR
st. Using PrL
st≃ (PrR
st)op by [L-HTT, Corollary 5.5.3.4], we get the desired functor
D(−) :Iop/∫hortrightarrowPrL
st.
To incorporate the symmetric monoidal structure, letD be the∞-operadD⊗ associated to
the given symmetric monoidal structure onD. By (c) and [L-HA, Proposition 2.2.1.9], for all
Z∈I , the inclusion of the full sub-∞-operadD⊗
Z⊆D⊗ spanned byDZ admits a symmetric
monoidal left adjointL⊗
Z :D⊗/∫hortrightarrowD⊗
Z which recoversLZ on underlying∞-categories. Using this
observation, the same argument as above can be repeated withD replaced byD⊗.
2.2. Lemma. — In the situation of2.1, assume that covers inI always have finite refinements
and that for any finite covering family{Zi/∫hortrightarrowZ}i=1,...,r, the functorsLZi :DZ/∫hortrightarrowDZi are jointly
conservative. Then
D(−) :Iop−/∫hortrightarrowCAlg(PrL
st)
is a sheaf onI. In particular,CAlg(D(−)):Iop/∫hortrightarrowPrL is a sheaf as well.
13
