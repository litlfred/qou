---
doc_id: arxiv-1610.09640v4
doc_title: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI"
section_id: sec-028-36-complexes-in-abelian-categories
section_title: "Complexes in Abelian Categories"
section_number: 3.6
pages: 65-66
source_pdf: 1610.09640v4.pdf
source_sha256: db5e7a5c5e85f95f
doc_brief: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI — This is the fourth (and last) prepublication version of a book on derived categories, that will be published by"
---
from the classical homological theory, and place them within our context. In this
subsection M is aK-linear abelian category.
A complex of objects ofM, or acomplex in M, is a diagram
(3.6.1)
(
···→M−1 d−1
M
−−→M0 d0
M
−−→M1 d1
M
−−→M2→···
{
of objects and morphisms inM, such thatdi+1
M ◦di
M = 0. The collection of objects
M :={Mi}i∈Z is nothing but a graded object ofM, as deﬁned in Subsection 3.1.
The collection of morphismsdM :={di
M}i∈Z is called adiﬀerential, or acoboundary
operator. Thus a complex is a pair(M, dM) made up of a graded objectM and a
diﬀerentialdM on it. We sometimes writed instead of dM or di
M. At other times
we leave the diﬀerential implicit, and just refer to the complex asM.
Let N be another complex inM. A strict morphism of complexesφ:M→N is
a collectionφ={φi}i∈Z of morphismsφi :Mi→Ni in M, such that
(3.6.2) di
N◦φi =φi+1◦di
M.
Note that a strict morphismφ:M→N can be viewed as a commutative diagram
···//Mi di
M //
φi

Mi+1 //
φi+1

···
···//Ni di
N //Ni+1 //···
in M. The identity automorphismidM of the complexM is a strict morphism.
Remark 3.6.3. In most textbooks, what we call “strict morphism of complexes”
is simply called a “morphism of complexes”. See Remark 3.1.35 for an explanation.
Let us denote byCstr(M) the category of complexes inM, with strict morphisms.
This is aK-linear abelian category. Indeed, the direct sum of complexes is the
degree-wise direct sum, i.e. (M⊕N)i = Mi⊕Ni. The same for kernels and
cokernels. If N is a full abelian subcategory ofM, then Cstr(N) is a full abelian
subcategory of Cstr(M).
A single objectM0∈M can be viewed as a complex
M :=
(
···→0→M0→0→···
{
,
where M0 is in degree 0; the diﬀerential of this complex is of course zero. The
assignmentM0↦→M is a fully faithfulK-linear functor M→Cstr(M).
Let M and N be complexes in M. As in (3.1.42) there is a gradedK-module
HomM(M,N ). It is a DGK-module with diﬀerentiald given by the formula
(3.6.4) d(φ) := dN◦φ−(−1)i·φ◦dM
65
Derived Categories | Amnon Yekutieli | 14 Apr 2019
for φ∈HomM(M,N )i. It is easy to check thatd◦d = 0. We sometimes denote
this diﬀerential bydHom or dHomM(M,N).
Thus, an elementφ∈HomM(M,N )i is a collectionφ={φj}j∈Z of morphisms
φj :Mj→Nj+i. In a diagram, fori = 2, it looks like this:
···//Mj d //
φj
((
Mj+1 d //
φj+1
))
Mj+2 d //Mj+3 //···
···//Nj d //Nj+1 d //Nj+2 d //Nj+3 //···
Warning: sinceφdoes not have to commute with the diﬀerentials, this is usually
not a commutative diagram!
For a triple of complexesM0,M 1,M 2 and degreesi0,i 1 there areK-linear homo-
morphisms
HomM(M1,M 2)i1⊗HomM(M0,M 1)i0− →HomM(M0,M 2)i0+i1,
φ1⊗φ0↦→φ1◦φ0.
Lemma 3.6.5. The composition homomorphism
HomM(M1,M 2)⊗HomM(M0,M 1)− →HomM(M0,M 2)
is a strict homomorphism of DGK-modules.
Exercise 3.6.6. Prove the lemma.
The lemma justiﬁes the next deﬁnition.
Deﬁnition 3.6.7.Let C(M) be the DGK-linear category whose objects are the
complexes in M, and whose morphism DGK-modules are HomM(M,N ), from for-
mulas (3.1.42) and (3.6.4).
It is clear, from comparing formulas (3.6.4) and (3.6.2), that the strict morphisms
of complexes deﬁned at the top of this subsection are the same as those from
Deﬁnition 3.4.6(1). In other words,Str(C(M)) = Cstr(M).
Remark 3.6.8. A possible ambiguity could arise in the meaning ofHomM(M,N )
if M,N ∈M. Does it mean the K-module of morphisms in the category M ?
Or, if we viewM and N as complexes by the canonical embeddingM⊆C(M),
does HomM(M,N ) mean the complex of morphisms in the DG categoryC(M) ?
It turns out that there is no actual diﬃculty: since the complex ofK-modules
HomM(M,N ) is concentrated in degree0, we may view it as a singleK-module,
and this is precisely theK-module of morphisms in the categoryM.
When M = ModA for a ringA, there is no essential distinction between com-
plexes and DG modules. The next proposition is the DG version of Exercise 3.1.44.
Proposition 3.6.9. Let A be a ring. Given a complex M ∈C(ModA), with
notation as in(3.6.1), deﬁne the DGA-moduleF (M) :=⨁
i∈ZMi, with diﬀerential
d :=∑
i∈Z di
M. Then the functorF : C(ModA)→DGModA is an isomorphism of
DG categories.
Exercise 3.6.10. Prove this proposition. (Hint: choose good notation.)
