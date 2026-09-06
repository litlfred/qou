---
doc_id: arxiv-1610.09640v4
doc_title: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI"
section_id: sec-002-02-a-motivating-discussion-duality
section_title: "A Motivating Discussion: Duality"
section_number: 0.2
pages: 9-13
source_pdf: 1610.09640v4.pdf
source_sha256: db5e7a5c5e85f95f
doc_brief: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI — This is the fourth (and last) prepublication version of a book on derived categories, that will be published by"
---
gories from another perspective, very diﬀerent from the one taken in the previous
subsection, by considering the idea ofduality in algebra.
We begin with something elementary: linear algebra. Take a ﬁeldK. Given a
K-module M (i.e. a vector space), letD(M) := Hom K(M,K), the dual module.
There is a canonical homomorphism
(0.2.1) evM :M→D(D(M)),
called Hom-evaluation, whose formula is evM(m)(φ) := φ(m) for m ∈M and
φ∈D(M). IfM is ﬁnitely generated thenevM is an isomorphism (actually this is
“if and only if”).
To formalize this situation, letModK denote the category ofK-modules. Then
D : ModK→ModK is a contravariant functor, andev : Id→D◦D is a morphism
of functors (i.e. a natural transformation). HereId is the identity functor ofModK.
Now let us replaceK by some nonzero commutative ringA. Again we can deﬁne
a contravariant functor
(0.2.2) D : ModA→ModA, D (M) := HomA(M,A ),
and a morphism of functorsev : Id →D◦D. It is easy to see thatevM : M→
D(D(M)) is an isomorphism ifM is a ﬁnitely generated freeA-module. Of course
we can’t expect reﬂexivity (i.e.evM being an isomorphism) if M is not ﬁnitely
generated; but what about a ﬁnitely generated module that is not free?
In order to understand this better, let us concentrate on the ringA =Z. Since
Z-modules are just abelian groups, the category ModZ is often denoted by Ab.
Let Abf be the full subcategory of ﬁnitely generated abelian groups. Every ﬁnitely
generated abelian group is of the formM∼=T⊕F, withT ﬁnite andF free. (The
letters “T” and “F” stand for “torsion” and “free” respectively.) It is important
to note that this isnot a canonical isomorphism. There is a canonical short exact
sequence
(0.2.3) 0→T
φ
− →M
ψ
− →F→0
9
Derived Categories | Amnon Yekutieli | 14 Apr 2019
in Abf, but the decompositionM∼=T⊕F comes fromchoosing a splittingσ:F→
M of this sequence.
Exercise 0.2.4. Prove that the exact sequence (0.2.3) is functorial; namely there
are functors T,F : Abf →Abf, and natural transformations φ: T →Id and
ψ: Id→F, such that for eachM∈Abf the groupT (M) is ﬁnite, the groupF (M)
is free, and the sequence of homomorphisms
(0.2.5) 0→T (M)
φM
−−→M
ψM
−−→F (M)→0
is exact.
Next, prove that there does not exist afunctorial decomposition of a ﬁnitely
generated abelian group into a free part and a ﬁnite part. Namely, there is no
natural transformation σ: F →Id, such that for everyM the homomorphism
σM :F (M)→M splits the sequence (0.2.5). (Hint: ﬁnd a counterexample.)
We know that for a free ﬁnitely generated abelian groupF there is reﬂexivity,
i.e. evF : F →D(D(F )) is an isomorphism. But for a ﬁnite abelian groupT we
haveD(T ) = HomZ(T,Z) = 0. Thus, for a groupM∈Abf with a nonzero torsion
subgroup T, reﬂexivity fails:evM :M→D(D(M)) is not an isomorphism.
On the other hand, for an abelian groupM we can deﬁne another sort of dual:
D′(M) := Hom Z(M,Q/Z). There is a morphism of functors ev′: Id →D′◦
D′. For a ﬁnite abelian groupT the homomorphism ev′
T : T →D′(D′(T )) is an
isomorphism; this can be seen by decomposingT into cyclic groups, and for a ﬁnite
cyclic group it is clear. SoD′is a duality for ﬁnite abelian groups. (We may view
the abelian groupQ/Z as the group of roots of1 inC, via the exponential function;
and thenD′becomes Pontryagin Duality.)
But for a ﬁnitely generated free abelian groupF we getD′(D′(F )) = ˆF, the
proﬁnite completion ofF. So once more this is not a good duality for all ﬁnitely
generated abelian groups.
This is where thederived categoryenters. For every commutative ringA there is
the derived categoryD(ModA). Here is a very quick explanation of it, in concrete
terms – as opposed to the abstract point of view taken in the previous subsection.
Recall that acomplex of A-modules is a diagram
(0.2.6) M =
(
···→M−1 d−1
M
−−→M0 d0
M
−−→M1→···
{
in the categoryModA. Namely theMi areA-modules, and thedi
M are homomor-
phisms. The condition is thatdi+1
M ◦di
M = 0. We sometimes writeM ={Mi}i∈Z.
The collection dM ={di
M}i∈Z is called thediﬀerentialof M.
Given a second complex
N =
(
···→N−1 d−1
N
−−→N0 d0
N
−−→N1→···
{
,
a homomorphism of complexesφ: M →N is a collectionφ={φi}i∈Z of homo-
morphisms φi :Mi→Ni in ModA satisfying φi+1◦di
M = di
N◦φi. The resulting
category is denoted byC(ModA).
The i-th cohomologyof the complexM is
(0.2.7) Hi(M ) := Ker(di
M)/ Im(di−1
M )∈ModA.
A homomorphism φ: M →N in C(ModA) induces homomorphisms Hi(φ) :
Hi(M )→Hi(N ) in ModA. We call φa quasi-isomorphism if all the homomor-
phisms Hi(φ) are isomorphisms.
The derived category D(ModA) is the localization of C(ModA) with respect
to the quasi-isomorphisms. This means that D(ModA) has the same objects as
10
Derived Categories | Amnon Yekutieli | 14 Apr 2019
C(ModA). There is a functor
(0.2.8) Q : C(ModA)→D(ModA)
which is the identity on objects, it sends quasi-isomorphisms to isomorphisms, and
it is universal for this property.
A singleA-module M0 can be viewed as a complexM concentrated in degree0:
M =
(
···→0
0
− →M0 0
− →0→···
{
.
This turns out to be a fully faithful embedding
(0.2.9) ModA→D(ModA).
The essential image of this embedding is the full subcategory ofD(ModA) on the
complexes M whose cohomology is concentrated in degree0. In this way we have
enlarged the category ofA-modules. All this is explained in Sections 6-7 of the
book.
Here is a very important kind of quasi-isomorphism. SupposeM is anA-module
and
(0.2.10) ···→P−2 d−2
P
−−→P−1 d−1
P
−−→P 0 ρ
− →M→0
is a projective resolution of it. We can viewM as a complex concentrated in degree
0, by the embedding (0.2.9). Deﬁne the complex
(0.2.11) P :=
(
···→P−2 d−2
P
−−→P−1 d−1
P
−−→P 0→0→···
{
,
concentrated in nonpositive degrees. Then ρbecomes a morphism of complexes
ρ: P →M. The exactness of the sequence (0.2.10) says that ρis actually a
quasi-isomorphism. Thus Q(ρ) :P→M is an isomorphism inD(ModA).
Let us ﬁx a complexR∈C(ModA). For every complexM∈C(ModA) we can
form the complex
D(M) := HomA(M,R )∈C(ModA).
This is the usual Hom complex (we recall it in Subsection 3.6). AsM changes we
get a contravariant functor
D : C(ModA)→C(ModA).
The functorD has acontravariant right derived functor
(0.2.12) RD : D(ModA)→D(ModA).
If P is a bounded above complex of projective modules (like in formula (0.2.11)),
or more generally a K-projective complex (see Subsection 10.2), then there is a
canonical isomorphism
(0.2.13) RD(P )∼=D(P ) = HomA(P,R ).
Every complexM admits a K-projective resolutionρ: P →M, and this allows
us to calculate RD(M). Indeed, because the morphism Q(ρ) : P →M is an
isomorphism in D(ModA), it follows that RD(Q(ρ)) : R D(M)→RD(P ) is an
isomorphism in D(ModA). And the complex RD(P ) is known by the canonical
isomorphism (0.2.13). All this is explained in Sections 8, 10 and 11 of the book.
It turns out that there is a canonical morphism
(0.2.14) evR : Id→RD◦RD
of functors fromD(ModA) to itself, calledderived Hom-evaluation. See Subsection
13.1.
11
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Let us now return to the ringA =Z and the complexR =Z. So the functorD
is the same one we had in (0.2.2). Given a ﬁnitely generated abelian groupM, we
want to calculate the complexesRD(M) and RD(RD(M)), and the morphism
(0.2.15) evR
M :M→RD(RD(M))
in D(ModA). As explained above, for this we choose a projective resolutionρ:
P→M, and then we calculate the complexesRD(P ) and RD(RD(P )), and the
morphism evR
P. For convenience we choose a projective resolutionP of this shape:
P =
(
···→0→P−1 d−1
P
−−→P 0→0→···
{
=
(
···→0− →Zr1 a·(−)
−−−−→Zr0− →0···
{
,
where r0,r 1∈N anda is a matrix of integers. The complexRD(P ) is this:
RD(P )∼=D(P ) = HomZ(P,Z) =
(
···→0− →Zr0 at·(−)
−−−−→Zr1− →0···
{
,
a complex of free modules concentrated in degrees 0 and 1, with the transpose
matrixat as its diﬀerential.
Because RD(P )∼=D(P ) is itself a bounded complex of free modules, its derived
dual is
(0.2.16) RD(RD(P ))∼=D(D(P )) = HomZ
(
HomZ(P,Z),Z
{
.
Under the isomorphism (0.2.16), the derived Hom-evaluation morphismevR
P in this
case is just the naive Hom-evaluation homomorphism evP : P →D(D(P )) in
C(ModZ) from (0.2.1); see Exercise 13.1.17. BecauseP 0 and P−1 are ﬁnite rank
free modules, it follows thatevP is an isomorphism in C(ModZ). Therefore the
morphism evR
M in D(ModZ) is an isomorphism. We see thatRD is a duality that
holds for all ﬁnitely generatedZ-modulesM !
Actually, much more is true. Let us denote byDf(ModZ) the full subcategory of
D(ModZ) on the complexesM such thatHi(M) is ﬁnitely generated for alli. Then,
according to Theorem 13.1.18,evR
M is an isomorphism for everyM∈Df(ModZ).
It follows that
(0.2.17) RD : Df(ModZ)→Df(ModZ)
is a duality (a contravariant equivalence). This is the celebrated Grothendieck
Duality.
Here is the connection between the derived dualityRD and the classical dualities
D and D′. Take a ﬁnitely generated abelian groupM, with short exact sequence
(0.2.3). There are canonical isomorphisms
H0(RD(M))∼= Ext0
Z(M,Z)∼= HomZ(M,Z)∼= HomZ(F,Z) =D(F )
and
H1(RD(M))∼= Ext1
Z(M,Z)∼= Ext1
Z(T,Z)∼=D′(T ).
The cohomologies Hi(RD(M)) vanish for i⁄= 0, 1. We see that if M is neither
free nor ﬁnite, thenH0(RD(M)) and H1(RD(M)) are both nonzero; so that the
complex RD(M) is not isomorphic inD(ModZ) to an object ofModZ, under the
embedding (0.2.9).
Grothendieck Duality holds for many noetherian commutative ringsA. A suﬃ-
cient condition is thatA is a ﬁnitely generated ring over a regular noetherian ring
K (e.g.K =Z or a ﬁeld). A complexR∈D(ModA) for which the contravariant
functor
(0.2.18) RD = RHomA(−,R ) : Df(ModA)→Df(ModA)
12
Derived Categories | Amnon Yekutieli | 14 Apr 2019
is an equivalence is called adualizing complex. (This is not quite accurate – see
Deﬁnition 13.1.9 for the precise technical conditions onR.) A dualizing complex
R over A is unique (up to a degree translation and tensoring with an invertible
module). See Theorems 13.1.18, 13.1.34 and 13.1.35.
Interestingly, the structure of the dualizing complexR depends on the geometry
of the ringA (i.e. of the aﬃne schemeSpec(A)). IfA is a regular ring (likeZ) then
R =A is dualizing. IfA is a Cohen-Macaulay ring (andSpec(A) is connected) then
R is a singleA-module (up to a shift in degrees). But ifA is a more singular ring,
then R must live in several degrees, as the next example shows.
Example 0.2.19.Consider the aﬃne algebraic varietyX⊆A3
R which is the union
of a plane and a line that meet at a point, with coordinate ring
A =R[t1,t 2,t 3]/(t3·t1, t3·t2).
See ﬁgure 1. A dualizing complexR over A must live in two adjacent degrees;
namely there is some i such that both Hi(R) and Hi+1(R) are nonzero. This
calculation is worked out in full in Example 13.3.12.
Figure 1. An algebraic variety X that is connected but not
equidimensional, and hence not Cohen-Macaulay.
One can also talk about dualizing complexes overnoncommutative rings. We
will do this in Sections 17 and 18.
