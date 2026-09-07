---
doc_id: arxiv-1610.09640v4
doc_title: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI"
section_id: sec-030-39-contravariant-dg-functors
section_title: "Contravariant DG Functors"
section_number: 3.9
pages: 74-79
source_pdf: 1610.09640v4.pdf
source_sha256: db5e7a5c5e85f95f
doc_brief: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI — This is the fourth (and last) prepublication version of a book on derived categories, that will be published by"
---
fashion, the issue of reversing arrows in DG categories. As always, we work over a
commutative base ringK.
Deﬁnition 3.9.1.Let C and D be DG categories. A contravariant DG functor
F : C→D consists of a functionF : Ob(C)→Ob(D), and for each pair of objects
M0,M 1∈Ob(C) a homomorphism
F : HomC(M0,M 1)→HomD
(
F (M1),F (M0)
{
in Cstr(K). The conditions are:
(a) Units: F (idM) = idF(M).
(b) Graded reversed composition: suppose that for k ∈ {0, 1}we are given
morphisms φk∈HomC(Mk,Mk+1)ik. Then there is equality
F (φ1◦φ0) = (−1)i0·i1·F (φ0)◦F (φ1)
inside HomD
(
F (M2),F (M0)
{i0+i1
.
Warning: a contravariant DG functor does not remain a contravariant functor
after the grading is forgotten; cf. Remark 3.1.26.
Here is the categorical version of Deﬁnition 3.3.13.
74
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Deﬁnition 3.9.2.Let C be a DG category. Theopposite DG categoryCop has the
same set of objects. The morphism DGK-modules are
HomCop(M0,M 1) := HomC(M1,M 0).
The composition◦op of Cop is the composition◦of C, reversed and multiplied by
signs:
φ0◦opφ1 := (−1)i0·i1·φ1◦φ0
for morphismsφk∈HomC(Mk,Mk+1)ik.
One needs to verify that this is indeed a DG category. This is basically the same
veriﬁcation as in Exercise 3.3.14.
As before, we deﬁne the operationOp : C→Cop to be the identity on objects,
and the identity on morphisms in reversed order, i.e.
Op = id : HomC(M0,M 1)
≃
− →HomCop(M1,M 0).
Note that (Cop)op = C, and we denote the inverse operationCop→C also by Op.
Proposition 3.9.3. Let C, D and E be DG categories.
(1) The operations Op : C→Cop and Op : Cop→C are contravariant DG
functors.
(2) If F : C→D is a contravariant DG functor, then the compositionF◦Op :
Cop→D is a DG functor; and vice versa.
(3) If F : C→D and G : D→E are contravariant DG functors, then the
compositionG◦F : C→E is a DG functor.
Exercise 3.9.4. Prove the previous proposition.
Deﬁnitions 3.9.2 and 3.9.1 make sense for graded categories, by forgetting diﬀer-
entials. Thus for graded categoriesC and D we can talk about contravariant graded
functors C→D, and about the graded categoryCop.
We already met G(M), the category of graded objects in an abelian category
M; see Deﬁnition 3.1.43. It is a graded category. Its objects are collectionsM =
{Mi}i∈Z of objectsMi∈M.
Let M and N be abelian categories, and letF : M→N be a contravariant linear
functor. For a graded objectM ={Mi}i∈Z∈G(M) let us deﬁne the graded object
(3.9.5) G(F )(M) :={Ni}i∈Z∈G(N), N i :=F (M−i)∈N.
Next consider a pair of objectsM0,M 1∈G(M) and a degreei morphism φ:
M0→M1 in G(M). Thus
φ={φj}j∈Z∈HomG(M)(M0,M 1)i,
where, as in formula (3.1.41), the morphismφj belongs to HomM(Mj
0,M j+i
1 ). We
have objectsNk := G(F )(Mk)∈G(N), fork∈{0, 1}, deﬁned by (3.9.5). Explicitly,
Nk ={Ni
k}i∈Z and Ni
k =F (M−i
k ). For eachj∈Z deﬁne the morphism
(3.9.6) ψj := (−1)i·j·F (φ−j−i)∈HomN
(
Nj
1,N j+i
0
{
.
Collecting them we obtain a morphism
(3.9.7) G(F )(φ) :={ψj}j∈Z∈HomG(N)(N1,N 0)i.
Lemma 3.9.8.The assignments(3.9.5) and (3.9.7) produce a contravariant graded
functor G(F ) : G(M)→G(N).
Proof. Since for morphisms of degree 0 there is no sign twist, the identity au-
tomorphism idM ={idMi}i∈Z of M ={Mi}i∈Z in G(M) is sent to the identity
automorphism of G(F )(M) in G(N).
75
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Next we look at morphismsφk ={φj
k}j∈Z in HomG(M)(Mk,Mk+1)ik fork = 0, 1.
The compositionφ1◦φ0 has degreei0 +i1, and thej-th component ofφ1◦φ0 is
φj+i0
1 ◦φj
0. Therefore thej-th component ofG(F )(φ1◦φ0) is
(3.9.9)
G(F )(φ1◦φ0)j = (−1)j·(i0+i1)·F
(
φ−j−i1
1 ◦φ−j−(i0+i1)
0
{
= (−1)j·(i0+i1)·F (φ−j−(i0+i1)
0 )◦F (φ−j−i1
1 ).
The j-th component ofG(F )(φk) is G(F )(φk)j = (−1)j·ik·F (φ−j−ik
k ). So thej-th
component of (−1)i0·i1·G(F )(φ0)◦G(F )(φ1) is
(3.9.10)
(−1)i0·i1·
(
G(F )(φ0)◦G(F )(φ1)
{j
= (−1)i0·i1·(−1)(j+i1)·i0·F (φ−(j+i1)−i0
0 )◦(−1)j·i1·F (φ−j−i1
1 ).
We see that the morphisms (3.9.9) and (3.9.10) are equal. □
Now we consider a complex(M, dM)∈C(M). This is made up of a graded object
M ={Mi}i∈Z∈G(M) together with a diﬀerentialdM ={di
M}i∈Z, where di
M :
Mi→Mi+1. We can viewdM as an element ofEndG(M)(M)1 = HomG(M)(M,M )1.
We specify a diﬀerentialdC(F)(M) on the graded objectG(F )(M)∈G(N) as follows:
(3.9.11) dC(F)(M) :=−G(F )(dM)∈EndG(N)
(
G(F )(M)
{1
.
To be explicit, the component
di
C(F)(M) : G(F )(M)i =F (M−i)→F (M−i−1) = G(F )(M)i+1
of dC(F)(M) is, by (3.9.6),
(3.9.12) di
C(F)(M) = (−1)i+1·F (d−i−1
M ) :F (M−i)→F (M−i−1).
This shows that our formula coincides with the one in [75, Remark 1.8.11].
The full subcategory C⋆(N)⊆C(N), for a given boundedness condition⋆, was
introducedinDeﬁnition3.8.20. Eachboundednesscondition ⋆hasa reversed bound-
edness condition−⋆, with the obvious meaning; e.g. if⋆is + then−⋆is−.
Theorem 3.9.13. Let M and N be abelian categories, and letF : M→N be a
contravariant linear functor. The assignments(3.9.5), (3.9.7) and (3.9.11) produce
a contravariant DG functor
C(F ) : C(M)→C(N).
For every boundedness condition⋆we have C(F )
(
C⋆(M)
{
⊆C−⋆(N), where−⋆is
the reversed boundedness condition.
Proof. We already know, by Lemma 3.9.8, thatG(F ) is a graded functor. We need
to prove that for a pair of DG modules(M0, dM0) and (M1, dM1) in C(M) the strict
homomorphism of gradedK-modules
G(F ) : HomG(M)(M0,M 1)→HomG(N)
(
G(F )(M1), G(F )(M0)
{
respects diﬀerentials. Take anyφ∈HomG(M)(M0,M 1)i. By deﬁnition we have
d(φ) = dM1◦φ−(−1)i·φ◦dM0. Using the fact thatG(F ) is a contravariant graded
functor, we obtain these equalities:
G(F )(d(φ))
= (−1)i·G(F )(φ)◦G(F )(dM1)−(−1)i·(−1)i·G(F )(dM0)◦G(F )(φ)
= dC(F)(M0)◦G(F )(φ)−(−1)i·G(F )(φ)◦dC(F)(M1) = d(G(F )(φ)).
The claim about the boundedness conditions is immediate from equation (3.9.5).
□
76
Derived Categories | Amnon Yekutieli | 14 Apr 2019
The sign appearing in formula (3.9.11) might seem arbitrary. Besides being the
only sign for which Theorem 3.9.13 holds, there is another explanation, which can
be seen in the next exercise.
Exercise 3.9.14. Take M = N := ModK, and consider the contravariant additive
functor F := Hom K(−,K) from M to itself. LetM∈C(M); we can viewM as a
complex ofK-modules or as a DGK-module, as done in Proposition 3.6.9. Show
that C(F )(M)∼= HomK(M,K) in Cstr(K), where the second object is the graded
module from formula (3.1.42), with the diﬀerentiald from Deﬁnition 3.2.3(2).
The next deﬁnition and theorem will help us later when studying contravariant
triangulated functors.
Deﬁnition 3.9.15.Let A be a DG ring and letM be an abelian category. The
ﬂipped categoryof C(A, M) is the DG categoryC(A, M)ﬂip := C(Aop, Mop).
Theorem 3.9.16. LetA be a DG ring and letM be an abelian category. Then:
(1) There is a canonical isomorphism of DG categories
Flip : C(A, M)op ≃
− →C(Aop, Mop) = C(A, M)ﬂip.
(2) For every boundedness condition⋆we have
Flip
(
C⋆(A, M)op{
= C−⋆(Aop, Mop),
where−⋆is the reversed boundedness condition.
(3) The induced isomorphism on the strict categories
Str(Flip) : Cstr(A, M)op ≃
− →Cstr(Aop, Mop)
is an exact functor, for the respective abelian category structures.
(4) For every integeri, the functorStr(Flip) makes the diagram
Cstr(A, M)op Str(Flip)
∼=
//
Hi
))
Cstr(Aop, Mop)
H−i

Mop
commutative, up to an isomorphism of linear functors.
Proof.
(1) According to Proposition 3.9.3 there is a contravariant DG functor Op :
C(A, M)op→C(A, M). It is bijective on objects and morphisms. We are going
to construct a contravariant DG functorE : C(A, M)→C(Aop, Mop) which is also
bijective on objects and morphisms. The composed DG functor
Flip :=E◦Op : C(A, M)op→C(Aop, Mop)
will have the desired properties.
Let us constructE. We start with the contravariant additive functorF := Op :
M→Mop. Theorem 3.9.13 says thatC(F ) : C(M)→C(Mop) is a contravariant DG
functor. Recall that an object ofC(A, M)is a triple(M, dM,fM), whereM∈G(M);
dM is a diﬀerential on the graded objectM; andfM : A→EndC(M)(M) is a DG
ring homomorphism. See Deﬁnitions 3.1.47, 3.8.1 and 3.8.3. Deﬁne(N, dN) :=
C(F )(M, dM)∈C(Mop). Since C(F ) : End C(M)(M, dM)→EndC(Mop)(N, dN) is
a DG ring anti-homomorphism (by which we mean the single object version of a
contravariant DG functor), andOp :Aop→A is also such an anti-homomorphism,
it follows that
fN := C(F )◦fM◦Op :Aop→EndC(Mop)(N, dN)
77
Derived Categories | Amnon Yekutieli | 14 Apr 2019
is a DG ring homomorphism. ThusE(M, dM,fM) := (N, dN,fN) is an object of
C(Aop, Mop). In this way we have a function
E : Ob
(
C(A, M)
{
→Ob
(
C(Aop, Mop)
{
,
and it is clearly bijective.
The operation ofE on morphisms is of course that ofC(F ). It remains to verify
that the resulting morphisms in C(Mop) respect the action of elements of Aop.
Namely that the condition in Deﬁnition 3.1.47 is satisﬁed. Take any morphism
φ∈HomC(A,M)
(
(M0, dM0,fM0), (M1, dM1,fM1)
{i
and any elementa∈(Aop)j; and write(Nk, dNk,fNk) :=E(Mk, dMk,fMk) and
ψ:= G(F )(φ)∈HomC(Mop)
(
(N1, dN1), (N0, dN0)
{i
.
We have to prove that
(3.9.17) ψ◦fN1(a) = (−1)i·j·fN0(a)◦ψ.
This is done using Lemma 3.9.8, like in the proof of Theorem 3.9.13; and we leave
this to the reader.
(2) Clear from Theorem 3.9.13.
(3) Exactness in the categoriesCstr(A, M)op and Cstr(Aop, Mop) is checked in each
degree separately, and both are exactness in the abelian categoryMop. The functor
Str(Flip) is±IdMop in each degree, so it is exact.
(4) As complexes in Mop, M and Flip(M) are equal, up to the renumbering of
degrees and the signs of the diﬀerentials in various degrees. So the cohomology
objects satisfy Hi(M)∼= H−i(Flip(M)) in Mop. □
Exercise 3.9.18. Prove formula (3.9.17) above.
Remark 3.9.19.Theorem 3.9.16 will be used to introduce a triangulated structure
on the categoryK(A, M)op. This will be done in Subsection 5.6.
Combined with Proposition 3.9.3, Theorem 3.9.16 allows us to replace a con-
travariant DG functor F : C(A, M) →D with a usual, covariant, DG functor
F◦Flip−1 : C(Aop, Mop)→D. This replacement is going to be very useful when
discussing formal properties, such as existence of derived functors etc.
However, in practical terms (e.g. for producing resolutions of DG modules), the
category C(Aop, Mop) is not very helpful. The reason is that the opposite abelian
category Mop is almost always a synthetic construction (it does not “really exist in
concrete terms”). See Remark 2.7.20 and Example 2.7.21.
We are going to maneuver between the two approaches for reversal of morphisms,
each time choosing the more useful approach.
78
Derived Categories | Amnon Yekutieli | 14 Apr 2019
