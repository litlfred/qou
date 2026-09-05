---
doc_id: arxiv-1610.09640v4
doc_title: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI"
section_id: sec-026-34-dg-categories
section_title: "DG Categories"
section_number: 3.4
pages: 62-64
source_pdf: 1610.09640v4.pdf
source_sha256: db5e7a5c5e85f95f
doc_brief: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI — This is the fourth (and last) prepublication version of a book on derived categories, that will be published by"
---
DG version.
Deﬁnition 3.4.1.A DGK-linear categoryis aK-linear category C, endowed with
a DG K-module structure on each of the morphismK-modules HomC(M0,M 1).
The conditions are these:
(a) For every objectM, the identity automorphismidM is a degree0 cocycle
in HomC(M,M ).
(b) Foreverytripleofobjects M0,M 1,M 2∈C, thecompositionhomomorphism
HomC(M1,M 2)⊗HomC(M0,M 1)− →HomC(M0,M 2)
is a strict homomorphism of DGK-modules.
The diﬀerential in a DGK-linear category C is sometimes denoted bydC; for
instance
(3.4.2) dC : HomC(M0,M 1)i→HomC(M0,M 1)i+1.
The next convention extends Convention 3.3.3.
Convention 3.4.3. We shall often write “DG category” instead of the longer
expression “DGK-linear category”.
If C′is a full subcategory of a DG categoryC, then of courseC′is itself a DG
category.
Deﬁnition 3.4.4.Let C be a DG category.
(1) A morphismφ∈HomC(M,N )i is called adegreei morphism.
(2) A morphismφ∈HomC(M,N ) is called acocycleif dC(φ) = 0.
(3) A morphismφ:M→N in C is called astrict morphismif it is a degree0
cocycle.
Lemma 3.4.5. Let C be a DG category, and fori = 0, 1, 2 let φi :Mi→Mi+1 be
a morphism inC of degreeki.
(1) The morphismφ1◦φ0 has degreek0 +k1, and
dC(φ1◦φ0) = dC(φ1)◦φ0 + (−1)k1·φ1◦dC(φ0).
(2) If φ0 and φ1 are cocycles, then so isφ1◦φ0.
62
Derived Categories | Amnon Yekutieli | 14 Apr 2019
(3) If φ1 is a coboundary, andφ0 and φ2 are cocycles, thenφ2◦φ1◦φ0 is a
coboundary.
Proof. (1) This is just a rephrasing of item (b) in Deﬁnition 3.4.1.
(2) This is immediate from (1).
(3) Sayφ1 = dC(ψ1) for some degreek1−1 morphism ψ1 :M1→M2. Then
φ2◦φ1◦φ0 = dC
(
(−1)k2·φ2◦ψ1◦φ0
{
. □
The previous lemma makes the next deﬁnition possible.
Deﬁnition 3.4.6. Let C be a DG category.
(1) The strict subcategoryof C is the categoryStr(C), with the same objects as
C, but with strict morphisms only. Thus
HomStr(C)(M,N ) = Z0(
HomC(M,N )
{
.
(2) The homotopy categoryof C is the categoryHo(C), with the same objects
as C, and with morphism sets
HomHo(C)(M,N ) := H0(
HomC(M,N )
{
.
(3) We denote by P : Str( C)→Ho(C) the functor which is the identity on
objects, and sends a strict morphism to its homotopy class.
The categoriesStr(C) and Ho(C) are linear, and the inclusion functorStr(C)→C
and the projection functorP : Str(C)→Ho(C) are linear. The ﬁrst is faithful, and
the second is full.
Example 3.4.7. If A is a DG category, then for every objectx∈A, its set of
endomorphisms A := EndA(x) is a DG ring. Conversely, every DG ringA can be
viewed as a DG categoryA with a single object.
Example 3.4.8. Let A be a DG ring. The set of DG A-modules forms a DG
category DGModA, in which the morphism DGK-modules are
HomDGModA(M,N ) := HomA(M,N )
from Deﬁnition 3.3.24. We shall often writeC(A) := DGModA. The strict subcat-
egory here is
Str(DGModA) = DGModstrA = Cstr(A);
cf. Deﬁnition 3.3.19.
Here is a result that will be used later.
Proposition 3.4.9. Letφ:M→N be a degreei isomorphism in a DG category
C. Assume φis a cocycle, namelydC(φ) = 0. Then its inverseφ−1 : N→M is
also a cocycle.
Proof. According the Leibniz rule (Lemma 3.4.5(1)), and the fact thatidM is a
cocycle, we have
0 = dC(idM) = d(φ−1◦φ)
= dC(φ−1)◦φ+ (−1)−i·φ−1◦dC(φ) = dC(φ−1)◦φ.
Because φis an isomorphism, we conclude thatdC(φ−1) = 0. □
Remark 3.4.10.The fact that the concept “DG category” refers both to DG rings
(Example 3.4.7) and to the categories of DG modules over them (Example 3.4.8)
is a source of frequent confusion. See Remarks 3.1.51 and 3.8.21.
63
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Remark 3.4.11. For other accounts of DG categories see the relatively old refer-
ences [85], [79], [25], or the more recent [151]. An internet search can give plenty
more information, including the relation to simplicial and inﬁnity categories.
In this book we shall be exclusively concerned with the DG categoriesC(A, M),
to be introduced in Subsection 3.8, which have a lot more structure than other DG
categories.
See Remark 3.8.21 regarding the DG categoryC(A) of DG modules over a DG
category A, in the sense of [79]; and Remark 3.8.22 regardingA∞categories.
3.5. DGFunctors. Here Cand DareDG K-linearcategories(seeDeﬁnition3.4.1).
When we forget diﬀerentials,C and D become gradedK-linear categories. So we
can talk about gradedK-linear functors C→D, as in Deﬁnition 3.1.36.
Recall the meaning of a strict homomorphism of DGK-modules: it has degree
0 and commutes with the diﬀerentials.
Deﬁnition 3.5.1.Let C and D be DGK-linear categories. A functorF : C→D
is called aDGK-linear functorif it satisﬁes this condition:
⊿ For every pair of objectsM0,M 1∈C, the function
F : HomC(M0,M 1)→HomD
(
F (M0),F (M1)
{
is a strict homomorphism of DGK-modules.
In other words,F is a DG functor if it is a graded functor, anddD◦F =F◦dC
as degree 1 homomorphisms
HomC(M0,M 1)→HomD
(
F (M0),F (M1)
{
.
To match Convention 3.4.3, here is:
Convention 3.5.2. We shall usually write “DG functor” instead of the longer
expression “DGK-linear functor”.
Example 3.5.3. Let f :A→B be a homomorphism of DG rings, and letA and
B be the corresponding single-object DG categories. Then f gives rise to a DG
functor F : A→B.
