---
doc_id: arxiv-1412.4229v4
doc_title: "THE SQUARING OPERATION FOR COMMUTATIVE DG RINGS AMNON YEKUTIELI"
section_id: sec-000-0-introduction
section_title: "Introduction"
section_number: 0
pages: 1-12
source_pdf: 1412.4229v4.pdf
source_sha256: 248d6a1e28a76a94
doc_brief: "THE SQUARING OPERATION FOR COMMUTATIVE DG RINGS AMNON YEKUTIELI — Let A → B be a homomorphism of commutative rings."
---
1. Some Facts on DG Rings and Modules 7
2. Resolutions of DG Modules 12
3. Central Pairs of DG Rings and their Resolutions 16
4. DG Ring Homotopies 23
5. Pairs of DG Modules, Compound Resolutions, and Rectangles 26
6. The Rectangle Operation 32
7. The Squaring Operation 38
References 43
0. Introduction
0.1. Background: Rigid Dualizing Complexes.The concept ofrigid dualizing
complex was introduced by M. Van den Bergh in his inﬂuential paper [VdB] from
1997. This was done for a noncommutative ringA over a base ﬁeldK. Let us recall
Date: 24 October 2015.
Key words and phrases. DG rings, DG modules, derived categories, derived functors,
resolutions.
Mathematics Subject Classiﬁcation2010. Primary: 16E45. Secondary: 16E35, 18G10, 13D03,
18E30.
Supported by the Israel Science Foundation grant no. 253/13.
1
arXiv:1412.4229v4  [math.KT]  24 Oct 2015
2 AMNON YEKUTIELI
the deﬁnition; but to simplify matters (and because here we are interested in the
commutative situation), we shall state it for a commutative ringA.
So letK be a ﬁeld andA a commutativeK-ring. We denote byD(A) the derived
category ofA-modules. Given a complexM∈D(A), itssquare is the complex
(0.1.1) SqA/K(M) := RHomA⊗KA(A,M⊗KM)∈D(A).
The A-module structure on SqA/K(M) comes from the ﬁrst argument ofRHom.
Note that ifM is a single module, then
Hq(
SqA/K(M)
{
= HHq(A,M⊗KM),
the q-th Hochschild cohomology of theA-bimodule M⊗KM.
Now assumeA is ﬁnitely generated overK (and hence it is noetherian). Arigid
dualizing complexoverArelative toKis a pair(R,ρ), whereR∈D(A)is a dualizing
complex (in the sense of [RD]), and
(0.1.2) ρ:R
≃
− →SqA/K(R)
is an isomorphism inD(A). Van den Bergh proved that a rigid dualizing complex
(R,ρ) exists, and it is unique up to isomorphism. Further work in this direction was
done by J.J. Zhang and the author in a series of papers; see [YZ1] and its references.
(These papers dealt with the noncommutative situation, which is signiﬁcantly more
complicated.)
In the current paper we are interested incommutative rings, but in arelative sit-
uation: instead of a base ﬁeldK, we have a homomorphismA→B of commutative
rings, and we want to produce a useful theory of squaring and rigidity.
If the homomorphismA→B is ﬂat, then there is a pretty easy way to generalize
(0.1.1), as follows. Given a complexM∈D(B), we may deﬁne
(0.1.3) SqB/A(M) := RHomB⊗AB(B,M ⊗L
AM)∈D(B).
However, whenA→B is not ﬂat, formula (0.1.3) is meaningless, since there is no
way to interpretM⊗L
AM as an object ofD(B⊗AB) !
In our paper with Zhang [YZ2], we proposed to solve the ﬂatness problem by
replacing the ringB with aﬂat DG ring resolution˜B→B overA. Further work
on rigid dualizing complexes over commutative rings was done in the paper [YZ3],
and more is outlined in the survey paper [Ye1].
There is work in progress ([Ye6] and [Ye7]) about rigid dualizing on schemes
and Deligne-Mumford stacks. Indeed, the rigid approach to Grothendieck duality
allows, for the ﬁrst time, to state and prove global duality for a proper map between
DM stacks. The ideas are outlined in the lecture notes [Ye3].
Unfortunately, there wereserious ﬂaws in the proofs in[YZ2], as explained in
Subsection 0.5 of the Introduction. The discovery of these ﬂaws forced us to go back
and repair the foundations. Thus,in the present paper we provide a comprehensive
and correct treatment of the squaring operation, using the DG ring method. The
companion paper [Ye5] is destined to repair further problems in [YZ2], and to
enhance the results of [YZ3].
Once the repairs to the foundations are done, we intend to proceed with the
geometric application of rigid dualizing complexes (namely the papers in progress
[Ye6] and [Ye7]).
0.2. DGRingsandtheirResolutions. LetA =⨁
i∈ZAi beaDGring, whereas
usual “DG” is short for “diﬀerential graded”. (Most other texts would callAa unital
associative DG algebra overZ; see Remark 1.4 for a discussion of nomenclature.)
We say thatA is nonpositive if Ai = 0 for i> 0. The DG ringA is calledstrongly
commutativeifa·b = (−1)ij·b·afora∈Ai andb∈Aj, anda·a = 0ifiis odd. We
THE SQUARING OPERATION 3
call A a commutative DG ringif it is both nonpositive and strongly commutative.
This is the term appearing in the title of the paper.
We denote byDGR≤0
sc the category of commutative DG rings. Observe that the
category of commutative rings is a full subcategory ofDGR≤0
sc , since a ring can be
seen as a DG ring concentrated in degree0. All DG rings appearing in the Intro-
duction are commutative (with the exception of Subsections 0.4 and 0.5). However,
in the paper itself we must deal with noncommutative DG rings, as explained in
Subsection 0.4.
Even though our motivation is the squaring operation for commutative rings,
we develop the squaring operation more generally for commutative DG rings, and
this is the way we shall present the results in the Introduction. The reason is
twofold: ﬁrst, there is no added diﬃculty in working with commutative DG rings
(as compared to commutative rings); and second, the presentation is cleaner when
working totally in the commutative DG framework.
Let A
u
− →B be a homomorphism of commutative DG rings, i.e. a morphism in
DGR≤0
sc . We refer to A
u
− →B as a pair of commutative DG rings, with notation
B/A. These pairs form a category: given another pair B′/A′= (A′u′
−→B′), a
morphism of pairsw/v :B′/A′→B/A is a commutative diagram
(0.2.1) A′u′
//
v

B′
w

A u //B
in DGR≤0
sc . The resulting category is denoted byPDGR≤0
sc .
Consider a pairB/A in PDGR≤0
sc . A K-ﬂat resolutionof B/A is a morphism
s/r : ˜B/ ˜A→B/A in PDGR≤0
sc , such that˜B is K-ﬂat as a DG˜A-module, r : ˜A→A
is a quasi-isomorphism, ands : ˜B→B is a surjective quasi-isomorphism. (See
Section 2 for a review of various kinds of DG module resolutions, including K-ﬂat
ones.)
(0.2.2) ˜A ˜u //
r

qu-isom
˜B
s

K-ﬂat
surj qu-isom
A u
//B
Let w/v :B′/A′→B/A be a morphism inPDGR≤0
sc . A K-ﬂat resolution ofw/v
is a commutative diagram
(0.2.3) ˜B′/ ˜A′˜w/˜v //
s′/r′

˜B/ ˜A
s/r

B′/A′w/v //B/A
in PDGR≤0
sc , where the vertical arrowss/r ands′/r′are K-ﬂat resolutions. We also
say that ˜w/˜v is a morphism of resolutions abovew/v. In caseB′/A′= B/A, and
w/v is the identity automorphism of this pair, we say that˜w/˜v is a morphism of
resolutions ofB/A. According to Proposition 7.2, K-ﬂat resolutions of pairs, and
of morphisms between pairs, exist.
4 AMNON YEKUTIELI
Let A
u
− →B
v
− →C be homomorphisms in DGR≤0
sc . We refer to this data as a
triple of commutative DG rings. A K-ﬂat resolution of this triple is a commutative
diagram
(0.2.4) ˜A ˜u //
r

˜B
s

˜v // ˜C
t

A u //B v //C
in DGR≤0
sc , such that˜B/ ˜A is a K-ﬂat resolution of the pairB/A, and ˜C/ ˜A is a K-ﬂat
resolution of the pairC/A. The ﬁrst triple above can be viewed as a morphism of
pairs v/idA : B/A→C/A; and ˜v/id ˜A : ˜B/ ˜A→˜C/ ˜A can be viewed as a K-ﬂat
resolution ofv/idA. Such resolutions exist by Proposition 7.9.
0.3. The Squaring Operation. Recall that our DG rings are all commutative.
To a DG ringA we associate the category of DGA-modules M(A), and its derived
category D(A). Thereisanadditivefunctor Q : M(A)→D(A), whichistheidentity
on objects, and which sends quasi-isomorphisms to isomorphisms. In Sections 1 and
2 we recall some facts about DG modules, their resolutions, and related derived
functors.
LetA
u
− →B be a homomorphism of DG rings, namely an objectB/A of PDGR≤0
sc .
Given a DGB-module M, and a K-ﬂat resolution˜B/ ˜A of B/A, we let
(0.3.1) Sq
˜B/ ˜A
B/A(M) := RHom ˜B⊗˜A ˜B(B,M ⊗L
˜AM)∈D(B).
In Proposition 5.15 and Deﬁnition 7.3 we provide an explicit presentation of
Sq
˜B/ ˜A
B/A(M), in terms ofcompound resolutions. See Remark 7.5 regarding symmetric
compound resolutions.
Consider a morphism of pairsw/v : B′/A′→B/A, a DG moduleM∈D(B),
a DG moduleM′∈D(B′), and a morphismθ: M→M′in D(B′). Clariﬁcation:
actually θis a morphismForw(M)→M′, where Forw : D(B)→D(B′) is the for-
getful functor (restriction of scalars) corresponding to the DG ring homomorphism
w :B′→B. However, most of the time we shall suppress these forgetful functors,
for the sake of clarity.
Given a K-ﬂat resolution˜w/˜v : ˜B′/ ˜A′→˜B/ ˜A of w/v, there is a morphism
(0.3.2) Sq ˜w/˜v
w/v(θ) : Sq
˜B/ ˜A
B/A(M)→Sq
˜B′/ ˜A′
B′/A′(M′)
in D(B′). The morphismSq ˜w/˜v
w/v(θ) is constructed using compound resolutions – see
Proposition5.16andDeﬁnition7.4. Thisconstructionisfunctorialinallarguments.
By this we mean that ifw′/v′:B′′/A′′→B′/A′is another morphism inPDGR≤0
sc ,
with K-ﬂat resolution˜w′/˜v′: ˜B′′/ ˜A′′→˜B′/ ˜A′, and ifθ′:M′→M′′is a morphism
in D(B′′), then
Sq( ˜w/˜v)◦( ˜w′/˜v′)
(w/v)◦(w′/v′)(θ′◦θ) = Sq ˜w′/˜v′
w′/v′(θ′)◦Sq ˜w/˜v
w/v(θ),
as morphisms
Sq
˜B/ ˜A
B/A(M)→Sq
˜B′′/ ˜A′′
B′′/A′′(M′′)
in D(B′′). See Proposition 5.17.
Here is the key technical result of our paper. It is repeated as Theorem 7.6 in
the body of the paper, and proved there. A brief discussion of the proof can be
found in Subsection 0.4 of the Introduction.
THE SQUARING OPERATION 5
Theorem 0.3.3(Homotopy Invariance). Letw/v :B′/A′→B/A be a morphism
in PDGR≤0
sc , let M ∈D(B), let M′∈D(B′), and let θ: M →M′be a mor-
phism in D(B′). Suppose ˜B/ ˜A and ˜B′/ ˜A′are K-ﬂat resolutions ofB/A and B′/A′
respectively inPDGR≤0
sc , and
˜w0/˜v0, ˜w1/˜v1 : ˜B′/ ˜A′→˜B/ ˜A
are morphisms of resolutions abovew/v. Then the morphisms
Sq ˜w0/˜v0
w/v (θ), Sq ˜w1/˜v1
w/v (θ) : Sq
˜B/ ˜A
B/A(M)→Sq
˜B′/ ˜A′
B′/A′(M′)
in D(B′) are equal.
Here is the ﬁrst main theorem of our paper.
Theorem0.3.4 (ExistenceofSquares) . LetA→B be a homomorphism of commu-
tative DG rings, and letM be a DGB-module. There is a DGB-module SqB/A(M),
unique up to a unique isomorphism inD(B), together with an isomorphism
sq
˜B/ ˜A : SqB/A(M)
≃
− →Sq
˜B/ ˜A
B/A(M)
in D(B) for any K-ﬂat resolution˜B/ ˜A of B/A, satisfying the following condition.
(∗) For any morphism˜w/˜v : ˜B′/ ˜A′→˜B/ ˜A of resolutions ofB/A, the diagram
SqB/A(M)
sq
˜B/ ˜A

sq
˜B′/ ˜A′
((
Sq
˜B/ ˜A
B/A(M)
Sq ˜w/˜v
id/id(idM)
// Sq
˜B′/ ˜A′
B/A (M)
of isomorphisms inD(B) is commutative.
The DG moduleSqB/A(M) is called thesquare ofM over B relative toA.
This theorem is repeated as Theorem 7.7 in the body of the paper. As we already
mentioned, this assertion (for rings only, not DG rings) appeared as [YZ2, Theorem
2.2]; but the proof there had a large gap in it. For a discussion, and a comparison
to [AILN, Theorem 3.2], see Subsection 0.5 below.
Here is the second main theorem of the paper.
Theorem 0.3.5 (Trace Functoriality). Let A→B
v
− →C be homomorphisms of
commutative DG rings, letM ∈D(B), let N ∈D(C), and letθ: N →M be a
morphism in D(B). There is a unique morphism
Sqv/idA(θ) : SqC/A(N)→SqB/A(M)
in D(B), satisfying the condition:
(∗∗) For any K-ﬂat resolution˜A→˜B
˜v
− →˜C of the triple A→B
v
− →C, the
diagram
SqC/A(N)
sq
˜C/ ˜A

Sqv/id(θ)
// SqB/A(M)
sq
˜B/ ˜A

Sq
˜C/ ˜A
C/A(N)
Sq˜v/id
v/id(θ)
// Sq
˜B/ ˜A
B/A(M)
in D(B) is commutative.
6 AMNON YEKUTIELI
This theorem is repeated as Theorem 7.10. The statement already appeared as
[YZ2, Theorem 2.3] (for rings only, not DG rings). But the proof in loc. cit. was
also incorrect.
The known functoriality of the operationSq
˜B/ ˜A
B/A (from Section 5) now implies
that the assignmentsM↦→SqB/A(M) and θ↦→SqidB/idA(θ) are a functor
SqB/A : D(B)→D(B),
called thesquaring operation overB relative toA.
The functorSqB/A is not linear; in fact it is aquadratic functor, in the following
sense. Given a morphismθ:N→M in D(B) and an elementb∈H0(B), we have
SqB/A(b·θ) =b2·SqB/A(θ),
as morphisms SqB/A(N)→SqB/A(M) in D(B). See Theorem 7.16 for a slightly
more general statement.
0.4. On the Proofs.Theorems 0.3.4 and 0.3.5 are rather easy to prove, once we
know Theorem 0.3.3 (and the existence of resolutions).
However, the proof of Theorem 0.3.3 is quite long and diﬃcult. As its name
suggests, it involves a homotopy between the homomorphisms˜w0, ˜w1 : ˜B′→˜B.
The only way we know to produce a homotopy˜w0⇒˜w1 is when the DG ring˜B′
is noncommutative semi-freeover ˜A′, and there is equality˜v0 = ˜v1. See Deﬁnition
4.1 and Theorem 4.3.
We are thus forced to deal withnoncommutative DG rings. Instead of the pairs
of commutative DG rings that were discussed above, the relevant noncommutative
object is acentral pair of DG rings, namely a central homomorphismu : A→B
with commutative sourceA. See Deﬁnitions 1.6 and 3.6.
LetB/A be a central pair of DG rings. A K-ﬂat resolution of it is a central pair
of DG rings ˜B/ ˜A, such that ˜B is a K-ﬂat DG˜A-module, together with a quasi-
isomorphism ˜B/ ˜A→B/A as in diagram (0.2.2). NowB is a DG bimodule over
˜B, namely it is a DG module over theenveloping DG ring ˜B⊗˜A ˜Bop. Because of
this, we must replace the single DG moduleM by a pair(Ml,M r), consisting of a
left DGB-module Ml and a right DGB-module Mr. In this situation, instead of
a “square” we have a “rectangle”:
(0.4.1) Rect
˜B/ ˜A
B/A(Ml,M r) := RHom ˜B⊗˜A ˜Bop(B,M l⊗L
˜AMr).
This object lives in the derived categoryD(Bce), whereBce is thecenter of B (in
the graded sense, see Deﬁnition 1.6).
In the noncommutative situation, the Homotopy Theorem (the noncommutative
version of Theorem 0.3.3) is Theorem 6.11. It is proved in two stages. First, an
important special case (˜B′/ ˜A′is noncommutative semi-free and˜v0 = ˜v1) is done in
Lemma 6.7. The proof of this lemma relies on Theorem 4.3, and uses the cylinder
DG ring. The general case is then reduced to that special case. Theorem 6.15
(Existence of Rectangles) is the noncommutative version of Theorem 0.3.4.
The rectangle operation is interesting on its own, even whenB/A is a commu-
tative pair of rings. This is due to its connection with the monoidal operation⊗!.
See Remark 6.16.
0.5. Discussion of Related Papers.Early versions of Theorems 0.3.4 and 0.3.5
had already appeared in our paper [YZ2] with Zhang, as Theorems 2.2 and 2.3
respectively. However, to our great embarrassment, the proofs of these results in
[YZ2] had severe gaps in them. The gaps are well-hidden in the text; but one clear
error is this: the homomorphism
[
φ0 0
0 φ1
]
in the middle of page 3225 (in the proof
of Theorem 2.2) does not make any sense (unlessφ0 = φ1). In order to give a
THE SQUARING OPERATION 7
correct treatment, it is necessary to work with noncommutative semi-free DG ring
resolutions, as explained in Subsection 0.4 above.
The mistake in the proof of [YZ2, Theorem 2.2] was discovered by Avramov,
Iyengar, Lipman and Nayak [AILN]. They also found a way to ﬁx it, and their
[AILN, Theorem 3.2] is a generalization of our [YZ2, Theorem 2.2]. Indeed, [AILN,
Theorem 3.2] establishes the rectangle operation in the case whenA→B is a
central pair of rings. The proof of [AILN, Theorem 3.2] relies on the Quillen model
structure on the category DGR/ceA of noncommutative DG rings, central over
a commutative base ringA, following [BP]. More on this aspect can be found in
Remark 4.6. Note that our Theorem 6.11 (the noncommutative version of Theorem
0.3.4) is stronger than [AILN, Theorem 3.2], because we allowA→B be a central
pair of nonpositive DG rings.
Our goals are diﬀerent from those of [AILN], and hence we adopt a diﬀerent
strategy. For us the relative situation of a homomorphism of commutative rings
A→B is crucial, and we must consider triples of commutative ringsA→B→C.
For this reason we stick to commutative K-ﬂat DG ring resolutions, relying on
Theorem 0.3.3. We do not know whether the methods of [AILN] can be adapted
to yield the trace functoriality of the squaring operation (Theorem 0.3.5).
Acknowledgments. I wish to thank James Zhang, Bernhard Keller, Vladimir Hinich,
Liran Shaul, Rishi Vyas, Asaf Yekutieli and Sharon Hollander for their help in
writing this paper.
1. Some F acts on DG Rings and Modules
In this section we review some known facts about DG rings and modules. We
talk about central homomorphisms of DG rings. Finally, we introduce the cylinder
construction for DG rings and modules.
A diﬀerential graded ring, orDG ringfor short, is a graded ringA =⨁
i∈ZAi,
together with an additive endomorphismdA of degree1 called thediﬀerential. The
diﬀerentialdA satisﬁesdA◦dA = 0, and it is a graded derivation ofA, namely it
satisﬁes the graded Leibniz rule
(1.1) dA(a·b) = dA(a)·b + (−1)i·a·dA(b)
for a∈Ai and b∈Aj. (Most other texts would call suchA an associative unital
DG algebra.)
Deﬁnition 1.2.We denote byDGR the category of all DG rings, where the mor-
phisms are the graded ring homomorphismsu : A→B that commute with the
diﬀerentials.
We consider rings as DG rings concentrated in degree0. Thus the category of
rings becomes a full subcategory ofDGR.
Deﬁnition 1.3.LetA be a DG ring. ADG ring overA, or aDGA-ring, is a pair
(B,u ), whereB is a DG ring andu :A→B is a DG ring homomorphism.
Suppose (B,u ) and (B′,u′) are DG rings overA. Ahomomorphism of DG rings
overA, oraDGA-ring homomorphism, isa homomorphism ofDG ringsv :B→B′
such thatu′=v◦u.
We denote byDGR/A the category of DG rings overA.
Thus DGR/A is the usual “coslice category”, except that we say “over” instead
of “under”. See Remark 1.28 regarding the direction of arrows. There is an obvious
forgetful functor DGR/A→DGR. A morphism v in DGR/A is shown in this
8 AMNON YEKUTIELI
commutative diagram:
B v //B′
A
u
OO
u′
>>
Remark 1.4. We should probably justify the use of “DG ring”, instead of the
traditional “DG algebra”. We maintain that more generally, whenever we have a
homomorphism A→B in the category of rings, thenB ought to be called an
A-ring. Below is an explanation.
Consider a commutative base ringK. Given a ring homomorphismK→A such
that the targetA is commutative, we simply say that “A is a commutativeK-ring”.
In the noncommutative context things are more delicate. When one says that “A is
a K-algebra” (associative and unital), the meaning is that the ring homomorphism
K→A is central; namely the image ofK is in the center ofA. We suggest instead
to use “A is a centralK-ring”.
In the DG context, one says that “A is a DGK-algebra” (again associative and
unital) if the image ofK lies inside the subring of degree0 central cocycles ofA.
We propose to use “central DGK-ring” instead, as in Deﬁnition 1.6 below.
Notice that the name “ring” allows us to drop the adjectives “associative” and
“unital”; and it also separates DG rings from DG Lie algebras etc.
In the present paper we actually need to consider DG ring homomorphisms
u :A→B, where the sourceA is a genuine DG ring, and in some cases it is even
noncommutative. Thusu(A) is sometimes not in the center ofB, nor in the subring
of cocycles, and we can’t say that “B is a DGA-algebra”. But we can, and do, say
that “B is a DGA-ring”. The homomorphismu might be central nonetheless, as
in Deﬁnition 1.6.
Consider a graded ringA. For homogeneous elementsa∈Ai and b∈Aj we
deﬁne the graded commutator to be
(1.5) ad(a)(b) :=a·b−(−1)ij·b·a.
This extends to alla,b∈A using bilinearity. Namely, ifa =∑
kak and b =∑
lbl,
with ak∈Aik and bl∈Ajl, then
ad(a)(b) :=
∑
k,l
ad(ak)(bl).
Often the notation[a,b ] is used for the graded commutator.
Deﬁnition 1.6.Let A be a DG ring.
(1) The center of A is the DG subring
Ace :={a∈A|ad(a)(b) = 0 for all b∈A}.
(2) The DG ringA is calledweakly commutativeifAce =A. In other words, if
a·b = (−1)ij·b·a
for alla∈Ai and b∈Aj.
(3) A homomorphismu :A→B in DGR is calledcentral if u(Ace)⊆Bce. In
this case, the resulting DG ring homomorphismAce→Bce is denoted by
uce.
(4) We denote byDGR/ceA to be the the full subcategory ofDGR/Aconsisting
of pairs (B,u ) such thatu :A→B is central.
THE SQUARING OPERATION 9
Implicit in item (1) of the deﬁnition above is the (easy to check) fact thatAce is
indeed a DG subring ofA. The DG ringAce itself is weakly commutative. As for
item (4): a morphismv : B→B′in the categoryDGR/ceA is not required to be
central; the centrality condition is only onA
u
− →B and A
u′
−→B′.
If u : A→B and v : B→C are central homomorphisms inDGR, thenv◦u :
A →C is also central. Thus we get a subcategory DGR⃗ce of DGR, consisting
of all objects, but only the central homomorphisms. Letting DGRwc be the full
subcategory of DGR on the weakly commutative DG rings, we get a functor
(−)ce : DGR⃗ce→DGRwc.
Let A be a DG ring. Recall that a left DGA-module is a left gradedA-module
M =⨁
i∈ZMi, with diﬀerentialdM of degree 1, that satisﬁesdM◦dM = 0 and
the graded Leibniz rule (equation (1.1), but withm∈Mj instead ofb). Right DG
A-modules are deﬁned similarly. By default all DG modules in this paper are left
DG modules.
Let A be a DG ring, letM and N be left DGA-modules, and letφ: M→N
be a degreek additive (i.e. Z-linear) homomorphism. We say thatφis A-linear if
(1.7) φ(a·m) = (−1)ik·a·φ(m)
for alla∈Ai and m∈Mj. (This is the sign convention of [ML].) The abelian
group ofA-linear homomorphisms of degreek is denoted by HomA(M,N )k, and
we let
(1.8) HomA(M,N ) :=
⨁
k∈Z
HomA(M,N )k.
The graded abelian groupHomA(M,N ) has a diﬀerentiald given by
(1.9) d(φ) := dN◦φ−(−1)k·φ◦dM
for φ∈HomA(M,N )k. In particular, forN =M we get a DG ring
(1.10) EndA(M) := HomA(M,M ).
Suppose A is a DG ring and M a DG abelian group (i.e. a DG Z-module).
From (1.7) we see that a DGA-module structure onM is the same as a DG ring
homomorphism A→EndZ(M).
IfM is a right DGA-module andN is a left DGA-module, then the usual tensor
product M⊗AN is a graded abelian group:
M⊗AN =
⨁
k∈Z
(M⊗AN)k,
where (M⊗AN)k is the subgroup generated by the tensorsm⊗n such thatm∈Mi
and n∈Nk−i. The graded abelian groupM⊗AN has a diﬀerentiald satisfying
(1.11) d(m⊗n) := dM(m)⊗n + (−1)i·m⊗dN(n)
for m,n as above.
Let A and B be DG rings. The tensor product A⊗Z B is a DG ring, with
multiplication
(1.12) (a1⊗b1)·(a2⊗b2) := (−1)i2j1·(a1·a2)⊗(b1·b2)
for ak∈Aik and bk∈Bjk, and with diﬀerential like in (1.11).
Let B be a DG ring. Its opposite DG ringBop is the same DG abelian group,
but we denote its elements bybop, b∈B. The multiplication inBop is
bop
1 ·bop
2 := (−1)j1j2·(b2·b1)op
for bk∈Bjk. Note that the centers satisfy(Bop)ce = (Bce)op, andBop =B iﬀB
is weakly commutative.
10 AMNON YEKUTIELI
IfM is a right DGB-module, then it can be seen as a left DGBop-module, with
action
bop·m := (−1)kj·m·b
for b ∈Bj and m ∈Mk. Because of this observation, working only with left
DG modules is not a limitation. We shall switch between notations according to
convenience.
Now consider a DGA-B-bimodule M, namelyM has a leftA action and a right
B action, and they commute, i.e.a·(m·b) = (a·m)·b. ThenM can be viewed as
a leftA⊗ZBop -module with action
(1.13) (a⊗bop)·m := (−1)kj·a·m·b
for a∈Ai, b∈Bj and m∈Mk. Thus a DGA-B-bimodule structure on a DG
abelian groupM is the same as a homomorphism of DG rings
A⊗ZBop→EndZ(M).
Let A be a weakly commutative DG ring. Any B ∈DGR/ceA is a DG A-
bimodule. IfB,C ∈DGR/ceA, then the DGA-module B⊗AC has an obvious DG
ring structure, and moreoverB⊗AC∈DGR/ceA. Given a DGB-module M and
and a DGC-module N, the tensor productM⊗AN is a DG module overB⊗AC,
with action
(b⊗c)·(m⊗n) := (−1)ij·(b·m)⊗(c·n)
for c∈Ci and m∈Mj.
Deﬁnition 1.14.LetA be a DG ring. We denote byDGModA the category of left
DGA-modules, where the morphisms are theA-linear homomorphismsφ:M→N
of degree 0 that commute with the diﬀerentials. Since the name is too long, we
mostly use the abbreviationM(A) := DGModA.
The category M(A) is abelian. The setM(A) also has a DG category structure
on it, in which the set of morphismsM→N is the DG abelian groupHomA(M,N ).
The relation between these structures is
(1.15) HomM(A)(M,N ) = Z0(
HomA(M,N )
{
,
the group of0-cocycles.
LetM =⨁
i∈Z Mi be a graded abelian group. Recall that the shift (or twist, or
translation, or suspension) ofM is the graded abelian groupT(M) =⨁
i∈Z T(M)i
deﬁned as follows. The graded component of degreei of T(M) is T(M)i :=Mi+1.
Note that as (ungraded) abelian groups we haveT(M) =M, but the gradings are
diﬀerent. Thus the identity automorphism ofM becomes a degree−1 invertible
homomorphismofgradedabeliangroups t :M→T(M). Weshallusuallyrepresent
elements of T(M)i as t(m), withm∈Mi+1.
IfM is a DGA-module, thenT(M) has the following structure of DGA-module.
The diﬀerentialdT(M) is
(1.16) dT(M)(t(m)) :=−t(dM(m)) = t(−dM(m))
for m∈Mk. The action ofA is
(1.17) a·t(m) := (−1)i·t(a·m) = t((−1)i·a·m)
for a∈Ai. If M is a DG right module, or a DG bimodule, then the structure of
T(M) is determined by (1.16), (1.17) and (1.13). Concretely,
a·t(m)·b = (−1)i·t(a·m·b)
THE SQUARING OPERATION 11
for a∈Ai, m∈Mk and b∈Aj. Note that our sign conventions for the shift are
such that the canonical bijection
T(Z)⊗ZM→T(M), t(c)⊗m↦→t(c·m) =c·t(m),
for c∈Z and m∈M, is an isomorphism of DGA-bimodules.
For anyk∈Z, thek-th power ofT is denoted byTk. There is a corresponding
degree−k homomorphism of graded abelian groups
(1.18) tk :M→Tk(M),
which is the identity on the underlying ungraded abelian group. Note that
Tl(Tk(M)) = T k+l(M), and Tk is an automorphism of the category M(A). As
usual, we writeM[k] := Tk(M).
We now recall thecone construction, as it looks using the operatort. Let A
be a DG ring, and letφ: M→N be a homomorphism inM(A). The cone ofφ
is the DGA-module Cone(φ) := N⊕M[1], whose diﬀerential, when we express
this module as the column
[N
M[1]
]
, is left multiplication by the matrix of degree1
abelian group homomorphisms
[
dN φ◦t−1
0 d M [1]
]
.
We learned the concept ofcylinder DG ring, deﬁned below, from B. Keller. It
appears (without this name) in his [Ke2].
Consider the matrix DG ring
(1.19) Cyl(Z) :=
[Z Z [−1]
0 Z
]
=
⨁[a0 b·ξ
0 a1
]⏐⏐a0,a 1,b∈Z
}
,
where the elementξ:= t−1(1)∈Z[−1] has degree 1. The multiplication is
(1.20)
[a0 b·ξ
0 a1
]
·
[a′
0 b′·ξ
0 a′
1
]
:=
[a0·a′
0 (a0·b′+b·a′
1)·ξ
0 a1·a′
1
]
where a′
0,a′
1,b′∈Z. The diﬀerential isdcyl := ad(
[0 ξ
0 0
]
), the graded commutator
with the element
[0 ξ
0 0
]
. Explicitly we have
(1.21) dcyl(
[a0 b·ξ
0 a1
]
) =
[0 ( −a0 +a1)·ξ
0 0
]
.
There are DG ring homomorphismsZ
ϵ
− →Cyl(Z)
ηi
−→Z, fori = 0, 1, with formulas
(1.22) ϵ(a) :=
[a 0
0 a
]
and ηi(
[a0 b·ξ
0 a1
]
) :=ai.
It is easy to see thatϵandηi are quasi-isomorphisms, andηi◦ϵ= idZ, the identity
automorphism of Z.
Deﬁnition 1.23.Let A be a DG ring. Thecylinder of A is the DG ring
Cyl(A) := Cyl(Z)⊗ZA∼=
[A A [−1]
0 A
]
,
with multiplication induced from (1.20), and diﬀerential induced from (1.21), using
formulas (1.12) and (1.11).
It will be convenient to denote elements ofCyl(A) as matrices
[a0 ξ·b
0 a0
]
, rather
than as tensors. Note that the elementξis central and has degree1, so b·ξ=
(−1)k·ξ·b for b∈Ak.
Proposition 1.24. LetA be a DG ring. Consider the induced DG ring homomor-
phisms A
ϵ
− →Cyl(A)
ηi
−→A.
(1) The homomorphismsϵand ηi are DG ring quasi-isomorphisms.
(2) The homomorphismsϵand ηi are central, and moreover the induced homo-
morphisms ϵce :Ace− →Cyl(A)ce and ηce
i : Cyl(A)ce→Ace are bijective.
12 AMNON YEKUTIELI
Proof. Since Cyl(Z)isafreegraded Z-module(via ϵ, andforgettingthediﬀerential),
these are direct consequences of the corresponding assertions forZ; and those are
clear. □
Deﬁnition 1.25.LetA be a DG ring andM a DGA-module. The cylinder ofM
is the DGCyl(A)-module
Cyl(M) := Cyl(Z)⊗ZM∼= Cyl(A)⊗AM∼=
[M M [−1]
0 M
]
,
with multiplication induced from (1.20), and diﬀerential induced from (1.21).
The deﬁnition above relates also to right DG modules and to bimodules, as
explained in (1.13).
Proposition 1.26.LetA be a DG ring and letM be a DGA-module. The induced
DG module homomorphismsϵ: M →Cyl(M) and ηi : Cyl(M)→M are quasi-
isomorphisms.
When considering the homomorphismϵ: M→Cyl(M), we viewCyl(M) as a
DG A-module via the DG ring homomorphismϵ: A→Cyl(A). Likewise, when
considering the homomorphismηi : Cyl(M)→M, we viewM as a DG Cyl(A)-
module via the DG ring homomorphismηi : Cyl(A)→A.
Proof. As in Proposition 1.24(1), this is immediate from the fact thatϵ: Z→
Cyl(Z) and ηi : Cyl(Z)→Z are quasi-isomorphisms. □
Thecylinderoperation(onDGringsandmodules)hasthefollowingfunctoriality.
If u : A→B is a DG ring homomorphism, then there is an induced DG ring
homomorphism Cyl(u) : Cyl(A)→Cyl(B), Cyl(u) := id Cyl(Z)⊗u. Explicitly the
formula is
(1.27) Cyl(u)(
[a0 ξ·b
0 a1
]
) =
[u(a0) ξ·u(b)
0 u(a1)
]
.
Likewise for modules.
Remark 1.28. In the abstract categorical sense, the DG ringCyl(A) plays a role
dual to that of a cylinder; so perhaps we should have called it “the path object of
A”. Indeed, this is precisely the path object described on page 503 of [ScSh].
We decided to adhere to the name “cylinder” for two reasons. First, this is the
name used in [YZ2]. The second reason is that we are dealing with rings here,
and so (as happens in algebraic geometry) arrows tend to be reversed. The same
reversal occurs in Deﬁnition 1.3: we talk about “DG rings overA”, rather than
about “DG rings underA”, as the categorical convention would dictate.
