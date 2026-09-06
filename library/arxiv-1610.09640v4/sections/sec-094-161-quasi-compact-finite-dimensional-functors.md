---
doc_id: arxiv-1610.09640v4
doc_title: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI"
section_id: sec-094-161-quasi-compact-finite-dimensional-functors
section_title: "Quasi-Compact Finite Dimensional Functors"
section_number: 16.1
pages: 351-355
source_pdf: 1610.09640v4.pdf
source_sha256: db5e7a5c5e85f95f
doc_brief: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI — This is the fourth (and last) prepublication version of a book on derived categories, that will be published by"
---
section is adapted from [157, Section 1]. We state the results in the context of
algebraically graded rings and modules, since here we need them for the graded
m-torsion functorF := Γ m; yet these results hold in greater generality (see [157]).
Recall from Subsection 15.1 that given a graded ringA, the category of gradedA-
modules isM(A, gr). This is aK-linear abelian category. The category of complexes
in M(A, gr)is C(A, gr), the homotopy category isK(A, gr), and the derived category
is D(A, gr).
In this subsection we consider the following setup:
Setup 16.1.1. A and B are graded rings, andF : M(A, gr)→M(B, gr) is a left
exact linear functor.
The functor F extends to a triangulated functor F : K(A, gr) →K(B, gr)
between the homotopy categories. Because there are enough K-injective resolu-
tions, F has a right derived functor (RF,ηR). Let us recall what this means:
RF : D(A, gr)→D(B, gr) is a triangulated functor, andηR : Q◦F →RF◦Q
is a morphism of triangulated functors K(A, gr) →D(B, gr) that has a certain
universal property (see Deﬁnition 8.4.7). The right derived functor(RF,ηR) can
be constructed using a K-injective presentation: for each complexM we choose a
K-injective resolutionρM : M→IM in Cstr(A, gr), and then we takeRF (M) :=
F (IM) and ηR
M :=F (ρM).
Recall that the functor F has the classical right derived functors RqF :
M(A, gr)→M(B, gr). These can be expressed as follows:RqF (M) = Hq(RF (M))
for a moduleM∈M(A, gr). Since F is left exact, the canonical homomorphism
F→R0F is an isomorphism.
Here is a classical deﬁnition:
ThismaterialwillbepublishedbyCambridgeUniversityPressas Derived CategoriesbyAmnon
Yekutieli. This prepublication version is free to view and download for personal use only. Not for
redistribution, resale or use in derivative works.c© Amnon Yekutieli, 2019.
351
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Deﬁnition 16.1.2.The right cohomological dimension ofF is
d := sup{q∈N|RqF⁄= 0}∈N∪{±∞}.
If F ⁄= 0 then d∈N∪{∞}, but forF = 0 the dimension isd =−∞. The
generalized integerd is said to be ﬁnite ifd <∞; this terminology is designed so
that the zero functor will have ﬁnite right cohomological dimension.
Here is another standard deﬁnition.
Deﬁnition 16.1.3.A module I ∈M(A, gr) is called a right F-acyclic object if
RqF (I) = 0 for allq >0.
Of course every injective object ofM(A, gr) is rightF-acyclic. But often there
are many more rightF-acyclic objects.
Deﬁnition 16.1.4.A complexI∈C(A, gr) is called aright F-acyclic complexif
the morphismηR
I :F (I)→RF (I) in D(B, gr) is an isomorphism.
Of course a K-injective complex is rightF-acyclic, but often there are many
more. It is easy to see that a moduleI∈M(A, gr) is a rightF-acyclic object in
the sense of Deﬁnition 16.1.3 if and only if it is rightF-acyclic as a complex, in the
sense of Deﬁnition 16.1.4.
Lemma 16.1.5. Let I ∈C(A, gr) be a complex such that each of the modules
Iq is right F-acyclic. If I is a bounded below complex, or ifF has ﬁnite right
cohomological dimension, thenI is a rightF-acyclic complex.
Proof. This is contained in the proof of [62, Corollary I.5.3], but for the sake of
completeness we give a proof here.
We can assume that neitherF nor I are zero. First let us assume that I is
bounded below. We can ﬁnd a quasi-isomorphismI→J in Cstr(A, gr), whereJ
is a bounded below complex of injective objects ofM(A, gr), and thus it is a K-
injective complex. We must show thatF (I)→F (J) is a quasi-isomorphism. This
amounts to showing that the complexF (K) is acyclic, whereK is the standard
cone on the quasi-isomorphismI →J. Thus we reduce the problem to proving
that for an acyclic bounded below complexI made up of rightF-acyclic objects,
the complexF (I) is acyclic.
Say inf(I) =d0∈Z. For anyq let Zq(I) := Ker(Iq→Iq+1), the object of degree
q cocycles. The acyclicity of the complexI says that we have short exact sequences
0→Zq(I)→Iq→Zq+1(I)→0.
By induction onq≥d0−1, using the long exact cohomology sequence, we prove
that each Zq(I) is a rightF-acyclic object. Therefore the sequences
0→F (Zq(I))→F (Iq)→F (Zq+1(I))→0
are exact for allq. Splicing together three sequences like this, forq−1,q andq + 1,
shows that the sequenceF (Iq−1)→F (Iq)→F (Iq+1) is exact. Thus the complex
F (I) is acyclic.
NowI is no longer bounded below, but the right cohomological dimension ofF
is ﬁnite, sayd∈N. Let I→J be a quasi-isomorphism inCstr(A, gr), whereJ is
a K-injective complex made up of injective objects (see Corollary 15.3.7(3)). We
must show thatF (I)→F (J) is a quasi-isomorphism. As above, by replacingI
with the standard cone onI→J, we reduce the problem to proving that for an
acyclic complexI made up of rightF-acyclic objects, the complexF (I) is acyclic.
Fix an an integerq. LetM := Zq(I), and let
J := (···→0→Iq→Iq+1→···),
352
Derived Categories | Amnon Yekutieli | 14 Apr 2019
the complex withIq placed in degree0 (soJ is a shift of a stupid truncation ofI).
By the previous part of the proof we know thatRF (J)∼= F (J) in D(B, gr). We
have a quasi-isomorphismM→J. Hence, for everyp > d, by our assumption on
F we have
0 = Hp(RF (M))∼= Hp(RF (J))∼= Hp(F (J))∼= Hp+q(F (I)).
Since q was chosen arbitrarily, we conclude thatF (I) is acyclic. □
Recall thecohomological dimensionof the triangulated functorRF : D(A, gr)→
D(B, gr) from Deﬁnition 12.4.1. In what follows we use the various notions intro-
duced in Subsection 12.4, adapted to the graded setting, such as the concentration
interval con(M)⊆Z of an objectM∈G(A, gr).
Lemma 16.1.6. The cohomological dimension of the right derived functor RF
equals the right cohomological dimension ofF.
Proof. As explained in Example 12.4.5, the cohomological dimension of(RF )|M(A)
equals the right cohomological dimension of the functorF. We need to prove the
reverse inequality.
We can assume thatF⁄= 0, and it has ﬁnite right cohomological dimension, say
d∈N. We shall prove that the cohomological displacement of the derived functor
RF is contained in the interval[d0,d 1] := [0,d ]. To be explicit, we shall prove that
for every complexM∈D(A, gr) the integer intervalcon
(
H(RF (M))
{
is contained
in the intervalcon
(
H(M)
{
+ [0,d ]. This is done by cases, and we can assume that
M⁄= 0.
Case 1. IfM is not inD−(A, gr), i.e.con(H(M)) = [d0,∞] for somed0∈Z∪{−∞},
then we can take a K-injective resolutionM →I such that inf(I) = d0. Then
H(RF (M)) = H(F (I)) is concentrated in[d0,∞].
Case 2. HereM∈D−(A, gr), so thatcon(H(M)) = [d0,d 1] for somed0∈Z∪{−∞}
and d1∈Z. We now take a K-injective resolutionM→I such that inf(I) = d0
and I is made up of injective objects. We must prove thatHq(F (I)) = 0 for all
q >d1 +d. This is done like in the proof of Lemma 16.1.5. LetN := Zd1(I), and
let
J := (···→0→Id1→Id1+1→···),
the complex withId1 placed in degree0. So there is a quasi-isomorphismN→J,
and it is an injective resolution ofN. Hence for everyp>d we have
0 = Hp(RF (N))∼= Hp(F (J))∼= Hd1+p(F (I)). □
Deﬁnition 16.1.7.Let M and N be linear categories with arbitrarily direct sums.
A linear functorG : M→N is called quasi-compact if it commutes with inﬁnite
direct sums. Namely, for every collection{Mx}x∈X of objects ofM, the canonical
morphism ⨁
x∈X
G(Mx)→G
(⨁
x∈X
Mx
{
in N is an isomorphism.
The name “quasi-compact functor” is inspired by the property of pushforward
of quasi-coherent sheaves along a quasi-compact map of schemes.
Lemma 16.1.8. Assume that the functorsRqF are quasi-compact, for allq >0.
Let{Ix}x∈X be a collection of rightF-acyclic objects ofM(A, gr). Then the object
I :=⨁
x∈XIx∈M(A, gr) is rightF-acyclic.
Proof. Take someq >0. Because RqF is quasi-compact, the canonical homomor-
phism ⨁
x∈X RqF (Ix)→RqF (I) in N is an isomorphism. But by assumption,
RqF (Ix) = 0 for allx. □
353
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Lemma 16.1.9. Assume the functors RqF are quasi-compact for allq≥0. Let
{Ix}x∈X be a collection of rightF-acyclic complexes in C(A, gr), and deﬁneI :=⨁
x∈XIx ∈C(A, gr). If I is a bounded below complex, or ifF has ﬁnite right
cohomological dimension, thenI is a rightF-acyclic complex.
Proof. For every indexx let us choose a quasi-isomorphismφx : Ix→Jx, where
Jx is a K-injective complex consisting of injective objects, andinf(Jx)≥inf(Ix).
DeﬁneJ := ⨁
x∈XJx. We get a quasi-isomorphism φ:= ⨁
x∈Xφx : I →J in
Cstr(A, gr). By construction, ifI is a bounded below complex, then so isJ.
For everyx∈X there is a commutative diagram
F (Ix)
F(φx) //
ηR
Ix

F (Jx)
ηR
Jx

RF (Ix)
RF(φx) // RF (Jx)
in D(B, gr). The vertical arrows are isomorphisms because bothIx andJx are right
F-acyclic complexes. The morphismRF (φx)is also an isomorphism. It follows that
F (φx) is an isomorphism in D(B, gr); and therefore it is a quasi-isomorphism in
Cstr(B, gr).
Next consider this commutative diagram inCstr(B, gr) :
⨁
x∈X F (Ix)
⨁
x∈X F(φx)
//

⨁
x∈X F (Jx)

F (I)
F(φ) //F (J)
Because eachF (φx) is a quasi-isomorphism, it follows that the top horizontal ar-
row is a quasi-isomorphism. Because the functorF = R0F is quasi-compact, the
vertical arrows are isomorphisms. We conclude thatF (φ) is a quasi-isomorphism
in Cstr(B, gr).
Finally we look at this commutative diagram inD(B, gr) :
F (I)
F(φ) //
ηR
I

F (J)
ηR
J

RF (I)
RF(φ) // RF (J)
We know that the morphismsF (φ) and RF (φ) are isomorphisms. For everyp, the
objectJp =⨁
x∈X Jp
x in M(A, gr) is a direct sum of injective objects. So according
to Lemma 16.1.8,Jp is a rightF-acyclic object. By Lemma 16.1.5, in either of the
two cases, the complexJ is a rightF-acyclic complex. This says that the morphism
ηR
J is an isomorphism. We conclude that the morphismηR
I is an isomorphism too,
and this says thatI is a rightF-acyclic complex. □
Theorem 16.1.10. Under Setup 16.1.1, assume the functor F has ﬁnite right
cohomological dimension, and the functorsRqF, for allq≥0, are quasi-compact.
Then the triangulated functorRF : D(A, gr)→D(B, gr) has ﬁnite cohomological
dimensional and is quasi-compact.
Proof. By Lemma 16.1.6 the functorRF is ﬁnite dimensional. We need to prove
that RF commutes with inﬁnite direct sums. Namely, consider a collection
{Mx}x∈X of complexes inC(A, gr), and letM :=⨁
x∈XMx. We have to prove that
the canonical morphism⨁
x∈X RF (Mx)→RF (M) in D(B, gr) is an isomorphism.
354
Derived Categories | Amnon Yekutieli | 14 Apr 2019
For every indexx we choose a quasi-isomorphismφx : Mx→Ix in Cstr(A, gr),
where Ix is a K-injective complex. Deﬁne I := ⨁
x∈XIx, so there is a quasi-
isomorphism φ:M→I in Cstr(A, gr). We get a commutative diagram
⨁
x∈X RF (Mx)
⨁
RF(φx)
//

⨁
x∈X RF (Ix)

RF (M)
RF(φ) // RF (I)
in D(B, gr), in which the horizontal arrows are isomorphisms. Therefore it suﬃces
to prove that the canonical morphism
(16.1.11)
⨁
x∈X
RF (Ix)→RF (I)
in D(B, gr) is an isomorphism.
Consider this commutative diagram inD(B, gr) :
⨁
x∈X F (Ix)
⨁
ηR
Ix //

⨁
x∈X RF (Ix)

F (I)
ηR
I // RF (I)
For eachx the morphismηR
Ix is an isomorphism; and hence the top horizontal arrow
is an isomorphism. BecauseF = R0F is quasi-compact, the left vertical arrow is an
isomorphism(in Cstr(B, gr), andsoalsoin D(B, gr)). ByLemma16.1.9thecomplex
I is rightF-acyclic, and thereforeηR
I is an isomorphism. Hence the remaining arrow
is an isomorphism; but this is the morphism (16.1.11). □
