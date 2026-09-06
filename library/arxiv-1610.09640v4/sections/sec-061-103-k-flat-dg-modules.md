---
doc_id: arxiv-1610.09640v4
doc_title: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI"
section_id: sec-061-103-k-flat-dg-modules
section_title: "K-Flat DG Modules"
section_number: 10.3
pages: 181-182
source_pdf: 1610.09640v4.pdf
source_sha256: db5e7a5c5e85f95f
doc_brief: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI — This is the fourth (and last) prepublication version of a book on derived categories, that will be published by"
---
Aop. The objects ofC(Aop) are the right DGA-modules.
Deﬁnition 10.3.1.A DG moduleP ∈C(A) is called K-ﬂatif for every acyclic
DG moduleN∈C(Aop), the DGK-module N⊗AP is acyclic.
Deﬁnition 10.3.2.Let M ∈C(A). A K-ﬂat resolutionof M is a quasi-iso-
morphism ρ:P→M in Cstr(A), whereP is a K-ﬂat DG module.
Remark 10.1.5 on terminology applies here as well.
Deﬁnition 10.3.3.Let K be a full triangulated subcategory ofK(A). We denote
by Kﬂat the full subcategory ofK(A) on the K-ﬂat complexes in it. ThusKﬂat =
K∩K(A)ﬂat.
The warning in Remark 10.1.8 applies here too.
Proposition 10.3.4. If P∈C(A) is K-projective then it is K-ﬂat.
Proof. LetK∗be an injective cogenerator ofM(K) = ModK. This means thatK∗
is an injectiveK-module, such that every nonzeroK-module W admits a nonzero
homomorphism W →K∗. See Examples 11.6.1 and 11.6.1. It is not hard to see
that a DGK-module W is acyclic if and only ifHomK(W,K∗) is acyclic.
Take an acyclic complexN∈C(Aop). Then by Hom-tensor adjunction there is
an isomorphism of DGK-modules
HomK(N⊗AP,K∗)∼= HomA
(
P, HomK(N,K∗)
{
.
The right side is acyclic by our assumptions. Hence so is the left side. It follows
that N⊗AP is acyclic. □
Proposition 10.3.5. A DG moduleP∈K(A) is K-ﬂat iﬀ
HomK(A)
(
P, HomK(N,J )
{
= 0
for every acyclicN∈C(Aop) and every injectiveJ∈ModK.
Exercise 10.3.6.Prove Proposition 10.3.5. (Hint: look at the proof of Proposition
10.3.4.)
Proposition 10.3.7. Let K be a full triangulated subcategory ofK(A). Then Kﬂat
is a full triangulated subcategory ofK.
Exercise 10.3.8. Prove Proposition 10.3.7. (Hint: The challenge is to show that
Kﬂat is closed under distinguished triangles. Use Proposition 10.3.5.)
InTheorem12.3.1ontheleftderivedbifunctor (−⊗L
A−)ofthebifunctor (−⊗A−)
we will use K-ﬂat resolutions.
Remark 10.3.9. In view of Proposition 10.3.4, the reader might wonder why we
bother with K-ﬂat DG modules. The reason is that there are situations in which
there are enough K-ﬂat objects but not enough K-projective objects. One such
situation is that of the categoryC(A) = C(ModA), where (X,A) is a ringed space
and ModA is the category of sheaves ofA-modules; see Example 11.3.16. Another
situation is when K-ﬂatness is needed is for DG bimodules over noncommutative
DG rings, as in Sections 14 and later.
181
Derived Categories | Amnon Yekutieli | 14 Apr 2019
